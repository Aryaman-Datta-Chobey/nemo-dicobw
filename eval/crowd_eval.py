#!/usr/bin/env python
"""Per-speaker evaluation of diarization systems on the EAR-1 crowd set, with session-bootstrap CIs.

Inputs: systems as name=<run dir> (RTTMs at <run>/rttm/<manifest stem>/<uniq_id>.rttm, as written by
recipes/diarization/nemotron_infer.py) and manifests from recipes/diarization/make_crowd_set.py.
Each recording is scored at collar 0 with eval/vad_postproc.py's base and fill_nearest_vad, then
analysed per reference speaker as in eval/count_diagnostics.py (D2): recall under the DER mapping,
missed = recall < 5%, and the fate of a missed speaker's solo frames (absorbed / silence / overlap_only).
Per system x method x manifest:
    DER (miss / FA / conf), exact speaker count, count bias, missed-speaker rate, absorbed rate,
    mean speaker recall (each reference speaker of each recording counts once)
with 95% bootstrap intervals over the manifest's "group" (the session, or the session pair for
synthetic recordings; views of one session are resampled together), and the paired difference of
each system against the first one. Writes <out>/crowd_eval.{json,md}.

    python eval/crowd_eval.py --out results/<run> --system base=$EXP/<base run> --system ft=$EXP/<ft run> \
        --manifest $DATA/manifests/nemo/ear1_crowd_real.jsonl --manifest $DATA/manifests/nemo/ear1_crowd_synth8.jsonl
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from pathlib import Path

import numpy as np

from count_diagnostics import analyse_recording
from nemo_dicobw.rttm import load_rttm, load_uem, merge_intervals
from vad_postproc import FR, apply, to_frames, to_turns

METHODS = ["base", "fill_nearest_vad"]
METRICS = ["der", "miss", "fa", "conf", "exact", "bias", "missed_rate", "absorbed_rate", "mean_recall"]
N_BOOT = 1000


def min_speech_filter(hyp: np.ndarray, abs_s: float, frac: float) -> np.ndarray:
    """Drop hypothesis speakers with less than max(abs_s, frac x the recording's hypothesis speech)."""
    if not (abs_s or frac) or not hyp.size:
        return hyp
    speech = hyp.sum(1) / FR
    keep = speech >= max(abs_s, frac * hyp.any(0).sum() / FR)
    return hyp & keep[:, None] if keep.any() else hyp


def one(row: dict, rttm_dir: Path, min_speech: tuple[float, float] = (0.0, 0.0), methods: list[str] = METHODS) -> dict:
    """Per-method recording analysis; min_speech = (seconds, fraction) for min_speech_filter, applied
    to the diarizer output before the method (so the fill reassigns a dropped speaker's VAD frames)."""
    uid, sess = row["uniq_id"], row["session"]
    ref = load_rttm([Path(row["rttm_filepath"])]).get(sess, [])
    uem = load_uem([Path(row["uem_filepath"])])[sess]
    n = int(round(row["duration"] * FR))
    path = rttm_dir / f"{uid}.rttm"
    if not path.exists():
        raise FileNotFoundError(path)  # an empty hypothesis would silently score as all-missed
    hyp_turns = load_rttm([path]).get(uid, [])
    labels = sorted({t.speaker for t in hyp_turns}) or ["spk"]
    hyp = min_speech_filter(to_frames(hyp_turns, n, labels), *min_speech)
    vad = np.zeros(n, bool)
    for s, e in merge_intervals((t.start, t.end) for t in ref):
        vad[int(round(s * FR)):int(round(e * FR))] = True
    out = {}
    for m in methods:
        rec = analyse_recording("ear1_crowd_set", row, ref, to_turns(apply(m, hyp, None, vad), labels), uem)
        s = rec.pop("score")
        rec.update(ref_speech=s.ref_speech, miss=s.miss, fa=s.fa, conf=s.conf, group=row.get("group", sess))
        out[m] = rec
    return out


def metrics(recs: list[dict]) -> dict[str, float]:
    rs = sum(r["ref_speech"] for r in recs)
    spk = [s for r in recs for s in r["speakers"]]
    missed = [m for r in recs for m in r["missed"]]
    return {"der": sum(r["miss"] + r["fa"] + r["conf"] for r in recs) / rs,
            "miss": sum(r["miss"] for r in recs) / rs, "fa": sum(r["fa"] for r in recs) / rs,
            "conf": sum(r["conf"] for r in recs) / rs,
            "exact": float(np.mean([r["err"] == 0 for r in recs])), "bias": float(np.mean([r["err"] for r in recs])),
            "missed_rate": len(missed) / len(spk),
            "absorbed_rate": sum(m["fate"] == "absorbed" for m in missed) / len(spk),
            "mean_recall": float(np.mean([s["recall"] for s in spk]))}


def bootstrap(per_sys: dict[str, list[dict]], ref_sys: str, seed: int = 0) -> dict:
    groups = sorted({r["group"] for r in per_sys[ref_sys]})
    by = {s: defaultdict(list) for s in per_sys}
    for s, recs in per_sys.items():
        for r in recs:
            by[s][r["group"]].append(r)
    rng = np.random.default_rng(seed)
    draws = {s: {k: [] for k in METRICS} for s in per_sys}
    for _ in range(N_BOOT):
        g = rng.choice(groups, len(groups))
        for s in per_sys:
            m = metrics([r for x in g for r in by[s][x]])
            for k in METRICS:
                draws[s][k].append(m[k])
    out = {}
    for s in per_sys:
        point = metrics(per_sys[s])
        ci = {k: [float(np.percentile(draws[s][k], q)) for q in (2.5, 97.5)] for k in METRICS}
        diff = {k: [float(np.percentile(np.array(draws[s][k]) - np.array(draws[ref_sys][k]), q)) for q in (2.5, 97.5)]
                for k in METRICS}
        delta = {k: point[k] - metrics(per_sys[ref_sys])[k] for k in METRICS}
        out[s] = {"point": point, "ci": ci, "delta": delta, "delta_ci": diff}
    return {"n_groups": len(groups), "n_recordings": len(per_sys[ref_sys]), "systems": out}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--system", action="append", required=True, help="name=<run dir>; the first is the reference")
    ap.add_argument("--manifest", action="append", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--jobs", type=int, default=8)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    systems = dict(s.split("=", 1) for s in args.system)
    ref_sys = next(iter(systems))

    result = {"systems": systems, "collar": 0.0, "n_boot": N_BOOT, "manifests": {}}
    md = ["# EAR-1 crowd set: per-speaker evaluation", "",
          "Collar 0. missed = reference speaker with recall < 5% under the DER mapping; absorbed = missed and "
          "≥ 50% of its solo frames covered by some hypothesis speaker (rates over all reference speakers). "
          f"[a, b] = 95% bootstrap interval over sessions ({N_BOOT} draws); Δ = paired difference vs `{ref_sys}`. "
          "Generated by eval/crowd_eval.py.", ""]
    with ProcessPoolExecutor(args.jobs) as ex:
        for man in args.manifest:
            rows = [json.loads(x) for x in man.read_text().splitlines() if x.strip()]
            per = {s: list(ex.map(partial(one, rttm_dir=Path(d) / "rttm" / man.stem), rows)) for s, d in systems.items()}
            result["manifests"][man.stem] = {}
            n_spk = sum(len(r["base"]["speakers"]) for r in per[ref_sys])
            for m in METHODS:
                b = bootstrap({s: [r[m] for r in per[s]] for s in systems}, ref_sys)
                result["manifests"][man.stem][m] = b
                md += [f"## {man.stem} — {m}", "",
                       f"{b['n_recordings']} recordings, {b['n_groups']} sessions/pairs, {n_spk} reference speakers.", "",
                       "| system | DER | miss / FA / conf | exact count | bias | missed spk | absorbed | mean recall | Δ DER | Δ missed spk | Δ recall |",
                       "|---|---|---|---|---|---|---|---|---|---|---|"]
                for s, v in b["systems"].items():
                    p, c, d, dc = v["point"], v["ci"], v["delta"], v["delta_ci"]
                    pct = lambda k: f"{100 * p[k]:.1f} [{100 * c[k][0]:.1f}, {100 * c[k][1]:.1f}]"
                    dlt = lambda k: "–" if s == ref_sys else f"{100 * d[k]:+.1f} [{100 * dc[k][0]:+.1f}, {100 * dc[k][1]:+.1f}]"
                    md.append(f"| {s} | {pct('der')} | {100 * p['miss']:.1f} / {100 * p['fa']:.1f} / {100 * p['conf']:.1f} | "
                              f"{100 * p['exact']:.0f}% | {p['bias']:+.2f} | {pct('missed_rate')} | {100 * p['absorbed_rate']:.1f} | "
                              f"{pct('mean_recall')} | {dlt('der')} | {dlt('missed_rate')} | {dlt('mean_recall')} |")
                md.append("")
    (args.out / "crowd_eval.json").write_text(json.dumps(result, indent=1))
    (args.out / "crowd_eval.md").write_text("\n".join(md))
    print("\n".join(md))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
