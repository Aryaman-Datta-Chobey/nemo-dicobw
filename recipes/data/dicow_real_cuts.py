#!/usr/bin/env python
"""Lhotse manifests of the real far-field train corpora for the open DiCoW recipe (EXPERIMENTS.md 20261031-dicow-open-prep).

Writes under <out>/<corpus>/:
  <corpus>_cutset_train.jsonl.gz      one cut per session x far-field channel, all supervisions (SE-DiCoW's parent cutset)
  <corpus>_cutset_train_30s.jsonl.gz  the same sessions in windows of at most 30 s, same windows on every channel
  <corpus>_cutset_train.stats.json    hours, windows, speakers per window, tightening and window-cut counts

Every channel is its own recording, so uniform sampling over cuts picks a random channel per sample. Text is the
re-punctuated `punct` field of recipes/data/punctuate_transcripts.py.

Speakers: AliMeeting and AISHELL-5 ids are global. AISHELL-4 labels repeat across sessions (14 labels over 191 sessions),
so they are scoped by session here; do not read them as global speaker identities.

Masks: where the close-talk MFA pass of recipes/data/dicow_seed_mfa.py covers a segment and its words reproduce the text
exactly, the segment becomes one supervision per word run (split at silences > --run-gap, text split at the matching
character). Other segments stay as annotated, and all of AISHELL-4 (no close-talk audio). The STNO mask is built from
these supervisions, so this is what keeps it tight.

Windows: a window ends at the latest silence within 30 s. A chain of overlapping speech longer than 30 s has no such
point: the window ends where the fewest runs are crossed, and crossed runs move whole to the next window, which starts
at the earliest of them. Their tail stays in this window's audio unlabelled; the stats count these runs.

    python recipes/data/dicow_real_cuts.py --jobs 4                # dicow env
    python recipes/data/dicow_real_cuts.py --corpus aishell5 --limit 2 --out <scratch>   # trial
"""
from __future__ import annotations

import argparse
import bisect
import json
import re
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import soundfile as sf
from lhotse import CutSet, Recording, SupervisionSegment
from lhotse.audio import AudioSource
from lhotse.cut import MonoCut

DATA = Path("/mnt/data")
WORK = DATA / "work/dicow_open"
KEEP = re.compile(r"[0-9a-z㐀-鿿]")
TG_ITEM = re.compile(r'xmin = ([\d.]+)\s*\n\s*xmax = ([\d.]+)\s*\n\s*text = "(.*)"')


def norm(text: str) -> str:
    return "".join(KEEP.findall(text.lower()))


def tier_words(path: Path) -> list[tuple[float, float, str]]:
    """Non-empty intervals of the `words` tier of a long-format TextGrid."""
    body = path.read_text(encoding="utf-8").split('name = "phones"')[0]
    return [(float(a), float(b), t) for a, b, t in TG_ITEM.findall(body) if t.strip()]


def split_text(punct: str, counts: list[int]) -> list[str]:
    """Split text after the n-th kept character of each part; following punctuation stays with the earlier part."""
    parts, cur, seen, i = [], "", 0, 0
    for ch in punct:
        if i < len(counts) - 1 and seen == counts[i] and KEEP.match(ch.lower()):
            parts.append(cur.strip())
            cur, seen, i = "", 0, i + 1
        cur += ch
        seen += bool(KEEP.match(ch.lower()))
    parts.append(cur.strip())
    return parts


def runs_of(seg: dict, words: list[tuple[float, float, str]], gap: float) -> list[dict] | None:
    """Word runs of a segment, or None when the words don't reproduce its text."""
    if not words or norm("".join(w[2] for w in words)) != norm(seg["punct"]):
        return None
    groups = [[words[0]]]
    for w in words[1:]:
        if w[0] - groups[-1][-1][1] > gap:
            groups.append([])
        groups[-1].append(w)
    texts = split_text(seg["punct"], [len(norm("".join(w[2] for w in g))) for g in groups])
    if len(texts) != len(groups):
        return None
    return [{"start": g[0][0], "end": g[-1][1], "speaker": seg["speaker"], "text": t} for g, t in zip(groups, texts)]


def tighten(segs: list[dict], aligned: dict[tuple[str, str], list], key_to_file: dict, gap: float, n: Counter) -> list[dict]:
    """Assign each aligned word to the nearest segment of its file, then replace segments by their word runs."""
    by_file = defaultdict(list)
    for i, s in enumerate(segs):
        f = key_to_file.get(s["speaker"])
        if f is not None:
            by_file[f].append(i)
    words_of = defaultdict(list)
    for f, idx in by_file.items():
        idx.sort(key=lambda i: segs[i]["start"])
        starts = [segs[i]["start"] for i in idx]
        for w in aligned.get(f, []):
            mid = (w[0] + w[1]) / 2
            p = bisect.bisect_right(starts, mid)
            cand = [idx[j] for j in (p - 1, p) if 0 <= j < len(idx)]
            words_of[min(cand, key=lambda i: max(segs[i]["start"] - mid, mid - segs[i]["end"], 0))].append(w)
    out = []
    for i, s in enumerate(segs):
        runs = runs_of(s, sorted(words_of.get(i, [])), gap)
        n["segments"] += 1
        n["speech_annotated"] += s["end"] - s["start"]
        if runs is None:
            n["segments_as_annotated"] += 1
            runs = [{k: s[k] for k in ("start", "end", "speaker")} | {"text": s["punct"]}]
        n["speech_kept"] += sum(r["end"] - r["start"] for r in runs)
        out += runs
    return sorted(out, key=lambda r: (r["start"], r["end"]))


def windows(sups: list[dict], total: float, maxlen: float, n: Counter) -> list[tuple[float, float, list[dict]]]:
    """Partition supervisions into windows; every supervision lands whole in exactly one window."""
    out, todo = [], sorted(sups, key=lambda s: s["start"])
    while todo:
        t0 = max(todo[0]["start"] - 0.1, 0.0)
        limit = min(t0 + maxlen, total)
        inside = [s for s in todo if s["start"] < limit]
        crossing = [s for s in inside if s["end"] > limit]
        if not crossing:
            cut = limit
        else:
            # latest silence: a candidate end that no run crosses
            cands = sorted({s["end"] for s in inside if s["end"] <= limit}, reverse=True)
            clean = [c for c in cands if not any(s["start"] < c < s["end"] for s in inside)]
            if clean:
                cut = clean[0]
            elif cands:
                cut = min(cands, key=lambda c: (sum(s["start"] < c < s["end"] for s in inside), -c))
            else:  # one run longer than the window
                n["runs_dropped_too_long"] += 1
                n["speech_dropped_too_long"] += todo[0]["end"] - todo[0]["start"]
                todo = todo[1:]
                continue
        keep = [s for s in inside if s["end"] <= cut]
        moved = [s for s in inside if s["end"] > cut and s["start"] < cut]
        n["runs_moved"] += len(moved)
        kept_ids = {id(s) for s in keep}
        todo = [s for s in todo if id(s) not in kept_ids]
        out.append((t0, cut - t0, keep))
    return out


def supervisions(cut_id: str, rec: str, t0: float, sups: list[dict]) -> list[SupervisionSegment]:
    return [SupervisionSegment(id=f"{cut_id}-{i}", recording_id=rec, start=round(s["start"] - t0, 3), duration=round(s["end"] - s["start"], 3),
                               channel=0, text=s["text"], speaker=s["speaker"], language="zh") for i, s in enumerate(sups)]


def session_job(job: dict) -> tuple[list[dict], list[dict], Counter]:
    n: Counter = Counter()
    aligned = {f: tier_words(p) for f, p in job["aligned"].items()}
    sups = tighten(job["segs"], aligned, job["key_to_file"], job["run_gap"], n)
    full, wins = [], []
    win_list = None
    for ch in sorted(job["channels"]):
        info = sf.info(ch)
        if info.samplerate != 16000 or info.channels != 1:
            raise ValueError(f"{ch}: {info.samplerate} Hz, {info.channels} channels")
        rec = Recording(id=f"{job['session']}__{Path(ch).stem}", sources=[AudioSource(type="file", channels=[0], source=ch)],
                        sampling_rate=16000, num_samples=info.frames, duration=info.frames / 16000)
        inside = [s for s in sups if s["end"] <= rec.duration]
        n["runs_past_end"] += len(sups) - len(inside)
        full.append(MonoCut(id=rec.id, start=0, duration=rec.duration, channel=0, recording=rec,
                            supervisions=supervisions(rec.id, rec.id, 0.0, inside)).to_dict())
        if win_list is None:
            win_list = windows(inside, rec.duration, job["maxlen"], n)
            n["hours"] += sum(w[1] for w in win_list) / 3600
            n["windows"] += len(win_list)
            for w in win_list:
                n[f"spk_{len({s['speaker'] for s in w[2]})}"] += 1
        for k, (t0, dur, keep) in enumerate(win_list):
            cid = f"{rec.id}-w{k:04d}"
            wins.append(MonoCut(id=cid, start=round(t0, 3), duration=round(min(dur, rec.duration - t0), 3), channel=0, recording=rec,
                                supervisions=supervisions(cid, rec.id, round(t0, 3), keep)).to_dict())
    n["sessions"] += 1
    n["channels"] += len(job["channels"])
    return full, wins, n


def load_text(corpus: str) -> list[dict]:
    with open(WORK / "text" / f"{corpus}.jsonl", encoding="utf-8") as f:
        return [json.loads(x) for x in f]


def jobs_for(corpus: str, args) -> list[dict]:
    rows = load_text(corpus)
    mfa = WORK / "mfa"
    if corpus == "alimeeting":
        rows = [r for r in rows if r["tier_source"] == "far"]
        audio = {p.parent.name: p.parent for p in (DATA / "audio16k/alimeeting/Train_Ali").glob("*/far_ch1.flac")}
        pattern = "far_ch*.flac"
    elif corpus == "aishell4":
        audio = {p.parent.name: p.parent for sp in ("train_L", "train_M", "train_S") for p in (DATA / "audio16k/aishell4" / sp).glob("*/far_ch1.flac")}
        pattern = "far_ch*.flac"
        for r in rows:
            r["speaker"] = f"aishell4_{r['session']}_{r['speaker']}"
    elif corpus == "aishell5":
        audio = {p.parent.name: p.parent for p in (DATA / "audio16k/aishell5/train").glob("*/DX01C01.flac")}
        pattern = "DX0[1-4]C01.flac"  # DX05/DX06 (191 sessions) have no TextGrid and are about 25 dB quieter than DX01-04
        rows = [r for r in rows if r["tier_source"].startswith("DX")]
        for r in rows:
            r["speaker"] = f"aishell5_{r['speaker']}"
    else:
        raise ValueError(corpus)

    utt: dict = defaultdict(dict)
    if corpus != "aishell4":
        with open(mfa / f"utterances_{corpus}.json", encoding="utf-8") as f:
            ulist = json.load(f)
        if corpus == "alimeeting":
            for r in rows:  # far tiers read <session>_<gender>_SPK####; the SPK id is global
                r["speaker"] = f"alimeeting_{r['speaker'].rsplit('_', 1)[-1]}"
        for u in ulist:
            utt[u["session"]][u["speaker"]] = u["file"]  # far and close-talk times can differ; runs_of checks the text

    segs = defaultdict(list)
    for r in rows:
        if norm(r["clean"]) and r["end"] > r["start"]:
            segs[r["session"]].append({k: r[k] for k in ("start", "end", "speaker", "punct")})
    missing = sorted(set(segs) - set(audio))
    if missing:
        raise FileNotFoundError(f"{corpus}: no audio for {len(missing)} sessions, e.g. {missing[:3]}")
    jobs = []
    for sess in sorted(segs)[: args.limit or None]:
        keys = utt.get(sess, {})
        aligned = {}
        if corpus != "aishell4":
            for f in set(keys.values()):
                for sub in (corpus, "topup_zh"):
                    p = mfa / "aligned" / sub / f"{sess}__{f}.TextGrid"
                    if p.exists():
                        aligned.setdefault(f, p)
        jobs.append({"session": sess, "segs": segs[sess], "channels": [str(p) for p in sorted(audio[sess].glob(pattern))], "aligned": aligned,
                     "key_to_file": keys, "run_gap": args.run_gap, "maxlen": args.maxlen})
    return jobs


def build(corpus: str, args) -> dict:
    out = args.out / corpus
    out.mkdir(parents=True, exist_ok=True)
    full, wins, n = [], [], Counter()
    with ProcessPoolExecutor(args.jobs) as ex:
        for k, (a, b, c) in enumerate(ex.map(session_job, jobs_for(corpus, args))):
            full += a
            wins += b
            n.update(c)
            if k % 25 == 0:
                print(f"{corpus}: session {k}", flush=True)
    speakers = len({s["speaker"] for c in full for s in c["supervisions"]})  # from_dicts consumes the dicts
    max_window = max(c["duration"] for c in wins)
    n_full, n_wins = len(full), len(wins)
    CutSet.from_dicts(full).to_file(out / f"{corpus}_cutset_train.jsonl.gz")
    CutSet.from_dicts(wins).to_file(out / f"{corpus}_cutset_train_30s.jsonl.gz")
    stats = {"corpus": corpus, "cuts_full": n_full, "cuts_30s": n_wins, "speakers": speakers,
             "max_window_s": max_window, "run_gap_s": args.run_gap, **{k: round(v, 3) for k, v in sorted(n.items())},
             "speech_kept_over_annotated": round(n["speech_kept"] / n["speech_annotated"], 3),
             "segments_as_annotated_share": round(n["segments_as_annotated"] / n["segments"], 3)}
    (out / f"{corpus}_cutset_train.stats.json").write_text(json.dumps(stats, indent=1))
    print(json.dumps(stats), flush=True)
    return stats


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--corpus", nargs="+", default=["aishell5", "aishell4", "alimeeting"])
    ap.add_argument("--out", type=Path, default=DATA / "manifests/lhotse")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--limit", type=int, default=0, help="first N sessions only (trial)")
    ap.add_argument("--run-gap", type=float, default=0.3)
    ap.add_argument("--maxlen", type=float, default=30.0)
    args = ap.parse_args()
    for c in args.corpus:
        build(c, args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
