#!/usr/bin/env python
"""tcpCER of a finished DiCoW decode under different segment timings, with its tokens unchanged (dicow env, CPU only).

The model emits no timestamps, so the recipe's tcp_wer_hyp.json gives each speaker's text the bounds of its decoding window. Here the
same text is re-timed, spread evenly in order over the speaker's speech inside each window (nemo_dicobw.timing):
    window     recipe output as is, whole window
    segments   the speaker's annotated reference segments, which are also the masks the decode used
    nemotron   Nemotron RTTM, streams mapped to reference speakers by largest total overlap. Only timing comes from Nemotron:
               the text still comes from a decode with reference masks, so this is not a Nemotron end-to-end score.
A window with no speech for the speaker falls back to the window bounds. The tcpCER references keep their own segment-level timing.

    PYTHONPATH=src python eval/tcp_timing_check.py --set dev_small=<eval dir>/4000 --set dev_full=<test dir>/5000 --out results/<run>
"""
from __future__ import annotations

import argparse
import json
import multiprocessing as mp
from collections import defaultdict
from pathlib import Path

import meeteval
import numpy as np
from meeteval.io.seglst import SegLST
from scipy.optimize import linear_sum_assignment

from nemo_dicobw.timing import text_units, to_segments, uniform_units
from nemo_dicobw.txt_norm_zh import normalize

Interval = tuple[float, float]


def merged(iv: list[Interval]) -> list[Interval]:
    out: list[list[float]] = []
    for s, e in sorted(iv):
        if out and s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return [(s, e) for s, e in out]


def rttm_path(root: Path, session: str) -> Path:
    if session.startswith("aishell5_Dev_"):
        return root / "aishell5_Dev_DX01C01" / f"{session.rsplit('_', 1)[1]}__DX01C01.rttm"
    return root / "alimeeting_Eval_Ali_far_ch1" / f"{session.removeprefix('alimeeting_Eval_')}__far_ch1.rttm"


def read_rttm(path: Path) -> dict[str, list[Interval]]:
    out: dict[str, list[Interval]] = defaultdict(list)
    for line in path.read_text().splitlines():
        p = line.split()
        out[p[7]].append((float(p[3]), float(p[3]) + float(p[4])))
    return {k: merged(v) for k, v in out.items()}


def overlap(a: list[Interval], b: list[Interval]) -> float:
    return sum(max(0.0, min(x[1], y[1]) - max(x[0], y[0])) for x in a for y in b)


def map_streams(ref: dict[str, list[Interval]], hyp: dict[str, list[Interval]]) -> dict[str, list[Interval]]:
    rs, hs = sorted(ref), sorted(hyp)
    if not hs:
        return {}
    m = np.array([[overlap(ref[r], hyp[h]) for h in hs] for r in rs])
    return {rs[i]: hyp[hs[j]] for i, j in zip(*linear_sum_assignment(-m)) if m[i, j] > 0}


def retime(segs: list[dict], speech: dict[str, list[Interval]]) -> tuple[list[dict], int]:
    out, fallback = [], 0
    for s in segs:
        lo, hi = float(s["start_time"]), float(s["end_time"])
        iv = [(max(a, lo), min(b, hi)) for a, b in speech.get(s["speaker"], []) if b > lo and a < hi]
        if not iv:
            iv, fallback = [(lo, hi)], fallback + 1
        rel = [(a - lo, b - lo) for a, b in iv]
        for x in to_segments(uniform_units(s["words"], rel), iv, s["session_id"], s["speaker"], lo):
            x["words"] = normalize(x["words"])
            out.append(x)
    return out, fallback


def score(job: tuple) -> list[dict]:
    set_name, wer_dir, rttm_root, collars = job
    ref = json.loads((wer_dir / "ref.json").read_text())
    hyp = [s for s in json.loads((wer_dir / "tcp_wer_hyp.json").read_text()) if s["words"].strip()]
    session = wer_dir.name
    by_spk: dict[str, list[Interval]] = defaultdict(list)
    for s in ref:
        by_spk[s["speaker"]].append((float(s["start_time"]), float(s["end_time"])))
    seg_speech = {k: merged(v) for k, v in by_spk.items()}
    mapped = map_streams(seg_speech, read_rttm(rttm_path(rttm_root, session)))
    timings = {"window": (hyp, 0), "segments": retime(hyp, seg_speech), "nemotron": retime(hyp, mapped)}
    rows = []
    r = SegLST(ref)
    for name, (segs, fb) in timings.items():
        h = SegLST(segs)
        cp = meeteval.wer.cpwer(reference=r, hypothesis=h)[session]
        row = {"set": set_name, "session": session, "timing": name, "fallback_windows": fb, "windows": len(hyp), "mapped_speakers": len(mapped), "ref_speakers": len(seg_speech),
               "length": cp.length, "cp_errors": cp.errors}
        for c in collars:
            t = meeteval.wer.tcpwer(reference=r, hypothesis=h, collar=c)[session]
            row[f"tcp_errors_{c:g}"], row[f"tcp_ins_{c:g}"], row[f"tcp_del_{c:g}"], row[f"tcp_sub_{c:g}"] = t.errors, t.insertions, t.deletions, t.substitutions
        rows.append(row)
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--set", action="append", required=True, help="name=decode dir holding wer/<session>/")
    ap.add_argument("--rttm-root", type=Path, default=Path("/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm"))
    ap.add_argument("--collars", type=float, nargs="+", default=[5.0, 2.0])
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    jobs = []
    for spec in args.set:
        name, d = spec.split("=", 1)
        jobs += [(name, p, args.rttm_root, args.collars) for p in sorted((Path(d) / "wer").iterdir())]
    with mp.Pool(args.jobs) as pool:
        rows = [r for rs in pool.imap(score, jobs) for r in rs]
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "metrics.json").write_text(json.dumps({"sets": args.set, "rttm_root": str(args.rttm_root), "collars": args.collars, "rows": rows}, indent=1) + "\n")
    lines = ["# tcpCER under different segment timings", "", "Same tokens in every row. cpCER moves slightly because a few decoding windows overlap, so re-timing can reorder tokens when a speaker's segments are concatenated. Generated by `eval/tcp_timing_check.py`.", ""]
    cols = "".join(f" tcpCER@{c:g} | gap@{c:g} |" for c in args.collars)
    lines += [f"| Set | Sessions | Timing | cpCER |{cols} ins / del / sub @{args.collars[0]:g} | Fallback windows |", "|" + "---|" * (6 + 2 * len(args.collars)), ]
    c0 = f"{args.collars[0]:g}"
    groups = sorted({(r["set"], g) for r in rows for g in ("all", r["session"].split("_")[0])})
    for s, g in groups:
        for t in ("window", "segments", "nemotron"):
            rr = [r for r in rows if r["set"] == s and r["timing"] == t and (g == "all" or r["session"].startswith(g))]
            n = sum(r["length"] for r in rr)
            cp = 100 * sum(r["cp_errors"] for r in rr) / n
            cells = ""
            for c in args.collars:
                v = 100 * sum(r[f"tcp_errors_{c:g}"] for r in rr) / n
                cells += f" {v:.2f} | {v - cp:+.2f} |"
            parts = " / ".join(f"{100 * sum(r[f'tcp_{k}_{c0}'] for r in rr) / n:.1f}" for k in ("ins", "del", "sub"))
            lines.append(f"| {s} | {g} ({len(rr)}) | {t} | {cp:.2f} |{cells} {parts} | {sum(r['fallback_windows'] for r in rr)} / {sum(r['windows'] for r in rr)} |")
    (args.out / "metrics.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
