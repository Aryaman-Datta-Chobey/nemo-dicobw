# Diarization scores: A-fa_s250_blend32_a25/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa_s250_blend32_a25/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s250_blend32_a25/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T09:10:12+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa_s250_blend32_a25`
- model: `/mnt/data/exp/nemotron/20261029-nemotron-ft-ear1-step0/ckpts32/A-fa_s250_blend32_a25.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.43 | 5.61 | 4.13 | 0.69 | 11.01 | 100.00 | 0.00 |
| 0.25 | 1.65 | 1.00 | 0.58 | 0.07 | 2.45 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.41 (IoU 95.40) | 1.95 (IoU 1.99) |
| silence | 1.98 (IoU 2.02) | 14.66 (IoU 78.87) |

Speech P/R/F1: 97.63 / 97.66 / 97.64; miss 2.34 of ref speech, FA 11.90 of ref silence, SAD error 4.71.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 12865 | 92.38 | 90.74 | 91.55 | 0.041 | 0.030 | -0.003 | 0.000 |
| 0.25 | offset | 13095 | 12868 | 92.63 | 91.03 | 91.82 | 0.044 | 0.030 | -0.000 | 0.010 |
| 0.25 | all | 26193 | 25733 | 92.51 | 90.88 | 91.69 | 0.043 | 0.030 | -0.002 | 0.000 |
| 0.50 | onset | 13098 | 12865 | 93.28 | 91.62 | 92.45 | 0.045 | 0.030 | -0.002 | 0.000 |
| 0.50 | offset | 13095 | 12868 | 93.46 | 91.84 | 92.64 | 0.047 | 0.030 | 0.000 | 0.010 |
| 0.50 | all | 26193 | 25733 | 93.37 | 91.73 | 92.54 | 0.046 | 0.030 | -0.001 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.67 | 9.95 | 1.19 | 1.42 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.34 | 11.86 | 1.79 | 2.89 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.09 | 10.29 | 1.29 | 1.69 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.82 | 22.19 | 5.20 | 7.47 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.80 | 19.78 | 2.85 | 3.09 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.35 | 7.36 | 1.58 | 1.69 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.91 | 18.95 | 7.79 | 7.66 | 4 | 4 |
| R8006_M8012__far_ch1 | 9.98 | 10.52 | 1.85 | 2.06 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.83 | 7.52 | 0.76 | 0.89 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.22 | 10.50 | 2.02 | 2.32 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.37 | 9.76 | 1.28 | 2.24 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.29 | 6.18 | 0.45 | 0.58 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.32 | 7.00 | 0.60 | 0.59 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.24 | 6.88 | 1.12 | 1.36 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.14 | 12.50 | 0.86 | 1.05 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.38 | 4.30 | 0.66 | 0.66 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.96 | 6.69 | 0.67 | 0.59 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.48 | 8.28 | 1.07 | 1.22 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.93 | 5.74 | 1.71 | 1.64 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.31 | 6.16 | 1.44 | 1.42 | 2 | 2 |
