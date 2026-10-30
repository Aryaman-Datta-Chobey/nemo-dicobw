#!/usr/bin/env python
"""Speaker-count distribution of the samples a Nemotron fine-tuning run actually trains on.

Builds NeMo's AudioToSpeechE2ESpkDiarDataset exactly as the training config does (subsegment mode,
session length, subsegment_nspk_bias; no noise augmentation, which does not change the targets) and
draws --passes passes over the training manifest (one sample per manifest line per pass, as the
training sampler does). Per sample: active speakers in the target window, speech and overlap
fraction of frames, sample length. Repeated with subsegment_nspk_bias = 1.0 for comparison.
Reported by corpus (manifest "corpus") x active speakers, next to the gold speaker-count
distribution of the evaluation sets (recordings, from their reference RTTMs).
Writes <out>/train_sample_stats.{json,md}. Run in the `nemo` env (CPU only).

    python eval/train_sample_stats.py --config recipes/diarization/configs/nemotron_ft_ear1.yaml \
        --out results/20261028-nemotron-ft-ear1-drift
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

import torch
from omegaconf import OmegaConf

EVAL = {"ear1_dev_D1": "EAR-1 dev D1", "ear1_dev_R1": "EAR-1 dev R1", "alimeeting_Test_Ali_far_ch1": "AliMeeting Test-far",
        "notsofar_eval_sc160": "NOTSOFAR eval-SC160", "ear1_crowd_real": "crowd real", "ear1_crowd_synth8": "crowd synth8"}


def dataset(cfg, bias: float):
    from nemo.collections.asr.data.audio_to_diar_label import AudioToSpeechE2ESpkDiarDataset
    from nemo.collections.asr.parts.preprocessing.features import FilterbankFeatures, WaveformFeaturizer

    ds, pp = cfg.model.train_ds, cfg.model.preprocessor
    sr = ds.sample_rate
    fb = FilterbankFeatures(sample_rate=sr, normalize=pp.normalize, n_window_size=int(pp.window_size * sr),
                            n_window_stride=int(pp.window_stride * sr), window=pp.window, nfilt=pp.features,
                            n_fft=pp.n_fft, frame_splicing=pp.frame_splicing, dither=pp.dither)
    return AudioToSpeechE2ESpkDiarDataset(
        manifest_filepath=ds.manifest_filepath, soft_label_thres=0.5, session_len_sec=ds.session_len_sec,
        num_spks=ds.num_spks, featurizer=WaveformFeaturizer(sample_rate=sr), fb_featurizer=fb,
        window_stride=pp.window_stride, global_rank=0, soft_targets=ds.soft_targets,
        subsampling_factor=cfg.model.output_subsampling_factor, device="cpu", subsegment_mode=ds.subsegment_mode,
        subsegment_single_chunk_min_len_sec=ds.subsegment_single_chunk_min_len_sec,
        subsegment_two_chunk_min_len_sec=ds.subsegment_two_chunk_min_len_sec,
        subsegment_two_chunks_rate=ds.subsegment_two_chunks_rate, subsegment_nspk_bias=bias,
        subsegment_start_guard_sec=ds.subsegment_start_guard_sec,
        subsegment_min_first_spk_sec=ds.subsegment_min_first_spk_sec,
        subsegment_splice_silence_sec=ds.subsegment_splice_silence_sec, validate_manifest_paths=False)


def draw(cfg, bias: float, corpus: list[str], passes: int, jobs: int, seed: int) -> list[dict]:
    ds = dataset(cfg, bias)
    assert len(ds) == len(corpus), "dataset and manifest lengths differ"
    g = torch.Generator().manual_seed(seed)
    order = torch.cat([torch.randperm(len(ds), generator=g) for _ in range(passes)]).tolist()
    dl = torch.utils.data.DataLoader(ds, sampler=order, batch_size=None, num_workers=jobs,
                                     worker_init_fn=lambda w: torch.manual_seed(seed + w))
    out = []
    for i, (audio, alen, targets, tlen, _) in zip(order, dl):
        act = targets[: int(tlen)] > 0.5
        n = act.sum(1)
        out.append({"corpus": corpus[i], "n_active": int(act.any(0).sum()), "sec": float(alen) / cfg.model.sample_rate,
                    "speech": float((n > 0).float().mean()), "overlap": float((n > 1).float().mean())})
    return out


def gold(manifests: Path) -> dict[str, Counter]:
    out = {}
    for stem, label in EVAL.items():
        c = Counter()
        for row in (json.loads(x) for x in (manifests / f"{stem}.jsonl").read_text().splitlines() if x.strip()):
            c[len({ln.split()[7] for ln in Path(row["rttm_filepath"]).read_text().splitlines() if ln.startswith("SPEAKER")})] += 1
        out[label] = c
    return out


def table(samples: list[dict]) -> dict[str, dict]:
    by = defaultdict(list)
    for s in samples:
        by[s["corpus"]].append(s)
        by["all"].append(s)
    return {k: {"n": len(v), "n_active": dict(sorted(Counter(s["n_active"] for s in v).items())),
                "speech": sum(s["speech"] for s in v) / len(v), "overlap": sum(s["overlap"] for s in v) / len(v),
                "sec": sum(s["sec"] for s in v) / len(v)} for k, v in by.items()}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--manifests", type=Path, default=Path("/mnt/data/manifests/nemo"))
    ap.add_argument("--passes", type=int, default=5)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--train-manifest", type=Path, help="override the config's training manifest")
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    cfg = OmegaConf.load(args.config)
    if args.train_manifest:
        cfg.model.train_ds.manifest_filepath = str(args.train_manifest)
    corpus = [json.loads(x)["corpus"] for x in Path(cfg.model.train_ds.manifest_filepath).read_text().splitlines() if x.strip()]
    trained = cfg.model.train_ds.subsegment_nspk_bias
    res = {"config": str(args.config), "passes": args.passes, "gold": {k: dict(sorted(v.items())) for k, v in gold(args.manifests).items()},
           "samples": {}}
    for bias in dict.fromkeys([float(trained), 1.0]):
        res["samples"][f"nspk_bias={bias:g}"] = table(draw(cfg, bias, corpus, args.passes, args.jobs, args.seed))
        print(f"drew nspk_bias={bias:g}", flush=True)
    (args.out / "train_sample_stats.json").write_text(json.dumps(res, indent=1))

    ks = range(0, 9)
    pct = lambda c, n: " | ".join(f"{100 * c.get(k, 0) / n:.0f}" for k in ks)
    md = ["# Speaker count of training samples vs evaluation recordings", "",
          f"Training: `{cfg.model.train_ds.manifest_filepath}`, {args.passes} passes (one {cfg.model.train_ds.session_len_sec} s-max "
          "subsegment per manifest line per pass), active speakers in the target window. Evaluation: gold speakers per recording. "
          "Cells are % of samples / recordings. Generated by eval/train_sample_stats.py.", "",
          "| set | n | " + " | ".join(f"{k} spk" for k in ks) + " | speech | overlap | mean s |", "|---|---" + "|---" * (len(ks) + 3) + "|"]
    for key, t in res["samples"].items():
        for corp, r in t.items():
            c = {int(k): v for k, v in r["n_active"].items()}
            md.append(f"| train {key} {corp} | {r['n']} | {pct(c, r['n'])} | {100 * r['speech']:.0f}% | {100 * r['overlap']:.0f}% | {r['sec']:.0f} |")
    for label, c in res["gold"].items():
        md.append(f"| eval {label} | {sum(c.values())} | {pct(c, sum(c.values()))} | | | |")
    (args.out / "train_sample_stats.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
