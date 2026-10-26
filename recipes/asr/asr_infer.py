#!/usr/bin/env python
"""Whisper-family / DiCoW inference on diarized multi-speaker recordings (one condition per call).

Modes (see nemo_dicobw.longform for windowing):
    whole        <= 30 s windows cut at silences of the diarized union speech; the mixture is decoded.
    per_speaker  per diarized speaker, <= 30 s windows cut at that speaker's silences; Whisper gets the
                 audio with only-non-target frames zeroed, DiCoW gets the unmasked audio plus STNO masks.
Diarization: `nemotron:<run_id>` (RTTMs under /mnt/data/exp/nemotron/<run_id>/rttm/<manifest name>/,
probabilities used for late fusion) or `oracle` (the manifest's reference RTTM).

Output under <out>/<condition>/:
    windows.jsonl                one line per decoded window: uniq_id, session, stream, window, text,
                                 segments (absolute), chars (absolute DTW times), language
    hyp_<variant>.seglst.json    SegLST hypotheses (session_id = reference session):
        per_speaker: seg (model timestamp segments; timestamps on), dtw (characters grouped onto the
                     stream's diarized intervals, whose bounds give the times)
        whole:       agnostic_seg / agnostic_dtw (one stream "all"), fusion_nemotron / fusion_oracle
                     (late fusion of DTW characters with that diarization)
    config.json                  model, decoding and windowing settings, counts, real-time factor
Recordings already in windows.jsonl are skipped; SegLST files are rebuilt from windows.jsonl.

Example (dicow env):
    python recipes/asr/asr_infer.py --model /mnt/data/models/BELLE-2__Belle-whisper-large-v3-zh \
        --manifest /mnt/data/manifests/nemo/alimeeting_Eval_Ali_far_ch1.jsonl --diar nemotron:20261026-nemotron-zeroshot \
        --mode per_speaker --timestamps on --language zh --out /mnt/data/exp/asr/20261027-whisper-zeroshot \
        --condition alimeeting_Eval_Ali__belle-zh__perspk__ts-on__nemotron
"""
from __future__ import annotations

import argparse
import json
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import soundfile as sf

from nemo_dicobw import late_fusion
from nemo_dicobw.longform import stno_mask, target_mask, windows
from nemo_dicobw.rttm import Turn, intersect_intervals, load_rttm, merge_intervals

EXP_NEMOTRON = Path("/mnt/data/exp/nemotron")


def diar_turns(spec: str, manifest: Path, row: dict) -> tuple[list[Turn], np.ndarray | None]:
    if spec == "oracle":
        return load_rttm(row["rttm_filepath"]).get(row["session"], []), None
    run = spec.split(":", 1)[1]
    cond = manifest.name.removesuffix(".jsonl")
    hyp = load_rttm(EXP_NEMOTRON / run / "rttm" / cond / f"{row['uniq_id']}.rttm").get(row["uniq_id"], [])
    probs = EXP_NEMOTRON / run / "probs" / cond / f"{row['uniq_id']}.npy"
    return hyp, (np.load(probs).astype(np.float32) if probs.exists() else None)


def by_speaker(turns: list[Turn]) -> dict[str, list[tuple[float, float]]]:
    d = defaultdict(list)
    for t in turns:
        d[t.speaker].append((t.start, t.end))
    return {k: merge_intervals(v) for k, v in d.items()}


def decode_recording(dec, args, row, turns) -> list[dict]:
    audio, sr = sf.read(row["audio_filepath"], dtype="float32")
    rec_end = len(audio) / sr
    spk = by_speaker(turns)
    jobs = []  # (stream, window, audio, stno)
    if args.mode == "whole":
        union = merge_intervals(x for v in spk.values() for x in v)
        for w in windows(union, rec_end, audio):
            jobs.append(("all", w, audio[int(w[0] * sr):int(w[1] * sr)], None))
    else:
        for s, ivs in spk.items():
            others = [x for k, v in spk.items() if k != s for x in v]
            for w in windows(ivs, rec_end, audio):
                seg = audio[int(w[0] * sr):int(w[1] * sr)]
                if args.dicow:
                    jobs.append((s, w, seg, stno_mask(w, ivs, others)))
                else:
                    jobs.append((s, w, seg * target_mask(w, ivs, others, n=len(seg)), None))
    out = []
    order = sorted(range(len(jobs)), key=lambda i: -(jobs[i][1][1] - jobs[i][1][0]))
    for b in range(0, len(order), args.batch_size):
        idx = order[b:b + args.batch_size]
        res = dec.decode([jobs[i][2] for i in idx], [jobs[i][3] for i in idx] if args.dicow else None)
        for i, r in zip(idx, res):
            stream, (ws, we), _, _ = jobs[i]
            out.append({"uniq_id": row["uniq_id"], "session": row["session"], "stream": stream,
                        "window": [round(ws, 3), round(we, 3)], "text": r["text"], "language": r["language"],
                        "segments": [[round(ws + s, 3), round(min(ws + e, we), 3), t] for s, e, t in r["segments"]],
                        "chars": [[round(ws + t, 3), c] for t, c in r["chars"]]})
    return sorted(out, key=lambda x: (x["stream"], x["window"][0]))


def build_seglst(rows: list[dict], lines: list[dict], args, manifest: Path) -> dict[str, list[dict]]:
    hyps: dict[str, list[dict]] = defaultdict(list)
    by_uid = defaultdict(list)
    for x in lines:
        by_uid[x["uniq_id"]].append(x)
    for row in rows:
        ws = by_uid.get(row["uniq_id"], [])
        sess = row["session"]
        if args.mode == "per_speaker":
            turns, _ = diar_turns(args.diar, manifest, row)
            spk = by_speaker(turns)
            for x in ws:
                hyps["seg"] += [{"session_id": sess, "speaker": x["stream"], "start_time": s, "end_time": e, "words": t}
                                for s, e, t in x["segments"]]
                ivs = intersect_intervals(spk.get(x["stream"], []), [tuple(x["window"])]) or [tuple(x["window"])]
                groups = defaultdict(list)
                for t, c in x["chars"]:
                    k = min(range(len(ivs)), key=lambda j: max(ivs[j][0] - t, t - ivs[j][1], 0.0))
                    groups[k].append(c)
                for k, cs in sorted(groups.items()):
                    hyps["dtw"].append({"session_id": sess, "speaker": x["stream"], "start_time": round(ivs[k][0], 3),
                                        "end_time": round(ivs[k][1], 3), "words": _join(cs)})
        else:
            chars = [(t, c) for x in ws for t, c in x["chars"]]
            for x in ws:
                hyps["agnostic_seg"] += [{"session_id": sess, "speaker": "all", "start_time": s, "end_time": e, "words": t}
                                         for s, e, t in x["segments"]]
            hyps["agnostic_dtw"] += late_fusion.segments(chars, ["all"] * len(chars), sess)
            for name, spec in (("fusion_nemotron", args.fusion_nemotron), ("fusion_oracle", "oracle")):
                if spec:
                    turns, probs = diar_turns(spec, manifest, row)
                    hyps[name] += late_fusion.segments(chars, late_fusion.assign(chars, turns, probs), sess)
    if args.mode == "per_speaker" and not args.timestamps:
        hyps.pop("seg", None)
    return {k: v for k, v in hyps.items() if v or k in ("seg", "dtw", "agnostic_dtw")}


def _join(cs: list[str]) -> str:
    out = ""
    for c in cs:
        out += (" " if out and c.isascii() and out[-1:].isascii() else "") + c
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True)
    ap.add_argument("--dicow", action="store_true")
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--diar", required=True, help="nemotron:<run_id> or oracle")
    ap.add_argument("--fusion-nemotron", default="nemotron:20261026-nemotron-zeroshot",
                    help="diarization for whole-mode late fusion (empty to skip)")
    ap.add_argument("--mode", choices=["whole", "per_speaker"], required=True)
    ap.add_argument("--timestamps", choices=["on", "off"], required=True)
    ap.add_argument("--language", choices=["zh", "auto"], default="zh")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--condition", required=True)
    ap.add_argument("--batch-size", type=int, default=16)
    ap.add_argument("--limit", type=int, help="only the first N recordings (smoke tests)")
    args = ap.parse_args()
    args.timestamps = args.timestamps == "on"

    from nemo_dicobw.whisper_decode import Decoder

    rows = [json.loads(l) for l in args.manifest.read_text().splitlines() if l.strip()][:args.limit]
    out = args.out / args.condition
    out.mkdir(parents=True, exist_ok=True)
    wpath = out / "windows.jsonl"
    done = {json.loads(l)["uniq_id"] for l in wpath.read_text().splitlines()} if wpath.exists() else set()
    dec, audio_s, wall = None, 0.0, 0.0
    for i, row in enumerate(rows, 1):
        if row["uniq_id"] in done:
            continue
        if dec is None:
            dec = Decoder(args.model, dicow=args.dicow, timestamps=args.timestamps,
                          language=None if args.language == "auto" else "zh")
        turns, _ = diar_turns(args.diar, args.manifest, row)
        t0 = time.time()
        lines = decode_recording(dec, args, row, turns)
        wall += time.time() - t0
        audio_s += row["duration"]
        with open(wpath, "a") as f:
            f.writelines(json.dumps(x, ensure_ascii=False) + "\n" for x in lines)
        print(f"[{args.condition} {i}/{len(rows)}] {row['uniq_id']}: {len(lines)} windows, "
              f"{row['duration'] / 60:.1f} min in {time.time() - t0:.0f}s", flush=True)

    lines = [json.loads(l) for l in wpath.read_text().splitlines() if l.strip()]
    for name, segs in build_seglst(rows, lines, args, args.manifest).items():
        (out / f"hyp_{name}.seglst.json").write_text(json.dumps(segs, ensure_ascii=False) + "\n")
    cfg = {k: str(v) if isinstance(v, Path) else v for k, v in vars(args).items()}
    cfg.update({"decoding": "greedy, num_beams 1, no temperature fallback, max_new_tokens 440, bf16, SDPA attention",
                "char_times": "cross-attention DTW in one teacher-forced decoder pass (openai-whisper find_alignment rows)",
                "windowing": "<= 30 s, cut at diarized silences (pad 0.3 s); long runs cut at the energy minimum of the last 8 s",
                "borrowed_alignment_heads": getattr(dec, "borrowed_heads", None) if dec else None,
                "n_recordings": len(rows), "n_windows": len(lines)})
    if audio_s:
        cfg["rtfx_this_call"] = round(audio_s / wall, 1)
    (out / "config.json").write_text(json.dumps(cfg, indent=1) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
