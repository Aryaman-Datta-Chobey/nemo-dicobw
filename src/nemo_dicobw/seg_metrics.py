"""Speaker-agnostic speech segmentation metrics.

Reference and hypothesis are each collapsed to speech regions (the union over speakers,
optionally joining gaps <= `merge_gap`) and clipped to the UEM. Silence is UEM minus
speech.

Region confusion: for every (ref class, hyp class) pair with classes in {speech, silence},
the duration of the intersection and of the union, and their ratio (IoU). The four
intersections form the 2x2 confusion matrix and sum to the UEM duration.

Boundaries: onsets (speech starts) and offsets (speech ends) of those regions, excluding
starts/ends created only by UEM clipping. Reference and hypothesis boundaries of the same
kind are matched one-to-one within a tolerance `tol`, maximising the number of matches and
then minimising total displacement. Reported per kind (onset, offset, all): precision,
recall, F1, MAE and median absolute error over matched pairs, and the signed displacement
(hyp - ref; positive means the hypothesis boundary is late).
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from scipy.optimize import linear_sum_assignment

from nemo_dicobw.diar_metrics import build_activity
from nemo_dicobw.rttm import Interval, Turn, intersect_intervals, merge_intervals

CLASSES = ("speech", "silence")


def speech_regions(turns: list[Turn], uem: list[Interval], merge_gap: float = 0.0) -> list[Interval]:
    return intersect_intervals(merge_intervals([(t.start, t.end) for t in turns], merge_gap), uem)


def region_confusion(ref: list[Interval], hyp: list[Interval], uem: list[Interval]) -> dict[str, float]:
    """Durations of intersection/union for each (ref class, hyp class) pair."""
    act = build_activity({"s": ref}, {"s": hyp}, uem)
    d = act.durs
    masks = {
        ("ref", "speech"): act.ref[:, 0], ("ref", "silence"): ~act.ref[:, 0],
        ("hyp", "speech"): act.hyp[:, 0], ("hyp", "silence"): ~act.hyp[:, 0],
    }
    out: dict[str, float] = {"uem_time": float(d.sum())}
    for rc in CLASSES:
        for hc in CLASSES:
            a, b = masks["ref", rc], masks["hyp", hc]
            out[f"ref_{rc}__hyp_{hc}__inter"] = float(d[a & b].sum())
            out[f"ref_{rc}__hyp_{hc}__union"] = float(d[a | b].sum())
    return out


def confusion_summary(c: dict[str, float]) -> dict[str, float | None]:
    """IoUs, the confusion matrix as fractions of UEM time, and speech-detection rates."""
    def ratio(a: float, b: float) -> float | None:
        return a / b if b > 0 else None

    tp = c["ref_speech__hyp_speech__inter"]
    fn = c["ref_speech__hyp_silence__inter"]
    fp = c["ref_silence__hyp_speech__inter"]
    tn = c["ref_silence__hyp_silence__inter"]
    out: dict[str, float | None] = {"uem_time": c["uem_time"], "ref_speech": tp + fn, "ref_silence": fp + tn}
    for rc in CLASSES:
        for hc in CLASSES:
            k = f"ref_{rc}__hyp_{hc}"
            out[f"{k}__inter"] = c[f"{k}__inter"]
            out[f"{k}__union"] = c[f"{k}__union"]
            out[f"{k}__iou"] = ratio(c[f"{k}__inter"], c[f"{k}__union"])
            out[f"{k}__frac_uem"] = ratio(c[f"{k}__inter"], c["uem_time"])
    p, r = ratio(tp, tp + fp), ratio(tp, tp + fn)
    out.update(
        speech_precision=p,
        speech_recall=r,
        speech_f1=2 * p * r / (p + r) if p and r else None,
        speech_miss_rate=ratio(fn, tp + fn),  # of reference speech
        speech_fa_rate=ratio(fp, fp + tn),  # of reference silence
        sad_error=ratio(fn + fp, tp + fn),  # (miss + fa) / reference speech, DER-style
    )
    return out


def boundaries(regions: list[Interval], uem: list[Interval]) -> tuple[np.ndarray, np.ndarray]:
    """Onsets and offsets of `regions`, dropping those that coincide with a UEM edge."""
    uem_starts, uem_ends = {s for s, _ in uem}, {e for _, e in uem}
    on = np.array([s for s, _ in regions if s not in uem_starts], dtype=np.float64)
    off = np.array([e for _, e in regions if e not in uem_ends], dtype=np.float64)
    return on, off


def match_boundaries(ref: np.ndarray, hyp: np.ndarray, tol: float) -> np.ndarray:
    """Signed displacements hyp - ref of an optimal one-to-one matching within `tol`.

    Points are split into chains whose consecutive members are <= tol apart (no match can
    cross a chain break), and each chain is solved with the Hungarian algorithm, using a
    penalty larger than any chain's total valid cost for out-of-tolerance pairs so that the
    number of matches is maximised first.
    """
    if ref.size == 0 or hyp.size == 0:
        return np.zeros(0)
    pts = np.concatenate([ref, hyp])
    is_ref = np.concatenate([np.ones(ref.size, bool), np.zeros(hyp.size, bool)])
    order = np.argsort(pts, kind="stable")
    pts, is_ref = pts[order], is_ref[order]
    breaks = np.flatnonzero(np.diff(pts) > tol) + 1
    disp: list[float] = []
    for lo, hi in zip(np.r_[0, breaks], np.r_[breaks, pts.size]):
        r, h = pts[lo:hi][is_ref[lo:hi]], pts[lo:hi][~is_ref[lo:hi]]
        if r.size == 0 or h.size == 0:
            continue
        dist = np.abs(h[None, :] - r[:, None])
        penalty = tol * (r.size + h.size) + 1.0
        rows, cols = linear_sum_assignment(np.where(dist <= tol, dist, penalty))
        ok = dist[rows, cols] <= tol
        disp.extend((h[cols[ok]] - r[rows[ok]]).tolist())
    return np.asarray(disp)


@dataclass
class BoundaryCounts:
    n_ref: int = 0
    n_hyp: int = 0
    disp: np.ndarray = field(default_factory=lambda: np.zeros(0))

    def __add__(self, other: "BoundaryCounts") -> "BoundaryCounts":
        return BoundaryCounts(self.n_ref + other.n_ref, self.n_hyp + other.n_hyp,
                              np.concatenate([self.disp, other.disp]))

    def summary(self) -> dict[str, float | int | None]:
        m = self.disp.size
        p = m / self.n_hyp if self.n_hyp else None
        r = m / self.n_ref if self.n_ref else None
        a = np.abs(self.disp)
        return {
            "n_ref": self.n_ref,
            "n_hyp": self.n_hyp,
            "n_match": m,
            "precision": p,
            "recall": r,
            "f1": 2 * m / (self.n_ref + self.n_hyp) if self.n_ref + self.n_hyp else None,
            "mae": float(a.mean()) if m else None,
            "median_abs_err": float(np.median(a)) if m else None,
            "mean_disp": float(self.disp.mean()) if m else None,
            "median_disp": float(np.median(self.disp)) if m else None,
        }


def boundary_counts(
    ref_regions: list[Interval], hyp_regions: list[Interval], uem: list[Interval], tol: float
) -> dict[str, BoundaryCounts]:
    (r_on, r_off), (h_on, h_off) = boundaries(ref_regions, uem), boundaries(hyp_regions, uem)
    on = BoundaryCounts(r_on.size, h_on.size, match_boundaries(r_on, h_on, tol))
    off = BoundaryCounts(r_off.size, h_off.size, match_boundaries(r_off, h_off, tol))
    return {"onset": on, "offset": off, "all": on + off}
