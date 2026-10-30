# Diarization scores: A-fa-r75b-seed43_s1750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b-seed43_s1750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s1750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T07:38:30+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b-seed43_s1750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7812-epoch=6.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.34 | 16.66 | 1.11 | 0.57 | 18.99 | 100.00 | 0.00 |
| 0.25 | 10.45 | 9.84 | 0.45 | 0.17 | 12.18 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.73 (IoU 89.71) | 9.22 (IoU 9.25) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 45.06) |

Speech P/R/F1: 99.69 / 89.97 / 94.58; miss 10.03 of ref speech, FA 3.24 of ref silence, SAD error 10.31.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12806 | 35.07 | 92.12 | 50.80 | 0.086 | 0.080 | 0.067 | 0.070 |
| 0.25 | offset | 4875 | 12806 | 34.80 | 91.41 | 50.40 | 0.091 | 0.090 | -0.078 | -0.080 |
| 0.25 | all | 9750 | 25612 | 34.93 | 91.76 | 50.60 | 0.088 | 0.080 | -0.005 | -0.010 |
| 0.50 | onset | 4875 | 12806 | 36.12 | 94.87 | 52.32 | 0.093 | 0.080 | 0.072 | 0.080 |
| 0.50 | offset | 4875 | 12806 | 36.56 | 96.04 | 52.96 | 0.102 | 0.090 | -0.087 | -0.090 |
| 0.50 | all | 9750 | 25612 | 36.34 | 95.46 | 52.64 | 0.098 | 0.090 | -0.008 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.23 | 16.52 | 11.36 | 11.82 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.96 | 21.22 | 15.88 | 18.05 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.08 | 16.70 | 10.13 | 11.41 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.90 | 25.43 | 17.94 | 20.10 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.79 | 24.36 | 16.32 | 16.49 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.18 | 12.81 | 9.97 | 9.05 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.17 | 28.05 | 25.23 | 24.65 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.39 | 16.82 | 10.87 | 10.97 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.14 | 16.86 | 12.18 | 12.71 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.99 | 22.90 | 18.18 | 18.67 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.31 | 22.72 | 13.63 | 17.03 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.76 | 17.09 | 12.45 | 13.09 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.56 | 16.47 | 4.22 | 4.05 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.13 | 15.31 | 2.54 | 2.99 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.21 | 18.41 | 3.45 | 4.81 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.75 | 13.69 | 1.60 | 1.59 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.46 | 14.15 | 2.46 | 2.30 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.51 | 17.62 | 3.16 | 3.20 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.31 | 16.23 | 4.52 | 4.41 | 2 | 2 |
| R8009_M8028__far_ch1 | 15.44 | 14.63 | 5.01 | 4.60 | 2 | 2 |
