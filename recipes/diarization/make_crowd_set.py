#!/usr/bin/env python
"""EAR-1 crowd set: speaker-disjoint 7-8-speaker recordings for measuring the ESD-ON under-count regime.

Built only from sessions whose speakers never appear in Nemotron fine-tuning data (EAR-1 dev and the
held-out EAR-1 train sessions of prepare_ft_ear1.py), so voices are unseen; EAR-1 train has no other
speaker-disjoint crowded sessions (all of its >= 6-speaker sessions share one core speaker group).

  real    sessions with >= --min-real speakers (dev 20260924-2, 20260924-5; held-out 20260924-8), every
          view (D1, R1, H*) -> <manifests>/ear1_crowd_real.jsonl, original audio and references
  synth8  every speaker-disjoint pair of 4-speaker sessions, concatenated per view (--synth-views):
          audio A + audio B, reference turns of each clipped to its own UEM and B shifted by A's audio
          length -> 8 speakers, real EAR-1 rooms and turn-taking, but the second group arrives at the
          concatenation point (no 8-way interleaving) and the room changes there.
          <audio16k>/ear1/crowd_synth8/<A>+<B>/<view>.flac, <refs>/ear1/crowd_synth8/{rttm,uem}/,
          <manifests>/ear1_crowd_synth8.jsonl; session = uniq_id, "group" = the pair (bootstrap unit).
Existing synthetic audio is not rewritten.

    python recipes/diarization/make_crowd_set.py
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np
import soundfile as sf

from nemo_dicobw.rttm import Turn, intersect_intervals, load_rttm, load_uem, write_rttm, write_uem

DATA = Path("/mnt/data")


def rows(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.read_text().splitlines() if x.strip()]


def speakers(row: dict) -> set[str]:
    return {t.speaker for t in load_rttm([row["rttm_filepath"]])[row["session"]]}


def clipped(row: dict) -> tuple[list[Turn], list[tuple[float, float]]]:
    uem = load_uem([row["uem_filepath"]])[row["session"]]
    turns = []
    for t in load_rttm([row["rttm_filepath"]])[row["session"]]:
        turns += [Turn(t.speaker, s, e) for s, e in intersect_intervals([(t.start, t.end)], uem)]
    return turns, uem


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--manifests", type=Path, default=DATA / "manifests/nemo")
    ap.add_argument("--heldout", type=Path, default=DATA / "manifests/nemotron_ft/ear1_v1/config.json",
                    help="prepare_ft_ear1.py config with the held-out session list")
    ap.add_argument("--min-real", type=int, default=7)
    ap.add_argument("--synth-views", nargs="+", default=["D1", "R1", "H1"])
    args = ap.parse_args()

    held = set(json.loads(args.heldout.read_text())["heldout"])
    pool = rows(args.manifests / "ear1_dev_all.jsonl") + [r for r in rows(args.manifests / "ear1_train_all.jsonl")
                                                          if r["session"] in held]
    spk = {r["session"]: speakers(r) for r in pool}

    real = [{**r, "group": r["session"]} for r in pool if len(spk[r["session"]]) >= args.min_real]
    (args.manifests / "ear1_crowd_real.jsonl").write_text("".join(json.dumps(r) + "\n" for r in real))
    print(f"real: {len(real)} recordings, sessions {sorted({r['session'] for r in real})}")

    four = sorted(s for s, v in spk.items() if len(v) == 4)
    pairs = [(a, b) for a, b in itertools.combinations(four, 2) if not spk[a] & spk[b]]
    by_view = {(r["session"], r["channel"]): r for r in pool}
    audio_root, ref_root = DATA / "audio16k/ear1/crowd_synth8", DATA / "refs/ear1/crowd_synth8"
    (ref_root / "rttm").mkdir(parents=True, exist_ok=True)
    (ref_root / "uem").mkdir(parents=True, exist_ok=True)
    synth = []
    for a, b in pairs:
        for view in args.synth_views:
            ra, rb = by_view.get((a, view)), by_view.get((b, view))
            if ra is None or rb is None:
                continue
            uid = f"{a}+{b}__{view}"
            wav = audio_root / f"{a}+{b}" / f"{view}.flac"
            info_a = sf.info(ra["audio_filepath"])
            off = info_a.frames / info_a.samplerate
            if not wav.exists():
                xa, sr = sf.read(ra["audio_filepath"], dtype="float32")
                xb, sr_b = sf.read(rb["audio_filepath"], dtype="float32")
                assert sr == sr_b == 16000 and xa.ndim == xb.ndim == 1
                wav.parent.mkdir(parents=True, exist_ok=True)
                sf.write(wav, np.concatenate([xa, xb]), sr)
            ta, ua = clipped(ra)
            tb, ub = clipped(rb)
            turns = ta + [Turn(t.speaker, t.start + off, t.end + off) for t in tb]
            uem = ua + [(s + off, e + off) for s, e in ub]
            write_rttm({uid: turns}, ref_root / "rttm" / f"{uid}.rttm")
            write_uem({uid: uem}, ref_root / "uem" / f"{uid}.uem")
            info = sf.info(wav)
            synth.append({"audio_filepath": str(wav), "uniq_id": uid, "offset": 0,
                          "duration": info.frames / info.samplerate,
                          "rttm_filepath": str(ref_root / "rttm" / f"{uid}.rttm"),
                          "uem_filepath": str(ref_root / "uem" / f"{uid}.uem"), "session": uid, "channel": view,
                          "ref_type": "segments", "group": f"{a}+{b}", "sources": [a, b], "concat_at": off})
    (args.manifests / "ear1_crowd_synth8.jsonl").write_text("".join(json.dumps(r) + "\n" for r in synth))
    print(f"synth8: {len(pairs)} speaker-disjoint pairs {pairs}, {len(synth)} recordings, "
          f"{sum(r['duration'] for r in synth) / 3600:.1f} h")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
