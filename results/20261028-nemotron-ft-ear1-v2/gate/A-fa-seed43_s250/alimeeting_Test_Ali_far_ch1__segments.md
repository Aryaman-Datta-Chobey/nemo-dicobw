# Diarization scores: A-fa-seed43_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-seed43_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-seed43_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T14:53:20+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-seed43_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7790-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.90 | 16.49 | 0.92 | 0.50 | 18.62 | 100.00 | 0.00 |
| 0.25 | 9.93 | 9.49 | 0.28 | 0.15 | 11.73 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.26 (IoU 90.29) | 8.70 (IoU 8.72) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 46.47) |

Speech P/R/F1: 99.69 / 90.54 / 94.89; miss 9.46 of ref speech, FA 3.25 of ref silence, SAD error 9.74.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12745 | 35.93 | 93.93 | 51.98 | 0.089 | 0.090 | 0.073 | 0.080 |
| 0.25 | offset | 4875 | 12745 | 36.12 | 94.42 | 52.25 | 0.083 | 0.070 | -0.068 | -0.070 |
| 0.25 | all | 9750 | 25490 | 36.02 | 94.17 | 52.11 | 0.086 | 0.080 | 0.002 | 0.000 |
| 0.50 | onset | 4875 | 12745 | 36.90 | 96.47 | 53.38 | 0.095 | 0.090 | 0.077 | 0.080 |
| 0.50 | offset | 4875 | 12745 | 37.20 | 97.25 | 53.81 | 0.090 | 0.080 | -0.073 | -0.070 |
| 0.50 | all | 9750 | 25490 | 37.05 | 96.86 | 53.60 | 0.092 | 0.080 | 0.002 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.76 | 16.96 | 11.42 | 11.85 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.01 | 21.28 | 15.47 | 17.63 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.03 | 16.73 | 9.98 | 11.31 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.63 | 25.20 | 17.51 | 19.48 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.43 | 24.94 | 16.55 | 16.70 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.30 | 12.92 | 9.87 | 9.03 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.71 | 28.54 | 25.41 | 24.84 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.32 | 16.70 | 10.61 | 10.72 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.70 | 16.36 | 11.58 | 12.07 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.43 | 22.24 | 17.51 | 17.97 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.49 | 22.93 | 13.49 | 16.90 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.30 | 16.56 | 12.12 | 12.67 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.30 | 15.25 | 3.50 | 3.37 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.66 | 13.69 | 1.76 | 2.12 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.63 | 16.41 | 2.07 | 2.81 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.67 | 12.59 | 0.93 | 0.92 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.24 | 14.03 | 2.59 | 2.71 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.19 | 16.32 | 2.53 | 2.57 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.32 | 14.24 | 3.10 | 2.98 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.46 | 12.21 | 1.91 | 1.89 | 2 | 2 |
