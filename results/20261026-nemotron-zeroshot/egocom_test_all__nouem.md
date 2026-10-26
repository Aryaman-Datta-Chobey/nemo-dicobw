# Diarization scores: 20261026-nemotron-zeroshot/egocom_test_all__nouem

- name: `20261026-nemotron-zeroshot/egocom_test_all__nouem`
- manifest: `/mnt/data/manifests/nemo/egocom_test_all.jsonl`
- ref: `9 files under /mnt/data/refs/egocom/test/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/egocom_test_all`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `14dba5ba9283b3c5a43d24e874fc385f7285cb11-dirty`
- created: `2026-10-26T15:39:48+00:00`
- condition: `egocom_test_all__nouem`
- ref_type: `fa`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 38.09 | 14.15 | 20.18 | 3.75 | 32.85 | 92.31 | 0.08 |
| 0.25 | 22.71 | 6.92 | 13.87 | 1.91 | 22.02 | 92.31 | 0.08 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 67.34 (IoU 81.23) | 5.33 (IoU 5.94) |
| silence | 10.22 (IoU 10.80) | 17.10 (IoU 52.36) |

Speech P/R/F1: 86.82 / 92.66 / 89.65; miss 7.34 of ref speech, FA 37.42 of ref silence, SAD error 21.41.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 8123 | 8572 | 56.72 | 59.85 | 58.24 | 0.057 | 0.030 | -0.009 | -0.005 |
| 0.25 | offset | 8133 | 8576 | 57.91 | 61.06 | 59.44 | 0.076 | 0.055 | 0.010 | 0.010 |
| 0.25 | all | 16256 | 17148 | 57.31 | 60.46 | 58.84 | 0.067 | 0.040 | 0.001 | 0.000 |
| 0.50 | onset | 8123 | 8572 | 70.52 | 74.42 | 72.42 | 0.116 | 0.050 | -0.019 | -0.010 |
| 0.50 | offset | 8133 | 8576 | 70.49 | 74.33 | 72.36 | 0.125 | 0.070 | 0.011 | 0.010 |
| 0.50 | all | 16256 | 17148 | 70.50 | 74.37 | 72.39 | 0.121 | 0.060 | -0.004 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| day_1__con_4__part1__person_1 | 16.48 | 20.78 | 9.04 | 10.99 | 3 | 3 |
| day_1__con_4__part1__person_2 | 17.37 | 21.02 | 7.11 | 9.87 | 3 | 3 |
| day_1__con_4__part1__person_3 | 16.04 | 19.81 | 6.76 | 8.95 | 3 | 3 |
| day_1__con_4__part2__person_1 | 24.91 | 29.60 | 14.57 | 20.12 | 3 | 3 |
| day_1__con_4__part2__person_2 | 20.81 | 21.88 | 9.67 | 11.54 | 3 | 3 |
| day_1__con_4__part2__person_3 | 22.43 | 25.77 | 11.00 | 15.41 | 3 | 3 |
| day_1__con_4__part3__person_1 | 24.34 | 22.76 | 15.44 | 14.63 | 3 | 3 |
| day_1__con_4__part3__person_2 | 27.52 | 25.09 | 18.06 | 17.16 | 3 | 3 |
| day_1__con_4__part3__person_3 | 28.40 | 25.77 | 18.89 | 17.40 | 3 | 3 |
| day_1__con_4__part4__person_1 | 32.57 | 37.54 | 22.99 | 28.42 | 3 | 3 |
| day_1__con_4__part4__person_2 | 32.95 | 36.79 | 22.96 | 27.99 | 3 | 3 |
| day_1__con_4__part4__person_3 | 33.88 | 38.31 | 24.14 | 29.56 | 3 | 3 |
| day_4__con_5__person_1 | 34.01 | 32.76 | 23.53 | 23.72 | 3 | 3 |
| day_4__con_5__person_2 | 35.21 | 32.71 | 25.30 | 24.60 | 3 | 3 |
| day_4__con_5__person_3 | 34.22 | 32.35 | 23.51 | 23.48 | 3 | 3 |
| day_5__con_1__person_1 | 31.50 | 32.63 | 17.18 | 21.44 | 3 | 3 |
| day_5__con_1__person_2 | 38.57 | 35.64 | 20.46 | 24.39 | 3 | 3 |
| day_5__con_4__person_1 | 37.62 | 40.02 | 19.39 | 23.92 | 3 | 3 |
| day_5__con_4__person_2 | 43.60 | 41.89 | 21.19 | 25.25 | 3 | 3 |
| day_5__con_4__person_3 | 41.69 | 41.26 | 19.69 | 23.08 | 3 | 4 |
| day_5__con_7__person_1 | 36.82 | 31.97 | 23.05 | 21.41 | 3 | 3 |
| day_5__con_7__person_2 | 41.60 | 34.37 | 27.40 | 24.01 | 3 | 3 |
| day_5__con_7__person_3 | 37.74 | 31.95 | 25.79 | 22.68 | 3 | 3 |
| day_6__con_4__person_1 | 56.67 | 45.68 | 40.94 | 33.26 | 3 | 3 |
| day_6__con_4__person_2 | 60.08 | 49.24 | 41.48 | 35.27 | 3 | 4 |
| day_6__con_4__person_3 | 59.97 | 46.48 | 42.61 | 34.04 | 3 | 3 |
