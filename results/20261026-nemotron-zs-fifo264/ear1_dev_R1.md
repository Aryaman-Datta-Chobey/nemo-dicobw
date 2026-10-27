# Diarization scores: 20261026-nemotron-zs-fifo264/ear1_dev_R1

- name: `20261026-nemotron-zs-fifo264/ear1_dev_R1`
- manifest: `/mnt/data/manifests/nemo/ear1_dev_R1.jsonl`
- ref: `7 files under /mnt/data/refs/ear1/dev/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zs-fifo264/rttm/ear1_dev_R1`
- uem: `7 files under /mnt/data/refs/ear1/dev/uem`
- seg_merge_gap: `0.0`
- git_commit: `d87d4bdc6476a710ee4195f2401f921cf5f6d5b5-dirty`
- created: `2026-10-27T14:41:24+00:00`
- condition: `ear1_dev_R1`
- ref_type: `segments`
- run: `20261026-nemotron-zs-fifo264`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":264,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 38.38 | 26.25 | 5.36 | 6.77 | 47.62 | 57.14 | 1.00 |
| 0.25 | 27.52 | 18.26 | 3.41 | 5.85 | 40.64 | 57.14 | 1.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 69.35 (IoU 77.76) | 15.69 (IoU 16.37) |
| silence | 4.14 (IoU 4.91) | 10.82 (IoU 35.30) |

Speech P/R/F1: 94.36 / 81.55 / 87.49; miss 18.45 of ref speech, FA 27.69 of ref silence, SAD error 23.32.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 2529 | 4356 | 35.17 | 60.58 | 44.50 | 0.124 | 0.120 | 0.037 | 0.070 |
| 0.25 | offset | 2527 | 4357 | 22.91 | 39.49 | 28.99 | 0.127 | 0.130 | -0.095 | -0.120 |
| 0.25 | all | 5056 | 8713 | 29.04 | 50.04 | 36.75 | 0.125 | 0.120 | -0.015 | -0.010 |
| 0.50 | onset | 2529 | 4356 | 47.87 | 82.44 | 60.57 | 0.190 | 0.160 | -0.010 | 0.050 |
| 0.50 | offset | 2527 | 4357 | 39.38 | 67.91 | 49.85 | 0.227 | 0.220 | -0.169 | -0.190 |
| 0.50 | all | 5056 | 8713 | 43.62 | 75.18 | 55.21 | 0.207 | 0.180 | -0.082 | -0.100 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| 20260908-1__R1 | 48.98 | 53.91 | 39.56 | 44.77 | 4 | 6 |
| 20260908-2__R1 | 33.06 | 37.97 | 20.71 | 26.78 | 4 | 4 |
| 20260923-1__R1 | 52.65 | 52.53 | 44.38 | 47.26 | 4 | 5 |
| 20260923-2__R1 | 45.04 | 43.18 | 33.33 | 34.79 | 4 | 4 |
| 20260923-5__R1 | 21.64 | 24.55 | 10.92 | 15.40 | 4 | 4 |
| 20260924-2__R1 | 22.20 | 32.89 | 16.25 | 26.62 | 7 | 7 |
| 20260924-5__R1 | 44.99 | 73.47 | 35.51 | 70.02 | 8 | 4 |
