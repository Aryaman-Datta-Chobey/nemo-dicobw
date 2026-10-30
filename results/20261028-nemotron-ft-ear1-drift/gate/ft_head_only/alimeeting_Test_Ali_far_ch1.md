# Diarization scores: ft_head_only/alimeeting_Test_Ali_far_ch1

- name: `ft_head_only/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/ft_head_only/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:41:14+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `ft_head_only`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/ft_head_only.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.49 | 5.72 | 4.08 | 0.69 | 11.07 | 100.00 | 0.00 |
| 0.25 | 1.69 | 1.04 | 0.57 | 0.07 | 2.50 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 80.96 (IoU 95.35) | 2.05 (IoU 2.09) |
| silence | 1.90 (IoU 1.94) | 15.09 (IoU 79.26) |

Speech P/R/F1: 97.71 / 97.53 / 97.62; miss 2.47 of ref speech, FA 11.19 of ref silence, SAD error 4.76.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12940 | 92.15 | 91.00 | 91.57 | 0.042 | 0.030 | -0.003 | 0.000 |
| 0.25 | offset | 13103 | 12940 | 92.43 | 91.28 | 91.85 | 0.044 | 0.030 | -0.004 | 0.000 |
| 0.25 | all | 26206 | 25880 | 92.29 | 91.14 | 91.71 | 0.043 | 0.030 | -0.003 | 0.000 |
| 0.50 | onset | 13103 | 12940 | 93.07 | 91.91 | 92.49 | 0.045 | 0.030 | -0.002 | 0.000 |
| 0.50 | offset | 13103 | 12940 | 93.25 | 92.09 | 92.66 | 0.047 | 0.030 | -0.004 | 0.000 |
| 0.50 | all | 26206 | 25880 | 93.16 | 92.00 | 92.57 | 0.046 | 0.030 | -0.003 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.70 | 10.00 | 1.27 | 1.53 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.31 | 11.84 | 1.79 | 2.95 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.12 | 10.36 | 1.30 | 1.67 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.93 | 22.25 | 5.17 | 7.41 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.90 | 19.87 | 2.90 | 3.15 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.34 | 7.37 | 1.61 | 1.71 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.02 | 19.06 | 7.99 | 7.85 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.06 | 10.62 | 1.91 | 2.13 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.82 | 7.56 | 0.81 | 0.95 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.17 | 10.36 | 2.06 | 2.33 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.51 | 9.91 | 1.32 | 2.30 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.40 | 6.30 | 0.48 | 0.62 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.19 | 6.89 | 0.62 | 0.61 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.34 | 7.02 | 1.18 | 1.44 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.43 | 12.83 | 0.90 | 1.09 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.38 | 4.29 | 0.71 | 0.70 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.86 | 6.67 | 0.66 | 0.59 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.63 | 8.42 | 1.11 | 1.26 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.00 | 5.83 | 1.71 | 1.64 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.35 | 6.20 | 1.47 | 1.45 | 2 | 2 |
