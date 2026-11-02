#!/usr/bin/env python
"""CTC character times against MFA word times on single-speaker cuts (EXPERIMENTS.md 20261101-dicow-timing). Dicow env.

Aligns each cut's reference text with a CTC head and compares every Han character's start and centre with its MFA word, whose
time is split evenly over its characters. MFA is itself an estimate, so this measures agreement, not truth. Reference text,
clean read speech and no STNO mask, so it says nothing yet about meetings or decoded text. `uniform` is the fallback given MFA's
own speech span as the diarization, for comparison.

    PYTHONPATH=third_party/TS-ASR-Whisper/src:src python eval/timing_diag.py --head <checkpoint>/model.safetensors --out results/<run>/
    ... --checkpoint <dir of a jointly trained DiCoW checkpoint> --stno span|full --out results/<run>/

A jointly trained encoder has FDDT, so it needs an STNO mask: `span` marks target over MFA's speech span and silence elsewhere
(as a diarizer would), `full` marks the whole window target and gives the head no timing hint.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import lhotse
import numpy as np
import torch

from nemo_dicobw.timing import _is_han, align_text, ctc_log_probs, text_units, uniform_units

MODEL = "/mnt/data/models/BELLE-2__Belle-whisper-large-v3-zh-punct"
CUTS = "/mnt/data/manifests/lhotse/dicow_open/ctc_dev_aishell3_cutset.jsonl.gz"


def mfa_chars(cut) -> list[tuple[str, float, float]]:
    out = []
    for w in cut.supervisions[0].alignment["word"]:
        hans = [c for c in w.symbol if _is_han(c)]
        for i, c in enumerate(hans):
            out.append((c, w.start + i * w.duration / len(hans), w.start + (i + 1) * w.duration / len(hans)))
    return out


def errors(units, ref) -> dict:
    hans = [u for u in units if _is_han(u.text[0])]
    if [u.text[0] for u in hans] != [r[0] for r in ref]:
        return {}
    return {"start": [u.start - r[1] for u, r in zip(hans, ref)], "inside": [r[1] <= (u.start + u.end) / 2 < r[2] for u, r in zip(hans, ref)],
            "near": [abs((u.start + u.end) / 2 - (r[1] + r[2]) / 2) for u, r in zip(hans, ref)]}


def stno_mask(cuts, kind: str) -> torch.Tensor:
    """(B, 4, 1500) silence / target / non-target / overlap channels at the encoder's 20 ms input rate."""
    mask = torch.zeros(len(cuts), 4, 1500)
    for i, c in enumerate(cuts):
        ref = mfa_chars(c)
        lo, hi = (0, 1500) if kind == "full" else (int(ref[0][1] / 0.02), int(np.ceil(ref[-1][2] / 0.02)))
        mask[i, 0] = 1
        mask[i, 0, lo:hi] = 0
        mask[i, 1, lo:hi] = 1
    return mask


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--head", help="frozen-encoder CTC head safetensors, loaded onto --model, no FDDT")
    src.add_argument("--checkpoint", help="jointly trained DiCoW checkpoint directory, needs --stno")
    ap.add_argument("--stno", choices=["span", "full"])
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--cuts", default=CUTS)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--batch", type=int, default=8)
    args = ap.parse_args()
    if bool(args.checkpoint) != bool(args.stno):
        ap.error("--stno goes with --checkpoint")
    from safetensors.torch import load_file
    from transformers import WhisperFeatureExtractor, WhisperTokenizerFast

    from models.dicow.modeling_dicow import DiCoWForConditionalGeneration

    tok = WhisperTokenizerFast.from_pretrained(args.model)
    fe = WhisperFeatureExtractor.from_pretrained(args.model)
    if args.checkpoint:
        model = DiCoWForConditionalGeneration.from_pretrained(args.checkpoint, torch_dtype=torch.bfloat16)
        assert model.config.use_fddt and model.get_encoder().config.ctc_weight > 0
    else:
        model = DiCoWForConditionalGeneration.from_pretrained(args.model, ctc_weight=0.3, use_fddt=False, pre_ctc_sub_sample=True, additional_self_attention_layer=True,
                                                              remove_timestamps_from_ctc=True, torch_dtype=torch.bfloat16)
    enc = model.get_encoder()
    if args.head:
        print(enc.load_state_dict(load_file(args.head), strict=False))
    enc = enc.cuda().eval()
    cuts = [c for c in lhotse.load_manifest(args.cuts) if c.supervisions[0].alignment]
    res = {"ctc": {"start": [], "inside": [], "near": []}, "uniform": {"start": [], "inside": [], "near": []}}
    scores, failed = [], 0
    sync = {"first_minus_start": [], "last_minus_end": [], "span_ratio": [], "emissions": []}
    for b in range(0, len(cuts), args.batch):
        batch = cuts[b:b + args.batch]
        feats = fe([c.load_audio().squeeze() for c in batch], sampling_rate=16000, return_tensors="pt").input_features.cuda().to(torch.bfloat16)
        lp = ctc_log_probs(enc, feats, stno_mask(batch, args.stno).cuda().to(torch.bfloat16) if args.stno else None)
        for c, lps in zip(batch, lp):
            ref = mfa_chars(c)
            text = c.supervisions[0].text
            emitted = np.where(lps.argmax(-1).cpu().numpy() != lps.shape[-1] - 1)[0] * 0.08 if torch.is_tensor(lps) else np.where(lps.argmax(-1) != lps.shape[-1] - 1)[0] * 0.08
            if len(emitted) >= 2:
                sync["first_minus_start"].append(emitted[0] - ref[0][1])
                sync["last_minus_end"].append(emitted[-1] - ref[-1][2])
                sync["span_ratio"].append((emitted[-1] - emitted[0]) / (ref[-1][2] - ref[0][1]))
                sync["emissions"].append(len(emitted))
            al = align_text(text, lps[: int(c.duration / 0.08) + 1], tok, lps.shape[-1] - 1)
            e = errors(al[0], ref) if al else {}
            if not e:
                failed += 1
                continue
            scores.append(al[1])
            for k in e:
                res["ctc"][k] += e[k]
            for k, v in errors(uniform_units(text, [(ref[0][1], ref[-1][2])]), ref).items():
                res["uniform"][k] += v
    out = {"head": args.head or args.checkpoint, "stno": args.stno, "cuts": len(cuts), "failed": failed, "mean_score": round(float(np.mean(scores)), 3), "frame_s": 0.08, "reference": "MFA words split evenly over characters"}
    for name, r in res.items():
        s, near = np.array(r["start"]), np.array(r["near"])
        out[name] = {"chars": len(s), "start_bias_s": round(float(np.median(s)), 3), "start_abs_median_s": round(float(np.median(np.abs(s))), 3), "start_abs_p90_s": round(float(np.percentile(np.abs(s), 90)), 3),
                     "centre_abs_median_s": round(float(np.median(near)), 3), "centre_abs_p90_s": round(float(np.percentile(near, 90)), 3), "centre_inside_mfa_char": round(float(np.mean(r["inside"])), 3)}
    out["greedy_emissions"] = {"utterances": len(sync["span_ratio"]), **{f"{k}_median": round(float(np.median(v)), 3) for k, v in sync.items()},
                               "last_minus_end_p90": round(float(np.percentile(sync["last_minus_end"], 90)), 3)}
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "timing_diag.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
