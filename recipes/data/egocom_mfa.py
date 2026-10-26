#!/usr/bin/env python
"""Prepare EgoCom test/val for Montreal Forced Aligner (forced-alignment reference labels).

Each speaker is aligned on their own head-worn microphone (wearer person_N is transcript speaker
N); a speaker without a recording falls back to the first available wearer. Per (conversation
part, speaker) this writes, under <work>/corpus/<split>/:
    <session>__spk<N>.flac      symlink to /mnt/data/audio16k/egocom/<split>/<session>/person_<M>.flac
    <session>__spk<N>.TextGrid  one tier "<session>__spk<N>" (MFA speaker id): utterance windows + text
and <work>/utterances_<split>.json with every window and its words in order as [start, end, in_text]
(transcript or interpolated times; in_text = sent to MFA), which build_refs.py uses to check and
patch the alignment.

Utterances group consecutive words of a speaker (in transcript order) until a gap of more than
--split-gap seconds or a length of --max-len seconds. Word times come from build_refs.egocom_words
(transcript timestamps, untimed words interpolated). Windows are padded by up to --pad seconds,
without overlapping the speaker's neighbouring windows. Annotation tags and numerals are left out
of the text (the dictionary and G2P cannot pronounce them).

Example (dicow env):
    python recipes/data/egocom_mfa.py --work /mnt/data/work/egocom_mfa
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import soundfile as sf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_refs import egocom_words  # noqa: E402


def textgrid(path: Path, tier: str, dur: float, intervals: list[tuple[float, float, str]]) -> None:
    """Long-format Praat TextGrid with one IntervalTier; gaps are filled with empty intervals."""
    full, t = [], 0.0
    for s, e, txt in intervals:
        if s > t:
            full.append((t, s, ""))
        full.append((s, e, txt))
        t = e
    if t < dur:
        full.append((t, dur, ""))
    lines = ['File type = "ooTextFile"', 'Object class = "TextGrid"', "", "xmin = 0", f"xmax = {dur}",
             "tiers? <exists>", "size = 1", "item []:", "    item [1]:", '        class = "IntervalTier"',
             f'        name = "{tier}"', "        xmin = 0", f"        xmax = {dur}",
             f"        intervals: size = {len(full)}"]
    for i, (s, e, txt) in enumerate(full, 1):
        txt = txt.replace('"', '""')
        lines += [f"        intervals [{i}]:", f"            xmin = {s:.3f}", f"            xmax = {e:.3f}",
                  f'            text = "{txt}"']
    path.write_text("\n".join(lines) + "\n")


def mfa_text(w: dict) -> str | None:
    if w["tag"] or not re.search(r"[a-z]", w["text"]):
        return None
    return re.sub(r"[^a-z']", "", w["text"]) or None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", type=Path, default=Path("/mnt/data"))
    ap.add_argument("--work", type=Path, default=Path("/mnt/data/work/egocom_mfa"))
    ap.add_argument("--split-gap", type=float, default=1.5)
    ap.add_argument("--max-len", type=float, default=20.0)
    ap.add_argument("--pad", type=float, default=1.0)
    args = ap.parse_args()

    ann = args.data / "corpora" / "egocom" / "annotations"
    by_conv: dict[str, list[dict]] = defaultdict(list)
    with open(ann / "ground_truth_transcriptions.csv") as f:
        for r in csv.DictReader(f):
            by_conv[r["conversation_id"]].append(r)

    for split in ("test", "val"):
        corpus = args.work / "corpus" / split
        corpus.mkdir(parents=True, exist_ok=True)
        utts_out, stats = [], defaultdict(int)
        for sess_dir in sorted((args.data / "audio16k" / "egocom" / split).iterdir()):
            sess = sess_dir.name
            wearers = sorted(p.stem for p in sess_dir.glob("person_*.flac"))
            dur = min(sf.info(str(sess_dir / f"{w}.flac")).duration for w in wearers)
            per_spk: dict[str, list[dict]] = defaultdict(list)
            for w in egocom_words(by_conv[sess], stats):
                per_spk[w["spk"]].append(w)
            for spk, words in sorted(per_spk.items()):
                own = f"person_{spk}"
                mic = own if own in wearers else wearers[0]
                stats["speakers_on_own_mic" if mic == own else "speakers_on_other_mic"] += 1
                groups: list[list[dict]] = []
                for w in sorted(words, key=lambda w: w["s"]):
                    if groups and w["s"] - groups[-1][-1]["e"] <= args.split_gap \
                            and w["e"] - groups[-1][0]["s"] <= args.max_len:
                        groups[-1].append(w)
                    else:
                        groups.append([w])
                spans = [(g[0]["s"], max(x["e"] for x in g)) for g in groups]
                intervals, utts = [], []
                for i, (g, (s, e)) in enumerate(zip(groups, spans)):
                    lo = max(0.0, s - args.pad, (spans[i - 1][1] + s) / 2 if i else 0.0)
                    hi = min(dur, e + args.pad, (e + spans[i + 1][0]) / 2 if i + 1 < len(spans) else dur)
                    text = " ".join(t for t in map(mfa_text, g) if t)
                    if lo < hi:
                        if text:
                            intervals.append((lo, hi, text))
                        utts.append({"session": sess, "speaker": f"spk{spk}", "mic": mic, "start": round(lo, 3),
                                     "end": round(hi, 3), "text": text, "aligned_by_mfa": bool(text),
                                     "words": [(round(x["s"], 3), round(x["e"], 3), mfa_text(x) is not None)
                                               for x in g]})
                stem = f"{sess}__spk{spk}"
                link = corpus / f"{stem}.flac"
                if link.is_symlink() or link.exists():
                    link.unlink()
                link.symlink_to(sess_dir / f"{mic}.flac")
                textgrid(corpus / f"{stem}.TextGrid", stem, round(dur, 3), intervals)  # tier = MFA speaker id
                utts_out += utts
                stats["utterances"] += len(utts)
        (args.work / f"utterances_{split}.json").write_text(json.dumps(utts_out) + "\n")
        print(f"{split}: {dict(stats)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
