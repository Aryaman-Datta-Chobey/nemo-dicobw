# Diarization scores: A-fa-seed43_s1250/alimeeting_Test_Ali_far_ch1

- name: `A-fa-seed43_s1250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-seed43_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T15:31:41+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-seed43_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7798-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.68 | 5.46 | 4.49 | 0.72 | 11.32 | 100.00 | 0.00 |
| 0.25 | 1.72 | 1.01 | 0.63 | 0.08 | 2.53 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.08 (IoU 95.21) | 1.93 (IoU 1.97) |
| silence | 2.15 (IoU 2.20) | 14.84 (IoU 78.42) |

Speech P/R/F1: 97.41 / 97.68 / 97.54; miss 2.32 of ref speech, FA 12.68 of ref silence, SAD error 4.92.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12756 | 92.56 | 90.11 | 91.32 | 0.043 | 0.030 | 0.003 | 0.010 |
| 0.25 | offset | 13103 | 12756 | 92.84 | 90.38 | 91.60 | 0.048 | 0.040 | 0.012 | 0.020 |
| 0.25 | all | 26206 | 25512 | 92.70 | 90.25 | 91.46 | 0.045 | 0.030 | 0.008 | 0.010 |
| 0.50 | onset | 13103 | 12756 | 93.49 | 91.01 | 92.23 | 0.046 | 0.030 | 0.003 | 0.010 |
| 0.50 | offset | 13103 | 12756 | 93.60 | 91.12 | 92.34 | 0.050 | 0.040 | 0.013 | 0.020 |
| 0.50 | all | 26206 | 25512 | 93.54 | 91.06 | 92.29 | 0.048 | 0.030 | 0.008 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.71 | 10.95 | 1.10 | 1.30 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.25 | 13.02 | 1.94 | 3.21 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.23 | 10.46 | 1.51 | 1.98 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.31 | 21.68 | 5.18 | 7.49 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.81 | 18.84 | 2.76 | 2.97 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.46 | 7.44 | 1.57 | 1.67 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.86 | 18.92 | 7.76 | 7.47 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.57 | 11.06 | 2.31 | 2.49 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.30 | 8.05 | 0.87 | 1.05 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.64 | 10.88 | 1.84 | 2.06 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.96 | 11.47 | 1.41 | 2.38 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.62 | 6.55 | 0.67 | 0.87 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.20 | 7.85 | 0.78 | 0.76 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.47 | 7.09 | 1.12 | 1.32 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.76 | 12.10 | 0.92 | 1.14 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.04 | 4.96 | 1.13 | 1.12 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.47 | 7.12 | 0.71 | 0.64 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.37 | 8.19 | 1.03 | 1.14 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.23 | 6.06 | 1.91 | 1.84 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.25 | 6.07 | 1.17 | 1.15 | 2 | 2 |
