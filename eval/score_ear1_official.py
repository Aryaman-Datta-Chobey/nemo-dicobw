#!/usr/bin/env python
"""Score our EAR-1 dev diarization with the organisers' scorer (third_party/ear1-baselines/diarization).

Stages <run>/rttm/ear1_dev_<track>/<session>__<track>.rttm into the layout ear1_baseline.py expects,
<out>/infer/dev/<track>/<session>.rttm with the RTTM file id rewritten to the session id, links the
reference RTTMs its `prepare` stage wrote (--prepared, e.g. the DiariZen baseline run's output dir), and
runs its `score` stage unchanged (pyannote.metrics DER, collar 0, overlap scored, track-specific
full-recording UEM). Run in the `diarizen` env, which has pyannote.metrics.

    python eval/score_ear1_official.py --run-dir $DATA/exp/nemotron/20261026-nemotron-zeroshot \
        --prepared $DATA/exp/diarizen/20261027-ear1-baseline
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
BASELINE = REPO / "third_party" / "ear1-baselines" / "diarization" / "ear1_baseline.py"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run-dir", type=Path, required=True)
    ap.add_argument("--prepared", type=Path, required=True, help="output dir of ear1_baseline.py prepare")
    ap.add_argument("--data", type=Path, default=Path("/mnt/data/corpora/ear1/TrainDev"))
    ap.add_argument("--out", type=Path, help="default: <run-dir>/ear1_official")
    ap.add_argument("--tracks", nargs="+", default=["D1", "R1"])
    ap.add_argument("--collar", default="0.0")
    args = ap.parse_args()
    out = args.out or args.run_dir / "ear1_official"
    (out / "prepare").mkdir(parents=True, exist_ok=True)
    link = out / "prepare" / "dev"
    if not link.exists():
        link.symlink_to((args.prepared / "prepare" / "dev").resolve())
    for track in args.tracks:
        src = args.run_dir / "rttm" / f"ear1_dev_{track}"
        dst = out / "infer" / "dev" / track
        dst.mkdir(parents=True, exist_ok=True)
        for f in sorted(src.glob(f"*__{track}.rttm")):
            sid = f.name.removesuffix(f"__{track}.rttm")
            lines = [ln.split() for ln in f.read_text().splitlines() if ln.startswith("SPEAKER")]
            (dst / f"{sid}.rttm").write_text("".join(" ".join([p[0], sid, *p[2:]]) + "\n" for p in lines))
    return subprocess.run([sys.executable, "-u", str(BASELINE), "score", "--data", str(args.data),
                           "--split", str(args.data / "split.lst"), "--out", str(out),
                           "--tracks", *args.tracks, "--collar", args.collar]).returncode


if __name__ == "__main__":
    raise SystemExit(main())
