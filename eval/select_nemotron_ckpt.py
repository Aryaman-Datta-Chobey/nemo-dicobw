#!/usr/bin/env python
"""Score every checkpoint of a Nemotron fine-tuning run for ESD-ON checkpoint selection.

For each <exp>/**/checkpoints/*.ckpt (plus the base model as "base"):
  1. recipes/diarization/nemotron_infer.py (nemo env) on EAR-1 dev D1/R1 and the held-out train sessions
     (<ft manifests>/heldout_{D1,R1}.jsonl) -> <exp>/selection/<ckpt>/
  2. eval/vad_postproc.py with methods base and fill_nearest_vad (oracle VAD = per-speaker TextGrid
     intervals, the organisers' definition) -> <results>/<ckpt>.json
  3. crowd set (recipes/diarization/make_crowd_set.py: ear1_crowd_real, ear1_crowd_synth8, speaker-disjoint
     7-8-speaker recordings) and the dev 4-speaker count gate, via eval/crowd_eval.py with the fill
     -> <results>/<ckpt>.crowd.json
Skips checkpoints already scored, so it can be re-run while training continues. Writes
<results>/selection.md: per checkpoint DER without and with the oracle-VAD fill, and speaker-count
accuracy, for dev D1, dev R1, held-out D1, held-out R1, plus the dev mean after the fill (the selection
criterion until 2026-10-28; held-out is the check on the 5–8-speaker regime), and the crowd columns: DER after the
fill / missed-speaker rate on crowd real and synth8, dev 4-speaker exact count (D1+R1; gate = not below base), and
the selection score = mean of the dev mean and the two crowd DERs (all after the fill).

    python eval/select_nemotron_ckpt.py --exp $DATA/exp/nemotron/20261027-nemotron-ft-ear1 \
        --ft-manifests $DATA/manifests/nemotron_ft/ear1_v1 --results results/20261027-nemotron-ft-ear1
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from pathlib import Path

from crowd_eval import metrics, one

REPO = Path(__file__).resolve().parents[1]
NEMO_PY = Path.home() / "miniforge3/envs/nemo/bin/python"
DICOW_PY = Path.home() / "miniforge3/envs/dicow/bin/python"
BASE = "/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo"
SETS = {"dev_D1": "ear1_dev_D1", "dev_R1": "ear1_dev_R1", "held_D1": "heldout_D1", "held_R1": "heldout_R1"}
CROWD = {"crowd_real": "ear1_crowd_real", "crowd_synth8": "ear1_crowd_synth8"}


def score(name: str, model: str, args) -> dict:
    out = args.results / f"{name}.json"
    if out.exists():
        return json.loads(out.read_text())
    run = args.exp / "selection" / name
    man = {k: (args.manifests / f"{v}.jsonl" if k.startswith("dev") else args.ft_manifests / f"{v}.jsonl")
           for k, v in SETS.items()}
    subprocess.run([str(NEMO_PY), str(REPO / "recipes/diarization/nemotron_infer.py"), "--out", str(run),
                    "--model", model, *map(str, man.values())], check=True, stdout=subprocess.DEVNULL)
    res = {}
    for key, cond in SETS.items():
        tmp = args.results / "tmp" / name
        subprocess.run([str(DICOW_PY), str(REPO / "eval/vad_postproc.py"), "--name", key, "--rttm-root",
                        str(run / "rttm"), "--conditions", cond, "--manifests", str(man[key].parent),
                        "--out", str(tmp)], check=True, stdout=subprocess.DEVNULL)
        r = json.loads((tmp / f"{key}.json").read_text())["conditions"][cond]
        res[key] = {m: r[m] for m in ("base", "fill_nearest_vad")}
    shutil.rmtree(args.results / "tmp" / name)
    out.write_text(json.dumps(res, indent=1))
    return res


def crowd(name: str, model: str, args) -> dict:
    out = args.results / f"{name}.crowd.json"
    if out.exists():
        return json.loads(out.read_text())
    run = args.exp / "selection" / name
    man = {k: args.manifests / f"{v}.jsonl" for k, v in {**CROWD, "dev_D1": SETS["dev_D1"], "dev_R1": SETS["dev_R1"]}.items()}
    subprocess.run([str(NEMO_PY), str(REPO / "recipes/diarization/nemotron_infer.py"), "--out", str(run),
                    "--model", model, *map(str, man.values())], check=True, stdout=subprocess.DEVNULL)
    res, dev4 = {}, []
    with ProcessPoolExecutor(8) as ex:
        for key, path in man.items():
            rows = [json.loads(x) for x in path.read_text().splitlines() if x.strip()]
            recs = [r["fill_nearest_vad"] for r in ex.map(partial(one, rttm_dir=run / "rttm" / path.stem), rows)]
            if key in CROWD:
                res[key] = metrics(recs)
            else:
                dev4 += [r for r in recs if r["n_ref"] == 4]
    res["dev_4spk"] = {"n": len(dev4), "exact": sum(r["err"] == 0 for r in dev4) / len(dev4),
                       "bias": sum(r["err"] for r in dev4) / len(dev4)}
    out.write_text(json.dumps(res, indent=1))
    return res


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--exp", type=Path, required=True)
    ap.add_argument("--ft-manifests", type=Path, required=True)
    ap.add_argument("--manifests", type=Path, default=Path("/mnt/data/manifests/nemo"))
    ap.add_argument("--results", type=Path, required=True)
    args = ap.parse_args()
    args.results.mkdir(parents=True, exist_ok=True)
    ckpts = sorted(p for p in args.exp.rglob("checkpoints/*.ckpt") if "-last" not in p.stem)
    rows = {"base": score("base", BASE, args)}
    crowds = {"base": crowd("base", BASE, args)}
    for c in ckpts:
        rows[c.stem] = score(c.stem, str(c), args)
        crowds[c.stem] = crowd(c.stem, str(c), args)
    md = ["# Nemotron fine-tuning checkpoint selection (ESD-ON)", "",
          "DER % collar 0 without / with oracle-VAD fill (fill_nearest_vad), speaker-count accuracy % with fill. "
          "Selection: lowest dev mean after the fill. Generated by eval/select_nemotron_ckpt.py.", "",
          "| checkpoint | " + " | ".join(SETS) + " | dev mean (fill) | " + " | ".join(CROWD)
          + " | dev 4-spk exact | score |", "|---|" + "---|" * (len(SETS) + len(CROWD) + 3)]
    base4 = crowds["base"]["dev_4spk"]["exact"]
    for name, r in rows.items():
        cells = [f"{100 * r[k]['base']['der']:.2f} / **{100 * r[k]['fill_nearest_vad']['der']:.2f}** "
                 f"({100 * r[k]['fill_nearest_vad']['spk_count_acc']:.0f}%)" for k in SETS]
        dev = 50 * (r["dev_D1"]["fill_nearest_vad"]["der"] + r["dev_R1"]["fill_nearest_vad"]["der"])
        cr = crowds[name]
        ccells = [f"{100 * cr[k]['der']:.2f} / {100 * cr[k]['missed_rate']:.1f}%" for k in CROWD]
        ex4 = cr["dev_4spk"]["exact"]
        sel = (dev + sum(100 * cr[k]["der"] for k in CROWD)) / 3
        md.append(f"| {name} | " + " | ".join(cells) + f" | {dev:.2f} | " + " | ".join(ccells)
                  + f" | {100 * ex4:.0f}%{'' if ex4 >= base4 else ' ✗'} | {sel:.2f} |")
    (args.results / "selection.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
