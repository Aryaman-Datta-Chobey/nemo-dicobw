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
| egocom     | test, val             | words (ground_truth_transcriptions.csv) | [0, shortest wearer]   |

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


def build_egocom(args) -> None:
    ann = args.corpora / "egocom" / "annotations"
    words: dict[str, dict[str, list[Interval]]] = defaultdict(lambda: defaultdict(list))
    with open(ann / "ground_truth_transcriptions.csv") as f:
        for r in csv.DictReader(f):
            if r["startTime"] and r["endTime"] and r["word"].strip():
                s, e = float(r["startTime"]), float(r["endTime"])
                if e > s:
                    words[r["conversation_id"]][f"spk{r['speaker_id']}"].append((s, e))
    for split in ("test", "val"):
        w = Writer(args.refs, "egocom", split)
        w.prov["ref_types"]["words"] = {
            "source": "annotations/ground_truth_transcriptions.csv word timings (facebookresearch/EgoCom-Dataset), "
                      f"merged per speaker across gaps <= {args.word_gap} s", "word_gap": args.word_gap}
        w.prov["uem"] = "[0, shortest wearer recording of the conversation part]"
        for sess_dir in sorted((args.audio / "egocom" / split).iterdir()):
            s = sess_dir.name
            durs = audio_durations(sess_dir)
            dur = min(durs.values())
            if max(durs.values()) - dur > 1.0:
                print(f"  WARNING {s}: wearer recordings differ in length {sorted(durs.values())}", file=sys.stderr)
            turns = rename([Turn(spk, a, b) for spk, iv in words[s].items()
                            for a, b in merge_intervals(iv, args.word_gap)])
            check_within(s, turns, dur)
            w.add("words", s, turns)
            w.uem[s] = [(0.0, dur)]
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
