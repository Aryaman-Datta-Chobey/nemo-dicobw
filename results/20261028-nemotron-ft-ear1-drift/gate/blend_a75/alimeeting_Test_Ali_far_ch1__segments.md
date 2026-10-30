# Diarization scores: blend_a75/alimeeting_Test_Ali_far_ch1__segments

- name: `blend_a75/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/blend_a75/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:40:49+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `blend_a75`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/blend_a75.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.77 | 15.97 | 1.21 | 0.59 | 18.39 | 95.00 | 0.05 |
| 0.25 | 9.78 | 9.31 | 0.30 | 0.17 | 11.49 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.30 (IoU 90.22) | 8.66 (IoU 8.69) |
| silence | 0.37 (IoU 0.41) | 7.67 (IoU 45.92) |

Speech P/R/F1: 99.55 / 90.59 / 94.86; miss 9.41 of ref speech, FA 4.64 of ref silence, SAD error 9.82.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12562 | 35.73 | 92.06 | 51.48 | 0.084 | 0.080 | 0.057 | 0.060 |
| 0.25 | offset | 4875 | 12562 | 35.37 | 91.14 | 50.96 | 0.093 | 0.090 | -0.071 | -0.080 |
| 0.25 | all | 9750 | 25124 | 35.55 | 91.60 | 51.22 | 0.088 | 0.080 | -0.007 | -0.010 |
| 0.50 | onset | 4875 | 12562 | 36.71 | 94.61 | 52.90 | 0.090 | 0.080 | 0.061 | 0.060 |
| 0.50 | offset | 4875 | 12562 | 37.18 | 95.82 | 53.58 | 0.104 | 0.090 | -0.079 | -0.080 |
| 0.50 | all | 9750 | 25124 | 36.95 | 95.21 | 53.24 | 0.097 | 0.090 | -0.009 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.29 | 16.54 | 11.41 | 11.86 | 4 | 4 |
| R8002_M8003__far_ch1 | 18.33 | 19.51 | 13.80 | 15.87 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.25 | 16.93 | 10.13 | 11.44 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.76 | 25.28 | 17.62 | 19.65 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.79 | 24.35 | 15.99 | 16.15 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.40 | 13.01 | 9.93 | 9.07 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.54 | 28.34 | 25.46 | 24.84 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.13 | 16.55 | 10.60 | 10.70 | 4 | 4 |
| R8008_M8014__far_ch1 | 14.63 | 15.35 | 10.80 | 11.30 | 3 | 3 |
| R8008_M8015__far_ch1 | 19.79 | 20.86 | 15.73 | 16.14 | 3 | 4 |
| R8008_M8016__far_ch1 | 17.91 | 21.08 | 12.54 | 15.66 | 3 | 3 |
| R8008_M8017__far_ch1 | 14.09 | 15.28 | 10.52 | 11.09 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.42 | 16.33 | 4.16 | 4.01 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.13 | 15.28 | 2.52 | 2.91 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.04 | 18.24 | 3.33 | 4.73 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.72 | 13.64 | 1.67 | 1.66 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.29 | 13.86 | 2.48 | 2.30 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.84 | 16.97 | 3.01 | 3.07 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.83 | 14.83 | 3.80 | 3.74 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.74 | 12.50 | 1.94 | 1.93 | 2 | 2 |
