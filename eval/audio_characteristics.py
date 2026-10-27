#!/usr/bin/env python
"""Acoustic characteristics of diarization inputs, per recording, from audio + reference RTTM (CPU only).

For every recording of the given NeMo manifests (16 kHz mono audio, reference RTTM), with speech /
non-speech / overlap taken from the reference:
    speech_db               mean power (dBFS) of reference speech frames
    noise_db                median frame level (dBFS) of non-speech frames >= 0.3 s away from any
                            reference speech and above -100 dBFS (robust to transients, ignores digital
                            silence; NaN if < 2 s of such frames, noise_s)
    snr_ref_db              speech_db - noise_db
    snr_pct_db              95th - 10th percentile of frame level (reference-free)
    noise_var_db            std of the non-speech frame level (noise stationarity)
    level_var_db            std of 1-s solo-speech levels (moving mic, changing distance)
    spk_level_range_db      max - min over speakers of their mean solo-speech level (distance spread)
    srmr                    speech-to-reverberation modulation energy ratio proxy: modulation energy of
                            23 mel-band envelopes in 4-18 Hz over 18-128 Hz (log-spaced bands as SRMR,
                            Falk et al. 2010), on up to 120 s of solo speech; lower = more reverb/noise
    rolloff99_hz            frequency below which 99% of the speech long-term spectrum lies (bandwidth)
    tilt_db_oct             slope of the speech long-term spectrum, 250-4000 Hz, dB per octave
    hf_ratio_db             speech energy 4-8 kHz relative to 0.3-4 kHz
    noise_lf_ratio_db       non-speech energy below 200 Hz relative to 200-8000 Hz (hum, HVAC, handling)
    zero_pct                frames below -100 dBFS (digital silence / dropouts)
    clip_pct, speech_pct, overlap_pct (of reference speech), n_spk, duration_s
Writes <out>/<manifest>.jsonl (one row per recording) and <out>/summary.md (per-manifest medians and
IQRs; with --target, the z-scored distance of each manifest's median vector to the target manifests).

    python eval/audio_characteristics.py --jobs 8 --out results/20261027-audio-characteristics \
        aishell4_test_far_ch1 alimeeting_Eval_Ali_far_ch1 ...
"""
from __future__ import annotations

import argparse
import json
import math
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
import soundfile as sf

from nemo_dicobw.rttm import load_rttm

SR = 16000
HOP = 160  # 10 ms
WIN = 400  # 25 ms
MOD_EDGES = np.array([4, 6.5, 10.7, 17.6, 28.9, 47.5, 78.1, 128.0])  # SRMR-style modulation bands
FEATURES = ("snr_ref_db", "snr_pct_db", "speech_db", "noise_db", "noise_var_db", "level_var_db",
            "spk_level_range_db", "srmr", "rolloff99_hz", "tilt_db_oct", "hf_ratio_db", "noise_lf_ratio_db",
            "clip_pct", "overlap_pct")


def frame_power(x: np.ndarray) -> np.ndarray:
    n = 1 + max(0, (len(x) - WIN) // HOP)
    idx = np.arange(WIN)[None, :] + HOP * np.arange(n)[:, None]
    return np.mean(x[idx] ** 2, axis=1) + 1e-12


def db(p) -> float:
    return float(10 * np.log10(np.mean(p))) if np.size(p) else math.nan


def activity(turns, n_frames: int) -> tuple[np.ndarray, dict[str, np.ndarray]]:
    per = {}
    for t in turns:
        m = per.setdefault(t.speaker, np.zeros(n_frames, bool))
        m[int(t.start * 100):int(math.ceil(t.end * 100))] = True
    count = np.sum(list(per.values()), axis=0) if per else np.zeros(n_frames, int)
    return count, per


def mel_fb(n_fft: int, n_mels: int = 23, fmin: float = 125.0, fmax: float = 8000.0) -> np.ndarray:
    mel = lambda f: 2595 * np.log10(1 + f / 700)  # noqa: E731
    imel = lambda m: 700 * (10 ** (m / 2595) - 1)  # noqa: E731
    pts = imel(np.linspace(mel(fmin), mel(fmax), n_mels + 2))
    freqs = np.fft.rfftfreq(n_fft, 1 / SR)
    fb = np.zeros((n_mels, len(freqs)))
    for i in range(n_mels):
        lo, c, hi = pts[i:i + 3]
        fb[i] = np.clip(np.minimum((freqs - lo) / (c - lo), (hi - freqs) / (hi - c)), 0, None)
    return fb


def srmr_proxy(chunks: list[np.ndarray]) -> float:
    """Modulation-energy ratio over solo-speech chunks (each >= 1 s)."""
    n_fft, hop = 512, 64  # 32 ms window, 4 ms hop -> envelope at 250 Hz
    fb = mel_fb(n_fft)
    win = np.hanning(n_fft)
    lo = hi = 0.0
    for x in chunks:
        n = 1 + (len(x) - n_fft) // hop
        idx = np.arange(n_fft)[None, :] + hop * np.arange(n)[:, None]
        env = np.sqrt(fb @ (np.abs(np.fft.rfft(x[idx] * win, axis=1)) ** 2).T)  # (bands, frames)
        seg = 250  # 1-s modulation windows
        for s in range(0, env.shape[1] - seg + 1, seg // 2):
            e = env[:, s:s + seg]
            spec = np.abs(np.fft.rfft((e - e.mean(1, keepdims=True)) * np.hanning(seg), axis=1)) ** 2
            f = np.fft.rfftfreq(seg, 1 / 250)
            lo += spec[:, (f >= MOD_EDGES[0]) & (f < MOD_EDGES[4])].sum()
            hi += spec[:, (f >= MOD_EDGES[4]) & (f < MOD_EDGES[-1])].sum()
    return float(lo / hi) if hi > 0 else math.nan


def ltas(x: np.ndarray, frames: np.ndarray, n_fft: int = 512, max_frames: int = 30000) -> np.ndarray:
    """Mean power spectrum over the given 10-ms frame indices (subsampled)."""
    if len(frames) > max_frames:
        frames = frames[np.linspace(0, len(frames) - 1, max_frames).astype(int)]
    starts = np.clip(frames * HOP, 0, len(x) - n_fft)
    seg = x[starts[:, None] + np.arange(n_fft)[None, :]] * np.hanning(n_fft)
    return np.mean(np.abs(np.fft.rfft(seg, axis=1)) ** 2, axis=0) + 1e-20


def analyse(row: dict) -> dict:
    x, sr = sf.read(row["audio_filepath"], dtype="float32")
    if x.ndim > 1:
        x = x.mean(axis=1)
    assert sr == SR, (row["audio_filepath"], sr)
    p = frame_power(x)
    n = len(p)
    turns = load_rttm([Path(row["rttm_filepath"])]).get(row["session"], [])
    count, per = activity(turns, n)
    speech = count > 0
    lv = 10 * np.log10(p)
    # >= 0.3 s from speech, excluding digital silence (exact zeros, dropouts), which is not background noise
    far = (np.convolve(speech.astype(float), np.ones(61), "same") == 0) & (lv > -100)
    solo = count == 1
    out = {"uniq_id": row["uniq_id"], "session": row["session"], "channel": row.get("channel"),
           "duration_s": round(len(x) / SR, 2), "n_spk": len(per),
           "speech_pct": 100 * speech.mean(), "overlap_pct": 100 * (count > 1).sum() / max(1, speech.sum()),
           "clip_pct": 100 * float(np.mean(np.abs(x) >= 0.999)), "zero_pct": 100 * float(np.mean(lv <= -100)),
           "speech_db": db(p[speech]), "noise_s": far.sum() / 100,
           "noise_db": float(np.median(lv[far])) if far.sum() >= 200 else math.nan,
           "snr_pct_db": float(np.percentile(lv, 95) - np.percentile(lv, 10)),
           "noise_var_db": float(np.std(lv[far])) if far.sum() >= 200 else math.nan}
    out["snr_ref_db"] = out["speech_db"] - out["noise_db"]
    # 1-s solo-speech levels and per-speaker levels
    sec = [db(p[i:i + 100][solo[i:i + 100]]) for i in range(0, n - 100, 100) if solo[i:i + 100].mean() >= 0.5]
    out["level_var_db"] = float(np.std(sec)) if len(sec) >= 10 else math.nan
    spk_db = [db(p[m & solo]) for m in per.values() if (m & solo).sum() >= 300]
    out["spk_level_range_db"] = float(max(spk_db) - min(spk_db)) if len(spk_db) >= 2 else math.nan
    # solo-speech chunks >= 1 s, up to 120 s, spread over the recording
    edges = np.flatnonzero(np.diff(np.r_[0, solo.astype(int), 0]))
    runs = [(s, e) for s, e in zip(edges[::2], edges[1::2]) if e - s >= 100]
    pick, total = [], 0
    for s, e in [runs[i] for i in np.linspace(0, len(runs) - 1, min(len(runs), 200)).astype(int)] if runs else []:
        if total >= 12000:
            break
        e = min(e, s + 1000)
        pick.append(x[s * HOP:e * HOP])
        total += e - s
    out["srmr"] = srmr_proxy(pick) if total >= 1000 else math.nan
    # long-term spectra
    f = np.fft.rfftfreq(512, 1 / SR)
    if speech.sum() >= 500:
        S = ltas(x, np.flatnonzero(speech))
        c = np.cumsum(S) / S.sum()
        out["rolloff99_hz"] = float(f[np.searchsorted(c, 0.99)])
        band = (f >= 250) & (f <= 4000)
        out["tilt_db_oct"] = float(np.polyfit(np.log2(f[band]), 10 * np.log10(S[band]), 1)[0])
        out["hf_ratio_db"] = float(10 * np.log10(S[(f >= 4000)].sum() / S[(f >= 300) & (f < 4000)].sum()))
    if far.sum() >= 200:
        N = ltas(x, np.flatnonzero(far))
        out["noise_lf_ratio_db"] = float(10 * np.log10(N[f < 200].sum() / N[f >= 200].sum()))
    return {k: (round(v, 3) if isinstance(v, float) else v) for k, v in out.items()}


def summarise(rows: dict[str, list[dict]], targets: list[str]) -> str:
    md = ["# Audio characteristics of diarization inputs", "",
          "Per manifest: median [IQR] over recordings. Generated by eval/audio_characteristics.py.", "",
          "| manifest | n | " + " | ".join(FEATURES) + " |", "|---|---|" + "---|" * len(FEATURES)]
    med = {}
    for name, rs in rows.items():
        cells, med[name] = [], {}
        for k in FEATURES:
            v = np.array([r.get(k, math.nan) for r in rs], float)
            v = v[~np.isnan(v)]
            if len(v):
                q1, m, q3 = np.percentile(v, [25, 50, 75])
                med[name][k] = m
                cells.append(f"{m:.1f} [{q1:.1f}, {q3:.1f}]")
            else:
                med[name][k] = math.nan
                cells.append("–")
        md.append(f"| {name} | {len(rs)} | " + " | ".join(cells) + " |")
    if targets:
        # z-score features over recordings of all manifests, then distance between medians
        allv = {k: np.array([r.get(k, math.nan) for rs in rows.values() for r in rs], float) for k in FEATURES}
        sd = {k: np.nanstd(v) or 1.0 for k, v in allv.items()}
        keys = [k for k in FEATURES if k not in ("overlap_pct",)]
        md += ["", "## Distance to targets", "",
               "RMS over features of the z-scored difference of medians (overlap excluded; NaN features skipped).", "",
               "| manifest | " + " | ".join(targets) + " |", "|---|" + "---|" * len(targets)]
        for name in rows:
            d = []
            for t in targets:
                z = [(med[name][k] - med[t][k]) / sd[k] for k in keys
                     if not (math.isnan(med[name][k]) or math.isnan(med[t][k]))]
                d.append(f"{math.sqrt(np.mean(np.square(z))):.2f}" if z else "–")
            md.append(f"| {name} | " + " | ".join(d) + " |")
    return "\n".join(md) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("manifests", nargs="+", help="manifest names in --manifest-dir (or paths)")
    ap.add_argument("--manifest-dir", type=Path, default=Path("/mnt/data/manifests/nemo"))
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--target", nargs="*", default=[], help="manifests to measure distances to")
    ap.add_argument("--jobs", type=int, default=8)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    rows: dict[str, list[dict]] = {}
    with ProcessPoolExecutor(args.jobs) as ex:
        for m in args.manifests + [t for t in args.target if t not in args.manifests]:
            path = Path(m) if m.endswith(".jsonl") else args.manifest_dir / f"{m}.jsonl"
            name = path.stem
            cache = args.out / f"{name}.jsonl"
            if cache.exists():
                rows[name] = [json.loads(x) for x in cache.read_text().splitlines()]
                print(f"{name}: cached ({len(rows[name])})", flush=True)
                continue
            recs = [json.loads(x) for x in path.read_text().splitlines() if x.strip()]
            rows[name] = list(ex.map(analyse, recs))
            cache.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows[name]))
            print(f"{name}: {len(recs)} recordings", flush=True)
    (args.out / "summary.md").write_text(summarise(rows, [Path(t).stem for t in args.target]))
    print(f"wrote {args.out / 'summary.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
