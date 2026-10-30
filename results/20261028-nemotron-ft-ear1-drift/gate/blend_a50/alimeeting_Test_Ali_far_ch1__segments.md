# Diarization scores: blend_a50/alimeeting_Test_Ali_far_ch1__segments

- name: `blend_a50/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/blend_a50/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:40:19+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `blend_a50`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/blend_a50.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.02 | 16.38 | 1.07 | 0.56 | 18.66 | 100.00 | 0.00 |
| 0.25 | 10.06 | 9.61 | 0.29 | 0.17 | 11.82 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.96 (IoU 89.93) | 9.00 (IoU 9.02) |
| silence | 0.29 (IoU 0.32) | 7.75 (IoU 45.49) |

Speech P/R/F1: 99.65 / 90.22 / 94.70; miss 9.78 of ref speech, FA 3.61 of ref silence, SAD error 10.10.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12752 | 35.37 | 92.51 | 51.17 | 0.082 | 0.080 | 0.059 | 0.060 |
| 0.25 | offset | 4875 | 12752 | 35.03 | 91.63 | 50.68 | 0.093 | 0.090 | -0.080 | -0.080 |
| 0.25 | all | 9750 | 25504 | 35.20 | 92.07 | 50.93 | 0.088 | 0.080 | -0.010 | -0.010 |
| 0.50 | onset | 4875 | 12752 | 36.33 | 95.04 | 52.57 | 0.089 | 0.080 | 0.064 | 0.070 |
| 0.50 | offset | 4875 | 12752 | 36.85 | 96.39 | 53.32 | 0.104 | 0.090 | -0.088 | -0.090 |
| 0.50 | all | 9750 | 25504 | 36.59 | 95.71 | 52.94 | 0.097 | 0.090 | -0.013 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.16 | 16.42 | 11.39 | 11.85 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.07 | 20.24 | 14.87 | 16.93 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.20 | 16.92 | 10.06 | 11.38 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.94 | 25.59 | 17.85 | 20.08 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.93 | 24.45 | 16.15 | 16.29 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.33 | 12.94 | 9.97 | 9.08 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.39 | 28.17 | 25.33 | 24.68 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.26 | 16.72 | 10.80 | 10.90 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.32 | 16.02 | 11.45 | 11.95 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.01 | 21.87 | 17.39 | 17.82 | 3 | 3 |
| R8008_M8016__far_ch1 | 18.57 | 21.80 | 13.16 | 16.43 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.23 | 16.47 | 11.92 | 12.51 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.20 | 16.12 | 3.93 | 3.78 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.14 | 15.28 | 2.47 | 2.84 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.03 | 18.17 | 3.20 | 4.50 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.63 | 13.56 | 1.55 | 1.55 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.19 | 13.85 | 2.32 | 2.15 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.22 | 17.34 | 3.16 | 3.23 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.67 | 15.62 | 4.13 | 4.04 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.05 | 12.81 | 2.02 | 2.01 | 2 | 2 |
