#!/usr/bin/env python
"""Run Nemotron-3-Diarization over NeMo manifests; write RTTMs and per-frame speaker probabilities.

For each manifest line (see make_eval_manifests.py) and each recording `<uniq_id>`:
    <out>/rttm/<manifest name>/<uniq_id>.rttm     speakers speaker_0..speaker_7
    <out>/probs/<manifest name>/<uniq_id>.npy     float16 (frames, 8) sigmoid outputs, 10 ms frames
    <out>/timing/<manifest name>.tsv              per-recording duration, wall time, RTFx
and once per run <out>/config.json (model, NeMo commit, streaming and postprocessing settings).
--model takes a .nemo file or a training checkpoint (.ckpt, loaded strictly into the released
architecture), e.g. from recipes/diarization/train_nemotron_ft.py.
Recordings whose RTTM and probabilities already exist are skipped, so a run can be resumed.

Defaults reproduce the model card's offline evaluation: streaming config spkcache_len=264,
fifo_len=40, chunk_len=340, chunk_right_context=40, spkcache_update_period=300 (30.4 s input
buffer), bf16, and NeMo's default postprocessing (onset = offset = 0.5, no padding, no minimum
durations), which is what e2e_diarize_speech.py uses.

Example (run in the `nemo` env):
    python recipes/diarization/nemotron_infer.py --out $DATA/exp/nemotron/20261026-nemotron-zeroshot \
        $DATA/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import soundfile as sf
import torch

from nemo_dicobw.rttm import Turn, write_rttm

DEFAULT_MODEL = "/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo"
STREAMING_KEYS = ("spkcache_len", "fifo_len", "chunk_len", "chunk_right_context", "spkcache_update_period")


def _git(repo: Path, *cmd: str) -> str:
    try:
        return subprocess.run(["git", "-C", str(repo), *cmd], capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def load_model(path: str, args: argparse.Namespace):
    from nemo.collections.asr.models import SortformerEncLabelModel

    if path.endswith(".ckpt"):  # training checkpoint: architecture from the released .nemo, weights strict
        model = SortformerEncLabelModel.restore_from(restore_path=DEFAULT_MODEL, map_location="cuda", strict=False)
        state = torch.load(path, map_location="cuda", weights_only=False)["state_dict"]
        model.load_state_dict(state, strict=True)
    else:
        model = SortformerEncLabelModel.restore_from(restore_path=path, map_location="cuda", strict=False)
    if args.precision == "bf16":
        model = model.to(dtype=torch.bfloat16)
    model.eval()
    sm = model.sortformer_modules
    for k in STREAMING_KEYS:
        setattr(sm, k, getattr(args, k))
    model._check_streaming_parameters()
    return model


def parse_segments(lines: list[str]) -> list[Turn]:
    """NeMo diarize() output lines '<start> <end> speaker_<k>' -> turns."""
    turns = []
    for line in lines:
        start, end, spk = line.split()
        if float(end) > float(start):
            turns.append(Turn(spk, float(start), float(end)))
    return sorted(turns, key=lambda t: (t.start, t.end, t.speaker))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("manifests", nargs="+", type=Path)
    ap.add_argument("--out", type=Path, required=True, help="run directory, e.g. $DATA/exp/nemotron/<run_id>")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--precision", choices=["bf16", "fp32"], default="bf16")
    ap.add_argument("--spkcache-len", dest="spkcache_len", type=int, default=264)
    ap.add_argument("--fifo-len", dest="fifo_len", type=int, default=40)
    ap.add_argument("--chunk-len", dest="chunk_len", type=int, default=340)
    ap.add_argument("--chunk-right-context", dest="chunk_right_context", type=int, default=40)
    ap.add_argument("--spkcache-update-period", dest="spkcache_update_period", type=int, default=300)
    ap.add_argument("--no-probs", action="store_true", help="do not save per-frame probabilities")
    args = ap.parse_args()

    repo = Path(__file__).resolve().parents[2]
    import nemo

    config = {
        "model": args.model,
        "model_revision": (Path(args.model).parent / "REVISION").read_text().strip()
        if (Path(args.model).parent / "REVISION").exists() else None,
        "nemo_version": nemo.__version__,
        "precision": args.precision,
        "streaming": {k: getattr(args, k) for k in STREAMING_KEYS},
        "postprocessing": "NeMo default PostProcessingParams (onset=offset=0.5, no padding, no min durations)",
        "git_commit": _git(repo, "rev-parse", "HEAD") + ("-dirty" if _git(repo, "status", "--porcelain", "--untracked-files=no") else ""),
        "started": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "manifests": [str(m) for m in args.manifests],
    }
    args.out.mkdir(parents=True, exist_ok=True)
    cfg_path = args.out / "config.json"
    if cfg_path.exists():
        old = json.loads(cfg_path.read_text())
        for k in ("model", "precision", "streaming"):
            if old.get(k) != config[k]:
                print(f"ERROR: {cfg_path} has {k}={old.get(k)}, this run {config[k]}; use a new --out", file=sys.stderr)
                return 1
        config["manifests"] = sorted(set(old.get("manifests", [])) | set(config["manifests"]))
        config["started"] = old.get("started", config["started"])
    cfg_path.write_text(json.dumps(config, indent=1) + "\n")

    model = None
    for manifest in args.manifests:
        name = manifest.name.removesuffix(".jsonl")
        rttm_dir, prob_dir = args.out / "rttm" / name, args.out / "probs" / name
        rttm_dir.mkdir(parents=True, exist_ok=True)
        if not args.no_probs:
            prob_dir.mkdir(parents=True, exist_ok=True)
        rows = [json.loads(line) for line in manifest.read_text().splitlines() if line.strip()]
        timing_path = args.out / "timing" / f"{name}.tsv"
        timing_path.parent.mkdir(parents=True, exist_ok=True)
        new_timing = not timing_path.exists()
        with open(timing_path, "a") as tf:
            if new_timing:
                tf.write("uniq_id\tduration_s\twall_s\trtfx\tn_speakers\n")
            for i, r in enumerate(rows, 1):
                uid = r["uniq_id"]
                rttm_path, prob_path = rttm_dir / f"{uid}.rttm", prob_dir / f"{uid}.npy"
                if rttm_path.exists() and (args.no_probs or prob_path.exists()):
                    continue
                if model is None:
                    model = load_model(args.model, args)
                audio, sr = sf.read(r["audio_filepath"], dtype="float32")
                if audio.ndim > 1:
                    raise ValueError(f"{r['audio_filepath']} is not mono")
                t0 = time.time()
                with torch.inference_mode(), torch.autocast("cuda", dtype=torch.bfloat16,
                                                            enabled=args.precision == "bf16"):
                    segs, probs = model.diarize(audio=[audio], batch_size=1, sample_rate=sr,
                                                include_tensor_outputs=True, verbose=False)
                wall = time.time() - t0
                turns = parse_segments(segs[0])
                write_rttm({uid: turns}, rttm_path)
                if not args.no_probs:
                    np.save(prob_path, probs[0].squeeze(0).float().cpu().numpy().astype(np.float16))
                dur = len(audio) / sr
                n_spk = len({t.speaker for t in turns})
                tf.write(f"{uid}\t{dur:.2f}\t{wall:.2f}\t{dur / wall:.1f}\t{n_spk}\n")
                tf.flush()
                print(f"[{name} {i}/{len(rows)}] {uid}: {dur / 60:.1f} min in {wall:.1f}s "
                      f"(RTFx {dur / wall:.0f}), {n_spk} speakers", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
