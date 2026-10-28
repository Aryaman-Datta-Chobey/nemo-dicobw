#!/usr/bin/env python
"""Data for fine-tuning Nemotron-3-Diarization on EAR-1 (ESD-ON), with rehearsal and noise.

Stages (each skipped when its output exists):
  rehearsal-alimeeting  extract --ali-sessions random AliMeeting Train_Ali_far sessions (seed --seed) from
                        the raw tarball, convert to 16 kHz (all far channels; one random channel per
                        session is used), forced-alignment RTTMs (nttcslab-sp/diar-forced-alignment)
  rehearsal-aishell4    extract the AISHELL-4 train_M sessions with >= --a4-min-spk speakers (up to
                        --a4-sessions), convert, official RTTMs; one random channel per session
  musan                 extract MUSAN noise/ and write a NeMo noise manifest (augmentor input)
  manifests             <out>/train.json   EAR-1 train sessions except the held-out ones, every D1, R1 and H*
                                           view (sessions with >= 2 female speakers repeated --female-repeat
                                           times; genders from refs/ear1/spk_gender.json = spkinfo.xlsx),
                                           plus the rehearsal recordings
                        <out>/val.json     EAR-1 dev D1 + R1 (NeMo validation during training)
                        <out>/heldout_{D1,R1}.jsonl  the held-out EAR-1 train sessions in the eval-manifest
                                           format of make_eval_manifests.py (checkpoint selection)
Held-out sessions: the EAR-1 train sessions whose speakers occur in no other train session (the speaker
graph of train has one 16-speaker component over 53 sessions and two isolated sessions).
Manifest lines: {"audio_filepath", "offset": 0, "duration", "num_speakers", "rttm_filepath", "corpus"}.

    python recipes/diarization/prepare_ft_ear1.py --out /mnt/data/manifests/nemotron_ft/ear1_v1
"""
from __future__ import annotations

import argparse
import collections
import json
import random
import subprocess
import sys
from pathlib import Path

import soundfile as sf

DATA = Path("/mnt/data")
REPO = Path(__file__).resolve().parents[2]


def sh(cmd: list[str]) -> None:
    print("+", " ".join(cmd), flush=True)
    subprocess.run(cmd, check=True)


def speakers(rttm: Path) -> set[str]:
    return {ln.split()[7] for ln in rttm.read_text().splitlines() if ln.startswith("SPEAKER")}


def line(audio: Path, rttm: Path, corpus: str) -> dict:
    return {"audio_filepath": str(audio), "offset": 0.0, "duration": round(sf.info(str(audio)).duration, 3),
            "num_speakers": len(speakers(rttm)), "rttm_filepath": str(rttm), "corpus": corpus}


def heldout_sessions(rttm_dir: Path) -> list[str]:
    sess = {f.stem: speakers(f) for f in sorted(rttm_dir.glob("*.rttm"))}
    count = collections.Counter(s for spk in sess.values() for s in spk)
    return sorted(s for s, spk in sess.items() if all(count[x] == 1 for x in spk))


def rehearsal_alimeeting(args, rng: random.Random) -> list[dict]:
    fa = DATA / "refs/alimeeting/forced_alignment/AliMeeting/Train_Ali_far"
    chosen = sorted(rng.sample(sorted(f.stem for f in fa.glob("*.rttm")), args.ali_sessions))
    src = DATA / "corpora/alimeeting/Train_Ali"
    audio = DATA / "audio16k/alimeeting/Train_Ali"
    if not all((audio / s / "far_ch1.flac").exists() for s in chosen):
        src.mkdir(parents=True, exist_ok=True)
        sh(["tar", "-I", "pigz", "-xf", str(DATA / "raw/alimeeting/Train_Ali_far.tar.gz"), "-C", str(src),
            "--wildcards", *[f"Train_Ali_far/audio_dir/{s}_*.wav" for s in chosen]])
        sh([sys.executable, str(REPO / "scripts/convert_16k.py"), "--corpus", "alimeeting", "--src",
            str(DATA / "corpora/alimeeting"), "--include", "Train_Ali/*", "--jobs", str(args.jobs),
            "--report-name", "conversion_report.train_rehearsal.tsv"])
    out = []
    for s in chosen:
        ch = rng.choice(sorted((audio / s).glob("far_ch*.flac")))
        out.append(line(ch, fa / f"{s}.rttm", "alimeeting_train"))
    return out


def rehearsal_aishell4(args, rng: random.Random) -> list[dict]:
    raw = DATA / "raw/aishell4/train_M.tar.gz"
    src = DATA / "corpora/aishell4"
    tg = src / "train_M/TextGrid"
    if not tg.is_dir():
        sh(["tar", "-I", "pigz", "-xf", str(raw), "-C", str(src), "--wildcards", "train_M/TextGrid/*.rttm"])
    many = sorted(f.stem for f in tg.glob("*.rttm") if len(speakers(f)) >= args.a4_min_spk)
    chosen = sorted(rng.sample(many, min(args.a4_sessions, len(many))))
    audio = DATA / "audio16k/aishell4/train_M"
    if not all((audio / s / "far_ch1.flac").exists() for s in chosen):
        sh(["tar", "-I", "pigz", "-xf", str(raw), "-C", str(src), "--wildcards",
            *[f"train_M/wav/{s}.flac" for s in chosen]])
        sh([sys.executable, str(REPO / "scripts/convert_16k.py"), "--corpus", "aishell4", "--src", str(src),
            "--include", "train_M/*", "--jobs", str(args.jobs), "--report-name", "conversion_report.train_rehearsal.tsv"])
    out = []
    for s in chosen:
        ch = rng.choice(sorted((audio / s).glob("far_ch*.flac")))
        out.append(line(ch, tg / f"{s}.rttm", "aishell4_train"))
    return out


def musan_noise(args) -> Path:
    root = DATA / "corpora/musan"
    man = args.out / "musan_noise.json"
    if not (root / "musan/noise").is_dir():
        root.mkdir(parents=True, exist_ok=True)
        sh(["tar", "-I", "pigz", "-xf", str(DATA / "raw/musan/musan.tar.gz"), "-C", str(root), "--wildcards", "musan/noise/*"])
    rows = [{"audio_filepath": str(f), "offset": 0.0, "duration": round(sf.info(str(f)).duration, 3), "text": ""}
            for f in sorted((root / "musan/noise").rglob("*.wav"))]
    man.write_text("".join(json.dumps(r) + "\n" for r in rows))
    print(f"musan noise: {len(rows)} files -> {man}")
    return man


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--ali-sessions", type=int, default=24)
    ap.add_argument("--a4-sessions", type=int, default=10)
    ap.add_argument("--a4-min-spk", type=int, default=5)
    ap.add_argument("--female-repeat", type=int, default=2,
                    help="repeat EAR-1 views of sessions with >= 2 female speakers (similar-voice discrimination)")
    ap.add_argument("--jobs", type=int, default=8)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    refs = DATA / "refs/ear1/train/rttm/segments"
    held = heldout_sessions(refs)
    gender = json.loads((DATA / "refs/ear1/spk_gender.json").read_text())
    print(f"held-out EAR-1 train sessions: {held}")
    train = []
    for sess_dir in sorted((DATA / "audio16k/ear1/train").iterdir()):
        if sess_dir.name in held:
            continue
        for f in sorted(sess_dir.glob("*.flac")):
            if f.stem in ("D1", "R1") or f.stem.startswith("H"):
                r = line(f, refs / f"{sess_dir.name}.rttm", f"ear1_{f.stem[0]}")
                n_female = sum(gender.get(s) == "Female" for s in speakers(Path(r["rttm_filepath"])))
                train += [r] * (args.female_repeat if n_female >= 2 else 1)
    ear1_h = sum(r["duration"] for r in train) / 3600
    train += rehearsal_alimeeting(args, rng)
    train += rehearsal_aishell4(args, rng)
    musan_noise(args)
    rng.shuffle(train)
    (args.out / "train.json").write_text("".join(json.dumps(r) + "\n" for r in train))
    hours = collections.Counter()
    for r in train:
        hours[r["corpus"]] += r["duration"] / 3600
    print("train hours:", {k: round(v, 1) for k, v in sorted(hours.items())},
          f"rehearsal share {100 * (sum(hours.values()) - ear1_h) / sum(hours.values()):.1f}%")

    val = []
    man = DATA / "manifests/nemo"
    for t in ("D1", "R1"):
        for ln in (man / f"ear1_dev_{t}.jsonl").read_text().splitlines():
            r = json.loads(ln)
            val.append(line(Path(r["audio_filepath"]), Path(r["rttm_filepath"]), f"ear1_dev_{t}"))
        rows = [json.loads(x) for x in (man / f"ear1_train_{t}.jsonl").read_text().splitlines()]
        (args.out / f"heldout_{t}.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows if r["session"] in held))
    (args.out / "val.json").write_text("".join(json.dumps(r) + "\n" for r in val))
    (args.out / "config.json").write_text(json.dumps({**{k: (str(v) if isinstance(v, Path) else v) for k, v in vars(args).items()},
                                                       "heldout": held, "train_hours": {k: round(v, 2) for k, v in hours.items()}}, indent=1))
    print(f"train {len(train)} recordings, val {len(val)}, held-out {held}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
