# Diarization scores: 20261026-nemotron-zeroshot/aishell5_Eval2_DX01C01

- name: `20261026-nemotron-zeroshot/aishell5_Eval2_DX01C01`
- manifest: `/mnt/data/manifests/nemo/aishell5_Eval2_DX01C01.jsonl`
- ref: `18 files under /mnt/data/refs/aishell5/Eval2/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/aishell5_Eval2_DX01C01`
- uem: `18 files under /mnt/data/refs/aishell5/Eval2/uem`
- seg_merge_gap: `0.0`
- git_commit: `14dba5ba9283b3c5a43d24e874fc385f7285cb11-dirty`
- created: `2026-10-26T15:05:10+00:00`
- condition: `aishell5_Eval2_DX01C01`
- ref_type: `segments`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 24.95 | 20.59 | 3.66 | 0.69 | 25.48 | 0.00 | 1.56 |
| 0.25 | 17.81 | 13.76 | 3.52 | 0.53 | 17.47 | 0.00 | 1.56 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 68.73 (IoU 82.47) | 12.27 (IoU 12.56) |
| silence | 2.34 (IoU 2.66) | 16.66 (IoU 53.29) |

Speech P/R/F1: 96.71 / 84.85 / 90.39; miss 15.15 of ref speech, FA 12.30 of ref silence, SAD error 18.03.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 2390 | 5152 | 39.97 | 86.15 | 54.60 | 0.106 | 0.104 | 0.094 | 0.100 |
| 0.25 | offset | 2390 | 5152 | 37.50 | 80.84 | 51.23 | 0.124 | 0.126 | -0.101 | -0.120 |
| 0.25 | all | 4780 | 10304 | 38.73 | 83.49 | 52.92 | 0.115 | 0.114 | -0.000 | 0.020 |
| 0.50 | onset | 2390 | 5152 | 41.96 | 90.46 | 57.33 | 0.117 | 0.110 | 0.102 | 0.104 |
| 0.50 | offset | 2390 | 5152 | 40.90 | 88.16 | 55.87 | 0.142 | 0.130 | -0.112 | -0.126 |
| 0.50 | all | 4780 | 10304 | 41.43 | 89.31 | 56.60 | 0.130 | 0.120 | -0.003 | 0.020 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| 001__DX01C01 | 17.62 | 22.83 | 7.10 | 10.65 | 2 | 3 |
| 002__DX01C01 | 31.37 | 28.81 | 23.37 | 20.14 | 2 | 4 |
| 003__DX01C01 | 40.16 | 33.69 | 27.32 | 18.89 | 2 | 4 |
| 004__DX01C01 | 32.79 | 26.58 | 27.72 | 20.78 | 2 | 4 |
| 005__DX01C01 | 24.14 | 25.28 | 19.76 | 21.68 | 2 | 4 |
| 006__DX01C01 | 29.68 | 28.71 | 22.50 | 21.45 | 2 | 4 |
| 007__DX01C01 | 33.30 | 32.04 | 25.61 | 24.41 | 2 | 4 |
| 008__DX01C01 | 13.83 | 15.95 | 10.45 | 11.96 | 2 | 3 |
| 009__DX01C01 | 29.13 | 32.79 | 20.87 | 24.72 | 2 | 3 |
| 010__DX01C01 | 13.27 | 15.81 | 8.71 | 11.02 | 2 | 3 |
| 011__DX01C01 | 27.08 | 25.22 | 19.94 | 16.34 | 2 | 3 |
| 012__DX01C01 | 22.83 | 18.84 | 18.55 | 14.14 | 2 | 4 |
| 013__DX01C01 | 13.55 | 16.61 | 8.57 | 7.35 | 2 | 4 |
| 014__DX01C01 | 22.73 | 25.13 | 15.42 | 16.81 | 2 | 3 |
| 015__DX01C01 | 28.57 | 24.30 | 23.25 | 18.59 | 2 | 4 |
| 016__DX01C01 | 38.42 | 37.63 | 27.70 | 27.16 | 2 | 4 |
| 017__DX01C01 | 23.96 | 23.29 | 12.35 | 11.82 | 2 | 3 |
| 018__DX01C01 | 21.35 | 25.03 | 14.94 | 16.51 | 2 | 3 |
