#!/usr/bin/env python
"""Speaker-count diagnostics D1–D7 for a diarization run (collar 0, overlap scored).

D1  extra (unmapped) hypothesis speakers: phantom (>50% of its speech on reference silence),
    sliver (< SLIVER_S of speech) or long split; long splits are typed by temporal coherence =
    max over t of min(share of extra ∩ r after t, share of mapped ∩ r before t), for the reference
    speaker r it overlaps most (>= 0.8: r's speech moves from the mapped to the extra speaker at t,
    a takeover; else the two interleave). Using the minimum keeps a tiny extra share from scoring high.
D2  missed reference speakers (recall < 5% under the DER mapping), fate of their solo frames as in
    arXiv 2609.27315: absorbed (another hypothesis speaker active), silence (none active),
    overlap-only (no solo frames); plus gold > 8 (model capacity).
D3  channel consistency of count outcomes across the microphones of one session (conditions with
    several channels per session).
D4  count accuracy when reference speakers with < X s of speech are ignored.
D5  per reference speaker recall and miss rate by airtime share.
D6  regime table: corpus x gold count -> exact / ±1 / bias / DER / JER.
D7  inference counterfactuals on dev: re-binarised thresholds from cached probabilities, and
    alternative streaming configurations (other run dirs).
Writes <results>/<run>/count_diagnostics.{json,md}.

Example:
    python eval/count_diagnostics.py --run 20261026-nemotron-zeroshot \
        --config-runs 20261026-nemotron-zs-cache2x 20261026-nemotron-zs-chunk2x ...
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

from nemo_dicobw.diar_metrics import DiarSummary, merge_speaker_turns, score_file
from nemo_dicobw.rttm import Turn, intersect_intervals, load_rttm, load_uem, merge_intervals

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extra_speaker_analysis import CONDITIONS, DEV, corpus_of  # noqa: E402

REPO = Path(__file__).resolve().parents[1]
SLIVER_S = 10.0
MULTI_CHANNEL = ["alimeeting_Eval_Ali_far_all", "alimeeting_Test_Ali_far_all", "aishell5_Dev_DX_all",
                 "aishell5_Eval1_DX_all", "aishell5_Eval2_DX_all", "aishell4_test_far_all", "chime6_dev_U_all",
                 "chime6_eval_U_all", "notsofar_eval_sc_all", "egocom_test_all", "egocom_val_all"]
THRESHOLDS = [0.3, 0.4, 0.5, 0.6, 0.7]


def dur(iv) -> float:
    return sum(e - s for s, e in iv)


def outcome(err: int) -> str:
    return "under" if err < 0 else "over" if err > 0 else "correct"


def load_condition(exp: Path, run: str, manifests: Path, cond: str):
    rows = [json.loads(l) for l in (manifests / f"{cond}.jsonl").read_text().splitlines() if l.strip()]
    hyp = load_rttm(exp / run / "rttm" / cond) if (exp / run / "rttm" / cond).is_dir() else {}
    ref = load_rttm(sorted({r["rttm_filepath"] for r in rows}))
    uem = load_uem(sorted({r["uem_filepath"] for r in rows}))
    return rows, hyp, ref, uem


def coherence(extra: list, mapped: list, r: list) -> tuple[float, float]:
    """Best single switch time t of r's speech from the mapped to the extra speaker:
    max_t min(share of extra∩r after t, share of mapped∩r before t)."""
    a, b = intersect_intervals(extra, r), intersect_intervals(mapped, r)
    da, db = dur(a), dur(b)
    if da == 0 or db == 0:
        return 0.0, 0.0
    best, best_t = 0.0, 0.0
    for t in sorted({t for iv in a + b for t in iv}):
        score = min(dur(intersect_intervals(a, [(t, float("inf"))])) / da,
                    dur(intersect_intervals(b, [(float("-inf"), t)])) / db)
        if score > best:
            best, best_t = score, t
    return best, best_t


def analyse_recording(cond: str, r: dict, ref_t: list, hyp_t: list, uem: list) -> dict:
    s = score_file(ref_t, hyp_t, uem, 0.0)
    ref = {k: intersect_intervals(v, uem) for k, v in merge_speaker_turns(ref_t).items()}
    hyp = {k: intersect_intervals(v, uem) for k, v in merge_speaker_turns(hyp_t).items()}
    ref = {k: v for k, v in ref.items() if dur(v) > 0}
    hyp = {k: v for k, v in hyp.items() if dur(v) > 0}
    ref_speech = merge_intervals(iv for v in ref.values() for iv in v)
    total_ref = sum(dur(v) for v in ref.values())
    rec = {"condition": cond, "corpus": corpus_of(cond), "file": r["uniq_id"], "session": r["session"],
           "channel": r["channel"], "n_ref": s.n_ref_speakers, "n_hyp": s.n_hyp_speakers,
           "err": s.n_hyp_speakers - s.n_ref_speakers, "score": s, "extras": [], "missed": [], "speakers": []}
    inv = {h: rf for rf, h in s.mapping.items()}
    for h, iv in hyp.items():  # D1
        if h in inv:
            continue
        d = dur(iv)
        on_ref = dur(intersect_intervals(iv, ref_speech)) / d
        ov = {rf: dur(intersect_intervals(iv, riv)) for rf, riv in ref.items()}
        top = max(ov, key=ov.get) if ov and max(ov.values()) > 0 else None
        kind, coh, t_switch = ("phantom", None, None) if on_ref < 0.5 else (("sliver", None, None) if d < SLIVER_S else ("long_split", None, None))
        if kind == "long_split" and top in s.mapping:
            coh, t_switch = coherence(iv, hyp[s.mapping[top]], ref[top])
            kind = "long_split_temporal" if coh >= 0.8 else "long_split_interleaved"
        rec["extras"].append({"speaker": h, "dur": d, "on_ref": on_ref, "kind": kind, "coherence": coh,
                              "t_switch": t_switch, "t_first": iv[0][0] if iv else None,
                              "rec_len": uem[-1][1] - uem[0][0]})
    hyp_any = merge_intervals(iv for v in hyp.values() for iv in v)
    for rf, iv in ref.items():  # D2, D5
        d = dur(iv)
        mapped = hyp.get(s.mapping.get(rf), [])
        recall = dur(intersect_intervals(iv, mapped)) / d
        rec["speakers"].append({"speaker": rf, "airtime": d, "share": d / total_ref if total_ref else 0.0, "recall": recall})
        if recall < 0.05:
            others = merge_intervals(x for k, v in ref.items() if k != rf for x in v)
            solo = [x for x in intersect_intervals(iv, [(uem[0][0], uem[-1][1])])]
            solo = _subtract(solo, others)
            if dur(solo) == 0:
                fate = "overlap_only"
            else:
                active = dur(intersect_intervals(solo, hyp_any)) / dur(solo)
                fate = "absorbed" if active >= 0.5 else "silence"
            rec["missed"].append({"speaker": rf, "airtime": d, "fate": fate, "beyond_capacity": s.n_ref_speakers > 8})
    return rec


def _subtract(a, b):
    from nemo_dicobw.rttm import subtract_intervals
    return subtract_intervals(a, b)


def binarize(probs: np.ndarray, thr: float, frame: float = 0.01) -> list[Turn]:
    turns = []
    for k in range(probs.shape[1]):
        on = np.r_[False, probs[:, k] > thr, False].astype(np.int8)
        d = np.flatnonzero(np.diff(on))
        turns += [Turn(f"speaker_{k}", a * frame, b * frame) for a, b in zip(d[0::2], d[1::2])]
    return turns


def group_summary(recs: list[dict]) -> dict:
    o = DiarSummary({f"{r['condition']}/{r['file']}": r["score"] for r in recs}).overall()
    errs = [r["err"] for r in recs]
    return {"n": len(recs), "exact": float(np.mean([e == 0 for e in errs])), "within1": float(np.mean([abs(e) <= 1 for e in errs])),
            "bias": float(np.mean(errs)), "der": o["der"], "jer": o["jer"]}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", required=True)
    ap.add_argument("--config-runs", nargs="*", default=[])
    ap.add_argument("--exp", type=Path, default=Path("/mnt/data/exp/nemotron"))
    ap.add_argument("--manifests", type=Path, default=Path("/mnt/data/manifests/nemo"))
    ap.add_argument("--results", type=Path, default=REPO / "results")
    args = ap.parse_args()

    recs = []
    for cond in CONDITIONS:
        rows, hyp, ref, uem = load_condition(args.exp, args.run, args.manifests, cond)
        for r in rows:
            recs.append(analyse_recording(cond, r, ref.get(r["session"], []), hyp.get(r["uniq_id"], []), uem[r["session"]]))
    out: dict = {"run": args.run, "conditions": CONDITIONS, "dev": sorted(DEV)}
    corpora = sorted({r["corpus"] for r in recs})

    # D1
    extras = [dict(e, corpus=r["corpus"], condition=r["condition"], file=r["file"]) for r in recs for e in r["extras"]]
    kinds = ["phantom", "sliver", "long_split_temporal", "long_split_interleaved", "long_split"]
    out["D1"] = {c: {k: {"n": sum(e["kind"] == k for e in extras if c in ("all", e["corpus"])),
                         "speech_s": sum(e["dur"] for e in extras if c in ("all", e["corpus"]) and e["kind"] == k)}
                     for k in kinds} for c in ["all"] + corpora}
    out["D1_long_splits"] = [{k: e[k] for k in ("corpus", "file", "dur", "coherence", "t_switch", "t_first", "rec_len")}
                             for e in extras if e["kind"].startswith("long_split")]
    # D2
    missed = [dict(m, corpus=r["corpus"], file=r["file"], n_ref=r["n_ref"]) for r in recs for m in r["missed"]]
    out["D2"] = {c: {f: sum(m["fate"] == f for m in missed if c in ("all", m["corpus"]))
                     for f in ("absorbed", "silence", "overlap_only")}
                 | {"beyond_capacity": sum(m["beyond_capacity"] for m in missed if c in ("all", m["corpus"])),
                    "airtime_median_s": float(np.median([m["airtime"] for m in missed if c in ("all", m["corpus"])] or [0]))}
                 for c in ["all"] + corpora}
    out["D2_missed"] = missed
    # D4
    out["D4"] = {}
    for x in (0, 2, 5, 10):
        def acc(rs):
            ok = [sum(sp["airtime"] >= x for sp in r["speakers"]) == r["n_hyp"] for r in rs]
            return float(np.mean(ok)) if ok else None
        out["D4"][str(x)] = {c: acc([r for r in recs if c in ("all", r["corpus"])]) for c in ["all"] + corpora}
    # D5
    bins = [(0, .02), (.02, .05), (.05, .10), (.10, .25), (.25, 1.01)]
    sp = [dict(s, corpus=r["corpus"]) for r in recs for s in r["speakers"]]
    out["D5"] = {c: [{"share": f"{lo:.0%}-{hi:.0%}" if hi <= 1 else f">{lo:.0%}",
                      "n": len(g := [s for s in sp if c in ("all", s["corpus"]) and lo <= s["share"] < hi]),
                      "mean_recall": float(np.mean([s["recall"] for s in g])) if g else None,
                      "missed_rate": float(np.mean([s["recall"] < 0.05 for s in g])) if g else None}
                     for lo, hi in bins] for c in ["all"] + corpora}
    # D6
    out["D6"] = {f"{c}/{g}": group_summary(rs) for c in corpora for g in sorted({r["n_ref"] for r in recs})
                 if (rs := [r for r in recs if r["corpus"] == c and r["n_ref"] == g])}
    out["D6"].update({f"all/{g}": group_summary([r for r in recs if r["n_ref"] == g]) for g in sorted({r["n_ref"] for r in recs})})

    # D3
    out["D3"] = {}
    for cond in MULTI_CHANNEL:
        rows, hyp, ref, uem = load_condition(args.exp, args.run, args.manifests, cond)
        if not hyp:
            continue
        by_sess = defaultdict(list)
        for r in rows:
            s = score_file(ref.get(r["session"], []), hyp.get(r["uniq_id"], []), uem[r["session"]], 0.0)
            by_sess[r["session"]].append((r["channel"], s.n_hyp_speakers - s.n_ref_speakers, s.der))
        sess = list(by_sess.values())
        n_mixed = sum(len({outcome(e) for _, e, _ in v}) > 1 for v in sess)
        per_ch = defaultdict(list)
        for v in sess:
            for ch, e, d in v:
                per_ch[ch].append(e)
        out["D3"][cond] = {
            "sessions": len(sess), "channels_per_session": float(np.mean([len(v) for v in sess])),
            "sessions_all_correct": sum(all(e == 0 for _, e, _ in v) for v in sess),
            "sessions_all_wrong": sum(all(e != 0 for _, e, _ in v) for v in sess),
            "sessions_mixed_outcome": n_mixed,
            "recording_exact": float(np.mean([e == 0 for v in sess for _, e, _ in v])),
            "per_channel_exact": {ch: float(np.mean([e == 0 for e in es])) for ch, es in sorted(per_ch.items())
                                  if not ch.startswith("sc_") and not ch.startswith("person")},
            "der_spread_median": float(np.median([max(d for *_, d in v) - min(d for *_, d in v) for v in sess])),
        }

    # D7: thresholds from cached probabilities (dev conditions)
    out["D7_threshold"] = {}
    for cond in sorted(DEV):
        rows, hyp, ref, uem = load_condition(args.exp, args.run, args.manifests, cond)
        res = {t: {} for t in THRESHOLDS}
        repro = {}
        for r in rows:
            p = np.load(args.exp / args.run / "probs" / cond / f"{r['uniq_id']}.npy").astype(np.float32)
            u, rt = uem[r["session"]], ref.get(r["session"], [])
            for t in THRESHOLDS:
                res[t][r["uniq_id"]] = score_file(rt, binarize(p, t), u, 0.0)
            repro[r["uniq_id"]] = score_file(rt, hyp.get(r["uniq_id"], []), u, 0.0)
        nemo = DiarSummary(repro).overall()
        out["D7_threshold"][cond] = {"nemo_postprocessed": {"der": nemo["der"], "spk_acc": nemo["spk_count_acc"]},
                                     **{str(t): {k: DiarSummary(v).overall()[k] for k in ("der", "spk_count_acc", "spk_count_bias", "miss_rate", "fa_rate", "conf_rate")}
                                        for t, v in res.items()}}
    # D7: streaming configurations
    out["D7_config"] = {}
    for run in [args.run] + args.config_runs:
        cfg = json.loads((args.exp / run / "config.json").read_text())["streaming"] if (args.exp / run / "config.json").exists() else None
        out["D7_config"][run] = {"streaming": cfg}
        for cond in sorted(DEV):
            rows, hyp, ref, uem = load_condition(args.exp, run, args.manifests, cond)
            if len(hyp) < len(rows):
                out["D7_config"][run][cond] = None
                continue
            o = DiarSummary({r["uniq_id"]: score_file(ref.get(r["session"], []), hyp.get(r["uniq_id"], []), uem[r["session"]], 0.0)
                             for r in rows}).overall()
            out["D7_config"][run][cond] = {k: o[k] for k in ("der", "spk_count_acc", "spk_count_bias", "miss_rate", "fa_rate", "conf_rate")}

    rdir = args.results / args.run
    (rdir / "count_diagnostics.json").write_text(json.dumps(out, indent=1, default=float) + "\n")
    (rdir / "count_diagnostics.md").write_text(render(out))
    print(render(out))
    return 0


def render(o: dict) -> str:
    p = lambda x: "–" if x is None else f"{100 * x:.1f}"  # noqa: E731
    md = [f"# Speaker-count diagnostics: {o['run']}", "", "Collar 0, overlap scored. Generated by eval/count_diagnostics.py; "
          "definitions in its docstring. Dev = " + ", ".join(o["dev"]) + ".", ""]
    md += ["## D1 Extra hypothesis speakers (count / speech s)", "",
           "| set | phantom | sliver | long split temporal | long split interleaved | long split (unmapped ref) |", "|---|---|---|---|---|---|"]
    for c, k in o["D1"].items():
        md.append(f"| {c} | " + " | ".join(f"{k[x]['n']} / {k[x]['speech_s']:.0f}" for x in
                                            ("phantom", "sliver", "long_split_temporal", "long_split_interleaved", "long_split")) + " |")
    md += ["", "Long splits (coherence, switch time / recording length): " + "; ".join(
        f"{e['corpus']} {e['dur']:.0f}s coh {e['coherence'] if e['coherence'] is None else round(e['coherence'], 2)} "
        f"t={e['t_switch'] if e['t_switch'] is None else round(e['t_switch'])}/{e['rec_len']:.0f}" for e in o["D1_long_splits"])]
    md += ["", "## D2 Missed reference speakers (recall < 5%)", "",
           "| set | absorbed | silence | overlap-only | in sessions > 8 spk | median airtime s |", "|---|---|---|---|---|---|"]
    md += [f"| {c} | {v['absorbed']} | {v['silence']} | {v['overlap_only']} | {v['beyond_capacity']} | {v['airtime_median_s']:.0f} |"
           for c, v in o["D2"].items() if sum(v[f] for f in ("absorbed", "silence", "overlap_only"))]
    md += ["", "## D3 Channel consistency of count outcomes", "",
           "| condition | sessions | ch/session | all channels correct | all wrong | mixed | recording exact % | per-channel exact % | median DER spread across channels |",
           "|---|---|---|---|---|---|---|---|---|"]
    for c, v in o["D3"].items():
        pc = ", ".join(f"{k} {100 * x:.0f}" for k, x in v["per_channel_exact"].items()) or "–"
        md.append(f"| {c} | {v['sessions']} | {v['channels_per_session']:.1f} | {v['sessions_all_correct']} | {v['sessions_all_wrong']} | "
                  f"{v['sessions_mixed_outcome']} | {p(v['recording_exact'])} | {pc} | {100 * v['der_spread_median']:.1f} |")
    md += ["", "## D4 Count accuracy ignoring reference speakers with < X s of speech (%)", "",
           "| X (s) | " + " | ".join(o["D4"]["0"]) + " |", "|---|" + "---|" * len(o["D4"]["0"])]
    md += [f"| {x} | " + " | ".join(p(v) for v in d.values()) + " |" for x, d in o["D4"].items()]
    md += ["", "## D5 Per-speaker recall by airtime share", "", "| set | " + " | ".join(b["share"] for b in o["D5"]["all"])
           + " |", "|---|" + "---|" * len(o["D5"]["all"])]
    md += [f"| {c} | " + " | ".join(f"n={b['n']}, rec {p(b['mean_recall'])}, miss {p(b['missed_rate'])}" for b in bs) + " |"
           for c, bs in o["D5"].items()]
    md += ["", "## D6 Regime table (corpus / gold speakers)", "", "| regime | n | exact % | ±1 % | bias | DER % | JER % |",
           "|---|---|---|---|---|---|---|"]
    md += [f"| {k} | {v['n']} | {p(v['exact'])} | {p(v['within1'])} | {v['bias']:+.2f} | {p(v['der'])} | {p(v['jer'])} |"
           for k, v in sorted(o["D6"].items(), key=lambda kv: (kv[0].startswith("all"), kv[0]))]
    md += ["", "## D7 Inference counterfactuals on dev", "", "### Threshold (re-binarised cached probabilities; DER % / spk acc %)", "",
           "| condition | NeMo output | " + " | ".join(f"τ={t}" for t in THRESHOLDS) + " |", "|---|---|" + "---|" * len(THRESHOLDS)]
    for c, v in o["D7_threshold"].items():
        md.append(f"| {c} | {p(v['nemo_postprocessed']['der'])} / {p(v['nemo_postprocessed']['spk_acc'])} | "
                  + " | ".join(f"{p(v[str(t)]['der'])} / {p(v[str(t)]['spk_count_acc'])}" for t in THRESHOLDS) + " |")
    md += ["", "### Streaming configuration (DER % / spk acc % / bias)", "",
           "| run | streaming | " + " | ".join(o["dev"]) + " |", "|---|---|" + "---|" * len(o["dev"])]
    for run, v in o["D7_config"].items():
        md.append(f"| {run} | {v['streaming']} | " + " | ".join(
            "pending" if v.get(c) is None else f"{p(v[c]['der'])} / {p(v[c]['spk_count_acc'])} / {v[c]['spk_count_bias']:+.2f}"
            for c in o["dev"]) + " |")
    return "\n".join(md) + "\n"


if __name__ == "__main__":
    raise SystemExit(main())
