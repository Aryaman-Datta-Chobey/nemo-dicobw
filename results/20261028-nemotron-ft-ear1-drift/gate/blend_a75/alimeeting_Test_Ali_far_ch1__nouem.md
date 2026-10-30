# Diarization scores: blend_a75/alimeeting_Test_Ali_far_ch1__nouem

- name: `blend_a75/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/blend_a75/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:40:47+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `blend_a75`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/blend_a75.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.07 | 5.35 | 4.99 | 0.73 | 11.66 | 95.00 | 0.05 |
| 0.25 | 1.65 | 0.98 | 0.61 | 0.07 | 2.44 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.52 (IoU 94.94) | 1.84 (IoU 1.88) |
| silence | 2.51 (IoU 2.56) | 14.13 (IoU 76.47) |

Speech P/R/F1: 97.01 / 97.80 / 97.40; miss 2.20 of ref speech, FA 15.09 of ref silence, SAD error 5.22.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13099 | 12545 | 93.01 | 89.08 | 91.00 | 0.047 | 0.040 | -0.009 | -0.010 |
| 0.25 | offset | 13095 | 12549 | 93.12 | 89.24 | 91.14 | 0.052 | 0.040 | 0.010 | 0.010 |
| 0.25 | all | 26194 | 25094 | 93.07 | 89.16 | 91.07 | 0.049 | 0.040 | 0.001 | 0.000 |
| 0.50 | onset | 13099 | 12545 | 93.92 | 89.95 | 91.89 | 0.050 | 0.040 | -0.009 | -0.010 |
| 0.50 | offset | 13095 | 12549 | 94.05 | 90.13 | 92.04 | 0.054 | 0.040 | 0.011 | 0.010 |
| 0.50 | all | 26194 | 25094 | 93.98 | 90.04 | 91.97 | 0.052 | 0.040 | 0.001 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.79 | 10.08 | 1.11 | 1.32 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.92 | 13.07 | 1.69 | 2.71 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.43 | 10.59 | 1.32 | 1.65 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.00 | 22.26 | 4.99 | 7.16 | 4 | 4 |
| R8005_M8007__far_ch1 | 20.00 | 19.89 | 2.76 | 2.97 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.53 | 7.52 | 1.61 | 1.72 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.23 | 19.29 | 7.95 | 7.84 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.52 | 11.04 | 2.12 | 2.31 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.68 | 8.36 | 0.68 | 0.83 | 3 | 3 |
| R8008_M8015__far_ch1 | 12.12 | 13.56 | 1.76 | 2.16 | 3 | 4 |
| R8008_M8016__far_ch1 | 8.84 | 11.17 | 1.38 | 2.36 | 3 | 3 |
| R8008_M8017__far_ch1 | 7.56 | 8.04 | 0.43 | 0.50 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.25 | 7.88 | 0.77 | 0.76 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.18 | 6.83 | 1.24 | 1.49 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.52 | 13.03 | 1.15 | 1.44 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.74 | 4.64 | 0.88 | 0.88 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.81 | 7.46 | 0.80 | 0.76 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.42 | 8.22 | 1.00 | 1.15 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.44 | 6.19 | 1.68 | 1.65 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.61 | 6.41 | 0.96 | 0.96 | 2 | 2 |
