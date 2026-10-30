# Diarization scores: A-fa_s250_blend_a75/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa_s250_blend_a75/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s250_blend_a75/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T08:47:00+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa_s250_blend_a75`
- model: `/mnt/data/exp/nemotron/20261029-nemotron-ft-ear1-step0/ckpts/A-fa_s250_blend_a75.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.95 | 16.49 | 0.94 | 0.51 | 18.64 | 100.00 | 0.00 |
| 0.25 | 10.01 | 9.58 | 0.28 | 0.15 | 11.80 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.08 (IoU 90.09) | 8.88 (IoU 8.91) |
| silence | 0.25 (IoU 0.28) | 7.79 (IoU 46.02) |

Speech P/R/F1: 99.70 / 90.34 / 94.79; miss 9.66 of ref speech, FA 3.14 of ref silence, SAD error 9.93.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12797 | 35.62 | 93.50 | 51.58 | 0.087 | 0.080 | 0.071 | 0.080 |
| 0.25 | offset | 4875 | 12797 | 35.71 | 93.74 | 51.72 | 0.086 | 0.080 | -0.072 | -0.075 |
| 0.25 | all | 9750 | 25594 | 35.66 | 93.62 | 51.65 | 0.086 | 0.080 | -0.001 | 0.000 |
| 0.50 | onset | 4875 | 12797 | 36.61 | 96.10 | 53.02 | 0.094 | 0.090 | 0.076 | 0.080 |
| 0.50 | offset | 4875 | 12797 | 37.00 | 97.13 | 53.59 | 0.094 | 0.080 | -0.078 | -0.080 |
| 0.50 | all | 9750 | 25594 | 36.81 | 96.62 | 53.30 | 0.094 | 0.080 | -0.001 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.54 | 16.80 | 11.34 | 11.79 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.06 | 21.30 | 15.60 | 17.74 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.02 | 16.68 | 10.01 | 11.29 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.75 | 25.33 | 17.75 | 19.83 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.01 | 24.58 | 16.36 | 16.53 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.25 | 12.85 | 9.93 | 9.03 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.25 | 28.08 | 25.13 | 24.57 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.39 | 16.77 | 10.79 | 10.87 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.99 | 16.69 | 11.91 | 12.40 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.72 | 22.39 | 17.94 | 18.28 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.27 | 22.63 | 13.57 | 16.99 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.30 | 16.55 | 12.12 | 12.68 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.54 | 15.48 | 3.63 | 3.50 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.20 | 14.21 | 2.00 | 2.32 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.06 | 16.89 | 2.30 | 3.18 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.91 | 12.86 | 1.05 | 1.05 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.02 | 13.59 | 2.29 | 2.08 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.68 | 16.79 | 2.78 | 2.82 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.84 | 14.74 | 3.37 | 3.25 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.67 | 12.45 | 1.91 | 1.90 | 2 | 2 |
