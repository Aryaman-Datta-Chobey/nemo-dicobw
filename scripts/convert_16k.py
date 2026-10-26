#!/usr/bin/env python
"""Convert a corpus' audio to 16 kHz mono FLAC, one file per channel.

Output layout: <out_root>/<corpus>/<split>/<session>/<channel>.flac

Every output is re-read and its duration compared with the source (default tolerance
10 ms). Results go to <out_root>/<corpus>/conversion_report.tsv, which is rewritten on each
run and covers only the files selected by that run. Re-running is safe: outputs that already
exist with a matching duration are skipped. Use --include to restrict a run to splits that
have finished extracting.

Example (run in the `dicow` env):
    python scripts/convert_16k.py --corpus aishell5 \
        --src /mnt/data/corpora/aishell5 --out /mnt/data/audio16k --jobs 10 \
        --include 'Dev/*' --include 'Eval1/*'
"""
from __future__ import annotations

import argparse
import csv
import fnmatch
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterator

import numpy as np
import soundfile as sf
import soxr

TARGET_SR = 16000
AUDIO_EXTS = {".wav", ".flac"}


@dataclass(frozen=True)
class Job:
    src: Path
    dst_stem: Path  # <out>/<corpus>/<split>/<session>/<channel>, no extension
    downmix: bool


# A layout maps a source file (relative to --src) to (split, session, channel).
Layout = Callable[[Path], tuple[str, str, str]]


def layout_split_session_channel(rel: Path) -> tuple[str, str, str]:
    """<split>/.../<session>/<channel>.wav, e.g. AISHELL-5 Dev/001/DX01C01.wav."""
    if len(rel.parts) < 3:
        raise ValueError(f"expected <split>/.../<session>/<file>, got {rel}")
    return rel.parts[0], rel.parent.name, rel.stem


LAYOUTS: dict[str, Layout] = {
    "aishell5": layout_split_session_channel,
}


def iter_jobs(src: Path, out: Path, corpus: str, layout: Layout,
              includes: list[str], excludes: list[str], downmix: bool) -> Iterator[Job]:
    for path in sorted(src.rglob("*")):
        if path.suffix.lower() not in AUDIO_EXTS or not path.is_file():
            continue
        rel = path.relative_to(src)
        if includes and not any(fnmatch.fnmatch(str(rel), pat) for pat in includes):
            continue
        if any(fnmatch.fnmatch(str(rel), pat) for pat in excludes):
            continue
        split, session, channel = layout(rel)
        yield Job(path, out / corpus / split / session / channel, downmix)


def outputs_for(job: Job, n_channels: int) -> list[Path]:
    if job.downmix or n_channels == 1:
        return [job.dst_stem.with_suffix(".flac")]
    return [job.dst_stem.with_name(f"{job.dst_stem.name}_ch{c + 1}.flac") for c in range(n_channels)]


def convert(job: Job, tol: float) -> list[tuple[str, str, float, float, str]]:
    """Convert one source file; returns report rows (src, dst, src_dur, dst_dur, status)."""
    info = sf.info(str(job.src))
    src_dur = info.frames / info.samplerate
    dsts = outputs_for(job, info.channels)

    def dur_ok(p: Path) -> float | None:
        if not p.exists():
            return None
        d = sf.info(str(p)).duration
        return d if abs(d - src_dur) <= tol else None

    done = [dur_ok(p) for p in dsts]
    if all(d is not None for d in done):
        return [(str(job.src), str(p), src_dur, d, "skip") for p, d in zip(dsts, done)]

    audio, sr = sf.read(str(job.src), dtype="float32", always_2d=True)  # (frames, channels)
    if job.downmix:
        audio = audio.mean(axis=1, keepdims=True)
    if sr != TARGET_SR:
        audio = soxr.resample(audio, sr, TARGET_SR, quality="HQ")
    audio = np.clip(audio, -1.0, 1.0)

    rows = []
    for c, dst in enumerate(dsts):
        dst.parent.mkdir(parents=True, exist_ok=True)
        tmp = dst.with_suffix(".flac.tmp")
        sf.write(str(tmp), audio[:, c], TARGET_SR, format="FLAC", subtype="PCM_16")
        tmp.rename(dst)
        d = sf.info(str(dst)).duration
        rows.append((str(job.src), str(dst), src_dur, d, "ok" if abs(d - src_dur) <= tol else "DUR_MISMATCH"))
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--corpus", required=True, choices=sorted(LAYOUTS))
    ap.add_argument("--src", type=Path, required=True, help="extracted corpus root")
    ap.add_argument("--out", type=Path, default=Path("/mnt/data/audio16k"))
    ap.add_argument("--jobs", type=int, default=10)
    ap.add_argument("--include", action="append", default=[],
                    help="only convert paths (relative to --src) matching this glob, e.g. 'Dev/*' (repeatable)")
    ap.add_argument("--exclude", action="append", default=[], help="glob on path relative to --src (repeatable)")
    ap.add_argument("--downmix", action="store_true", help="average channels instead of splitting them")
    ap.add_argument("--tol", type=float, default=0.010, help="max |duration difference| in seconds")
    args = ap.parse_args(argv)

    jobs = list(iter_jobs(args.src, args.out, args.corpus, LAYOUTS[args.corpus],
                          args.include, args.exclude, args.downmix))
    if not jobs:
        print(f"no audio found under {args.src}", file=sys.stderr)
        return 1
    print(f"{len(jobs)} source files -> {args.out / args.corpus} with {args.jobs} workers", flush=True)

    rows, failed = [], []
    with ProcessPoolExecutor(max_workers=args.jobs) as pool:
        futs = {pool.submit(convert, j, args.tol): j for j in jobs}
        for i, fut in enumerate(as_completed(futs), 1):
            try:
                rows.extend(fut.result())
            except Exception as e:  # keep going; report at the end
                failed.append((futs[fut].src, repr(e)))
            if i % 100 == 0 or i == len(jobs):
                print(f"  {i}/{len(jobs)} files", flush=True)

    report = args.out / args.corpus / "conversion_report.tsv"
    report.parent.mkdir(parents=True, exist_ok=True)
    with report.open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["src", "dst", "src_dur", "dst_dur", "status"])
        w.writerows(sorted(rows))
        w.writerows((str(s), "", "", "", f"ERROR {e}") for s, e in failed)

    mismatches = [r for r in rows if r[4] == "DUR_MISMATCH"]
    hours = sum(r[3] for r in rows) / 3600
    print(f"wrote {len(rows)} files ({hours:.1f} h), {len(mismatches)} duration mismatches, "
          f"{len(failed)} errors; report: {report}")
    for s, e in failed[:10]:
        print(f"  ERROR {s}: {e}", file=sys.stderr)
    return 1 if (failed or mismatches) else 0


if __name__ == "__main__":
    sys.exit(main())
