#!/usr/bin/env python
"""Attribute DER components (miss / false alarm / confusion; collar 0, overlap scored) to causes.

Frame-level (10 ms) with the DER speaker mapping. Per frame, with N_ref / N_hyp active speakers and
N_corr correctly mapped: miss = max(0, N_ref - N_hyp), fa = max(0, N_hyp - N_ref),
conf = min(N_ref, N_hyp) - N_corr (as in md-eval / nemo_dicobw.diar_metrics, up to 10 ms quantisation).

E1  distance of error frames to the nearest reference turn boundary (<=0.1, 0.1-0.25, 0.25-0.5, >0.5 s).
E2  oracle components: speech-activity errors (fa where no reference speech; miss where no hypothesis
    speech) that an oracle VAD would remove, vs speaker errors inside speech; oracle speaker count
    (keep the n_ref longest hypothesis speakers) -> DER change.
E3  errors by number of active reference speakers (0, 1, 2, >=3).
E4  per reference speaker frames not covered by its mapped hypothesis speaker, by the length of the
    reference turn they belong to (<1, 1-3, 3-10, >10 s): taken by another speaker vs left silent.
E5  per-recording Spearman correlation of DER and component rates with structure features (overlap
    ratio, mean turn length, speaker-time entropy, number of speakers) and an acoustic one (SNR proxy:
    frame-energy dB of reference speech minus reference silence).
E6  components under every reference type available for a condition (sessions that type covers).
Writes <results>/<run>/der_attribution.{json,md}.

Example:
    python eval/der_attribution.py --run 20261026-nemotron-zeroshot
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.stats import spearmanr

from nemo_dicobw.diar_metrics import DiarSummary, merge_speaker_turns, score_file
from nemo_dicobw.rttm import load_rttm, load_uem

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extra_speaker_analysis import CONDITIONS, corpus_of  # noqa: E402

REPO = Path(__file__).resolve().parents[1]
FR = 0.01
B_BINS = [(0, .1), (.1, .25), (.25, .5), (.5, 1e9)]
T_BINS = [(0, 1), (1, 3), (3, 10), (10, 1e9)]
REF_TYPES = ("fa", "words", "words_timedonly", "segments")


def activity(ivs, t0: float, n: int) -> np.ndarray:
    a = np.zeros(n, bool)
    for s, e in ivs:
        a[max(0, int(round((s - t0) / FR))):max(0, int(round((e - t0) / FR)))] = True
    return a


def _bin(lo: float, hi: float) -> str:
    return f">{lo}" if hi >= 1e9 else f"{lo}-{hi}"


def analyse(rec: dict, ref_t, hyp_t, uem, audio_path: str) -> dict:
    t0, t1 = uem[0][0], uem[-1][1]
    n = int(round((t1 - t0) / FR))
    keep = np.zeros(n, bool)
    for s, e in uem:
        keep[int(round((s - t0) / FR)):int(round((e - t0) / FR))] = True
    sc = score_file(ref_t, hyp_t, uem, 0.0)
    ref, hyp = merge_speaker_turns(ref_t), merge_speaker_turns(hyp_t)
    R = {k: activity(v, t0, n) & keep for k, v in ref.items()}
    H = {k: activity(v, t0, n) & keep for k, v in hyp.items()}
    nref = sum(R.values()) if R else np.zeros(n, int)
    nhyp = sum(H.values()) if H else np.zeros(n, int)
    ncorr = sum((R[r] & H[h]) for r, h in sc.mapping.items() if r in R and h in H) if sc.mapping else np.zeros(n, int)
    nref, nhyp, ncorr = (np.asarray(x, int) for x in (nref, nhyp, ncorr))
    miss, fa, conf = np.maximum(0, nref - nhyp), np.maximum(0, nhyp - nref), np.minimum(nref, nhyp) - ncorr
    out = {"ref_speech": float(nref.sum() * FR), "miss": float(miss.sum() * FR), "fa": float(fa.sum() * FR),
           "conf": float(conf.sum() * FR)}

    # E1 boundary distance
    bounds = np.array(sorted({x for t in ref_t for x in (t.start, t.end)})) if ref_t else np.array([t0])
    tt = t0 + (np.arange(n) + 0.5) * FR
    i = np.clip(np.searchsorted(bounds, tt), 1, len(bounds) - 1) if len(bounds) > 1 else np.zeros(n, int)
    dist = np.minimum(np.abs(tt - bounds[i - 1]), np.abs(tt - bounds[i])) if len(bounds) > 1 else np.abs(tt - bounds[0])
    out["E1"] = {_bin(lo, hi): {k: float(v[(dist >= lo) & (dist < hi)].sum() * FR) for k, v in
                                (("miss", miss), ("fa", fa), ("conf", conf))} for lo, hi in B_BINS}
    # E2 speech-activity vs speaker errors; oracle count
    out["E2"] = {"fa_in_silence": float(fa[nref == 0].sum() * FR), "fa_in_speech": float(fa[nref > 0].sum() * FR),
                 "miss_no_hyp": float(miss[nhyp == 0].sum() * FR), "miss_partial": float(miss[nhyp > 0].sum() * FR)}
    if sc.n_hyp_speakers > sc.n_ref_speakers:
        dur = {k: v.sum() for k, v in H.items()}
        top = set(sorted(dur, key=dur.get, reverse=True)[:sc.n_ref_speakers])
        o = score_file(ref_t, [t for t in hyp_t if t.speaker in top], uem, 0.0)
        out["E2"]["oracle_count_errors"] = float(o.miss + o.fa + o.conf)
    else:
        out["E2"]["oracle_count_errors"] = float(sc.miss + sc.fa + sc.conf)
    # E3 by number of reference speakers
    out["E3"] = {lab: {k: float(v[m].sum() * FR) for k, v in (("miss", miss), ("fa", fa), ("conf", conf))}
                 | {"ref_speech": float(nref[m].sum() * FR)}
                 for lab, m in (("0", nref == 0), ("1", nref == 1), ("2", nref == 2), (">=3", nref >= 3))}
    # E4 per reference-speaker coverage by turn length
    any_hyp = nhyp > 0
    e4 = {_bin(lo, hi): {"frames": 0, "taken_by_other": 0, "left_silent": 0} for lo, hi in T_BINS}
    for r, ivs in ref.items():
        h = H.get(sc.mapping.get(r), np.zeros(n, bool))
        for s, e in ivs:
            a, b = max(0, int(round((s - t0) / FR))), min(n, int(round((e - t0) / FR)))
            if b <= a:
                continue
            seg = slice(a, b)
            m = keep[seg] & ~h[seg]
            key = next(_bin(lo, hi) for lo, hi in T_BINS if lo <= e - s < hi)
            e4[key]["frames"] += int(keep[seg].sum())
            e4[key]["taken_by_other"] += int((m & any_hyp[seg]).sum())
            e4[key]["left_silent"] += int((m & ~any_hyp[seg]).sum())
    out["E4"] = e4
    # E5 features
    sp = nref >= 1
    turns = [e - s for ivs in ref.values() for s, e in ivs]
    air = np.array([v.sum() for v in R.values()], float)
    p = air / air.sum() if air.sum() else air
    ent = float(-(p[p > 0] * np.log(p[p > 0])).sum() / np.log(len(p))) if len(p) > 1 else 0.0
    snr = None
    try:
        x, srate = sf.read(audio_path, dtype="float32", start=int(t0 * 16000), frames=n * 160)
        m = min(len(x) // 160, n)
        en = 10 * np.log10(np.mean(x[:m * 160].reshape(m, 160) ** 2, axis=1) + 1e-10)
        if sp[:m].any() and (~sp[:m] & keep[:m]).any():
            snr = float(np.median(en[sp[:m]]) - np.median(en[~sp[:m] & keep[:m]]))
    except (RuntimeError, ValueError):
        pass
    out["E5"] = {"overlap_ratio": float((nref >= 2).sum() / max(1, sp.sum())), "mean_turn_s": float(np.mean(turns)) if turns else 0.0,
                 "speaker_entropy": ent, "n_speakers": len(ref), "snr_proxy_db": snr}
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", required=True)
    ap.add_argument("--exp", type=Path, default=Path("/mnt/data/exp/nemotron"))
    ap.add_argument("--manifests", type=Path, default=Path("/mnt/data/manifests/nemo"))
    ap.add_argument("--results", type=Path, default=REPO / "results")
    args = ap.parse_args()

    recs, e6 = [], {}
    for cond in CONDITIONS:
        rows = [json.loads(l) for l in (args.manifests / f"{cond}.jsonl").read_text().splitlines() if l.strip()]
        hyp = load_rttm(args.exp / args.run / "rttm" / cond)
        ref = load_rttm(sorted({r["rttm_filepath"] for r in rows}))
        uem = load_uem(sorted({r["uem_filepath"] for r in rows}))
        for r in rows:
            a = analyse(r, ref.get(r["session"], []), hyp.get(r["uniq_id"], []), uem[r["session"]], r["audio_filepath"])
            recs.append({"condition": cond, "corpus": corpus_of(cond), "file": r["uniq_id"], **a})
        ref_root = Path(rows[0]["rttm_filepath"]).parents[1]
        types = [t for t in REF_TYPES if (ref_root / t).is_dir()]
        if len(types) > 1:
            e6[cond] = {}
            for t in types:
                rt = load_rttm(ref_root / t)
                covered = [r for r in rows if r["session"] in rt]
                o = DiarSummary({r["uniq_id"]: score_file(rt[r["session"]], hyp.get(r["uniq_id"], []),
                                                          uem[r["session"]], 0.0) for r in covered}).overall()
                e6[cond][t] = {k: o[k] for k in ("der", "miss_rate", "fa_rate", "conf_rate", "ref_speech")} | {"n": len(covered)}
        print(f"done {cond}", flush=True)

    corpora = sorted({r["corpus"] for r in recs})

    def agg(group: list[dict]) -> dict:
        rs = sum(r["ref_speech"] for r in group)
        errs = sum(r["miss"] + r["fa"] + r["conf"] for r in group)
        o = {"n": len(group), "ref_speech_h": rs / 3600, "der": errs / rs,
             **{k: sum(r[k] for r in group) / rs for k in ("miss", "fa", "conf")}}
        o["E1"] = {b: {k: sum(r["E1"][b][k] for r in group) / errs for k in ("miss", "fa", "conf")} for b in group[0]["E1"]}
        e2 = {k: sum(r["E2"][k] for r in group) for k in group[0]["E2"]}
        o["E2"] = {"speech_activity_share": (e2["fa_in_silence"] + e2["miss_no_hyp"]) / errs,
                   "fa_in_silence": e2["fa_in_silence"] / rs, "miss_no_hyp": e2["miss_no_hyp"] / rs,
                   "fa_in_speech": e2["fa_in_speech"] / rs, "miss_partial": e2["miss_partial"] / rs,
                   "der_oracle_count": e2["oracle_count_errors"] / rs}
        o["E3"] = {b: {k: sum(r["E3"][b][k] for r in group) / rs for k in ("miss", "fa", "conf")}
                   | {"speech_share": sum(r["E3"][b]["ref_speech"] for r in group) / rs} for b in group[0]["E3"]}
        o["E4"] = {}
        for b in group[0]["E4"]:
            fr = sum(r["E4"][b]["frames"] for r in group)
            o["E4"][b] = {"ref_speaker_time_h": fr * FR / 3600,
                          "taken_by_other": sum(r["E4"][b]["taken_by_other"] for r in group) / fr if fr else None,
                          "left_silent": sum(r["E4"][b]["left_silent"] for r in group) / fr if fr else None}
        feats = ("overlap_ratio", "mean_turn_s", "speaker_entropy", "n_speakers", "snr_proxy_db")
        o["E5"] = {}
        if len(group) >= 15:
            for f in feats:
                xs = [(r["E5"][f], r) for r in group if r["E5"][f] is not None and r["ref_speech"] > 0]
                if len({x for x, _ in xs}) < 3:
                    continue
                o["E5"][f] = {m: float(spearmanr([x for x, _ in xs], [(r[m] if m != "der" else r["miss"] + r["fa"] + r["conf"]) / r["ref_speech"]
                                                                     for _, r in xs]).statistic)
                              for m in ("der", "miss", "fa", "conf")}
        return o

    out = {"run": args.run, "conditions": CONDITIONS, "all": agg(recs),
           "per_corpus": {c: agg([r for r in recs if r["corpus"] == c]) for c in corpora}, "E6": e6,
           "recordings": [{k: v for k, v in r.items() if k in ("condition", "file", "ref_speech", "miss", "fa", "conf", "E5")} for r in recs]}
    rdir = args.results / args.run
    (rdir / "der_attribution.json").write_text(json.dumps(out, indent=1) + "\n")
    (rdir / "der_attribution.md").write_text(render(out))
    print(render(out))
    return 0


def render(o: dict) -> str:
    p = lambda x: "–" if x is None else f"{100 * x:.1f}"  # noqa: E731
    sets = {"all": o["all"], **o["per_corpus"]}
    md = [f"# DER-component attribution: {o['run']}", "", "Collar 0, overlap scored, 10 ms frames, main reference per condition. "
          "Generated by eval/der_attribution.py; definitions in its docstring.", "",
          "| set | recordings | ref speech h | DER | miss | FA | conf |", "|---|---|---|---|---|---|---|"]
    md += [f"| {c} | {v['n']} | {v['ref_speech_h']:.1f} | {p(v['der'])} | {p(v['miss'])} | {p(v['fa'])} | {p(v['conf'])} |" for c, v in sets.items()]
    md += ["", "## E1 Share of all errors by distance to the nearest reference boundary (% of the set's errors: miss / FA / conf)", "",
           "| set | " + " | ".join(f"{b} s" for b in o["all"]["E1"]) + " |", "|---|" + "---|" * len(o["all"]["E1"])]
    md += [f"| {c} | " + " | ".join(f"{p(x['miss'])} / {p(x['fa'])} / {p(x['conf'])}" for x in v["E1"].values()) + " |" for c, v in sets.items()]
    md += ["", "## E2 Oracle components (% of reference speech)", "",
           "| set | DER | removable by oracle VAD (share of errors) | FA in silence | miss with no hyp speech | FA inside speech (extra spk) | miss inside speech (too few spk) | DER with oracle count |",
           "|---|---|---|---|---|---|---|---|"]
    md += [f"| {c} | {p(v['der'])} | {p(v['E2']['speech_activity_share'])} | {p(v['E2']['fa_in_silence'])} | {p(v['E2']['miss_no_hyp'])} | "
           f"{p(v['E2']['fa_in_speech'])} | {p(v['E2']['miss_partial'])} | {p(v['E2']['der_oracle_count'])} |" for c, v in sets.items()]
    md += ["", "## E3 Errors by number of active reference speakers (% of reference speech: miss / FA / conf; share of speech)", "",
           "| set | " + " | ".join(f"{b} spk" for b in o["all"]["E3"]) + " |", "|---|" + "---|" * len(o["all"]["E3"])]
    md += [f"| {c} | " + " | ".join(f"{p(x['miss'])} / {p(x['fa'])} / {p(x['conf'])} ({p(x['speech_share'])})" for x in v["E3"].values()) + " |"
           for c, v in sets.items()]
    md += ["", "## E4 Reference-speaker time not covered by its mapped speaker, by turn length (% taken by another speaker / % left silent; hours)", "",
           "| set | " + " | ".join(f"{b} s" for b in o["all"]["E4"]) + " |", "|---|" + "---|" * len(o["all"]["E4"])]
    md += [f"| {c} | " + " | ".join(f"{p(x['taken_by_other'])} / {p(x['left_silent'])} ({x['ref_speaker_time_h']:.1f} h)" for x in v["E4"].values()) + " |"
           for c, v in sets.items()]
    md += ["", "## E5 Spearman correlation across recordings (DER / miss / FA / conf rate vs feature; sets with ≥ 15 recordings)", ""]
    feats = ("overlap_ratio", "mean_turn_s", "speaker_entropy", "n_speakers", "snr_proxy_db")
    md += ["| set | " + " | ".join(feats) + " |", "|---|" + "---|" * len(feats)]
    for c, v in sets.items():
        if v["E5"]:
            md.append(f"| {c} | " + " | ".join(
                ("–" if f not in v["E5"] else " / ".join(f"{v['E5'][f][m]:+.2f}" for m in ("der", "miss", "fa", "conf"))) for f in feats) + " |")
    md += ["", "## E6 Components by reference type (DER / miss / FA / conf %)", "", "| condition | " + " | ".join(REF_TYPES) + " |",
           "|---|" + "---|" * len(REF_TYPES)]
    for c, v in o["E6"].items():
        md.append(f"| {c} | " + " | ".join(
            (f"{p(v[t]['der'])} / {p(v[t]['miss_rate'])} / {p(v[t]['fa_rate'])} / {p(v[t]['conf_rate'])} (n={v[t]['n']})" if t in v else "–") for t in REF_TYPES) + " |")
    return "\n".join(md) + "\n"


if __name__ == "__main__":
    raise SystemExit(main())
