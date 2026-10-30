# Diarization scores: D-fa_s250/alimeeting_Test_Ali_far_ch1

- name: `D-fa_s250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-fa_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T23:53:52+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `D-fa_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7695-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.94 | 6.79 | 3.53 | 0.62 | 11.55 | 100.00 | 0.00 |
| 0.25 | 1.73 | 1.22 | 0.45 | 0.05 | 2.59 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.03 (IoU 95.29) | 1.98 (IoU 2.02) |
| silence | 2.02 (IoU 2.06) | 14.97 (IoU 78.91) |

Speech P/R/F1: 97.56 / 97.62 / 97.59; miss 2.38 of ref speech, FA 11.91 of ref silence, SAD error 4.82.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 13233 | 90.76 | 91.66 | 91.21 | 0.042 | 0.030 | -0.008 | -0.010 |
| 0.25 | offset | 13103 | 13233 | 91.05 | 91.95 | 91.49 | 0.044 | 0.030 | -0.002 | 0.000 |
| 0.25 | all | 26206 | 26466 | 90.90 | 91.80 | 91.35 | 0.043 | 0.030 | -0.005 | 0.000 |
| 0.50 | onset | 13103 | 13233 | 91.73 | 92.64 | 92.18 | 0.045 | 0.030 | -0.008 | -0.010 |
| 0.50 | offset | 13103 | 13233 | 91.90 | 92.81 | 92.35 | 0.047 | 0.030 | -0.002 | 0.000 |
| 0.50 | all | 26206 | 26466 | 91.81 | 92.72 | 92.27 | 0.046 | 0.030 | -0.005 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.96 | 10.31 | 1.32 | 1.58 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.69 | 12.38 | 1.69 | 2.70 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.50 | 10.80 | 1.33 | 1.68 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.77 | 24.49 | 6.21 | 8.36 | 4 | 4 |
| R8005_M8007__far_ch1 | 21.11 | 21.15 | 3.32 | 3.52 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.84 | 7.89 | 1.80 | 1.96 | 4 | 4 |
| R8005_M8009__far_ch1 | 20.32 | 20.24 | 8.46 | 8.16 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.56 | 11.06 | 2.12 | 2.39 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.92 | 7.67 | 0.76 | 0.91 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.45 | 10.60 | 2.02 | 2.26 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.62 | 10.06 | 1.31 | 2.25 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.69 | 6.57 | 0.58 | 0.72 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.00 | 6.70 | 0.53 | 0.52 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.20 | 6.88 | 1.06 | 1.29 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.61 | 12.92 | 0.83 | 1.02 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.46 | 4.34 | 0.61 | 0.61 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.71 | 6.56 | 0.66 | 0.59 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.75 | 8.49 | 1.04 | 1.19 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.08 | 5.87 | 1.63 | 1.57 | 2 | 2 |
| R8009_M8028__far_ch1 | 5.93 | 5.79 | 1.09 | 1.08 | 2 | 2 |
