# Diarization scores: A-fa-r75b-seed43_s1500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b-seed43_s1500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s1500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T07:29:01+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b-seed43_s1500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7953-epoch=5.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.16 | 16.55 | 1.03 | 0.58 | 18.86 | 100.00 | 0.00 |
| 0.25 | 10.22 | 9.74 | 0.31 | 0.17 | 12.00 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.78 (IoU 89.76) | 9.18 (IoU 9.21) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 45.18) |

Speech P/R/F1: 99.69 / 90.02 / 94.60; miss 9.98 of ref speech, FA 3.23 of ref silence, SAD error 10.27.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12785 | 35.21 | 92.35 | 50.99 | 0.086 | 0.080 | 0.068 | 0.070 |
| 0.25 | offset | 4875 | 12786 | 34.94 | 91.63 | 50.59 | 0.091 | 0.090 | -0.079 | -0.080 |
| 0.25 | all | 9750 | 25571 | 35.07 | 91.99 | 50.79 | 0.089 | 0.080 | -0.005 | -0.010 |
| 0.50 | onset | 4875 | 12785 | 36.27 | 95.12 | 52.51 | 0.094 | 0.090 | 0.072 | 0.080 |
| 0.50 | offset | 4875 | 12786 | 36.70 | 96.27 | 53.15 | 0.102 | 0.090 | -0.087 | -0.090 |
| 0.50 | all | 9750 | 25571 | 36.49 | 95.69 | 52.83 | 0.098 | 0.090 | -0.008 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.13 | 16.39 | 11.27 | 11.70 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.82 | 21.18 | 15.56 | 17.83 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.04 | 16.69 | 10.02 | 11.25 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.76 | 25.33 | 17.86 | 20.06 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.67 | 24.24 | 16.19 | 16.38 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.13 | 12.75 | 9.90 | 8.99 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.94 | 27.83 | 24.96 | 24.37 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.33 | 16.80 | 10.77 | 10.89 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.14 | 16.89 | 12.18 | 12.72 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.91 | 22.89 | 18.08 | 18.59 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.25 | 22.67 | 13.66 | 17.07 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.78 | 17.10 | 12.47 | 13.11 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.41 | 16.32 | 4.08 | 3.92 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.05 | 15.23 | 2.46 | 2.89 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.03 | 18.14 | 3.17 | 4.43 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.63 | 13.58 | 1.46 | 1.45 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.44 | 14.09 | 2.45 | 2.27 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.32 | 17.43 | 3.03 | 3.06 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.05 | 15.96 | 4.26 | 4.14 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.55 | 13.25 | 2.56 | 2.51 | 2 | 2 |
