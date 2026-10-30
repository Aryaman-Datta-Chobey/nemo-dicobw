#!/usr/bin/env python
"""Forced-alignment (fa) reference for EAR-1 train/dev from the headset audio, with Montreal Forced Aligner.

The organiser references (A/P*.TextGrid) mark whole utterances, so pauses inside an utterance count as
speech. This builds a word-tight reference in the convention of the AliMeeting forced-alignment RTTMs
(nttcslab-sp/diar-forced-alignment: Mandarin MFA acoustic v3.0.0, mandarin_china_mfa dictionary and G2P
v3.0.0; their turns merge words across gaps < 0.2 s, the smallest same-speaker gap in those RTTMs).

  prepare  per (session, participant), under <work>/corpus/<split>/:
               <session>__<P>.flac      symlink to audio16k/ear1/<split>/<session>/<P>.flac (headset)
               <session>__<P>.TextGrid  one tier "<session>__<P>": each annotated utterance, padded by up
                                        to --pad s (at most half-way to the neighbouring utterances), with its text
           Text: NFKC, punctuation and bracketed tags removed, Han runs split into dictionary words by
           forward maximum matching (single characters otherwise; the G2P covers OOVs). Utterances with
           Latin letters or digits are not sent to MFA (the Mandarin dictionary and G2P cannot pronounce
           them) and keep their annotated interval. <work>/utterances_<split>.json lists every utterance.
  build    after `mfa align` into <work>/aligned/<split>/: per utterance, the MFA words inside its window
           (words longer than --max-word s are cut to that length around their centre); an utterance MFA
           left empty, or not sent, keeps its annotated interval. Words of a speaker are merged across gaps
           < --merge-gap s -> refs/ear1/<split>/rttm/fa/<session>.rttm (+ fa_stats.json).

    python recipes/data/ear1_mfa.py prepare                      # dicow env
    mfa align <work>/corpus/train mandarin_china_mfa.dict mandarin_mfa.zip <work>/aligned/train \
        --g2p_model_path mandarin_china_mfa.zip \
        --config_path recipes/data/mfa_simple_tokenization.yaml -j 6 --clean --output_format long_textgrid
    python recipes/data/ear1_mfa.py build
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

import soundfile as sf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from egocom_mfa import textgrid  # noqa: E402

from nemo_dicobw.rttm import Turn, merge_intervals, write_rttm

DATA = Path("/mnt/data")
DICT = DATA / "mfa/pretrained_models/dictionary/mandarin_china_mfa.dict"
HAN = re.compile(r"[㐀-䶿一-鿿豈-﫿]+")
TAG = re.compile(r"\[[^\]]*\]|<[^>]*>|\([^)]*\)")


def words_of(dic: set[str], run: str, max_len: int) -> list[str]:
    out, i = [], 0
    while i < len(run):
        for n in range(min(max_len, len(run) - i), 0, -1):
            if n == 1 or run[i:i + n] in dic:
                out.append(run[i:i + n])
                i += n
                break
    return out


def mfa_text(text: str, dic: set[str], max_len: int) -> str | None:
    """Space-separated dictionary words, or None when the utterance has Latin letters or digits."""
    t = TAG.sub(" ", unicodedata.normalize("NFKC", text))
    t = "".join(" " if unicodedata.category(c)[0] in "PSZ" else c for c in t)
    if re.search(r"[A-Za-z0-9]", t):
        return None
    out = [w for run in HAN.findall(t) for w in words_of(dic, run, max_len)]
    return " ".join(out) or None


def tiers(path: Path) -> list[tuple[float, float, str]]:
    import textgrid as tg

    tier = tg.TextGrid.fromFile(str(path)).tiers[0]
    return [(float(i.minTime), float(i.maxTime), i.mark.strip()) for i in tier if i.mark and i.mark.strip()]


def prepare(args) -> None:
    dic = {ln.split("\t", 1)[0] for ln in DICT.read_text().splitlines() if ln.strip()}
    max_len = 4
    for split in ("train", "dev"):
        corpus = args.work / "corpus" / split
        corpus.mkdir(parents=True, exist_ok=True)
        utts, stats = [], defaultdict(int)
        for sess_dir in sorted((args.data / "audio16k/ear1" / split).iterdir()):
            sess = sess_dir.name
            for tg_path in sorted((args.data / "corpora/ear1/TrainDev" / sess / "A").glob("P*.TextGrid")):
                spk, audio = tg_path.stem, sess_dir / f"{tg_path.stem}.flac"
                if not audio.exists():
                    stats["speakers_without_audio"] += 1
                    continue
                dur = sf.info(str(audio)).duration
                segs = sorted(tiers(tg_path))
                intervals = []
                for i, (s, e, text) in enumerate(segs):
                    lo = max(0.0, s - args.pad, (segs[i - 1][1] + s) / 2 if i else 0.0)
                    hi = min(dur, e + args.pad, (e + segs[i + 1][0]) / 2 if i + 1 < len(segs) else dur)
                    t = mfa_text(text, dic, max_len)
                    stats["utterances"] += 1
                    stats["sent" if t else "not_sent"] += 1
                    if t and lo < hi:
                        intervals.append((round(lo, 3), round(hi, 3), t))
                    utts.append({"session": sess, "speaker": spk, "start": s, "end": e, "win": [lo, hi], "sent": bool(t)})
                stem = f"{sess}__{spk}"
                link = corpus / f"{stem}.flac"
                if link.is_symlink() or link.exists():
                    link.unlink()
                link.symlink_to(audio)
                textgrid(corpus / f"{stem}.TextGrid", stem, round(dur, 3), intervals)
        (args.work / f"utterances_{split}.json").write_text(json.dumps(utts) + "\n")
        print(f"{split}: {dict(stats)}")


def build(args) -> None:
    import textgrid as tg

    for split in ("train", "dev"):
        utts = json.loads((args.work / f"utterances_{split}.json").read_text())
        mfa: dict[tuple[str, str], list[tuple[float, float]]] = {}
        for p in sorted((args.work / "aligned" / split).glob("*.TextGrid")):
            sess, _, spk = p.stem.rpartition("__")
            tier = next(t for t in tg.TextGrid.fromFile(str(p)).tiers if t.name == "words")
            mfa[(sess, spk)] = [(float(i.minTime), float(i.maxTime)) for i in tier
                                if i.mark and i.mark.strip() and i.mark.strip() != "<eps>"]
        per: dict[str, dict[str, list[tuple[float, float]]]] = defaultdict(lambda: defaultdict(list))
        stats = defaultdict(float)
        for u in utts:
            lo, hi = u["win"]
            got = [(a, b) for a, b in mfa.get((u["session"], u["speaker"]), []) if lo <= (a + b) / 2 < hi] if u["sent"] else []
            stats["annotated_s"] += u["end"] - u["start"]
            if not got:
                stats["fallback_" + ("unaligned" if u["sent"] else "not_sent")] += 1
                per[u["session"]][u["speaker"]].append((u["start"], u["end"]))
                continue
            stats["aligned"] += 1
            for a, b in got:
                if b - a > args.max_word:
                    m = (a + b) / 2
                    a, b = m - args.max_word / 2, m + args.max_word / 2
                    stats["words_cut"] += 1
                per[u["session"]][u["speaker"]].append((a, b))
                stats["words"] += 1
        out = args.data / "refs/ear1" / split / "rttm/fa"
        out.mkdir(parents=True, exist_ok=True)
        for sess, spks in per.items():
            turns = []
            for spk, iv in spks.items():
                merged = merge_intervals(iv, gap=args.merge_gap - 1e-6)  # join gaps strictly below merge_gap
                turns += [Turn(spk, a, b) for a, b in merged]
                stats["fa_s"] += sum(b - a for a, b in merged)
            write_rttm({sess: sorted(turns, key=lambda t: t.start)}, out / f"{sess}.rttm")
        stats["fa_over_annotated"] = stats["fa_s"] / stats["annotated_s"]
        (out / "fa_stats.json").write_text(json.dumps({"merge_gap": args.merge_gap, "max_word": args.max_word,
                                                       "pad": args.pad, **stats}, indent=1) + "\n")
        print(f"{split}: {dict(stats)}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", choices=["prepare", "build"])
    ap.add_argument("--data", type=Path, default=DATA)
    ap.add_argument("--work", type=Path, default=DATA / "work/ear1_mfa")
    ap.add_argument("--pad", type=float, default=0.5)
    ap.add_argument("--merge-gap", type=float, default=0.2)
    ap.add_argument("--max-word", type=float, default=2.0)
    args = ap.parse_args()
    prepare(args) if args.stage == "prepare" else build(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
