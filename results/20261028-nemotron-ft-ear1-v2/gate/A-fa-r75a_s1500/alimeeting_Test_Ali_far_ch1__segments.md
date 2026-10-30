# Diarization scores: A-fa-r75a_s1500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a_s1500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s1500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T00:15:17+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a_s1500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7874-epoch=5.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.19 | 16.61 | 1.01 | 0.57 | 18.88 | 100.00 | 0.00 |
| 0.25 | 10.26 | 9.79 | 0.30 | 0.17 | 12.03 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.74 (IoU 89.72) | 9.22 (IoU 9.25) |
| silence | 0.25 (IoU 0.28) | 7.79 (IoU 45.10) |

Speech P/R/F1: 99.69 / 89.97 / 94.58; miss 10.03 of ref speech, FA 3.16 of ref silence, SAD error 10.31.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12849 | 35.20 | 92.78 | 51.04 | 0.086 | 0.080 | 0.068 | 0.070 |
| 0.25 | offset | 4875 | 12849 | 34.89 | 91.96 | 50.59 | 0.092 | 0.090 | -0.079 | -0.080 |
| 0.25 | all | 9750 | 25698 | 35.05 | 92.37 | 50.81 | 0.089 | 0.080 | -0.005 | -0.000 |
| 0.50 | onset | 4875 | 12849 | 36.23 | 95.49 | 52.53 | 0.093 | 0.080 | 0.073 | 0.080 |
| 0.50 | offset | 4875 | 12849 | 36.64 | 96.57 | 53.13 | 0.102 | 0.090 | -0.087 | -0.090 |
| 0.50 | all | 9750 | 25698 | 36.43 | 96.03 | 52.83 | 0.098 | 0.090 | -0.008 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.26 | 16.55 | 11.45 | 11.91 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.61 | 20.88 | 15.39 | 17.54 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.14 | 16.81 | 10.16 | 11.44 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.89 | 25.47 | 17.89 | 19.99 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.73 | 24.29 | 16.30 | 16.46 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.27 | 12.87 | 10.08 | 9.15 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.16 | 28.08 | 25.22 | 24.66 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.31 | 16.78 | 10.87 | 10.99 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.20 | 16.92 | 12.25 | 12.79 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.92 | 22.79 | 18.17 | 18.58 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.30 | 22.68 | 13.71 | 17.11 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.67 | 17.00 | 12.47 | 13.11 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.28 | 16.19 | 3.96 | 3.81 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.23 | 15.43 | 2.52 | 2.96 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.16 | 18.29 | 3.24 | 4.56 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.66 | 13.59 | 1.47 | 1.46 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.36 | 14.09 | 2.34 | 2.23 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.16 | 17.27 | 2.96 | 2.99 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.08 | 16.00 | 4.25 | 4.14 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.40 | 13.12 | 2.29 | 2.26 | 2 | 2 |
