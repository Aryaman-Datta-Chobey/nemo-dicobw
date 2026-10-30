#!/usr/bin/env python
"""Local vs recording-wide speaker confusion (windowed re-mapping, after Yu et al., arXiv 2610.08828 §4).

Speaker confusion C (collar 0, overlap scored, frames inside the UEM) uses one optimal reference->hypothesis
speaker mapping for the whole recording. Re-solving the mapping inside each W-second window gives the local
confusion L_W (errors no mapping can fix); G_W = C - L_W is the recording-wide consistency penalty (a speaker
split over time into several outputs, or two speakers swapping outputs). Long-split over-counts and identity
drift show up in G_W; frame-level confusion of similar voices stays in L_W.

Per checkpoint name, on the RTTMs in <exp>/selection/<name>/rttm/<condition>/:
    EAR-1 dev D1/R1, held-out D1/R1, crowd real/synth8   after the oracle-VAD fill (eval/vad_postproc.py
                                                         fill_nearest_vad), segment refs
    AliMeeting Test-far ch1, NOTSOFAR eval-SC160         diarizer output as is, forced-alignment refs
Writes <results>/remap/<name>.json and <results>/remap.md (all names scored so far; a D1/R1 mean table, then
per track, with the crowd sets split by view from the per-recording rows). Confusion is % of
reference speech; C is checked against the scorer's confusion (nemo_dicobw.diar_metrics.score_file).

    python eval/remap_diag.py --exp $DATA/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval \
        --ft-manifests $DATA/manifests/nemotron_ft/ear1_v1 --results results/20261028-nemotron-ft-ear1-v2 \
        --names base A-seg_s1250 ...
"""
from __future__ import annotations

import argparse
import json
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from pathlib import Path

import numpy as np
from scipy.optimize import linear_sum_assignment

from nemo_dicobw.diar_metrics import score_file
from nemo_dicobw.rttm import load_rttm, load_uem, merge_intervals
from vad_postproc import FR, apply, to_frames, to_turns

# condition -> (manifest dir key, VAD method)
CONDS = {"ear1_dev_D1": ("nemo", "fill_nearest_vad"), "ear1_dev_R1": ("nemo", "fill_nearest_vad"),
         "heldout_D1": ("ft", "fill_nearest_vad"), "heldout_R1": ("ft", "fill_nearest_vad"),
         "ear1_crowd_real": ("nemo", "fill_nearest_vad"), "ear1_crowd_synth8": ("nemo", "fill_nearest_vad"),
         "alimeeting_Test_Ali_far_ch1": ("nemo", "base"), "notsofar_eval_sc160": ("nemo", "base")}
WINDOWS = (10.0, 30.0)


def confusion(ref: np.ndarray, hyp: np.ndarray) -> int:
    """Confused frames under the best one-to-one mapping: sum_t min(n_ref, n_hyp) - mapped co-active frames."""
    if not ref.size or not hyp.size:
        return 0
    co = ref.astype(np.int32) @ hyp.T.astype(np.int32)
    r, c = linear_sum_assignment(co, maximize=True)
    return int(np.minimum(ref.sum(0), hyp.sum(0)).sum() - co[r, c].sum())


def one(row: dict, rttm_dir: Path, method: str) -> dict:
    uid, sess = row["uniq_id"], row["session"]
    ref_turns = load_rttm([Path(row["rttm_filepath"])]).get(sess, [])
    uem = load_uem([Path(row["uem_filepath"])])[sess]
    n = int(round(row["duration"] * FR))
    path = rttm_dir / f"{uid}.rttm"
    if not path.exists():
        raise FileNotFoundError(path)
    hyp_turns = load_rttm([path]).get(uid, [])
    hl = sorted({t.speaker for t in hyp_turns}) or ["spk"]
    vad = np.zeros(n, bool)
    for s, e in merge_intervals((t.start, t.end) for t in ref_turns):
        vad[int(round(s * FR)):int(round(e * FR))] = True
    hyp_turns = to_turns(apply(method, to_frames(hyp_turns, n, hl), None, vad), hl)
    scorer_conf = score_file(ref_turns, hyp_turns, uem, 0.0).conf
    keep = np.zeros(n, bool)
    for s, e in uem:
        keep[int(round(s * FR)):int(round(e * FR))] = True
    rl = sorted({t.speaker for t in ref_turns})
    ref, hyp = to_frames(ref_turns, n, rl)[:, keep], to_frames(hyp_turns, n, hl)[:, keep]
    out = {"uid": uid, "ref_speech": int(ref.sum()), "C": confusion(ref, hyp), "scorer_C": scorer_conf * FR}
    for w in WINDOWS:
        step = int(w * FR)
        out[f"L{w:g}"] = sum(confusion(ref[:, i:i + step], hyp[:, i:i + step]) for i in range(0, ref.shape[1], step))
    return out


def pooled(per: list[dict]) -> dict:
    tot = sum(p["ref_speech"] for p in per)
    d = {"C": sum(p["C"] for p in per) / tot,
         "max_abs_diff_vs_scorer_s": max(abs(p["C"] - p["scorer_C"]) for p in per) / FR}
    for w in WINDOWS:
        d[f"L{w:g}"] = sum(p[f"L{w:g}"] for p in per) / tot
        d[f"G{w:g}"] = d["C"] - d[f"L{w:g}"]
    return d


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--exp", type=Path, required=True)
    ap.add_argument("--ft-manifests", type=Path, required=True)
    ap.add_argument("--manifests", type=Path, default=Path("/mnt/data/manifests/nemo"))
    ap.add_argument("--results", type=Path, required=True)
    ap.add_argument("--names", nargs="*", default=[])
    ap.add_argument("--jobs", type=int, default=8)
    args = ap.parse_args()
    out_dir = args.results / "remap"
    out_dir.mkdir(parents=True, exist_ok=True)
    mdir = {"nemo": args.manifests, "ft": args.ft_manifests}
    with ProcessPoolExecutor(args.jobs) as ex:
        for name in args.names:
            out = out_dir / f"{name}.json"
            if out.exists():
                continue
            res = {}
            for cond, (key, method) in CONDS.items():
                rows = [json.loads(x) for x in (mdir[key] / f"{cond}.jsonl").read_text().splitlines() if x.strip()]
                per = list(ex.map(partial(one, rttm_dir=args.exp / "selection" / name / "rttm" / cond, method=method), rows))
                res[cond] = pooled(per) | {"method": method, "per_recording": per}
            out.write_text(json.dumps(res, indent=1))
            print(f"remap {name}", flush=True)

    res = {p.stem: json.loads(p.read_text()) for p in sorted(out_dir.glob("*.json"))}
    pairs = {"dev": ("ear1_dev_D1", "ear1_dev_R1"), "held": ("heldout_D1", "heldout_R1"),
             "crowd real": ("ear1_crowd_real",), "crowd synth8": ("ear1_crowd_synth8",),
             "AliMeeting": ("alimeeting_Test_Ali_far_ch1",), "NOTSOFAR": ("notsofar_eval_sc160",)}
    md = ["# Local vs recording-wide speaker confusion", "",
          "Speaker confusion % of reference speech, C = L30 + G30: L30 = confusion left after re-solving the speaker "
          "mapping in every 30 s window (local), G30 = recording-wide consistency penalty (splits, identity swaps); "
          "G10 in brackets. dev / held = mean of D1 and R1. EAR-1 sets after the oracle-VAD fill vs segment refs; "
          "AliMeeting / NOTSOFAR raw output vs forced-alignment refs. Generated by eval/remap_diag.py.", "",
          "| checkpoint | " + " | ".join(pairs) + " |", "|---|" + "---|" * len(pairs)]
    for name, r in res.items():
        cells = []
        for conds in pairs.values():
            m = {k: 100 * np.mean([r[c][k] for c in conds]) for k in ("C", "L30", "G30", "G10")}
            cells.append(f"{m['C']:.2f} = {m['L30']:.2f} + {m['G30']:.2f} ({m['G10']:.2f})")
        md.append(f"| {name} | " + " | ".join(cells) + " |")
    md += ["", "## Per track", "", "C = L30 + G30 as above, D1 (fixed mic) and R1 (moving mic) separately; crowd sets split by "
           "view (real: 3 recordings per view, synth8: 12).", "",
           "| checkpoint | dev D1 | dev R1 | held D1 | held R1 | crowd real D1 | crowd real R1 | synth8 D1 | synth8 R1 |",
           "|---|" + "---|" * 8]
    tracks = [("ear1_dev_D1", None), ("ear1_dev_R1", None), ("heldout_D1", None), ("heldout_R1", None),
              ("ear1_crowd_real", "D1"), ("ear1_crowd_real", "R1"), ("ear1_crowd_synth8", "D1"), ("ear1_crowd_synth8", "R1")]
    for name, r in res.items():
        cells = []
        for cond, view in tracks:
            per = [p for p in r[cond]["per_recording"] if view is None or p["uid"].endswith(f"__{view}")]
            m = pooled(per)
            cells.append(f"{100 * m['C']:.2f} = {100 * m['L30']:.2f} + {100 * m['G30']:.2f}")
        md.append(f"| {name} | " + " | ".join(cells) + " |")
    (args.results / "remap.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
