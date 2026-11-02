#!/usr/bin/env python
"""Simulated meetings for the open DiCoW recipe (EXPERIMENTS.md 20261031-dicow-open-prep).

  fit       mean pause and overlap of AliMeeting + AISHELL-4 train (one far-field channel per session, recipes/data/dicow_real_cuts.py)
            with FastMSS's TransitionParams.fit -> <root>/hmm_betas.json. Only the betas are used; p_ind stays the paper's.
  simulate  one FastMSS run per speaker count, config recipes/data/configs/fastmss_dicow_open.yaml, sharing the source-cut prep.
  manifest  join the per-k cuts, re-join the text FastMSS split at pauses (no spaces except between Latin words), and write
            <out>/sim_open_cutset_train.jsonl.gz (uncut) and sim_open_cutset_train_30s.jsonl.gz, using the window rule of
            dicow_real_cuts.py, with a .stats.json of active speakers per window.

Env `fastmss` for fit and simulate, `dicow` for manifest:
    python recipes/data/sim_dicow_open.py fit
    python recipes/data/sim_dicow_open.py simulate --mix 2:30 3:30 4:40 --root <dir>
    python recipes/data/sim_dicow_open.py manifest --root <dir> --out <dir>
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

DATA = Path("/mnt/data")
REPO = Path(__file__).resolve().parents[2]
FASTMSS = Path.home() / "src/FastMSS"
ROOT = DATA / "sim/dicow_open"
LHOTSE = DATA / "manifests/lhotse"
LATIN_GAP = re.compile(r"(?<![0-9A-Za-z.,!?'])\s+|\s+(?![0-9A-Za-z])")


def fit(args) -> None:
    from lhotse import CutSet, SupervisionSet

    from fastmss.hmm_turn_taking import TransitionParams

    sups = []
    for c in ("alimeeting", "aishell4"):
        for cut in CutSet.from_file(LHOTSE / c / f"{c}_cutset_train.jsonl.gz"):
            if cut.recording_id.endswith("__far_ch1"):
                sups += list(cut.supervisions)
    tp = TransitionParams()
    tp.fit(SupervisionSet.from_segments(sups))
    out = {"beta_th": tp.beta_th, "beta_ts": tp.beta_ts, "beta_ir": tp.beta_ir, "beta_bc": tp.beta_bc, "fitted_p_ind_unused": tp.p_ind, "supervisions": len(sups)}
    args.root.mkdir(parents=True, exist_ok=True)
    (args.root / "hmm_betas.json").write_text(json.dumps(out, indent=1) + "\n")
    print(out)


def simulate(args) -> None:
    betas = json.loads((args.betas or args.root / "hmm_betas.json").read_text())
    mix = {int(k): int(n) for k, n in (x.split(":") for x in args.mix)}
    for k, n in sorted(mix.items()):
        cmd = [sys.executable, str(FASTMSS / "recipes/sim.py"), "--config-path", str(REPO / "recipes/data/configs"), "--config-name", args.config,
               f"output_dir={args.root / f'{k}spk'}", f"data_dir={args.prep or args.root / 'prep'}", f"min_max_spk=[{k},{k}]", f"n_meetings={n}",
               f"n_jobs={args.jobs}", f"seed={args.seed + k}"] + [f"+hmm_params.{b}={betas[b]}" for b in ("beta_th", "beta_ts", "beta_ir", "beta_bc")]
        print(" ".join(cmd), flush=True)
        subprocess.run(cmd, check=True, cwd=FASTMSS)


def rejoin(text: str) -> str:
    return re.sub(r"\s+", " ", LATIN_GAP.sub("", text)).strip()


def manifest(args) -> None:
    from lhotse import CutSet, SupervisionSegment
    from lhotse.cut import MonoCut

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from dicow_real_cuts import windows

    args.out.mkdir(parents=True, exist_ok=True)
    full, wins = [], []
    n: Counter = Counter()
    hist: Counter = Counter()
    hist5: Counter = Counter()
    per_k: dict = {}
    for d in sorted(args.root.glob("*spk"), key=lambda p: int(p.name[:-3])):
        k_hist: Counter = Counter()
        for path in d.glob("manifests/synth-*-cuts.jsonl.gz"):
            for cut in CutSet.from_file(path):
                sups = [{"start": s.start, "end": s.end, "speaker": s.speaker, "text": rejoin(s.text)} for s in cut.supervisions]
                sups = [s for s in sups if s["end"] <= cut.duration]
                full.append(cut.with_id(cut.id))
                for i, s in enumerate(cut.supervisions):
                    s.text = rejoin(s.text)
                    s.alignment = None
                for t0, dur, keep in windows(sups, cut.duration, 30.0, n):
                    cid = f"{cut.recording_id}-w{int(t0 * 100):06d}"
                    wins.append(MonoCut(id=cid, start=round(t0, 3), duration=round(dur, 3), channel=0, recording=cut.recording, supervisions=[
                        SupervisionSegment(id=f"{cid}-{i}", recording_id=cut.recording_id, start=round(s["start"] - t0, 3), duration=round(s["end"] - s["start"], 3),
                                           channel=0, text=s["text"], speaker=s["speaker"], language="zh") for i, s in enumerate(keep)]))
                    act: Counter = Counter()
                    for s in keep:
                        act[s["speaker"]] += s["end"] - s["start"]
                    hist[len(act)] += 1
                    k_hist[len(act)] += 1
                    hist5[sum(v >= 5.0 for v in act.values())] += 1
                n["hours"] += cut.duration / 3600
        per_k[d.name] = dict(sorted(k_hist.items()))
    CutSet.from_cuts(full).to_file(args.out / "sim_open_cutset_train.jsonl.gz")
    CutSet.from_cuts(wins).to_file(args.out / "sim_open_cutset_train_30s.jsonl.gz")
    total = sum(hist.values())
    stats = {"meetings": len(full), "windows": total, **{a: round(b, 2) for a, b in sorted(n.items())},
             "active_any": dict(sorted(hist.items())), "share_any_ge5": round(sum(v for k, v in hist.items() if k >= 5) / total, 3),
             "active_ge5s": dict(sorted(hist5.items())), "share_ge5s_ge5": round(sum(v for k, v in hist5.items() if k >= 5) / total, 3), "per_k_any": per_k}
    (args.out / "sim_open_cutset_train.stats.json").write_text(json.dumps(stats, indent=1) + "\n")
    print(json.dumps(stats))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", choices=["fit", "simulate", "manifest"])
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--betas", type=Path, help="default <root>/hmm_betas.json")
    ap.add_argument("--prep", type=Path, help="shared source-cut prep (default <root>/prep)")
    ap.add_argument("--out", type=Path, default=LHOTSE / "dicow_open")
    ap.add_argument("--config", default="fastmss_dicow_open")
    ap.add_argument("--mix", nargs="+", default=[], help="k:meetings ...")
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--seed", type=int, default=2000)
    args = ap.parse_args()
    {"fit": fit, "simulate": simulate, "manifest": manifest}[args.stage](args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
