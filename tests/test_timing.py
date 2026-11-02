"""Tests for CTC alignment and segment building, on synthetic frame probabilities."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from nemo_dicobw.timing import Unit, align_text, join_units, text_units, to_segments, uniform_units, viterbi, window_segments

BLANK = 9
BELLE = Path("/mnt/data/models/BELLE-2__Belle-whisper-large-v3-zh-punct")


def probs(path: list[int], v: int = 10, hit: float = 0.9) -> np.ndarray:
    lp = np.full((len(path), v), np.log((1 - hit) / (v - 1)))
    lp[np.arange(len(path)), path] = np.log(hit)
    return lp


def test_viterbi_finds_spans():
    spans, score = viterbi(probs([9, 1, 1, 9, 2, 3, 3, 3, 9]), [1, 2, 3], BLANK)
    assert spans == [(1, 3), (4, 5), (5, 8)]
    assert score == pytest.approx(0.9)


def test_viterbi_repeated_token_needs_blank():
    spans, _ = viterbi(probs([1, 9, 1]), [1, 1], BLANK)
    assert spans == [(0, 1), (2, 3)]
    assert viterbi(probs([1, 1]), [1, 1], BLANK) is None


def test_viterbi_too_many_tokens():
    assert viterbi(probs([1, 2]), [1, 2, 3], BLANK) is None
    assert viterbi(probs([1, 2]), [], BLANK) is None


def test_viterbi_ends_on_token_or_blank():
    assert viterbi(probs([1, 2]), [1, 2], BLANK)[0] == [(0, 1), (1, 2)]


def test_text_units_punctuation_and_words():
    assert [u.text for u in text_units("你好，OK. 我们")] == ["你", "好，", "OK.", "我", "们"]
    assert [u.text for u in text_units("I don't，好")] == ["I", "don't，", "好"]
    assert [u.n_chars for u in text_units("Ok好")] == [2, 1]


def test_join_units_spaces_latin_only():
    assert join_units([Unit("你"), Unit("I"), Unit("don't"), Unit("好")]) == "你I don't好"


def test_uniform_units_stay_in_speech():
    us = uniform_units("一二三四", [(0.0, 1.0), (5.0, 6.0)])
    assert [round(u.start, 3) for u in us] == [0.0, 0.5, 5.0, 5.5]
    assert [round(u.end, 3) for u in us] == [0.5, 1.0, 5.5, 6.0]


def test_to_segments_splits_at_pauses_and_takes_diarized_bounds():
    us = [Unit("一", 0.1, 0.2), Unit("二", 0.4, 0.5), Unit("三", 5.1, 5.2)]
    seg = to_segments(us, [(10.0, 11.0), (15.0, 16.0)], "s", "a", offset=10.0)
    assert [(x["start_time"], x["end_time"], x["words"]) for x in seg] == [(10.0, 11.0, "一二"), (15.0, 16.0, "三")]


def test_to_segments_never_runs_backwards():
    us = [Unit("一", 5.0, 5.1), Unit("二", 0.1, 0.2)]
    assert [x["words"] for x in to_segments(us, [(0.0, 1.0), (5.0, 6.0)], "s", "a")] == ["一二"]


@pytest.mark.skipif(not BELLE.exists(), reason="tokenizer not on this machine")
def test_align_text_real_tokenizer():
    from transformers import WhisperTokenizerFast

    tok = WhisperTokenizerFast.from_pretrained(BELLE)
    text = "你好，我们OK。"
    ids = tok("你好我们OK", add_special_tokens=False).input_ids
    v = max(ids) + 2
    path = [v - 1] + [i for t in ids for i in (t, t, v - 1)]
    res = align_text(text, probs(path, v=v), tok, v - 1, frame_s=0.1)
    assert res is not None
    units, score = res
    assert [u.text for u in units] == ["你", "好，", "我", "们", "OK。"]
    assert all(a.start < a.end <= b.start for a, b in zip(units, units[1:]))
    assert score > 0.8
    seg, how = window_segments(text, probs(path, v=v), tok, v - 1, [(100.0, 103.0)], 100.0, "s", "a", frame_s=0.1)
    assert how == "ctc" and seg[0]["words"] == "你好，我们OK。"
    seg, how = window_segments(text, None, tok, v - 1, [(100.0, 103.0)], 100.0, "s", "a")
    assert how == "uniform" and seg[0]["words"] == "你好，我们OK。"
