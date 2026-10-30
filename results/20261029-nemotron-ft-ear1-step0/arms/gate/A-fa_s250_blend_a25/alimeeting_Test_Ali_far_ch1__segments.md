# Diarization scores: A-fa_s250_blend_a25/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa_s250_blend_a25/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s250_blend_a25/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T08:27:21+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa_s250_blend_a25`
- model: `/mnt/data/exp/nemotron/20261029-nemotron-ft-ear1-step0/ckpts/A-fa_s250_blend_a25.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.09 | 16.60 | 0.96 | 0.53 | 18.76 | 100.00 | 0.00 |
| 0.25 | 10.12 | 9.68 | 0.29 | 0.15 | 11.90 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.89 (IoU 89.89) | 9.07 (IoU 9.09) |
| silence | 0.25 (IoU 0.27) | 7.79 (IoU 45.55) |

Speech P/R/F1: 99.70 / 90.14 / 94.68; miss 9.86 of ref speech, FA 3.06 of ref silence, SAD error 10.13.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12864 | 35.33 | 93.23 | 51.24 | 0.084 | 0.080 | 0.065 | 0.070 |
| 0.25 | offset | 4875 | 12864 | 35.06 | 92.51 | 50.85 | 0.091 | 0.080 | -0.080 | -0.080 |
| 0.25 | all | 9750 | 25728 | 35.20 | 92.87 | 51.05 | 0.087 | 0.080 | -0.007 | -0.010 |
| 0.50 | onset | 4875 | 12864 | 36.32 | 95.84 | 52.67 | 0.091 | 0.080 | 0.070 | 0.070 |
| 0.50 | offset | 4875 | 12864 | 36.70 | 96.84 | 53.23 | 0.101 | 0.090 | -0.087 | -0.090 |
| 0.50 | all | 9750 | 25728 | 36.51 | 96.34 | 52.95 | 0.096 | 0.090 | -0.009 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.28 | 16.53 | 11.39 | 11.83 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.00 | 21.21 | 15.63 | 17.77 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.10 | 16.77 | 10.02 | 11.29 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.94 | 25.45 | 17.90 | 19.97 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.04 | 24.62 | 16.34 | 16.54 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.34 | 12.92 | 10.03 | 9.09 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.19 | 28.02 | 25.10 | 24.49 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.33 | 16.78 | 10.75 | 10.85 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.92 | 16.59 | 11.91 | 12.39 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.79 | 22.57 | 18.02 | 18.38 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.19 | 22.49 | 13.66 | 17.07 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.46 | 16.73 | 12.24 | 12.83 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.77 | 15.70 | 3.70 | 3.57 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.71 | 14.79 | 2.21 | 2.56 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.54 | 17.51 | 2.70 | 3.79 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.30 | 13.25 | 1.24 | 1.24 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.22 | 13.85 | 2.32 | 2.14 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.12 | 17.23 | 3.02 | 3.07 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.49 | 15.40 | 3.81 | 3.68 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.17 | 12.91 | 2.18 | 2.15 | 2 | 2 |
