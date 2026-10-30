# Diarization scores: A-fa-r75b-seed43_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b-seed43_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T06:40:57+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b-seed43_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7797-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.05 | 16.49 | 1.02 | 0.54 | 18.72 | 100.00 | 0.00 |
| 0.25 | 10.11 | 9.62 | 0.34 | 0.16 | 11.87 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.91 (IoU 89.92) | 9.05 (IoU 9.07) |
| silence | 0.25 (IoU 0.28) | 7.79 (IoU 45.59) |

Speech P/R/F1: 99.70 / 90.16 / 94.69; miss 9.84 of ref speech, FA 3.12 of ref silence, SAD error 10.11.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12864 | 35.49 | 93.66 | 51.48 | 0.084 | 0.080 | 0.066 | 0.070 |
| 0.25 | offset | 4875 | 12864 | 35.18 | 92.82 | 51.02 | 0.091 | 0.080 | -0.080 | -0.080 |
| 0.25 | all | 9750 | 25728 | 35.34 | 93.24 | 51.25 | 0.088 | 0.080 | -0.006 | -0.010 |
| 0.50 | onset | 4875 | 12864 | 36.37 | 95.96 | 52.74 | 0.091 | 0.080 | 0.070 | 0.070 |
| 0.50 | offset | 4875 | 12864 | 36.74 | 96.94 | 53.28 | 0.101 | 0.090 | -0.087 | -0.090 |
| 0.50 | all | 9750 | 25728 | 36.55 | 96.45 | 53.01 | 0.096 | 0.090 | -0.008 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.36 | 16.61 | 11.37 | 11.83 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.98 | 21.24 | 15.60 | 17.79 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.96 | 16.61 | 9.98 | 11.24 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.63 | 25.22 | 17.54 | 19.67 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.98 | 24.53 | 16.27 | 16.44 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.21 | 12.85 | 9.90 | 9.01 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.88 | 27.70 | 24.83 | 24.23 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.24 | 16.67 | 10.64 | 10.75 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.05 | 16.68 | 12.00 | 12.46 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.90 | 22.73 | 18.08 | 18.43 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.35 | 22.64 | 13.70 | 17.09 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.48 | 16.73 | 12.29 | 12.87 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.87 | 15.80 | 3.73 | 3.59 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.46 | 14.53 | 2.13 | 2.48 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.45 | 17.41 | 2.70 | 3.74 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.28 | 13.22 | 1.24 | 1.24 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.28 | 13.91 | 2.39 | 2.20 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.91 | 17.05 | 2.97 | 3.03 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.46 | 15.37 | 3.74 | 3.61 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.81 | 13.38 | 2.99 | 2.87 | 2 | 2 |
