# Diarization scores: A-fa_s250_blend_a50/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa_s250_blend_a50/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s250_blend_a50/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T08:37:06+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa_s250_blend_a50`
- model: `/mnt/data/exp/nemotron/20261029-nemotron-ft-ear1-step0/ckpts/A-fa_s250_blend_a50.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.08 | 16.60 | 0.95 | 0.53 | 18.76 | 100.00 | 0.00 |
| 0.25 | 10.13 | 9.69 | 0.28 | 0.15 | 11.91 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.93 (IoU 89.94) | 9.03 (IoU 9.05) |
| silence | 0.25 (IoU 0.27) | 7.79 (IoU 45.65) |

Speech P/R/F1: 99.70 / 90.18 / 94.70; miss 9.82 of ref speech, FA 3.07 of ref silence, SAD error 10.09.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12834 | 35.40 | 93.19 | 51.31 | 0.084 | 0.080 | 0.066 | 0.070 |
| 0.25 | offset | 4875 | 12834 | 35.20 | 92.66 | 51.01 | 0.090 | 0.080 | -0.079 | -0.080 |
| 0.25 | all | 9750 | 25668 | 35.30 | 92.92 | 51.16 | 0.087 | 0.080 | -0.006 | -0.010 |
| 0.50 | onset | 4875 | 12834 | 36.36 | 95.71 | 52.70 | 0.091 | 0.080 | 0.071 | 0.070 |
| 0.50 | offset | 4875 | 12834 | 36.79 | 96.84 | 53.32 | 0.099 | 0.090 | -0.086 | -0.080 |
| 0.50 | all | 9750 | 25668 | 36.57 | 96.28 | 53.01 | 0.095 | 0.090 | -0.008 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.32 | 16.56 | 11.37 | 11.81 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.02 | 21.25 | 15.63 | 17.80 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.09 | 16.81 | 10.03 | 11.33 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.91 | 25.44 | 17.92 | 19.97 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.00 | 24.58 | 16.32 | 16.52 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.31 | 12.92 | 10.00 | 9.09 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.24 | 28.07 | 25.24 | 24.66 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.44 | 16.89 | 10.81 | 10.95 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.02 | 16.72 | 11.99 | 12.50 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.87 | 22.68 | 18.10 | 18.47 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.18 | 22.50 | 13.62 | 17.04 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.47 | 16.72 | 12.26 | 12.84 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.70 | 15.63 | 3.68 | 3.54 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.63 | 14.70 | 2.18 | 2.52 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.45 | 17.40 | 2.63 | 3.68 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.20 | 13.15 | 1.22 | 1.22 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.16 | 13.78 | 2.32 | 2.14 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.04 | 17.15 | 2.99 | 3.04 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.42 | 15.32 | 3.78 | 3.65 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.09 | 12.84 | 2.14 | 2.12 | 2 | 2 |
