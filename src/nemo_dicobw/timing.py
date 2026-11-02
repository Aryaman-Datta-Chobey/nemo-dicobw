"""Character times and per-speaker segments for a model without timestamp tokens.

One decoded <= 30 s window of one target speaker goes in, SegLST segments come out:
  1. `ctc_log_probs`  frame log-probabilities of the DiCoW encoder's CTC head (80 ms frames, conditioned on the STNO mask).
  2. `viterbi`        CTC forced alignment of the decoded text's tokens to those frames. The head was trained on text without
                      punctuation (`normalize_ctc`), so only that text is aligned.
  3. `align_text`     frames back to units: one Han character or one Latin / digit word, punctuation attached to its neighbour.
                      Byte-level tokens are grouped into characters first; a token spanning several characters is split evenly.
  4. `uniform_units`  fallback when alignment is impossible (more tokens than frames, a loop) or scores below `min_score`:
                      units spread over the speaker's diarized speech, in order.
  5. `to_segments`    units split at diarized pauses. Each unit goes to its nearest diarized interval and a segment takes that
                      interval's bounds, so segment times come from the diarizer and CTC only decides which text belongs where.

Everything takes and returns seconds relative to the window except `to_segments`, which takes absolute times via `offset`.
"""
from __future__ import annotations

import unicodedata
from dataclasses import dataclass

import numpy as np

from nemo_dicobw.txt_norm_zh import normalize_ctc, normalize_train

Interval = tuple[float, float]
FRAME_S = 30.0 / 375  # 1500 encoder frames, subsampled 4x before the CTC head


@dataclass
class Unit:
    text: str  # with attached punctuation
    start: float = 0.0
    end: float = 0.0
    n_chars: int = 1  # characters that carry time, without punctuation


def _dropped_by_ctc(c: str) -> bool:
    return c != "'" and unicodedata.category(c).startswith(("P", "S"))


def _is_han(c: str) -> bool:
    return unicodedata.name(c, "").startswith("CJK")


def text_units(text: str) -> list[Unit]:
    """Units of a window's text after `normalize_train`. Latin and digit runs are one unit, as the scorer treats them."""
    units: list[Unit] = []
    lead, in_word = "", False
    for c in normalize_train(text):
        if c.isspace():
            in_word = False
        elif _dropped_by_ctc(c):
            if units:
                units[-1].text += c
            else:
                lead += c
            in_word = False
        elif in_word and not _is_han(c):
            units[-1].text += c
            units[-1].n_chars += 1
        else:
            units.append(Unit(lead + c))
            lead, in_word = "", not _is_han(c)
    return units


def viterbi(log_probs: np.ndarray, tokens: list[int], blank: int) -> tuple[list[tuple[int, int]], float] | None:
    """Best CTC path of `tokens` through (T, V) log-probs: per token (first frame, last frame + 1), and the mean probability
    of the frames assigned to tokens. None if the tokens cannot fit, counting the blank that repeated tokens need."""
    n, t_max = len(tokens), len(log_probs)
    if n == 0 or n + sum(a == b for a, b in zip(tokens, tokens[1:])) > t_max:
        return None
    # states: 0 = blank before token 0, odd 2j+1 = on token j, even 2j+2 = blank after token j
    s = 2 * n + 1
    tok = np.array(tokens)
    same = np.r_[False, tok[1:] == tok[:-1]]
    score = np.full(s, -np.inf)
    back = np.zeros((t_max, s), dtype=np.int32)
    on_tok, on_blank = np.arange(1, s, 2), np.arange(0, s, 2)
    for t in range(t_max):
        lp_tok, lp_blank = log_probs[t, tok], log_probs[t, blank]
        new = np.full(s, -np.inf)
        if t == 0:
            new[0], new[1] = lp_blank, lp_tok[0]
            back[0] = -1
        else:
            # token j: stay, come from the blank before it, or directly from token j-1 if the label differs
            prev_blank, stay = score[on_blank[:-1]], score[on_tok]
            direct = np.r_[-np.inf, score[on_tok[:-1]]]
            direct[same] = -np.inf
            choice = np.stack([stay, prev_blank, direct])
            k = choice.argmax(0)
            new[on_tok] = choice[k, np.arange(n)] + lp_tok
            back[t, on_tok] = np.where(k == 0, on_tok, np.where(k == 1, on_tok - 1, on_tok - 2))
            # blank j: stay, or leave the token before it
            stay_b, leave = score[on_blank], np.r_[-np.inf, score[on_tok]]
            b_new = np.maximum(stay_b, leave)
            new[on_blank] = b_new + lp_blank
            back[t, on_blank] = np.where(stay_b >= leave, on_blank, on_blank - 1)
        score = new
    state = int(s - 1 if score[s - 1] >= score[s - 2] else s - 2)
    if not np.isfinite(score[state]):
        return None
    spans: list[list[int]] = [[-1, -1] for _ in range(n)]
    probs = []
    for t in range(t_max - 1, -1, -1):
        if state % 2:
            j = state // 2
            spans[j][0] = t
            if spans[j][1] < 0:
                spans[j][1] = t + 1
            probs.append(float(np.exp(log_probs[t, tok[j]])))
        state = int(back[t, state])
    return [(a, b) for a, b in spans], float(np.mean(probs))


def align_text(text: str, log_probs: np.ndarray, tokenizer, blank: int, frame_s: float = FRAME_S) -> tuple[list[Unit], float] | None:
    """Units with times from CTC alignment, and the alignment score. None if the alignment is not possible."""
    units = text_units(text)
    ids = tokenizer(normalize_ctc(text), add_special_tokens=False).input_ids
    res = viterbi(log_probs, ids, blank)
    if res is None:
        return None
    spans, score = res
    times: list[tuple[float, float]] = []  # one per non-space character
    chars, buf, first = "", [], 0
    for i, (tok, (a, b)) in enumerate(zip(ids, spans)):
        first = a if not buf else first
        buf.append(tok)
        piece = tokenizer.decode(buf)
        if "�" in piece and i < len(ids) - 1:
            continue
        piece = "".join(piece.split())
        step = (b - first) / max(len(piece), 1)
        times += [((first + k * step) * frame_s, (first + (k + 1) * step) * frame_s) for k in range(len(piece))]
        chars += piece
        buf = []
    if sum(u.n_chars for u in units) != len(times):  # the tokenizer must give back exactly the characters the units hold
        return None
    k = 0
    for u in units:
        u.start, u.end = times[k][0], times[k + u.n_chars - 1][1]
        k += u.n_chars
    return units, score


def uniform_units(text: str, speech: list[Interval]) -> list[Unit]:
    """Fallback: units spread evenly over `speech` in order, weighted by characters."""
    units = text_units(text)
    total = sum(e - s for s, e in speech)
    n = sum(u.n_chars for u in units)
    if not units or total <= 0:
        return units
    edges = np.cumsum([0.0] + [e - s for s, e in speech])

    def at(x: float) -> float:
        j = min(int(np.searchsorted(edges, x, side="right")) - 1, len(speech) - 1)
        return speech[j][0] + x - edges[j]

    done = 0
    for u in units:
        u.start, u.end = at(done / n * total), at(min((done + u.n_chars) / n, 1.0) * total - 1e-9)
        done += u.n_chars
    return units


def join_units(units: list[Unit]) -> str:
    out = ""
    for u in units:
        out += (" " if out and out[-1].isascii() and out[-1].isalnum() and u.text[0].isascii() and u.text[0].isalnum() else "") + u.text
    return out


def to_segments(units: list[Unit], speech: list[Interval], session: str, speaker: str, offset: float = 0.0) -> list[dict]:
    """SegLST segments: `speech` (absolute, sorted) gives the times, units are split at its pauses and never run backwards."""
    if not units:
        return []
    if not speech:
        speech = [(offset + units[0].start, offset + units[-1].end)]
    groups: dict[int, list[Unit]] = {}
    last = 0
    for u in units:
        mid = offset + (u.start + u.end) / 2
        k = min(range(last, len(speech)), key=lambda j: max(speech[j][0] - mid, mid - speech[j][1], 0.0))
        groups.setdefault(k, []).append(u)
        last = k
    return [{"session_id": session, "speaker": speaker, "start_time": round(speech[k][0], 3), "end_time": round(speech[k][1], 3),
             "words": join_units(us)} for k, us in sorted(groups.items())]


def window_segments(text: str, log_probs: np.ndarray | None, tokenizer, blank: int, speech: list[Interval], window_start: float,
                    session: str, speaker: str, min_score: float = 0.0, frame_s: float = FRAME_S) -> tuple[list[dict], str]:
    """Segments of one window and the method used ("ctc" or "uniform"). `speech` is the speaker's diarized speech in this window."""
    aligned = align_text(text, log_probs, tokenizer, blank, frame_s) if log_probs is not None else None
    if aligned is not None and aligned[1] >= min_score:
        return to_segments(aligned[0], speech, session, speaker, window_start), "ctc"
    relative = [(s - window_start, e - window_start) for s, e in speech]
    return to_segments(uniform_units(text, relative), speech, session, speaker, window_start), "uniform"


def ctc_log_probs(encoder, input_features, stno_mask=None) -> np.ndarray:
    """(B, T, V) log-probabilities of a DiCoW encoder's CTC head. The blank is the last index."""
    import torch

    with torch.inference_mode():
        logits = encoder(input_features, stno_mask=stno_mask, return_logits=True).logits
        return torch.log_softmax(logits.float(), dim=-1).cpu().numpy()
