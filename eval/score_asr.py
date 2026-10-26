#!/usr/bin/env python
"""Score multi-speaker Mandarin ASR output (SegLST) against SegLST references.

Both sides are normalised with nemo_dicobw.txt_norm_zh (CJK characters become tokens, English words
stay whole), so meeteval's word-level metrics are CER here. Reported:
    ORC-CER  speaker-agnostic: each reference utterance assigned to its best hypothesis stream
             (one stream for whole-audio runs, one per diarized speaker for per-speaker runs).
             Exact search for single-stream hypotheses; meeteval's greedy ORC when any session has
             several streams (exact ORC is impractical for 4-8 streams over hour-long sessions)
    cpCER    concatenated minimum-permutation CER (speaker-attributed)
    tcpCER   time-constrained cpCER (collar --collar s; hypothesis timing from segment boundaries)
    per-speaker CER for every (reference speaker, hypothesis stream) pair of the cpCER assignment
    each with its substitution / deletion / insertion rates (counts / reference length, summing to
    the CER)
    gaps: cpCER - ORC-CER (speaker attribution), tcpCER - cpCER (timing)
    LID / non-Mandarin tracing on the raw hypothesis text: per segment script composition (Han,
    traditional Han, Latin, kana, other), English-dominant segments, empty segments and repetition
    loops (an n-gram, n = 1..8, repeated >= 4 times in a row).

The hypothesis SegLST must use the reference session ids; sessions without any hypothesis segment
are scored as all deleted. Writes <out>.json and <out>.md.

Example:
    python eval/score_asr.py --ref /mnt/data/refs/alimeeting/Eval_Ali/seglst \
        --hyp $DATA/exp/asr/<run>/<condition>.seglst.json --name <run>/<condition> --out results/<run>/<condition>.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

import meeteval
from meeteval.io.seglst import SegLST
from meeteval.wer.wer.error_rate import combine_error_rates
from meeteval.wer.wer.siso import siso_word_error_rate

from nemo_dicobw.txt_norm_zh import _t2s, normalize

_HAN = re.compile(r"[㐀-䶿一-鿿豈-﫿]")
_KANA = re.compile(r"[぀-ヿ]")
_LATIN = re.compile(r"[A-Za-z]")
_WORD = re.compile(r"[A-Za-z]+")


def load_seglst(paths: list[Path]) -> list[dict]:
    segs = []
    for p in paths:
        files = sorted(p.glob("*.json")) if p.is_dir() else [p]
        for f in files:
            segs += json.loads(f.read_text())
    return segs


def repetition_loop(text: str) -> bool:
    toks = normalize(text).split()
    for n in range(1, 9):
        for i in range(0, max(0, len(toks) - 4 * n + 1)):
            g = toks[i:i + n]
            if all(toks[i + k * n:i + (k + 1) * n] == g for k in range(1, 4)):
                return True
    return False


def lid_trace(hyp: list[dict]) -> dict:
    c, examples = Counter(), defaultdict(list)
    for s in hyp:
        raw = s.get("words", "")
        han = _HAN.findall(raw)
        trad = sum(ch != _t2s().convert(ch) for ch in han)
        latin = len(_LATIN.findall(raw))
        kana = len(_KANA.findall(raw))
        c["segments"] += 1
        c["han_chars"] += len(han)
        c["traditional_chars"] += trad
        c["latin_letters"] += latin
        c["kana_chars"] += kana
        kind = None
        if not normalize(raw):
            kind = "empty"
        elif kana:
            kind = "kana"
        elif latin > 2 * len(han) and len(_WORD.findall(raw)) >= 2:
            kind = "english_dominant"
        elif trad and trad >= 0.5 * len(han):
            kind = "traditional"
        if kind:
            c[f"seg_{kind}"] += 1
            if len(examples[kind]) < 5:
                examples[kind].append({k: s.get(k) for k in ("session_id", "speaker", "start_time", "end_time", "words")})
        if repetition_loop(raw):
            c["seg_repetition_loop"] += 1
            if len(examples["repetition_loop"]) < 5:
                examples["repetition_loop"].append({k: s.get(k) for k in ("session_id", "speaker", "start_time", "words")})
    n = max(1, c["segments"])
    rates = {k: c[k] / n for k in c if k.startswith("seg_")}
    return {"counts": dict(c), "segment_rates": rates,
            "traditional_char_rate": c["traditional_chars"] / max(1, c["han_chars"]), "examples": dict(examples)}


def er_dict(e) -> dict:
    n = max(1, e.length)
    return {"error_rate": e.error_rate, "errors": e.errors, "length": e.length, "insertions": e.insertions,
            "deletions": e.deletions, "substitutions": e.substitutions, "sub_rate": e.substitutions / n,
            "del_rate": e.deletions / n, "ins_rate": e.insertions / n}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ref", nargs="+", type=Path, required=True, help="reference SegLST files or directories")
    ap.add_argument("--hyp", nargs="+", type=Path, required=True, help="hypothesis SegLST files or directories")
    ap.add_argument("--sessions", nargs="*", help="score only these sessions (default: all reference sessions)")
    ap.add_argument("--collar", type=float, default=5.0)
    ap.add_argument("--name")
    ap.add_argument("--meta", nargs="*", default=[], metavar="KEY=VALUE")
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    ref_raw, hyp_raw = load_seglst(args.ref), load_seglst(args.hyp)
    sessions = sorted(set(args.sessions) if args.sessions else {s["session_id"] for s in ref_raw})
    ref_raw = [s for s in ref_raw if s["session_id"] in sessions]
    hyp_raw = [s for s in hyp_raw if s["session_id"] in sessions]
    missing = sorted(set(sessions) - {s["session_id"] for s in hyp_raw})
    if missing:
        print(f"WARNING: {len(missing)} session(s) without hypothesis, scored as all deleted: {missing[:5]}", file=sys.stderr)

    def norm(segs: list[dict]) -> list[dict]:
        out = []
        for s in segs:
            w = normalize(s.get("words", ""))
            if w:
                out.append({k: s[k] for k in ("session_id", "speaker", "start_time", "end_time")} | {"words": w})
        return out

    ref, hyp = norm(ref_raw), norm(hyp_raw)
    hyp += [{"session_id": m, "speaker": "<none>", "start_time": 0.0, "end_time": 0.0, "words": ""} for m in missing]
    R, H = SegLST(ref), SegLST(hyp)
    multi_stream = any(len({s["speaker"] for s in hyp if s["session_id"] == m}) > 1 for m in sessions)
    orc = (meeteval.wer.greedy_orcwer if multi_stream else meeteval.wer.orcwer)(R, H)
    cp = meeteval.wer.cpwer(R, H)
    tcp = meeteval.wer.tcpwer(R, H, collar=args.collar)

    per_speaker, files = [], {}
    for sess in sessions:
        rs = defaultdict(list)
        hs = defaultdict(list)
        for s in sorted((x for x in ref if x["session_id"] == sess), key=lambda x: x["start_time"]):
            rs[s["speaker"]].append(s["words"])
        for s in sorted((x for x in hyp if x["session_id"] == sess), key=lambda x: x["start_time"]):
            hs[s["speaker"]].append(s["words"])
        for r_spk, h_spk in cp[sess].assignment:
            rt, ht = " ".join(rs.get(r_spk, [])), " ".join(hs.get(h_spk, []))
            e = siso_word_error_rate(rt, ht)
            per_speaker.append({"session": sess, "ref_speaker": r_spk, "hyp_stream": h_spk, **er_dict(e)})
        files[sess] = {"orc": er_dict(orc[sess]), "cp": er_dict(cp[sess]), "tcp": er_dict(tcp[sess]),
                       "missed_speaker": cp[sess].missed_speaker, "falarm_speaker": cp[sess].falarm_speaker}

    O, C, T = (combine_error_rates(*x.values()) for x in (orc, cp, tcp))
    paired = [p for p in per_speaker if p["ref_speaker"] is not None and p["hyp_stream"] is not None]
    res = {
        "meta": {"name": args.name, "ref": [str(p) for p in args.ref], "hyp": [str(p) for p in args.hyp],
                 "collar": args.collar, "normaliser": "nemo_dicobw.txt_norm_zh", "n_sessions": len(sessions),
                 "orc": "greedy" if multi_stream else "exact",
                 "created": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                 "git_commit": subprocess.run(["git", "-C", str(Path(__file__).resolve().parents[1]), "rev-parse", "HEAD"],
                                              capture_output=True, text=True).stdout.strip(),
                 **dict(kv.split("=", 1) for kv in args.meta)},
        "overall": {"orc_cer": er_dict(O), "cp_cer": er_dict(C), "tcp_cer": er_dict(T),
                    "gap_attribution": C.error_rate - O.error_rate, "gap_timing": T.error_rate - C.error_rate,
                    "per_speaker_cer": {"n_pairs": len(paired),
                                        "pooled": sum(p["errors"] for p in paired) / max(1, sum(p["length"] for p in paired)),
                                        **{f"{short}_rate": sum(p[k] for p in paired) / max(1, sum(p["length"] for p in paired))
                                           for k, short in (("substitutions", "sub"), ("deletions", "del"), ("insertions", "ins"))},
                                        "missed_ref_speakers": sum(p["hyp_stream"] is None for p in per_speaker),
                                        "extra_hyp_streams": sum(p["ref_speaker"] is None for p in per_speaker)},
                    "lid": lid_trace(hyp_raw)},
        "per_speaker": per_speaker,
        "files": files,
    }
    md = render(res)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n")
        args.out.with_suffix(".md").write_text(md)
    print(md)
    return 0


def render(res: dict) -> str:
    o = res["overall"]
    p = lambda x: f"{100 * x:.2f}"  # noqa: E731
    f = lambda e: f"{p(e['error_rate'])} | {p(e['sub_rate'])} | {p(e['del_rate'])} | {p(e['ins_rate'])}"  # noqa: E731
    lid = o["lid"]
    md = [f"# ASR scores: {res['meta']['name']}", "", *[f"- {k}: `{v}`" for k, v in res["meta"].items()], "",
          "| metric | CER % | sub % | del % | ins % |", "|---|---|---|---|---|",
          f"| ORC-CER (speaker-agnostic) | {f(o['orc_cer'])} |", f"| cpCER | {f(o['cp_cer'])} |",
          f"| tcpCER (collar {res['meta']['collar']} s) | {f(o['tcp_cer'])} |",
          f"| per-speaker CER, pooled over {o['per_speaker_cer']['n_pairs']} pairs | {p(o['per_speaker_cer']['pooled'])} | "
          f"{p(o['per_speaker_cer']['sub_rate'])} | {p(o['per_speaker_cer']['del_rate'])} | {p(o['per_speaker_cer']['ins_rate'])} |",
          f"| cpCER − ORC-CER (attribution) | {p(o['gap_attribution'])} | | | |", f"| tcpCER − cpCER (timing) | {p(o['gap_timing'])} | | | |", "",
          f"Missed reference speakers {o['per_speaker_cer']['missed_ref_speakers']}, extra hypothesis streams {o['per_speaker_cer']['extra_hyp_streams']}.", "",
          "## LID / non-Mandarin tracing (hypothesis segments)", "",
          f"Segments {lid['counts'].get('segments', 0)}; traditional-character rate {p(lid['traditional_char_rate'])}%; "
          + ", ".join(f"{k[4:]} {p(v)}%" for k, v in sorted(lid["segment_rates"].items()))]
    for k, ex in lid["examples"].items():
        md.append(f"- {k}: " + "; ".join(f"`{e['words'][:60]}`" for e in ex[:3]))
    return "\n".join(md) + "\n"


if __name__ == "__main__":
    raise SystemExit(main())
