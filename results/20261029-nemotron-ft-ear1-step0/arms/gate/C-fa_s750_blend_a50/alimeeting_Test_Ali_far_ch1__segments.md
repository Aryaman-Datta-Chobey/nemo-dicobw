# Diarization scores: C-fa_s750_blend_a50/alimeeting_Test_Ali_far_ch1__segments

- name: `C-fa_s750_blend_a50/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-fa_s750_blend_a50/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T08:57:27+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `C-fa_s750_blend_a50`
- model: `/mnt/data/exp/nemotron/20261029-nemotron-ft-ear1-step0/ckpts/C-fa_s750_blend_a50.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.16 | 16.68 | 0.95 | 0.53 | 18.86 | 100.00 | 0.00 |
| 0.25 | 10.24 | 9.77 | 0.30 | 0.16 | 12.04 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.93 (IoU 89.93) | 9.03 (IoU 9.05) |
| silence | 0.25 (IoU 0.28) | 7.79 (IoU 45.63) |

Speech P/R/F1: 99.70 / 90.18 / 94.70; miss 9.82 of ref speech, FA 3.12 of ref silence, SAD error 10.09.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12888 | 35.11 | 92.82 | 50.95 | 0.083 | 0.080 | 0.065 | 0.070 |
| 0.25 | offset | 4875 | 12888 | 34.94 | 92.37 | 50.70 | 0.089 | 0.080 | -0.077 | -0.080 |
| 0.25 | all | 9750 | 25776 | 35.02 | 92.59 | 50.82 | 0.086 | 0.080 | -0.006 | -0.010 |
| 0.50 | onset | 4875 | 12888 | 36.13 | 95.53 | 52.43 | 0.090 | 0.080 | 0.071 | 0.070 |
| 0.50 | offset | 4875 | 12888 | 36.58 | 96.72 | 53.09 | 0.099 | 0.090 | -0.084 | -0.080 |
| 0.50 | all | 9750 | 25776 | 36.36 | 96.12 | 52.76 | 0.095 | 0.080 | -0.007 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.54 | 16.79 | 11.57 | 12.02 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.92 | 21.27 | 15.56 | 17.80 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.12 | 16.84 | 10.14 | 11.46 | 4 | 4 |
| R8004_M8006__far_ch1 | 23.08 | 25.59 | 18.16 | 20.19 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.08 | 24.64 | 16.47 | 16.66 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.39 | 13.00 | 10.06 | 9.17 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.71 | 28.57 | 25.63 | 25.05 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.43 | 16.90 | 10.90 | 11.05 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.14 | 16.91 | 12.10 | 12.67 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.01 | 22.87 | 18.17 | 18.56 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.07 | 22.39 | 13.53 | 16.94 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.45 | 16.75 | 12.30 | 12.92 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.60 | 15.53 | 3.66 | 3.52 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.78 | 14.90 | 2.30 | 2.66 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.39 | 17.41 | 2.69 | 3.78 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.09 | 13.03 | 1.21 | 1.21 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.94 | 13.55 | 2.24 | 2.05 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.16 | 17.30 | 3.13 | 3.21 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.45 | 15.37 | 3.92 | 3.80 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.35 | 13.01 | 2.56 | 2.49 | 2 | 2 |
