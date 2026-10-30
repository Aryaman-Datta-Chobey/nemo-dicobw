# Diarization scores: A-fa_s250_blend_a75/alimeeting_Test_Ali_far_ch1

- name: `A-fa_s250_blend_a75/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s250_blend_a75/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T08:46:56+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa_s250_blend_a75`
- model: `/mnt/data/exp/nemotron/20261029-nemotron-ft-ear1-step0/ckpts/A-fa_s250_blend_a75.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.42 | 5.52 | 4.24 | 0.67 | 11.00 | 100.00 | 0.00 |
| 0.25 | 1.51 | 0.88 | 0.58 | 0.05 | 2.30 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.22 (IoU 95.42) | 1.79 (IoU 1.83) |
| silence | 2.11 (IoU 2.15) | 14.88 (IoU 79.23) |

Speech P/R/F1: 97.46 / 97.84 / 97.65; miss 2.16 of ref speech, FA 12.43 of ref silence, SAD error 4.70.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12797 | 93.11 | 90.93 | 92.01 | 0.042 | 0.030 | 0.004 | 0.010 |
| 0.25 | offset | 13103 | 12797 | 93.33 | 91.15 | 92.23 | 0.046 | 0.040 | 0.012 | 0.020 |
| 0.25 | all | 26206 | 25594 | 93.22 | 91.04 | 92.12 | 0.044 | 0.030 | 0.008 | 0.010 |
| 0.50 | onset | 13103 | 12797 | 93.92 | 91.73 | 92.81 | 0.045 | 0.030 | 0.005 | 0.010 |
| 0.50 | offset | 13103 | 12797 | 94.09 | 91.89 | 92.98 | 0.049 | 0.040 | 0.012 | 0.020 |
| 0.50 | all | 26206 | 25594 | 94.01 | 91.81 | 92.90 | 0.047 | 0.030 | 0.008 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.31 | 10.56 | 1.05 | 1.24 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.62 | 12.21 | 1.76 | 2.79 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.86 | 10.08 | 1.23 | 1.59 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.59 | 21.98 | 4.98 | 7.24 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.61 | 19.65 | 2.73 | 2.93 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.26 | 7.28 | 1.54 | 1.65 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.74 | 18.76 | 7.62 | 7.41 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.03 | 10.53 | 1.82 | 1.95 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.13 | 7.82 | 0.70 | 0.82 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.36 | 10.48 | 1.81 | 2.06 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.60 | 10.17 | 1.16 | 2.18 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.02 | 5.91 | 0.36 | 0.47 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.44 | 8.01 | 0.50 | 0.50 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.21 | 6.81 | 0.91 | 1.12 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.84 | 10.90 | 0.72 | 0.90 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.55 | 4.48 | 0.45 | 0.45 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.63 | 7.18 | 0.66 | 0.58 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.78 | 7.61 | 0.89 | 1.01 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.44 | 5.25 | 1.35 | 1.29 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.12 | 5.97 | 1.20 | 1.19 | 2 | 2 |
