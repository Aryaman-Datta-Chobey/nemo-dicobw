#!/usr/bin/env python
"""Seed voices for the open DiCoW simulations (EXPERIMENTS.md 20261031-dicow-open-prep), as one FastMSS source CutSet.

Writes <out>/dicow_seeds_cutset_train.jsonl.gz (FastMSS `manifest_prefix: dicow_seeds`, `dset_splits: [cutset_train]`)
and a .stats.json with hours, speakers and drop counts per corpus. One speaker per cut, word alignments in the recording
frame, globally unique speaker ids. Open data only.

  alimeeting  Train_Ali near-field, per annotated utterance
  aishell5    train close-talk (DA*), per annotated utterance
  ascend      train clips. Clips MFA could not align (mixed Han + Latin) keep their span as one "word", so the code-switching
              ones stay in; FastMSS cannot split them at pauses
  aishell3    train, re-chunked at word boundaries to phrase lengths drawn from AliMeeting and AISHELL-4 train supervisions
              (recipes/data/dicow_real_cuts.py), not from challenge data

FastMSS rebuilds text from the word symbols when it splits at pauses, so each word symbol carries the punctuation that
follows it; the text must then be re-joined downstream (recipes/data/sim_dicow_open.py). An utterance whose words do not
reproduce its text is dropped and counted, except that AliMeeting's Latin-only utterances also keep their span: their
alignments were stretched into the padding.

    python recipes/data/dicow_seed_cuts.py --jobs 6     # dicow env
"""
from __future__ import annotations

import argparse
import bisect
import json
import random
import sys
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import soundfile as sf
from lhotse import CutSet, Recording, SupervisionSegment
from lhotse.audio import AudioSource
from lhotse.cut import MonoCut
from lhotse.supervision import AlignmentItem

sys.path.insert(0, str(Path(__file__).resolve().parent))
from aishell3_prepare import chunk_cut  # noqa: E402
from dicow_real_cuts import KEEP, WORK, norm, tier_words  # noqa: E402

DATA = Path("/mnt/data")
MFA = WORK / "mfa"
PAD = 0.1


def attach(words: list[tuple[float, float, str]], punct: str) -> list[tuple[float, float, str]] | None:
    """Give every word the punctuation that follows it; None when the words don't reproduce the text."""
    if not words or norm("".join(w[2] for w in words)) != norm(punct):
        return None
    out, i, text = [], 0, punct.strip()
    for k, (a, b, w) in enumerate(words):
        need, s = len(norm(w)), ""
        while i < len(text) and need > 0:  # the word's own characters, with any punctuation before them
            need -= bool(KEEP.match(text[i].lower()))
            s += text[i]
            i += 1
        while i < len(text) and not KEEP.match(text[i].lower()):  # what follows, up to the next word
            s += text[i]
            i += 1
        out.append((a, b, s.strip()))
    return out


def recording(path: str, rec_id: str) -> Recording:
    info = sf.info(path)
    if info.samplerate != 16000 or info.channels != 1:
        raise ValueError(f"{path}: {info.samplerate} Hz, {info.channels} channels")
    return Recording(id=rec_id, sources=[AudioSource(type="file", channels=[0], source=path)], sampling_rate=16000,
                     num_samples=info.frames, duration=info.frames / 16000)


def make_cut(rec: Recording, cid: str, spk: str, text: str, words: list[tuple[float, float, str]], s: float, e: float) -> MonoCut:
    s, e = round(max(s, 0.0), 3), round(min(e, rec.duration), 3)
    items = [AlignmentItem(symbol=w, start=round(a, 3), duration=round(b - a, 3)) for a, b, w in words]
    sup = SupervisionSegment(id=cid, recording_id=rec.id, start=0.0, duration=round(e - s, 3), channel=0, text=text, language="zh",
                             speaker=spk, alignment={"word": items})
    return MonoCut(id=cid, start=s, duration=round(e - s, 3), channel=0, recording=rec, supervisions=[sup])


def session_file_job(job: dict) -> tuple[list[MonoCut], Counter]:
    """One close-talk file: assign words to the nearest utterance, then one cut per utterance."""
    n: Counter = Counter()
    rec = recording(job["audio"], f"{job['corpus']}_{job['session']}__{job['file']}")
    utts = sorted(job["utts"], key=lambda u: u["start"])
    starts = [u["start"] for u in utts]
    words_of = defaultdict(list)
    for p in job["grids"]:
        for w in tier_words(Path(p)):
            mid = (w[0] + w[1]) / 2
            j = bisect.bisect_right(starts, mid)
            cand = [x for x in (j - 1, j) if 0 <= x < len(utts)]
            words_of[min(cand, key=lambda x: max(utts[x]["start"] - mid, mid - utts[x]["end"], 0))].append(w)
    cuts = []
    for i, u in enumerate(utts):
        if u["end"] > rec.duration or not norm(u["clean"]):
            n["dropped"] += 1
            continue
        cid = f"{rec.id}-{i:05d}"
        if u.get("topup") == "en":
            cuts.append(make_cut(rec, cid, u["speaker"], u["punct"].strip(), [(u["start"], u["end"], u["punct"].strip())], u["start"], u["end"]))
            n["kept_span"] += 1
            continue
        words = attach(sorted(words_of.get(i, [])), u["punct"])
        if words is None:
            n["dropped"] += 1
            continue
        cuts.append(make_cut(rec, cid, u["speaker"], u["punct"].strip(), words, words[0][0] - PAD, words[-1][1] + PAD))
    return cuts, n


def ascend_job(u: dict) -> tuple[list[MonoCut], Counter]:
    n: Counter = Counter()
    if not norm(u["clean"]):
        n["dropped"] += 1
        return [], n
    rec = recording(u["audio"], f"ascend_{u['file']}")
    text = u["punct"].strip()
    words = None
    for sub in ("ascend", "topup_en"):
        p = MFA / "aligned" / sub / u["speaker"] / f"{u['file']}.TextGrid"
        if p.exists():
            words = attach(tier_words(p), text)
            break
    if words is None:
        n["kept_span"] += 1
        return [make_cut(rec, rec.id, u["speaker"], text, [(0.0, rec.duration, text)], 0.0, rec.duration)], n
    return [make_cut(rec, rec.id, u["speaker"], text, words, words[0][0] - PAD, words[-1][1] + PAD)], n


def real_durations(manifests: Path) -> list[float]:
    durs: list[float] = []
    for c in ("alimeeting", "aishell4"):
        for cut in CutSet.from_file(manifests / c / f"{c}_cutset_train.jsonl.gz"):
            if cut.recording_id.endswith("__far_ch1"):
                durs += [s.duration for s in cut.supervisions]
    return sorted(durs)


def aishell3(manifests: Path, seed: int) -> tuple[list[MonoCut], Counter]:
    n: Counter = Counter()
    with open(WORK / "text/aishell3.jsonl", encoding="utf-8") as f:
        punct = {r["session"]: r["punct"] for r in map(json.loads, f)}
    durs = real_durations(manifests)
    print(f"chunk targets: {len(durs)} supervisions, median {durs[len(durs) // 2]:.2f} s", flush=True)
    rng = random.Random(seed)
    out = []
    for cut in CutSet.from_file(manifests / "aishell3/aishell3_cutset_train.jsonl.gz"):
        sup = cut.supervisions[0]
        ws = sorted(sup.alignment["word"], key=lambda w: w.start)
        words = attach([(w.start, w.end, w.symbol) for w in ws], punct.get(sup.recording_id, ""))
        if words is None:
            n["dropped"] += 1
            continue
        c = make_cut(cut.recording, cut.id, f"aishell3_{sup.speaker}", punct[sup.recording_id].strip(), words, cut.start, cut.start + cut.duration)
        out += chunk_cut(c, rng, durs, 0.5)
    return out, n


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--manifests", type=Path, default=DATA / "manifests/lhotse")
    ap.add_argument("--out", type=Path, default=DATA / "manifests/lhotse/dicow_open")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--limit", type=int, default=0, help="first N files / clips per corpus (trial)")
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    with open(MFA / "utterances_topup.json", encoding="utf-8") as f:
        topup = {(u["session"], u["file"], u.get("start"), u.get("end")): u["topup"] for u in json.load(f)}
    jobs = []
    for corpus, audio in (("alimeeting", "audio16k/alimeeting/Train_Ali"), ("aishell5", "audio16k/aishell5/train")):
        with open(MFA / f"utterances_{corpus}.json", encoding="utf-8") as f:
            groups = defaultdict(list)
            for u in json.load(f):
                u["topup"] = topup.get((u["session"], u["file"], u["start"], u["end"]))
                groups[(u["session"], u["file"])].append(u)
        keys = sorted(groups)[: args.limit or None]
        for sess, file in keys:
            grids = [MFA / "aligned" / sub / f"{sess}__{file}.TextGrid" for sub in (corpus, "topup_zh")]
            jobs.append({"corpus": corpus, "session": sess, "file": file, "utts": groups[(sess, file)], "audio": str(DATA / audio / sess / f"{file}.flac"),
                         "grids": [str(p) for p in grids if p.exists()]})
    with open(MFA / "utterances_ascend.json", encoding="utf-8") as f:
        ascend = json.load(f)[: args.limit or None]

    cuts: list[MonoCut] = []
    per: dict[str, Counter] = defaultdict(Counter)

    def add(corpus: str, res: list[MonoCut], n: Counter) -> None:
        cuts.extend(res)
        per[corpus].update(n)
        per[corpus]["cuts"] += len(res)
        per[corpus]["hours"] += sum(c.duration for c in res) / 3600

    with ProcessPoolExecutor(args.jobs) as ex:
        for job, (res, n) in zip(jobs, ex.map(session_file_job, jobs, chunksize=8)):
            add(job["corpus"], res, n)
        print("session corpora done", flush=True)
        for res, n in ex.map(ascend_job, ascend, chunksize=64):
            add("ascend", res, n)
    print("ascend done", flush=True)
    res, n = aishell3(args.manifests, args.seed)
    add("aishell3", res[: args.limit or None], n)

    speakers: dict[str, set] = defaultdict(set)
    for c in cuts:
        speakers[c.supervisions[0].speaker.split("_")[0]].add(c.supervisions[0].speaker)
    CutSet.from_cuts(cuts).to_file(args.out / "dicow_seeds_cutset_train.jsonl.gz")
    stats = {k: {"speakers": len(speakers[k]), **{a: round(b, 2) for a, b in sorted(v.items())}} for k, v in per.items()}
    (args.out / "dicow_seeds_cutset_train.stats.json").write_text(json.dumps(stats, indent=1) + "\n")
    print(json.dumps(stats), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
