#!/usr/bin/env python
"""Write NeMo diarization manifests for the evaluation conditions.

One JSONL per condition at <out>/<condition>.jsonl, one line per recording:
    {"audio_filepath", "uniq_id": "<session>__<channel>", "offset": 0, "duration",
     "rttm_filepath", "uem_filepath", "session", "channel", "ref_type"}
The RTTM is the preferred reference for the split (fa > words > segments, unless the condition
pins one); other reference
types live next to it under refs/<corpus>/<split>/rttm/<type>/.

Conditions select one channel (or a set of channels) per session from audio16k; see CONDITIONS.

Example:
    python recipes/diarization/make_eval_manifests.py            # all conditions with audio
    python recipes/diarization/make_eval_manifests.py alimeeting_Test_Ali_far_ch1
"""
from __future__ import annotations

import argparse
import csv
import fnmatch
import json
import sys
from dataclasses import dataclass
from pathlib import Path

import soundfile as sf

DATA = Path("/mnt/data")
REF_PREFERENCE = ("fa", "words", "segments")


@dataclass(frozen=True)
class Condition:
    corpus: str
    split: str
    channels: str  # fnmatch pattern over channel names, or "@<file>" for an explicit (session, channel) list
    note: str = ""
    ref_type: str | None = None  # default: first available of REF_PREFERENCE


CONDITIONS: dict[str, Condition] = {
    "aishell4_test_far_ch1": Condition("aishell4", "test", "far_ch1", "array channel 1"),
    **{f"aishell5_{s}_DX01C01": Condition("aishell5", s, "DX01C01", "far-field door mic 1") for s in ("Dev", "Eval1", "Eval2")},
    **{f"alimeeting_{s}_far_ch1": Condition("alimeeting", s, "far_ch1", "array channel 1 (assumed for the Nemotron card's Test-far)")
       for s in ("Eval_Ali", "Test_Ali")},
    "notsofar_eval_sc160": Condition("notsofar", "eval", "@eval_sc_160.tsv", "CHiME-8 / Nemotron-card eval-SC set"),
    "notsofar_eval_sc_all": Condition("notsofar", "eval", "sc_*", "every single-channel device of all 129 meetings "
                                      "(fa covers only the 80 eval-SC meetings)", ref_type="segments"),
    **{f"chime6_{s}_U06_CH1": Condition("chime6", s, "U06.CH1", "reference array U06, channel 1") for s in ("dev", "eval")},
    **{f"egocom_{s}_all": Condition("egocom", s, "person_*", "every wearer (moving egocentric mic)") for s in ("test", "val")},
    "indic_diarbench_far_field": Condition("indic_diarbench", "far_field", "mix"),
    # training-only corpora for the speaker-count run (manifests for window profiles and selection)
    "ami_train_Array1-01": Condition("ami", "train", "Array1-01", "AMI single distant mic (array 1, mic 1)"),
    "icsi_train_mix": Condition("icsi", "train", "mix", "ICSI headset mix (no distant mics available)"),
    # EAR-1 ESD-ON tracks (D1 = Fixed-Array, R1 = Moving-Array) and the auxiliary near mics
    **{f"ear1_{s}_{ch}": Condition("ear1", s, ch, note) for s in ("train", "dev")
       for ch, note in (("D1", "Fixed-Array track input"), ("R1", "Moving-Array track input"))},
    **{f"ear1_{s}_H_all": Condition("ear1", s, "H[1-3]", "mics in front of participants (training-only)")
       for s in ("train", "dev")},
    **{f"ear1_{s}_all": Condition("ear1", s, "[DRH][0-9]", "D1, R1 and H* of each session (channel consistency)")
       for s in ("train", "dev")},
    # every channel of multi-microphone sessions (channel-consistency diagnostics)
    "aishell4_test_far_all": Condition("aishell4", "test", "far_ch*", "all 8 array channels"),
    **{f"aishell5_{s}_DX_all": Condition("aishell5", s, "DX0[1-4]C01", "all 4 far-field door mics") for s in ("Dev", "Eval1", "Eval2")},
    **{f"alimeeting_{s}_far_all": Condition("alimeeting", s, "far_ch*", "all 8 array channels") for s in ("Eval_Ali", "Test_Ali")},
    **{f"chime6_{s}_U_all": Condition("chime6", s, "U0[1-6].CH[1-4]", "all Kinect array channels") for s in ("dev", "eval")},
}


def recordings(c: Condition, audio: Path, refs: Path) -> list[tuple[str, str, Path]]:
    split_dir = audio / c.corpus / c.split
    if c.channels.startswith("@"):
        with open(refs / c.corpus / c.split / c.channels[1:]) as f:
            pairs = [(r["meeting"], r["channel"]) for r in csv.DictReader(f, delimiter="\t")]
        return [(s, ch, split_dir / s / f"{ch}.flac") for s, ch in pairs]
    out = []
    for sess in sorted(p for p in split_dir.iterdir() if p.is_dir()):
        for f in sorted(sess.glob("*.flac")):
            if fnmatch.fnmatch(f.stem, c.channels):
                out.append((sess.name, f.stem, f))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("conditions", nargs="*", help=f"default: all of {sorted(CONDITIONS)}")
    ap.add_argument("--data", type=Path, default=DATA)
    args = ap.parse_args()
    audio, refs, out = args.data / "audio16k", args.data / "refs", args.data / "manifests" / "nemo"
    out.mkdir(parents=True, exist_ok=True)

    for name in args.conditions or sorted(CONDITIONS):
        c = CONDITIONS[name]
        ref_dir = refs / c.corpus / c.split
        if not (audio / c.corpus / c.split).is_dir() or not (ref_dir / "uem").is_dir():
            print(f"skip {name}: audio or references not built yet")
            continue
        ref_type = c.ref_type or next(t for t in REF_PREFERENCE if (ref_dir / "rttm" / t).is_dir())
        rows, missing = [], []
        for sess, ch, path in recordings(c, audio, refs):
            rttm = ref_dir / "rttm" / ref_type / f"{sess}.rttm"
            uem = ref_dir / "uem" / f"{sess}__{ch}.uem"  # channel-specific region, where channels differ in length
            if not uem.exists():
                uem = ref_dir / "uem" / f"{sess}.uem"
            if not path.exists() or not rttm.exists() or not uem.exists():
                missing.append(f"{sess}/{ch}")
                continue
            rows.append({"audio_filepath": str(path), "uniq_id": f"{sess}__{ch}", "offset": 0,
                         "duration": round(sf.info(str(path)).duration, 3), "rttm_filepath": str(rttm),
                         "uem_filepath": str(uem), "session": sess, "channel": ch, "ref_type": ref_type})
        if missing:
            print(f"ERROR {name}: {len(missing)} recordings lack audio or references, e.g. {missing[:3]}", file=sys.stderr)
            return 1
        with open(out / f"{name}.jsonl", "w") as f:
            f.writelines(json.dumps(r) + "\n" for r in rows)
        hours = sum(r["duration"] for r in rows) / 3600
        print(f"{name}: {len(rows)} recordings, {hours:.1f} h, ref={ref_type} -> {out / name}.jsonl")
    return 0


if __name__ == "__main__":
    sys.exit(main())
