#!/usr/bin/env python
"""Attribute Mandarin ASR errors to overlap, turn type, insertion source, pinyin class, scoring
conventions, code-switching, LID and domain terms (diagnostics A1-A6, L1-L4, T1-T2; see EXPERIMENTS.md,
"ASR error attribution").

Each reference speaker is aligned token by token (nemo_dicobw.txt_norm_zh tokens: Han characters,
English words) with the hypothesis stream that cpCER assigned to it (read from the eval/score_asr.py
result JSON), on the same start-time-ordered concatenations cpCER uses. Counts match that JSON's
per-speaker sub/del/ins up to tie-breaking between equally short alignments. Unassigned reference
speakers are all deletions, unassigned hypothesis streams all insertions. Token times are interpolated
uniformly inside their segment; speaker activity comes from the forced-alignment RTTM.

    A1  sub/del by number of reference speakers active at the reference token (0, 1, 2, >=3);
        insertions by the same count at the hypothesis token time
    A2  sub/del rate on backchannel (<= 2 tokens, all fillers/acknowledgements), short (< 1 s) and
        long reference segments
    A3  near- vs far-field: per-condition summary rows; compare conditions that differ only in channel
    A4  insertions: loop (hypothesis segment holds a degenerate loop, see degenerate_loop), silence (no reference speaker within
        +-0.5 s), leakage (the token occurs in another reference speaker's text within +-2 s), other
    A5  Han substitutions by pinyin (heteronyms allowed): homophone (same toned syllable), tone
        (same toneless syllable), near (same initial or final), different
    A6  substitutions within a convention group (他/她/它, 的/地/得, filler variants, 两/二, ...)
    L1  masked error rate (sub+del over reference tokens) of Han tokens vs English words
    L2  fate of English reference words: correct / deleted / substituted by Han / substituted by Latin;
        Han reference tokens substituted by Latin
    L3  SETER (first token of each new script run) and SPER@1/@3 by switch direction (zh->en, en->zh),
        masked rates as in Okocha & Grant, arXiv 2609.11786
    L4  masked error rate of reference tokens inside windows decoded with a detected language != zh
    T1  term recall / precision / TermER (Chung et al., arXiv 2607.05058): per session, terms are English
        words and Han 2-4-grams occurring >= 3 times in the session reference and in no other session
        (maximal n-grams kept); presence within the reference segment +-2 s in the assigned stream
    T2  masked error rate inside vs outside term spans (B-CER / U-CER)

Writes <out>/<condition>__<variant>.{json,md}; with --run-dir, every condition's main variants
(per_speaker: dtw, seg; whole: fusion_nemotron, fusion_oracle) plus <out>/summary.md.

Example (dicow env):
    python eval/asr_error_attribution.py --run-dir /mnt/data/exp/asr/20261027-whisper-zeroshot --jobs 10
"""
from __future__ import annotations

import argparse
import bisect
import json
import re
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache
from pathlib import Path

from rapidfuzz.distance import Levenshtein

from nemo_dicobw.rttm import load_rttm, merge_intervals
from nemo_dicobw.txt_norm_zh import normalize

REPO = Path(__file__).resolve().parents[1]
REFS = Path("/mnt/data/refs")
DATASETS = {  # dataset prefix of the condition name -> (reference SegLST dir, forced-alignment RTTM dir)
    "alimeeting_Eval_Ali": REFS / "alimeeting/Eval_Ali",
    "alimeeting_Test_Ali": REFS / "alimeeting/Test_Ali",
    "aishell4_test": REFS / "aishell4/test",
    "aishell5_Eval1": REFS / "aishell5/Eval1",
    "aishell5_Eval2": REFS / "aishell5/Eval2",
}
MAIN_VARIANTS = {"per_speaker": ("dtw", "seg"), "whole": ("fusion_nemotron", "fusion_oracle")}
BACKCHANNEL = set("嗯啊哦噢喔呃额对是好行哎唉诶欸哈呵唔恩嘛吧呀")
CONVENTION_GROUPS = ["他她它祂", "的地得", "嗯恩唔呣", "哪那", "两二", "吗嘛么", "啊呀哇", "诶欸哎唉", "哦噢喔", "呃额"]
_GROUP = {c: i for i, g in enumerate(CONVENTION_GROUPS) for c in g}
_HAN = re.compile(r"[㐀-䶿一-鿿豈-﫿]")


def script(tok: str) -> str:
    return "han" if _HAN.fullmatch(tok) else "latin"


def degenerate_loop(text: str) -> bool:
    """An n-gram (n = 1..8) repeated in a row until the run spans >= 16 tokens (>= 4 repeats). Stricter
    than eval/score_asr.py's loop flag, which also catches genuine repetition such as 对对对对."""
    toks = normalize(text).split()
    for n in range(1, 9):
        reps = max(4, -(-16 // n))
        for i in range(0, max(0, len(toks) - reps * n + 1)):
            g = toks[i:i + n]
            if all(toks[i + k * n:i + (k + 1) * n] == g for k in range(1, reps)):
                return True
    return False


def tokens_with_times(segs: list[dict]) -> list[tuple[str, float, int]]:
    """(token, time, segment index) over start-ordered segments; times interpolated inside segments."""
    out = []
    for k, s in enumerate(segs):
        toks = normalize(s.get("words", "")).split()
        dur = max(s["end_time"] - s["start_time"], 0.0)
        out += [(t, s["start_time"] + (i + 0.5) * dur / len(toks), k) for i, t in enumerate(toks)]
    return out


class Activity:
    """Per-speaker merged reference turns; counts active speakers at a time or near it."""

    def __init__(self, turns):
        by = defaultdict(list)
        for t in turns:
            by[t.speaker].append((t.start, t.end))
        self.iv = {k: merge_intervals(v) for k, v in by.items()}
        self.starts = {k: [a for a, _ in v] for k, v in self.iv.items()}

    def _active(self, spk: str, a: float, b: float) -> bool:
        i = bisect.bisect_right(self.starts[spk], b) - 1
        return i >= 0 and self.iv[spk][i][1] >= a

    def count(self, t: float) -> int:
        return sum(self._active(k, t, t) for k in self.iv)

    def any_near(self, t: float, w: float) -> bool:
        return any(self._active(k, t - w, t + w) for k in self.iv)


@lru_cache(maxsize=None)
def pinyin_sets(ch: str) -> tuple[frozenset, frozenset, frozenset, frozenset]:
    from pypinyin import Style, pinyin

    toned = frozenset(pinyin(ch, style=Style.TONE3, heteronym=True, neutral_tone_with_five=True)[0])
    plain = frozenset(pinyin(ch, style=Style.NORMAL, heteronym=True)[0])
    ini = frozenset(x for x in pinyin(ch, style=Style.INITIALS, heteronym=True, strict=False)[0] if x)
    fin = frozenset(x for x in pinyin(ch, style=Style.FINALS, heteronym=True, strict=False)[0] if x)
    return toned, plain, ini, fin


def pinyin_class(r: str, h: str) -> str:
    rt, rp, ri, rf = pinyin_sets(r)
    ht, hp, hi, hf = pinyin_sets(h)
    if rt & ht:
        return "homophone"
    if rp & hp:
        return "tone"
    if (ri & hi) or (rf & hf):
        return "near"
    return "different"


def align(ref: list[str], hyp: list[str]) -> tuple[list[str], list[int | None], list[int]]:
    """Per reference token 'C'/'S'/'D' and its aligned hypothesis index; hypothesis indices inserted."""
    ops, rmap, ins = ["C"] * len(ref), [None] * len(ref), []
    i = j = 0
    for e in Levenshtein.editops(ref, hyp):  # ordered by position; equal runs lie between edits
        while i < e.src_pos:
            rmap[i] = j
            i, j = i + 1, j + 1
        if e.tag == "replace":
            ops[i], rmap[i] = "S", j
            i, j = i + 1, j + 1
        elif e.tag == "delete":
            ops[i] = "D"
            i += 1
        else:
            ins.append(j)
            j += 1
    while i < len(ref):
        rmap[i] = j
        i, j = i + 1, j + 1
    return ops, rmap, ins


def session_terms(ref_by_sess: dict[str, list[dict]]) -> dict[str, set[str]]:
    texts = {s: ["".join(normalize(x["words"]).split()) for x in segs] for s, segs in ref_by_sess.items()}
    counts = {s: Counter(g for t in ts for n in (2, 3, 4) for g in (t[i:i + n] for i in range(len(t) - n + 1))
                         if _HAN.fullmatch(g[0]) and all(_HAN.fullmatch(c) for c in g)) for s, ts in texts.items()}
    df = Counter(g for c in counts.values() for g in c)
    out = {}
    for s, c in counts.items():
        cand = {g: n for g, n in c.items() if n >= 3 and df[g] == 1}
        keep = {g for g, n in cand.items() if not any(len(o) > len(g) and g in o and cand[o] == n for o in cand)}
        latin = {t for x in ref_by_sess[s] for t in normalize(x["words"]).split() if script(t) == "latin"}
        out[s] = keep | latin
    return out


def term_hits(text_tokens: list[str], terms: set[str]) -> list[str]:
    """Term occurrences in a token list, in order (Han terms matched on the joined text)."""
    joined, out = "", []
    for t in text_tokens:
        joined += t if script(t) == "han" else f" {t} "
    for term in terms:
        key = term if script(term[0]) == "han" else f" {term} "
        start = joined.find(key)
        while start >= 0:
            out.append((start, term))
            start = joined.find(key, start + 1)
    return [t for _, t in sorted(out)]


def term_spans(tokens: list[str], terms: set[str]) -> set[int]:
    """Indices of tokens covered by a term occurrence (within one segment's tokens)."""
    cover = set()
    for n in (4, 3, 2):
        for i in range(len(tokens) - n + 1):
            if "".join(tokens[i:i + n]) in terms and all(script(x) == "han" for x in tokens[i:i + n]):
                cover.update(range(i, i + n))
    cover.update(i for i, t in enumerate(tokens) if script(t) == "latin" and t in terms)
    return cover


def analyse(cond_dir: Path, variant: str, score_json: Path, out: Path) -> dict:
    ds =next(k for k in DATASETS if cond_dir.name.startswith(k))
    ref_root = DATASETS[ds]
    ref_all = [s for f in sorted((ref_root / "seglst").glob("*.json")) for s in json.loads(f.read_text())]
    hyp_all = json.loads((cond_dir / f"hyp_{variant}.seglst.json").read_text())
    score = json.loads(score_json.read_text())
    ref_by_sess = defaultdict(list)
    for s in ref_all:
        ref_by_sess[s["session_id"]].append(s)
    terms = session_terms(ref_by_sess)
    windows = defaultdict(list)  # (session, stream) -> [(start, end, language)]
    wpath = cond_dir / "windows.jsonl"
    if wpath.exists():
        for line in wpath.read_text().splitlines():
            w = json.loads(line)
            windows[(w["session"], w["stream"])].append((w["window"][0], w["window"][1], w["language"]))
    n_win = Counter(lang for v in windows.values() for _, _, lang in v)

    C = defaultdict(Counter)  # diagnostic -> counter
    sub_examples = defaultdict(Counter)
    for sess, rsegs in ref_by_sess.items():
        act = Activity(load_rttm(ref_root / "rttm/fa" / f"{sess}.rttm").get(sess, []))
        rsp = defaultdict(list)
        for s in sorted(rsegs, key=lambda x: x["start_time"]):
            rsp[s["speaker"]].append(s)
        hsp = defaultdict(list)
        for s in sorted((x for x in hyp_all if x["session_id"] == sess), key=lambda x: x["start_time"]):
            hsp[s["speaker"]].append(s)
        rtok = {k: tokens_with_times(v) for k, v in rsp.items()}
        tok_times = defaultdict(lambda: defaultdict(list))  # ref speaker -> token -> sorted times (leakage)
        for k, v in rtok.items():
            for x, t, _ in v:
                tok_times[k][x].append(t)

        def near(times: list[float], t: float, w: float) -> bool:
            i = bisect.bisect_left(times, t - w)
            return i < len(times) and times[i] <= t + w

        def in_window(toks: list[tuple[str, float, int]], times: list[float], a: float, b: float) -> list[str]:
            return [x for x, _, _ in toks[bisect.bisect_left(times, a):bisect.bisect_right(times, b)]]
        pairs = [(p["ref_speaker"], p["hyp_stream"]) for p in score["per_speaker"] if p["session"] == sess]
        for r_spk, h_spk in pairs:
            R = rtok.get(r_spk, []) if r_spk else []
            hsegs = hsp.get(h_spk, []) if h_spk else []
            H = tokens_with_times(hsegs)
            loop_seg = [degenerate_loop(s["words"]) for s in hsegs]
            ops, rmap, ins = align([t for t, _, _ in R], [t for t, _, _ in H])
            # reference-side diagnostics
            seg_tok = defaultdict(list)
            for i, (_, _, k) in enumerate(R):
                seg_tok[k].append(i)
            for k, idx in seg_tok.items():
                seg = rsp[r_spk][k]
                toks = [R[i][0] for i in idx]
                dur = seg["end_time"] - seg["start_time"]
                turn = ("backchannel" if len(toks) <= 2 and all(t in BACKCHANNEL for t in toks)
                        else "short" if dur < 1.0 else "long")
                tspan = term_spans(toks, terms[sess])
                scr = [script(t) for t in toks]
                entries = [p for p in range(1, len(toks)) if scr[p] != scr[p - 1]]
                for p, i in enumerate(idx):
                    op, t = ops[i], R[i][1]
                    bad = op != "C"
                    n_act = min(act.count(t), 3)
                    for diag, key in (("A1", n_act), ("A2", turn), ("L1", scr[p]), ("T2", "term" if p in tspan else "other")):
                        C[diag][(key, "n")] += 1
                        C[diag][(key, op)] += 1
                    lang = next((l for a, b, l in windows.get((sess, h_spk), []) + windows.get((sess, "all"), [])
                                 if a <= t < b), None)
                    if lang:
                        C["L4"][(lang, "n")] += 1
                        C["L4"][(lang, "bad")] += bad
                    for e in entries:
                        d = abs(p - e)
                        direction = "zh->en" if scr[e] == "latin" else "en->zh"
                        for kk in (0, 1, 3):
                            if d <= kk:
                                C["L3"][(direction, kk, "n")] += 1
                                C["L3"][(direction, kk, "bad")] += bad
                    hj = rmap[i]
                    htok = H[hj][0] if op == "S" and hj is not None and hj < len(H) else None
                    if scr[p] == "latin":
                        fate = {"C": "correct", "D": "deleted"}.get(op) or ("to_han" if htok and script(htok) == "han" else "to_latin")
                        C["L2"][("english_ref", fate)] += 1
                    elif op == "S" and htok and script(htok) == "latin":
                        C["L2"][("han_ref", "to_latin")] += 1
                    if op == "S" and htok:
                        r = R[i][0]
                        if script(r) == "han" and script(htok) == "han":
                            cls = pinyin_class(r, htok)
                            C["A5"][cls] += 1
                            if sum(sub_examples[cls].values()) < 10_000:
                                sub_examples[cls][f"{r}->{htok}"] += 1
                        C["A6"]["convention" if _GROUP.get(R[i][0], -1) == _GROUP.get(htok, -2) else "other"] += 1
            # insertions
            for j in ins:
                tok, t, k = H[j]
                n_act = min(act.count(t), 3)
                C["A1"][(n_act, "I")] += 1
                if loop_seg[k]:
                    kind = "loop"
                elif not act.any_near(t, 0.5):
                    kind = "silence"
                elif any(near(tok_times[o][tok], t, 2.0) for o in rtok if o != r_spk and tok in tok_times[o]):
                    kind = "leakage"
                else:
                    kind = "other"
                C["A4"][kind] += 1
            # T1: term presence per reference segment / hypothesis segment, TermER per stream
            Hs = sorted(H, key=lambda x: x[1])
            Ht = [t for _, t, _ in Hs]
            Rs = sorted(R, key=lambda x: x[1])
            Rt = [t for _, t, _ in Rs]
            for k, seg in enumerate(rsp.get(r_spk, []) if r_spk else []):
                found = set(term_hits([R[i][0] for i in seg_tok.get(k, [])], terms[sess]))
                if not found:
                    continue
                got = set(term_hits(in_window(Hs, Ht, seg["start_time"] - 2, seg["end_time"] + 2), terms[sess]))
                C["T1"]["ref_terms"] += len(found)
                C["T1"]["recalled"] += len(found & got)
            hseg_tok = defaultdict(list)
            for x, _, k in H:
                hseg_tok[k].append(x)
            for k, seg in enumerate(hsegs):
                got = set(term_hits(hseg_tok.get(k, []), terms[sess]))
                if not got:
                    continue
                window = in_window(Rs, Rt, seg["start_time"] - 2, seg["end_time"] + 2)
                C["T1"]["hyp_terms"] += len(got)
                C["T1"]["precise"] += len(got & set(term_hits(window, terms[sess])))
            rt, ht = term_hits([x for x, _, _ in R], terms[sess]), term_hits([x for x, _, _ in H], terms[sess])
            C["T1"]["term_edits"] += Levenshtein.distance(rt, ht)
            C["T1"]["term_ref_len"] += len(rt)

    res = {"condition": cond_dir.name, "variant": variant, "score_json": str(score_json),
           "n_windows_by_language": dict(n_win), "counts": {d: {json.dumps(k, ensure_ascii=False) if isinstance(k, tuple) else str(k): v
                                                                for k, v in c.items()} for d, c in C.items()},
           "top_substitutions": {c: v.most_common(15) for c, v in sub_examples.items()}}
    res["summary"] = summarise(C)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.with_suffix(".json").write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n")
    out.with_suffix(".md").write_text(render(res))
    return res


def summarise(C: dict) -> dict:
    r = lambda a, b: a / b if b else None  # noqa: E731
    s = {}
    for key in (0, 1, 2, 3):
        n = C["A1"][(key, "n")]
        s[f"A1_{key}spk"] = {"n": n, "sub": r(C["A1"][(key, "S")], n), "del": r(C["A1"][(key, "D")], n),
                             "ins_per_ref_tok": r(C["A1"][(key, "I")], n)}
    for key in ("backchannel", "short", "long"):
        n = C["A2"][(key, "n")]
        s[f"A2_{key}"] = {"n": n, "sub": r(C["A2"][(key, "S")], n), "del": r(C["A2"][(key, "D")], n)}
    ins = sum(C["A4"].values())
    s["A4_insertions"] = {"n": ins, **{k: r(C["A4"][k], ins) for k in ("loop", "silence", "leakage", "other")}}
    subs = sum(C["A5"].values())
    s["A5_han_substitutions"] = {"n": subs, **{k: r(C["A5"][k], subs) for k in ("homophone", "tone", "near", "different")}}
    s["A6_convention_share_of_subs"] = r(C["A6"]["convention"], sum(C["A6"].values()))
    for key in ("han", "latin"):
        n = C["L1"][(key, "n")]
        s[f"L1_{key}"] = {"n": n, "masked_er": r(C["L1"][(key, "S")] + C["L1"][(key, "D")], n)}
    eng = sum(v for (a, _), v in C["L2"].items() if a == "english_ref")
    s["L2_english_ref"] = {"n": eng, **{f: r(C["L2"][("english_ref", f)], eng) for f in ("correct", "deleted", "to_han", "to_latin")}}
    s["L2_han_ref_to_latin_per_han"] = r(C["L2"][("han_ref", "to_latin")], C["L1"][("han", "n")])
    for d in ("zh->en", "en->zh"):
        for k in (0, 1, 3):
            s[f"L3_{d}_{'SETER' if k == 0 else f'SPER@{k}'}"] = {"n": C["L3"][(d, k, "n")], "er": r(C["L3"][(d, k, "bad")], C["L3"][(d, k, "n")])}
    s["L4"] = {lang: {"n": C["L4"][(lang, "n")], "masked_er": r(C["L4"][(lang, "bad")], C["L4"][(lang, "n")])}
               for lang in sorted({k[0] for k in C["L4"]})}
    t = C["T1"]
    rec, prec = r(t["recalled"], t["ref_terms"]), r(t["precise"], t["hyp_terms"])
    s["T1"] = {"ref_terms": t["ref_terms"], "recall": rec, "precision": prec,
               "f1": 2 * rec * prec / (rec + prec) if rec and prec else None, "term_er": r(t["term_edits"], t["term_ref_len"])}
    for key in ("term", "other"):
        n = C["T2"][(key, "n")]
        s[f"T2_{key}"] = {"n": n, "masked_er": r(C["T2"][(key, "S")] + C["T2"][(key, "D")], n)}
    return s


def _p(x) -> str:
    return "–" if x is None else f"{100 * x:.1f}"


def render(res: dict) -> str:
    s = res["summary"]
    md = [f"# ASR error attribution: {res['condition']} / {res['variant']}", "",
          "Rates in %. Masked rates = (sub+del) / reference tokens of the subset. Generated by eval/asr_error_attribution.py.", "",
          "## A1 overlap (active reference speakers at the token)", "", "| active | n | sub | del | ins / ref tok |", "|---|---|---|---|---|"]
    md += [f"| {k} | {s[f'A1_{k}spk']['n']} | {_p(s[f'A1_{k}spk']['sub'])} | {_p(s[f'A1_{k}spk']['del'])} | {_p(s[f'A1_{k}spk']['ins_per_ref_tok'])} |"
           for k in (0, 1, 2, 3)]
    md += ["", "## A2 turn type", "", "| turn | n | sub | del |", "|---|---|---|---|"]
    md += [f"| {k} | {s[f'A2_{k}']['n']} | {_p(s[f'A2_{k}']['sub'])} | {_p(s[f'A2_{k}']['del'])} |" for k in ("backchannel", "short", "long")]
    a4, a5 = s["A4_insertions"], s["A5_han_substitutions"]
    md += ["", f"## A4 insertions (n={a4['n']}): " + ", ".join(f"{k} {_p(a4[k])}" for k in ("loop", "silence", "leakage", "other")),
           "", f"## A5 Han substitutions (n={a5['n']}): " + ", ".join(f"{k} {_p(a5[k])}" for k in ("homophone", "tone", "near", "different")),
           ""] + [f"- {c}: " + ", ".join(f"{p} ×{n}" for p, n in ex[:8]) for c, ex in res["top_substitutions"].items()]
    md += ["", f"## A6 convention-equivalent share of substitutions: {_p(s['A6_convention_share_of_subs'])}", "",
           "## L1–L4 code-switching / LID", "",
           f"- L1 masked ER: Han {_p(s['L1_han']['masked_er'])} (n={s['L1_han']['n']}), English {_p(s['L1_latin']['masked_er'])} (n={s['L1_latin']['n']})",
           "- L2 English reference words: " + ", ".join(f"{k} {_p(s['L2_english_ref'][k])}" for k in ("correct", "deleted", "to_han", "to_latin"))
           + f"; Han→Latin per Han token {_p(s['L2_han_ref_to_latin_per_han'])}",
           "- L3: " + "; ".join(f"{k[3:]} {_p(v['er'])} (n={v['n']})" for k, v in s.items() if k.startswith("L3_")),
           "- L4 masked ER by window language: " + ", ".join(f"{k} {_p(v['masked_er'])} (n={v['n']})" for k, v in s["L4"].items())
           + f"; windows {res['n_windows_by_language']}", "",
           "## T1–T2 terms", "",
           f"- T1 term recall {_p(s['T1']['recall'])}, precision {_p(s['T1']['precision'])}, F1 {_p(s['T1']['f1'])}, TermER {_p(s['T1']['term_er'])} (reference terms {s['T1']['ref_terms']})",
           f"- T2 masked ER inside terms {_p(s['T2_term']['masked_er'])} (n={s['T2_term']['n']}), outside {_p(s['T2_other']['masked_er'])}"]
    return "\n".join(md) + "\n"


def summary_table(results: list[dict]) -> str:
    md = ["# ASR error attribution summary", "",
          "Rates in %. A1: del at 1 / 2 / ≥3 active speakers. A2: del on backchannel / short / long. A4: share of insertions. "
          "A5: share of Han substitutions. L1: masked ER Han / English. T1: term recall / precision. Generated by eval/asr_error_attribution.py.", "",
          "| condition | variant | A1 del 1/2/≥3 | A1 ins/tok 0spk | A2 del bc/short/long | A4 loop/sil/leak/other | A5 homo/tone/near/diff | A6 conv | L1 han/en | L2 en→han | T1 rec/prec | T2 term/other |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in results:
        s = r["summary"]
        a4, a5 = s["A4_insertions"], s["A5_han_substitutions"]
        md.append(f"| {r['condition']} | {r['variant']} | " + "/".join(_p(s[f'A1_{k}spk']['del']) for k in (1, 2, 3))
                  + f" | {_p(s['A1_0spk']['ins_per_ref_tok'])} | " + "/".join(_p(s[f'A2_{k}']['del']) for k in ("backchannel", "short", "long"))
                  + " | " + "/".join(_p(a4[k]) for k in ("loop", "silence", "leakage", "other"))
                  + " | " + "/".join(_p(a5[k]) for k in ("homophone", "tone", "near", "different"))
                  + f" | {_p(s['A6_convention_share_of_subs'])} | {_p(s['L1_han']['masked_er'])}/{_p(s['L1_latin']['masked_er'])}"
                  + f" | {_p(s['L2_english_ref']['to_han'])} | {_p(s['T1']['recall'])}/{_p(s['T1']['precision'])}"
                  + f" | {_p(s['T2_term']['masked_er'])}/{_p(s['T2_other']['masked_er'])} |")
    return "\n".join(md) + "\n"


def _job(a):
    return analyse(*a)


def main() -> int:
    ap =argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run-dir", type=Path, help="analyse every condition's main variants")
    ap.add_argument("--condition-dir", type=Path)
    ap.add_argument("--variant")
    ap.add_argument("--results", type=Path, default=REPO / "results", help="where the score_asr JSONs are (<results>/<run_id>/)")
    ap.add_argument("--out", type=Path, help="output dir (default <results>/<run_id>/attribution)")
    ap.add_argument("--jobs", type=int, default=10)
    args = ap.parse_args()
    if args.run_dir:
        run_id, conds = args.run_dir.name, sorted(p for p in args.run_dir.iterdir() if (p / "config.json").exists())
    else:
        run_id, conds = args.condition_dir.parent.name, [args.condition_dir]
    out = args.out or args.results / run_id / "attribution"
    jobs = []
    for c in conds:
        mode = "per_speaker" if "__per_speaker__" in c.name else "whole"
        for v in ([args.variant] if args.variant else MAIN_VARIANTS[mode]):
            score = args.results / run_id / f"{c.name}__{v}.json"
            if (c / f"hyp_{v}.seglst.json").exists() and score.exists():
                jobs.append((c, v, score, out / f"{c.name}__{v}"))
    print(f"{len(jobs)} condition/variant pairs, {args.jobs} jobs", flush=True)
    with ProcessPoolExecutor(args.jobs) as ex:
        results = list(ex.map(_job, jobs))
    if args.run_dir:
        (out / "summary.md").write_text(summary_table(results))
        print(f"wrote {out / 'summary.md'} ({len(results)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
