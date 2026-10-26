# nemo-dicobw
repository for finetuning nemotron-3-diarization on meeting room, multi-party conversational datasets , then using it as the diarizer in the Diarization conditioning fine-tuning of a belle-whisper checkpoint into a DiCoW style model for mandarin diarized transcription

## Pinned submodules

| Submodule | Commit |
|---|---|
| `third_party/TS-ASR-Whisper` (BUTSpeechFIT/TS-ASR-Whisper) | `4f100c039dd14e4a329afb9e5159eba70bd634aa` |
| `third_party/DiCoW` (BUTSpeechFIT/DiCoW) | `801e2130d00142a7da5845754f87b97550053a75` |
| `third_party/dscore` (nryant/dscore, scoring oracle for tests) | `e02f949ac6592279300a2c33d03daf9e0c12fd27` |

## Diarization scoring

`eval/score_diar.py` scores hypothesis RTTMs against reference RTTMs (+ UEM) and writes a
results JSON plus a markdown table generated from it (`python -m nemo_dicobw.diar_report <json>`
regenerates the table).

- **DER** (miss / false alarm / confusion, overlap scored) and **JER** at each `--collars`
  value (default `0 0.25`), plus speaker-count accuracy / MAE. Exact interval arithmetic,
  no frame quantisation. DER and its collar handling follow `md-eval-22.pl`; JER follows
  dscore, which applies no collar, so collared JER is our extension on the same scored region.
- **Speaker-agnostic segmentation:** 2x2 speech/silence confusion with intersection, union
  and IoU per cell; onset/offset precision / recall / F1 / MAE / signed displacement at each
  `--boundary-tols` tolerance (default `0.25 0.5` s).

Setup (both envs): `pip install --no-deps -e .`. Tests: `pytest tests/`. The cross-checks
against md-eval-22.pl and dscore use the pinned `third_party/dscore` submodule (override with
`DSCORE_DIR`) and are skipped if it is not checked out.
