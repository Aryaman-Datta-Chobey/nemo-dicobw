# Diarization scores: C-fa_s750_blend_a50/alimeeting_Test_Ali_far_ch1

- name: `C-fa_s750_blend_a50/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-fa_s750_blend_a50/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T08:57:22+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `C-fa_s750_blend_a50`
- model: `/mnt/data/exp/nemotron/20261029-nemotron-ft-ear1-step0/ckpts/C-fa_s750_blend_a50.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.47 | 5.64 | 4.15 | 0.68 | 11.08 | 100.00 | 0.00 |
| 0.25 | 1.65 | 0.98 | 0.61 | 0.07 | 2.45 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.13 (IoU 95.38) | 1.88 (IoU 1.92) |
| silence | 2.05 (IoU 2.09) | 14.94 (IoU 79.19) |

Speech P/R/F1: 97.54 / 97.74 / 97.64; miss 2.26 of ref speech, FA 12.06 of ref silence, SAD error 4.73.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12888 | 92.53 | 91.01 | 91.76 | 0.041 | 0.030 | -0.001 | 0.000 |
| 0.25 | offset | 13103 | 12888 | 92.74 | 91.22 | 91.97 | 0.045 | 0.030 | 0.006 | 0.010 |
| 0.25 | all | 26206 | 25776 | 92.63 | 91.11 | 91.87 | 0.043 | 0.030 | 0.003 | 0.010 |
| 0.50 | onset | 13103 | 12888 | 93.40 | 91.86 | 92.62 | 0.044 | 0.030 | 0.000 | 0.000 |
| 0.50 | offset | 13103 | 12888 | 93.60 | 92.06 | 92.82 | 0.048 | 0.030 | 0.006 | 0.010 |
| 0.50 | all | 26206 | 25776 | 93.50 | 91.96 | 92.72 | 0.046 | 0.030 | 0.003 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.86 | 10.14 | 1.17 | 1.38 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.51 | 12.20 | 1.79 | 3.00 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.94 | 10.18 | 1.32 | 1.69 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.67 | 22.08 | 5.24 | 7.42 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.56 | 19.60 | 2.73 | 2.96 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.32 | 7.38 | 1.58 | 1.70 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.94 | 19.03 | 7.79 | 7.54 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.02 | 10.56 | 1.96 | 2.16 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.01 | 7.74 | 0.78 | 0.92 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.47 | 10.85 | 1.95 | 2.29 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.59 | 10.08 | 1.25 | 2.22 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.21 | 6.12 | 0.54 | 0.69 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.76 | 7.39 | 0.51 | 0.51 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.32 | 6.95 | 1.05 | 1.27 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.70 | 11.98 | 0.79 | 1.00 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.49 | 4.41 | 0.59 | 0.58 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.18 | 6.80 | 0.66 | 0.58 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.45 | 8.25 | 1.00 | 1.13 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.92 | 5.71 | 1.73 | 1.66 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.66 | 6.42 | 1.82 | 1.76 | 2 | 2 |
