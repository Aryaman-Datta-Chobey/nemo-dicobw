# Diarization scores: 20261026-nemotron-zeroshot/ear1_dev_H_all

- name: `20261026-nemotron-zeroshot/ear1_dev_H_all`
- manifest: `/mnt/data/manifests/nemo/ear1_dev_H_all.jsonl`
- ref: `7 files under /mnt/data/refs/ear1/dev/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/ear1_dev_H_all`
- uem: `13 files under /mnt/data/refs/ear1/dev/uem`
- seg_merge_gap: `0.0`
- git_commit: `d87d4bdc6476a710ee4195f2401f921cf5f6d5b5-dirty`
- created: `2026-10-27T14:05:35+00:00`
- condition: `ear1_dev_H_all`
- ref_type: `segments`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 29.97 | 23.21 | 2.75 | 4.02 | 47.84 | 53.85 | 1.38 |
| 0.25 | 20.28 | 13.55 | 2.53 | 4.20 | 40.82 | 53.85 | 1.38 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 72.49 (IoU 83.46) | 12.70 (IoU 12.92) |
| silence | 1.66 (IoU 1.90) | 13.15 (IoU 47.80) |

Speech P/R/F1: 97.76 / 85.09 / 90.99; miss 14.91 of ref speech, FA 11.20 of ref silence, SAD error 16.86.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4259 | 8093 | 45.46 | 86.38 | 59.57 | 0.105 | 0.100 | 0.077 | 0.090 |
| 0.25 | offset | 4259 | 8094 | 34.56 | 65.67 | 45.28 | 0.131 | 0.130 | -0.111 | -0.130 |
| 0.25 | all | 8518 | 16187 | 40.01 | 76.03 | 52.43 | 0.116 | 0.110 | -0.004 | 0.000 |
| 0.50 | onset | 4259 | 8093 | 49.10 | 93.31 | 64.35 | 0.122 | 0.110 | 0.094 | 0.100 |
| 0.50 | offset | 4259 | 8094 | 48.04 | 91.29 | 62.95 | 0.193 | 0.170 | -0.169 | -0.160 |
| 0.50 | all | 8518 | 16187 | 48.57 | 92.30 | 63.65 | 0.157 | 0.130 | -0.036 | -0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| 20260908-1__H1 | 23.62 | 24.86 | 12.43 | 11.38 | 4 | 4 |
| 20260908-1__H2 | 19.21 | 20.48 | 9.99 | 9.69 | 4 | 4 |
| 20260908-2__H1 | 27.84 | 29.62 | 13.98 | 13.50 | 4 | 4 |
| 20260908-2__H2 | 24.25 | 26.99 | 11.83 | 12.71 | 4 | 4 |
| 20260923-1__H1 | 21.96 | 23.90 | 8.47 | 11.06 | 4 | 4 |
| 20260923-2__H1 | 26.26 | 29.94 | 15.61 | 20.07 | 4 | 4 |
| 20260923-5__H1 | 14.54 | 19.07 | 5.28 | 10.86 | 4 | 4 |
| 20260924-2__H1 | 29.07 | 48.68 | 23.26 | 44.62 | 7 | 5 |
| 20260924-2__H2 | 35.06 | 54.42 | 29.37 | 50.90 | 7 | 5 |
| 20260924-2__H3 | 40.61 | 53.95 | 35.49 | 50.19 | 7 | 5 |
| 20260924-5__H1 | 41.40 | 71.39 | 31.52 | 67.78 | 8 | 4 |
| 20260924-5__H2 | 39.86 | 70.14 | 29.97 | 66.35 | 8 | 4 |
| 20260924-5__H3 | 40.31 | 70.14 | 30.28 | 66.19 | 8 | 4 |
