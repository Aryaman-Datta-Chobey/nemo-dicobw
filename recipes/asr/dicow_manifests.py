#!/usr/bin/env python
"""Extra Lhotse manifests of the open DiCoW recipe (EXPERIMENTS.md 20261101-dicow-open-train-setup). Dicow env.

  dev      AliMeeting Eval far_ch1 + AISHELL-5 Dev DX01C01, annotated-segment supervisions, into <out>/dicow_dev_{small,full}_cutset{,_30s}.jsonl.gz.
           Parent cuts are the references; windows of at most 30 s (same rule as recipes/data/dicow_real_cuts.py) are what gets decoded,
           because the model has no timestamps for long-form decoding. Small = 4 sessions of each, for evaluation during training.
           Segment masks count pauses as speech, so these numbers rank checkpoints and are not oracle results.
  split    AISHELL-4 train into aishell4_7spk_* and aishell4_lt7spk_* (parent and _30s), so the 7-speaker sessions can get their own weight.
  ctc      AISHELL-3 test speakers absent from train only: 12 utterances each into ctc_dev and ctc_eval cutsets of the CTC head.
  shares   real sampled shares of a Hydra config: weight x cuts x speakers per cut, as upstream's prepare_cuts indexes them.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

import lhotse
import yaml
from lhotse import CutSet, Recording, SupervisionSegment
from lhotse.cut import MonoCut

DATA = Path("/mnt/data")
LHOTSE = DATA / "manifests/lhotse"
OUT = LHOTSE / "dicow_open"
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "data"))


def dev_session(corpus: str, split: str, audio: Path, seglst: Path) -> tuple[MonoCut, list[MonoCut]]:
    from dicow_real_cuts import windows

    rid = f"{corpus}_{split}_{seglst.stem}"
    rec = Recording.from_file(audio, recording_id=rid)
    sups = [{"start": s["start_time"], "end": min(s["end_time"], rec.duration), "speaker": s["speaker"], "text": s["words"]}
            for s in json.loads(seglst.read_text()) if s["start_time"] < rec.duration and s["end_time"] > s["start_time"]]

    def seg(cid: str, i: int, s: dict, t0: float) -> SupervisionSegment:
        return SupervisionSegment(id=f"{cid}-{i}", recording_id=rid, start=round(s["start"] - t0, 3), duration=round(s["end"] - s["start"], 3),
                                  channel=0, text=s["text"], speaker=s["speaker"], language="zh")

    parent = MonoCut(id=rid, start=0, duration=rec.duration, channel=0, recording=rec, supervisions=[seg(rid, i, s, 0.0) for i, s in enumerate(sups)])
    wins = []
    for t0, dur, keep in windows(sups, rec.duration, 30.0, Counter()):
        cid = f"{rid}-w{int(t0 * 100):06d}"
        wins.append(MonoCut(id=cid, start=round(t0, 3), duration=round(dur, 3), channel=0, recording=rec, supervisions=[seg(cid, i, s, t0) for i, s in enumerate(keep)]))
    return parent, wins


def dev(args) -> None:
    ali = sorted((DATA / "refs/alimeeting/Eval_Ali/seglst").glob("*.json"))
    a5 = sorted((DATA / "refs/aishell5/Dev/seglst").glob("*.json"))
    jobs = [("alimeeting", "Eval", DATA / f"audio16k/alimeeting/Eval_Ali/{f.stem}/far_ch1.flac", f) for f in ali]
    jobs += [("aishell5", "Dev", DATA / f"audio16k/aishell5/Dev/{f.stem}/DX01C01.flac", f) for f in a5]
    built = {j[3]: dev_session(*j) for j in jobs}
    small = set(ali[::2][:4]) | set(a5[::len(a5) // 4][:4])
    for name, keys in (("full", list(built)), ("small", [k for k in built if k in small])):
        parents = [built[k][0] for k in keys]
        wins = [w for k in keys for w in built[k][1]]
        CutSet.from_cuts(parents).to_file(OUT / f"dicow_dev_{name}_cutset.jsonl.gz")
        CutSet.from_cuts(wins).to_file(OUT / f"dicow_dev_{name}_cutset_30s.jsonl.gz")
        print(name, len(parents), "sessions", round(sum(c.duration for c in parents) / 3600, 2), "h", len(wins), "windows",
              sum(len({s.speaker for s in w.supervisions}) for w in wins), "window x speaker")


def split(args) -> None:
    src = LHOTSE / "aishell4/aishell4_cutset_train"
    spk = {}
    for c in lhotse.load_manifest(f"{src}.jsonl.gz"):
        spk[c.recording_id] = len({s.speaker for s in c.supervisions})
    for suffix in ("", "_30s"):
        cuts = lhotse.load_manifest(f"{src}{suffix}.jsonl.gz")
        for name, keep in (("7spk", lambda r: spk[r] >= 7), ("lt7spk", lambda r: spk[r] < 7)):
            sub = cuts.filter(lambda c: keep(c.recording_id)).to_eager()
            sub.to_file(LHOTSE / f"aishell4/aishell4_{name}_cutset_train{suffix}.jsonl.gz")
            print(name, suffix, len(sub), "cuts", len({c.recording_id.split('__')[0] for c in sub}), "sessions")


def ctc(args) -> None:
    train = {s.speaker for c in lhotse.load_manifest(LHOTSE / "aishell3/aishell3_cutset_train.jsonl.gz") for s in c.supervisions}
    by = defaultdict(list)
    for c in lhotse.load_manifest(LHOTSE / "aishell3/aishell3_cutset_test.jsonl.gz"):
        spk = c.supervisions[0].speaker
        if spk not in train:
            by[spk].append(c)
    rng = random.Random(2027)
    dev_cuts, eval_cuts = [], []
    for spk in sorted(by):
        rng.shuffle(by[spk])
        dev_cuts += by[spk][:12]
        eval_cuts += by[spk][12:24]
    CutSet.from_cuts(dev_cuts).to_file(OUT / "ctc_dev_aishell3_cutset.jsonl.gz")
    CutSet.from_cuts(eval_cuts).to_file(OUT / "ctc_eval_aishell3_cutset.jsonl.gz")
    print(len(by), "unseen speakers;", len(dev_cuts), "dev;", len(eval_cuts), "eval")


def shares(args) -> None:
    cfg = yaml.safe_load(args.config.read_text())["data"]
    rows = []
    for path, w in zip(cfg["train_cutsets"], cfg["dataset_weights"]):
        path = path.replace("${oc.env:MANIFEST_DIR}", os.environ.get("MANIFEST_DIR", str(LHOTSE)))
        n = sec = 0
        for c in lhotse.load_manifest_lazy(path):
            k = len({s.speaker for s in c.supervisions})
            n += k
            sec += k * c.duration
        rows.append({"cutset": Path(path).name.removesuffix(".jsonl.gz"), "weight": w, "cut_x_speaker": n, "index": w * n, "mean_s": round(sec / n, 2), "hours": w * sec / 3600})
    total = sum(r["index"] for r in rows)
    synth = sum(r["index"] for r in rows if r["cutset"].startswith("sim"))
    for r in rows:
        r["share"] = round(r["index"] / total, 4)
        r["hours"] = round(r["hours"], 1)
    out = {"config": str(args.config), "rows": rows, "real_share": round(1 - synth / total, 4), "synthetic_share": round(synth / total, 4), "index_length": total}
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(out, indent=1) + "\n")
    lines = [f"Sampled shares of `{args.config}` (weight x cuts x speakers per cut). Real {out['real_share']:.1%}, synthetic {out['synthetic_share']:.1%}.", "",
             "| Cutset | Weight | Cut x speaker | Share | Mean window (s) |", "|---|---|---|---|---|"]
    lines += [f"| {r['cutset']} | {r['weight']} | {r['cut_x_speaker']:,} | {r['share']:.1%} | {r['mean_s']} |" for r in rows]
    args.out_json.with_suffix(".md").write_text("\n".join(lines) + "\n")
    print(json.dumps(out, indent=1))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", choices=["dev", "split", "ctc", "shares"])
    ap.add_argument("--config", type=Path)
    ap.add_argument("--out-json", type=Path, default=Path("results/20261101-dicow-open-train-setup/shares.json"))
    args = ap.parse_args()
    {"dev": dev, "split": split, "ctc": ctc, "shares": shares}[args.stage](args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
