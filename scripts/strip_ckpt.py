#!/usr/bin/env python
"""Drop optimizer state from Lightning training checkpoints in place, keeping weights and metadata.

Inference (recipes/diarization/nemotron_infer.py) and weight analyses (eval/drift_diag.py) read only
"state_dict"; optimizer state is needed only to resume a run exactly. Each file is rewritten to a
temporary file next to it, reloaded and checked (same state_dict keys, bit-identical tensors, every
other key kept), and only then atomically replaces the original. Files without optimizer state are skipped.

    python scripts/strip_ckpt.py --log results/disk_cleanup/strip_ckpt.tsv /mnt/data/exp/nemotron/<run>/**/*.ckpt
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path

import torch

DROP = ("optimizer_states",)


def strip(path: Path) -> tuple[str, int, int]:
    before = path.stat().st_size
    ckpt = torch.load(path, map_location="cpu", weights_only=False)
    if not any(k in ckpt for k in DROP):
        return "skip", before, before
    slim = {k: v for k, v in ckpt.items() if k not in DROP}
    tmp = path.with_name(path.name + ".strip.tmp")
    torch.save(slim, tmp)
    back = torch.load(tmp, map_location="cpu", weights_only=False)
    ref = ckpt["state_dict"]
    ok = (set(back) == set(slim) and list(back["state_dict"]) == list(ref)
          and all(back["state_dict"][k].dtype == ref[k].dtype and torch.equal(back["state_dict"][k], ref[k]) for k in ref))
    if not ok:
        tmp.unlink()
        raise RuntimeError(f"verification failed for {path}; original kept")
    os.replace(tmp, path)
    return "stripped", before, path.stat().st_size


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ckpts", type=Path, nargs="+")
    ap.add_argument("--log", type=Path, required=True, help="TSV: path, status, bytes before, bytes after")
    args = ap.parse_args()
    args.log.parent.mkdir(parents=True, exist_ok=True)
    freed = 0
    with args.log.open("a") as log:
        for p in args.ckpts:
            status, b, a = strip(p)
            freed += b - a
            log.write(f"{p}\t{status}\t{b}\t{a}\n")
            log.flush()
            print(f"{status}\t{b / 2**20:.0f} -> {a / 2**20:.0f} MB\t{p}", flush=True)
    print(f"freed {freed / 2**30:.1f} GB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
