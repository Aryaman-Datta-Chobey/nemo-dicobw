# Diarization scores: C-seg_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `C-seg_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-seg_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T18:01:50+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `C-seg_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8148-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 16.85 | 14.48 | 1.77 | 0.60 | 17.38 | 100.00 | 0.00 |
| 0.25 | 8.98 | 8.15 | 0.65 | 0.18 | 10.57 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 84.30 (IoU 91.10) | 7.66 (IoU 7.70) |
| silence | 0.58 (IoU 0.63) | 7.46 (IoU 47.54) |

Speech P/R/F1: 99.32 / 91.67 / 95.34; miss 8.33 of ref speech, FA 7.20 of ref silence, SAD error 8.96.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11905 | 37.55 | 91.69 | 53.28 | 0.086 | 0.080 | 0.048 | 0.060 |
| 0.25 | offset | 4875 | 11906 | 37.15 | 90.73 | 52.71 | 0.092 | 0.090 | -0.058 | -0.070 |
| 0.25 | all | 9750 | 23811 | 37.35 | 91.21 | 53.00 | 0.089 | 0.080 | -0.004 | -0.010 |
| 0.50 | onset | 4875 | 11905 | 38.57 | 94.19 | 54.73 | 0.093 | 0.080 | 0.051 | 0.060 |
| 0.50 | offset | 4875 | 11906 | 39.04 | 95.34 | 55.40 | 0.103 | 0.090 | -0.064 | -0.070 |
| 0.50 | all | 9750 | 23811 | 38.81 | 94.77 | 55.06 | 0.098 | 0.090 | -0.007 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.66 | 16.99 | 11.28 | 11.77 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.85 | 18.97 | 12.85 | 14.97 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.78 | 16.37 | 9.90 | 11.17 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.30 | 23.79 | 16.26 | 18.39 | 4 | 4 |
| R8005_M8007__far_ch1 | 22.87 | 23.51 | 15.45 | 15.71 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.73 | 12.40 | 9.39 | 8.59 | 4 | 4 |
| R8005_M8009__far_ch1 | 26.89 | 26.75 | 23.96 | 23.40 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.31 | 16.67 | 10.77 | 10.83 | 4 | 4 |
| R8008_M8014__far_ch1 | 14.81 | 15.43 | 10.73 | 11.15 | 3 | 3 |
| R8008_M8015__far_ch1 | 15.19 | 16.45 | 10.58 | 11.24 | 3 | 3 |
| R8008_M8016__far_ch1 | 17.22 | 20.37 | 11.77 | 14.60 | 3 | 3 |
| R8008_M8017__far_ch1 | 11.11 | 11.99 | 4.86 | 5.49 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.81 | 15.74 | 3.78 | 3.65 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.33 | 14.42 | 2.16 | 2.56 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.57 | 17.45 | 2.93 | 3.82 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.10 | 13.05 | 1.25 | 1.26 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.69 | 14.23 | 2.77 | 2.54 | 2 | 2 |
| R8009_M8026__far_ch1 | 15.45 | 15.68 | 2.49 | 2.59 | 2 | 2 |
| R8009_M8027__far_ch1 | 9.45 | 9.29 | 1.97 | 1.95 | 2 | 2 |
| R8009_M8028__far_ch1 | 15.33 | 14.17 | 6.13 | 5.41 | 2 | 2 |
