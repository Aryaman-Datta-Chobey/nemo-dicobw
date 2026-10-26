#!/usr/bin/env python
"""Speaker-count error analysis over the scoring JSONs of a diarization run.

Unit: one recording (session x channel), using n_ref_speakers / n_hyp_speakers at collar 0
(speakers with speech in the scored region). Each recording is classified as under / correct /
over (hyp - ref < 0 / = 0 / > 0). Reports
    1. the over/under partition of incorrect counts, overall and per corpus;
    2. outcomes by gold participant count over the union of conditions, overall and per corpus,
       plus a session-level view (a session's recordings share its gold count: the share of a
       session's recordings in each outcome is averaged per session).
Writes <results>/<run>/spk_count_analysis.{json,md}.

Example:
    python eval/spk_count_analysis.py --run 20261026-nemotron-zeroshot
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
# Main scoring variant of each condition; notsofar_eval_sc160 is a subset of notsofar_eval_sc_all.
DEFAULT_CONDITIONS = [
    "aishell4_test_far_ch1", "aishell5_Dev_DX01C01", "aishell5_Eval1_DX01C01", "aishell5_Eval2_DX01C01",
    "alimeeting_Eval_Ali_far_ch1", "alimeeting_Test_Ali_far_ch1", "chime6_dev_U06_CH1", "chime6_eval_U06_CH1",
    "egocom_test_all", "egocom_val_all", "indic_diarbench_far_field", "notsofar_eval_sc_all",
]
OUTCOMES = ("under", "correct", "over")


def outcome(err: int) -> str:
    return "under" if err < 0 else "over" if err > 0 else "correct"


def tally(recs: list[dict]) -> dict:
    n = len(recs)
    c = {o: sum(r["outcome"] == o for r in recs) for o in OUTCOMES}
    wrong = c["under"] + c["over"]
    errs = [r["err"] for r in recs]
    return {
        "n": n, **c,
        "pct": {o: 100 * c[o] / n for o in OUTCOMES} if n else None,
        "wrong_partition_pct": {"under": 100 * c["under"] / wrong, "over": 100 * c["over"] / wrong} if wrong else None,
        "mean_err": sum(errs) / n if n else None,
        "mae": sum(map(abs, errs)) / n if n else None,
        "err_hist": {str(k): errs.count(k) for k in sorted(set(errs))},
    }


def session_tally(recs: list[dict]) -> dict:
    by_sess: dict[tuple, list[dict]] = defaultdict(list)
    for r in recs:
        by_sess[(r["condition"], r["session"])].append(r)  # session names repeat across splits (AISHELL-5)
    shares = [{o: sum(x["outcome"] == o for x in rs) / len(rs) for o in OUTCOMES} for rs in by_sess.values()]
    n = len(shares)
    return {"n_sessions": n, "pct": {o: 100 * sum(s[o] for s in shares) / n for o in OUTCOMES} if n else None}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", required=True)
    ap.add_argument("--results", type=Path, default=REPO / "results")
    ap.add_argument("--manifests", type=Path, default=Path("/mnt/data/manifests/nemo"))
    ap.add_argument("--conditions", nargs="*", default=DEFAULT_CONDITIONS)
    args = ap.parse_args()
    rdir = args.results / args.run

    recs: list[dict] = []
    for cond in args.conditions:
        res = json.loads((rdir / f"{cond}.json").read_text())
        sess = {json.loads(l)["uniq_id"]: json.loads(l)["session"]
                for l in (args.manifests / f"{cond}.jsonl").read_text().splitlines() if l.strip()}
        corpus = cond.split("_")[0] if not cond.startswith("indic") else "indic_diarbench"
        for fid, f in res["files"].items():
            d = f["diar"]["0.00"]
            err = d["n_hyp_speakers"] - d["n_ref_speakers"]
            recs.append({"condition": cond, "corpus": corpus, "file": fid, "session": sess.get(fid, fid),
                         "n_ref": d["n_ref_speakers"], "n_hyp": d["n_hyp_speakers"], "err": err,
                         "outcome": outcome(err), "der": d["der"]})

    corpora = sorted({r["corpus"] for r in recs})
    gold = sorted({r["n_ref"] for r in recs})
    out = {
        "run": args.run, "conditions": args.conditions, "unit": "recording (session x channel), collar 0",
        "overall": tally(recs),
        "per_corpus": {c: tally([r for r in recs if r["corpus"] == c]) for c in corpora},
        "by_gold": {str(g): {**tally([r for r in recs if r["n_ref"] == g]),
                             "sessions": session_tally([r for r in recs if r["n_ref"] == g]),
                             "corpora": {c: len([r for r in recs if r["n_ref"] == g and r["corpus"] == c])
                                         for c in corpora if any(r["n_ref"] == g and r["corpus"] == c for r in recs)}}
                    for g in gold},
        "by_gold_corpus": {f"{c}/{g}": tally([r for r in recs if r["corpus"] == c and r["n_ref"] == g])
                           for c in corpora for g in gold if any(r["corpus"] == c and r["n_ref"] == g for r in recs)},
        "recordings": recs,
    }
    (rdir / "spk_count_analysis.json").write_text(json.dumps(out, indent=1) + "\n")

    def row(name: str, t: dict, extra: str = "") -> str:
        p, w = t["pct"], t["wrong_partition_pct"]
        part = f"{w['under']:.0f} / {w['over']:.0f}" if w else "–"
        return (f"| {name} | {t['n']} | {t['under']} ({p['under']:.0f}%) | {t['correct']} ({p['correct']:.0f}%) | "
                f"{t['over']} ({p['over']:.0f}%) | {part} | {t['mean_err']:+.2f} | {t['mae']:.2f} |{extra}")

    head = "| {} | recordings | under | correct | over | wrong: under / over % | mean err | MAE |"
    md = [f"# Speaker-count errors: {args.run}", "",
          "Unit: recording (session x channel); gold = reference speakers with speech in the scored region, "
          "hyp = Nemotron speakers; collar 0. NOTSOFAR = all 819 single-channel recordings (contains eval-SC160). "
          "Generated by eval/spk_count_analysis.py.", "",
          "## 1. Over- vs under-counting", "", head.format("set"), "|---|---|---|---|---|---|---|---|",
          row("**all**", out["overall"])]
    md += [row(c, t) for c, t in out["per_corpus"].items()]
    md += ["", "## 2. By gold participant count (union of all conditions)", "",
           head.format("gold speakers") + " sessions | session-level under / correct / over % | corpora |",
           "|---|---|---|---|---|---|---|---|---|---|---|"]
    for g, t in out["by_gold"].items():
        sp = t["sessions"]["pct"]
        md.append(row(g, t, f" {t['sessions']['n_sessions']} | {sp['under']:.0f} / {sp['correct']:.0f} / {sp['over']:.0f} | "
                      + ", ".join(f"{c} {n}" for c, n in t["corpora"].items()) + " |"))
    md += ["", "### By corpus and gold count", "", head.format("corpus / gold"), "|---|---|---|---|---|---|---|---|"]
    md += [row(k, t) for k, t in out["by_gold_corpus"].items()]
    md += ["", "Error histogram (hyp − gold : recordings), all: "
           + ", ".join(f"{k}: {v}" for k, v in out["overall"]["err_hist"].items())]
    (rdir / "spk_count_analysis.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
