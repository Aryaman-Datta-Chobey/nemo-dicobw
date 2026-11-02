"""Tests for the Mandarin normaliser, including 50 real reference lines per corpus
(skipped if the corpora are not on this machine)."""
from __future__ import annotations

import glob
import random
import re

import pytest

from nemo_dicobw.txt_norm_zh import normalize, tokens


@pytest.mark.parametrize("raw,want", [
    ("你好，世界。", "你 好 世 界"),
    ("這個問題", "这 个 问 题"),                       # traditional -> simplified
    ("ＰＰＴ做好了吗？", "ppt 做 好 了 吗"),               # full-width Latin, case
    ("嗯<sil>但是<->咱们<#>说", "嗯 但 是 咱 们 说"),      # AISHELL-4 tags
    ("这块儿&呃&别的", "这 块 儿 呃 别 的"),              # AISHELL-4 filler delimiters
    ("回去*发烧。", "回 去 发 烧"),                     # AISHELL-5 unintelligible
    ("hello kitty嘞", "hello kitty 嘞"),
    ("it's ok", "it's ok"),
    ("[noise] 好的", "好 的"),
    ("23个人", "二 十 三 个 人"),
    ("10", "十"),
    ("105", "一 百 零 五"),
    ("10001", "一 零 零 零 一"),                       # >= 5 digits read digit by digit
    ("2023年", "二 零 二 三 年"),
    ("3.5", "三 点 五"),
    ("50%", "百 分 之 五 十"),
    ("010", "零 一 零"),
    ("", ""),
])
def test_normalize(raw: str, want: str):
    assert normalize(raw) == want


def test_idempotent():
    s = "我们20号开会，讨论PPT和office的事情。"
    assert normalize(normalize(s)) == normalize(s)


CORPORA = {
    "alimeeting": "/mnt/data/corpora/alimeeting/*/*_far/textgrid_dir/*.TextGrid",
    "aishell4": "/mnt/data/corpora/aishell4/test/TextGrid/*.TextGrid",
    "aishell5": "/mnt/data/corpora/aishell5/Eval*/*/DX01C01.TextGrid",
}
_OK = re.compile(r"^(?:[㐀-䶿一-鿿豈-﫿]|[a-z0-9]+(?:'[a-z]+)*)$")


@pytest.mark.parametrize("corpus", sorted(CORPORA))
def test_real_lines(corpus: str):
    textgrid = pytest.importorskip("textgrid")
    files = sorted(glob.glob(CORPORA[corpus]))
    if not files:
        pytest.skip(f"{corpus} TextGrids not available")
    lines = [i.mark for f in files for t in textgrid.TextGrid.fromFile(f).tiers for i in t if i.mark and i.mark.strip()]
    random.Random(0).shuffle(lines)
    for line in lines[:50]:
        toks = tokens(line)
        assert all(_OK.match(t) for t in toks), (line, toks)
        assert normalize(" ".join(toks)) == " ".join(toks), line
        assert not re.search(r"[<>&*，。？！]", " ".join(toks)), line
        han_in = len(re.findall(r"[一-鿿]", re.sub(r"<[^>]*>", "", line)))
        assert sum(len(t) == 1 and "一" <= t <= "鿿" for t in toks) == han_in, line  # no Han lost or added


from nemo_dicobw.txt_norm_zh import normalize_ctc, normalize_train  # noqa: E402


def test_train_keeps_punctuation_and_cleans_spacing():
    assert normalize_train("﻿十套 楼的，  都有。 我们") == "十套楼的，都有。我们"
    assert normalize_train("我們<sil>在這") == "我们在这"
    assert normalize_train("yes yes, ld o然后") == "yes yes, ld o然后"
    assert normalize_train("Ａ１好") == "A1好"


def test_train_joins_spelled_letters_only():
    assert normalize_train("它的 C P U 是") == "它的CPU是"
    assert normalize_train("I I don't care") == "I I don't care"
    assert normalize_train("e c e 的课") == "ece的课"


def test_train_is_idempotent():
    for s in ("好了，OK. 我们 M A C", "Because they don't play.", " Oppo."):
        assert normalize_train(normalize_train(s)) == normalize_train(s)


def test_ctc_strips_punctuation():
    assert normalize_ctc("好了，OK.我们？") == "好了OK我们"
    assert normalize_ctc("I don't, care。") == "I don't care"
    assert normalize_ctc("，。") == ""
