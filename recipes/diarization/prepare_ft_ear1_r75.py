#!/usr/bin/env python
"""75% rehearsal manifests for nemotron-ft-ear1 (see EXPERIMENTS.md, 20261029-nemotron-ft-ear1-r75).

The T2 r50 manifest already uses every rehearsal session on disk (AliMeeting Train_Ali_far 141, AISHELL-4 train 106,
NOTSOFAR train/dev 108 meetings), one random channel / device each. A 75% share needs 3 x 352 = 1056 rehearsal lines,
so the extra lines come from one of two sources:
  a  other channels / devices of the r50 sessions (same voices and conversations, other acoustics), 40/30/30 mix
     AliMeeting / AISHELL-4 / NOTSOFAR of rehearsal lines as in T2
  b  new sessions first: AMI train (Array1-01, forced-alignment RTTMs) and ICSI (headset mix, word-level RTTMs; meetings
     with > 8 reference speakers dropped, Nemotron's cap); the remainder from option a's extra views (a prefix of a's
     per-corpus view order, so b's views are a subset of a's)
EAR-1 lines and the r50 rehearsal lines are unchanged (r25 c r50 c r75a, r75b). Extra views are spread round-robin over
sessions in a seeded order. val / held-out / MUSAN copied from r50.

    python recipes/diarization/prepare_ft_ear1_r75.py --out /mnt/data/manifests/nemotron_ft/ear1_t2
"""
from __future__ import annotations

import argparse
import collections
import json
import random
import shutil
from pathlib import Path

from prepare_ft_ear1 import DATA, line, speakers

MIX = {"alimeeting_train": 0.4, "aishell4_train": 0.3, "notsofar": 0.3}
MAX_SPK = 8


def group(corpus: str) -> str:
    return "notsofar" if corpus.startswith("notsofar_") else corpus


def other_views(r: dict) -> list[dict]:
    """Every other converted channel / device of a rehearsal line's session, as manifest lines."""
    audio = Path(r["audio_filepath"])
    if r["corpus"] in ("alimeeting_train", "aishell4_train"):
        return [line(a, Path(r["rttm_filepath"]), r["corpus"]) for a in sorted(audio.parent.glob("far_ch*.flac")) if a != audio]
    split, meeting = r["corpus"].removeprefix("notsofar_"), audio.parent.name
    out = []
    for a in sorted(audio.parent.glob("sc_*.flac")):
        rttm = DATA / "refs/notsofar" / split / "rttm/fa" / f"{meeting}__{a.stem}.rttm"
        if a != audio and rttm.exists():  # devices without a FastMSS RTTM are skipped
            out.append(line(a, rttm, r["corpus"]))
    return out


def views_in_order(rehearsal: list[dict], used: set[str], rng: random.Random) -> dict[str, list[dict]]:
    """Per corpus group: extra views ordered round-robin over sessions (seeded), so any prefix spreads evenly. Audio
    already in the base manifest is excluded and each view listed once (a session can have two base lines)."""
    by_group: dict[str, list[list[dict]]] = collections.defaultdict(list)
    seen = set(used)
    for r in rehearsal:
        v = [x for x in other_views(r) if x["audio_filepath"] not in seen]
        seen.update(x["audio_filepath"] for x in v)
        rng.shuffle(v)
        if v:
            by_group[group(r["corpus"])].append(v)
    out = {}
    for g, sess in by_group.items():
        rng.shuffle(sess)
        out[g] = [s[i] for i in range(max(map(len, sess))) for s in sess if i < len(s)]
    return out


def new_sessions() -> list[dict]:
    ami = [line(DATA / "audio16k/ami/train" / f.stem / "Array1-01.flac", f, "ami_train")
           for f in sorted((DATA / "refs/ami/train/rttm/fa").glob("*.rttm"))]
    icsi = [line(DATA / "audio16k/icsi/train" / f.stem / "mix.flac", f, "icsi_train")
            for f in sorted((DATA / "refs/icsi/train/rttm/words").glob("*.rttm")) if len(speakers(f)) <= MAX_SPK]
    return ami + icsi


def take_views(views: dict[str, list[dict]], n: int) -> list[dict]:
    want = {g: round(n * w) for g, w in MIX.items()}
    want["alimeeting_train"] += n - sum(want.values())
    out = []
    for g, k in want.items():
        if k > len(views[g]):
            raise ValueError(f"{g}: {k} extra views wanted, {len(views[g])} available")
        out += views[g][:k]
    return out


def write(dst: Path, src: Path, lines: list[dict], info: dict) -> None:
    dst.mkdir(parents=True, exist_ok=True)
    for f in ("val.json", "heldout_D1.jsonl", "heldout_R1.jsonl", "musan_noise.json"):
        shutil.copy(src / f, dst / f)
    (dst / "train.json").write_text("".join(json.dumps(x) + "\n" for x in lines))
    (dst / "config.json").write_text(json.dumps(info, indent=1) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", type=Path, default=DATA / "manifests/nemotron_ft/ear1_t2_r50")
    ap.add_argument("--out", type=Path, required=True, help="prefix; writes <out>_r75a/ and <out>_r75b/")
    ap.add_argument("--share", type=float, default=0.75)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    base = [json.loads(x) for x in (args.base / "train.json").read_text().splitlines() if x.strip()]
    ear1 = [r for r in base if r["corpus"].startswith("ear1_")]
    rehearsal = [r for r in base if not r["corpus"].startswith("ear1_")]
    n_reh = round(len(ear1) * args.share / (1 - args.share))
    rng = random.Random(args.seed)
    used = {r["audio_filepath"] for r in base}
    views = views_in_order(rehearsal, used, rng)
    new = new_sessions()
    if any(r["audio_filepath"] in used for r in new):
        raise ValueError("new-session line already in the base manifest")
    for opt, extra in (("a", take_views(views, n_reh - len(rehearsal))),
                       ("b", new + take_views(views, n_reh - len(rehearsal) - len(new)))):
        lines = ear1 + rehearsal + extra
        paths = [r["audio_filepath"] for r in lines]
        reh_paths = [r["audio_filepath"] for r in rehearsal + extra]  # EAR-1 lines repeat by design (--female-repeat)
        if len(reh_paths) != len(set(reh_paths)) or set(reh_paths) & {r["audio_filepath"] for r in ear1}:
            raise ValueError(f"r75{opt}: duplicate rehearsal audio lines")
        if any("/eval/" in p or "/test" in p.lower() or "/dev/" in p and "/notsofar/" not in p for p in paths):
            raise ValueError(f"r75{opt}: held-out audio in the training manifest")
        reh = [r for r in lines if not r["corpus"].startswith("ear1_")]
        info = {"base": str(args.base), "option": opt, "share_target": args.share, "lines": len(lines),
                "rehearsal_lines": len(reh), "share_lines": round(len(reh) / len(lines), 4),
                "distinct_rehearsal_sessions": len({(r["corpus"], Path(r["rttm_filepath"]).stem.split("__")[0]) for r in reh}),
                "lines_by_corpus": dict(collections.Counter(r["corpus"] for r in lines)),
                "hours_by_corpus": {c: round(sum(r["duration"] for r in lines if r["corpus"] == c) / 3600, 2)
                                    for c in sorted({r["corpus"] for r in lines})},
                "rehearsal_num_speakers": dict(sorted(collections.Counter(r["num_speakers"] for r in reh).items())),
                "seed": args.seed, "mix": MIX}
        write(Path(f"{args.out}_r75{opt}"), args.base, lines, info)
        print(f"r75{opt}: {json.dumps(info)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
