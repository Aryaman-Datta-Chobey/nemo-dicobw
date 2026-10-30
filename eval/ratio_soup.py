#!/usr/bin/env python
"""Seed soups and module swaps for the rehearsal-ratio study (see EXPERIMENTS.md, 20261030-nemotron-ft-ear1-ratio-study).

  soup-<family>_s<step>       uniform average (float32) of the seed-42 and seed-43 checkpoints of a family at one step
  swap-<family>_s<step>-base_lower / -base_upper
                              the seed-42 checkpoint with the base model's lower (layers 0-15, pre_encode, embed_norm) or
                              upper (16-30, final_norm) encoder (eval/drift_diag.py take / GROUPS)
Checkpoints come from <arms>/arms.json; each is written as <out>/<name>.ckpt ({"state_dict"}), loaded strictly by
recipes/diarization/nemotron_infer.py. Prints name=path pairs for eval/score_ft_arms.py --ckpts.

    python eval/ratio_soup.py --arms results/20261028-nemotron-ft-ear1-v2 --out $DATA/exp/nemotron/20261030-ratio-study/ckpts \
        --soup r0:500,1250 A-fa:500,1250 --swap r0:1250 A-fa:1250
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import torch

from drift_diag import base_state, ft_state, mix, take


def ckpt_name(fam: str, step: int, seed43: bool) -> str:
    return f"A-fa{'' if fam == 'A-fa' else '-' + fam}{'-seed43' if seed43 else ''}_s{step}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--arms", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--soup", nargs="*", default=[], help="family:step[,step...]")
    ap.add_argument("--swap", nargs="*", default=[], help="family:step[,step...] (seed 42)")
    args = ap.parse_args()
    arms = json.loads((args.arms / "arms.json").read_text())
    path = lambda n: Path(arms[n]["ckpt"])
    args.out.mkdir(parents=True, exist_ok=True)
    out = []
    for spec in args.soup:
        fam, steps = spec.split(":")
        for step in map(int, steps.split(",")):
            name = f"soup-{ckpt_name(fam, step, False)}"
            dst = args.out / f"{name}.ckpt"
            if not dst.exists():
                a, b = ft_state(path(ckpt_name(fam, step, False))), ft_state(path(ckpt_name(fam, step, True)))
                torch.save({"state_dict": mix(a, b, 0.5)}, dst)
            out.append(f"{name}={dst}")
    base = base_state() if args.swap else None
    for spec in args.swap:
        fam, steps = spec.split(":")
        for step in map(int, steps.split(",")):
            ft = ft_state(path(ckpt_name(fam, step, False)))
            for group in ("lower", "upper"):
                name = f"swap-{ckpt_name(fam, step, False)}-base_{group}"
                dst = args.out / f"{name}.ckpt"
                if not dst.exists():
                    torch.save({"state_dict": take(ft, base, group)}, dst)
                out.append(f"{name}={dst}")
    print(" ".join(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
