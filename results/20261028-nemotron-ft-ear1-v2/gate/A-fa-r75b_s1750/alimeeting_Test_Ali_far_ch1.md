# Diarization scores: A-fa-r75b_s1750/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r75b_s1750/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s1750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T02:51:14+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r75b_s1750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7883-epoch=6.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.70 | 5.66 | 4.32 | 0.72 | 11.29 | 100.00 | 0.00 |
| 0.25 | 1.82 | 1.10 | 0.65 | 0.07 | 2.60 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 80.96 (IoU 95.22) | 2.05 (IoU 2.09) |
| silence | 2.02 (IoU 2.06) | 14.98 (IoU 78.66) |

Speech P/R/F1: 97.57 / 97.53 / 97.55; miss 2.47 of ref speech, FA 11.87 of ref silence, SAD error 4.90.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12826 | 92.48 | 90.53 | 91.50 | 0.043 | 0.030 | 0.000 | 0.000 |
| 0.25 | offset | 13103 | 12826 | 92.65 | 90.69 | 91.66 | 0.045 | 0.030 | 0.004 | 0.010 |
| 0.25 | all | 26206 | 25652 | 92.57 | 90.61 | 91.58 | 0.044 | 0.030 | 0.002 | 0.010 |
| 0.50 | onset | 13103 | 12826 | 93.40 | 91.42 | 92.40 | 0.046 | 0.030 | 0.001 | 0.000 |
| 0.50 | offset | 13103 | 12826 | 93.47 | 91.49 | 92.47 | 0.048 | 0.030 | 0.004 | 0.010 |
| 0.50 | all | 26206 | 25652 | 93.43 | 91.46 | 92.43 | 0.047 | 0.030 | 0.002 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.78 | 10.04 | 1.11 | 1.32 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.67 | 12.24 | 1.79 | 2.80 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.33 | 10.51 | 1.39 | 1.78 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.69 | 22.05 | 5.23 | 7.50 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.69 | 19.70 | 2.83 | 3.07 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.44 | 7.44 | 1.62 | 1.71 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.15 | 19.19 | 8.07 | 7.93 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.20 | 10.76 | 2.07 | 2.25 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.84 | 7.65 | 0.85 | 1.01 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.48 | 10.90 | 2.02 | 2.39 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.95 | 10.53 | 1.63 | 2.80 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.42 | 6.37 | 0.68 | 0.88 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.73 | 8.32 | 0.73 | 0.72 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.98 | 7.67 | 1.22 | 1.47 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.73 | 13.17 | 1.31 | 1.54 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.81 | 4.74 | 1.23 | 1.24 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.97 | 6.76 | 0.71 | 0.62 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.28 | 8.11 | 0.93 | 1.05 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.15 | 5.99 | 1.92 | 1.85 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.17 | 6.90 | 2.37 | 2.27 | 2 | 2 |
