#!/usr/bin/env python
"""Build diarization references for the held-out evaluation sets.

Output, per corpus and split:
    <refs>/<corpus>/<split>/rttm/<ref_type>/<session>.rttm   one file per session
    <refs>/<corpus>/<split>/uem/<session>.uem
    <refs>/<corpus>/<split>/PROVENANCE.json                  sources, commits, counts
RTTM file ids are session ids; every channel of a session shares its reference.

ref_type:
    segments  the corpus' own segment-level annotation (counts within-segment pauses as speech)
    fa        published forced-alignment labels (tighter boundaries)
    words     word-level timings merged into segments across gaps <= --word-gap seconds

| corpus     | splits                | ref types          | UEM                                   |
|------------|-----------------------|--------------------|---------------------------------------|
| aishell4   | test                  | segments (official RTTM) | [0, recording]                  |
| aishell5   | Dev, Eval1, Eval2     | segments (far-field DX*C01 TextGrids) | [0, recording]     |
| alimeeting | Eval_Ali, Test_Ali    | segments (far TextGrid), fa (nttcslab-sp/diar-forced-alignment) | [0, recording] |
| notsofar   | eval                  | segments (gt_transcription.json, 129 meetings), fa (FastMSS MFA, 80 meetings) | [0, shortest device] |
| chime6     | dev, eval             | segments (transcription JSON), fa (official alignment RTTM) | [official start, min(12000, recording)] |
| egocom     | test, val             | words (ground_truth_transcriptions.csv, untimed words interpolated), words_timedonly | [0, shortest wearer] |

Recording durations come from the converted 16 kHz audio. NOTSOFAR also gets eval_sc_160.tsv,
the (meeting, device) pairs of the CHiME-8 / Nemotron-card eval-SC set.

Example (run in the `dicow` env, which has `textgrid`):
    python recipes/data/build_refs.py aishell5 alimeeting notsofar
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import tarfile
from collections import defaultdict
from pathlib import Path

import soundfile as sf

from nemo_dicobw.rttm import Interval, Turn, load_rttm, merge_intervals, write_rttm, write_uem

DATA = Path("/mnt/data")
Refs = dict[str, list[Turn]]


def audio_durations(session_dir: Path) -> dict[str, float]:
    return {p.stem: sf.info(str(p)).duration for p in sorted(session_dir.glob("*.flac"))}


def textgrid_turns(paths: list[Path]) -> list[Turn]:
    """Union of speaker tiers over TextGrids; a tier repeated in several files must be identical."""
    import textgrid

    tiers: dict[str, list[Interval]] = {}
    for p in paths:
        for tier in textgrid.TextGrid.fromFile(str(p)).tiers:
            iv = [(float(i.minTime), float(i.maxTime)) for i in tier if i.mark and i.mark.strip()]
            if tier.name in tiers and tiers[tier.name] != iv:
                raise ValueError(f"tier {tier.name} differs between TextGrids of {p.parent}")
            tiers[tier.name] = iv
    return [Turn(spk, s, e) for spk, ivs in tiers.items() for s, e in ivs if e > s]


def rename(turns: list[Turn], spk_fn=lambda s: s) -> list[Turn]:
    return sorted((Turn(re.sub(r"\s+", "_", spk_fn(t.speaker)), t.start, t.end) for t in turns),
                  key=lambda t: (t.start, t.end, t.speaker))


class Writer:
    """Collects references for one corpus/split and writes them with provenance."""

    def __init__(self, refs_root: Path, corpus: str, split: str):
        self.dir = refs_root / corpus / split
        self.corpus, self.split = corpus, split
        self.refs: dict[str, Refs] = defaultdict(dict)
        self.uem: dict[str, list[Interval]] = {}
        self.prov: dict = {"corpus": corpus, "split": split, "ref_types": {}, "uem": None}

    def add(self, ref_type: str, session: str, turns: list[Turn]) -> None:
        self.refs[ref_type][session] = turns

    def write(self) -> None:
        for ref_type, sessions in self.refs.items():
            d = self.dir / "rttm" / ref_type
            d.mkdir(parents=True, exist_ok=True)
            for s, turns in sessions.items():
                write_rttm({s: turns}, d / f"{s}.rttm")
            p = self.prov["ref_types"].setdefault(ref_type, {})
            p["n_sessions"] = len(sessions)
            p["speech_hours"] = round(sum(e - s for t in sessions.values()
                                          for s, e in merge_intervals((x.start, x.end) for x in t)) / 3600, 3)
        (self.dir / "uem").mkdir(parents=True, exist_ok=True)
        for s, iv in self.uem.items():
            write_uem({s: iv}, self.dir / "uem" / f"{s}.uem")
        self.prov["n_uem_sessions"] = len(self.uem)
        self.prov["uem_hours"] = round(sum(e - s for iv in self.uem.values() for s, e in iv) / 3600, 3)
        (self.dir / "PROVENANCE.json").write_text(json.dumps(self.prov, indent=1, ensure_ascii=False) + "\n")
        summary = ", ".join(f"{k}: {v['n_sessions']} sessions / {v['speech_hours']} h speech"
                            for k, v in self.prov["ref_types"].items())
        print(f"{self.corpus}/{self.split}: {summary}; UEM {len(self.uem)} sessions / {self.prov['uem_hours']} h")


def check_within(session: str, turns: list[Turn], dur: float, tol: float = 0.5) -> None:
    end = max((t.end for t in turns), default=0.0)
    if end > dur + tol:
        print(f"  WARNING {session}: reference ends at {end:.2f}s, audio is {dur:.2f}s", file=sys.stderr)


# --- corpora -------------------------------------------------------------------------

def build_aishell4(args) -> None:
    src = args.corpora / "aishell4" / "test" / "TextGrid"
    w = Writer(args.refs, "aishell4", "test")
    w.prov["ref_types"]["segments"] = {"source": "official test/TextGrid/<session>.rttm (OpenSLR 111)"}
    w.prov["uem"] = "[0, recording duration]"
    official = load_rttm(sorted(src.glob("*.rttm")))
    for sess_dir in sorted((args.audio / "aishell4" / "test").iterdir()):
        s = sess_dir.name
        dur = min(audio_durations(sess_dir).values())
        turns = rename(official[s])
        check_within(s, turns, dur)
        w.add("segments", s, turns)
        w.uem[s] = [(0.0, dur)]
    w.write()


def build_aishell5(args) -> None:
    for split in ("Dev", "Eval1", "Eval2"):
        w = Writer(args.refs, "aishell5", split)
        w.prov["ref_types"]["segments"] = {
            "source": f"corpora/aishell5/{split}/<session>/DX*C01.TextGrid (OpenSLR 159), union of speaker tiers",
            "note": "The DX01-DX04 TextGrids are identical and on the far-field timeline. The near-field DA0x "
                    "TextGrids are not used: in 23 of 54 sessions they differ (extra/missing utterances, and "
                    "offsets of several seconds, e.g. Eval2/016 ~3.8 s)."}
        w.prov["uem"] = "[0, recording duration]"
        for sess_dir in sorted((args.audio / "aishell5" / split).iterdir()):
            s = sess_dir.name
            dur = min(audio_durations(sess_dir).values())
            turns = rename(textgrid_turns(sorted((args.corpora / "aishell5" / split / s).glob("DX*C01.TextGrid"))))
            check_within(s, turns, dur)
            w.add("segments", s, turns)
            w.uem[s] = [(0.0, dur)]
        w.write()


def build_alimeeting(args) -> None:
    fa_root = args.refs / "alimeeting" / "forced_alignment"
    fa_commit = (fa_root / ".git" / "HEAD").read_text().strip() if (fa_root / ".git").exists() else "?"
    for split in ("Eval_Ali", "Test_Ali"):
        w = Writer(args.refs, "alimeeting", split)
        w.prov["ref_types"]["segments"] = {"source": f"{split}/{split}_far/textgrid_dir/<session>.TextGrid (OpenSLR 119)"}
        w.prov["ref_types"]["fa"] = {"source": f"nttcslab-sp/diar-forced-alignment AliMeeting/{split}_far",
                                     "commit": fa_commit}
        w.prov["uem"] = "[0, recording duration]"
        fa = load_rttm(sorted((fa_root / "AliMeeting" / f"{split}_far").glob("*.rttm")))
        for sess_dir in sorted((args.audio / "alimeeting" / split).iterdir()):
            s = sess_dir.name
            dur = min(d for c, d in audio_durations(sess_dir).items() if c.startswith("far_"))
            tg = args.corpora / "alimeeting" / split / f"{split}_far" / "textgrid_dir" / f"{s}.TextGrid"
            seg = rename(textgrid_turns([tg]))
            check_within(s, seg, dur)
            w.add("segments", s, seg)
            if s not in fa:
                raise KeyError(f"no forced-alignment RTTM for {split}/{s}")
            w.add("fa", s, rename(fa[s]))
            w.uem[s] = [(0.0, dur)]
        w.write()


def build_notsofar(args) -> None:
    mtg_root = args.corpora / "notsofar" / "benchmark-datasets" / "eval_set" / "240825.1_eval_full_with_GT" / "MTG"
    raw = args.data / "raw" / "notsofar_fa"
    w = Writer(args.refs, "notsofar", "eval")
    w.prov["ref_types"]["segments"] = {"source": "MTG/<meeting>/gt_transcription.json utterances (HF microsoft/NOTSOFAR @ba8fd0f, 240825.1_eval_full_with_GT)"}
    w.prov["ref_types"]["fa"] = {"source": "popcornell/FastMSS resources/notsofar1-channels_mfa_rttms.tar.gz eval/ (one per meeting; "
                                           "its two S<id> copies per meeting are identical)",
                                 "commit": "c240acf6930d6e6c8fc61a4463ceb08733fd6c29"}
    w.prov["uem"] = "[0, shortest single-channel device recording of the meeting]"

    sess_map = json.loads((raw / "c8map.json").read_text())["sessions_map"]["notsofar1"]
    inv = {v: k for k, v in sess_map.items()}
    fa: dict[str, list[Turn]] = {}
    pairs: list[tuple[str, str, str]] = []
    with tarfile.open(raw / "notsofar1-channels_mfa_rttms.tar.gz") as tar:
        for m in tar.getmembers():
            if not (m.isfile() and m.name.startswith("eval/") and m.name.endswith(".rttm")):
                continue
            sid = Path(m.name).stem
            meeting, _, rest = inv[sid].partition("_")[2].partition("_")
            meeting = f"MTG_{meeting}"
            device = rest.removesuffix("_sc")
            turns = sorted((Turn(p[7], float(p[3]), float(p[3]) + float(p[4]))
                            for p in (line.split() for line in tar.extractfile(m).read().decode().splitlines())
                            if p and p[0] == "SPEAKER" and float(p[4]) > 0),
                           key=lambda t: (t.start, t.end, t.speaker))
            if meeting in fa and fa[meeting] != turns:
                raise ValueError(f"FastMSS sessions of {meeting} differ")
            fa[meeting] = turns
            pairs.append((sid, meeting, f"sc_{device}"))

    for sess_dir in sorted((args.audio / "notsofar" / "eval").iterdir()):
        s = sess_dir.name
        dur = min(audio_durations(sess_dir).values())
        utts = json.loads((mtg_root / s / "gt_transcription.json").read_text())
        seg = rename([Turn(u["speaker_id"], float(u["start_time"]), float(u["end_time"])) for u in utts
                      if float(u["end_time"]) > float(u["start_time"])])
        check_within(s, seg, dur)
        w.add("segments", s, seg)
        if s in fa:
            w.add("fa", s, rename(fa[s]))
        w.uem[s] = [(0.0, dur)]
    missing = sorted(set(fa) - set(w.refs["segments"]))
    if missing:
        raise KeyError(f"FastMSS meetings without converted audio: {missing[:5]}")
    for _, meeting, ch in pairs:
        if not (args.audio / "notsofar" / "eval" / meeting / f"{ch}.flac").exists():
            raise FileNotFoundError(f"eval-SC recording {meeting}/{ch} not converted")
    w.dir.mkdir(parents=True, exist_ok=True)
    with open(w.dir / "eval_sc_160.tsv", "w", newline="") as f:
        cw = csv.writer(f, delimiter="\t")
        cw.writerow(["fastmss_session", "meeting", "channel"])
        cw.writerows(sorted(pairs, key=lambda x: (x[1], x[2])))
    w.prov["eval_sc_160"] = "eval_sc_160.tsv: (meeting, channel) pairs of the CHiME-8 / Nemotron-card eval-SC set, " \
                            "via chime-utils chime_utils/dgen/c8map.json @152882404f"
    w.write()


def _hms(t: str | float) -> float:
    if isinstance(t, (int, float)):
        return float(t)
    h, m, s = t.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def build_chime6(args) -> None:
    official = args.refs / "chime6" / "official"
    uem_start: dict[str, float] = {}
    for line in (official / "kaldi_chime6_uem_file").read_text().splitlines():
        rec, _, start, end = line.split()
        sess = rec.split("_")[0]
        if sess in uem_start and uem_start[sess] != float(start):
            raise ValueError(f"inconsistent official UEM start for {sess}")
        uem_start[sess] = float(start)
        uem_end = float(end)
    trans = next((p for p in (args.corpora / "chime6").rglob("transcriptions") if (p / "dev").is_dir()), None)
    if trans is None:
        raise FileNotFoundError("CHiME-6 transcriptions not extracted yet")
    for split in ("dev", "eval"):
        w = Writer(args.refs, "chime6", split)
        w.prov["ref_types"]["segments"] = {"source": f"CHiME6 transcriptions/{split}/<session>.json utterances (OpenSLR 150)"}
        w.prov["ref_types"]["fa"] = {"source": f"nateanl/chime6_rttm {split}_rttm (official Track 2 alignment RTTM, U06 timeline)",
                                     "commit": "792c26b8bd196591388afe2255894532e56a2d00"}
        w.prov["uem"] = ("[official start (Kaldi egs/chime6/s5_track2/local/uem_file @36afe3b, excludes speaker "
                         "introductions), min(12000, shortest Kinect channel)]")
        fa = load_rttm(official / "chime6_rttm" / f"{split}_rttm")
        fa = {k.split("_")[0]: v for k, v in fa.items()}
        for sess_dir in sorted((args.audio / "chime6" / split).iterdir()):
            s = sess_dir.name
            dur = min(d for c, d in audio_durations(sess_dir).items() if c.startswith("U"))
            utts = json.loads((trans / split / f"{s}.json").read_text())
            seg = rename([Turn(u["speaker"], _hms(u["start_time"]), _hms(u["end_time"])) for u in utts
                          if "speaker" in u and _hms(u["end_time"]) > _hms(u["start_time"])])
            check_within(s, seg, dur)
            w.add("segments", s, seg)
            w.add("fa", s, rename(fa[s]))
            w.uem[s] = [(uem_start[s], min(uem_end, dur))]
        w.write()


# EgoCom transcript tokens that mark untranscribed or non-lexical audio; untimed ones get no interval.
EGOCOM_TAGS = {"crosstalk", "inaudible", "laughs", "laughter", "laugh", "music", "foreign"}
EGOCOM_WORD_DUR = 0.17  # median timed word duration (s)
EGOCOM_MIN_WORD, EGOCOM_MAX_WORD = 0.10, 0.60  # per-word bounds when spreading untimed words over a gap


def egocom_words(rows: list[dict], stats: dict[str, int]) -> list[dict]:
    """Spoken words of one conversation in transcript order, as dicts with keys
    spk, s, e, text, interpolated (bool) and tag (bool: an annotation tag such as "laughs").

    About 10% of the transcript's words have no timestamps. The transcript is chronological, so
    each run of untimed words is spread evenly over the gap between its timed neighbours (prev
    end p, next start n), at most EGOCOM_MAX_WORD per word; if that leaves the gap partly empty,
    the run sits next to the neighbour of the same speaker (else centred). If the gap is smaller
    than EGOCOM_MIN_WORD per word (overlapping crosstalk), each word gets EGOCOM_WORD_DUR centred on
    the gap. Runs at a conversation edge are anchored to their one timed neighbour. Untimed
    annotation tags (EGOCOM_TAGS) get no interval. A contraction suffix ("it ' s") is joined to
    the previous word's text ("it's") and extends its interval if it has one. Numerals count as
    words.
    """
    words: list[dict] = []  # s/e None while untimed
    prev_tok = ""
    for r in rows:
        tok = r["word"].strip()
        if not tok or not any(c.isalnum() for c in tok):
            prev_tok = tok or prev_tok
            continue
        has_s, has_e = bool(r["startTime"]), bool(r["endTime"])
        if prev_tok == "'" and words and words[-1]["spk"] == r["speaker_id"]:
            words[-1]["text"] += "'" + tok.lower()
            if has_s and has_e and words[-1]["s"] is not None:
                words[-1]["e"] = max(words[-1]["e"], float(r["endTime"]))
            stats["contraction_suffix_joined"] += 1
        elif not has_s and tok.lower() in EGOCOM_TAGS:
            stats["untimed_tag_skipped"] += 1
        elif has_s:
            s = float(r["startTime"])
            e = float(r["endTime"]) if has_e else s + EGOCOM_WORD_DUR
            stats["timed" if has_e else "start_only"] += 1
            if e > s:
                words.append({"spk": r["speaker_id"], "s": s, "e": e, "text": tok.lower(),
                              "interpolated": False, "tag": tok.lower() in EGOCOM_TAGS})
        else:
            words.append({"spk": r["speaker_id"], "s": None, "e": None, "text": tok.lower(),
                          "interpolated": True, "tag": False})
        prev_tok = tok

    i = 0
    while i < len(words):
        if words[i]["s"] is not None:
            i += 1
            continue
        j = i
        while j < len(words) and words[j]["s"] is None:
            j += 1
        run, k = words[i:j], j - i
        prev, nxt = (words[i - 1] if i > 0 else None), (words[j] if j < len(words) else None)
        if prev is None and nxt is None:
            stats["untimed_unanchored_skipped"] += k
            del words[i:j]
            continue
        if prev is None or nxt is None:
            d = EGOCOM_WORD_DUR
            start = nxt["s"] - k * d if prev is None else prev["e"]
            stats["interpolated_edge"] += k
        else:
            gap = nxt["s"] - prev["e"]
            if gap >= k * EGOCOM_MIN_WORD:
                d = min(gap / k, EGOCOM_MAX_WORD)
                spare = gap - k * d
                if spare <= 1e-9 or run[0]["spk"] == prev["spk"]:
                    start = prev["e"]
                elif run[-1]["spk"] == nxt["spk"]:
                    start = nxt["s"] - k * d
                else:
                    start = prev["e"] + spare / 2
                stats["interpolated_gap"] += k
            else:
                d = EGOCOM_WORD_DUR
                start = (prev["e"] + nxt["s"]) / 2 - k * d / 2
                stats["interpolated_overlap"] += k
        for n, w in enumerate(run):
            w["s"], w["e"] = max(0.0, start + n * d), max(0.0, start + (n + 1) * d)
        i = j
    return [w for w in words if w["e"] > w["s"]]


EGOCOM_MAX_ALIGNED_WORD = 1.0  # longer MFA words are treated as stretched over unexplained audio


def egocom_fa_words(aligned: Path, utts: list[dict], stats: dict[str, int]) -> dict[str, dict[str, list[Interval]]]:
    """session -> speaker -> word intervals from MFA output (recipes/data/egocom_mfa.py corpus).

    Within each utterance window, the MFA words (midpoint inside the window, in order) are matched
    one-to-one with the window's words that were sent to MFA. An MFA word longer than
    EGOCOM_MAX_ALIGNED_WORD (MFA stretching a word, mostly an isolated backchannel, over other
    speakers' speech or noise in the window) is replaced by that word's transcript/interpolated
    interval. Words not sent to MFA (tags, numerals) keep their transcript/interpolated interval.
    If the counts do not match, stretched words are cut to EGOCOM_MAX_ALIGNED_WORD around their
    centre instead. A window MFA left empty falls back entirely to the transcript/interpolated words."""
    import textgrid

    mfa: dict[tuple[str, str], list[Interval]] = {}
    for tg_path in sorted(aligned.glob("*.TextGrid")):
        sess, _, spk = tg_path.stem.rpartition("__")
        tier = next(t for t in textgrid.TextGrid.fromFile(str(tg_path)).tiers if t.name == "words")
        mfa[(sess, spk)] = [(float(i.minTime), float(i.maxTime)) for i in tier
                            if i.mark and i.mark.strip() and i.mark.strip() != "<eps>"]
    cap = EGOCOM_MAX_ALIGNED_WORD
    out: dict[str, dict[str, list[Interval]]] = defaultdict(lambda: defaultdict(list))
    for u in utts:
        orig = [(a, b) for a, b, _ in u["words"]]
        sent = [(a, b) for a, b, in_text in u["words"] if in_text]
        unsent = [(a, b) for a, b, in_text in u["words"] if not in_text]
        got = [(a, b) for a, b in mfa.get((u["session"], u["speaker"]), [])
               if u["start"] <= (a + b) / 2 < u["end"]] if sent else []
        if not got:
            stats["windows_fallback_" + ("unaligned" if sent else "no_text")] += 1
            out[u["session"]][u["speaker"]].extend(orig)
            continue
        stats["windows_mfa"] += 1
        words = []
        matched = len(got) == len(sent)
        stats["windows_matched" if matched else "windows_count_mismatch"] += 1
        for k, (a, b) in enumerate(got):
            if b - a <= cap:
                words.append((a, b))
                stats["words_mfa"] += 1
            elif matched:
                words.append(sent[k])
                stats["words_stretched_replaced"] += 1
            else:
                m = (a + b) / 2
                words.append((m - cap / 2, m + cap / 2))
                stats["words_stretched_cut"] += 1
        stats["words_unsent_kept"] += len(unsent)
        out[u["session"]][u["speaker"]].extend(words + unsent)
    return out


def build_egocom(args) -> None:
    ann = args.corpora / "egocom" / "annotations"
    by_conv: dict[str, list[dict]] = defaultdict(list)
    with open(ann / "ground_truth_transcriptions.csv") as f:
        for r in csv.DictReader(f):
            by_conv[r["conversation_id"]].append(r)
    for split in ("test", "val"):
        w = Writer(args.refs, "egocom", split)
        src = "annotations/ground_truth_transcriptions.csv word timings (facebookresearch/EgoCom-Dataset)"
        stats: dict[str, int] = defaultdict(int)
        w.prov["ref_types"]["words"] = {
            "source": f"{src}; untimed words interpolated (see build_refs.egocom_words); merged per speaker across "
                      f"gaps <= {args.word_gap} s", "word_gap": args.word_gap, "interpolation": stats}
        w.prov["ref_types"]["words_timedonly"] = {
            "source": f"{src}; timed words only (untimed ~10% dropped); merged per speaker across gaps <= {args.word_gap} s",
            "word_gap": args.word_gap}
        w.prov["uem"] = "[0, shortest wearer recording of the conversation part]"
        mfa_dir = args.data / "work" / "egocom_mfa"
        fa = None
        if (mfa_dir / "aligned" / split).is_dir():
            fa_stats: dict[str, int] = defaultdict(int)
            fa = egocom_fa_words(mfa_dir / "aligned" / split,
                                 json.loads((mfa_dir / f"utterances_{split}.json").read_text()), fa_stats)
            w.prov["ref_types"]["fa"] = {
                "source": "Montreal Forced Aligner 3.4.3 (english_mfa acoustic v3.1.0, english_us_mfa dictionary v3.1.0, "
                          "OOVs via english_us_mfa G2P v3.0.0) on each speaker's own head-worn mic "
                          "(recipes/data/egocom_mfa.py); aligned words > 1.0 s replaced by transcript/interpolated times, "
                          "windows MFA left empty fall back to them; "
                          f"merged per speaker across gaps <= {args.word_gap} s",
                "word_gap": args.word_gap, "alignment": dict(fa_stats)}
        for sess_dir in sorted((args.audio / "egocom" / split).iterdir()):
            s = sess_dir.name
            durs = audio_durations(sess_dir)
            dur = min(durs.values())
            if max(durs.values()) - dur > 1.0:
                print(f"  WARNING {s}: wearer recordings differ in length {sorted(durs.values())}", file=sys.stderr)
            rows = by_conv[s]
            timed: dict[str, list[Interval]] = defaultdict(list)
            for r in rows:
                if r["startTime"] and r["endTime"] and r["word"].strip() and float(r["endTime"]) > float(r["startTime"]):
                    timed[f"spk{r['speaker_id']}"].append((float(r["startTime"]), float(r["endTime"])))
            interp: dict[str, list[Interval]] = defaultdict(list)
            for wd in egocom_words(rows, stats):
                interp[f"spk{wd['spk']}"].append((wd["s"], wd["e"]))
            sets = [("words", interp), ("words_timedonly", timed)] + ([("fa", fa[s])] if fa is not None else [])
            for ref_type, words in sets:
                turns = rename([Turn(spk, a, b) for spk, iv in words.items() for a, b in merge_intervals(iv, args.word_gap)])
                check_within(s, turns, dur)
                w.add(ref_type, s, turns)
            w.uem[s] = [(0.0, dur)]
        w.prov["ref_types"]["words"]["interpolation"] = dict(stats)
        w.write()


BUILDERS = {
    "aishell4": build_aishell4,
    "aishell5": build_aishell5,
    "alimeeting": build_alimeeting,
    "notsofar": build_notsofar,
    "chime6": build_chime6,
    "egocom": build_egocom,
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpora_to_build", nargs="+", choices=sorted(BUILDERS), metavar="corpus")
    ap.add_argument("--data", type=Path, default=DATA)
    ap.add_argument("--word-gap", type=float, default=0.3, help="EgoCom: merge words across gaps <= this (s)")
    args = ap.parse_args()
    args.corpora, args.audio, args.refs = args.data / "corpora", args.data / "audio16k", args.data / "refs"
    for c in args.corpora_to_build:
        BUILDERS[c](args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
