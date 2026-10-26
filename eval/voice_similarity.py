#!/usr/bin/env python
"""D8: speaker-embedding similarity behind counting errors.

extract  (run once per embedder, in an env that supports it: campplus_zh -> `dicow`, titanet_large -> `nemo`)
    Embeds every reference speaker of the main conditions from its solo speech (frames where it is
    the only active reference speaker; chunks of 1-10 s, up to MAX_S seconds, mean of chunk
    embeddings), plus two split-half embeddings (first / second half of those chunks) as a
    same-speaker baseline, and every hypothesis speaker (solo hypothesis frames) in recordings that
    have extra speakers. Cache: <exp>/<run>/embeddings/<model>.npz.
analyse
    Absorbed missed speakers (D2): cosine to the absorbing reference speaker (the one mapped to the
    hypothesis speaker most active on the absorbed speaker's solo speech), against all other
    reference-speaker pairs of the same corpus (different-speaker baseline).
    Extra hypothesis speakers (D1): cosine to the hypothesis speaker mapped to the reference speaker
    they overlap most, against the split-half same-speaker and the different-speaker baselines.
    Writes <results>/<run>/voice_similarity.{json,md}. Language-matched model: CAM++ (Mandarin) for
    aishell4/aishell5/alimeeting, TitaNet for the rest; both are reported.

Example:
    ~/miniforge3/envs/dicow/bin/python eval/voice_similarity.py extract --model campplus_zh --run <run>
    ~/miniforge3/envs/nemo/bin/python  eval/voice_similarity.py extract --model titanet_large --run <run>
    ~/miniforge3/envs/nemo/bin/python  eval/voice_similarity.py analyse --run <run>
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

from nemo_dicobw.diar_metrics import merge_speaker_turns, score_file
from nemo_dicobw.rttm import intersect_intervals, load_rttm, load_uem, merge_intervals, subtract_intervals

sys.path.insert(0, str(Path(__file__).resolve().parent))
from count_diagnostics import analyse_recording  # noqa: E402
from extra_speaker_analysis import CONDITIONS, corpus_of  # noqa: E402

REPO = Path(__file__).resolve().parents[1]
MAX_S, MIN_CHUNK, MAX_CHUNK = 60.0, 1.0, 10.0
MANDARIN = {"aishell4", "aishell5", "alimeeting"}


def solo(spk_iv: dict, who: str) -> list:
    others = merge_intervals(x for k, v in spk_iv.items() if k != who for x in v)
    return subtract_intervals(spk_iv[who], others)


def chunks(iv: list) -> list[tuple[float, float]]:
    out, total = [], 0.0
    for s, e in iv:
        while e - s >= MIN_CHUNK and total < MAX_S:
            c = min(e, s + MAX_CHUNK)
            out.append((s, c))
            total += c - s
            s = c
    return out


def conditions_data(args):
    for cond in CONDITIONS:
        rows = [json.loads(l) for l in (args.manifests / f"{cond}.jsonl").read_text().splitlines() if l.strip()]
        yield cond, rows, load_rttm(args.exp / args.run / "rttm" / cond), \
            load_rttm(sorted({r["rttm_filepath"] for r in rows})), load_uem(sorted({r["uem_filepath"] for r in rows}))


def extract(args) -> None:
    import soundfile as sf
    from nemo_dicobw.spk_embed import make

    emb = make(args.model)
    cache: dict[str, np.ndarray] = {}
    for cond, rows, hyp, ref, uem in conditions_data(args):
        for r in rows:
            u = uem[r["session"]]
            ref_iv = {k: intersect_intervals(v, u) for k, v in merge_speaker_turns(ref.get(r["session"], [])).items()}
            hyp_t = hyp.get(r["uniq_id"], [])
            sc = score_file(ref.get(r["session"], []), hyp_t, u, 0.0)
            want = [("ref", k, ref_iv) for k in ref_iv]
            if sc.n_hyp_speakers > len(sc.mapping):  # recording has unmapped (extra) hypothesis speakers
                hyp_iv = {k: intersect_intervals(v, u) for k, v in merge_speaker_turns(hyp_t).items()}
                want += [("hyp", k, hyp_iv) for k in hyp_iv]
            audio, sr = sf.read(r["audio_filepath"], dtype="float32")
            for side, spk, ivs in want:
                ch = chunks(solo(ivs, spk))
                if not ch:
                    continue
                vecs = [emb.embed(audio[int(s * sr):int(e * sr)]) for s, e in ch]
                key = f"{side}|{cond}|{r['uniq_id']}|{spk}"
                cache[key] = _mean(vecs)
                if side == "ref" and len(vecs) >= 2:
                    h = len(vecs) // 2
                    cache[key + "|A"], cache[key + "|B"] = _mean(vecs[:h]), _mean(vecs[h:])
        print(f"{args.model}: done {cond} ({len(cache)} embeddings)", flush=True)
    out = args.exp / args.run / "embeddings" / f"{args.model}.npz"
    out.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(out, **{k.replace("/", "%"): v for k, v in cache.items()})


def _mean(vs: list[np.ndarray]) -> np.ndarray:
    m = np.mean(vs, axis=0)
    return m / (np.linalg.norm(m) + 1e-12)


def analyse(args) -> None:
    models = {}
    for m in ("campplus_zh", "titanet_large"):
        f = args.exp / args.run / "embeddings" / f"{m}.npz"
        if f.exists():
            z = np.load(f)
            models[m] = {k.replace("%", "/"): z[k] for k in z.files}
    res: dict = {m: defaultdict(lambda: defaultdict(list)) for m in models}
    for cond, rows, hyp, ref, uem in conditions_data(args):
        corpus = corpus_of(cond)
        for r in rows:
            u = uem[r["session"]]
            rt, ht = ref.get(r["session"], []), hyp.get(r["uniq_id"], [])
            rec = analyse_recording(cond, r, rt, ht, u)
            sc = rec["score"]
            ref_iv = {k: intersect_intervals(v, u) for k, v in merge_speaker_turns(rt).items()}
            hyp_iv = {k: intersect_intervals(v, u) for k, v in merge_speaker_turns(ht).items()}
            inv = {h: k for k, h in sc.mapping.items()}
            for m, E in models.items():
                g = lambda side, spk, half="": E.get(f"{side}|{cond}|{r['uniq_id']}|{spk}" + (f"|{half}" if half else ""))  # noqa: E731
                spks = [k for k in ref_iv if g("ref", k) is not None]
                for i, a in enumerate(spks):  # baselines
                    for b in spks[i + 1:]:
                        res[m][corpus]["diff_pair"].append(float(g("ref", a) @ g("ref", b)))
                    if g("ref", a, "A") is not None:
                        res[m][corpus]["same_split_half"].append(float(g("ref", a, "A") @ g("ref", a, "B")))
                for mi in rec["missed"]:  # absorbed speakers
                    if mi["fate"] != "absorbed" or g("ref", mi["speaker"]) is None:
                        continue
                    so = solo(ref_iv, mi["speaker"])
                    cover = {h: sum(e - s for s, e in intersect_intervals(so, iv)) for h, iv in hyp_iv.items()}
                    h_star = max(cover, key=cover.get) if cover else None
                    absorber = inv.get(h_star)
                    if absorber and g("ref", absorber) is not None:
                        c = float(g("ref", mi["speaker"]) @ g("ref", absorber))
                        res[m][corpus]["absorbed_pair"].append(c)
                        res[m]["_items"]["absorbed"].append({"corpus": corpus, "file": r["uniq_id"], "missed": mi["speaker"],
                                                             "absorber": absorber, "cos": c, "airtime": mi["airtime"]})
                for ex in rec["extras"]:  # extra hypothesis speakers vs the mapped speaker they split from
                    ov = {k: sum(e - s for s, e in intersect_intervals(hyp_iv[ex["speaker"]], iv)) for k, iv in ref_iv.items()}
                    top = max(ov, key=ov.get) if ov and max(ov.values()) > 0 else None
                    hm = sc.mapping.get(top)
                    if hm is None or g("hyp", ex["speaker"]) is None or g("hyp", hm) is None:
                        continue
                    c = float(g("hyp", ex["speaker"]) @ g("hyp", hm))
                    res[m][corpus][f"extra_{ex['kind']}"].append(c)
                    res[m]["_items"]["extra"].append({"corpus": corpus, "file": r["uniq_id"], "kind": ex["kind"],
                                                      "dur": ex["dur"], "cos_to_mapped": c})

    def stats(v):
        a = np.array(v)
        return {"n": len(a), "median": float(np.median(a)), "p10": float(np.percentile(a, 10)),
                "p90": float(np.percentile(a, 90))} if len(a) else {"n": 0}

    out = {"run": args.run, "models": list(models)}
    for m in models:
        items = res[m].pop("_items", {})
        out[m] = {c: {k: stats(v) for k, v in d.items()} for c, d in res[m].items()}
        # absorbed pairs: percentile within their corpus's different-speaker baseline
        for it in items.get("absorbed", []):
            base = np.array(res[m][it["corpus"]]["diff_pair"])
            it["pct_of_diff_pairs_below"] = float(np.mean(base < it["cos"])) if len(base) else None
        out[m + "_items"] = items
    rdir = args.results / args.run
    (rdir / "voice_similarity.json").write_text(json.dumps(out, indent=1) + "\n")
    md = [f"# D8 Voice similarity behind counting errors: {args.run}", "",
          "Cosine of mean solo-speech embeddings. Language-matched model: CAM++ zh for aishell4/aishell5/alimeeting, "
          "TitaNet-large for the others. Generated by eval/voice_similarity.py.", ""]
    for m in models:
        md += [f"## {m}", "", "| corpus | same speaker (split-half) | different speakers | absorbed→absorber | extra: sliver | extra: phantom | extra: long split interleaved | extra: long split temporal |",
               "|---|---|---|---|---|---|---|---|"]
        f = lambda s: "–" if not s or not s.get("n") else f"{s['median']:.2f} [{s['p10']:.2f}, {s['p90']:.2f}] n={s['n']}"  # noqa: E731
        for c, d in sorted(out[m].items()):
            match = (c in MANDARIN) == (m == "campplus_zh")
            md.append(f"| {c}{' *' if match else ''} | {f(d.get('same_split_half'))} | {f(d.get('diff_pair'))} | {f(d.get('absorbed_pair'))} | "
                      f"{f(d.get('extra_sliver'))} | {f(d.get('extra_phantom'))} | {f(d.get('extra_long_split_interleaved'))} | "
                      f"{f(d.get('extra_long_split_temporal'))} |")
        md += ["", "\\* language-matched model. Cells: median [p10, p90] n.", "", "Absorbed speakers (cos, share of the corpus's different-speaker pairs below it):",
               ""] + [f"- {it['corpus']} {it['file']} {it['missed']} → {it['absorber']}: cos {it['cos']:.2f} "
                      f"({100 * it['pct_of_diff_pairs_below']:.0f}th pct), airtime {it['airtime']:.0f} s" for it in out[m + "_items"].get("absorbed", [])] + [""]
    (rdir / "voice_similarity.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["extract", "analyse"])
    ap.add_argument("--run", required=True)
    ap.add_argument("--model", choices=["campplus_zh", "titanet_large"])
    ap.add_argument("--exp", type=Path, default=Path("/mnt/data/exp/nemotron"))
    ap.add_argument("--manifests", type=Path, default=Path("/mnt/data/manifests/nemo"))
    ap.add_argument("--results", type=Path, default=REPO / "results")
    args = ap.parse_args()
    extract(args) if args.mode == "extract" else analyse(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
