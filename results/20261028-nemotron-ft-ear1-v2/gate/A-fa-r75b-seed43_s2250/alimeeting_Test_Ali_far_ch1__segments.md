# Diarization scores: A-fa-r75b-seed43_s2250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b-seed43_s2250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s2250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T07:57:35+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b-seed43_s2250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7882-epoch=8.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.22 | 16.62 | 1.02 | 0.58 | 18.91 | 100.00 | 0.00 |
| 0.25 | 10.26 | 9.79 | 0.30 | 0.17 | 12.04 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.74 (IoU 89.72) | 9.22 (IoU 9.24) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 45.08) |

Speech P/R/F1: 99.69 / 89.98 / 94.58; miss 10.02 of ref speech, FA 3.24 of ref silence, SAD error 10.31.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12852 | 35.12 | 92.57 | 50.92 | 0.087 | 0.080 | 0.068 | 0.070 |
| 0.25 | offset | 4875 | 12853 | 34.83 | 91.84 | 50.51 | 0.091 | 0.090 | -0.079 | -0.080 |
| 0.25 | all | 9750 | 25705 | 34.97 | 92.21 | 50.71 | 0.089 | 0.080 | -0.005 | -0.010 |
| 0.50 | onset | 4875 | 12852 | 36.18 | 95.38 | 52.46 | 0.094 | 0.090 | 0.073 | 0.080 |
| 0.50 | offset | 4875 | 12853 | 36.57 | 96.41 | 53.02 | 0.101 | 0.090 | -0.086 | -0.090 |
| 0.50 | all | 9750 | 25705 | 36.37 | 95.90 | 52.74 | 0.098 | 0.090 | -0.007 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.22 | 16.48 | 11.44 | 11.89 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.65 | 20.99 | 15.41 | 17.61 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.18 | 16.83 | 10.16 | 11.44 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.84 | 25.36 | 17.91 | 20.01 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.88 | 24.47 | 16.36 | 16.56 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.22 | 12.82 | 9.96 | 9.02 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.30 | 28.19 | 25.27 | 24.70 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.43 | 16.86 | 10.92 | 11.05 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.24 | 16.94 | 12.30 | 12.80 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.13 | 23.07 | 18.34 | 18.76 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.18 | 22.56 | 13.62 | 17.03 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.82 | 17.14 | 12.53 | 13.16 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.40 | 16.30 | 4.06 | 3.90 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.98 | 15.18 | 2.40 | 2.85 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.01 | 18.14 | 3.11 | 4.39 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.84 | 13.78 | 1.59 | 1.59 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.39 | 14.05 | 2.37 | 2.19 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.23 | 17.32 | 2.89 | 2.91 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.87 | 15.78 | 4.11 | 3.98 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.36 | 13.13 | 2.23 | 2.23 | 2 | 2 |
