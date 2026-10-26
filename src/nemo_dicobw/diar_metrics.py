"""Exact (interval-based, no frame quantisation) DER and JER.

Every reference/hypothesis/score-region boundary splits the timeline into elementary
intervals on which the set of active speakers is constant, so all metrics are exact sums
over those intervals.

DER follows NIST md-eval-22.pl: overlap is scored; a collar of `c` seconds removes
[t - c, t + c] around every reference turn boundary from the scored region (as in md-eval,
boundaries between touching or overlapping turns of the same speaker also get a collar,
while speaker time is the per-speaker union, so such overlaps are not double counted);
speakers are mapped one-to-one to maximise the total matched time on the scored region.
Per interval with N_ref, N_hyp active speakers and N_corr correctly mapped pairs:
    miss = max(0, N_ref - N_hyp), fa = max(0, N_hyp - N_ref), conf = min(N_ref, N_hyp) - N_corr
and DER = (miss + fa + conf) / sum(N_ref), all weighted by duration.

JER follows dscore (github.com/nryant/dscore): per reference speaker 1 - |R n H| / |R u H|
under the one-to-one mapping that minimises the summed per-speaker JER; unmapped
reference speakers score 1. The file JER is the mean over its reference speakers and the
global JER is the mean over all reference speakers pooled across files. dscore itself
applies no collar to JER; here JER is computed on the same scored region as DER, so at
collar 0 it equals dscore's and at collar > 0 it is the collar-consistent extension.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

import numpy as np
from scipy.optimize import linear_sum_assignment

from nemo_dicobw.rttm import Interval, Turn, merge_intervals, subtract_intervals


@dataclass
class Activity:
    """Speaker activity on the elementary intervals of a scored region."""

    starts: np.ndarray  # (n,) interval start times
    durs: np.ndarray  # (n,) interval durations
    ref: np.ndarray  # (n, n_ref) bool
    hyp: np.ndarray  # (n, n_hyp) bool
    ref_speakers: list[str]
    hyp_speakers: list[str]


def merge_speaker_turns(turns: Iterable[Turn]) -> dict[str, list[Interval]]:
    """Per-speaker union of turns (overlapping or touching same-speaker turns are joined)."""
    by_spk: dict[str, list[Interval]] = {}
    for t in turns:
        by_spk.setdefault(t.speaker, []).append((t.start, t.end))
    return {spk: merge_intervals(iv) for spk, iv in by_spk.items()}


def build_activity(
    ref: dict[str, list[Interval]], hyp: dict[str, list[Interval]], regions: list[Interval]
) -> Activity:
    points = [p for r in regions for p in r]
    for side in (ref, hyp):
        points.extend(p for ivs in side.values() for iv in ivs for p in iv)
    grid = np.unique(np.asarray(points, dtype=np.float64))
    if grid.size < 2:
        empty = np.zeros(0)
        return Activity(empty, empty, np.zeros((0, len(ref)), bool), np.zeros((0, len(hyp)), bool),
                        list(ref), list(hyp))
    n = grid.size - 1

    def mask(ivs: list[Interval]) -> np.ndarray:
        m = np.zeros(n, dtype=bool)
        for s, e in ivs:
            m[np.searchsorted(grid, s):np.searchsorted(grid, e)] = True
        return m

    keep = mask(regions)
    ref_spk, hyp_spk = sorted(ref), sorted(hyp)
    R = np.stack([mask(ref[s]) for s in ref_spk], axis=1) if ref_spk else np.zeros((n, 0), bool)
    H = np.stack([mask(hyp[s]) for s in hyp_spk], axis=1) if hyp_spk else np.zeros((n, 0), bool)
    return Activity(grid[:-1][keep], np.diff(grid)[keep], R[keep], H[keep], ref_spk, hyp_spk)


def collar_regions(uem: list[Interval], ref_turns: Iterable[Turn], collar: float) -> list[Interval]:
    """UEM minus +-collar around every reference turn boundary (raw turns, not merged)."""
    if collar <= 0:
        return list(uem)
    zones = [(t - collar, t + collar) for tr in ref_turns for t in (tr.start, tr.end)]
    return subtract_intervals(uem, merge_intervals(zones))


@dataclass
class FileDiarScore:
    scored_time: float  # duration of the scored region
    ref_speech: float  # reference speaker time (DER denominator)
    miss: float
    fa: float
    conf: float
    n_ref_speakers: int  # speakers with scored time
    n_hyp_speakers: int
    speaker_jer: dict[str, float]  # reference speaker -> JER in [0, 1]
    mapping: dict[str, str]  # reference speaker -> hypothesis speaker (DER mapping)
    jer_no_ref_speech: bool = False  # dscore: such a file has JER 100 but adds no speakers

    @property
    def der(self) -> float | None:
        return (self.miss + self.fa + self.conf) / self.ref_speech if self.ref_speech > 0 else None

    @property
    def jer(self) -> float | None:
        if self.speaker_jer:
            return float(np.mean(list(self.speaker_jer.values())))
        return 1.0 if self.jer_no_ref_speech else None


def score_activity(act: Activity) -> FileDiarScore:
    d, R, H = act.durs, act.ref.astype(np.float64), act.hyp.astype(np.float64)
    ref_dur, hyp_dur = d @ R, d @ H
    r_live, h_live = ref_dur > 0, hyp_dur > 0
    R, H, ref_dur, hyp_dur = R[:, r_live], H[:, h_live], ref_dur[r_live], hyp_dur[h_live]
    ref_spk = [s for s, k in zip(act.ref_speakers, r_live) if k]
    hyp_spk = [s for s, k in zip(act.hyp_speakers, h_live) if k]

    cooc = (R * d[:, None]).T @ H  # (n_ref, n_hyp) jointly active time
    n_ref, n_hyp = R.sum(1), H.sum(1)
    n_corr = np.zeros_like(d)
    mapping: dict[str, str] = {}
    if cooc.size:
        for i, j in zip(*linear_sum_assignment(cooc, maximize=True)):
            if cooc[i, j] > 0:
                mapping[ref_spk[i]] = hyp_spk[j]
                n_corr += R[:, i] * H[:, j]

    speaker_jer: dict[str, float] = {}
    if ref_spk:
        speaker_jer = {s: 1.0 for s in ref_spk}
        if hyp_spk:
            jer_m = 1.0 - cooc / (ref_dur[:, None] + hyp_dur[None, :] - cooc)
            for i, j in zip(*linear_sum_assignment(jer_m)):
                speaker_jer[ref_spk[i]] = float(jer_m[i, j])

    return FileDiarScore(
        scored_time=float(d.sum()),
        ref_speech=float(d @ n_ref),
        miss=float(d @ np.maximum(0, n_ref - n_hyp)),
        fa=float(d @ np.maximum(0, n_hyp - n_ref)),
        conf=float(d @ (np.minimum(n_ref, n_hyp) - n_corr)),
        n_ref_speakers=len(ref_spk),
        n_hyp_speakers=len(hyp_spk),
        speaker_jer=speaker_jer,
        mapping=mapping,
        jer_no_ref_speech=not ref_spk and bool(hyp_spk),
    )


def score_file(
    ref_turns: list[Turn], hyp_turns: list[Turn], uem: list[Interval], collar: float = 0.0
) -> FileDiarScore:
    ref, hyp = merge_speaker_turns(ref_turns), merge_speaker_turns(hyp_turns)
    return score_activity(build_activity(ref, hyp, collar_regions(uem, ref_turns, collar)))


@dataclass
class DiarSummary:
    files: dict[str, FileDiarScore] = field(default_factory=dict)

    def overall(self) -> dict[str, float | int | None]:
        f = list(self.files.values())
        ref_speech = sum(x.ref_speech for x in f)
        miss, fa, conf = (sum(getattr(x, k) for x in f) for k in ("miss", "fa", "conf"))
        spk_jers = [j for x in f for j in x.speaker_jer.values()]
        if spk_jers:
            jer = float(np.mean(spk_jers))
        else:
            jer = 1.0 if any(x.jer_no_ref_speech for x in f) else None
        count_err = [x.n_hyp_speakers - x.n_ref_speakers for x in f]
        return {
            "n_files": len(f),
            "scored_time": sum(x.scored_time for x in f),
            "ref_speech": ref_speech,
            "miss": miss,
            "fa": fa,
            "conf": conf,
            "der": (miss + fa + conf) / ref_speech if ref_speech > 0 else None,
            "miss_rate": miss / ref_speech if ref_speech > 0 else None,
            "fa_rate": fa / ref_speech if ref_speech > 0 else None,
            "conf_rate": conf / ref_speech if ref_speech > 0 else None,
            "jer": jer,
            "spk_count_acc": float(np.mean([e == 0 for e in count_err])) if f else None,
            "spk_count_mae": float(np.mean(np.abs(count_err))) if f else None,
            "spk_count_bias": float(np.mean(count_err)) if f else None,
        }


def file_score_dict(s: FileDiarScore) -> dict:
    rs = s.ref_speech
    return {
        "scored_time": s.scored_time,
        "ref_speech": rs,
        "miss": s.miss,
        "fa": s.fa,
        "conf": s.conf,
        "der": s.der,
        "miss_rate": s.miss / rs if rs > 0 else None,
        "fa_rate": s.fa / rs if rs > 0 else None,
        "conf_rate": s.conf / rs if rs > 0 else None,
        "jer": s.jer,
        "n_ref_speakers": s.n_ref_speakers,
        "n_hyp_speakers": s.n_hyp_speakers,
        "speaker_jer": s.speaker_jer,
        "mapping": s.mapping,
    }
