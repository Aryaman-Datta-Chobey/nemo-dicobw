#!/usr/bin/env python
"""How much speech do over-counted ("extra") hypothesis speakers carry, and where?

An extra speaker is a hypothesis speaker left unmapped by the DER speaker mapping (collar 0,
optimal one-to-one). For each one, within the UEM: total speech, share of the recording's
hypothesis speech, fraction lying on reference speech vs reference silence, and the reference
speaker it overlaps most (a "split" if that reference speaker is also mapped to another
hypothesis speaker). Missing speakers (unmapped reference speakers) are listed likewise.

Also simulates a minimum-speech-per-speaker filter: hypothesis speakers with less than T seconds
of speech in the recording (absolute), or less than a fraction R of the recording's hypothesis
speech (relative), are removed, and speaker-count accuracy and DER (collar 0) are
recomputed exactly. Dev conditions (DEV) and the rest are reported separately; choose T on dev.

Writes <results>/<run>/extra_speaker_analysis.{json,md}.

Example:
    python eval/extra_speaker_analysis.py --run 20261026-nemotron-zeroshot
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

import numpy as np

from nemo_dicobw.diar_metrics import DiarSummary, merge_speaker_turns, score_file
from nemo_dicobw.rttm import Turn, intersect_intervals, load_rttm, load_uem, merge_intervals

REPO = Path(__file__).resolve().parents[1]
CONDITIONS = [
    "aishell4_test_far_ch1", "aishell5_Dev_DX01C01", "aishell5_Eval1_DX01C01", "aishell5_Eval2_DX01C01",
    "alimeeting_Eval_Ali_far_ch1", "alimeeting_Test_Ali_far_ch1", "chime6_dev_U06_CH1", "chime6_eval_U06_CH1",
    "egocom_test_all", "egocom_val_all", "indic_diarbench_far_field", "notsofar_eval_sc_all",
    # EAR-1 ESD-ON inputs (train is zero-shot inference only, used as extra evaluation data)
    "ear1_dev_D1", "ear1_dev_R1", "ear1_train_D1", "ear1_train_R1",
]
DEV = {"aishell5_Dev_DX01C01", "alimeeting_Eval_Ali_far_ch1", "chime6_dev_U06_CH1", "egocom_val_all",
       "ear1_dev_D1", "ear1_dev_R1"}
THRESHOLDS = [("abs", t) for t in (0, 1, 2, 5, 10, 20, 30, 60)] + \
    [("rel", r) for r in (0.005, 0.01, 0.02, 0.03, 0.05, 0.08)]


def dur(iv: list[tuple[float, float]]) -> float:
    return sum(e - s for s, e in iv)


def corpus_of(cond: str) -> str:
    if cond.startswith("ear1"):  # the two ESD-ON tracks (and auxiliary mics) are reported separately
        return "ear1_" + cond.split("_")[2]
    return "indic_diarbench" if cond.startswith("indic") else cond.split("_")[0]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", required=True)
    ap.add_argument("--exp", type=Path, default=Path("/mnt/data/exp/nemotron"))
    ap.add_argument("--manifests", type=Path, default=Path("/mnt/data/manifests/nemo"))
    ap.add_argument("--results", type=Path, default=REPO / "results")
    args = ap.parse_args()

    extras, missing = [], []
    sim = {t: defaultdict(dict) for t in THRESHOLDS}  # t -> condition -> file -> FileDiarScore
    for cond in CONDITIONS:
        rows = [json.loads(l) for l in (args.manifests / f"{cond}.jsonl").read_text().splitlines() if l.strip()]
        hyp_all = load_rttm(args.exp / args.run / "rttm" / cond)
        ref_all = load_rttm(sorted({r["rttm_filepath"] for r in rows}))
        uem_all = load_uem(sorted({r["uem_filepath"] for r in rows}))
        for r in rows:
            fid, sess = r["uniq_id"], r["session"]
            ref, hyp, uem = ref_all.get(sess, []), hyp_all.get(fid, []), uem_all[sess]
            score = score_file(ref, hyp, uem, 0.0)
            ref_iv = {k: intersect_intervals(v, uem) for k, v in merge_speaker_turns(ref).items()}
            hyp_iv = {k: intersect_intervals(v, uem) for k, v in merge_speaker_turns(hyp).items()}
            ref_speech = merge_intervals(iv for v in ref_iv.values() for iv in v)
            hyp_total = dur(merge_intervals(iv for v in hyp_iv.values() for iv in v))
            mapped_hyp = set(score.mapping.values())
            inv = {h: rf for rf, h in score.mapping.items()}
            for h, iv in hyp_iv.items():
                d = dur(iv)
                if h in mapped_hyp or d == 0:
                    continue
                on_ref = dur(intersect_intervals(iv, ref_speech))
                ov = {rf: dur(intersect_intervals(iv, riv)) for rf, riv in ref_iv.items()}
                top = max(ov, key=ov.get) if ov and max(ov.values()) > 0 else None
                extras.append({
                    "condition": cond, "corpus": corpus_of(cond), "file": fid, "speaker": h,
                    "n_ref": score.n_ref_speakers, "n_hyp": score.n_hyp_speakers,
                    "dur": round(d, 2), "share_of_hyp_speech": round(d / hyp_total, 4) if hyp_total else None,
                    "frac_on_ref_speech": round(on_ref / d, 3), "n_segments": len(iv),
                    "top_ref_speaker": top, "top_ref_overlap": round(ov[top], 2) if top else 0.0,
                    "split_of_mapped": top in score.mapping if top else False,
                })
            for rf, iv in ref_iv.items():
                if rf not in score.mapping and dur(iv) > 0:
                    missing.append({"condition": cond, "corpus": corpus_of(cond), "file": fid, "speaker": rf,
                                    "dur": round(dur(iv), 2), "n_ref": score.n_ref_speakers,
                                    "n_hyp": score.n_hyp_speakers})
            hyp_dur = {h: dur(iv) for h, iv in hyp_iv.items()}
            for kind, t in THRESHOLDS:
                lim = t if kind == "abs" else t * hyp_total
                kept = [x for x in hyp if hyp_dur.get(x.speaker, 0.0) >= lim]
                sim[(kind, t)][cond][fid] = score_file(ref, kept, uem, 0.0)

    def dist(xs: list[float]) -> dict:
        a = np.array(xs)
        return {"n": len(a), "median": float(np.median(a)), "p25": float(np.percentile(a, 25)),
                "p75": float(np.percentile(a, 75)),
                **{f"lt_{t}s": float(np.mean(a < t)) for t in (2, 5, 10, 30, 60)}} if len(a) else {"n": 0}

    corpora = sorted({e["corpus"] for e in extras})
    summary = {}
    for c in ["all"] + corpora:
        es = [e for e in extras if c == "all" or e["corpus"] == c]
        tot = sum(e["dur"] for e in es)
        summary[c] = {
            "dur": dist([e["dur"] for e in es]),
            "share_of_hyp_speech_median": float(np.median([e["share_of_hyp_speech"] for e in es])) if es else None,
            "time_on_ref_speech_pct": 100 * sum(e["dur"] * e["frac_on_ref_speech"] for e in es) / tot if tot else None,
            "mostly_silence_pct": 100 * np.mean([e["frac_on_ref_speech"] < 0.5 for e in es]) if es else None,
            "split_of_mapped_pct": 100 * np.mean([e["split_of_mapped"] for e in es]) if es else None,
        }

    def sim_rows(conds: list[str]) -> list[dict]:
        out = []
        for t in THRESHOLDS:
            files = {f"{c}/{f}": s for c in conds for f, s in sim[t][c].items()}
            o = DiarSummary(files).overall()
            out.append({"threshold": f"{t[1]} s" if t[0] == "abs" else f"{100 * t[1]:g}% of speech", "der": o["der"], "spk_acc": o["spk_count_acc"],
                        "spk_mae": o["spk_count_mae"], "spk_bias": o["spk_count_bias"]})
        return out

    dev = [c for c in CONDITIONS if c in DEV]
    test = [c for c in CONDITIONS if c not in DEV]
    simulation = {"dev": sim_rows(dev), "test": sim_rows(test),
                  **{f"corpus:{c}": sim_rows([k for k in CONDITIONS if corpus_of(k) == c])
                     for c in sorted({corpus_of(k) for k in CONDITIONS})}}

    out = {"run": args.run, "conditions": CONDITIONS, "dev_conditions": dev, "summary": summary,
           "simulation": simulation, "extra_speakers": extras, "missing_speakers": missing}
    rdir = args.results / args.run
    (rdir / "extra_speaker_analysis.json").write_text(json.dumps(out, indent=1) + "\n")

    pct = lambda x: "–" if x is None else f"{100 * x:.1f}"  # noqa: E731
    md = [f"# Extra (over-counted) speakers: {args.run}", "",
          "Extra speaker = hypothesis speaker unmapped by the DER mapping (collar 0). Durations within the UEM. "
          "Generated by eval/extra_speaker_analysis.py.", "",
          "## Speech carried by extra speakers", "",
          "| set | extra spk | median s | p25–p75 s | <2 s | <5 s | <10 s | <30 s | median share of hyp speech | "
          "extra time on ref speech | mostly on silence | overlaps a mapped ref spk (split) |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for c, s in summary.items():
        d = s["dur"]
        if not d["n"]:
            continue
        md.append(f"| {c} | {d['n']} | {d['median']:.1f} | {d['p25']:.1f}–{d['p75']:.1f} | {pct(d['lt_2s'])}% | "
                  f"{pct(d['lt_5s'])}% | {pct(d['lt_10s'])}% | {pct(d['lt_30s'])}% | "
                  f"{pct(s['share_of_hyp_speech_median'])}% | {s['time_on_ref_speech_pct']:.0f}% | "
                  f"{s['mostly_silence_pct']:.0f}% | {s['split_of_mapped_pct']:.0f}% |")
    md += ["", f"Missing reference speakers (under-count side): {len(missing)}; durations (s): "
           + ", ".join(f"{m['corpus']} {m['dur']:.0f}" for m in sorted(missing, key=lambda m: m['dur']))]
    md += ["", "## Minimum-speech-per-speaker filter (simulated)", "",
           "Hypothesis speakers with less than T seconds, or less than R of the recording's hypothesis speech, "
           "removed. Choose the threshold on **dev**; test shown for reference only.", ""]
    for name, rows in simulation.items():
        md += [f"**{name}**", "", "| threshold | DER@0 | spk acc | spk MAE | spk bias |", "|---|---|---|---|---|"]
        md += [f"| {r['threshold']} | {pct(r['der'])} | {pct(r['spk_acc'])} | {r['spk_mae']:.2f} | {r['spk_bias']:+.2f} |"
               for r in rows]
        md.append("")
    (rdir / "extra_speaker_analysis.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
