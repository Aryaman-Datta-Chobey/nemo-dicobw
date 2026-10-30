# Diarization scores: blend_a50/alimeeting_Test_Ali_far_ch1__nouem

- name: `blend_a50/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/blend_a50/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:40:17+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `blend_a50`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/blend_a50.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.67 | 5.48 | 4.48 | 0.71 | 11.24 | 100.00 | 0.00 |
| 0.25 | 1.64 | 0.99 | 0.59 | 0.07 | 2.43 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.44 (IoU 95.24) | 1.91 (IoU 1.95) |
| silence | 2.16 (IoU 2.20) | 14.48 (IoU 78.04) |

Speech P/R/F1: 97.41 / 97.71 / 97.56; miss 2.29 of ref speech, FA 12.99 of ref silence, SAD error 4.89.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13100 | 12735 | 92.70 | 90.11 | 91.39 | 0.044 | 0.030 | -0.007 | 0.000 |
| 0.25 | offset | 13095 | 12740 | 92.97 | 90.45 | 91.69 | 0.046 | 0.040 | 0.002 | 0.010 |
| 0.25 | all | 26195 | 25475 | 92.83 | 90.28 | 91.54 | 0.045 | 0.030 | -0.002 | 0.000 |
| 0.50 | onset | 13100 | 12735 | 93.62 | 91.02 | 92.30 | 0.047 | 0.030 | -0.006 | 0.000 |
| 0.50 | offset | 13095 | 12740 | 93.79 | 91.25 | 92.50 | 0.049 | 0.040 | 0.002 | 0.010 |
| 0.50 | all | 26195 | 25475 | 93.71 | 91.13 | 92.40 | 0.048 | 0.030 | -0.002 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.49 | 9.80 | 1.13 | 1.33 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.69 | 12.07 | 1.67 | 2.60 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.38 | 10.59 | 1.31 | 1.69 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.04 | 22.47 | 5.13 | 7.50 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.98 | 19.87 | 2.76 | 2.98 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.44 | 7.44 | 1.60 | 1.70 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.11 | 19.14 | 7.83 | 7.68 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.19 | 10.73 | 1.98 | 2.18 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.17 | 7.85 | 0.72 | 0.85 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.63 | 10.99 | 1.83 | 2.17 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.96 | 10.34 | 1.28 | 2.24 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.91 | 6.68 | 0.50 | 0.61 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.59 | 7.26 | 0.66 | 0.65 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.19 | 6.83 | 1.20 | 1.44 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.60 | 13.05 | 1.00 | 1.20 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.60 | 4.51 | 0.81 | 0.81 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.21 | 6.94 | 0.72 | 0.67 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.47 | 8.28 | 1.04 | 1.18 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.37 | 6.17 | 1.83 | 1.78 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.37 | 6.21 | 1.07 | 1.07 | 2 | 2 |
