# Diarization scores: 20261026-nemotron-zs-cache2x/ear1_dev_D1

- name: `20261026-nemotron-zs-cache2x/ear1_dev_D1`
- manifest: `/mnt/data/manifests/nemo/ear1_dev_D1.jsonl`
- ref: `7 files under /mnt/data/refs/ear1/dev/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zs-cache2x/rttm/ear1_dev_D1`
- uem: `7 files under /mnt/data/refs/ear1/dev/uem`
- seg_merge_gap: `0.0`
- git_commit: `d87d4bdc6476a710ee4195f2401f921cf5f6d5b5-dirty`
- created: `2026-10-27T14:29:27+00:00`
- condition: `ear1_dev_D1`
- ref_type: `segments`
- run: `20261026-nemotron-zs-cache2x`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":528,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 29.14 | 22.77 | 2.71 | 3.65 | 45.54 | 71.43 | 1.00 |
| 0.25 | 18.29 | 12.18 | 2.71 | 3.39 | 38.13 | 71.43 | 1.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 72.16 (IoU 83.23) | 12.96 (IoU 13.16) |
| silence | 1.58 (IoU 1.82) | 13.31 (IoU 47.79) |

Speech P/R/F1: 97.85 / 84.78 / 90.85; miss 15.22 of ref speech, FA 10.63 of ref silence, SAD error 17.08.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 2531 | 4307 | 50.52 | 85.97 | 63.64 | 0.111 | 0.110 | 0.095 | 0.100 |
| 0.25 | offset | 2531 | 4307 | 41.03 | 69.81 | 51.68 | 0.133 | 0.130 | -0.125 | -0.130 |
| 0.25 | all | 5062 | 8614 | 45.77 | 77.89 | 57.66 | 0.121 | 0.120 | -0.003 | 0.000 |
| 0.50 | onset | 2531 | 4307 | 54.82 | 93.28 | 69.06 | 0.129 | 0.120 | 0.111 | 0.110 |
| 0.50 | offset | 2531 | 4307 | 53.24 | 90.60 | 67.07 | 0.183 | 0.160 | -0.169 | -0.160 |
| 0.50 | all | 5062 | 8614 | 54.03 | 91.94 | 68.06 | 0.156 | 0.140 | -0.027 | -0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| 20260908-1__D1 | 31.14 | 40.74 | 19.91 | 31.52 | 4 | 4 |
| 20260908-2__D1 | 29.66 | 33.80 | 15.76 | 19.19 | 4 | 4 |
| 20260923-1__D1 | 21.31 | 23.45 | 8.44 | 11.08 | 4 | 4 |
| 20260923-2__D1 | 27.22 | 31.89 | 17.01 | 22.23 | 4 | 4 |
| 20260923-5__D1 | 15.24 | 24.02 | 6.97 | 17.23 | 4 | 4 |
| 20260924-2__D1 | 32.45 | 58.93 | 27.14 | 56.40 | 7 | 4 |
| 20260924-5__D1 | 41.00 | 70.71 | 31.11 | 66.86 | 8 | 4 |
