#!/usr/bin/env python
"""Conversation-structure statistics of SegLST transcript references, per session and per corpus.

Per session (reference segments; tokens = nemo_dicobw.txt_norm_zh tokens: Han characters, English words):
    n_spk, dur_min                 speakers, minutes from the first segment start to the last end
    speech_pct                     union of speech over that span
    overlap_pct, overlap3_pct      speech time with >= 2 / >= 3 active speakers, % of speech time
    seg_per_min, seg_dur_med/p90   annotation segments (corpus segmentation convention)
    turn_per_min, turn_dur_med     turns = same-speaker segments merged across gaps <= 0.5 s
                                   (less sensitive to segmentation conventions)
    fto_med, fto_overlap_pct,      floor-transfer offsets between consecutive turns of different speakers:
    fto_gap1s_pct                  median (s), % overlapping (< 0), % gaps > 1 s
    interrupt_per_min              turns starting inside another speaker's turn that continues past their end
    bc_pct, bc_per_min,            backchannel segments (<= 2 tokens, all acknowledgement/filler characters):
    bc_inside_pct                  % of segments, per minute, % of them inside another speaker's turn
    tok_per_s                      median speaking rate of segments >= 1 s (tokens per second)
    filler_per_100                 filler characters (嗯啊呃额哦噢唔) per 100 tokens
    dominance_top_pct, spk_entropy share of speech time of the most active speaker; normalised entropy
    latin_pct, digit_seg_pct,      Latin-script tokens (code-switching), % of segments with digits,
    punct_seg_pct                  % of segments with punctuation (transcription conventions)
Writes <out>/<name>.jsonl and <out>/summary.md (median [IQR] over sessions per set; with --target, the
z-scored distance between set medians).

    python eval/conversation_stats.py --out results/20261027-conversation-stats \
        alimeeting_Eval=/mnt/data/refs/alimeeting/Eval_Ali/seglst aishell4_test=/mnt/data/refs/aishell4/test/seglst
"""
from __future__ import annotations

import argparse
import json
import math
import re
import unicodedata
from pathlib import Path

import numpy as np

from nemo_dicobw.txt_norm_zh import normalize

BACKCHANNEL = set("嗯啊哦噢喔呃额对是好行哎唉诶欸哈呵唔恩嘛吧呀")
FILLER = set("嗯啊呃额哦噢唔")
FEATURES = ("n_spk", "dur_min", "speech_pct", "overlap_pct", "overlap3_pct", "seg_per_min", "seg_dur_med",
            "seg_dur_p90", "turn_per_min", "turn_dur_med", "fto_med", "fto_overlap_pct", "fto_gap1s_pct",
            "interrupt_per_min", "bc_pct", "bc_per_min", "bc_inside_pct", "tok_per_s", "filler_per_100",
            "dominance_top_pct", "spk_entropy", "latin_pct", "digit_seg_pct", "punct_seg_pct")
DISTANCE_KEYS = [k for k in FEATURES if k not in ("dur_min", "digit_seg_pct", "punct_seg_pct")]


def coverage(segs: list[dict], t0: float, t1: float, step: float = 0.01) -> np.ndarray:
    n = int(math.ceil((t1 - t0) / step))
    count = np.zeros(n, np.int16)
    for s in segs:
        count[int((s["start_time"] - t0) / step):int(math.ceil((s["end_time"] - t0) / step))] += 1
    return count


def turns(segs: list[dict], gap: float = 0.5) -> list[tuple[str, float, float]]:
    out: dict[str, list[list]] = {}
    for s in sorted(segs, key=lambda x: x["start_time"]):
        lst = out.setdefault(s["speaker"], [])
        if lst and s["start_time"] - lst[-1][2] <= gap:
            lst[-1][2] = max(lst[-1][2], s["end_time"])
        else:
            lst.append([s["speaker"], s["start_time"], s["end_time"]])
    return sorted((tuple(t) for v in out.values() for t in v), key=lambda t: t[1])


def session_stats(segs: list[dict]) -> dict:
    segs = [s for s in segs if s["end_time"] > s["start_time"]]
    t0, t1 = min(s["start_time"] for s in segs), max(s["end_time"] for s in segs)
    mins = (t1 - t0) / 60
    cov = coverage(segs, t0, t1)
    speech = (cov > 0).sum()
    toks = [normalize(s["words"]).split() for s in segs]
    dur = np.array([s["end_time"] - s["start_time"] for s in segs])
    tr = turns(segs)
    fto, interrupts = [], 0
    for a, b in zip(tr, tr[1:]):
        if a[0] != b[0]:
            fto.append(b[1] - a[2])
    for i, (spk, s, e) in enumerate(tr):  # starts inside another speaker's still-running turn
        if any(o[0] != spk and o[1] < s and o[2] > e for o in tr[max(0, i - 20):i]):
            interrupts += 0  # contained (backchannel-like), not an interruption
        elif any(o[0] != spk and o[1] < s < o[2] for o in tr[max(0, i - 20):i]):
            interrupts += 1
    bc = [i for i, t in enumerate(toks) if 0 < len(t) <= 2 and all(x in BACKCHANNEL for x in t)]
    inside = sum(any(o[0] != segs[i]["speaker"] and o[1] <= segs[i]["start_time"] and o[2] >= segs[i]["end_time"]
                     for o in tr) for i in bc)
    spk_time: dict[str, float] = {}
    for s in segs:
        spk_time[s["speaker"]] = spk_time.get(s["speaker"], 0.0) + s["end_time"] - s["start_time"]
    share = np.array(list(spk_time.values())) / sum(spk_time.values())
    all_toks = [x for t in toks for x in t]
    rate = [len(t) / d for t, d in zip(toks, dur) if d >= 1 and t]
    pct = lambda a, b: 100 * a / b if b else math.nan  # noqa: E731
    return {
        "n_spk": len(spk_time), "dur_min": mins, "speech_pct": pct(speech, len(cov)),
        "overlap_pct": pct((cov > 1).sum(), speech), "overlap3_pct": pct((cov > 2).sum(), speech),
        "seg_per_min": len(segs) / mins, "seg_dur_med": float(np.median(dur)), "seg_dur_p90": float(np.percentile(dur, 90)),
        "turn_per_min": len(tr) / mins, "turn_dur_med": float(np.median([e - s for _, s, e in tr])),
        "fto_med": float(np.median(fto)) if fto else math.nan,
        "fto_overlap_pct": pct(sum(f < 0 for f in fto), len(fto)), "fto_gap1s_pct": pct(sum(f > 1 for f in fto), len(fto)),
        "interrupt_per_min": interrupts / mins,
        "bc_pct": pct(len(bc), len(segs)), "bc_per_min": len(bc) / mins, "bc_inside_pct": pct(inside, len(bc)),
        "tok_per_s": float(np.median(rate)) if rate else math.nan,
        "filler_per_100": pct(sum(x in FILLER for x in all_toks), len(all_toks)),
        "dominance_top_pct": 100 * float(share.max()),
        "spk_entropy": float(-(share * np.log(share)).sum() / math.log(len(share))) if len(share) > 1 else math.nan,
        "latin_pct": pct(sum(x.isascii() and x.isalpha() for x in all_toks), len(all_toks)),
        "digit_seg_pct": pct(sum(bool(re.search(r"\d", s["words"])) for s in segs), len(segs)),
        "punct_seg_pct": pct(sum(any(unicodedata.category(c).startswith("P") for c in s["words"]) for s in segs), len(segs)),
    }


def table(rows: dict[str, list[dict]], targets: list[str]) -> str:
    md = ["# Conversation-structure statistics of transcript references", "",
          "Median [IQR] over sessions. Generated by eval/conversation_stats.py.", "",
          "| set | sessions | " + " | ".join(FEATURES) + " |", "|---|---|" + "---|" * len(FEATURES)]
    med: dict[str, dict[str, float]] = {}
    for name, rs in rows.items():
        cells, med[name] = [], {}
        for k in FEATURES:
            v = np.array([r[k] for r in rs], float)
            v = v[~np.isnan(v)]
            med[name][k] = float(np.median(v)) if len(v) else math.nan
            cells.append(f"{np.median(v):.2f} [{np.percentile(v, 25):.2f}, {np.percentile(v, 75):.2f}]" if len(v) else "–")
        md.append(f"| {name} | {len(rs)} | " + " | ".join(cells) + " |")
    if targets:
        sd = {k: float(np.nanstd([r[k] for rs in rows.values() for r in rs])) or 1.0 for k in DISTANCE_KEYS}
        md += ["", "## Distance to targets", "",
               f"RMS of z-scored differences of set medians over {', '.join(DISTANCE_KEYS)}.", "",
               "| set | " + " | ".join(targets) + " |", "|---|" + "---|" * len(targets)]
        for name in rows:
            cells = []
            for t in targets:
                z = [(med[name][k] - med[t][k]) / sd[k] for k in DISTANCE_KEYS
                     if not (math.isnan(med[name][k]) or math.isnan(med[t][k]))]
                cells.append(f"{math.sqrt(np.mean(np.square(z))):.2f}")
            md.append(f"| {name} | " + " | ".join(cells) + " |")
    return "\n".join(md) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sets", nargs="+", help="<name>=<seglst dir>")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--target", nargs="*", default=[], help="set names to measure distances to")
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    rows = {}
    for spec in args.sets:
        name, d = spec.split("=", 1)
        rows[name] = []
        for f in sorted(Path(d).glob("*.json")):
            r = session_stats(json.loads(f.read_text()))
            rows[name].append({"session": f.stem, **{k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()}})
        (args.out / f"{name}.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows[name]))
        print(f"{name}: {len(rows[name])} sessions", flush=True)
    (args.out / "summary.md").write_text(table(rows, args.target))
    print(f"wrote {args.out / 'summary.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
