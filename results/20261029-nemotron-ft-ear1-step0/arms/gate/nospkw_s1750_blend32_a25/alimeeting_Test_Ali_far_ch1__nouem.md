# Diarization scores: nospkw_s1750_blend32_a25/alimeeting_Test_Ali_far_ch1__nouem

- name: `nospkw_s1750_blend32_a25/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/nospkw_s1750_blend32_a25/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T09:19:42+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `nospkw_s1750_blend32_a25`
- model: `/mnt/data/exp/nemotron/20261029-nemotron-ft-ear1-step0/ckpts32/nospkw_s1750_blend32_a25.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.48 | 5.58 | 4.22 | 0.68 | 11.06 | 100.00 | 0.00 |
| 0.25 | 1.66 | 1.01 | 0.59 | 0.06 | 2.43 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.39 (IoU 95.35) | 1.97 (IoU 2.01) |
| silence | 2.00 (IoU 2.04) | 14.64 (IoU 78.67) |

Speech P/R/F1: 97.60 / 97.64 / 97.62; miss 2.36 of ref speech, FA 12.04 of ref silence, SAD error 4.76.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13099 | 12814 | 92.57 | 90.56 | 91.55 | 0.042 | 0.030 | -0.005 | 0.000 |
| 0.25 | offset | 13095 | 12819 | 92.82 | 90.86 | 91.83 | 0.044 | 0.030 | -0.001 | 0.000 |
| 0.25 | all | 26194 | 25633 | 92.69 | 90.71 | 91.69 | 0.043 | 0.030 | -0.003 | 0.000 |
| 0.50 | onset | 13099 | 12814 | 93.48 | 91.45 | 92.46 | 0.045 | 0.030 | -0.004 | 0.000 |
| 0.50 | offset | 13095 | 12819 | 93.64 | 91.67 | 92.64 | 0.047 | 0.030 | -0.001 | 0.000 |
| 0.50 | all | 26194 | 25633 | 93.56 | 91.56 | 92.55 | 0.046 | 0.030 | -0.003 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.43 | 9.72 | 1.13 | 1.34 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.41 | 11.90 | 1.80 | 2.90 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.23 | 10.43 | 1.28 | 1.66 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.83 | 22.16 | 5.13 | 7.34 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.89 | 19.86 | 2.79 | 3.00 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.40 | 7.41 | 1.60 | 1.70 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.81 | 18.81 | 7.75 | 7.45 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.05 | 10.59 | 1.95 | 2.15 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.87 | 7.59 | 0.76 | 0.90 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.19 | 10.53 | 1.93 | 2.27 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.58 | 9.96 | 1.33 | 2.31 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.48 | 6.33 | 0.47 | 0.60 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.24 | 6.93 | 0.63 | 0.62 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.27 | 6.93 | 1.18 | 1.42 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.49 | 12.90 | 0.89 | 1.08 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.51 | 4.43 | 0.76 | 0.76 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.96 | 6.71 | 0.68 | 0.60 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.49 | 8.28 | 1.03 | 1.17 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.15 | 5.97 | 1.81 | 1.75 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.40 | 6.24 | 1.39 | 1.37 | 2 | 2 |
