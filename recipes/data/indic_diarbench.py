#!/usr/bin/env python
"""Export Indic DiarBench (evaluation only, never used for training) to 16 kHz FLAC plus
segment-level reference RTTM/UEM.

The HF parquet files embed the audio. For each selected sample:
    <audio_out>/indic_diarbench/<cond>/<sample_id>/mix.flac
    <refs_out>/indic_diarbench/<cond>/rttm/segments/<sample_id>.rttm   (speaker segments as annotated)
    <refs_out>/indic_diarbench/<cond>/uem/<sample_id>.uem     (whole clip)
    <refs_out>/indic_diarbench/<cond>/samples.tsv             (sample -> recording_id, language, ...)
Speaker ids have whitespace replaced by '_'. Samples are clips of longer recordings: the card
asks to aggregate by `recording_id`, which samples.tsv provides.

Example (run in the `nemo` env, which has pyarrow):
    python recipes/data/indic_diarbench.py --condition "Far field"
"""
from __future__ import annotations

import argparse
import csv
import io
import re
import sys
from pathlib import Path

import numpy as np
import pyarrow.parquet as pq
import soundfile as sf
import soxr

TARGET_SR = 16000


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", type=Path, default=Path("/mnt/data/corpora/indic_diarbench"))
    ap.add_argument("--audio-out", type=Path, default=Path("/mnt/data/audio16k"))
    ap.add_argument("--refs-out", type=Path, default=Path("/mnt/data/refs"))
    ap.add_argument("--condition", default="Far field", choices=["Far field", "Near field", "In the wild"])
    ap.add_argument("--tol", type=float, default=0.010, help="max |duration difference| in seconds")
    args = ap.parse_args()

    cond = args.condition.lower().replace(" ", "_")
    audio_dir = args.audio_out / "indic_diarbench" / cond
    ref_dir = args.refs_out / "indic_diarbench" / cond
    (ref_dir / "rttm" / "segments").mkdir(parents=True, exist_ok=True)
    (ref_dir / "uem").mkdir(parents=True, exist_ok=True)

    rows, bad = [], []
    for pf in sorted(args.src.glob("*/*.parquet")):
        types = pq.read_table(pf, columns=["dataset_type"]).column(0).to_pylist()
        keep = [i for i, t in enumerate(types) if t == args.condition]
        if not keep:
            continue
        table = pq.read_table(pf).take(keep)
        for r in table.to_pylist():
            sid = r["sample_id"]
            audio, sr = sf.read(io.BytesIO(r["audio"]["bytes"]), dtype="float32", always_2d=True)
            audio = audio.mean(axis=1)
            if sr != TARGET_SR:
                audio = soxr.resample(audio, sr, TARGET_SR, quality="HQ")
            dst = audio_dir / sid / "mix.flac"
            dst.parent.mkdir(parents=True, exist_ok=True)
            sf.write(str(dst), np.clip(audio, -1.0, 1.0), TARGET_SR, format="FLAC", subtype="PCM_16")
            dur = sf.info(str(dst)).duration
            if abs(dur - r["duration_seconds"]) > args.tol:
                bad.append((sid, dur, r["duration_seconds"]))

            segs = r["annotated_transcript"]
            with open(ref_dir / "rttm" / "segments" / f"{sid}.rttm", "w") as f:
                for s in sorted(segs, key=lambda s: (s["start_time"], s["end_time"])):
                    d = s["end_time"] - s["start_time"]
                    if d > 0:
                        spk = re.sub(r"\s+", "_", s["speaker_id"].strip())
                        f.write(f"SPEAKER {sid} 1 {s['start_time']:.3f} {d:.3f} <NA> <NA> {spk} <NA> <NA>\n")
            with open(ref_dir / "uem" / f"{sid}.uem", "w") as f:
                f.write(f"{sid} 1 0.000 {dur:.3f}\n")
            n_spk = len({s["speaker_id"] for s in segs})
            rows.append((sid, r["recording_id"], r["language"], n_spk, len(segs), round(dur, 3)))
            print(f"  {sid} {r['language']} {dur / 60:.1f} min, {n_spk} spk", flush=True)

    with open(ref_dir / "samples.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["sample_id", "recording_id", "language", "num_speakers", "num_segments", "duration_s"])
        w.writerows(sorted(rows))
    hours = sum(r[5] for r in rows) / 3600
    over8 = sum(r[3] > 8 for r in rows)
    print(f"wrote {len(rows)} samples ({hours:.1f} h, {over8} with >8 speakers), "
          f"{len(bad)} duration mismatches -> {audio_dir}, {ref_dir}")
    for b in bad[:10]:
        print(f"  DUR_MISMATCH {b}", file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
