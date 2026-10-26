"""Render a diarization scoring JSON (written by eval/score_diar.py) as markdown tables.

    python -m nemo_dicobw.diar_report results/<run>.json > results/<run>.md
"""
from __future__ import annotations

import argparse
import json
import sys


def _pct(x: float | None) -> str:
    return "–" if x is None else f"{100 * x:.2f}"


def _sec(x: float | None) -> str:
    return "–" if x is None else f"{x:.3f}"


def to_markdown(res: dict, per_file: bool = True) -> str:
    meta, overall = res["meta"], res["overall"]
    lines = [f"# Diarization scores: {meta.get('name') or meta['hyp']}", ""]
    lines += [f"- {k}: `{v}`" for k, v in meta.items() if k not in ("collars", "boundary_tols")]
    lines.append("")

    lines += ["## DER / JER (overlap scored, %)", "",
              "| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |",
              "|---|---|---|---|---|---|---|---|"]
    for c, o in overall["diar"].items():
        lines.append(f"| {c} | {_pct(o['der'])} | {_pct(o['miss_rate'])} | {_pct(o['fa_rate'])} | "
                     f"{_pct(o['conf_rate'])} | {_pct(o['jer'])} | {_pct(o['spk_count_acc'])} | "
                     f"{o['spk_count_mae']:.2f} |")

    seg = overall["seg"]["confusion"]
    lines += ["", "## Speech / silence confusion (speaker-agnostic, % of UEM time)", "",
              "| ref \\ hyp | speech | silence |", "|---|---|---|"]
    for rc in ("speech", "silence"):
        lines.append(f"| {rc} | " + " | ".join(
            f"{_pct(seg[f'ref_{rc}__hyp_{hc}__frac_uem'])} (IoU {_pct(seg[f'ref_{rc}__hyp_{hc}__iou'])})"
            for hc in ("speech", "silence")) + " |")
    lines += ["", f"Speech P/R/F1: {_pct(seg['speech_precision'])} / {_pct(seg['speech_recall'])} / "
              f"{_pct(seg['speech_f1'])}; miss {_pct(seg['speech_miss_rate'])} of ref speech, "
              f"FA {_pct(seg['speech_fa_rate'])} of ref silence, SAD error {_pct(seg['sad_error'])}."]

    lines += ["", "## Speech boundaries (speaker-agnostic)", "",
              "| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
    for tol, kinds in overall["seg"]["boundaries"].items():
        for kind, b in kinds.items():
            lines.append(f"| {tol} | {kind} | {b['n_ref']} | {b['n_hyp']} | {_pct(b['precision'])} | "
                         f"{_pct(b['recall'])} | {_pct(b['f1'])} | {_sec(b['mae'])} | "
                         f"{_sec(b['median_abs_err'])} | {_sec(b['mean_disp'])} | {_sec(b['median_disp'])} |")
    lines += ["", "Displacement = hyp − ref (positive: hypothesis boundary late)."]

    if per_file:
        collars = list(overall["diar"])
        lines += ["", "## Per file (DER / JER %)", "",
                  "| file | " + " | ".join(f"DER@{c} | JER@{c}" for c in collars) + " | #ref spk | #hyp spk |",
                  "|---|" + "---|" * (2 * len(collars) + 2)]
        for fid, f in res["files"].items():
            d0 = f["diar"][collars[0]]
            lines.append(f"| {fid} | " + " | ".join(
                f"{_pct(f['diar'][c]['der'])} | {_pct(f['diar'][c]['jer'])}" for c in collars)
                + f" | {d0['n_ref_speakers']} | {d0['n_hyp_speakers']} |")
    return "\n".join(lines) + "\n"


def summary_table(results: list[dict], tol: str = "0.25") -> str:
    """One row per scoring JSON: DER@collars (miss/FA/conf at collar 0), JER@0, speaker count,
    speech IoU, and speaker-agnostic boundary F1 / median displacement at tolerance `tol`."""
    collars = list(results[0]["overall"]["diar"]) if results else []
    head = (["condition", "ref", "UEM", "files", "hours"] + [f"DER@{c}" for c in collars]
            + ["Miss", "FA", "Conf", "JER@" + collars[0] if collars else "JER", "spk acc", "spk MAE",
               "speech IoU", "sil IoU", f"bnd F1@{tol}", "onset med disp", "offset med disp"])
    lines = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for r in results:
        m, o = r["meta"], r["overall"]
        d0 = o["diar"][collars[0]]
        conf = o["seg"]["confusion"]
        b = o["seg"]["boundaries"].get(tol, {})
        uem = "no" if str(m.get("uem", "")).startswith("auto") else "yes"
        row = ([m.get("condition", m.get("name")), m.get("ref_type", "?"), uem, str(d0["n_files"]),
                f"{d0['scored_time'] / 3600:.1f}" if uem == "yes" else "–"]
               + [_pct(o["diar"][c]["der"]) for c in collars]
               + [_pct(d0["miss_rate"]), _pct(d0["fa_rate"]), _pct(d0["conf_rate"]), _pct(d0["jer"]),
                  _pct(d0["spk_count_acc"]), f"{d0['spk_count_mae']:.2f}",
                  _pct(conf["ref_speech__hyp_speech__iou"]), _pct(conf["ref_silence__hyp_silence__iou"]),
                  _pct(b.get("all", {}).get("f1")), _sec(b.get("onset", {}).get("median_disp")),
                  _sec(b.get("offset", {}).get("median_disp"))])
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("json")
    ap.add_argument("--no-per-file", action="store_true")
    args = ap.parse_args()
    with open(args.json) as f:
        sys.stdout.write(to_markdown(json.load(f), per_file=not args.no_per_file))


if __name__ == "__main__":
    main()
