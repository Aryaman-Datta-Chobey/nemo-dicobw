"""Tests for the diarization / segmentation scoring harness.

Oracle tests compare against md-eval-22.pl (DER) and dscore (JER), using the pinned
third_party/dscore submodule (or DSCORE_DIR if set); they are skipped if it is not
checked out or `perl` is missing.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

from nemo_dicobw.diar_metrics import DiarSummary, score_file
from nemo_dicobw.rttm import (
    Turn, intersect_intervals, load_rttm, load_uem, merge_intervals, subtract_intervals, write_rttm, write_uem,
)
from nemo_dicobw.seg_metrics import (
    boundary_counts, confusion_summary, match_boundaries, region_confusion, speech_regions,
)

T = Turn


# --- interval helpers ---------------------------------------------------------------

def test_interval_ops():
    assert merge_intervals([(3, 4), (0, 1), (1, 2), (5, 5)]) == [(0, 2), (3, 4)]
    assert merge_intervals([(0, 1), (1.2, 2)], gap=0.3) == [(0, 2)]
    assert intersect_intervals([(0, 5), (6, 10)], [(4, 7), (9, 12)]) == [(4, 5), (6, 7), (9, 10)]
    assert subtract_intervals([(0, 10)], [(-1, 1), (4, 5), (9, 11)]) == [(1, 4), (5, 9)]
    assert subtract_intervals([(0, 2), (3, 5)], [(1, 4)]) == [(0, 1), (4, 5)]


def test_rttm_roundtrip(tmp_path: Path):
    turns = {"f1": [T("a", 0.0, 1.5), T("b", 1.0, 2.25)], "f2": [T("x", 3.0, 4.0)]}
    write_rttm(turns, tmp_path / "x.rttm")
    write_uem({"f1": [(0.0, 5.0)]}, tmp_path / "x.uem")
    assert load_rttm(tmp_path) == turns
    assert load_uem(tmp_path / "x.uem") == {"f1": [(0.0, 5.0)]}


# --- DER / JER, hand-computed -------------------------------------------------------

REF = [T("A", 0, 10), T("B", 5, 15)]
HYP = [T("X", 0, 10), T("Y", 10, 15)]
UEM = [(0.0, 20.0)]


def test_der_jer_collar0():
    s = score_file(REF, HYP, UEM, 0.0)
    # [5,10]: two ref speakers, one hyp -> 5 s missed; mapping A->X, B->Y, no confusion.
    assert s.ref_speech == pytest.approx(20)
    assert (s.miss, s.fa, s.conf) == pytest.approx((5, 0, 0))
    assert s.der == pytest.approx(0.25)
    assert s.mapping == {"A": "X", "B": "Y"}
    # A-X Jaccard 1, B-Y Jaccard 5/10.
    assert s.speaker_jer == pytest.approx({"A": 0.0, "B": 0.5})
    assert s.jer == pytest.approx(0.25)


def test_der_collar():
    s = score_file(REF, HYP, UEM, 0.25)
    # Collars at 0, 5, 10, 15 remove 0.25 + 3 * 0.5 = 1.75 s; each ref speaker loses 1 s.
    assert s.scored_time == pytest.approx(18.25)
    assert s.ref_speech == pytest.approx(18)
    assert s.miss == pytest.approx(4.5)
    assert s.der == pytest.approx(0.25)


def test_collar_at_touching_same_speaker_turns():
    # md-eval-22.pl gives 3.0 s scored speaker time here: the 4 s junction is collared too.
    s = score_file([T("A", 2, 4), T("A", 4, 6)], [T("X", 2, 6)], [(0, 20)], 0.25)
    assert s.ref_speech == pytest.approx(3.0) and s.der == pytest.approx(0)


def test_confusion_and_fa():
    ref = [T("A", 0, 10)]
    hyp = [T("X", 0, 6), T("Y", 6, 12)]
    s = score_file(ref, hyp, [(0, 12)], 0.0)
    assert (s.miss, s.fa, s.conf) == pytest.approx((0, 2, 4))
    assert s.jer == pytest.approx(1 - 6 / 10)


def test_same_speaker_overlap_not_double_counted():
    s = score_file([T("A", 0, 5), T("A", 3, 8)], [T("X", 0, 8)], [(0, 8)], 0.0)
    assert s.ref_speech == pytest.approx(8) and s.der == pytest.approx(0)


def test_empty_hyp_and_aggregate():
    s = score_file(REF, [], UEM, 0.0)
    assert s.der == pytest.approx(1.0) and s.jer == pytest.approx(1.0)
    summ = DiarSummary({"a": score_file(REF, HYP, UEM, 0.0), "b": s})
    o = summ.overall()
    assert o["der"] == pytest.approx((5 + 20) / 40)
    assert o["jer"] == pytest.approx(np.mean([0.0, 0.5, 1.0, 1.0]))  # pooled over ref speakers
    assert o["spk_count_acc"] == pytest.approx(0.5) and o["spk_count_mae"] == pytest.approx(1.0)


def test_perfect_self_score():
    for c in (0.0, 0.25):
        s = score_file(REF, REF, UEM, c)
        assert s.der == pytest.approx(0) and s.jer == pytest.approx(0)


# --- segmentation -------------------------------------------------------------------

def test_region_confusion():
    ref, hyp, uem = [T("a", 1, 5), T("b", 8, 10)], [T("x", 1.2, 4.9), T("y", 8.6, 10.1)], [(0.0, 12.0)]
    c = confusion_summary(region_confusion(speech_regions(ref, uem), speech_regions(hyp, uem), uem))
    assert c["ref_speech__hyp_speech__inter"] == pytest.approx(5.1)
    assert c["ref_speech__hyp_silence__inter"] == pytest.approx(0.9)
    assert c["ref_silence__hyp_speech__inter"] == pytest.approx(0.1)
    assert c["ref_silence__hyp_silence__inter"] == pytest.approx(5.9)
    assert c["ref_speech__hyp_speech__union"] == pytest.approx(6.1)
    assert c["ref_speech__hyp_speech__iou"] == pytest.approx(5.1 / 6.1)
    # union of ref silence (6) and hyp speech (5.2) overlap 0.1
    assert c["ref_silence__hyp_speech__iou"] == pytest.approx(0.1 / 11.1)
    assert sum(c[f"ref_{r}__hyp_{h}__frac_uem"] for r in ("speech", "silence")
               for h in ("speech", "silence")) == pytest.approx(1.0)


def test_boundaries():
    ref, hyp, uem = [T("a", 1, 5), T("b", 8, 10)], [T("x", 1.2, 4.9), T("y", 8.6, 10.1)], [(0.0, 12.0)]
    r, h = speech_regions(ref, uem), speech_regions(hyp, uem)
    b = {k: v.summary() for k, v in boundary_counts(r, h, uem, 0.25).items()}
    assert (b["onset"]["n_match"], b["onset"]["mean_disp"]) == (1, pytest.approx(0.2))
    assert b["offset"]["n_match"] == 2 and b["offset"]["mean_disp"] == pytest.approx(0.0)
    assert b["offset"]["mae"] == pytest.approx(0.1)
    assert b["all"]["precision"] == pytest.approx(0.75) and b["all"]["f1"] == pytest.approx(0.75)


def test_uem_edges_are_not_boundaries():
    uem = [(0.0, 10.0)]
    r = speech_regions([T("a", 0, 10)], uem)
    b = boundary_counts(r, r, uem, 0.25)["all"]
    assert b.n_ref == 0 and b.n_hyp == 0


def test_matching_maximises_count():
    # Greedy nearest-first could pair 0.4 with 0.2 and leave 0.0 unmatched.
    d = match_boundaries(np.array([0.0, 0.4]), np.array([0.2, 0.6]), 0.25)
    assert sorted(d.tolist()) == pytest.approx([0.2, 0.2])


# --- oracle cross-check -------------------------------------------------------------

DSCORE = os.environ.get("DSCORE_DIR", str(Path(__file__).resolve().parents[1] / "third_party" / "dscore"))
needs_oracle = pytest.mark.skipif(not (Path(DSCORE) / "score.py").is_file() or not shutil.which("perl"),
                                  reason="dscore not found: git submodule update --init third_party/dscore")


def _random_session(rng: np.random.Generator, dur: float = 120.0):
    """Reference with overlaps and pauses; hypothesis with jittered boundaries, a label
    swap, a dropped turn, a spurious turn and a split speaker. Times on a 10 ms grid."""
    q = lambda x: float(np.round(x, 2))  # noqa: E731
    n_spk = int(rng.integers(2, 6))
    ref, t = [], 0.0
    while t < dur - 3:
        s = q(t + rng.exponential(1.0))
        e = q(min(dur, s + rng.uniform(0.3, 6)))
        ref.append(T(f"s{rng.integers(n_spk)}", s, e))
        t = s + rng.uniform(-1.0, 3.0) * (e - s) / 3 + 0.2  # can go back -> overlap
    hyp = []
    for tr in ref:
        u = rng.random()
        if u < 0.05:
            continue
        spk = f"h{tr.speaker}"
        if u < 0.12:
            spk = f"h{rng.integers(n_spk)}"
        elif u < 0.2:
            spk = f"{spk}_split"
        s, e = q(tr.start + rng.normal(0, 0.15)), q(tr.end + rng.normal(0, 0.2))
        if e > s:
            hyp.append(T(spk, max(0.0, s), min(dur, e)))
        if rng.random() < 0.05:
            s2 = q(rng.uniform(0, dur - 1))
            hyp.append(T("hfa", s2, q(s2 + rng.uniform(0.2, 1))))
    return ref, hyp


@needs_oracle
@pytest.mark.parametrize("collar", [0.0, 0.25])
def test_der_matches_md_eval(tmp_path: Path, collar: float):
    rng = np.random.default_rng(0)
    ref, hyp, uem = {}, {}, {}
    for i in range(4):
        ref[f"f{i}"], hyp[f"f{i}"] = _random_session(rng)
        uem[f"f{i}"] = [(0.0, 120.0)]
    write_rttm(ref, tmp_path / "ref.rttm")
    write_rttm(hyp, tmp_path / "hyp.rttm")
    write_uem(uem, tmp_path / "all.uem")
    out = subprocess.run(
        ["perl", str(Path(DSCORE) / "scorelib" / "md-eval-22.pl"), "-r", str(tmp_path / "ref.rttm"),
         "-s", str(tmp_path / "hyp.rttm"), "-u", str(tmp_path / "all.uem"), "-c", str(collar)],
        capture_output=True, text=True, check=True).stdout
    md = {k: float(re.search(rf"{pat} =\s*([\d.]+)", out).group(1)) for k, pat in [
        ("ref_speech", "SCORED SPEAKER TIME"), ("miss", "MISSED SPEAKER TIME"),
        ("fa", "FALARM SPEAKER TIME"), ("conf", "SPEAKER ERROR TIME"),
        ("der", "OVERALL SPEAKER DIARIZATION ERROR")]}
    ours = DiarSummary({f: score_file(ref[f], hyp[f], uem[f], collar) for f in ref}).overall()
    for k in ("ref_speech", "miss", "fa", "conf"):
        assert ours[k] == pytest.approx(md[k], abs=0.02), k
    assert 100 * ours["der"] == pytest.approx(md["der"], abs=0.01)


@needs_oracle
def test_jer_matches_dscore(tmp_path: Path):
    rng = np.random.default_rng(1)
    ref, hyp, uem = {}, {}, {}
    for i in range(4):
        ref[f"f{i}"], hyp[f"f{i}"] = _random_session(rng)
        uem[f"f{i}"] = [(0.0, 120.0)]
    write_rttm(ref, tmp_path / "ref.rttm")
    write_rttm(hyp, tmp_path / "hyp.rttm")
    write_uem(uem, tmp_path / "all.uem")
    out = subprocess.run(
        [sys.executable, str(Path(DSCORE) / "score.py"), "-r", str(tmp_path / "ref.rttm"),
         "-s", str(tmp_path / "hyp.rttm"), "-u", str(tmp_path / "all.uem"), "--table_fmt", "tsv"],
        capture_output=True, text=True, check=True, cwd=DSCORE).stdout
    rows = {line.split("\t")[0].strip(): line.split("\t") for line in out.splitlines() if "\t" in line}
    hdr = [h.strip() for h in rows["File"]]
    for fid in ref:
        dscore_jer = float(rows[fid][hdr.index("JER")])
        assert 100 * score_file(ref[fid], hyp[fid], uem[fid]).jer == pytest.approx(dscore_jer, abs=0.05)
    ours = DiarSummary({f: score_file(ref[f], hyp[f], uem[f]) for f in ref}).overall()
    assert 100 * ours["jer"] == pytest.approx(float(rows["*** OVERALL ***"][hdr.index("JER")]), abs=0.05)
