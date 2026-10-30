# Diarization scores: A-fa_s250_blend_a25/alimeeting_Test_Ali_far_ch1

- name: `A-fa_s250_blend_a25/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s250_blend_a25/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T08:27:16+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa_s250_blend_a25`
- model: `/mnt/data/exp/nemotron/20261029-nemotron-ft-ear1-step0/ckpts/A-fa_s250_blend_a25.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.40 | 5.55 | 4.17 | 0.68 | 10.98 | 100.00 | 0.00 |
| 0.25 | 1.58 | 0.94 | 0.58 | 0.06 | 2.36 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.13 (IoU 95.44) | 1.87 (IoU 1.91) |
| silence | 2.00 (IoU 2.04) | 14.99 (IoU 79.45) |

Speech P/R/F1: 97.59 / 97.74 / 97.67; miss 2.26 of ref speech, FA 11.79 of ref silence, SAD error 4.67.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12864 | 92.68 | 90.99 | 91.82 | 0.042 | 0.030 | -0.001 | 0.000 |
| 0.25 | offset | 13103 | 12864 | 92.84 | 91.15 | 91.99 | 0.044 | 0.030 | 0.003 | 0.010 |
| 0.25 | all | 26206 | 25728 | 92.76 | 91.07 | 91.91 | 0.043 | 0.030 | 0.001 | 0.010 |
| 0.50 | onset | 13103 | 12864 | 93.55 | 91.84 | 92.69 | 0.044 | 0.030 | -0.001 | 0.000 |
| 0.50 | offset | 13103 | 12864 | 93.70 | 91.99 | 92.84 | 0.047 | 0.030 | 0.004 | 0.010 |
| 0.50 | all | 26206 | 25728 | 93.63 | 91.92 | 92.76 | 0.046 | 0.030 | 0.002 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.64 | 9.93 | 1.06 | 1.25 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.45 | 12.00 | 1.75 | 2.77 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.08 | 10.29 | 1.26 | 1.62 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.80 | 22.17 | 5.11 | 7.41 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.83 | 19.87 | 2.79 | 3.07 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.36 | 7.36 | 1.61 | 1.71 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.76 | 18.79 | 7.65 | 7.38 | 4 | 4 |
| R8006_M8012__far_ch1 | 9.94 | 10.51 | 1.78 | 1.94 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.94 | 7.64 | 0.71 | 0.84 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.23 | 10.45 | 1.86 | 2.13 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.38 | 9.85 | 1.25 | 2.23 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.16 | 6.06 | 0.42 | 0.54 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.58 | 7.24 | 0.55 | 0.54 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.09 | 6.71 | 1.02 | 1.24 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.57 | 11.89 | 0.78 | 0.97 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.35 | 4.27 | 0.57 | 0.57 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.26 | 6.92 | 0.67 | 0.59 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.20 | 8.00 | 0.97 | 1.10 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.74 | 5.55 | 1.59 | 1.52 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.24 | 6.08 | 1.40 | 1.38 | 2 | 2 |
