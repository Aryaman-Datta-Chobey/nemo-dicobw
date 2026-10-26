"""Late fusion: attribute time-stamped characters from speaker-agnostic ASR to diarized speakers.

Each character (absolute time t) goes to the speaker active at t. If several are active, the one with
the highest diarizer probability at t (when per-frame probabilities are given, 10 ms frames, column
k = speaker_k) else the one whose turn started last. If none is active, the speaker with the nearest
turn. Consecutive characters of one speaker, with gaps <= max_gap, form one SegLST segment
[first char time, last char time + last char duration]; a character lasts until the next character
(at most max_char s).
"""
from __future__ import annotations

import bisect

import numpy as np

from nemo_dicobw.rttm import Turn


def assign(chars: list[tuple[float, str]], turns: list[Turn], probs: np.ndarray | None = None,
           frame: float = 0.01) -> list[str]:
    starts = sorted(turns, key=lambda x: x.start)
    keys = [x.start for x in starts]
    out = []
    for t, _ in chars:
        lo = bisect.bisect_right(keys, t)
        active = [x for x in starts[max(0, lo - 64):lo] if x.start <= t < x.end]
        if len(active) > 1 and probs is not None:
            f = min(len(probs) - 1, int(t / frame))
            active.sort(key=lambda x: -probs[f, int(x.speaker.rsplit("_", 1)[-1])])
        elif len(active) > 1:
            active.sort(key=lambda x: -x.start)
        if active:
            out.append(active[0].speaker)
        elif starts:
            out.append(min(starts, key=lambda x: max(x.start - t, t - x.end, 0.0)).speaker)
        else:
            out.append("unknown")
    return out


def segments(chars: list[tuple[float, str]], speakers: list[str], session: str, max_gap: float = 1.0,
             max_char: float = 0.5) -> list[dict]:
    order = sorted(range(len(chars)), key=lambda i: chars[i][0])
    segs: list[dict] = []
    for n, i in enumerate(order):
        t, text = chars[i]
        nxt = chars[order[n + 1]][0] if n + 1 < len(order) else t + max_char
        end = t + min(max(nxt - t, 0.02), max_char)
        spk = speakers[i]
        last = next((s for s in reversed(segs) if s["speaker"] == spk), None)
        if last is not None and last is segs[-1] and t - last["end_time"] <= max_gap:
            last["end_time"] = round(end, 3)
            last["words"] += (" " if text.isascii() and last["words"][-1:].isascii() else "") + text
        else:
            segs.append({"session_id": session, "speaker": spk, "start_time": round(t, 3), "end_time": round(end, 3), "words": text})
    return segs
