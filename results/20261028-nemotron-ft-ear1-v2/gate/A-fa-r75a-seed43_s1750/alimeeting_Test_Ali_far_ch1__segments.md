# Diarization scores: A-fa-r75a-seed43_s1750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a-seed43_s1750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s1750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T05:17:19+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a-seed43_s1750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7849-epoch=6.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.29 | 16.72 | 1.01 | 0.57 | 18.97 | 100.00 | 0.00 |
| 0.25 | 10.29 | 9.84 | 0.28 | 0.17 | 12.06 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.67 (IoU 89.64) | 9.29 (IoU 9.32) |
| silence | 0.26 (IoU 0.28) | 7.78 (IoU 44.90) |

Speech P/R/F1: 99.69 / 89.89 / 94.54; miss 10.11 of ref speech, FA 3.20 of ref silence, SAD error 10.39.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12836 | 34.96 | 92.04 | 50.67 | 0.086 | 0.080 | 0.066 | 0.070 |
| 0.25 | offset | 4875 | 12836 | 34.64 | 91.22 | 50.22 | 0.092 | 0.090 | -0.081 | -0.090 |
| 0.25 | all | 9750 | 25672 | 34.80 | 91.63 | 50.44 | 0.089 | 0.080 | -0.007 | -0.010 |
| 0.50 | onset | 4875 | 12836 | 36.05 | 94.93 | 52.26 | 0.094 | 0.090 | 0.072 | 0.080 |
| 0.50 | offset | 4875 | 12836 | 36.49 | 96.08 | 52.89 | 0.104 | 0.090 | -0.090 | -0.090 |
| 0.50 | all | 9750 | 25672 | 36.27 | 95.51 | 52.58 | 0.099 | 0.090 | -0.009 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.06 | 16.33 | 11.40 | 11.86 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.60 | 20.91 | 15.45 | 17.61 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.18 | 16.81 | 10.17 | 11.46 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.98 | 25.56 | 17.92 | 20.03 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.85 | 24.42 | 16.24 | 16.40 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.28 | 12.90 | 10.02 | 9.09 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.28 | 28.15 | 25.25 | 24.69 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.32 | 16.77 | 10.81 | 10.90 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.12 | 16.87 | 12.14 | 12.66 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.02 | 22.97 | 18.13 | 18.60 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.16 | 22.56 | 13.59 | 17.02 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.74 | 17.06 | 12.46 | 13.09 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.58 | 16.49 | 4.10 | 3.94 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.41 | 15.61 | 2.59 | 3.04 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.63 | 18.72 | 3.55 | 4.86 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.06 | 14.00 | 1.71 | 1.71 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.46 | 14.15 | 2.36 | 2.21 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.59 | 17.69 | 3.22 | 3.27 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.28 | 16.20 | 4.41 | 4.30 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.54 | 13.29 | 2.33 | 2.30 | 2 | 2 |
