#!/usr/bin/env python
"""Build SegLST transcript references for the Mandarin evaluation sets.

Output: <refs>/<corpus>/<split>/seglst/<session>.json, a meeteval SegLST list of
    {"session_id", "speaker", "start_time", "end_time", "words"}
with the raw transcript text in "words" (scoring normalises both sides with
nemo_dicobw.txt_norm_zh). Speaker labels equal the RTTM reference labels (TextGrid tier names).

| corpus     | splits              | source |
|------------|---------------------|--------|
| alimeeting | Eval_Ali, Test_Ali  | <split>/<split>_far/textgrid_dir/<session>.TextGrid |
| aishell4   | test                | test/TextGrid/<session>.TextGrid |
| aishell5   | Dev, Eval1, Eval2   | <split>/<session>/DX01C01.TextGrid (far-field timeline; DX01-04 identical) |

Example (dicow env, which has `textgrid`):
    python recipes/data/build_seglst.py
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DATA = Path("/mnt/data")


def textgrid_segments(path: Path, session: str) -> list[dict]:
    import textgrid

    out = []
    for tier in textgrid.TextGrid.fromFile(str(path)).tiers:
        for iv in tier:
            if iv.mark and iv.mark.strip() and iv.maxTime > iv.minTime:
                out.append({"session_id": session, "speaker": tier.name, "start_time": round(float(iv.minTime), 3),
                            "end_time": round(float(iv.maxTime), 3), "words": iv.mark.strip()})
    return sorted(out, key=lambda s: (s["start_time"], s["end_time"], s["speaker"]))


def sources(corpora: Path) -> dict[tuple[str, str], dict[str, Path]]:
    src: dict[tuple[str, str], dict[str, Path]] = {}
    for split in ("Eval_Ali", "Test_Ali"):
        src[("alimeeting", split)] = {p.stem: p for p in sorted((corpora / "alimeeting" / split / f"{split}_far" / "textgrid_dir").glob("*.TextGrid"))}
    src[("aishell4", "test")] = {p.stem: p for p in sorted((corpora / "aishell4" / "test" / "TextGrid").glob("*.TextGrid"))}
    for split in ("Dev", "Eval1", "Eval2"):
        src[("aishell5", split)] = {p.parent.name: p for p in sorted((corpora / "aishell5" / split).glob("*/DX01C01.TextGrid"))}
    return src


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", type=Path, default=DATA)
    args = ap.parse_args()
    for (corpus, split), sessions in sources(args.data / "corpora").items():
        out = args.data / "refs" / corpus / split / "seglst"
        out.mkdir(parents=True, exist_ok=True)
        n_seg = 0
        for sess, tg in sessions.items():
            segs = textgrid_segments(tg, sess)
            (out / f"{sess}.json").write_text(json.dumps(segs, ensure_ascii=False, indent=0) + "\n")
            n_seg += len(segs)
        print(f"{corpus}/{split}: {len(sessions)} sessions, {n_seg} segments -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
