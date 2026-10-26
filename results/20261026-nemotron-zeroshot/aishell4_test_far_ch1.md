# Diarization scores: 20261026-nemotron-zeroshot/aishell4_test_far_ch1

- name: `20261026-nemotron-zeroshot/aishell4_test_far_ch1`
- manifest: `/mnt/data/manifests/nemo/aishell4_test_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/aishell4/test/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/aishell4_test_far_ch1`
- uem: `20 files under /mnt/data/refs/aishell4/test/uem`
- seg_merge_gap: `0.0`
- git_commit: `14dba5ba9283b3c5a43d24e874fc385f7285cb11-dirty`
- created: `2026-10-26T15:05:07+00:00`
- condition: `aishell4_test_far_ch1`
- ref_type: `segments`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.88 | 4.58 | 3.32 | 2.97 | 14.89 | 85.00 | 0.15 |
| 0.25 | 6.23 | 2.26 | 1.29 | 2.68 | 9.80 | 85.00 | 0.15 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 88.00 (IoU 95.37) | 2.46 (IoU 2.51) |
| silence | 1.81 (IoU 1.85) | 7.73 (IoU 64.43) |

Speech P/R/F1: 97.99 / 97.28 / 97.63; miss 2.72 of ref speech, FA 18.95 of ref silence, SAD error 4.72.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 7586 | 5784 | 66.34 | 50.58 | 57.40 | 0.077 | 0.064 | 0.030 | 0.033 |
| 0.25 | offset | 7586 | 5785 | 62.80 | 47.89 | 54.34 | 0.087 | 0.074 | -0.026 | -0.028 |
| 0.25 | all | 15172 | 11569 | 64.57 | 49.24 | 55.87 | 0.082 | 0.069 | 0.003 | 0.006 |
| 0.50 | onset | 7586 | 5784 | 68.53 | 52.25 | 59.30 | 0.085 | 0.067 | 0.033 | 0.034 |
| 0.50 | offset | 7586 | 5785 | 68.19 | 52.00 | 59.01 | 0.107 | 0.082 | -0.042 | -0.034 |
| 0.50 | all | 15172 | 11569 | 68.36 | 52.13 | 59.15 | 0.096 | 0.074 | -0.004 | 0.004 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| L_R003S01C02__far_ch1 | 23.92 | 28.44 | 19.44 | 22.44 | 6 | 6 |
| L_R003S02C02__far_ch1 | 8.59 | 13.32 | 4.71 | 8.80 | 6 | 6 |
| L_R003S03C02__far_ch1 | 15.57 | 15.39 | 9.08 | 9.49 | 6 | 7 |
| L_R003S04C02__far_ch1 | 10.15 | 14.11 | 5.04 | 7.82 | 6 | 6 |
| L_R004S01C01__far_ch1 | 15.62 | 25.10 | 12.49 | 20.61 | 7 | 7 |
| L_R004S02C01__far_ch1 | 8.41 | 17.56 | 4.93 | 14.01 | 7 | 7 |
| L_R004S03C01__far_ch1 | 8.66 | 13.66 | 4.28 | 7.97 | 7 | 7 |
| L_R004S06C01__far_ch1 | 18.01 | 28.73 | 15.49 | 26.96 | 7 | 6 |
| M_R003S01C01__far_ch1 | 10.10 | 11.76 | 3.63 | 4.48 | 6 | 6 |
| M_R003S02C01__far_ch1 | 10.11 | 11.45 | 5.97 | 7.12 | 6 | 6 |
| M_R003S04C01__far_ch1 | 14.58 | 15.96 | 6.10 | 7.81 | 6 | 6 |
| M_R003S05C01__far_ch1 | 14.23 | 13.93 | 8.99 | 8.63 | 6 | 7 |
| S_R003S01C01__far_ch1 | 9.40 | 12.61 | 1.99 | 3.86 | 5 | 5 |
| S_R003S02C01__far_ch1 | 7.36 | 7.86 | 1.49 | 1.95 | 5 | 5 |
| S_R003S03C01__far_ch1 | 8.75 | 8.97 | 2.20 | 2.65 | 5 | 5 |
| S_R003S04C01__far_ch1 | 10.54 | 18.45 | 4.58 | 9.89 | 5 | 5 |
| S_R004S01C01__far_ch1 | 6.47 | 7.96 | 3.96 | 5.16 | 5 | 5 |
| S_R004S02C01__far_ch1 | 4.94 | 8.69 | 2.62 | 6.24 | 5 | 5 |
| S_R004S03C01__far_ch1 | 5.05 | 5.25 | 3.72 | 3.88 | 5 | 5 |
| S_R004S04C01__far_ch1 | 6.11 | 7.34 | 3.32 | 4.36 | 5 | 5 |
