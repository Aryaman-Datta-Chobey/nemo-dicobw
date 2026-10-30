#!/usr/bin/env python
"""Where does Nemotron fine-tuning drift come from? Weight blending, module swaps and the gate by step.

Variants of the base model (B) and a fine-tuned checkpoint (F, --ft), all written as
<exp>/ckpts/<name>.ckpt ({"state_dict"}, loaded strictly by recipes/diarization/nemotron_infer.py):
  base, ft                          the two endpoints
  blend_a{25,50,75}                 (1 - a) B + a F (weight-space interpolation)
  avg_<epochs>                      uniform average of the --avg-epochs checkpoints of the same run
  ft_head_only                      B with F's sortformer_modules (encoder reset to base)
  ft_base_head                      F with B's sortformer_modules
  ft_base_lower / ft_base_upper     F with B's encoder layers 0-15 (+ pre_encode, embed_norm) /
                                    16-30 (+ final_norm)
Per variant: EAR-1 dev D1/R1 and held-out D1/R1 (vad_postproc base / fill), crowd set and dev 4-speaker
count (eval/select_nemotron_ckpt.py score / crowd), and the regression gate (AliMeeting Test-far ch1,
NOTSOFAR eval-SC160; eval/score_diar_run.py: forced-alignment and segment references). --gate-epochs:
the gate only, for those epochs of the --ft run (its dev / crowd scores are in its selection results).
Also the relative weight change ||W - W_B|| / ||W_B|| per module group for every checkpoint of the run.

Stages: build (CPU), infer (GPU; one nemotron_infer call per variant, resumable), score (CPU).
Writes <results>/{drift.json, drift.md, weight_drift.md}.

    python eval/drift_diag.py --stage all --exp $DATA/exp/nemotron/20261028-nemotron-ft-ear1-drift \
        --ft $DATA/exp/nemotron/20261027-nemotron-ft-ear1-nospkw/nemotron_ft_ear1_nospkw/checkpoints/<epoch=6>.ckpt \
        --ft-manifests $DATA/manifests/nemotron_ft/ear1_v1 --results results/20261028-nemotron-ft-ear1-drift
"""
from __future__ import annotations

import argparse
import io
import json
import re
import subprocess
import tarfile
from pathlib import Path

import torch

import select_nemotron_ckpt as sel

GATE = ["alimeeting_Test_Ali_far_ch1", "notsofar_eval_sc160"]
GROUPS = {
    "lower": lambda k: k.startswith(("encoder.pre_encode.", "encoder.embed_norm."))
    or (m := re.match(r"encoder\.layers\.(\d+)\.", k)) is not None and int(m[1]) < 16,
    "upper": lambda k: k.startswith("encoder.final_norm.")
    or (m := re.match(r"encoder\.layers\.(\d+)\.", k)) is not None and int(m[1]) >= 16,
    "head": lambda k: k.startswith("sortformer_modules."),
}


def base_state() -> dict[str, torch.Tensor]:
    with tarfile.open(sel.BASE) as tar:
        member = next(m for m in tar.getmembers() if m.name.endswith("model_weights.ckpt"))
        return torch.load(io.BytesIO(tar.extractfile(member).read()), map_location="cpu")


def ft_state(path: Path) -> dict[str, torch.Tensor]:
    return torch.load(path, map_location="cpu", weights_only=False)["state_dict"]


def epoch_ckpts(ft: Path) -> dict[int, Path]:
    return {int(re.search(r"epoch=(\d+)", p.stem)[1]): p for p in ft.parent.glob("*.ckpt") if "-last" not in p.stem}


def mix(b: dict, f: dict, a: float) -> dict:
    # float32: the released base is bf16, and (1 - a) * b in bf16 rounds by more than the fine-tuning delta unless 1 - a is a power of 2
    return {k: (1 - a) * b[k].float() + a * f[k].float() if f[k].is_floating_point() else f[k] for k in f}


def take(dst: dict, src: dict, group: str) -> dict:
    return {k: src[k] if GROUPS[group](k) else v for k, v in dst.items()}


def build(args) -> dict[str, Path]:
    b, f = base_state(), ft_state(args.ft)
    assert b.keys() == f.keys(), "base and fine-tuned state dicts differ"
    eps = epoch_ckpts(args.ft)
    avg = None
    if args.avg_epochs:
        sds = [ft_state(eps[e]) for e in args.avg_epochs]
        avg = {k: torch.stack([s[k].float() for s in sds]).mean(0).to(v.dtype) if v.is_floating_point() else v
               for k, v in f.items()}
        del sds
    variants = {"base": b, "ft": f, **{f"blend_a{int(100 * a)}": mix(b, f, a) for a in args.alphas},
                "ft_head_only": take(b, f, "head"), "ft_base_head": take(f, b, "head"),
                "ft_base_lower": take(f, b, "lower"), "ft_base_upper": take(f, b, "upper")}
    if avg is not None:
        variants["avg_e" + "-".join(map(str, args.avg_epochs))] = avg
    out = {}
    (args.exp / "ckpts").mkdir(parents=True, exist_ok=True)
    for name, sd in variants.items():
        path = args.exp / "ckpts" / f"{name}.ckpt"
        if not path.exists():
            torch.save({"state_dict": sd}, path)
        out[name] = path
    drift = {}
    for e, p in sorted(eps.items()):
        s = ft_state(p)
        drift[f"epoch={e}"] = {g: float(torch.sqrt(sum(((s[k].float() - b[k].float()) ** 2).sum() for k in b if fn(k)))
                                        / torch.sqrt(sum((b[k].float() ** 2).sum() for k in b if fn(k))))
                               for g, fn in GROUPS.items()}
        if p == args.ft:
            drift["per_layer"] = {
                str(i): float(torch.sqrt(sum(((s[k].float() - b[k].float()) ** 2).sum() for k in b if k.startswith(f"encoder.layers.{i}.")))
                              / torch.sqrt(sum((b[k].float() ** 2).sum() for k in b if k.startswith(f"encoder.layers.{i}."))))
                for i in range(31)}
    args.results.mkdir(parents=True, exist_ok=True)
    (args.results / "weight_drift.json").write_text(json.dumps(drift, indent=1))
    md = ["# Relative weight change vs base, ||W - W_base|| / ||W_base||", "",
          "Groups: lower = pre_encode + encoder layers 0-15, upper = layers 16-30 + final norm, head = sortformer_modules. "
          "Generated by eval/drift_diag.py.", "", "| checkpoint | lower | upper | head |", "|---|---|---|---|"]
    md += [f"| {k} | {v['lower']:.4f} | {v['upper']:.4f} | {v['head']:.4f} |" for k, v in drift.items() if k != "per_layer"]
    if "per_layer" in drift:
        md += ["", f"Per encoder layer, `{args.ft.stem}`:", "", "| layer | rel. change |", "|---|---|"]
        md += [f"| {i} | {v:.4f} |" for i, v in drift["per_layer"].items()]
    (args.results / "weight_drift.md").write_text("\n".join(md) + "\n")
    return out


def manifests(args, full: bool) -> list[Path]:
    m = [args.manifests / f"{c}.jsonl" for c in GATE]
    if full:
        m += [args.manifests / f"{v}.jsonl" for k, v in sel.SETS.items() if k.startswith("dev")]
        m += [args.ft_manifests / f"{v}.jsonl" for k, v in sel.SETS.items() if k.startswith("held")]
        m += [args.manifests / f"{v}.jsonl" for v in sel.CROWD.values()]
    return m


def infer(name: str, model: Path, args, full: bool) -> None:
    subprocess.run([str(sel.NEMO_PY), str(sel.REPO / "recipes/diarization/nemotron_infer.py"), "--out",
                    str(args.exp / "selection" / name), "--model", str(model), *map(str, manifests(args, full))],
                   check=True, stdout=subprocess.DEVNULL)
    print(f"inferred {name}", flush=True)


def gate(name: str, args) -> dict:
    run = args.exp / "selection" / name
    subprocess.run([str(sel.DICOW_PY), str(sel.REPO / "eval/score_diar_run.py"), "--run-dir", str(run),
                    "--results", str(args.results / "gate"), "--conditions", *GATE], check=True, stdout=subprocess.DEVNULL)
    out = {}
    for c in GATE:
        for suffix in ("", "__segments"):
            d = json.loads((args.results / "gate" / name / f"{c}{suffix}.json").read_text())["overall"]["diar"]["0.00"]
            out[c + suffix] = {k: d[k] / d["ref_speech"] for k in ("miss", "fa", "conf")} | {"der": d["der"]}
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stage", choices=["build", "infer", "score", "all"], default="all")
    ap.add_argument("--exp", type=Path, required=True)
    ap.add_argument("--ft", type=Path, required=True)
    ap.add_argument("--ft-manifests", type=Path, required=True)
    ap.add_argument("--manifests", type=Path, default=Path("/mnt/data/manifests/nemo"))
    ap.add_argument("--results", type=Path, required=True)
    ap.add_argument("--alphas", type=float, nargs="*", default=[0.25, 0.5, 0.75])
    ap.add_argument("--avg-epochs", type=int, nargs="*", default=[4, 5, 6, 7, 8])
    ap.add_argument("--gate-epochs", type=int, nargs="*", default=[0, 2, 4, 10, 15])
    args = ap.parse_args()
    eps = epoch_ckpts(args.ft)
    gate_eps = {f"epoch={e}": eps[e] for e in args.gate_epochs}

    if args.stage in ("build", "all"):
        variants = build(args)
    else:
        variants = {p.stem: p for p in sorted((args.exp / "ckpts").glob("*.ckpt"))}
    if args.stage in ("infer", "all"):
        for name, path in variants.items():
            infer(name, path, args, full=True)
        for name, path in gate_eps.items():
            infer(name, path, args, full=False)
    if args.stage not in ("score", "all"):
        return 0

    res = {}
    for name, path in variants.items():
        res[name] = {"sel": sel.score(name, str(path), args), "crowd": sel.crowd(name, str(path), args), "gate": gate(name, args)}
        print(f"scored {name}", flush=True)
    for name in gate_eps:
        res[name] = {"gate": gate(name, args)}
        print(f"scored {name}", flush=True)
    (args.results / "drift.json").write_text(json.dumps(res, indent=1))

    def g(r, c):
        x = r["gate"][c]
        return f"{100 * x['der']:.2f} ({100 * x['fa']:.2f} / {100 * x['conf']:.2f})"

    md = ["# Drift diagnostics: weight blending, module swaps, gate by step", "",
          f"F = `{args.ft.stem}`. Dev / crowd DER % after the oracle-VAD fill (collar 0); dev 4-spk = exact speaker count "
          "on the 4-speaker dev recordings; score = mean(dev mean, crowd real, crowd synth8). Gate DER % collar 0 "
          "(FA / conf) vs forced-alignment refs, and DER vs segment refs. Generated by eval/drift_diag.py.", "",
          "| variant | dev mean | dev 4-spk | crowd real (missed) | crowd synth8 (missed) | score | AliMeeting fa | AliMeeting seg | NOTSOFAR fa | NOTSOFAR seg |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for name, r in res.items():
        if "sel" in r:
            dev = 50 * (r["sel"]["dev_D1"]["fill_nearest_vad"]["der"] + r["sel"]["dev_R1"]["fill_nearest_vad"]["der"])
            cr = r["crowd"]
            score = (dev + 100 * cr["crowd_real"]["der"] + 100 * cr["crowd_synth8"]["der"]) / 3
            left = (f"{dev:.2f} | {100 * cr['dev_4spk']['exact']:.0f}% | {100 * cr['crowd_real']['der']:.2f} "
                    f"({100 * cr['crowd_real']['missed_rate']:.1f}%) | {100 * cr['crowd_synth8']['der']:.2f} "
                    f"({100 * cr['crowd_synth8']['missed_rate']:.1f}%) | {score:.2f}")
        else:
            left = "– | – | – | – | –"
        md.append(f"| {name} | {left} | {g(r, GATE[0])} | {100 * r['gate'][GATE[0] + '__segments']['der']:.2f} | "
                  f"{g(r, GATE[1])} | {100 * r['gate'][GATE[1] + '__segments']['der']:.2f} |")
    (args.results / "drift.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
