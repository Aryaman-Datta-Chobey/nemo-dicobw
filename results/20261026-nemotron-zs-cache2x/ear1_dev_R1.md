# Diarization scores: 20261026-nemotron-zs-cache2x/ear1_dev_R1

- name: `20261026-nemotron-zs-cache2x/ear1_dev_R1`
- manifest: `/mnt/data/manifests/nemo/ear1_dev_R1.jsonl`
- ref: `7 files under /mnt/data/refs/ear1/dev/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zs-cache2x/rttm/ear1_dev_R1`
- uem: `7 files under /mnt/data/refs/ear1/dev/uem`
- seg_merge_gap: `0.0`
- git_commit: `d87d4bdc6476a710ee4195f2401f921cf5f6d5b5-dirty`
- created: `2026-10-27T14:29:28+00:00`
- condition: `ear1_dev_R1`
- ref_type: `segments`
- run: `20261026-nemotron-zs-cache2x`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":528,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 36.43 | 25.60 | 5.51 | 5.32 | 47.74 | 57.14 | 0.86 |
| 0.25 | 25.98 | 17.86 | 3.57 | 4.54 | 41.25 | 57.14 | 0.86 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 69.75 (IoU 78.13) | 15.28 (IoU 15.96) |
| silence | 4.24 (IoU 5.01) | 10.72 (IoU 35.45) |

Speech P/R/F1: 94.27 / 82.03 / 87.72; miss 17.97 of ref speech, FA 28.34 of ref silence, SAD error 22.96.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 2529 | 4186 | 36.88 | 61.05 | 45.99 | 0.119 | 0.120 | 0.032 | 0.060 |
| 0.25 | offset | 2527 | 4187 | 24.15 | 40.01 | 30.12 | 0.127 | 0.130 | -0.089 | -0.120 |
| 0.25 | all | 5056 | 8373 | 30.51 | 50.53 | 38.05 | 0.122 | 0.120 | -0.016 | -0.010 |
| 0.50 | onset | 2529 | 4186 | 49.90 | 82.60 | 62.22 | 0.185 | 0.150 | -0.010 | 0.040 |
| 0.50 | offset | 2527 | 4187 | 40.91 | 67.79 | 51.03 | 0.225 | 0.210 | -0.164 | -0.180 |
| 0.50 | all | 5056 | 8373 | 45.41 | 75.20 | 56.62 | 0.203 | 0.180 | -0.080 | -0.090 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| 20260908-1__R1 | 38.30 | 51.04 | 28.81 | 45.41 | 4 | 5 |
| 20260908-2__R1 | 31.84 | 36.69 | 19.21 | 25.00 | 4 | 4 |
| 20260923-1__R1 | 52.58 | 52.71 | 44.32 | 47.41 | 4 | 4 |
| 20260923-2__R1 | 44.91 | 44.50 | 33.17 | 35.39 | 4 | 4 |
| 20260923-5__R1 | 21.50 | 24.50 | 10.80 | 15.42 | 4 | 4 |
| 20260924-2__R1 | 23.45 | 36.38 | 17.62 | 30.97 | 7 | 6 |
| 20260924-5__R1 | 43.32 | 72.32 | 34.18 | 69.07 | 8 | 4 |
