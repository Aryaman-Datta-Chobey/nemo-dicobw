#!/usr/bin/env python
"""AISHELL-3 as a source of single-speaker Mandarin voices for FastMSS simulated mixtures.

  mfa-corpus  per split, <work>/corpus/<split>/<speaker>/<utt>.{flac,lab}: symlink to the 16 kHz FLAC
              (audio16k/aishell3/<split>/<speaker>/<utt>.flac) and the transcript as space-separated Mandarin
              dictionary words (characters from content.txt; segmentation as recipes/data/mfa_zh.py).
  cuts        after `mfa align` into <work>/aligned/<split>/: a lhotse CutSet per split with one supervision per
              utterance (speaker, gender from spk-info.txt, text) and MFA word alignments, written to
              <manifest-dir>/aishell3_cutset_<split>.jsonl.gz (FastMSS `manifest_prefix: aishell3`,
              `dset_splits: [cutset_train]`). Utterances MFA could not align are dropped and counted.
  chunk       split every utterance at word boundaries into phrase-length cuts whose target durations are drawn
              from the conversational segments under --seg-refs (RTTM directory; --exclude drops sessions): read
              sentences are longer than conversational segments. The cut boundary is the middle of the inter-word gap; tails
              shorter than --min-chunk join the previous chunk. Word times stay in the recording frame (FastMSS's
              own pause split expects that). Written as <manifest-dir>/aishell3chunk_cutset_<split>.jsonl.gz
              (FastMSS `manifest_prefix: aishell3chunk`).

    python recipes/data/aishell3_prepare.py mfa-corpus                       # dicow env
    mfa align <work>/corpus/train mandarin_china_mfa.dict mandarin_mfa.zip <work>/aligned/train \\
        --g2p_model_path mandarin_china_mfa.zip \\
        --config_path recipes/data/mfa_simple_tokenization.yaml -j 6 --clean --output_format long_textgrid
    python recipes/data/aishell3_prepare.py cuts                             # dicow env
    python recipes/data/aishell3_prepare.py chunk                            # dicow env

The paper's speaker split is kept: train = 174 speakers (simulation voices), test = 44 (simulated sanity set).
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mfa_zh import DICT, mfa_text  # noqa: E402

DATA = Path("/mnt/data")
SPLITS = ("train", "test")


def corpus_root(src: Path) -> Path:
    return src / "data_aishell3" if (src / "data_aishell3").is_dir() else src


def transcripts(src: Path, split: str) -> dict[str, str]:
    """content.txt: '<utt>.wav<TAB>字 pin1 字 pin2 ...' -> {utt: characters}."""
    out = {}
    for line in (corpus_root(src) / split / "content.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        name, _, rest = line.partition("\t")
        toks = rest.split()
        out[Path(name).stem] = "".join(toks[0::2])
    return out


def speaker_info(src: Path) -> dict[str, dict[str, str]]:
    """spk-info.txt: '<speaker><TAB><age group><TAB><gender><TAB><accent>' after '#' comment lines."""
    info = {}
    for line in (corpus_root(src) / "spk-info.txt").read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or not line.strip():
            continue
        spk, age, gender, accent = line.split()[:4]
        info[spk] = {"age_group": age, "gender": gender, "accent": accent}
    return info


def mfa_corpus(args) -> None:
    dic = {ln.split()[0] for ln in DICT.read_text(encoding="utf-8").splitlines() if ln.strip()}
    max_len = max(map(len, dic))
    for split in SPLITS:
        text = transcripts(args.src, split)
        n = Counter()
        for flac in sorted((args.audio / split).glob("*/*.flac")):
            spk, utt = flac.parent.name, flac.stem
            t = mfa_text(text.get(utt, ""), dic, max_len)
            if t is None:
                n["no_text"] += 1
                continue
            d = args.work / "corpus" / split / spk
            d.mkdir(parents=True, exist_ok=True)
            link = d / f"{utt}.flac"
            if not link.exists():
                link.symlink_to(flac)
            (d / f"{utt}.lab").write_text(t + "\n", encoding="utf-8")
            n["sent"] += 1
        print(f"{split}: {dict(n)} ({len(text)} transcripts)", flush=True)


def _cut(job: tuple[str, str, str, dict, str]):
    from lhotse import Recording, SupervisionSegment
    from lhotse.supervision import AlignmentItem
    import textgrid as tg

    flac, tgp, spk, info, text = job
    utt = Path(flac).stem
    tgp = Path(tgp)
    if not tgp.exists():
        return None
    tier = next(t for t in tg.TextGrid.fromFile(str(tgp)).tiers if t.name == "words")
    words = [AlignmentItem(symbol=i.mark.strip(), start=round(float(i.minTime), 3),
                           duration=round(float(i.maxTime) - float(i.minTime), 3))
             for i in tier if i.mark and i.mark.strip() and i.mark.strip() != "<eps>"]
    if not words:
        return None
    rec = Recording.from_file(flac, recording_id=utt)
    sup = SupervisionSegment(id=utt, recording_id=utt, start=0.0, duration=rec.duration, channel=0, text=text,
                             language="zh", speaker=spk, gender=info.get("gender"),
                             custom={k: v for k, v in info.items() if k != "gender"}, alignment={"word": words})
    return rec, sup


def cuts(args) -> None:
    from lhotse import CutSet, RecordingSet, SupervisionSet

    info = speaker_info(args.src)
    args.manifest_dir.mkdir(parents=True, exist_ok=True)
    for split in SPLITS:
        text = transcripts(args.src, split)
        jobs = [(str(link.resolve()), str(args.work / "aligned" / split / link.parent.name / f"{link.stem}.TextGrid"),
                 link.parent.name, info.get(link.parent.name, {}), text.get(link.stem, ""))
                for link in sorted((args.work / "corpus" / split).glob("*/*.flac"))]
        with ProcessPoolExecutor(args.jobs) as ex:
            res = list(ex.map(_cut, jobs, chunksize=256))
        ok = [r for r in res if r]
        cs = CutSet.from_manifests(recordings=RecordingSet.from_recordings(r for r, _ in ok),
                                   supervisions=SupervisionSet.from_segments(s for _, s in ok))
        out = args.manifest_dir / f"aishell3_cutset_{split}.jsonl.gz"
        cs.to_file(out)
        spk = {s.speaker for _, s in ok}
        g = Counter(info.get(s, {}).get("gender") for s in spk)
        hours = sum(s.duration for _, s in ok) / 3600
        stats = {"split": split, "utterances": len(jobs), "aligned": len(ok), "dropped": len(jobs) - len(ok),
                 "speakers": len(spk), "gender": dict(g), "hours": round(hours, 2)}
        (args.manifest_dir / f"aishell3_cutset_{split}.stats.json").write_text(json.dumps(stats, indent=1) + "\n")
        print(stats, flush=True)


def segment_durations(refs: Path, exclude: list[str]) -> list[float]:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
    from nemo_dicobw.rttm import load_rttm

    out = []
    for p in sorted(refs.glob("*.rttm")):
        for sess, turns in load_rttm([p]).items():
            if sess not in exclude:
                out += [t.end - t.start for t in turns]
    return out


def chunk_cut(cut, rng, durs: list[float], min_chunk: float, pad: float = 0.1) -> list:
    from lhotse import MonoCut, SupervisionSegment

    sup = cut.supervisions[0]
    words = sorted(sup.alignment["word"], key=lambda w: w.start)
    rec_end = cut.start + cut.duration
    bounds = [max(cut.start, words[0].start - pad)]
    groups, cur = [], []
    target = rng.choice(durs)
    for i, w in enumerate(words):
        cur.append(w)
        if i + 1 < len(words) and w.end - bounds[-1] >= target:
            groups.append(cur)
            cur = []
            bounds.append((w.end + words[i + 1].start) / 2)
            target = rng.choice(durs)
    end = min(rec_end, words[-1].end + pad)
    if groups and end - bounds[-1] < min_chunk:
        groups[-1] += cur
        bounds.pop()
    else:
        groups.append(cur)
    bounds.append(end)
    out = []
    for k, ws in enumerate(groups):
        s, e = bounds[k], bounds[k + 1]
        cs = SupervisionSegment(id=f"{sup.id}_{k:02d}", recording_id=sup.recording_id, start=0.0,
                                duration=round(e - s, 3), channel=0, text="".join(w.symbol for w in ws),
                                language=sup.language, speaker=sup.speaker, gender=sup.gender, custom=sup.custom,
                                alignment={"word": ws})
        out.append(MonoCut(id=f"{cut.id}_{k:02d}", start=round(s, 3), duration=round(e - s, 3), channel=0,
                           recording=cut.recording, supervisions=[cs]))
    return out


def chunk(args) -> None:
    import random

    from lhotse import CutSet

    if args.seg_refs is None:
        raise SystemExit("chunk needs --seg-refs")
    durs = segment_durations(args.seg_refs, args.exclude)
    durs.sort()
    print(f"Reference segments: {len(durs)}, median {durs[len(durs) // 2]:.2f} s", flush=True)
    rng = random.Random(args.seed)
    for split in SPLITS:
        src = CutSet.from_file(args.manifest_dir / f"aishell3_cutset_{split}.jsonl.gz")
        cuts = [c for cut in src for c in chunk_cut(cut, rng, durs, args.min_chunk)]
        out = args.manifest_dir / f"aishell3chunk_cutset_{split}.jsonl.gz"
        CutSet.from_cuts(cuts).to_file(out)
        d = sorted(c.duration for c in cuts)
        stats = {"split": split, "utterances": len(src), "chunks": len(cuts), "median_s": d[len(d) // 2],
                 "p90_s": d[int(0.9 * len(d))], "hours": round(sum(d) / 3600, 2)}
        (args.manifest_dir / f"aishell3chunk_cutset_{split}.stats.json").write_text(json.dumps(stats, indent=1) + "\n")
        print(stats, flush=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", choices=["mfa-corpus", "cuts", "chunk"])
    ap.add_argument("--src", type=Path, default=DATA / "corpora/aishell3")
    ap.add_argument("--audio", type=Path, default=DATA / "audio16k/aishell3")
    ap.add_argument("--work", type=Path, default=DATA / "work/aishell3_mfa")
    ap.add_argument("--manifest-dir", type=Path, default=DATA / "manifests/lhotse/aishell3")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--seg-refs", type=Path)
    ap.add_argument("--exclude", nargs="*", default=[])
    ap.add_argument("--min-chunk", type=float, default=0.3)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    {"mfa-corpus": mfa_corpus, "cuts": cuts, "chunk": chunk}[args.stage](args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
