# Diarization scores: A-fa-seed43_s1000/alimeeting_Test_Ali_far_ch1

- name: `A-fa-seed43_s1000/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-seed43_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T15:22:05+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-seed43_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7738-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.71 | 5.46 | 4.52 | 0.73 | 11.34 | 95.00 | 0.05 |
| 0.25 | 1.74 | 1.03 | 0.63 | 0.08 | 2.51 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.11 (IoU 95.19) | 1.90 (IoU 1.94) |
| silence | 2.20 (IoU 2.24) | 14.80 (IoU 78.31) |

Speech P/R/F1: 97.36 / 97.71 / 97.54; miss 2.29 of ref speech, FA 12.94 of ref silence, SAD error 4.94.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12678 | 92.66 | 89.66 | 91.14 | 0.042 | 0.030 | -0.003 | 0.000 |
| 0.25 | offset | 13103 | 12678 | 92.99 | 89.97 | 91.45 | 0.048 | 0.040 | 0.010 | 0.020 |
| 0.25 | all | 26206 | 25356 | 92.83 | 89.82 | 91.30 | 0.045 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13103 | 12678 | 93.62 | 90.58 | 92.08 | 0.046 | 0.030 | -0.003 | 0.000 |
| 0.50 | offset | 13103 | 12678 | 93.74 | 90.70 | 92.19 | 0.050 | 0.040 | 0.010 | 0.020 |
| 0.50 | all | 26206 | 25356 | 93.68 | 90.64 | 92.13 | 0.048 | 0.030 | 0.004 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.80 | 11.05 | 1.10 | 1.31 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.23 | 13.01 | 1.88 | 3.19 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.11 | 10.30 | 1.39 | 1.71 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.21 | 21.55 | 5.09 | 7.16 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.91 | 18.99 | 2.79 | 3.11 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.45 | 7.45 | 1.52 | 1.62 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.87 | 18.88 | 7.74 | 7.47 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.63 | 11.14 | 2.26 | 2.45 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.25 | 7.97 | 0.84 | 1.02 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.80 | 11.10 | 1.82 | 2.05 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.83 | 11.34 | 1.36 | 2.31 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.61 | 6.52 | 0.67 | 0.86 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.56 | 7.24 | 0.79 | 0.77 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.56 | 7.15 | 1.16 | 1.34 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.55 | 12.98 | 1.09 | 1.39 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.96 | 4.79 | 0.98 | 0.96 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.26 | 6.94 | 0.76 | 0.69 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.53 | 8.33 | 1.06 | 1.18 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.48 | 6.31 | 1.98 | 1.92 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.76 | 6.48 | 1.70 | 1.64 | 2 | 3 |
