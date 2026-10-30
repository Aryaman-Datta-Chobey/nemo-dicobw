#!/usr/bin/env python
"""Rehearsal-ratio manifests for the T2 arms of nemotron-ft-ear1 (see EXPERIMENTS.md, 20261029-nemotron-ft-ear1-t2).

Starts from a base manifest dir (default ear1_v1_fa: 352 EAR-1 lines with forced-alignment labels + 34 rehearsal
lines) and adds rehearsal from corpora in Nemotron-3-Diarization's training data, keeping the EAR-1 lines unchanged.
The NeMo sampler draws one window per manifest line, so the rehearsal share of samples = rehearsal lines / all lines.

Stages (each skipped when its output exists):
  notsofar   convert the train_set / dev_set single-channel (sc_*) streams to 16 kHz and write one FastMSS
             forced-alignment RTTM per stream (the train/dev MFA RTTMs differ between devices of a meeting) to
             refs/notsofar/<split>/rttm/fa/<meeting>__<device>.rttm (session map: chime-utils c8map.json)
  alimeeting extract + convert further Train_Ali_far sessions (forced-alignment RTTMs, as ear1_v1)
  aishell4   extract + convert further AISHELL-4 train_{L,M,S} sessions (official RTTMs, any speaker count)
  manifests  <out>_r<pct>/train.json per --share, one random channel / device per session; the pool of a smaller
             share is a subset of a larger one's, so the arms differ only in the ratio. val / held-out / MUSAN copied.

    python recipes/diarization/prepare_ft_ear1_t2.py --shares 0.25 0.5 --out /mnt/data/manifests/nemotron_ft/ear1_t2
"""
from __future__ import annotations

import argparse
import collections
import json
import random
import shutil
import sys
import tarfile
from pathlib import Path

from prepare_ft_ear1 import DATA, REPO, line, sh, speakers

NOTSOFAR = DATA / "corpora/notsofar/benchmark-datasets"


def notsofar(args) -> list[dict]:
    """One line per (meeting, device); the caller picks one device per meeting."""
    for split in ("train", "dev"):
        if not (DATA / "audio16k/notsofar" / split).is_dir():
            sh([sys.executable, str(REPO / "scripts/convert_16k.py"), "--corpus", "notsofar", "--src", str(DATA / "corpora/notsofar"),
                "--include", f"benchmark-datasets/{split}_set/*/sc_*/*", "--jobs", str(args.jobs),
                "--report-name", f"conversion_report.{split}.tsv"])
    raw = DATA / "raw/notsofar_fa"
    inv = {v: k for k, v in json.loads((raw / "c8map.json").read_text())["sessions_map"]["notsofar1"].items()}
    out = []
    with tarfile.open(raw / "notsofar1-channels_mfa_rttms.tar.gz") as tar:
        for m in tar.getmembers():
            split = m.name.split("/")[0]
            if not (m.isfile() and split in ("train", "dev") and m.name.endswith(".rttm")):
                continue
            meeting, _, rest = inv[Path(m.name).stem].partition("_")[2].partition("_")  # MTG_<id>_<device>_sc
            meeting, device = f"MTG_{meeting}", "sc_" + rest.removesuffix("_sc")
            audio = DATA / "audio16k/notsofar" / split / meeting / f"{device}.flac"
            if not audio.exists():
                raise FileNotFoundError(f"{m.name}: no converted audio {audio}")
            rttm = DATA / "refs/notsofar" / split / "rttm/fa" / f"{meeting}__{device}.rttm"
            if not rttm.exists():
                rttm.parent.mkdir(parents=True, exist_ok=True)
                rttm.write_bytes(tar.extractfile(m).read())
            r = line(audio, rttm, f"notsofar_{split}")
            if max(float(p[3]) + float(p[4]) for p in (x.split() for x in rttm.read_text().splitlines()) if p) > r["duration"] + 0.5:
                raise ValueError(f"{rttm} ends after its audio")
            out.append({**r, "session": meeting})
    eval_meetings = {p.name for p in (DATA / "audio16k/notsofar/eval").iterdir()}
    if eval_meetings & {r["session"] for r in out}:
        raise ValueError("NOTSOFAR train/dev meeting also in eval")
    return out


def alimeeting(args, exclude: set[str], n: int, rng: random.Random) -> list[dict]:
    fa = DATA / "refs/alimeeting/forced_alignment/AliMeeting/Train_Ali_far"
    pool = sorted(f.stem for f in fa.glob("*.rttm") if f.stem not in exclude)
    chosen = sorted(rng.sample(pool, n))
    audio = DATA / "audio16k/alimeeting/Train_Ali"
    todo = [s for s in chosen if not (audio / s / "far_ch1.flac").exists()]
    if todo:
        sh(["tar", "-I", "pigz", "-xf", str(DATA / "raw/alimeeting/Train_Ali_far.tar.gz"), "-C", str(DATA / "corpora/alimeeting/Train_Ali"),
            "--wildcards", *[f"Train_Ali_far/audio_dir/{s}_*.wav" for s in todo]])
        sh([sys.executable, str(REPO / "scripts/convert_16k.py"), "--corpus", "alimeeting", "--src", str(DATA / "corpora/alimeeting"),
            "--include", "Train_Ali/*", "--jobs", str(args.jobs), "--report-name", "conversion_report.train_t2.tsv"])
    return [{**line(rng.choice(sorted((audio / s).glob("far_ch*.flac"))), fa / f"{s}.rttm", "alimeeting_train"), "session": s}
            for s in chosen]


def aishell4(args, exclude: set[str], n: int, rng: random.Random) -> list[dict]:
    src = DATA / "corpora/aishell4"
    pool = []
    for part in ("train_L", "train_M", "train_S"):
        tg = src / part / "TextGrid"
        if not any(tg.glob("*.rttm")):
            sh(["tar", "-I", "pigz", "-xf", str(DATA / f"raw/aishell4/{part}.tar.gz"), "-C", str(src), "--wildcards", f"{part}/TextGrid/*.rttm"])
        pool += [(part, f.stem) for f in sorted(tg.glob("*.rttm")) if f.stem not in exclude]
    chosen = sorted(rng.sample(pool, n))
    for part in ("train_L", "train_M", "train_S"):
        todo = [s for p, s in chosen if p == part and not (DATA / "audio16k/aishell4" / part / s / "far_ch1.flac").exists()]
        if todo:
            sh(["tar", "-I", "pigz", "-xf", str(DATA / f"raw/aishell4/{part}.tar.gz"), "-C", str(src), "--wildcards",
                *[f"{part}/wav/{s}.flac" for s in todo]])
            sh([sys.executable, str(REPO / "scripts/convert_16k.py"), "--corpus", "aishell4", "--src", str(src),
                "--include", f"{part}/*", "--jobs", str(args.jobs), "--report-name", f"conversion_report.{part}_t2.tsv"])
    return [{**line(rng.choice(sorted((DATA / "audio16k/aishell4" / p / s).glob("far_ch*.flac"))), src / p / "TextGrid" / f"{s}.rttm",
                    "aishell4_train"), "session": s} for p, s in chosen]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", type=Path, default=DATA / "manifests/nemotron_ft/ear1_v1_fa")
    ap.add_argument("--out", type=Path, required=True, help="prefix; writes <out>_r<pct>/ per share")
    ap.add_argument("--shares", type=float, nargs="+", default=[0.25, 0.5], help="rehearsal share of manifest lines")
    ap.add_argument("--mix", type=float, nargs=3, default=[0.4, 0.3, 0.3], metavar=("ALI", "A4", "NSF"),
                    help="target corpus mix of the rehearsal lines (AliMeeting, AISHELL-4, NOTSOFAR)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--jobs", type=int, default=10)
    args = ap.parse_args()
    rng = random.Random(args.seed)

    base = [json.loads(x) for x in (args.base / "train.json").read_text().splitlines() if x.strip()]
    ear1 = [r for r in base if r["corpus"].startswith("ear1")]
    old = [r for r in base if not r["corpus"].startswith("ear1")]
    old_sess = {Path(r["rttm_filepath"]).stem for r in old}
    n_max = round(len(ear1) * max(args.shares) / (1 - max(args.shares)))
    corpora = ("alimeeting_train", "aishell4_train", "notsofar")  # order of --mix
    quota = {c: round(n_max * f) for c, f in zip(corpora, args.mix)}
    have = collections.Counter(r["corpus"] for r in old)

    nsf = notsofar(args)
    by_meeting = collections.defaultdict(list)
    for r in nsf:
        by_meeting[r["session"]].append(r)
    meetings = sorted(by_meeting)
    rng.shuffle(meetings)
    if quota["notsofar"] > len(meetings):
        raise ValueError(f"NOTSOFAR has {len(meetings)} train/dev meetings, quota {quota['notsofar']}")
    new = {"notsofar": [rng.choice(by_meeting[m]) for m in meetings[:quota["notsofar"]]],
           "alimeeting_train": alimeeting(args, old_sess, quota["alimeeting_train"] - have["alimeeting_train"], rng),
           "aishell4_train": aishell4(args, old_sess, quota["aishell4_train"] - have["aishell4_train"], rng)}
    for v in new.values():
        rng.shuffle(v)

    for share in sorted(args.shares):
        n = round(len(ear1) * share / (1 - share))
        # the base rehearsal lines first, then a fixed-order prefix of each corpus' new lines
        take = {c: max(0, round(n * f) - have[c]) for c, f in zip(corpora, args.mix)}
        reh = old + [r for c, rows in new.items() for r in rows[:take[c]]]
        out = Path(f"{args.out}_r{round(100 * share)}")
        out.mkdir(parents=True, exist_ok=True)
        rows = [{k: v for k, v in r.items() if k != "session"} for r in ear1 + reh]
        rng.shuffle(rows)
        (out / "train.json").write_text("".join(json.dumps(r) + "\n" for r in rows))
        for f in ("val.json", "heldout_D1.jsonl", "heldout_R1.jsonl", "musan_noise.json"):
            shutil.copy(args.base / f, out / f)
        lines = collections.Counter(r["corpus"] for r in rows)
        hours = collections.Counter()
        for r in rows:
            hours[r["corpus"]] += r["duration"] / 3600
        spk = collections.Counter(min(r["num_speakers"], 8) for r in reh)
        summary = {"base": str(args.base), "share_target": share, "rehearsal_lines": len(reh), "lines": len(rows),
                   "share_lines": round(len(reh) / len(rows), 4), "lines_by_corpus": dict(lines),
                   "hours_by_corpus": {k: round(v, 2) for k, v in hours.items()}, "rehearsal_num_speakers": dict(sorted(spk.items())),
                   "seed": args.seed, "mix": args.mix}
        (out / "config.json").write_text(json.dumps(summary, indent=1))
        print(json.dumps(summary), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
