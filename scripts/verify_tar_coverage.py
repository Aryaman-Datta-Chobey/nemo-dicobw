#!/usr/bin/env python
"""Check that every file in a corpus tarball survives on disk, before deleting the tarball.

A member counts as covered when the same relative path exists under --corpora with the same size, or
(for .wav) when its 16 kHz FLAC under --audio16k is listed "ok" in a conversion_report*.tsv there.
Prints counts and the uncovered members; exit 1 if any member is uncovered.
"""
from __future__ import annotations

import argparse
import tarfile
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("tarballs", type=Path, nargs="+")
    ap.add_argument("--corpora", type=Path, required=True)
    ap.add_argument("--audio16k", type=Path, required=True)
    args = ap.parse_args()
    converted = set()
    for rep in args.audio16k.glob("conversion_report*.tsv"):
        for line in rep.read_text().splitlines()[1:]:
            src, dst, *_, status = line.split("\t")
            if status == "ok" and Path(dst).exists():
                converted.add(Path(src).resolve())
    bad = 0
    for tb in args.tarballs:
        n = {"same": 0, "converted": 0, "missing": 0}
        with tarfile.open(tb, "r|gz") as tf:
            for m in tf:
                if not m.isfile():
                    continue
                p = args.corpora / m.name
                if p.exists() and p.stat().st_size == m.size:
                    n["same"] += 1
                elif p.resolve() in converted:
                    n["converted"] += 1
                else:
                    n["missing"] += 1
                    if n["missing"] <= 20:
                        print(f"MISSING {tb.name}: {m.name} ({m.size} B)")
        bad += n["missing"]
        print(f"{tb.name}: {n}", flush=True)
    print("COVERED" if bad == 0 else f"UNCOVERED {bad}")
    return int(bad > 0)


if __name__ == "__main__":
    raise SystemExit(main())
