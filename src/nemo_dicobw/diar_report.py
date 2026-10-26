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


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("json")
    ap.add_argument("--no-per-file", action="store_true")
    args = ap.parse_args()
    with open(args.json) as f:
        sys.stdout.write(to_markdown(json.load(f), per_file=not args.no_per_file))


if __name__ == "__main__":
    main()
