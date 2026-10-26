# Diarization scores: 20261026-nemotron-zeroshot/aishell5_Dev_DX01C01

- name: `20261026-nemotron-zeroshot/aishell5_Dev_DX01C01`
- manifest: `/mnt/data/manifests/nemo/aishell5_Dev_DX01C01.jsonl`
- ref: `18 files under /mnt/data/refs/aishell5/Dev/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/aishell5_Dev_DX01C01`
- uem: `18 files under /mnt/data/refs/aishell5/Dev/uem`
- seg_merge_gap: `0.0`
- git_commit: `14dba5ba9283b3c5a43d24e874fc385f7285cb11-dirty`
- created: `2026-10-26T15:05:08+00:00`
- condition: `aishell5_Dev_DX01C01`
- ref_type: `segments`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 22.53 | 16.27 | 5.54 | 0.71 | 20.77 | 5.56 | 1.44 |
| 0.25 | 16.04 | 11.26 | 4.26 | 0.53 | 13.80 | 5.56 | 1.44 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 66.39 (IoU 83.42) | 9.45 (IoU 9.82) |
| silence | 3.74 (IoU 4.13) | 20.41 (IoU 60.74) |

Speech P/R/F1: 94.66 / 87.54 / 90.96; miss 12.46 of ref speech, FA 15.49 of ref silence, SAD error 17.40.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 2756 | 4738 | 49.49 | 85.09 | 62.58 | 0.086 | 0.080 | 0.048 | 0.064 |
| 0.25 | offset | 2756 | 4740 | 46.50 | 79.97 | 58.80 | 0.108 | 0.106 | -0.041 | -0.076 |
| 0.25 | all | 5512 | 9478 | 48.00 | 82.53 | 60.69 | 0.097 | 0.090 | 0.005 | 0.014 |
| 0.50 | onset | 2756 | 4738 | 51.69 | 88.86 | 65.36 | 0.097 | 0.084 | 0.055 | 0.064 |
| 0.50 | offset | 2756 | 4740 | 51.48 | 88.53 | 65.10 | 0.129 | 0.112 | -0.037 | -0.076 |
| 0.50 | all | 5512 | 9478 | 51.58 | 88.70 | 65.23 | 0.113 | 0.096 | 0.009 | 0.024 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| 001__DX01C01 | 38.09 | 30.66 | 31.93 | 22.16 | 2 | 4 |
| 002__DX01C01 | 25.43 | 21.61 | 20.12 | 15.52 | 2 | 4 |
| 003__DX01C01 | 23.09 | 18.70 | 15.97 | 11.16 | 2 | 4 |
| 004__DX01C01 | 30.35 | 28.90 | 23.44 | 21.42 | 2 | 3 |
| 005__DX01C01 | 27.41 | 22.27 | 19.63 | 12.81 | 2 | 3 |
| 006__DX01C01 | 17.22 | 16.44 | 12.70 | 11.96 | 2 | 3 |
| 007__DX01C01 | 13.72 | 12.20 | 9.09 | 7.02 | 2 | 3 |
| 008__DX01C01 | 25.00 | 20.43 | 20.70 | 14.61 | 2 | 4 |
| 009__DX01C01 | 18.15 | 15.69 | 9.21 | 8.49 | 2 | 4 |
| 010__DX01C01 | 16.94 | 12.98 | 9.29 | 6.20 | 2 | 3 |
| 011__DX01C01 | 25.57 | 25.89 | 18.73 | 19.27 | 2 | 2 |
| 012__DX01C01 | 23.80 | 23.55 | 18.94 | 18.80 | 2 | 4 |
| 013__DX01C01 | 29.85 | 29.39 | 23.30 | 22.50 | 2 | 4 |
| 014__DX01C01 | 22.96 | 21.54 | 16.46 | 14.90 | 2 | 4 |
| 015__DX01C01 | 14.02 | 14.07 | 5.26 | 4.48 | 2 | 3 |
| 016__DX01C01 | 24.33 | 24.50 | 17.37 | 17.47 | 2 | 3 |
| 017__DX01C01 | 16.31 | 13.60 | 8.73 | 5.81 | 2 | 4 |
| 018__DX01C01 | 22.14 | 21.48 | 14.17 | 13.73 | 2 | 3 |
