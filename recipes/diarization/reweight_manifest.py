#!/usr/bin/env python
"""Repeat lines of a Nemotron fine-tuning manifest to shift the speaker-count prior of the training samples.

The training sampler draws one subsegment per manifest line, so repeating a line raises the share of its
recording's windows. EAR-1 lines (corpus ear1_*) with <= --max-spk speakers are repeated --ear1-mult times;
rehearsal lines (every other corpus) --rehearsal-mult times, to keep the rehearsal share of samples near the
source manifest's. heldout_*.jsonl, val.json and musan_noise.json are copied unchanged.

    python recipes/diarization/reweight_manifest.py --src $DATA/manifests/nemotron_ft/ear1_v1 \\
        --dst $DATA/manifests/nemotron_ft/ear1_v1_rw4 --max-spk 4 --ear1-mult 4 --rehearsal-mult 2
"""
from __future__ import annotations

import argparse
import json
import shutil
from collections import Counter
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", type=Path, required=True)
    ap.add_argument("--dst", type=Path, required=True)
    ap.add_argument("--max-spk", type=int, default=4)
    ap.add_argument("--ear1-mult", type=int, default=4)
    ap.add_argument("--rehearsal-mult", type=int, default=2)
    args = ap.parse_args()
    args.dst.mkdir(parents=True, exist_ok=True)
    rows = [json.loads(x) for x in (args.src / "train.json").read_text().splitlines() if x.strip()]
    out = []
    for r in rows:
        if not r["corpus"].startswith("ear1_"):
            k = args.rehearsal_mult
        else:
            k = args.ear1_mult if r["num_speakers"] <= args.max_spk else 1
        out += [r] * k
    (args.dst / "train.json").write_text("".join(json.dumps(r) + "\n" for r in out))
    for f in args.src.iterdir():
        if f.name != "train.json":
            shutil.copy2(f, args.dst / f.name)
    reh = lambda rs: sum(not r["corpus"].startswith("ear1_") for r in rs) / len(rs)
    le = lambda rs: sum(r["corpus"].startswith("ear1_") and r["num_speakers"] <= args.max_spk for r in rs) / sum(
        r["corpus"].startswith("ear1_") for r in rs)
    print(f"lines {len(rows)} -> {len(out)}; rehearsal share {reh(rows):.3f} -> {reh(out):.3f}; "
          f"EAR-1 lines with <= {args.max_spk} speakers {le(rows):.3f} -> {le(out):.3f}")
    print("speakers per line:", dict(sorted(Counter(r["num_speakers"] for r in out).items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
