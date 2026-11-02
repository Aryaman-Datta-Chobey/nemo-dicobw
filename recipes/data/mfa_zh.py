"""Mandarin text preparation for Montreal Forced Aligner: dictionary-word segmentation of pre-segmented transcripts."""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

DATA = Path("/mnt/data")
DICT = DATA / "mfa/pretrained_models/dictionary/mandarin_china_mfa.dict"
HAN = re.compile(r"[㐀-䶿一-鿿豈-﫿]+")
TAG = re.compile(r"\[[^\]]*\]|<[^>]*>|\([^)]*\)")


def words_of(dic: set[str], run: str, max_len: int) -> list[str]:
    out, i = [], 0
    while i < len(run):
        for n in range(min(max_len, len(run) - i), 0, -1):
            if n == 1 or run[i:i + n] in dic:
                out.append(run[i:i + n])
                i += n
                break
    return out


def mfa_text(text: str, dic: set[str], max_len: int) -> str | None:
    """Space-separated dictionary words, or None when the utterance has Latin letters or digits."""
    t = TAG.sub(" ", unicodedata.normalize("NFKC", text))
    t = "".join(" " if unicodedata.category(c)[0] in "PSZ" else c for c in t)
    if re.search(r"[A-Za-z0-9]", t):
        return None
    out = [w for run in HAN.findall(t) for w in words_of(dic, run, max_len)]
    return " ".join(out) or None
