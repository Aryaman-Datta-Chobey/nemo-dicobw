# Diarization scores: ft/alimeeting_Test_Ali_far_ch1__nouem

- name: `ft/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/ft/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:39:16+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `ft`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/ft.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.85 | 5.18 | 5.92 | 0.75 | 12.44 | 100.00 | 0.00 |
| 0.25 | 1.73 | 0.97 | 0.69 | 0.07 | 2.54 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.55 (IoU 94.35) | 1.75 (IoU 1.81) |
| silence | 3.13 (IoU 3.18) | 13.57 (IoU 73.55) |

Speech P/R/F1: 96.31 / 97.90 / 97.09; miss 2.10 of ref speech, FA 18.73 of ref silence, SAD error 5.86.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13099 | 12190 | 92.99 | 86.54 | 89.65 | 0.051 | 0.040 | -0.013 | -0.010 |
| 0.25 | offset | 13097 | 12192 | 92.63 | 86.23 | 89.32 | 0.060 | 0.050 | 0.021 | 0.020 |
| 0.25 | all | 26196 | 24382 | 92.81 | 86.39 | 89.49 | 0.055 | 0.040 | 0.004 | 0.000 |
| 0.50 | onset | 13099 | 12190 | 93.95 | 87.43 | 90.57 | 0.054 | 0.040 | -0.013 | -0.010 |
| 0.50 | offset | 13097 | 12192 | 94.04 | 87.54 | 90.67 | 0.064 | 0.050 | 0.023 | 0.020 |
| 0.50 | all | 26196 | 24382 | 93.99 | 87.48 | 90.62 | 0.059 | 0.040 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.32 | 10.61 | 1.47 | 1.78 | 4 | 4 |
| R8002_M8003__far_ch1 | 14.18 | 14.92 | 1.74 | 2.86 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.59 | 10.74 | 1.35 | 1.69 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.13 | 22.44 | 5.11 | 7.29 | 4 | 4 |
| R8005_M8007__far_ch1 | 20.08 | 19.99 | 2.76 | 2.97 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.73 | 7.71 | 1.65 | 1.76 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.45 | 19.54 | 8.06 | 7.87 | 4 | 4 |
| R8006_M8012__far_ch1 | 11.16 | 11.58 | 2.31 | 2.52 | 4 | 4 |
| R8008_M8014__far_ch1 | 8.42 | 9.03 | 0.59 | 0.73 | 3 | 3 |
| R8008_M8015__far_ch1 | 17.30 | 17.48 | 1.70 | 2.15 | 3 | 3 |
| R8008_M8016__far_ch1 | 10.74 | 12.91 | 1.43 | 2.50 | 3 | 3 |
| R8008_M8017__far_ch1 | 11.61 | 11.40 | 0.70 | 0.81 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.94 | 8.52 | 0.87 | 0.85 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.25 | 6.92 | 1.24 | 1.52 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.25 | 12.71 | 1.19 | 1.47 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.35 | 5.26 | 1.46 | 1.46 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.87 | 7.37 | 0.74 | 0.66 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.30 | 8.10 | 0.93 | 1.06 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.68 | 6.38 | 1.63 | 1.60 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.90 | 6.64 | 0.89 | 0.89 | 2 | 2 |
