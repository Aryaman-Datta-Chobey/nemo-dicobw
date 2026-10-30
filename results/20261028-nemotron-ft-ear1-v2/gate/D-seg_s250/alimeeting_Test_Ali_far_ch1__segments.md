# Diarization scores: D-seg_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `D-seg_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-seg_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T18:36:22+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `D-seg_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7851-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 15.99 | 13.73 | 1.60 | 0.66 | 16.89 | 100.00 | 0.00 |
| 0.25 | 8.96 | 8.23 | 0.54 | 0.19 | 10.80 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 84.99 (IoU 91.96) | 6.97 (IoU 7.01) |
| silence | 0.46 (IoU 0.50) | 7.58 (IoU 50.48) |

Speech P/R/F1: 99.46 / 92.42 / 95.81; miss 7.58 of ref speech, FA 5.74 of ref silence, SAD error 8.09.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12367 | 37.36 | 94.77 | 53.59 | 0.068 | 0.060 | 0.027 | 0.030 |
| 0.25 | offset | 4875 | 12368 | 37.02 | 93.93 | 53.11 | 0.076 | 0.070 | -0.057 | -0.060 |
| 0.25 | all | 9750 | 24735 | 37.19 | 94.35 | 53.35 | 0.072 | 0.060 | -0.015 | -0.020 |
| 0.50 | onset | 4875 | 12367 | 37.93 | 96.23 | 54.41 | 0.072 | 0.060 | 0.030 | 0.030 |
| 0.50 | offset | 4875 | 12368 | 38.15 | 96.78 | 54.72 | 0.083 | 0.070 | -0.060 | -0.060 |
| 0.50 | all | 9750 | 24735 | 38.04 | 96.50 | 54.57 | 0.077 | 0.060 | -0.016 | -0.020 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 14.82 | 15.19 | 10.34 | 10.89 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.12 | 20.02 | 15.69 | 17.69 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.07 | 15.88 | 8.99 | 10.37 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.95 | 23.87 | 15.68 | 18.35 | 4 | 4 |
| R8005_M8007__far_ch1 | 22.55 | 23.20 | 14.82 | 15.05 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.27 | 12.06 | 8.82 | 8.11 | 4 | 4 |
| R8005_M8009__far_ch1 | 26.49 | 26.26 | 23.75 | 23.01 | 4 | 4 |
| R8006_M8012__far_ch1 | 15.52 | 16.13 | 9.83 | 10.06 | 4 | 4 |
| R8008_M8014__far_ch1 | 14.03 | 14.88 | 10.39 | 11.00 | 3 | 3 |
| R8008_M8015__far_ch1 | 20.11 | 21.28 | 16.48 | 17.16 | 3 | 3 |
| R8008_M8016__far_ch1 | 16.85 | 20.15 | 11.79 | 15.19 | 3 | 3 |
| R8008_M8017__far_ch1 | 13.89 | 15.21 | 10.57 | 11.23 | 3 | 3 |
| R8009_M8021__far_ch1 | 11.92 | 11.85 | 2.82 | 2.71 | 2 | 2 |
| R8009_M8022__far_ch1 | 10.76 | 11.73 | 1.44 | 1.78 | 2 | 2 |
| R8009_M8023__far_ch1 | 12.78 | 14.34 | 1.79 | 2.67 | 2 | 2 |
| R8009_M8024__far_ch1 | 10.06 | 9.93 | 0.80 | 0.80 | 2 | 2 |
| R8009_M8025__far_ch1 | 10.98 | 10.86 | 1.12 | 1.08 | 2 | 2 |
| R8009_M8026__far_ch1 | 13.72 | 13.80 | 2.10 | 2.14 | 2 | 2 |
| R8009_M8027__far_ch1 | 11.81 | 11.82 | 2.62 | 2.53 | 2 | 2 |
| R8009_M8028__far_ch1 | 10.23 | 9.98 | 1.47 | 1.43 | 2 | 2 |
