#!/usr/bin/env python
"""Score diarization output (RTTM) against reference RTTMs.

Diarization: DER (miss / false alarm / speaker confusion, overlap scored) and JER at each
--collars value, plus speaker-count accuracy / MAE.
Segmentation (speaker-agnostic): 2x2 speech/silence confusion with intersection, union
and IoU per cell, and onset/offset boundary precision / recall / F1 / MAE / signed
displacement at each --boundary-tols tolerance.
Definitions are in src/nemo_dicobw/{diar_metrics,seg_metrics}.py.

Files are those in the UEM (if given) or in the reference; a file with no hypothesis is
scored as all-missed. Without a UEM, each file is scored from the earliest to the latest
turn over reference and hypothesis (dscore's convention, also what NeMo does when no UEM is
given); pass a full-recording UEM so leading/trailing silence counts in the speech/silence
confusion.

With --manifest (a JSONL from recipes/diarization/make_eval_manifests.py) the scored files
are the manifest's recordings (`uniq_id` = <session>__<channel>), each scored against its
session's reference and UEM. The reference and UEM default to the manifest's
`rttm_filepath` / `uem_filepath`; --ref overrides the reference (e.g. another ref type) and
--no-uem drops the UEM.

Example:
    python eval/score_diar.py --manifest $DATA/manifests/nemo/aishell5_Eval2_DX01C01.jsonl \
        --hyp $DATA/exp/nemotron/<run>/rttm/aishell5_Eval2_DX01C01 \
        --name <run>_aishell5_Eval2_DX01C01 --out results/<run>_aishell5_Eval2_DX01C01.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import subprocess
import sys
from pathlib import Path

from nemo_dicobw.diar_metrics import DiarSummary, file_score_dict, score_file
from nemo_dicobw.diar_report import to_markdown
from nemo_dicobw.rttm import Interval, Turn, load_rttm, load_uem
from nemo_dicobw.seg_metrics import (
    BoundaryCounts, boundary_counts, confusion_summary, region_confusion, speech_regions,
)

log = logging.getLogger("score_diar")


def _git_commit() -> str:
    repo = Path(__file__).resolve().parents[1]
    try:
        sha = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"], capture_output=True, text=True,
                             check=True).stdout.strip()
        dirty = subprocess.run(["git", "-C", repo, "status", "--porcelain", "--untracked-files=no"],
                               capture_output=True, text=True).stdout.strip()
        return sha + ("-dirty" if dirty else "")
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def _auto_uem(ref: list[Turn], hyp: list[Turn]) -> list[Interval]:
    turns = ref + hyp
    return [(min(t.start for t in turns), max(t.end for t in turns))] if turns else []


def score(
    ref: dict[str, list[Turn]],
    hyp: dict[str, list[Turn]],
    uem: dict[str, list[Interval]] | None,
    collars: list[float],
    tols: list[float],
    merge_gap: float,
    sessions: dict[str, str] | None = None,
) -> dict:
    """`sessions` maps scored file ids to the reference/UEM id (identity if None)."""
    if sessions is not None:
        file_ids = sorted(sessions)
    else:
        file_ids = sorted(uem) if uem is not None else sorted(ref)
        sessions = {f: f for f in file_ids}
    if missing := [f for f in file_ids if f not in hyp]:
        log.warning("%d file(s) have no hypothesis, scored as all-missed: %s", len(missing), missing[:5])
    if extra := sorted(set(hyp) - set(file_ids)):
        log.warning("%d hypothesis file(s) not in the reference/UEM, ignored: %s", len(extra), extra[:5])
    if no_ref := [f for f in file_ids if sessions[f] not in ref]:
        log.warning("%d file(s) have no reference turns: %s", len(no_ref), no_ref[:5])
    if uem is not None and (no_uem := [f for f in file_ids if sessions[f] not in uem]):
        raise KeyError(f"{len(no_uem)} file(s) have no UEM, e.g. {no_uem[:3]}")

    ckey = {c: f"{c:.2f}" for c in collars}
    tkey = {t: f"{t:.2f}" for t in tols}
    diar = {c: DiarSummary() for c in collars}
    conf_tot: dict[str, float] = {}
    bnd_tot = {t: {k: BoundaryCounts() for k in ("onset", "offset", "all")} for t in tols}
    files: dict[str, dict] = {}

    for fid in file_ids:
        r, h = ref.get(sessions[fid], []), hyp.get(fid, [])
        u = uem[sessions[fid]] if uem is not None else _auto_uem(r, h)
        out: dict = {"uem_time": sum(e - s for s, e in u), "diar": {}, "seg": {}}
        for c in collars:
            s = diar[c].files[fid] = score_file(r, h, u, c)
            out["diar"][ckey[c]] = file_score_dict(s)

        r_sp, h_sp = speech_regions(r, u, merge_gap), speech_regions(h, u, merge_gap)
        conf = region_confusion(r_sp, h_sp, u)
        for k, v in conf.items():
            conf_tot[k] = conf_tot.get(k, 0.0) + v
        out["seg"]["confusion"] = confusion_summary(conf)
        out["seg"]["boundaries"] = {}
        for t in tols:
            bc = boundary_counts(r_sp, h_sp, u, t)
            out["seg"]["boundaries"][tkey[t]] = {k: v.summary() for k, v in bc.items()}
            for k, v in bc.items():
                bnd_tot[t][k] = bnd_tot[t][k] + v
        files[fid] = out

    overall = {
        "diar": {ckey[c]: diar[c].overall() for c in collars},
        "seg": {
            "confusion": confusion_summary(conf_tot) if conf_tot else None,
            "boundaries": {tkey[t]: {k: v.summary() for k, v in bnd_tot[t].items()} for t in tols},
        },
    }
    return {"overall": overall, "files": files}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--manifest", type=Path, help="NeMo eval manifest: defines files, sessions, ref and UEM")
    ap.add_argument("--ref", nargs="+", help="reference RTTM file(s) or directories")
    ap.add_argument("--hyp", nargs="+", required=True, help="hypothesis RTTM file(s) or directories")
    ap.add_argument("--uem", nargs="+", help="UEM file(s) or directories (recommended)")
    ap.add_argument("--no-uem", action="store_true", help="ignore the manifest's UEM (score first to last turn)")
    ap.add_argument("--collars", nargs="+", type=float, default=[0.0, 0.25],
                    help="DER/JER collars in seconds (default: 0 0.25)")
    ap.add_argument("--boundary-tols", nargs="+", type=float, default=[0.25, 0.5],
                    help="boundary matching tolerances in seconds (default: 0.25 0.5)")
    ap.add_argument("--seg-merge-gap", type=float, default=0.0,
                    help="join speech regions separated by <= this many seconds before the "
                         "segmentation metrics, on both sides (default: 0)")
    ap.add_argument("--name", help="label for this scoring run")
    ap.add_argument("--meta", nargs="*", default=[], metavar="KEY=VALUE",
                    help="extra provenance stored in the JSON (checkpoint, ref_type, corpus, ...)")
    ap.add_argument("--out", type=Path, help="write results JSON here (and markdown next to it)")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    sessions = None
    if args.manifest:
        rows = [json.loads(line) for line in args.manifest.read_text().splitlines() if line.strip()]
        sessions = {r["uniq_id"]: r["session"] for r in rows}
        if not args.ref:
            args.ref = sorted({r["rttm_filepath"] for r in rows})
        if not args.uem and not args.no_uem:
            args.uem = sorted({r["uem_filepath"] for r in rows})
    if not args.ref:
        ap.error("--ref is required without --manifest")
    if args.no_uem:
        args.uem = None
    ref, hyp = load_rttm(args.ref), load_rttm(args.hyp)
    uem = load_uem(args.uem) if args.uem else None
    if uem is None:
        log.warning("no UEM given: scoring each file from its first to its last turn")

    res = score(ref, hyp, uem, args.collars, args.boundary_tols, args.seg_merge_gap, sessions)
    res["meta"] = {
        "name": args.name,
        "manifest": str(args.manifest) if args.manifest else None,
        "ref": " ".join(args.ref) if len(args.ref) <= 3 else f"{len(args.ref)} files under {Path(args.ref[0]).parent}",
        "hyp": " ".join(args.hyp),
        "uem": (" ".join(args.uem) if len(args.uem) <= 3 else f"{len(args.uem)} files under {Path(args.uem[0]).parent}")
        if args.uem else "auto (first to last turn)",
        "collars": args.collars,
        "boundary_tols": args.boundary_tols,
        "seg_merge_gap": args.seg_merge_gap,
        "git_commit": _git_commit(),
        "created": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        **dict(kv.split("=", 1) for kv in args.meta),
    }
    res = {"meta": res.pop("meta"), **res}

    md = to_markdown(res)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(res, indent=1) + "\n")
        args.out.with_suffix(".md").write_text(md)
        log.info("wrote %s and %s", args.out, args.out.with_suffix(".md"))
    sys.stdout.write(to_markdown(res, per_file=False))


if __name__ == "__main__":
    main()
