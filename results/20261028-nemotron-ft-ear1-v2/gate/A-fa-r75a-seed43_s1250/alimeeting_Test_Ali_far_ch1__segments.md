# Diarization scores: A-fa-r75a-seed43_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a-seed43_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T04:55:13+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a-seed43_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7883-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.11 | 16.50 | 1.05 | 0.56 | 18.79 | 100.00 | 0.00 |
| 0.25 | 10.21 | 9.72 | 0.32 | 0.17 | 11.97 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.81 (IoU 89.80) | 9.15 (IoU 9.17) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 45.25) |

Speech P/R/F1: 99.68 / 90.05 / 94.62; miss 9.95 of ref speech, FA 3.29 of ref silence, SAD error 10.23.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12801 | 35.25 | 92.55 | 51.05 | 0.086 | 0.080 | 0.067 | 0.070 |
| 0.25 | offset | 4875 | 12801 | 34.97 | 91.84 | 50.66 | 0.090 | 0.080 | -0.078 | -0.080 |
| 0.25 | all | 9750 | 25602 | 35.11 | 92.19 | 50.85 | 0.088 | 0.080 | -0.005 | -0.010 |
| 0.50 | onset | 4875 | 12801 | 36.31 | 95.34 | 52.59 | 0.094 | 0.080 | 0.072 | 0.075 |
| 0.50 | offset | 4875 | 12801 | 36.75 | 96.49 | 53.22 | 0.102 | 0.090 | -0.086 | -0.090 |
| 0.50 | all | 9750 | 25602 | 36.53 | 95.92 | 52.91 | 0.098 | 0.090 | -0.007 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.18 | 16.47 | 11.40 | 11.89 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.64 | 20.97 | 15.50 | 17.71 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.14 | 16.82 | 10.17 | 11.45 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.58 | 25.12 | 17.61 | 19.74 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.74 | 24.31 | 16.21 | 16.39 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.21 | 12.80 | 9.97 | 9.03 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.92 | 27.81 | 24.98 | 24.41 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.23 | 16.66 | 10.74 | 10.83 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.95 | 16.71 | 12.03 | 12.58 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.66 | 22.42 | 17.94 | 18.28 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.15 | 22.57 | 13.58 | 17.01 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.62 | 16.94 | 12.35 | 12.98 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.22 | 16.13 | 3.95 | 3.79 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.16 | 15.36 | 2.50 | 2.95 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.27 | 18.41 | 3.50 | 4.79 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.51 | 13.44 | 1.43 | 1.42 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.26 | 14.02 | 2.30 | 2.20 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.32 | 17.44 | 3.08 | 3.13 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.98 | 15.92 | 4.26 | 4.17 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.60 | 13.25 | 2.66 | 2.58 | 2 | 2 |
