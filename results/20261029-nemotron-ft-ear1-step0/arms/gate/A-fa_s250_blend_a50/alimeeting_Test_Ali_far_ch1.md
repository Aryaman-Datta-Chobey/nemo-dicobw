# Diarization scores: A-fa_s250_blend_a50/alimeeting_Test_Ali_far_ch1

- name: `A-fa_s250_blend_a50/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s250_blend_a50/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T08:37:01+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa_s250_blend_a50`
- model: `/mnt/data/exp/nemotron/20261029-nemotron-ft-ear1-step0/ckpts/A-fa_s250_blend_a50.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.39 | 5.56 | 4.16 | 0.68 | 10.99 | 100.00 | 0.00 |
| 0.25 | 1.59 | 0.95 | 0.58 | 0.06 | 2.39 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.15 (IoU 95.44) | 1.86 (IoU 1.89) |
| silence | 2.02 (IoU 2.06) | 14.97 (IoU 79.42) |

Speech P/R/F1: 97.57 / 97.76 / 97.67; miss 2.24 of ref speech, FA 11.91 of ref silence, SAD error 4.67.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12834 | 92.85 | 90.94 | 91.88 | 0.041 | 0.030 | -0.001 | 0.000 |
| 0.25 | offset | 13103 | 12834 | 93.00 | 91.09 | 92.04 | 0.044 | 0.030 | 0.005 | 0.010 |
| 0.25 | all | 26206 | 25668 | 92.93 | 91.02 | 91.96 | 0.043 | 0.030 | 0.002 | 0.010 |
| 0.50 | onset | 13103 | 12834 | 93.70 | 91.77 | 92.72 | 0.044 | 0.030 | -0.000 | 0.000 |
| 0.50 | offset | 13103 | 12834 | 93.88 | 91.95 | 92.90 | 0.047 | 0.030 | 0.005 | 0.010 |
| 0.50 | all | 26206 | 25668 | 93.79 | 91.86 | 92.81 | 0.046 | 0.030 | 0.002 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.72 | 9.99 | 1.08 | 1.28 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.50 | 12.09 | 1.76 | 2.89 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.02 | 10.27 | 1.26 | 1.65 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.69 | 22.08 | 5.09 | 7.37 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.72 | 19.74 | 2.83 | 3.09 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.30 | 7.34 | 1.57 | 1.68 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.77 | 18.82 | 7.78 | 7.57 | 4 | 4 |
| R8006_M8012__far_ch1 | 9.97 | 10.55 | 1.81 | 2.03 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.95 | 7.67 | 0.74 | 0.88 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.32 | 10.56 | 1.94 | 2.20 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.35 | 9.84 | 1.22 | 2.21 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.16 | 6.04 | 0.46 | 0.58 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.72 | 7.36 | 0.54 | 0.53 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.14 | 6.76 | 1.00 | 1.22 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.46 | 11.74 | 0.78 | 0.96 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.37 | 4.29 | 0.58 | 0.57 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.27 | 6.92 | 0.68 | 0.60 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.20 | 8.00 | 0.96 | 1.09 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.72 | 5.53 | 1.58 | 1.51 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.24 | 6.08 | 1.38 | 1.35 | 2 | 2 |
