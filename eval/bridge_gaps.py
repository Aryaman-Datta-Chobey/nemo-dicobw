#!/usr/bin/env python
"""Same-speaker gap bridging as an ESD-ON post-process, before the oracle-VAD fill.

The EAR-1 organiser references are utterance segments: pauses inside an utterance count as speech, and
a pause of one speaker under another speaker's speech counts as overlap. A diarizer with word-tight
output (base Nemotron, or one trained on forced-alignment labels) misses those frames. This tests
whether joining a hypothesis speaker's turns across short gaps recovers the segment convention after
inference, so the model itself can stay word-tight (and inside the AliMeeting/NOTSOFAR gate).

Per run, mode and gap g, every hypothesis RTTM is rewritten with each speaker's turns joined across
gaps < g:
    all   every gap < g
    vad   only gaps lying entirely inside the oracle VAD (union of the reference turns, the organisers'
          oracle-VAD definition for EAR-1 train/dev)
then eval/vad_postproc.py scores base / mask / fill_nearest / fill_nearest_vad against the segment refs.
Bridged RTTMs: <exp>/<run>/<mode>_g<g>/rttm/<condition>/. Writes <out>/bridge.{json,md}.

    python eval/bridge_gaps.py --runs base=$EXP/selection/base ft=$EXP/selection/ft \
        --ft-manifests $DATA/manifests/nemotron_ft/ear1_v1 --exp $DATA/exp/nemotron/20261028-ear1-bridge \
        --out results/20261028-ear1-bridge
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from nemo_dicobw.rttm import Turn, load_rttm, merge_intervals, subtract_intervals, write_rttm

REPO = Path(__file__).resolve().parents[1]
SETS = {"dev_D1": "ear1_dev_D1", "dev_R1": "ear1_dev_R1", "held_D1": "heldout_D1", "held_R1": "heldout_R1"}


def bridge(turns: list[Turn], gap: float, vad: list[tuple[float, float]] | None) -> list[Turn]:
    out = []
    for spk in sorted({t.speaker for t in turns}):
        iv = merge_intervals((t.start, t.end) for t in turns if t.speaker == spk)
        joined = [iv[0]]
        for s, e in iv[1:]:
            ps, pe = joined[-1]
            if s - pe < gap and (vad is None or not subtract_intervals([(pe, s)], vad)):
                joined[-1] = (ps, e)
            else:
                joined.append((s, e))
        out += [Turn(spk, s, e) for s, e in joined]
    return sorted(out, key=lambda t: t.start)


def write_bridged(src: Path, dst: Path, manifest: Path, gap: float, mode: str) -> None:
    dst.mkdir(parents=True, exist_ok=True)
    for row in (json.loads(x) for x in manifest.read_text().splitlines() if x.strip()):
        uid, p = row["uniq_id"], src / f"{row['uniq_id']}.rttm"
        if not p.exists():
            continue
        vad = merge_intervals((t.start, t.end) for t in load_rttm([Path(row["rttm_filepath"])]).get(row["session"], []))
        turns = load_rttm([p]).get(uid, [])
        write_rttm({uid: bridge(turns, gap, vad if mode == "vad" else None) if turns else []}, dst / f"{uid}.rttm")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", nargs="+", required=True, help="name=<selection dir with rttm/<condition>/>")
    ap.add_argument("--manifests", type=Path, default=Path("/mnt/data/manifests/nemo"))
    ap.add_argument("--ft-manifests", type=Path, required=True)
    ap.add_argument("--exp", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--gaps", type=float, nargs="+", default=[0.25, 0.5, 1.0, 2.0, 4.0])
    ap.add_argument("--modes", nargs="+", default=["all", "vad"])
    ap.add_argument("--jobs", type=int, default=10)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    man = {k: (args.manifests if k.startswith("dev") else args.ft_manifests) / f"{v}.jsonl" for k, v in SETS.items()}

    res: dict = {}
    for spec in args.runs:
        run, src = spec.split("=", 1)
        variants = [("none", 0.0, Path(src) / "rttm")]
        for mode in args.modes:
            for g in args.gaps:
                root = args.exp / run / f"{mode}_g{g:g}" / "rttm"
                for cond in SETS.values():
                    write_bridged(Path(src) / "rttm" / cond, root / cond, man[next(k for k, v in SETS.items() if v == cond)], g, mode)
                variants.append((mode, g, root))
        for mode, g, root in variants:
            name = f"{run}__{mode}_g{g:g}"
            r = {}
            for group in ("dev", "held"):
                keys = [k for k in SETS if k.startswith(group)]
                tmp = args.out / "tmp"
                subprocess.run([sys.executable, str(REPO / "eval/vad_postproc.py"), "--name", f"{name}_{group}", "--rttm-root",
                                str(root), "--conditions", *(SETS[k] for k in keys), "--manifests", str(man[keys[0]].parent),
                                "--out", str(tmp), "--jobs", str(args.jobs)], check=True, stdout=subprocess.DEVNULL)
                d = json.loads((tmp / f"{name}_{group}.json").read_text())["conditions"]
                for k in keys:
                    r[k] = {m: d[SETS[k]][m] for m in ("base", "fill_nearest_vad")}
            res[name] = {"run": run, "mode": mode, "gap": g, **r}
            print(f"{name}: dev fill {50 * (r['dev_D1']['fill_nearest_vad']['der'] + r['dev_R1']['fill_nearest_vad']['der']):.2f} "
                  f"held fill {50 * (r['held_D1']['fill_nearest_vad']['der'] + r['held_R1']['fill_nearest_vad']['der']):.2f}", flush=True)
    (args.out / "bridge.json").write_text(json.dumps(res, indent=1))

    f = lambda x: f"{100 * x['der']:.2f} ({100 * x['miss_rate']:.1f} / {100 * x['fa_rate']:.1f} / {100 * x['conf_rate']:.1f})"
    md = ["# Same-speaker gap bridging before the oracle-VAD fill", "",
          "DER % (miss / FA / conf) after fill_nearest_vad, collar 0, overlap scored, against the EAR-1 segment refs "
          "(official). mode all = every gap < g joined, vad = only gaps inside the oracle VAD; none = unbridged. "
          "dev = EAR-1 dev, held = speaker-disjoint held-out fold of EAR-1 train. Generated by eval/bridge_gaps.py.", "",
          "| run | mode | g s | dev D1 | dev R1 | dev mean | held D1 | held R1 | held mean | dev raw mean |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for r in res.values():
        mean = lambda a, b, m="fill_nearest_vad": 50 * (r[a][m]["der"] + r[b][m]["der"])
        md.append(f"| {r['run']} | {r['mode']} | {r['gap']:g} | {f(r['dev_D1']['fill_nearest_vad'])} | {f(r['dev_R1']['fill_nearest_vad'])} | "
                  f"{mean('dev_D1', 'dev_R1'):.2f} | {f(r['held_D1']['fill_nearest_vad'])} | {f(r['held_R1']['fill_nearest_vad'])} | "
                  f"{mean('held_D1', 'held_R1'):.2f} | {mean('dev_D1', 'dev_R1', 'base'):.2f} |")
    (args.out / "bridge.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
