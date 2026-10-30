#!/usr/bin/env python
"""Score fine-tuned Nemotron checkpoints of several training arms on one table.

Per checkpoint (name=path), each step cached so the script can be re-run as checkpoints arrive:
  infer   recipes/diarization/nemotron_infer.py on EAR-1 dev D1/R1, held-out D1/R1, the crowd sets and
          the gate sets -> <exp>/selection/<name>/ (resumable)
  score   eval/select_nemotron_ckpt.py score / crowd: dev and held-out DER (oracle-VAD fill), crowd DER and
          missed speakers, dev 4-speaker exact count -> <results>/<name>{,.crowd}.json
  gate    AliMeeting Test-far ch1 / NOTSOFAR eval-SC160 DER vs forced-alignment and segment refs
          (eval/drift_diag.py gate) -> <results>/<name>.gate.json
  fa      EAR-1 dev DER against the forced-alignment refs (eval/vad_postproc.py on manifests whose
          rttm_filepath points at refs/ear1/dev/rttm/fa) -> <results>/<name>.fa.json
  drift   relative weight change vs base per module group (eval/drift_diag.py GROUPS)
  views   per-view (D1 / R1 / H*) DER, missed-speaker rate, count bias and 4-speaker exact count on EAR-1 dev
          and the crowd sets after the oracle-VAD fill (eval/crowd_eval.py) -> <results>/<name>.views.json
Writes <results>/arms.{json,md} over every checkpoint scored so far in <results>: the D1/R1 mean table, then a
per-track table (the fixed D1 and moving R1 tracks can move in opposite directions).

    python eval/score_ft_arms.py --exp $DATA/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval \
        --ft-manifests $DATA/manifests/nemotron_ft/ear1_v1 --results results/20261028-nemotron-ft-ear1-v2 \
        --ckpts A-seg_s1250=<ckpt> ...
"""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

import torch

import crowd_eval as ce
import drift_diag as dd
import select_nemotron_ckpt as sel

FA_MANIFESTS = Path("/mnt/data/manifests/nemo_fa")
BASE_GATE = {"alimeeting_Test_Ali_far_ch1": 10.48, "notsofar_eval_sc160": 10.98}


def fa_manifests(src: Path) -> None:
    FA_MANIFESTS.mkdir(parents=True, exist_ok=True)
    for c in ("ear1_dev_D1", "ear1_dev_R1"):
        rows = [json.loads(x) for x in (src / f"{c}.jsonl").read_text().splitlines() if x.strip()]
        for r in rows:
            r["rttm_filepath"] = r["rttm_filepath"].replace("/rttm/segments/", "/rttm/fa/")
            r["ref_type"] = "fa"
        (FA_MANIFESTS / f"{c}.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))


def fa_score(name: str, args) -> dict:
    out = args.results / f"{name}.fa.json"
    if not out.exists():
        tmp = args.results / "tmp_fa"
        subprocess.run([str(sel.DICOW_PY), str(sel.REPO / "eval/vad_postproc.py"), "--name", name, "--rttm-root",
                        str(args.exp / "selection" / name / "rttm"), "--conditions", "ear1_dev_D1", "ear1_dev_R1",
                        "--manifests", str(FA_MANIFESTS), "--out", str(tmp)], check=True, stdout=subprocess.DEVNULL)
        d = json.loads((tmp / f"{name}.json").read_text())["conditions"]
        out.write_text(json.dumps({c: {m: d[c][m] for m in ("base", "fill_nearest_vad")} for c in d}, indent=1))
        (tmp / f"{name}.json").unlink()
        (tmp / f"{name}.md").unlink()
    return json.loads(out.read_text())


def views(name: str, args) -> dict:
    """Per (condition, view) after the fill: DER, missed-speaker rate, count bias, exact count on 4-speaker recordings."""
    out = args.results / f"{name}.views.json"
    if not out.exists():
        res = {}
        for cond in ("ear1_dev_D1", "ear1_dev_R1", "ear1_crowd_real", "ear1_crowd_synth8"):
            rows = [json.loads(x) for x in (args.manifests / f"{cond}.jsonl").read_text().splitlines() if x.strip()]
            agg: dict = {}
            for row in rows:
                r = ce.one(row, args.exp / "selection" / name / "rttm" / cond, methods=["fill_nearest_vad"])["fill_nearest_vad"]
                a = agg.setdefault(row["channel"], {"ref_speech": 0.0, "err": 0.0, "n_ref": 0, "missed": 0, "bias": 0, "n": 0,
                                                    "n4": 0, "exact4": 0})
                a["ref_speech"] += r["ref_speech"]
                a["err"] += r["miss"] + r["fa"] + r["conf"]
                a["n_ref"] += r["n_ref"]
                a["missed"] += len(r["missed"])
                a["bias"] += r["n_hyp"] - r["n_ref"]
                a["n"] += 1
                if r["n_ref"] == 4:
                    a["n4"] += 1
                    a["exact4"] += r["n_hyp"] == 4
            res[cond] = {v: {"der": a["err"] / a["ref_speech"], "missed_rate": a["missed"] / a["n_ref"], "bias": a["bias"] / a["n"],
                             "n": a["n"], "exact4": a["exact4"] / a["n4"] if a["n4"] else None} for v, a in agg.items()}
        out.write_text(json.dumps(res, indent=1))
    return json.loads(out.read_text())


def drift(path: Path, base: dict) -> dict:
    s = base if path.name == "base" else dd.ft_state(path)
    return {g: float(torch.sqrt(sum(((s[k].float() - base[k].float()) ** 2).sum() for k in base if fn(k)))
                     / torch.sqrt(sum((base[k].float() ** 2).sum() for k in base if fn(k)))) for g, fn in dd.GROUPS.items()}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--exp", type=Path, required=True)
    ap.add_argument("--ft-manifests", type=Path, required=True)
    ap.add_argument("--manifests", type=Path, default=Path("/mnt/data/manifests/nemo"))
    ap.add_argument("--results", type=Path, required=True)
    ap.add_argument("--ckpts", nargs="*", default=[], help="name=<checkpoint>; base=base scores the released model")
    args = ap.parse_args()
    args.results.mkdir(parents=True, exist_ok=True)
    fa_manifests(args.manifests)
    base = dd.base_state()

    for spec in args.ckpts:
        name, path = spec.split("=", 1)
        model = str(sel.BASE) if path == "base" else path
        dd.infer(name, Path(model), args, full=True)
        r = {"ckpt": model, "sel": sel.score(name, model, args), "crowd": sel.crowd(name, model, args)}
        gate_out = args.results / f"{name}.gate.json"
        if not gate_out.exists():
            gate_out.write_text(json.dumps(dd.gate(name, args), indent=1))
        r["gate"] = json.loads(gate_out.read_text())
        r["fa"] = fa_score(name, args)
        r["drift"] = drift(Path(path), base)
        r["views"] = views(name, args)
        (args.results / f"{name}.arm.json").write_text(json.dumps(r, indent=1))
        print(f"scored {name}", flush=True)

    res = {p.name[: -len(".arm.json")]: json.loads(p.read_text()) for p in sorted(args.results.glob("*.arm.json"))}
    for name, r in res.items():
        if "views" not in r:  # scored before the per-view step existed
            r["views"] = views(name, args)
            (args.results / f"{name}.arm.json").write_text(json.dumps(r, indent=1))
    (args.results / "arms.json").write_text(json.dumps(res, indent=1))
    fill = lambda r, a, b: 50 * (r[a]["fill_nearest_vad"]["der"] + r[b]["fill_nearest_vad"]["der"])
    md = ["# Nemotron fine-tuning arms", "",
          "DER % collar 0. dev / held = EAR-1 dev / held-out train fold, mean of D1 and R1 after the oracle-VAD fill, "
          "against the organiser segment refs (official) and, for dev, the forced-alignment refs (`dev fa`: the fa union is "
          "also the VAD, a counterfactual). 4-spk = exact count on the 4-speaker dev recordings. crowd = DER (missed "
          "speakers). score = mean(dev, crowd real, crowd synth8). Gate = DER vs fa refs, Δ vs base (pass ≤ +1). "
          "Drift = ||W - W_base|| / ||W_base|| % for lower (layers 0-15) / upper (16-30) / head. Generated by eval/score_ft_arms.py.", "",
          "| checkpoint | dev | dev fa | held | 4-spk | crowd real | crowd synth8 | score | AliMeeting Δ | NOTSOFAR Δ | drift % |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for name, r in res.items():
        s, c, g = r["sel"], r["crowd"], r["gate"]
        dev = fill(s, "dev_D1", "dev_R1")
        score = (dev + 100 * c["crowd_real"]["der"] + 100 * c["crowd_synth8"]["der"]) / 3
        gd = {k: 100 * g[k]["der"] - BASE_GATE[k] for k in BASE_GATE}
        dr = " / ".join(f"{100 * r['drift'][k]:.2f}" for k in ("lower", "upper", "head"))
        md.append(f"| {name} | {dev:.2f} | {fill(r['fa'], 'ear1_dev_D1', 'ear1_dev_R1'):.2f} | {fill(s, 'held_D1', 'held_R1'):.2f} | "
                  f"{100 * c['dev_4spk']['exact']:.0f}% | {100 * c['crowd_real']['der']:.2f} ({100 * c['crowd_real']['missed_rate']:.1f}%) | "
                  f"{100 * c['crowd_synth8']['der']:.2f} ({100 * c['crowd_synth8']['missed_rate']:.1f}%) | {score:.2f} | "
                  + " | ".join(f"{v:+.2f}{'' if v <= 1 else ' ✗'}" for v in gd.values())
                  + f" | {dr} |")
    md += ["", "## Per track", "",
           "D1 = fixed far-field mic, R1 = moving mic (each an ESD-ON track). DER % after the oracle-VAD fill, segment refs; "
           "dev and held in brackets: confusion. dev fa = vs forced-alignment refs. 4-spk = exact count on the 4-speaker dev "
           "recordings (5 per track). crowd = DER (count bias); crowd real has 3 recordings per view, synth8 12.", "",
           "| checkpoint | dev D1 | dev R1 | held D1 | held R1 | dev fa D1 | dev fa R1 | 4-spk D1 | 4-spk R1 | "
           "crowd real D1 | crowd real R1 | synth8 D1 | synth8 R1 |", "|---|" + "---|" * 12]
    for name, r in res.items():
        s, f, v = r["sel"], r["fa"], r["views"]
        sd = lambda k: f"{100 * s[k]['fill_nearest_vad']['der']:.2f} ({100 * s[k]['fill_nearest_vad']['conf_rate']:.1f})"
        cw = lambda c, w: f"{100 * v[c][w]['der']:.2f} ({v[c][w]['bias']:+.1f})"
        md.append(f"| {name} | {sd('dev_D1')} | {sd('dev_R1')} | {sd('held_D1')} | {sd('held_R1')} | "
                  f"{100 * f['ear1_dev_D1']['fill_nearest_vad']['der']:.2f} | {100 * f['ear1_dev_R1']['fill_nearest_vad']['der']:.2f} | "
                  f"{100 * v['ear1_dev_D1']['D1']['exact4']:.0f}% | {100 * v['ear1_dev_R1']['R1']['exact4']:.0f}% | "
                  f"{cw('ear1_crowd_real', 'D1')} | {cw('ear1_crowd_real', 'R1')} | "
                  f"{cw('ear1_crowd_synth8', 'D1')} | {cw('ear1_crowd_synth8', 'R1')} |")
    (args.results / "arms.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
