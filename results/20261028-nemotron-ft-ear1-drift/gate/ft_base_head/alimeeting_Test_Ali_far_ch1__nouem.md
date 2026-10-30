# Diarization scores: ft_base_head/alimeeting_Test_Ali_far_ch1__nouem

- name: `ft_base_head/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/ft_base_head/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:41:47+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `ft_base_head`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/ft_base_head.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.92 | 5.12 | 6.02 | 0.78 | 12.53 | 100.00 | 0.00 |
| 0.25 | 1.74 | 0.95 | 0.71 | 0.07 | 2.61 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.62 (IoU 94.31) | 1.69 (IoU 1.74) |
| silence | 3.24 (IoU 3.29) | 13.46 (IoU 73.23) |

Speech P/R/F1: 96.19 / 97.98 / 97.07; miss 2.02 of ref speech, FA 19.38 of ref silence, SAD error 5.91.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13099 | 12112 | 93.11 | 86.09 | 89.46 | 0.051 | 0.040 | -0.014 | -0.010 |
| 0.25 | offset | 13098 | 12113 | 92.59 | 85.63 | 88.98 | 0.060 | 0.050 | 0.023 | 0.020 |
| 0.25 | all | 26197 | 24225 | 92.85 | 85.86 | 89.22 | 0.056 | 0.040 | 0.004 | 0.010 |
| 0.50 | onset | 13099 | 12112 | 94.07 | 86.98 | 90.39 | 0.054 | 0.040 | -0.014 | -0.010 |
| 0.50 | offset | 13098 | 12113 | 94.20 | 87.11 | 90.52 | 0.065 | 0.050 | 0.026 | 0.030 |
| 0.50 | all | 26197 | 24225 | 94.13 | 87.05 | 90.45 | 0.060 | 0.040 | 0.006 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.28 | 10.55 | 1.44 | 1.75 | 4 | 4 |
| R8002_M8003__far_ch1 | 14.31 | 15.04 | 1.79 | 2.92 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.75 | 10.94 | 1.47 | 1.94 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.19 | 22.72 | 5.21 | 7.82 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.97 | 19.90 | 2.73 | 2.95 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.75 | 7.74 | 1.65 | 1.77 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.56 | 19.68 | 8.12 | 7.93 | 4 | 4 |
| R8006_M8012__far_ch1 | 11.15 | 11.58 | 2.24 | 2.39 | 4 | 4 |
| R8008_M8014__far_ch1 | 8.58 | 9.18 | 0.63 | 0.75 | 3 | 3 |
| R8008_M8015__far_ch1 | 17.56 | 17.75 | 1.88 | 2.47 | 3 | 3 |
| R8008_M8016__far_ch1 | 11.06 | 13.13 | 1.44 | 2.58 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.21 | 11.96 | 0.74 | 0.86 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.94 | 8.51 | 0.84 | 0.82 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.21 | 6.87 | 1.24 | 1.52 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.26 | 12.68 | 1.19 | 1.46 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.33 | 5.25 | 1.38 | 1.38 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.85 | 7.34 | 0.71 | 0.63 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.29 | 8.08 | 0.90 | 1.02 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.63 | 6.32 | 1.59 | 1.56 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.91 | 6.65 | 0.89 | 0.88 | 2 | 2 |
