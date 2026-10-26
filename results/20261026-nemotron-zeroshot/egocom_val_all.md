# Diarization scores: 20261026-nemotron-zeroshot/egocom_val_all

- name: `20261026-nemotron-zeroshot/egocom_val_all`
- manifest: `/mnt/data/manifests/nemo/egocom_val_all.jsonl`
- ref: `6 files under /mnt/data/refs/egocom/val/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/egocom_val_all`
- uem: `6 files under /mnt/data/refs/egocom/val/uem`
- seg_merge_gap: `0.0`
- git_commit: `14dba5ba9283b3c5a43d24e874fc385f7285cb11-dirty`
- created: `2026-10-26T15:39:49+00:00`
- condition: `egocom_val_all`
- ref_type: `fa`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 31.17 | 14.71 | 14.75 | 1.71 | 28.85 | 83.33 | 0.17 |
| 0.25 | 14.42 | 6.97 | 7.01 | 0.44 | 13.26 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 65.08 (IoU 79.73) | 7.05 (IoU 7.79) |
| silence | 9.49 (IoU 10.22) | 18.37 (IoU 52.62) |

Speech P/R/F1: 87.27 / 90.22 / 88.72; miss 9.78 of ref speech, FA 34.07 of ref silence, SAD error 22.94.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 3576 | 3416 | 57.03 | 54.47 | 55.72 | 0.044 | 0.020 | -0.007 | 0.000 |
| 0.25 | offset | 3576 | 3423 | 57.23 | 54.78 | 55.98 | 0.075 | 0.055 | 0.022 | 0.020 |
| 0.25 | all | 7152 | 6839 | 57.13 | 54.63 | 55.85 | 0.060 | 0.035 | 0.008 | 0.007 |
| 0.50 | onset | 3576 | 3416 | 76.14 | 72.73 | 74.40 | 0.133 | 0.040 | -0.043 | -0.010 |
| 0.50 | offset | 3576 | 3423 | 76.45 | 73.18 | 74.78 | 0.143 | 0.090 | -0.023 | 0.010 |
| 0.50 | all | 7152 | 6839 | 76.30 | 72.96 | 74.59 | 0.138 | 0.060 | -0.033 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| day_1__con_2__part1__person_1 | 22.49 | 26.90 | 12.23 | 16.87 | 3 | 3 |
| day_1__con_2__part1__person_2 | 23.16 | 25.20 | 11.35 | 15.40 | 3 | 3 |
| day_1__con_2__part1__person_3 | 24.18 | 27.47 | 15.29 | 20.49 | 3 | 3 |
| day_1__con_2__part2__person_1 | 22.89 | 26.02 | 10.90 | 14.45 | 3 | 3 |
| day_1__con_2__part2__person_2 | 20.59 | 22.64 | 8.39 | 11.96 | 3 | 3 |
| day_1__con_2__part2__person_3 | 24.27 | 25.11 | 14.91 | 18.47 | 3 | 4 |
| day_1__con_2__part3__person_1 | 23.71 | 27.14 | 12.28 | 13.65 | 3 | 3 |
| day_1__con_2__part3__person_2 | 23.56 | 25.61 | 11.98 | 14.92 | 3 | 3 |
| day_1__con_2__part3__person_3 | 24.00 | 24.86 | 14.55 | 14.80 | 3 | 3 |
| day_1__con_2__part4__person_1 | 14.94 | 16.39 | 5.34 | 6.16 | 3 | 3 |
| day_1__con_2__part4__person_2 | 12.75 | 12.93 | 3.95 | 4.36 | 3 | 3 |
| day_1__con_2__part4__person_3 | 14.81 | 14.14 | 3.78 | 4.36 | 3 | 3 |
| day_1__con_2__part5__person_1 | 20.28 | 46.33 | 8.07 | 7.39 | 3 | 2 |
| day_1__con_2__part5__person_2 | 29.01 | 48.26 | 4.12 | 3.16 | 3 | 2 |
| day_1__con_2__part5__person_3 | 23.47 | 38.72 | 4.19 | 4.76 | 3 | 3 |
| day_5__con_5__person_1 | 32.47 | 38.65 | 17.94 | 23.15 | 3 | 3 |
| day_5__con_5__person_2 | 42.73 | 37.72 | 18.06 | 19.62 | 3 | 3 |
| day_5__con_5__person_3 | 41.82 | 35.20 | 17.37 | 16.49 | 3 | 3 |
