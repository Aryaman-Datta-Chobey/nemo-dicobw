# Diarization scores: A-fa-r75b_s750/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75b_s750/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T02:06:57+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75b_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7699-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.80 | 5.63 | 4.45 | 0.71 | 11.34 | 100.00 | 0.00 |
| 0.25 | 1.90 | 1.03 | 0.80 | 0.07 | 2.61 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.30 (IoU 95.19) | 2.06 (IoU 2.10) |
| silence | 2.05 (IoU 2.09) | 14.60 (IoU 78.04) |

Speech P/R/F1: 97.55 / 97.53 / 97.54; miss 2.47 of ref speech, FA 12.29 of ref silence, SAD error 4.93.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13095 | 12713 | 92.69 | 89.99 | 91.32 | 0.043 | 0.030 | 0.004 | 0.010 |
| 0.25 | offset | 13096 | 12713 | 92.98 | 90.26 | 91.60 | 0.046 | 0.040 | 0.006 | 0.010 |
| 0.25 | all | 26191 | 25426 | 92.84 | 90.13 | 91.46 | 0.045 | 0.030 | 0.005 | 0.010 |
| 0.50 | onset | 13095 | 12713 | 93.70 | 90.97 | 92.31 | 0.047 | 0.030 | 0.004 | 0.010 |
| 0.50 | offset | 13096 | 12713 | 93.89 | 91.14 | 92.49 | 0.049 | 0.040 | 0.006 | 0.010 |
| 0.50 | all | 26191 | 25426 | 93.79 | 91.05 | 92.40 | 0.048 | 0.030 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.29 | 10.52 | 1.09 | 1.29 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.73 | 12.39 | 1.77 | 2.91 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.01 | 10.20 | 1.36 | 1.77 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.64 | 22.03 | 5.18 | 7.52 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.45 | 19.43 | 2.78 | 2.98 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.23 | 7.25 | 1.50 | 1.62 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.05 | 19.13 | 8.00 | 7.92 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.23 | 10.77 | 2.00 | 2.17 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.93 | 7.66 | 0.80 | 0.96 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.41 | 10.57 | 1.90 | 2.24 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.74 | 10.30 | 1.33 | 2.32 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.21 | 6.07 | 0.56 | 0.68 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.42 | 8.03 | 0.68 | 0.67 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.16 | 7.84 | 1.18 | 1.42 | 2 | 2 |
| R8009_M8023__far_ch1 | 11.63 | 14.09 | 1.20 | 1.45 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.72 | 4.67 | 1.02 | 1.04 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.17 | 7.00 | 0.74 | 0.69 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.37 | 8.26 | 1.09 | 1.24 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.30 | 6.17 | 1.87 | 1.81 | 2 | 2 |
| R8009_M8028__far_ch1 | 9.42 | 8.74 | 4.69 | 4.29 | 2 | 2 |
