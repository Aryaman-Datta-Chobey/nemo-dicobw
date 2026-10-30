# Diarization scores: C-seg_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `C-seg_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-seg_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T17:39:48+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `C-seg_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7948-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 16.10 | 13.75 | 1.74 | 0.61 | 16.79 | 100.00 | 0.00 |
| 0.25 | 8.16 | 7.55 | 0.44 | 0.16 | 9.93 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 85.06 (IoU 91.85) | 6.90 (IoU 6.94) |
| silence | 0.65 (IoU 0.69) | 7.39 (IoU 49.50) |

Speech P/R/F1: 99.25 / 92.50 / 95.75; miss 7.50 of ref speech, FA 8.03 of ref silence, SAD error 8.20.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11613 | 39.28 | 93.58 | 55.34 | 0.086 | 0.080 | 0.042 | 0.050 |
| 0.25 | offset | 4875 | 11615 | 38.68 | 92.16 | 54.49 | 0.089 | 0.080 | -0.055 | -0.060 |
| 0.25 | all | 9750 | 23228 | 38.98 | 92.87 | 54.92 | 0.088 | 0.080 | -0.006 | -0.010 |
| 0.50 | onset | 4875 | 11613 | 40.05 | 95.41 | 56.42 | 0.091 | 0.080 | 0.044 | 0.050 |
| 0.50 | offset | 4875 | 11615 | 40.21 | 95.79 | 56.64 | 0.098 | 0.080 | -0.058 | -0.070 |
| 0.50 | all | 9750 | 23228 | 40.13 | 95.60 | 56.53 | 0.094 | 0.080 | -0.007 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.02 | 16.27 | 11.10 | 11.56 | 4 | 4 |
| R8002_M8003__far_ch1 | 18.10 | 19.23 | 13.38 | 15.40 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.64 | 16.24 | 9.63 | 10.88 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.65 | 24.31 | 16.26 | 18.70 | 4 | 4 |
| R8005_M8007__far_ch1 | 22.99 | 23.53 | 14.99 | 15.16 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.47 | 12.20 | 8.73 | 7.99 | 4 | 4 |
| R8005_M8009__far_ch1 | 26.66 | 26.62 | 23.70 | 23.21 | 4 | 4 |
| R8006_M8012__far_ch1 | 15.63 | 15.97 | 9.18 | 9.20 | 4 | 4 |
| R8008_M8014__far_ch1 | 12.17 | 12.70 | 7.52 | 7.82 | 3 | 3 |
| R8008_M8015__far_ch1 | 12.70 | 14.42 | 6.97 | 7.83 | 3 | 3 |
| R8008_M8016__far_ch1 | 17.57 | 20.99 | 11.88 | 15.01 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.66 | 13.79 | 7.74 | 8.43 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.04 | 14.98 | 3.57 | 3.44 | 2 | 2 |
| R8009_M8022__far_ch1 | 11.64 | 12.53 | 1.53 | 1.86 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.32 | 16.28 | 2.13 | 2.99 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.35 | 12.25 | 0.97 | 0.96 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.56 | 13.08 | 1.90 | 1.67 | 2 | 2 |
| R8009_M8026__far_ch1 | 13.64 | 13.83 | 1.75 | 1.78 | 2 | 2 |
| R8009_M8027__far_ch1 | 8.60 | 8.42 | 1.17 | 1.13 | 2 | 2 |
| R8009_M8028__far_ch1 | 10.78 | 10.64 | 1.11 | 1.13 | 2 | 2 |
