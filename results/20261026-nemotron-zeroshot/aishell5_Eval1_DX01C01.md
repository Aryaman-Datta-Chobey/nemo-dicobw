# Diarization scores: 20261026-nemotron-zeroshot/aishell5_Eval1_DX01C01

- name: `20261026-nemotron-zeroshot/aishell5_Eval1_DX01C01`
- manifest: `/mnt/data/manifests/nemo/aishell5_Eval1_DX01C01.jsonl`
- ref: `18 files under /mnt/data/refs/aishell5/Eval1/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/aishell5_Eval1_DX01C01`
- uem: `18 files under /mnt/data/refs/aishell5/Eval1/uem`
- seg_merge_gap: `0.0`
- git_commit: `14dba5ba9283b3c5a43d24e874fc385f7285cb11-dirty`
- created: `2026-10-26T15:05:09+00:00`
- condition: `aishell5_Eval1_DX01C01`
- ref_type: `segments`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 31.25 | 20.95 | 7.18 | 3.12 | 26.38 | 0.00 | 1.83 |
| 0.25 | 24.13 | 14.23 | 7.03 | 2.87 | 17.87 | 0.00 | 1.83 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 68.87 (IoU 80.52) | 12.11 (IoU 12.68) |
| silence | 4.56 (IoU 5.19) | 14.46 (IoU 46.46) |

Speech P/R/F1: 93.79 / 85.05 / 89.21; miss 14.95 of ref speech, FA 23.97 of ref silence, SAD error 20.58.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 2156 | 4900 | 34.67 | 78.80 | 48.16 | 0.110 | 0.110 | 0.088 | 0.104 |
| 0.25 | offset | 2156 | 4900 | 30.00 | 68.18 | 41.67 | 0.131 | 0.136 | -0.071 | -0.116 |
| 0.25 | all | 4312 | 9800 | 32.34 | 73.49 | 44.91 | 0.120 | 0.124 | 0.015 | 0.044 |
| 0.50 | onset | 2156 | 4900 | 37.57 | 85.39 | 52.18 | 0.127 | 0.114 | 0.099 | 0.110 |
| 0.50 | offset | 2156 | 4900 | 36.39 | 82.70 | 50.54 | 0.169 | 0.156 | -0.087 | -0.126 |
| 0.50 | all | 4312 | 9800 | 36.98 | 84.04 | 51.36 | 0.147 | 0.134 | 0.008 | 0.044 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| 001__DX01C01 | 21.91 | 15.68 | 10.96 | 4.89 | 2 | 4 |
| 002__DX01C01 | 32.69 | 28.87 | 26.99 | 22.77 | 2 | 4 |
| 003__DX01C01 | 37.20 | 39.40 | 28.13 | 29.58 | 2 | 4 |
| 004__DX01C01 | 16.89 | 16.31 | 6.25 | 6.68 | 2 | 3 |
| 005__DX01C01 | 32.56 | 31.80 | 23.44 | 22.54 | 2 | 3 |
| 006__DX01C01 | 31.72 | 20.44 | 24.41 | 11.35 | 2 | 4 |
| 007__DX01C01 | 13.48 | 11.23 | 7.79 | 5.82 | 2 | 4 |
| 008__DX01C01 | 33.54 | 27.89 | 27.78 | 21.08 | 2 | 4 |
| 009__DX01C01 | 57.95 | 41.90 | 50.05 | 33.00 | 2 | 4 |
| 010__DX01C01 | 37.30 | 23.21 | 36.47 | 15.55 | 2 | 5 |
| 011__DX01C01 | 37.56 | 37.03 | 28.92 | 27.08 | 2 | 3 |
| 012__DX01C01 | 31.66 | 29.18 | 24.31 | 21.58 | 2 | 4 |
| 013__DX01C01 | 22.42 | 23.40 | 14.23 | 14.66 | 2 | 3 |
| 014__DX01C01 | 31.20 | 31.14 | 20.90 | 17.39 | 2 | 4 |
| 015__DX01C01 | 41.58 | 40.82 | 34.73 | 34.00 | 2 | 4 |
| 016__DX01C01 | 22.00 | 21.48 | 15.20 | 14.05 | 2 | 4 |
| 017__DX01C01 | 34.39 | 21.58 | 27.53 | 14.07 | 2 | 4 |
| 018__DX01C01 | 18.93 | 13.57 | 12.05 | 5.61 | 2 | 4 |
