#!/usr/bin/env python
"""Extract EAR-1 Train&Dev and apply the organisers' mandatory corrections (see EXPERIMENTS.md, 20261027-ear1-setup).

Steps (each idempotent; a marker file in the data root records completion):
  1. extract   Train&Dev.zip -> <out>/TrainDev/<session>/ (sessions at the archive root; a single
               wrapper folder, if present, is dropped)
  2. timeline  extract correct.zip over it (audio/TextGrid timeline fixes for 20260909-6, 20260911-1,
               20260911-5, 20260911-6), replacing files
  3. speakers  speaker-ID corrections (correct_v2.txt): rename A/P###.{WAV,TextGrid} through temporary
               names (IDs swap) and rename the tiers in every TextGrid of the session; P040 of 20260924-8
               is deleted (headset files and its tier everywhere)
  4. exclude   move session 20260916-5 out of the data root to <out>/excluded/
  5. split     write <data root>/split.lst from the shipped split without 20260916-5; copy spkinfo.xlsx
Then validates: 55 train / 7 dev sessions, 27 / 20 speakers, speaker-disjoint, and in every session the
headset speakers equal the tier names of every TextGrid.

    python recipes/data/ear1_prepare.py --raw /mnt/data/raw/ear1 --out /mnt/data/corpora/ear1
"""
from __future__ import annotations

import argparse
import re
import shutil
import zipfile
from pathlib import Path

SPEAKER_FIX = {
    "20260910-4": {"P011": "P013", "P012": "P016", "P013": "P015", "P017": "P012", "P018": "P019"},
    "20260924-2": {"P029": "P034", "P030": "P035", "P032": "P031", "P033": "P036", "P034": "P029",
                   "P035": "P032", "P036": "P030"},
    "20260924-8": {"P037": "P045", "P038": "P046", "P039": "P047", "P040": None, "P041": "P048",
                   "P042": "P049", "P043": "P050", "P044": "P051"},
}
EXCLUDE = "20260916-5"
N_TRAIN, N_DEV, SPK_TRAIN, SPK_DEV = 55, 7, 27, 20
NAME = re.compile(r'^(\s*name = ")(P\d{3})(" *\r?)$')


def done(root: Path, step: str) -> bool:
    return (root / f".done_{step}").exists()


def mark(root: Path, step: str) -> None:
    (root / f".done_{step}").touch()
    print(f"[{step}] done")


def extract(zpath: Path, dest: Path) -> None:
    with zipfile.ZipFile(zpath) as z:
        tops = {Path(i.filename).parts[0] for i in z.infolist()}
        # a single top folder that is not a session (e.g. "Train&Dev/") wraps the sessions
        strip_top = len(tops) == 1 and not re.fullmatch(r"\d{8}-\d+", next(iter(tops)))
        for info in z.infolist():
            parts = Path(info.filename).parts
            rel = Path(*parts[1:]) if strip_top else Path(*parts)
            if not rel.parts or info.is_dir():
                continue
            target = dest / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            with z.open(info) as src, open(target, "wb") as dst:
                shutil.copyfileobj(src, dst, 16 << 20)


def rewrite_tiers(tg: Path, mapping: dict[str, str | None]) -> list[str]:
    """Rename speaker tiers by `mapping` (None = drop the tier); returns the change log."""
    lines = tg.read_bytes().decode("utf-8").splitlines(keepends=True)
    items: list[list[str]] = []
    head: list[str] = []
    for ln in lines:
        if re.match(r"^\s*item \[\d+\]:", ln):
            items.append([ln])
        elif items:
            items[-1].append(ln)
        else:
            head.append(ln)
    log, kept = [], []
    for it in items:
        m = next((NAME.match(x) for x in it if NAME.match(x)), None)
        spk = m.group(2) if m else None
        if spk in mapping and mapping[spk] is None:
            log.append(f"{tg.name}: drop tier {spk}")
            continue
        if spk in mapping:
            it = [NAME.sub(lambda mm: mm.group(1) + mapping[spk] + mm.group(3), x) if NAME.match(x) else x for x in it]
            log.append(f"{tg.name}: {spk}->{mapping[spk]}")
        kept.append(it)
    for i, it in enumerate(kept, 1):
        it[0] = re.sub(r"item \[\d+\]", f"item [{i}]", it[0])
    head = [re.sub(r"^(size = )\d+", rf"\g<1>{len(kept)}", x) for x in head]
    tg.write_bytes("".join(head + [x for it in kept for x in it]).encode("utf-8"))
    return log


def fix_speakers(root: Path) -> None:
    for sess, mapping in SPEAKER_FIX.items():
        a = root / sess / "A"
        for spk, new in mapping.items():  # pass 1: to temporary names (or delete)
            for ext in ("WAV", "TextGrid"):
                f = a / f"{spk}.{ext}"
                if not f.exists():
                    raise SystemExit(f"missing {f}")
                if new is None:
                    f.unlink()
                    print(f"  {sess}: deleted A/{f.name}")
                else:
                    f.rename(a / f"tmp_{new}.{ext}")
        for f in sorted(a.glob("tmp_*")):  # pass 2: final names
            f.rename(a / f.name.removeprefix("tmp_"))
        for tg in sorted((root / sess).rglob("*.TextGrid")):
            # headset TextGrids were renamed in pass 2 already, so their tier still has the old ID
            for line in rewrite_tiers(tg, mapping):
                print(f"  {sess}: {line}")


def read_split(path: Path) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {"train": [], "dev": []}
    cur = None
    for ln in path.read_text(encoding="utf-8").splitlines():
        s = ln.strip().replace("：", ":")
        if s.lower().startswith("train set:"):
            cur = "train"
        elif s.lower().startswith("dev set:"):
            cur = "dev"
        elif s and cur:
            out[cur].append(s)
    return out


def tiers(tg: Path) -> list[str]:
    return [m.group(2) for ln in tg.read_bytes().decode("utf-8").splitlines() if (m := NAME.match(ln))]


def validate(root: Path) -> None:
    split = read_split(root / "split.lst")
    assert (len(split["train"]), len(split["dev"])) == (N_TRAIN, N_DEV), {k: len(v) for k, v in split.items()}
    spk = {}
    for part, sessions in split.items():
        spk[part] = set()
        for sess in sessions:
            d = root / sess
            heads = sorted(p.stem for p in (d / "A").glob("P*.WAV"))
            assert heads and heads == sorted(p.stem for p in (d / "A").glob("P*.TextGrid")), (sess, heads)
            for tg in sorted(d.rglob("*.TextGrid")):
                t = tiers(tg)
                if tg.parent.name == "A":
                    assert t == [tg.stem], (sess, tg.name, t)
                else:
                    assert sorted(t) == heads, (sess, tg.name, sorted(t), heads)
            assert (d / "D1.WAV").exists() and any((d / n).exists() for n in ("R1.wav", "R1.WAV")), sess
            spk[part] |= set(heads)
    assert not spk["train"] & spk["dev"], spk["train"] & spk["dev"]
    print(f"valid: {len(split['train'])} train / {len(split['dev'])} dev sessions, "
          f"{len(spk['train'])} / {len(spk['dev'])} speakers, speaker-disjoint")
    if (len(spk["train"]), len(spk["dev"])) != (SPK_TRAIN, SPK_DEV):
        raise SystemExit(f"speaker counts differ from the organisers' {SPK_TRAIN} / {SPK_DEV}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raw", type=Path, default=Path("/mnt/data/raw/ear1"))
    ap.add_argument("--out", type=Path, default=Path("/mnt/data/corpora/ear1"))
    args = ap.parse_args()
    root = args.out / "TrainDev"
    root.mkdir(parents=True, exist_ok=True)
    if not done(root, "extract"):
        extract(args.raw / "Train&Dev.zip", root)
        mark(root, "extract")
    if not done(root, "timeline"):
        extract(args.raw / "correct.zip", root)
        mark(root, "timeline")
    if not done(root, "speakers"):
        fix_speakers(root)
        mark(root, "speakers")
    if not done(root, "exclude"):
        if (root / EXCLUDE).exists():
            (args.out / "excluded").mkdir(exist_ok=True)
            (root / EXCLUDE).rename(args.out / "excluded" / EXCLUDE)
        mark(root, "exclude")
    if not done(root, "split"):
        split = read_split(args.raw / "split_tr56_dev7.lst")
        split["train"] = [s for s in split["train"] if s != EXCLUDE]
        (root / "split.lst").write_text("Train Set:\n" + "\n".join(split["train"]) + "\n\nDev Set:\n"
                                        + "\n".join(split["dev"]) + "\n", encoding="utf-8")
        shutil.copy2(args.raw / "spkinfo.xlsx", args.out / "spkinfo.xlsx")
        mark(root, "split")
    validate(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
