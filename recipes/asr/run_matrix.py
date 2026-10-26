#!/usr/bin/env python
"""Enumerate and run the Whisper-family zero-shot condition matrix on the Mandarin sets.

Condition name: <dataset>__<checkpoint>__<mode>__ts-<on|off>__<diar>__<lang>, run by
recipes/asr/asr_infer.py into <out>/<condition>/ (skipped when its config.json exists).

Matrix (see EXPERIMENTS.md, "Whisper-family zero-shot on Mandarin sets"):
    dicow-large                       per_speaker, ts on, zh, diar {nemotron, oracle}
    whisper-large-v3 / -turbo         ts on, zh: whole; per_speaker x diar {nemotron, oracle}
    belle-zh / -zh-punct / -turbo-zh, buzzasr
                                      ts {on, off}, zh: whole; per_speaker x diar {nemotron, oracle}
    auto-LID (dev set only)           every checkpoint, language auto: whole ts on (DiCoW: per_speaker,
                                      nemotron)
Whole-mode runs also write late fusion with Nemotron and with oracle diarization.

Example:
    python recipes/asr/run_matrix.py --list                      # print the conditions
    python recipes/asr/run_matrix.py --datasets alimeeting_Eval_Ali_far_ch1 --run
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
MODELS = Path("/mnt/data/models")
MANIFESTS = Path("/mnt/data/manifests/nemo")
NEMOTRON = "nemotron:20261026-nemotron-zeroshot"
DATASETS = ["alimeeting_Eval_Ali_far_ch1", "alimeeting_Test_Ali_far_ch1", "aishell4_test_far_ch1",
            "aishell5_Eval1_DX01C01", "aishell5_Eval2_DX01C01"]
DEV = "alimeeting_Eval_Ali_far_ch1"
CKPT = {
    "dicow-large": "BUT-FIT__DiCoW_v3_3_large",
    "whisper-large-v3": "openai__whisper-large-v3",
    "whisper-large-v3-turbo": "openai__whisper-large-v3-turbo",
    "belle-zh": "BELLE-2__Belle-whisper-large-v3-zh",
    "belle-zh-punct": "BELLE-2__Belle-whisper-large-v3-zh-punct",
    "belle-turbo-zh": "BELLE-2__Belle-whisper-large-v3-turbo-zh",
    "buzzasr": "BuzzASR__mandarin",
}
BOTH_TS = ("belle-zh", "belle-zh-punct", "belle-turbo-zh", "buzzasr")


def conditions(datasets: list[str]) -> list[dict]:
    out = []
    for ds in datasets:
        out += [dict(ds=ds, ck="dicow-large", mode="per_speaker", ts="on", diar=d, lang="zh") for d in ("nemotron", "oracle")]
        for ck in ("whisper-large-v3", "whisper-large-v3-turbo", *BOTH_TS):
            for ts in (("on", "off") if ck in BOTH_TS else ("on",)):
                out.append(dict(ds=ds, ck=ck, mode="whole", ts=ts, diar="nemotron", lang="zh"))
                out += [dict(ds=ds, ck=ck, mode="per_speaker", ts=ts, diar=d, lang="zh") for d in ("nemotron", "oracle")]
        if ds == DEV:
            for ck in CKPT:
                mode = "per_speaker" if ck == "dicow-large" else "whole"
                out.append(dict(ds=ds, ck=ck, mode=mode, ts="on", diar="nemotron", lang="auto"))
    for c in out:
        c["name"] = f"{c['ds']}__{c['ck']}__{c['mode']}__ts-{c['ts']}__{c['diar']}__{c['lang']}"
    return out


def command(c: dict, out: Path) -> list[str]:
    cmd = [sys.executable, str(REPO / "recipes" / "asr" / "asr_infer.py"), "--model", str(MODELS / CKPT[c["ck"]]),
           "--manifest", str(MANIFESTS / f"{c['ds']}.jsonl"), "--diar", NEMOTRON if c["diar"] == "nemotron" else "oracle",
           "--fusion-nemotron", NEMOTRON, "--mode", c["mode"], "--timestamps", c["ts"], "--language", c["lang"],
           "--out", str(out), "--condition", c["name"]]
    return cmd + (["--dicow"] if c["ck"] == "dicow-large" else [])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--datasets", nargs="*", default=DATASETS)
    ap.add_argument("--checkpoints", nargs="*", default=list(CKPT))
    ap.add_argument("--out", type=Path, default=Path("/mnt/data/exp/asr/20261027-whisper-zeroshot"))
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--run", action="store_true")
    args = ap.parse_args()
    conds = [c for c in conditions(args.datasets) if c["ck"] in args.checkpoints]
    if args.list or not args.run:
        print("\n".join(c["name"] for c in conds))
        print(f"{len(conds)} conditions", file=sys.stderr)
    if args.run:
        for i, c in enumerate(conds, 1):
            if (args.out / c["name"] / "config.json").exists():
                continue
            print(f"=== [{i}/{len(conds)}] {c['name']}", flush=True)
            if subprocess.run(command(c, args.out)).returncode:
                print(f"FAILED {c['name']}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
