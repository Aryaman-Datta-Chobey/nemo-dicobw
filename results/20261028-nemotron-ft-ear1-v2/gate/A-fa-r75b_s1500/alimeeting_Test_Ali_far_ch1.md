# Diarization scores: A-fa-r75b_s1500/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r75b_s1500/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s1500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T02:40:11+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r75b_s1500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7932-epoch=5.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.55 | 5.55 | 4.29 | 0.71 | 11.17 | 100.00 | 0.00 |
| 0.25 | 1.65 | 1.01 | 0.58 | 0.06 | 2.46 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.09 (IoU 95.31) | 1.92 (IoU 1.96) |
| silence | 2.07 (IoU 2.11) | 14.92 (IoU 78.90) |

Speech P/R/F1: 97.51 / 97.69 / 97.60; miss 2.31 of ref speech, FA 12.20 of ref silence, SAD error 4.81.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12788 | 92.81 | 90.57 | 91.68 | 0.043 | 0.030 | 0.002 | 0.010 |
| 0.25 | offset | 13103 | 12788 | 93.02 | 90.78 | 91.89 | 0.046 | 0.040 | 0.007 | 0.010 |
| 0.25 | all | 26206 | 25576 | 92.91 | 90.68 | 91.78 | 0.044 | 0.030 | 0.005 | 0.010 |
| 0.50 | onset | 13103 | 12788 | 93.64 | 91.39 | 92.50 | 0.045 | 0.030 | 0.002 | 0.010 |
| 0.50 | offset | 13103 | 12788 | 93.77 | 91.51 | 92.63 | 0.048 | 0.040 | 0.008 | 0.010 |
| 0.50 | all | 26206 | 25576 | 93.71 | 91.45 | 92.56 | 0.047 | 0.030 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.04 | 10.30 | 1.13 | 1.34 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.79 | 12.42 | 1.82 | 2.91 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.12 | 10.32 | 1.36 | 1.75 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.71 | 22.16 | 5.28 | 7.53 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.41 | 19.41 | 2.85 | 3.08 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.34 | 7.37 | 1.53 | 1.65 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.89 | 18.93 | 7.73 | 7.43 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.22 | 10.83 | 2.03 | 2.24 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.94 | 7.69 | 0.81 | 0.96 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.56 | 10.80 | 1.98 | 2.24 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.70 | 10.25 | 1.37 | 2.41 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.30 | 6.25 | 0.60 | 0.81 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.84 | 8.41 | 0.67 | 0.65 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.94 | 7.63 | 1.11 | 1.38 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.13 | 12.59 | 1.00 | 1.30 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.43 | 4.34 | 0.75 | 0.75 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.87 | 6.58 | 0.68 | 0.59 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.03 | 7.86 | 0.95 | 1.06 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.92 | 5.75 | 1.73 | 1.66 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.05 | 5.95 | 1.04 | 1.03 | 2 | 2 |
