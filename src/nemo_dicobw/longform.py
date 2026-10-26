"""Long-form windowing for Whisper-family decoding on diarized audio.

windows        <= max_len s windows whose boundaries fall in silences of the given speech
               intervals (the union of all speakers for whole-audio decoding, the target speaker
               for per-speaker decoding). A run of speech longer than a window is cut at the
               lowest-energy 100 ms within its last `search` seconds.
target_mask    sample gain for a per-speaker window: 0 where only non-target speakers are active
               (target-only, overlap and silence are kept), with `ramp` s linear ramps.
stno_mask      DiCoW conditioning at 50 Hz for one target speaker over a window:
               rows (silence, target only, non-target only, overlap).
"""
from __future__ import annotations

import numpy as np

from nemo_dicobw.rttm import Interval, intersect_intervals, merge_intervals, subtract_intervals

SR = 16000


def _cut_point(audio: np.ndarray | None, lo: float, hi: float) -> float:
    if audio is None or hi - lo < 0.2:
        return hi
    a, b = int(lo * SR), min(len(audio), int(hi * SR))
    hop = SR // 10
    n = (b - a) // hop
    if n < 1:
        return hi
    e = (audio[a:a + n * hop].reshape(n, hop) ** 2).mean(axis=1)
    return lo + (int(np.argmin(e)) + 0.5) * hop / SR


def windows(speech: list[Interval], rec_end: float, audio: np.ndarray | None = None, max_len: float = 30.0,
            pad: float = 0.3, search: float = 8.0) -> list[Interval]:
    """Windows covering all `speech`, each <= max_len, cut in silences where possible."""
    runs: list[Interval] = []
    for s, e in merge_intervals(speech):  # split runs longer than one window
        while e - s > max_len - 2 * pad:
            c = _cut_point(audio, s + max_len - 2 * pad - search, s + max_len - 2 * pad)
            runs.append((s, c))
            s = c
        runs.append((s, e))
    out: list[Interval] = []
    i = 0
    while i < len(runs):
        start = max(0.0, runs[i][0] - pad, out[-1][1] if out else 0.0)
        j = i
        while j + 1 < len(runs) and runs[j + 1][1] + pad - start <= max_len:
            j += 1
        end = min(rec_end, runs[j][1] + pad, start + max_len)
        if j + 1 < len(runs):
            end = min(end, (runs[j][1] + runs[j + 1][0]) / 2) if runs[j + 1][0] > runs[j][1] else min(end, runs[j][1])
        out.append((start, max(end, runs[j][1]) if runs[j][1] - start <= max_len else end))
        i = j + 1
    return out


def target_mask(win: Interval, target: list[Interval], others: list[Interval], ramp: float = 0.02,
                n: int | None = None) -> np.ndarray:
    """Per-sample gain over `win` (n samples, default from the window length): 0 where only non-target
    speakers speak."""
    ws, we = win
    n = n if n is not None else int(round((we - ws) * SR))
    g = np.ones(n, np.float32)
    r = max(1, int(ramp * SR))
    for s, e in subtract_intervals(intersect_intervals(merge_intervals(others), [win]), merge_intervals(target)):
        a, b = int((s - ws) * SR), int((e - ws) * SR)
        g[a:b] = 0.0
        g[max(0, a - r):a] = np.minimum(g[max(0, a - r):a], np.linspace(1, 0, a - max(0, a - r), dtype=np.float32))
        g[b:b + r] = np.minimum(g[b:b + r], np.linspace(0, 1, len(g[b:b + r]), dtype=np.float32))
    return g


def stno_mask(win: Interval, target: list[Interval], others: list[Interval], frames: int = 1500, rate: int = 50) -> np.ndarray:
    """(4, frames) silence / target-only / non-target-only / overlap at `rate` Hz, padded as silence."""
    ws, we = win
    n = min(frames, int(round((we - ws) * rate)))
    t = np.zeros(n, bool)
    o = np.zeros(n, bool)
    for arr, ivs in ((t, target), (o, others)):
        for s, e in intersect_intervals(merge_intervals(ivs), [win]):
            arr[int((s - ws) * rate):int(np.ceil((e - ws) * rate))] = True
    m = np.zeros((4, frames), np.float32)
    m[0, :n], m[1, :n], m[2, :n], m[3, :n] = ~t & ~o, t & ~o, ~t & o, t & o
    m[0, n:] = 1.0
    return m
