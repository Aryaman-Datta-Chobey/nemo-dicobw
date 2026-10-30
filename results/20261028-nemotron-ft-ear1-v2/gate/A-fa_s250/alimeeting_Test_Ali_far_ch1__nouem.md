# Diarization scores: A-fa_s250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa_s250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T20:35:08+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7891-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.51 | 5.51 | 4.34 | 0.66 | 11.08 | 100.00 | 0.00 |
| 0.25 | 1.46 | 0.82 | 0.58 | 0.06 | 2.26 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.61 (IoU 95.32) | 1.75 (IoU 1.79) |
| silence | 2.26 (IoU 2.30) | 14.38 (IoU 78.21) |

Speech P/R/F1: 97.31 / 97.90 / 97.60; miss 2.10 of ref speech, FA 13.57 of ref silence, SAD error 4.81.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13092 | 12756 | 93.22 | 90.83 | 92.01 | 0.043 | 0.030 | 0.010 | 0.010 |
| 0.25 | offset | 13098 | 12752 | 93.41 | 90.95 | 92.16 | 0.049 | 0.040 | 0.020 | 0.020 |
| 0.25 | all | 26190 | 25508 | 93.32 | 90.89 | 92.08 | 0.046 | 0.040 | 0.015 | 0.020 |
| 0.50 | onset | 13092 | 12756 | 94.00 | 91.59 | 92.78 | 0.046 | 0.030 | 0.010 | 0.010 |
| 0.50 | offset | 13098 | 12752 | 94.11 | 91.62 | 92.85 | 0.051 | 0.040 | 0.020 | 0.020 |
| 0.50 | all | 26190 | 25508 | 94.06 | 91.61 | 92.82 | 0.049 | 0.040 | 0.015 | 0.020 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.90 | 11.14 | 0.99 | 1.17 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.77 | 12.35 | 1.73 | 2.70 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.71 | 9.93 | 1.22 | 1.56 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.44 | 21.82 | 4.90 | 7.18 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.53 | 19.59 | 2.88 | 3.13 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.23 | 7.28 | 1.52 | 1.67 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.67 | 18.71 | 7.67 | 7.46 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.13 | 10.64 | 1.91 | 2.07 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.38 | 8.06 | 0.65 | 0.76 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.60 | 10.62 | 1.67 | 1.88 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.06 | 10.69 | 1.14 | 2.17 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.15 | 6.02 | 0.35 | 0.46 | 3 | 3 |
| R8009_M8021__far_ch1 | 9.42 | 8.90 | 0.47 | 0.46 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.36 | 6.97 | 0.81 | 1.05 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.39 | 9.97 | 0.63 | 0.78 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.03 | 4.95 | 0.40 | 0.39 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.89 | 7.36 | 0.59 | 0.50 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.35 | 7.19 | 0.73 | 0.82 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.37 | 5.16 | 1.19 | 1.13 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.05 | 5.90 | 1.04 | 1.03 | 2 | 2 |
