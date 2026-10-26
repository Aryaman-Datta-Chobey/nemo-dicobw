"""RTTM and UEM reading/writing.

RTTM (NIST rich transcription) lines used here:
    SPEAKER <file> <chan> <start> <dur> <NA> <NA> <speaker> <NA> <NA>
UEM lines:
    <file> <chan> <start> <end>

Only SPEAKER lines are read; other RTTM types are ignored. Times are seconds.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

Interval = tuple[float, float]


@dataclass(frozen=True)
class Turn:
    speaker: str
    start: float
    end: float

    @property
    def dur(self) -> float:
        return self.end - self.start


def _expand(paths: str | Path | Iterable[str | Path], suffix: str) -> list[Path]:
    """A path may be a file, or a directory searched recursively for `*<suffix>`."""
    if isinstance(paths, (str, Path)):
        paths = [paths]
    out: list[Path] = []
    for p in map(Path, paths):
        if p.is_dir():
            out.extend(sorted(p.rglob(f"*{suffix}")))
        elif p.is_file():
            out.append(p)
        else:
            raise FileNotFoundError(p)
    return out


def load_rttm(paths: str | Path | Iterable[str | Path]) -> dict[str, list[Turn]]:
    """Read one or more RTTM files (or directories of them) into {file_id: [Turn, ...]}."""
    turns: dict[str, list[Turn]] = defaultdict(list)
    for path in _expand(paths, ".rttm"):
        with open(path) as f:
            for lineno, line in enumerate(f, 1):
                fields = line.split()
                if not fields or fields[0] != "SPEAKER":
                    continue
                if len(fields) < 8:
                    raise ValueError(f"{path}:{lineno}: malformed RTTM line: {line.rstrip()}")
                start, dur = float(fields[3]), float(fields[4])
                if dur < 0:
                    raise ValueError(f"{path}:{lineno}: negative duration")
                if dur > 0:
                    turns[fields[1]].append(Turn(fields[7], start, start + dur))
    return {k: sorted(v, key=lambda t: (t.start, t.end, t.speaker)) for k, v in turns.items()}


def load_uem(paths: str | Path | Iterable[str | Path]) -> dict[str, list[Interval]]:
    """Read one or more UEM files into {file_id: [(start, end), ...]} (merged, sorted)."""
    uem: dict[str, list[Interval]] = defaultdict(list)
    for path in _expand(paths, ".uem"):
        with open(path) as f:
            for lineno, line in enumerate(f, 1):
                fields = line.split()
                if not fields or fields[0].startswith(";"):
                    continue
                if len(fields) < 4:
                    raise ValueError(f"{path}:{lineno}: malformed UEM line: {line.rstrip()}")
                uem[fields[0]].append((float(fields[2]), float(fields[3])))
    return {k: merge_intervals(v) for k, v in uem.items()}


def write_rttm(turns: dict[str, list[Turn]], path: str | Path) -> None:
    with open(path, "w") as f:
        for file_id in sorted(turns):
            for t in turns[file_id]:
                f.write(f"SPEAKER {file_id} 1 {t.start:.3f} {t.dur:.3f} <NA> <NA> {t.speaker} <NA> <NA>\n")


def write_uem(uem: dict[str, list[Interval]], path: str | Path) -> None:
    with open(path, "w") as f:
        for file_id in sorted(uem):
            for s, e in uem[file_id]:
                f.write(f"{file_id} 1 {s:.3f} {e:.3f}\n")


def merge_intervals(intervals: Iterable[Interval], gap: float = 0.0) -> list[Interval]:
    """Union of intervals; intervals separated by at most `gap` seconds are joined."""
    out: list[list[float]] = []
    for s, e in sorted(intervals):
        if e <= s:
            continue
        if out and s - out[-1][1] <= gap:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return [(s, e) for s, e in out]


def intersect_intervals(a: list[Interval], b: list[Interval]) -> list[Interval]:
    """Intersection of two sorted, disjoint interval lists."""
    out: list[Interval] = []
    i = j = 0
    while i < len(a) and j < len(b):
        s, e = max(a[i][0], b[j][0]), min(a[i][1], b[j][1])
        if s < e:
            out.append((s, e))
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return out


def subtract_intervals(a: list[Interval], b: list[Interval]) -> list[Interval]:
    """`a` minus `b`, both sorted and disjoint."""
    out: list[Interval] = []
    j = 0
    for s, e in a:
        cur = s
        while j < len(b) and b[j][1] <= cur:
            j += 1
        k = j
        while k < len(b) and b[k][0] < e:
            if b[k][0] > cur:
                out.append((cur, b[k][0]))
            cur = max(cur, b[k][1])
            k += 1
        if cur < e:
            out.append((cur, e))
    return out
