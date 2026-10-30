#!/usr/bin/env python
"""Convert a corpus' audio to 16 kHz mono FLAC, one file per channel.

Output layout: <out_root>/<corpus>/<split>/<session>/<channel>.flac

Every output is re-read and its duration compared with the source (default tolerance
10 ms). Results go to <out_root>/<corpus>/<--report-name> (default conversion_report.tsv),
which is rewritten on each run and covers only the files selected by that run. Re-running is safe: outputs that already
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
import functools
import re
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


# A layout maps a source file (relative to --src, plus --src itself) to (split, session, channel).
Layout = Callable[[Path, Path], tuple[str, str, str]]


def layout_split_session_channel(rel: Path, src: Path) -> tuple[str, str, str]:
    """<split>/.../<session>/<channel>.wav, e.g. AISHELL-5 Dev/001/DX01C01.wav."""
    if len(rel.parts) < 3:
        raise ValueError(f"expected <split>/.../<session>/<file>, got {rel}")
    return rel.parts[0], rel.parent.name, rel.stem


def layout_alimeeting(rel: Path, src: Path) -> tuple[str, str, str]:
    """Eval_Ali/Eval_Ali_far/audio_dir/R8001_M8004_MS801.wav -> (Eval_Ali, R8001_M8004, far);
    the 8-channel far file becomes far_ch1..far_ch8. Near-field
    Eval_Ali/Eval_Ali_near/audio_dir/R8001_M8004_N_SPK8013.wav -> (Eval_Ali, R8001_M8004, N_SPK8013)."""
    parts = rel.stem.split("_")
    if len(parts) < 3 or not rel.parts[1].endswith(("_far", "_near")):
        raise ValueError(f"unexpected AliMeeting path {rel}")
    session = "_".join(parts[:2])
    channel = "far" if rel.parts[1].endswith("_far") else "_".join(parts[2:])
    return rel.parts[0], session, channel


def layout_notsofar(rel: Path, src: Path) -> tuple[str, str, str]:
    """benchmark-datasets/eval_set/<version>/MTG/MTG_32000/sc_plaza_0/ch0.wav -> (eval, MTG_32000, sc_plaza_0);
    mc_<dev>/chN.wav -> mc_<dev>_chN; close_talk/CT_20.wav -> CT_20."""
    split = rel.parts[1].removesuffix("_set")
    session = next(p for p in rel.parts if p.startswith("MTG_"))
    device = rel.parent.name
    if device == "close_talk":
        channel = rel.stem
    elif device.startswith("sc_"):
        channel = device
    else:
        channel = f"{device}_{rel.stem}"
    return split, session, channel


def layout_aishell4(rel: Path, src: Path) -> tuple[str, str, str]:
    """test/wav/L_R003S04C02.flac (8-channel array) -> (test, L_R003S04C02, far) -> far_ch1..far_ch8."""
    if len(rel.parts) != 3 or rel.parts[1] != "wav":
        raise ValueError(f"unexpected AISHELL-4 path {rel}")
    return rel.parts[0], rel.stem, "far"


def layout_chime6(rel: Path, src: Path) -> tuple[str, str, str]:
    """.../audio/<split>/S02_U01.CH1.wav -> (<split>, S02, U01.CH1); binaural S02_P05.wav -> P05 (-> P05_ch1/2)."""
    session, _, channel = rel.stem.partition("_")
    if not channel or rel.parent.name not in ("train", "dev", "eval"):
        raise ValueError(f"unexpected CHiME-6 path {rel}")
    return rel.parent.name, session, channel


@functools.cache
def _egocom_splits(src: Path) -> dict[str, str]:
    """video_name -> train/val/test from annotations/video_info.csv (split by conversation)."""
    with open(src / "annotations" / "video_info.csv") as f:
        return {r["video_name"]: next(k for k in ("train", "val", "test") if r[k] == "True")
                for r in csv.DictReader(f)}


def layout_egocom(rel: Path, src: Path) -> tuple[str, str, str]:
    """egocom_audio_only/vid_013__day_1__con_1__person_3_part3.wav -> (test, day_1__con_1__part3, person_3)."""
    m = re.fullmatch(r"vid_\d+__(day_\d+__con_\d+)__(person_\d+)(?:_(part\d+))?", rel.stem)
    if not m:
        raise ValueError(f"unexpected EgoCom path {rel}")
    session = m.group(1) + (f"__{m.group(3)}" if m.group(3) else "")
    return _egocom_splits(src)[rel.stem], session, m.group(2)


@functools.cache
def _ear1_splits(src: Path) -> dict[str, str]:
    """session -> train/dev from <src>/split.lst (written by recipes/data/ear1_prepare.py)."""
    out, cur = {}, None
    for ln in (src / "split.lst").read_text(encoding="utf-8").splitlines():
        s = ln.strip().replace("\uff1a", ":").lower()
        if s in ("train set:", "dev set:"):
            cur = s.split()[0]
        elif s and cur:
            out[ln.strip()] = cur
    return out


def layout_ear1(rel: Path, src: Path) -> tuple[str, str, str]:
    """<session>/D1.WAV -> (dev|train, <session>, D1); <session>/A/P006.WAV -> (.., <session>, P006)."""
    session = rel.parts[0]
    if session not in _ear1_splits(src) or len(rel.parts) not in (2, 3):
        raise ValueError(f"unexpected EAR-1 path {rel}")
    return _ear1_splits(src)[session], session, rel.stem


@functools.cache
def _ami_splits(src: Path) -> dict[str, str]:
    """meeting -> train/dev/test from <src>/partition.tsv (written by scripts/download_ami.sh)."""
    return dict(ln.split("\t")[::-1] for ln in (src / "partition.tsv").read_text().split("\n") if ln.strip())


def layout_ami(rel: Path, src: Path) -> tuple[str, str, str]:
    """<meeting>/audio/<meeting>.Array1-01.wav -> (train|dev|test, <meeting>, Array1-01)."""
    meeting, _, mic = rel.stem.partition(".")
    if len(rel.parts) != 3 or meeting != rel.parts[0] or meeting not in _ami_splits(src):
        raise ValueError(f"unexpected AMI path {rel}")
    return _ami_splits(src)[meeting], meeting, mic


def layout_icsi(rel: Path, src: Path) -> tuple[str, str, str]:
    """Signals/<meeting>/<meeting>.interaction.wav -> (train, <meeting>, mix). ICSI is training-only here."""
    if len(rel.parts) != 3 or rel.parts[0] != "Signals" or rel.name != f"{rel.parts[1]}.interaction.wav":
        raise ValueError(f"unexpected ICSI path {rel}")
    return "train", rel.parts[1], "mix"


LAYOUTS: dict[str, Layout] = {
    "ami": layout_ami,
    "ear1": layout_ear1,
    "icsi": layout_icsi,
    "aishell4": layout_aishell4,
    "aishell5": layout_split_session_channel,
    "alimeeting": layout_alimeeting,
    "chime6": layout_chime6,
    "egocom": layout_egocom,
    "notsofar": layout_notsofar,
}


def iter_jobs(src: Path, out: Path, corpus: str, layout: Layout, includes: list[str],
              excludes: list[str], downmix: bool, splits: list[str] | None = None) -> Iterator[Job]:
    for path in sorted(src.rglob("*")):
        # skip dotfiles, e.g. macOS AppleDouble "._x.wav" in the EgoCom archive
        if path.suffix.lower() not in AUDIO_EXTS or path.name.startswith(".") or not path.is_file():
            continue
        rel = path.relative_to(src)
        if includes and not any(fnmatch.fnmatch(str(rel), pat) for pat in includes):
            continue
        if any(fnmatch.fnmatch(str(rel), pat) for pat in excludes):
            continue
        split, session, channel = layout(rel, src)
        if splits and split not in splits:
            continue
        yield Job(path, out / corpus / split / session / channel, downmix)


def outputs_for(job: Job, n_channels: int) -> list[Path]:
    if job.downmix or n_channels == 1:
        return [job.dst_stem.with_name(f"{job.dst_stem.name}.flac")]  # channel names may contain dots (U01.CH1)
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
    ap.add_argument("--split", action="append", default=[],
                    help="only convert files the layout assigns to this split, e.g. test (repeatable)")
    ap.add_argument("--downmix", action="store_true", help="average channels instead of splitting them")
    ap.add_argument("--tol", type=float, default=0.010, help="max |duration difference| in seconds")
    ap.add_argument("--report-name", default="conversion_report.tsv",
                    help="report file name under <out>/<corpus>/, e.g. conversion_report.eval.tsv")
    args = ap.parse_args(argv)

    jobs = list(iter_jobs(args.src, args.out, args.corpus, LAYOUTS[args.corpus],
                          args.include, args.exclude, args.downmix, args.split))
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

    report = args.out / args.corpus / args.report_name
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
