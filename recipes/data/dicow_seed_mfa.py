#!/usr/bin/env python
"""MFA corpora for the close-talk seed voices of the open DiCoW simulations (EXPERIMENTS.md 20261031-dicow-open-prep).

Reads the transcripts written by recipes/data/punctuate_transcripts.py (`clean` text) and writes, under <work>/corpus/<corpus>/:

  alimeeting  <session>__<file>.{flac,TextGrid}  Train_Ali near-field, one tier named after the speaker. Near-field tiers
              are labelled `c1` / `S3`, so the speaker comes from the far-field tier with the same session and times
              (globally unique SPK id; one speaker can attend several meetings).
  aishell5    <session>__<DA0x>.{flac,TextGrid}  train close-talk, one tier per file.
  ascend      <speaker>/<id>.{flac,lab}          train clips, already one utterance each.

Text as recipes/data/mfa_zh.py. Utterances with Latin letters or digits are not sent to MFA, whose Mandarin
dictionary and G2P cannot pronounce them; <work>/utterances_<corpus>.json lists every utterance with `sent`.

  ascend-audio  extract the ASCEND train clips to audio16k/ascend/train/<speaker>/<id>.flac   (punc env, has pyarrow)
  prepare       write the MFA corpora                                                        (dicow env)
  topup         corpora for utterances `prepare` left out, under <work>/corpus/topup_{en,zh}/ (dicow env):
                  topup_en  only Latin words, English MFA dictionary (lowercase, spaces as written)
                  topup_zh  AliMeeting and AISHELL-5 Han + Latin, Mandarin dictionary, whose Latin entries and G2P give
                            letters and acronyms a Mandarin pronunciation
                Utterances with digits stay out, as do mixed ASCEND clips. <work>/utterances_topup.json lists what was sent.
"""
from __future__ import annotations

import argparse
import io
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

DATA = Path("/mnt/data")
sys.path.insert(0, str(Path(__file__).resolve().parent))


def load(text_dir: Path, corpus: str) -> list[dict]:
    with open(text_dir / f"{corpus}.jsonl", encoding="utf-8") as f:
        return [json.loads(ln) for ln in f]


def link(src: Path, dst: Path) -> None:
    if dst.is_symlink() or dst.exists():
        dst.unlink()
    dst.symlink_to(src)


def ascend_audio(args) -> None:
    import pyarrow.parquet as pq
    import soundfile as sf

    n = Counter()
    for p in sorted((args.data / "raw/ascend/hf/main").glob("train-*.parquet")):
        for x in pq.read_table(p, columns=["id", "audio", "original_speaker_id"]).to_pylist():
            out = args.data / "audio16k/ascend/train" / f"ascend_{x['original_speaker_id']}" / f"{x['id']}.flac"
            out.parent.mkdir(parents=True, exist_ok=True)
            wav, sr = sf.read(io.BytesIO(x["audio"]["bytes"]), dtype="int16")
            if sr != 16000 or wav.ndim != 1:
                raise ValueError(f"{x['id']}: {sr} Hz, shape {wav.shape}")
            sf.write(out, wav, sr, format="FLAC")
            n["clips"] += 1
            n["seconds"] += len(wav) / sr
    print(f"ascend audio: {dict(n)}", flush=True)


def session_tiers(args, corpus: str, groups: dict[tuple[str, str, str], list[dict]], audio_of, dic, max_len) -> None:
    import soundfile as sf

    from mfa_zh import mfa_text
    from egocom_mfa import textgrid

    out = args.work / "corpus" / corpus
    out.mkdir(parents=True, exist_ok=True)
    utts, n = [], Counter()
    for (session, file, speaker), rows in sorted(groups.items()):
        audio = audio_of(session, file)
        if not audio.exists():
            n["files_without_audio"] += 1
            continue
        dur = sf.info(str(audio)).duration
        rows = sorted(rows, key=lambda r: (r["start"], r["end"]))
        intervals, last = [], 0.0
        for i, r in enumerate(rows):
            s, e = r["start"], r["end"]
            lo = max(0.0, s - args.pad, (rows[i - 1]["end"] + s) / 2 if i else 0.0, last)
            hi = min(dur, e + args.pad, (e + rows[i + 1]["start"]) / 2 if i + 1 < len(rows) else dur)
            t = mfa_text(r["clean"], dic, max_len)
            sent = bool(t) and round(lo, 3) < round(hi, 3)
            n["sent" if sent else "not_sent"] += 1
            if sent:
                intervals.append((round(lo, 3), round(hi, 3), t))
                last = round(hi, 3)
            utts.append({"session": session, "file": file, "speaker": speaker, "start": s, "end": e, "win": [lo, hi],
                         "sent": sent, "clean": r["clean"], "punct": r["punct"]})
        stem = f"{session}__{file}"
        link(audio, out / f"{stem}.flac")
        textgrid(out / f"{stem}.TextGrid", speaker, round(dur, 3), intervals)
        n["files"] += 1
    (args.work / f"utterances_{corpus}.json").write_text(json.dumps(utts, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{corpus}: {dict(n)}, {len({u['speaker'] for u in utts})} speakers", flush=True)


def alimeeting(args, dic, max_len) -> None:
    rows = load(args.text_dir, "alimeeting")
    key = lambda r: (r["session"], round(r["start"], 3), round(r["end"], 3))
    far = {key(r): r["speaker"] for r in rows if r["tier_source"] == "far"}
    groups = defaultdict(list)
    for r in rows:
        if r["tier_source"] == "near":
            label = far[key(r)]  # R0003_M0046_F_SPK0093
            gender, spk = label.split("_")[-2:]
            groups[(r["session"], f"{gender}_{spk}", f"alimeeting_{spk}")].append(r)
    audio = lambda session, file: args.data / "audio16k/alimeeting/Train_Ali" / session / f"{file}.flac"
    session_tiers(args, "alimeeting", groups, audio, dic, max_len)


def aishell5(args, dic, max_len) -> None:
    groups = defaultdict(list)
    for r in load(args.text_dir, "aishell5"):
        if r["tier_source"].startswith("DA"):
            groups[(r["session"], r["tier_source"], f"aishell5_{r['speaker']}")].append(r)
    audio = lambda session, file: args.data / "audio16k/aishell5/train" / session / f"{file}.flac"
    session_tiers(args, "aishell5", groups, audio, dic, max_len)


def ascend(args, dic, max_len) -> None:
    from mfa_zh import mfa_text

    utts, n = [], Counter()
    for r in load(args.text_dir, "ascend"):
        audio = args.data / "audio16k/ascend/train" / r["speaker"] / f"{r['tier_source']}.flac"
        t = mfa_text(r["clean"], dic, max_len)
        n["sent" if t else "not_sent"] += 1
        utts.append({"session": r["session"], "file": r["tier_source"], "speaker": r["speaker"], "audio": str(audio),
                     "sent": bool(t), "clean": r["clean"], "punct": r["punct"]})
        if t:
            d = args.work / "corpus/ascend" / r["speaker"]
            d.mkdir(parents=True, exist_ok=True)
            link(audio, d / audio.name)
            (d / f"{audio.stem}.lab").write_text(t + "\n", encoding="utf-8")
    (args.work / "utterances_ascend.json").write_text(json.dumps(utts, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"ascend: {dict(n)}, {len({u['speaker'] for u in utts})} speakers", flush=True)


def prepare(args) -> None:
    from mfa_zh import DICT

    dic = {ln.split("\t", 1)[0] for ln in DICT.read_text(encoding="utf-8").splitlines() if ln.strip()}
    for f in (alimeeting, aishell5, ascend):
        f(args, dic, 4)


def topup(args) -> None:
    from mfa_zh import DICT, HAN, TAG, words_of
    from egocom_mfa import textgrid
    import soundfile as sf

    dic = {ln.split("\t", 1)[0] for ln in DICT.read_text(encoding="utf-8").splitlines() if ln.strip()}
    token = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)*|[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]+")
    groups, sent, n = defaultdict(list), [], Counter()
    for corpus in ("ascend", "alimeeting", "aishell5"):
        for u in json.loads((args.work / f"utterances_{corpus}.json").read_text(encoding="utf-8")):
            if u["sent"]:
                continue
            text = TAG.sub(" ", unicodedata.normalize("NFKC", u["clean"]))
            toks = token.findall(text)
            latin = [t.lower() for t in toks if not HAN.fullmatch(t)]
            if not latin or re.search(r"\d", text):
                n[f"{corpus}_left_out"] += 1
                continue
            if len(latin) == len(toks):
                lang, words = "en", latin
            elif corpus == "ascend":
                n["ascend_mixed_left_out"] += 1
                continue
            else:
                lang = "zh"
                words = [w for t in toks for w in (words_of(dic, t, 4) if HAN.fullmatch(t) else [t.lower()])]
                n["zh_latin_tokens"] += len(latin)
                n["zh_latin_in_dict"] += sum(t in dic for t in latin)
            line = " ".join(words)
            if corpus == "ascend":
                audio = Path(u["audio"])
                d = args.work / f"corpus/topup_{lang}" / u["speaker"]
                d.mkdir(parents=True, exist_ok=True)
                link(audio, d / audio.name)
                (d / f"{audio.stem}.lab").write_text(line + "\n", encoding="utf-8")
            else:
                lo, hi = round(u["win"][0], 3), round(u["win"][1], 3)
                if lo >= hi:
                    n[f"{corpus}_empty_window"] += 1
                    continue
                groups[(lang, corpus, u["session"], u["file"], u["speaker"])].append((lo, hi, line))
            n[f"{corpus}_{lang}"] += 1
            sent.append({**u, "topup": lang, "words": line})
    for (lang, corpus, session, file, speaker), iv in sorted(groups.items()):
        sub = "Train_Ali" if corpus == "alimeeting" else "train"
        audio = args.data / "audio16k" / corpus / sub / session / f"{file}.flac"
        out = args.work / f"corpus/topup_{lang}"
        out.mkdir(parents=True, exist_ok=True)
        stem = f"{session}__{file}"
        link(audio, out / f"{stem}.flac")
        textgrid(out / f"{stem}.TextGrid", speaker, round(sf.info(str(audio)).duration, 3), sorted(iv))
    (args.work / "utterances_topup.json").write_text(json.dumps(sent, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"topup: {dict(n)}", flush=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", choices=["ascend-audio", "prepare", "topup"])
    ap.add_argument("--data", type=Path, default=DATA)
    ap.add_argument("--text-dir", type=Path, default=DATA / "work/dicow_open/text")
    ap.add_argument("--work", type=Path, default=DATA / "work/dicow_open/mfa")
    ap.add_argument("--pad", type=float, default=0.5)
    args = ap.parse_args()
    {"ascend-audio": ascend_audio, "prepare": prepare, "topup": topup}[args.stage](args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
