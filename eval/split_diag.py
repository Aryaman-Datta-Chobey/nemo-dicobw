#!/usr/bin/env python
"""Over-counted ("extra") speakers on EAR-1 after the oracle-VAD fill, typed and timed against the streaming chunks.

For each system (name=<run dir with rttm/<condition>/>) and condition, every recording is analysed with
eval/crowd_eval.py one (fill_nearest_vad, optional minimum-speech filter before the fill). Each extra
hypothesis speaker (unmapped under the collar-0 DER mapping) is typed by eval/count_diagnostics.py D1:
phantom (mostly on reference silence), sliver (< 10 s), long split temporal (the reference speaker's speech
moves from the mapped to the extra speaker at one time t, coherence >= 0.8) or interleaved. For temporal
splits, t is compared with the streaming chunk grid (chunk_len x 80 ms frames; 27.2 s for the default
offline config): a cache / chunk effect would put t near a chunk boundary more often than chance.
Rows: system x view (D1 / R1 / H*), over the recordings with --gold speakers (default 4) and over all.
Writes <out>/split_diag.{json,md}.

    python eval/split_diag.py --out results/20261029-nemotron-ft-ear1-step0/split \
        --system base=$EXP/selection/base --system A-fa_s250=$EXP/selection/A-fa_s250 \
        --conditions ear1_dev_D1 ear1_dev_R1 ear1_dev_H_all
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from pathlib import Path

from crowd_eval import one

FRAME_S = 0.08


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--system", action="append", required=True, help="name=<run dir>")
    ap.add_argument("--conditions", nargs="+", default=["ear1_dev_D1", "ear1_dev_R1", "ear1_dev_H_all"])
    ap.add_argument("--manifests", type=Path, default=Path("/mnt/data/manifests/nemo"))
    ap.add_argument("--min-speech", type=float, default=0.0, help="absolute minimum-speech filter (s) before the fill")
    ap.add_argument("--gold", type=int, default=4)
    ap.add_argument("--chunk-len", type=int, default=340, help="streaming chunk length in 80 ms frames")
    ap.add_argument("--near-s", type=float, default=2.0, help="'near a chunk boundary' = within this many seconds")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--jobs", type=int, default=10)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    chunk_s = args.chunk_len * FRAME_S

    extras, recs = [], []
    with ProcessPoolExecutor(args.jobs) as ex:
        for spec in args.system:
            name, run = spec.split("=", 1)
            for cond in args.conditions:
                rows = [json.loads(x) for x in (args.manifests / f"{cond}.jsonl").read_text().splitlines() if x.strip()]
                rttm_dir = Path(run) / "rttm" / cond
                for row, r in zip(rows, ex.map(partial(one, rttm_dir=rttm_dir, min_speech=(args.min_speech, 0.0),
                                                       methods=["fill_nearest_vad"]), rows)):
                    r = r["fill_nearest_vad"]
                    recs.append({"system": name, "file": row["uniq_id"], "view": row["channel"], "n_ref": r["n_ref"],
                                 "n_hyp": r["n_hyp"]})
                    for e in r["extras"]:
                        phase = None if e["t_switch"] is None else e["t_switch"] % chunk_s
                        extras.append({"system": name, "file": row["uniq_id"], "view": row["channel"], "n_ref": r["n_ref"],
                                       **{k: e[k] for k in ("kind", "dur", "on_ref", "coherence", "t_switch", "t_first", "rec_len")},
                                       "chunk_phase": phase,
                                       "near_boundary": None if phase is None else min(phase, chunk_s - phase) <= args.near_s})

    def summary(rs: list[dict], es: list[dict]) -> dict:
        temporal = [e for e in es if e["kind"] == "long_split_temporal"]
        near = [e["near_boundary"] for e in temporal if e["near_boundary"] is not None]
        return {"recordings": len(rs), "exact": sum(r["n_hyp"] == r["n_ref"] for r in rs), "over": sum(r["n_hyp"] > r["n_ref"] for r in rs),
                "extras": len(es), "kinds": dict(Counter(e["kind"] for e in es)),
                "median_dur": sorted(e["dur"] for e in es)[len(es) // 2] if es else None,
                "switch_rel": [round(e["t_switch"] / e["rec_len"], 2) for e in temporal],
                "near_boundary": sum(near), "near_n": len(near)}

    table = {}
    for name in dict.fromkeys(r["system"] for r in recs):
        for view in sorted({r["view"] for r in recs if r["system"] == name}):
            for scope in (f"gold{args.gold}", "all"):
                keep = lambda x: x["system"] == name and x["view"] == view and (scope == "all" or x["n_ref"] == args.gold)
                table[f"{name}|{view}|{scope}"] = summary([r for r in recs if keep(r)], [e for e in extras if keep(e)])
    chance = 2 * args.near_s / chunk_s
    (args.out / "split_diag.json").write_text(json.dumps({"args": {k: str(v) for k, v in vars(args).items()}, "chunk_s": chunk_s,
                                                          "near_chance": chance, "table": table, "extras": extras}, indent=1, default=lambda o: o.item()))

    md = ["# Over-counted speakers after the oracle-VAD fill", "",
          f"Extra hypothesis speakers (unmapped, collar 0) after fill_nearest_vad, min-speech filter {args.min_speech:g} s. "
          "Kinds (eval/count_diagnostics.py D1): phantom = mostly on reference silence, sliver < 10 s, temporal = the reference "
          "speaker's speech moves to the extra speaker at one time t (coherence >= 0.8), interleaved = the two alternate. "
          f"t / len = switch time as a fraction of the recording. near chunk = temporal switches within ±{args.near_s:g} s of a "
          f"{chunk_s:.1f} s chunk boundary (chance {100 * chance:.0f}%). Generated by eval/split_diag.py.", "",
          "| system | view | scope | recordings | exact | over | extras | phantom / sliver / temporal / interleaved | median dur (s) | t / len (temporal) | near chunk |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for key, s in table.items():
        name, view, scope = key.split("|")
        k = s["kinds"]
        med = "" if s["median_dur"] is None else f"{s['median_dur']:.0f}"
        md.append(f"| {name} | {view} | {scope} | {s['recordings']} | {s['exact']} | {s['over']} | {s['extras']} | "
                  f"{k.get('phantom', 0)} / {k.get('sliver', 0)} / {k.get('long_split_temporal', 0)} / "
                  f"{k.get('long_split_interleaved', 0) + k.get('long_split', 0)} | {med} | "
                  f"{', '.join(map(str, s['switch_rel']))} | {s['near_boundary']}/{s['near_n']} |")
    md += ["", f"## Extra speakers on {args.gold}-speaker recordings", "",
           "| system | file | dur (s) | on ref | kind | coherence | t switch (s) | t first (s) | chunk phase (s) |", "|---|---|---|---|---|---|---|---|---|"]
    fmt = lambda v, f: "" if v is None else format(v, f)
    for e in extras:
        if e["n_ref"] == args.gold:
            md.append(f"| {e['system']} | {e['file']} | {e['dur']:.0f} | {e['on_ref']:.2f} | {e['kind']} | {fmt(e['coherence'], '.2f')} | "
                      f"{fmt(e['t_switch'], '.0f')} | {fmt(e['t_first'], '.0f')} | {fmt(e['chunk_phase'], '.1f')} |")
    (args.out / "split_diag.md").write_text("\n".join(md) + "\n")
    print("\n".join(md[:len(table) + 6]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
