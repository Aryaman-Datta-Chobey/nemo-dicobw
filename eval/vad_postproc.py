#!/usr/bin/env python
"""Oracle-VAD post-processing of diarization output (EAR-1 ESD-ON provides oracle VAD at evaluation).

The oracle VAD is the union of reference speech: for the EAR-1 training and development data the
organisers define oracle VAD as the annotated speech intervals of the per-speaker A/P*.TextGrid files
(no separate VAD files), which is exactly the union of the reference turns. Frame-level (10 ms), per recording of a manifest, collar 0, overlap
scored, the manifest's (per-channel) UEM:
    base            the diarizer's RTTM unchanged
    mask            hypothesis speech outside the VAD removed (false alarm in silence)
    fill_nearest    mask, then every VAD frame with no hypothesis speaker gets the speaker active at the
                    nearest hypothesis frame (RTTM only, so it applies to any diarizer)
    fill_nearest_vad  as fill_nearest, but the nearest speaker is searched within the same VAD region
                    first (falls back to the whole recording)
    fill_prob       mask, then VAD frames with no speaker get the speaker with the highest probability
                    (needs per-frame probabilities: Nemotron)
    thr<t>          inside the VAD binarise the probabilities at t instead of 0.5, outside nothing,
                    then fill_prob for frames still empty (t in --thresholds)
    thr<t>_ovl<u>   as thr<t>, plus the second most probable speaker wherever its probability >= u
                    (more overlap)
    *_med<k>        median filter of k frames on each speaker track before the steps above
Probabilities: <probs dir>/<uniq_id>.npy, (frames, 8), column k = speaker_k (recipes/diarization/nemotron_infer.py).
Writes <out>/<name>.json (per method x condition: DER, miss, FA, conf, speaker-count acc) and summary.md.

    python eval/vad_postproc.py --name nemotron --rttm-root $RUN/rttm --probs-root $RUN/probs \
        --conditions ear1_dev_D1 ear1_dev_R1 ear1_train_D1 ear1_train_R1 --out results/20261027-ear1-vad-postproc
"""
from __future__ import annotations

import argparse
import json
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from pathlib import Path

import numpy as np
from scipy.ndimage import median_filter

from nemo_dicobw.diar_metrics import DiarSummary, score_file
from nemo_dicobw.rttm import Turn, load_rttm, load_uem, merge_intervals

FR = 100  # frames per second


def to_frames(turns: list[Turn], n: int, labels: list[str]) -> np.ndarray:
    a = np.zeros((len(labels), n), bool)
    idx = {s: i for i, s in enumerate(labels)}
    for t in turns:
        a[idx[t.speaker], max(0, int(round(t.start * FR))):min(n, int(round(t.end * FR)))] = True
    return a


def to_turns(a: np.ndarray, labels: list[str]) -> list[Turn]:
    out = []
    for i, s in enumerate(labels):
        d = np.diff(np.r_[0, a[i].astype(np.int8), 0])
        out += [Turn(s, b / FR, e / FR) for b, e in zip(np.flatnonzero(d == 1), np.flatnonzero(d == -1))]
    return out


def nearest_fill(a: np.ndarray, vad: np.ndarray, within_region: bool) -> np.ndarray:
    """Give every empty VAD frame the speaker(s) active at the nearest non-empty frame."""
    a = a.copy()
    active = a.any(0)
    n = a.shape[1]
    idx = np.flatnonzero(active)
    if not len(idx):
        return a
    empty = np.flatnonzero(vad & ~active)
    if within_region:
        d = np.diff(np.r_[0, vad.astype(np.int8), 0])
        for b, e in zip(np.flatnonzero(d == 1), np.flatnonzero(d == -1)):
            inside = idx[(idx >= b) & (idx < e)]
            if not len(inside):
                continue
            fr = np.arange(b, e)
            fr = fr[~active[b:e]]
            pos = np.clip(np.searchsorted(inside, fr), 1, len(inside) - 1) if len(inside) > 1 else np.zeros(len(fr), int)
            left, right = inside[np.maximum(pos - 1, 0)], inside[pos]
            src = np.where(np.abs(fr - left) <= np.abs(right - fr), left, right)
            a[:, fr] = a[:, src]
        empty = np.flatnonzero(vad & ~a.any(0))
    if len(empty):
        pos = np.clip(np.searchsorted(idx, empty), 1, max(1, len(idx) - 1))
        left, right = idx[np.maximum(pos - 1, 0)], idx[np.minimum(pos, len(idx) - 1)]
        src = np.where(np.abs(empty - left) <= np.abs(right - empty), left, right)
        a[:, empty] = a[:, src]
    return a & vad[None, :] if n else a


def methods(has_probs: bool, thresholds: list[float], ovl: list[float], meds: list[int]) -> list[str]:
    m = ["base", "mask", "fill_nearest", "fill_nearest_vad"]
    if has_probs:
        m.append("fill_prob")
        for k in [0] + meds:
            sfx = f"_med{k}" if k else ""
            m += [f"thr{t}{sfx}" for t in thresholds]
            m += [f"thr{t}_ovl{u}{sfx}" for t in thresholds for u in ovl]
    return m


def apply(method: str, hyp: np.ndarray, probs: np.ndarray | None, vad: np.ndarray) -> np.ndarray:
    if method == "base":
        return hyp
    if method == "mask":
        return hyp & vad
    if method.startswith("fill_nearest"):
        return nearest_fill(hyp & vad, vad, method.endswith("_vad"))
    p = probs.T  # (8, frames)
    if method == "fill_prob":
        a = hyp & vad
    else:
        parts = method.split("_")
        med = next((int(x[3:]) for x in parts if x.startswith("med")), 0)
        if med:
            p = median_filter(p, size=(1, med))
        t = float(parts[0][3:])
        a = (p >= t) & vad
        ov = next((float(x[3:]) for x in parts if x.startswith("ovl")), None)
        if ov is not None:
            second = np.argsort(-p, axis=0)[1]
            add = np.zeros_like(a)
            add[second, np.arange(p.shape[1])] = p[second, np.arange(p.shape[1])] >= ov
            a |= add & vad
    empty = vad & ~a.any(0)
    a[np.argmax(p, axis=0)[empty], np.flatnonzero(empty)] = True
    return a


def one(row: dict, rttm_dir: Path, probs_dir: Path | None, ms: list[str]) -> dict[str, tuple]:
    uid, sess = row["uniq_id"], row["session"]
    ref = load_rttm([Path(row["rttm_filepath"])]).get(sess, [])
    uem = load_uem([Path(row["uem_filepath"])])[sess]
    n = int(round(row["duration"] * FR))
    hyp_turns = load_rttm([rttm_dir / f"{uid}.rttm"]).get(uid, []) if (rttm_dir / f"{uid}.rttm").exists() else []
    probs = None
    if probs_dir is not None:
        probs = np.load(probs_dir / f"{uid}.npy").astype(np.float32)[:n]
        if len(probs) < n:
            probs = np.pad(probs, ((0, n - len(probs)), (0, 0)))
        labels = [f"speaker_{k}" for k in range(probs.shape[1])]
    else:
        labels = sorted({t.speaker for t in hyp_turns}) or ["spk"]
    hyp = to_frames(hyp_turns, n, labels)
    vad = np.zeros(n, bool)
    for s, e in merge_intervals((t.start, t.end) for t in ref):
        vad[int(round(s * FR)):int(round(e * FR))] = True
    res = {}
    for m in ms:
        out_turns = to_turns(apply(m, hyp, probs, vad), labels)
        s = score_file(ref, out_turns, uem, 0.0)
        res[m] = s
    return {"uid": uid, "scores": res}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", required=True)
    ap.add_argument("--rttm-root", type=Path, required=True, help="<root>/<condition>/<uniq_id>.rttm")
    ap.add_argument("--probs-root", type=Path, help="<root>/<condition>/<uniq_id>.npy (optional)")
    ap.add_argument("--conditions", nargs="+", required=True)
    ap.add_argument("--manifests", type=Path, default=Path("/mnt/data/manifests/nemo"))
    ap.add_argument("--thresholds", nargs="*", type=float, default=[0.2, 0.3, 0.4, 0.5])
    ap.add_argument("--ovl", nargs="*", type=float, default=[0.2, 0.3])
    ap.add_argument("--med", nargs="*", type=int, default=[11])
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--jobs", type=int, default=8)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    ms = methods(args.probs_root is not None, args.thresholds, args.ovl, args.med)
    result: dict = {"name": args.name, "oracle_vad": "union of reference speech", "methods": ms, "conditions": {}}
    with ProcessPoolExecutor(args.jobs) as ex:
        for cond in args.conditions:
            rows = [json.loads(x) for x in (args.manifests / f"{cond}.jsonl").read_text().splitlines() if x.strip()]
            fn = partial(one, rttm_dir=args.rttm_root / cond,
                         probs_dir=(args.probs_root / cond) if args.probs_root else None, ms=ms)
            per = list(ex.map(fn, rows))
            result["conditions"][cond] = {}
            for m in ms:
                summ = DiarSummary({p["uid"]: p["scores"][m] for p in per})
                o = summ.overall()
                result["conditions"][cond][m] = {k: o[k] for k in ("der", "miss_rate", "fa_rate", "conf_rate", "spk_count_acc")}
            b = result["conditions"][cond]["base"]["der"]
            best = min(ms, key=lambda m: result["conditions"][cond][m]["der"])
            print(f"{args.name} {cond}: base {100 * b:.2f} -> best {best} {100 * result['conditions'][cond][best]['der']:.2f}", flush=True)
    (args.out / f"{args.name}.json").write_text(json.dumps(result, indent=1))
    md = [f"# Oracle-VAD post-processing: {args.name}", "",
          "DER % (miss / FA / conf), collar 0, overlap scored, per-channel UEM; oracle VAD = union of reference speech "
          "(the organisers' definition for EAR-1 train/dev). "
          "Generated by eval/vad_postproc.py.", "",
          "| method | " + " | ".join(args.conditions) + " |", "|---|" + "---|" * len(args.conditions)]
    for m in ms:
        cells = []
        for c in args.conditions:
            r = result["conditions"][c][m]
            cells.append(f"{100 * r['der']:.2f} ({100 * r['miss_rate']:.1f} / {100 * r['fa_rate']:.1f} / {100 * r['conf_rate']:.1f})")
        md.append(f"| {m} | " + " | ".join(cells) + " |")
    (args.out / f"{args.name}.md").write_text("\n".join(md) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
