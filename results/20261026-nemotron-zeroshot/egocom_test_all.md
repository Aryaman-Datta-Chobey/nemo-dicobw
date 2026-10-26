# Diarization scores: 20261026-nemotron-zeroshot/egocom_test_all

- name: `20261026-nemotron-zeroshot/egocom_test_all`
- manifest: `/mnt/data/manifests/nemo/egocom_test_all.jsonl`
- ref: `9 files under /mnt/data/refs/egocom/test/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/egocom_test_all`
- uem: `9 files under /mnt/data/refs/egocom/test/uem`
- seg_merge_gap: `0.0`
- git_commit: `14dba5ba9283b3c5a43d24e874fc385f7285cb11-dirty`
- created: `2026-10-26T15:39:46+00:00`
- condition: `egocom_test_all`
- ref_type: `fa`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 38.08 | 14.15 | 20.17 | 3.75 | 32.84 | 92.31 | 0.08 |
| 0.25 | 22.70 | 6.92 | 13.87 | 1.91 | 22.02 | 92.31 | 0.08 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 67.32 (IoU 81.24) | 5.33 (IoU 5.94) |
| silence | 10.21 (IoU 10.79) | 17.14 (IoU 52.43) |

Speech P/R/F1: 86.83 / 92.66 / 89.65; miss 7.34 of ref speech, FA 37.35 of ref silence, SAD error 21.40.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 8128 | 8582 | 56.79 | 59.97 | 58.34 | 0.057 | 0.030 | -0.009 | -0.005 |
| 0.25 | offset | 8133 | 8581 | 57.95 | 61.15 | 59.51 | 0.076 | 0.055 | 0.010 | 0.010 |
| 0.25 | all | 16261 | 17163 | 57.37 | 60.56 | 58.92 | 0.067 | 0.040 | 0.001 | 0.000 |
| 0.50 | onset | 8128 | 8582 | 70.58 | 74.52 | 72.50 | 0.116 | 0.050 | -0.019 | -0.010 |
| 0.50 | offset | 8133 | 8581 | 70.54 | 74.43 | 72.43 | 0.125 | 0.070 | 0.011 | 0.010 |
| 0.50 | all | 16261 | 17163 | 70.56 | 74.47 | 72.46 | 0.121 | 0.060 | -0.004 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| day_1__con_4__part1__person_1 | 16.48 | 20.78 | 9.04 | 10.99 | 3 | 3 |
| day_1__con_4__part1__person_2 | 17.26 | 20.97 | 6.96 | 9.79 | 3 | 3 |
| day_1__con_4__part1__person_3 | 15.96 | 19.78 | 6.65 | 8.89 | 3 | 3 |
| day_1__con_4__part2__person_1 | 24.91 | 29.60 | 14.57 | 20.12 | 3 | 3 |
| day_1__con_4__part2__person_2 | 20.81 | 21.88 | 9.67 | 11.54 | 3 | 3 |
| day_1__con_4__part2__person_3 | 22.37 | 25.73 | 11.00 | 15.41 | 3 | 3 |
| day_1__con_4__part3__person_1 | 24.34 | 22.76 | 15.44 | 14.63 | 3 | 3 |
| day_1__con_4__part3__person_2 | 27.52 | 25.09 | 18.06 | 17.16 | 3 | 3 |
| day_1__con_4__part3__person_3 | 28.37 | 25.74 | 18.89 | 17.40 | 3 | 3 |
| day_1__con_4__part4__person_1 | 32.53 | 37.52 | 22.99 | 28.42 | 3 | 3 |
| day_1__con_4__part4__person_2 | 32.95 | 36.79 | 22.96 | 27.99 | 3 | 3 |
| day_1__con_4__part4__person_3 | 33.87 | 38.30 | 24.14 | 29.56 | 3 | 3 |
| day_4__con_5__person_1 | 34.01 | 32.76 | 23.53 | 23.72 | 3 | 3 |
| day_4__con_5__person_2 | 35.21 | 32.71 | 25.30 | 24.60 | 3 | 3 |
| day_4__con_5__person_3 | 34.22 | 32.35 | 23.51 | 23.48 | 3 | 3 |
| day_5__con_1__person_1 | 31.50 | 32.63 | 17.18 | 21.44 | 3 | 3 |
| day_5__con_1__person_2 | 38.57 | 35.64 | 20.46 | 24.39 | 3 | 3 |
| day_5__con_4__person_1 | 37.61 | 40.02 | 19.39 | 23.92 | 3 | 3 |
| day_5__con_4__person_2 | 43.60 | 41.89 | 21.19 | 25.25 | 3 | 3 |
| day_5__con_4__person_3 | 41.69 | 41.26 | 19.69 | 23.08 | 3 | 4 |
| day_5__con_7__person_1 | 36.80 | 31.96 | 23.03 | 21.39 | 3 | 3 |
| day_5__con_7__person_2 | 41.60 | 34.37 | 27.40 | 24.01 | 3 | 3 |
| day_5__con_7__person_3 | 37.73 | 31.95 | 25.79 | 22.68 | 3 | 3 |
| day_6__con_4__person_1 | 56.67 | 45.68 | 40.94 | 33.26 | 3 | 3 |
| day_6__con_4__person_2 | 60.04 | 49.23 | 41.47 | 35.26 | 3 | 4 |
| day_6__con_4__person_3 | 59.96 | 46.47 | 42.61 | 34.04 | 3 | 3 |
