# Diarization scores: 20261026-nemotron-zs-chunk2x/ear1_dev_R1

- name: `20261026-nemotron-zs-chunk2x/ear1_dev_R1`
- manifest: `/mnt/data/manifests/nemo/ear1_dev_R1.jsonl`
- ref: `7 files under /mnt/data/refs/ear1/dev/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zs-chunk2x/rttm/ear1_dev_R1`
- uem: `7 files under /mnt/data/refs/ear1/dev/uem`
- seg_merge_gap: `0.0`
- git_commit: `d87d4bdc6476a710ee4195f2401f921cf5f6d5b5-dirty`
- created: `2026-10-27T14:34:08+00:00`
- condition: `ear1_dev_R1`
- ref_type: `segments`
- run: `20261026-nemotron-zs-chunk2x`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":680,"chunk_right_context":40,"spkcache_update_period":680}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 36.94 | 26.47 | 5.61 | 4.86 | 47.93 | 71.43 | 0.71 |
| 0.25 | 26.49 | 18.66 | 3.73 | 4.10 | 40.94 | 71.43 | 0.71 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 69.16 (IoU 77.36) | 15.88 (IoU 16.60) |
| silence | 4.37 (IoU 5.19) | 10.60 (IoU 34.36) |

Speech P/R/F1: 94.06 / 81.33 / 87.23; miss 18.67 of ref speech, FA 29.18 of ref silence, SAD error 23.80.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 2529 | 4280 | 35.42 | 59.94 | 44.53 | 0.123 | 0.120 | 0.034 | 0.070 |
| 0.25 | offset | 2527 | 4281 | 22.94 | 38.86 | 28.85 | 0.127 | 0.130 | -0.086 | -0.110 |
| 0.25 | all | 5056 | 8561 | 29.18 | 49.41 | 36.69 | 0.125 | 0.120 | -0.013 | -0.000 |
| 0.50 | onset | 2529 | 4280 | 48.36 | 81.85 | 60.80 | 0.190 | 0.160 | -0.009 | 0.050 |
| 0.50 | offset | 2527 | 4281 | 39.66 | 67.19 | 49.88 | 0.228 | 0.220 | -0.164 | -0.190 |
| 0.50 | all | 5056 | 8561 | 44.01 | 74.53 | 55.34 | 0.207 | 0.180 | -0.079 | -0.100 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| 20260908-1__R1 | 37.96 | 48.91 | 27.73 | 38.95 | 4 | 6 |
| 20260908-2__R1 | 32.86 | 38.52 | 20.21 | 26.30 | 4 | 4 |
| 20260923-1__R1 | 53.65 | 53.27 | 45.54 | 48.31 | 4 | 4 |
| 20260923-2__R1 | 44.89 | 43.00 | 33.10 | 34.29 | 4 | 4 |
| 20260923-5__R1 | 21.78 | 25.73 | 11.08 | 16.90 | 4 | 4 |
| 20260924-2__R1 | 25.41 | 37.63 | 19.79 | 32.18 | 7 | 7 |
| 20260924-5__R1 | 43.14 | 72.07 | 33.89 | 68.57 | 8 | 5 |
