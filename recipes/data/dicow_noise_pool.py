#!/usr/bin/env python
"""Noise pool of the open DiCoW recipe (EXPERIMENTS.md 20261101-dicow-open-train-setup), for upstream's `musan_root`.

Upstream picks one .wav uniformly and reads the whole file on every use. MUSAN noise files are small, so they are linked.
AISHELL-5 noise files last 30-75 min, which is too slow to read per sample, so --per-file random 32 s chunks of each go in as
16-bit WAV. Chunk count is what sets the MUSAN : AISHELL-5 share, because the choice is per file. AISHELL-5 noise is in-car,
so it is kept at about half. All-zero files are left out: upstream divides by the peak.

    python recipes/data/dicow_noise_pool.py        # dicow env
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

import numpy as np
import soundfile as sf

DATA = Path("/mnt/data")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=DATA / "noise/dicow_open")
    ap.add_argument("--per-file", type=int, default=3)
    ap.add_argument("--chunk", type=float, default=32.0)
    ap.add_argument("--seed", type=int, default=2027)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    n = {"musan": 0, "musan_silent": 0, "aishell5": 0, "aishell5_silent": 0}
    (args.out / "musan").mkdir(parents=True, exist_ok=True)
    (args.out / "aishell5").mkdir(parents=True, exist_ok=True)
    for f in sorted((DATA / "corpora/musan/musan/noise").rglob("*.wav")):
        if np.abs(sf.read(f, dtype="float32")[0]).max() == 0:
            n["musan_silent"] += 1
            continue
        link = args.out / "musan" / f.name
        if not link.exists():
            link.symlink_to(f)
        n["musan"] += 1
    for f in sorted((DATA / "corpora/aishell5/noise").rglob("*.wav")):
        info = sf.info(f)
        for i in range(args.per_file):
            start = rng.randrange(int(info.frames - args.chunk * info.samplerate))
            x, sr = sf.read(f, start=start, frames=int(args.chunk * info.samplerate), dtype="int16")
            if np.abs(x).max() == 0:
                n["aishell5_silent"] += 1
                continue
            sf.write(args.out / "aishell5" / f"{f.parent.name}_{f.stem}_{i}.wav", x, sr, subtype="PCM_16")
            n["aishell5"] += 1
    (args.out / "stats.json").write_text(json.dumps({**n, **vars(args), "out": str(args.out)}, indent=1) + "\n")
    print(n)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
