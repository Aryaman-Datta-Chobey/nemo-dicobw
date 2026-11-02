#!/usr/bin/env python
"""Strip punctuation and tags from training transcripts and re-punctuate them with one ct-transformer.

Belle-whisper-large-v3-zh-punct was trained on text punctuated by this model, so every training target uses its style
(EXPERIMENTS.md 20261031-dicow-open-prep). Held-out splits are not read. Identical texts share one model call.
Output: <out>/<corpus>.jsonl, one line per segment:
    session, speaker, start, end (null for clips), tier_source, raw, clean, punct
Run in the `punc` env, inside tmux:
    python recipes/data/punctuate_transcripts.py --out /mnt/data/work/dicow_open/text --workers 4
"""
from __future__ import annotations

import argparse
import glob
import json
import re
import unicodedata
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

DATA = Path("/mnt/data")
MODEL = DATA / "models/iic__punc_ct-transformer_cn-en-common-vocab471067-large"
TAG = re.compile(r"<[^>]*>|\[[^\]]*\]|\*")
IV = re.compile(r'xmin\s*=\s*([\d.]+)\s*xmax\s*=\s*([\d.]+)\s*text\s*=\s*"((?:[^"]|"")*)"')
_model = None


def clean(text: str) -> str:
    text = TAG.sub(" ", unicodedata.normalize("NFKC", text))
    kept = "".join(c if c == "'" or not unicodedata.category(c).startswith(("P", "S")) else " " for c in text)
    out = re.sub(r"\s+", " ", kept).strip()
    return re.sub(r"(?<=[^\x00-\x7f]) (?=[^\x00-\x7f])", "", out)


def textgrid_rows(path: str, session: str, source: str) -> list[dict]:
    """Own reader: the textgrid package rejects AISHELL-4 files whose last interval ends past the tier's xmax."""
    raw = Path(path).read_bytes()
    text = raw.decode("utf-16") if raw[:2] in (b"\xff\xfe", b"\xfe\xff") else raw.decode("utf-8-sig", errors="replace")
    rows = []
    for tier in re.split(r"item\s*\[\d+\]\s*:", text)[1:]:
        name = re.search(r'name\s*=\s*"([^"]*)"', tier).group(1)
        for a, b, mark in IV.findall(tier):
            if mark.strip() and float(b) > float(a):
                rows.append({"session": session, "speaker": name, "start": float(a), "end": float(b), "tier_source": source, "raw": mark.strip()})
    return rows


def alimeeting() -> list[dict]:
    rows = []
    for part in ("far", "near"):
        for p in sorted(glob.glob(str(DATA / f"corpora/alimeeting/Train_Ali/Train_Ali_{part}/textgrid_dir/*.TextGrid"))):
            s = Path(p).stem
            rows += textgrid_rows(p, s if part == "far" else "_".join(s.split("_")[:2]), part)
    return rows


def aishell4() -> list[dict]:
    rows = []
    for part in ("train_L", "train_M", "train_S"):
        for p in sorted(glob.glob(str(DATA / f"corpora/aishell4/{part}/TextGrid/*.TextGrid"))):
            rows += textgrid_rows(p, Path(p).stem, part)
    return rows


def aishell5() -> list[dict]:
    rows = []
    for d in sorted(glob.glob(str(DATA / "corpora/aishell5/train/*"))):
        far = sorted(glob.glob(f"{d}/DX01C01.TextGrid")) or sorted(glob.glob(f"{d}/DX*.TextGrid"))[:1]
        for p in far + sorted(glob.glob(f"{d}/DA*.TextGrid")):
            rows += textgrid_rows(p, Path(d).name, Path(p).stem)
    return rows


def aishell3() -> list[dict]:
    rows = []
    for line in (DATA / "corpora/aishell3/train/content.txt").read_text(encoding="utf-8").splitlines():
        utt, _, rest = line.partition("\t")
        utt = utt.removesuffix(".wav")
        rows.append({"session": utt, "speaker": utt[:7], "start": None, "end": None, "tier_source": "aishell3", "raw": "".join(rest.split()[0::2])})
    return rows


def ascend() -> list[dict]:
    import pyarrow.parquet as pq

    rows = []
    for f in sorted(glob.glob(str(DATA / "raw/ascend/hf/main/train-*.parquet"))):
        for x in pq.read_table(f, columns=["id", "transcription", "original_speaker_id", "session_id"]).to_pylist():
            rows.append({"session": str(x["session_id"]), "speaker": f"ascend_{x['original_speaker_id']}", "start": None, "end": None,
                         "tier_source": str(x["id"]), "raw": x["transcription"]})
    return rows


CORPORA = {"alimeeting": alimeeting, "aishell4": aishell4, "aishell5": aishell5, "aishell3": aishell3, "ascend": ascend}


def punct_batch(texts: list[str]) -> list[str]:
    global _model
    if _model is None:
        from funasr import AutoModel

        _model = AutoModel(model=str(MODEL), disable_update=True, device="cpu", disable_pbar=True, log_level="ERROR", ncpu=1)
    return [_model.generate(input=t, disable_pbar=True)[0]["text"] for t in texts]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--corpora", nargs="+", default=list(CORPORA))
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--limit", type=int, help="first N segments per corpus (smoke test)")
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    cache_path = args.out / "punct_cache.jsonl"
    cache = {}
    if cache_path.exists():
        cache = {x["clean"]: x["punct"] for x in map(json.loads, cache_path.read_text(encoding="utf-8").splitlines())}
    with ProcessPoolExecutor(args.workers) as ex:
        for name in args.corpora:
            rows = CORPORA[name]()[: args.limit]
            for r in rows:
                r["clean"] = clean(r["raw"])
            rows = [r for r in rows if r["clean"]]
            todo = sorted({r["clean"] for r in rows} - set(cache))
            chunks = [todo[i:i + 500] for i in range(0, len(todo), 500)]
            with open(cache_path, "a", encoding="utf-8") as f:
                for i, (chunk, res) in enumerate(zip(chunks, ex.map(punct_batch, chunks))):
                    for c, p in zip(chunk, res):
                        cache[c] = p
                        f.write(json.dumps({"clean": c, "punct": p}, ensure_ascii=False) + "\n")
                    f.flush()
                    if i % 20 == 0:
                        print(f"{name}: {min((i + 1) * 500, len(todo))}/{len(todo)} new texts", flush=True)
            with open(args.out / f"{name}.jsonl", "w", encoding="utf-8") as f:
                for r in rows:
                    r["punct"] = cache[r["clean"]]
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
            sp = {r["speaker"] for r in rows}
            print(f"{name}: {len(rows)} segments, {len(sp)} speakers, {len(todo)} new texts", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
