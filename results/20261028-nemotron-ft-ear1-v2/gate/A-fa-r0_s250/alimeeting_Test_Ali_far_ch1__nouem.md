# Diarization scores: A-fa-r0_s250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r0_s250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T17:13:34+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r0_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7701-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.96 | 6.27 | 3.99 | 0.70 | 11.58 | 100.00 | 0.00 |
| 0.25 | 1.55 | 0.92 | 0.51 | 0.13 | 2.42 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.48 (IoU 95.22) | 1.88 (IoU 1.92) |
| silence | 2.22 (IoU 2.26) | 14.43 (IoU 77.91) |

Speech P/R/F1: 97.35 / 97.75 / 97.55; miss 2.25 of ref speech, FA 13.31 of ref silence, SAD error 4.91.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13092 | 12967 | 92.16 | 91.28 | 91.71 | 0.045 | 0.040 | 0.013 | 0.020 |
| 0.25 | offset | 13097 | 12962 | 92.25 | 91.30 | 91.78 | 0.050 | 0.040 | 0.018 | 0.020 |
| 0.25 | all | 26189 | 25929 | 92.21 | 91.29 | 91.75 | 0.047 | 0.040 | 0.016 | 0.020 |
| 0.50 | onset | 13092 | 12967 | 92.97 | 92.09 | 92.53 | 0.048 | 0.040 | 0.013 | 0.020 |
| 0.50 | offset | 13097 | 12962 | 93.06 | 92.11 | 92.58 | 0.052 | 0.040 | 0.019 | 0.020 |
| 0.50 | all | 26189 | 25929 | 93.02 | 92.10 | 92.56 | 0.050 | 0.040 | 0.016 | 0.020 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.57 | 10.93 | 1.11 | 1.29 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.79 | 12.44 | 1.76 | 2.81 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.29 | 10.61 | 1.34 | 1.78 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.49 | 23.07 | 5.18 | 7.13 | 4 | 4 |
| R8005_M8007__far_ch1 | 20.79 | 20.88 | 3.18 | 3.50 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.83 | 7.92 | 1.58 | 1.75 | 4 | 4 |
| R8005_M8009__far_ch1 | 20.53 | 20.74 | 8.13 | 8.04 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.56 | 11.09 | 1.93 | 2.17 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.39 | 7.98 | 0.61 | 0.72 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.61 | 10.64 | 1.62 | 1.82 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.58 | 11.30 | 1.16 | 2.13 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.24 | 6.11 | 0.38 | 0.50 | 3 | 3 |
| R8009_M8021__far_ch1 | 9.63 | 9.10 | 0.48 | 0.48 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.36 | 7.03 | 0.78 | 1.04 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.46 | 9.60 | 0.55 | 0.66 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.27 | 5.20 | 0.38 | 0.37 | 2 | 2 |
| R8009_M8025__far_ch1 | 9.13 | 9.58 | 1.78 | 3.04 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.11 | 7.00 | 0.70 | 0.79 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.20 | 4.99 | 1.02 | 0.96 | 2 | 2 |
| R8009_M8028__far_ch1 | 5.72 | 5.62 | 0.67 | 0.67 | 2 | 2 |
