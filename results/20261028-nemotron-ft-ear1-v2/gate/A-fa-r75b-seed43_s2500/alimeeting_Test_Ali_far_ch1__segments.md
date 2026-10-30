# Diarization scores: A-fa-r75b-seed43_s2500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b-seed43_s2500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s2500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T08:07:13+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b-seed43_s2500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7955-epoch=9.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.20 | 16.57 | 1.05 | 0.58 | 18.90 | 100.00 | 0.00 |
| 0.25 | 10.28 | 9.77 | 0.33 | 0.18 | 12.07 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.75 (IoU 89.73) | 9.21 (IoU 9.24) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 45.10) |

Speech P/R/F1: 99.69 / 89.98 / 94.59; miss 10.02 of ref speech, FA 3.24 of ref silence, SAD error 10.30.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12863 | 35.12 | 92.66 | 50.93 | 0.087 | 0.080 | 0.068 | 0.070 |
| 0.25 | offset | 4875 | 12863 | 34.83 | 91.90 | 50.51 | 0.090 | 0.090 | -0.078 | -0.080 |
| 0.25 | all | 9750 | 25726 | 34.97 | 92.28 | 50.72 | 0.089 | 0.080 | -0.005 | -0.010 |
| 0.50 | onset | 4875 | 12863 | 36.17 | 95.43 | 52.45 | 0.095 | 0.090 | 0.073 | 0.080 |
| 0.50 | offset | 4875 | 12863 | 36.55 | 96.45 | 53.02 | 0.101 | 0.090 | -0.086 | -0.090 |
| 0.50 | all | 9750 | 25726 | 36.36 | 95.94 | 52.73 | 0.098 | 0.090 | -0.007 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.27 | 16.54 | 11.48 | 11.93 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.81 | 21.13 | 15.68 | 17.88 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.17 | 16.83 | 10.16 | 11.46 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.91 | 25.53 | 18.03 | 20.29 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.79 | 24.37 | 16.29 | 16.47 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.26 | 12.86 | 10.03 | 9.12 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.18 | 27.98 | 25.23 | 24.59 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.34 | 16.78 | 10.80 | 10.88 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.11 | 16.86 | 12.20 | 12.72 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.03 | 22.97 | 18.28 | 18.74 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.17 | 22.54 | 13.62 | 17.03 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.76 | 17.10 | 12.49 | 13.14 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.38 | 16.28 | 4.05 | 3.89 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.94 | 15.13 | 2.40 | 2.85 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.20 | 18.36 | 3.27 | 4.62 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.85 | 13.79 | 1.64 | 1.64 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.42 | 14.07 | 2.42 | 2.23 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.20 | 17.29 | 2.89 | 2.91 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.86 | 15.77 | 4.15 | 4.03 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.30 | 13.03 | 2.30 | 2.27 | 2 | 2 |
