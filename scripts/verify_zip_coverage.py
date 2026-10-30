#!/usr/bin/env python
"""Check that files on disk can be recovered byte-for-byte from zip archives, before deleting them.

A file is covered when some member of one of the --zip archives has the same size and CRC-32
(read from the zip central directory). Matching is by content, not name, so files renamed after
extraction (e.g. the EAR-1 speaker-ID corrections in recipes/data/ear1_prepare.py) still match.
Writes the covered paths to --covered (one per line) and prints the uncovered ones; exit 1 if any.

    python scripts/verify_zip_coverage.py --zip "/mnt/data/raw/ear1/Train&Dev.zip" --zip /mnt/data/raw/ear1/correct.zip \
        --covered covered.txt files...
"""
from __future__ import annotations

import argparse
import sys
import zipfile
import zlib
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path


def crc32(path: Path) -> tuple[int, int]:
    crc = 0
    with path.open("rb") as f:
        while chunk := f.read(1 << 24):
            crc = zlib.crc32(chunk, crc)
    return path.stat().st_size, crc


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", type=Path, nargs="*", help="files to check (or --files-from)")
    ap.add_argument("--files-from", type=Path, help="text file with one path per line")
    ap.add_argument("--zip", type=Path, action="append", required=True)
    ap.add_argument("--covered", type=Path, required=True)
    ap.add_argument("--jobs", type=int, default=6)
    args = ap.parse_args()
    files = list(args.files) + ([Path(x) for x in args.files_from.read_text().splitlines() if x.strip()] if args.files_from else [])
    members = {(i.file_size, i.CRC) for z in args.zip for i in zipfile.ZipFile(z).infolist() if not i.is_dir()}
    covered, missing = [], []
    with ProcessPoolExecutor(args.jobs) as ex:
        for p, key in zip(files, ex.map(crc32, files, chunksize=4)):
            (covered if key in members else missing).append(p)
    args.covered.write_text("".join(f"{p}\n" for p in covered))
    for p in missing:
        print(f"UNCOVERED {p}")
    gb = sum(p.stat().st_size for p in covered) / 2**30
    print(f"{len(covered)} covered ({gb:.1f} GB), {len(missing)} uncovered, of {len(files)}")
    return int(bool(missing) or not files)


if __name__ == "__main__":
    sys.exit(main())
