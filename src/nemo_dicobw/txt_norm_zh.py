"""Mandarin text normalisation for CER scoring (applied identically to references and hypotheses).

Steps:
 1. Unicode NFKC (full-width -> half-width).
 2. Traditional -> simplified Chinese (OpenCC t2s).
 3. Remove corpus markup: bracketed tags (<sil>, <$>, <#>, <->, <%>, <_>, [noise], {..}), AISHELL-4
    filler delimiters '&' (the filler itself is kept: &嗯& -> 嗯) and AISHELL-5 unintelligible '*'.
 4. Arabic numbers -> Chinese numerals (references write numbers in characters): integers read as
    numbers (23 -> 二十三), decimals with 点, '%' -> 百分之, years before 年 and digit strings with a
    leading zero or >= 5 digits read digit by digit.
 5. Lower-case Latin; strip punctuation and symbols (apostrophes inside English words are kept).
 6. Tokenise: every Han character is a token, every English word is one token.

`normalize(text)` returns the space-joined tokens, so whitespace-tokenised WER tools (meeteval)
compute CER on Chinese while keeping English words whole.
"""
from __future__ import annotations

import re
import unicodedata
from functools import lru_cache

_TAG = re.compile(r"<[^<>]*>|\[[^\[\]]*\]|\{[^{}]*\}")
_HAN = r"㐀-䶿一-鿿豈-﫿"
_TOKEN = re.compile(rf"[{_HAN}]|[a-z0-9]+(?:'[a-z]+)*")
_DIGITS = "零一二三四五六七八九"


@lru_cache(maxsize=1)
def _t2s():
    import opencc

    return opencc.OpenCC("t2s")


def _int_reading(n: int) -> str:
    """Chinese reading of a non-negative integer < 10^16 (二十三, 一百零五, 一万零一)."""
    if n == 0:
        return "零"

    def four(x: int) -> str:
        out, zero = "", False
        for unit_val, unit in ((1000, "千"), (100, "百"), (10, "十"), (1, "")):
            d = x // unit_val % 10
            if d:
                if zero:
                    out += "零"
                out += _DIGITS[d] + unit
                zero = False
            elif out:
                zero = True
        return out

    parts, groups = [], []
    while n:
        groups.append(n % 10000)
        n //= 10000
    for i in range(len(groups) - 1, -1, -1):
        g = groups[i]
        if g:
            if parts and g < 1000:
                parts.append("零")
            parts.append(four(g) + ("", "万", "亿", "万亿")[i])
        elif parts and parts[-1] != "零":
            parts.append("零")
    s = "".join(parts).rstrip("零")
    return s[1:] if s.startswith("一十") else s


def _digit_by_digit(s: str) -> str:
    return "".join(_DIGITS[int(c)] for c in s)


_NUM = re.compile(r"(\d+)(?:\.(\d+))?\s*(%)?(?=(年))?")


def _numbers(text: str) -> str:
    def repl(m: re.Match) -> str:
        whole, frac, pct = m.group(1), m.group(2), m.group(3)
        nian = m.group(4) is not None
        if nian and len(whole) == 4 and not frac:
            return _digit_by_digit(whole)
        if (len(whole) > 1 and whole.startswith("0")) or (len(whole) >= 5 and not frac):
            out = _digit_by_digit(whole)
        else:
            out = _int_reading(int(whole))
        if frac:
            out += "点" + _digit_by_digit(frac)
        return ("百分之" + out) if pct else out

    return _NUM.sub(repl, text)


def tokens(text: str) -> list[str]:
    text = unicodedata.normalize("NFKC", text)
    text = _t2s().convert(text)
    text = _TAG.sub(" ", text)
    text = text.replace("&", " ").replace("*", " ")
    text = _numbers(text)
    text = text.lower()
    return _TOKEN.findall(text)


def normalize(text: str) -> str:
    return " ".join(tokens(text))


# Training targets for belle-zh-punct. The frozen decoder learned ct-transformer punctuation, so unlike the scoring
# normaliser above these keep punctuation (NFKC would turn ， into an ASCII comma), digits and case.
_WIDE = {c: c - 0xFEE0 for c in (*range(0xFF10, 0xFF1A), *range(0xFF21, 0xFF3B), *range(0xFF41, 0xFF5B))}
_INVISIBLE = re.compile("[﻿​-‏⁠]")
_CJK = _HAN + "，。？！、；：“”‘’《》（）…—"
_CJK_GAP = re.compile(rf"\s+(?=[{_CJK}])|(?<=[{_CJK}])\s+")
_SPELLED = re.compile(r"(?<![A-Za-z'])(?:[A-Z] )+[A-Z](?![A-Za-z'])|(?<![A-Za-z'])(?:[a-z] )+[a-z](?![A-Za-z'])")


def _join_spelled(m: re.Match) -> str:
    """Corpus transcripts spell acronyms with spaces (C P U -> CPU); repeated letters are speech (I I don't)."""
    s = m.group(0)
    return s if len(set(s.replace(" ", ""))) == 1 else s.replace(" ", "")


def normalize_train(text: str) -> str:
    """Decoder target: t2s, tags and invisible characters removed, no space beside Han or CJK punctuation.

    ASCII punctuation after Latin text (`OK.`, `bug,`) stays: it is what the ct-transformer emits. Idempotent, because
    the training dataset applies it again after joining a speaker's segments with spaces.
    """
    text = _INVISIBLE.sub("", text).translate(_WIDE)
    text = _t2s().convert(text)
    text = _TAG.sub(" ", text).replace("&", " ").replace("*", " ")
    text = _CJK_GAP.sub("", text.strip())
    return re.sub(r"\s+", " ", _SPELLED.sub(_join_spelled, text)).strip()


def normalize_ctc(text: str) -> str:
    """CTC target: normalize_train without punctuation, which has no acoustic frames (and ， is three byte tokens)."""
    chars = (c if c == "'" or not unicodedata.category(c).startswith(("P", "S")) else " " for c in normalize_train(text))
    return normalize_train("".join(chars))
