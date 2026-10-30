# Diarization scores: blend_a25/alimeeting_Test_Ali_far_ch1__segments

- name: `blend_a25/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/blend_a25/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:39:48+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `blend_a25`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/blend_a25.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.13 | 16.55 | 1.02 | 0.56 | 18.78 | 100.00 | 0.00 |
| 0.25 | 10.18 | 9.71 | 0.30 | 0.17 | 11.95 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.84 (IoU 89.83) | 9.12 (IoU 9.14) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 45.33) |

Speech P/R/F1: 99.68 / 90.08 / 94.64; miss 9.92 of ref speech, FA 3.26 of ref silence, SAD error 10.20.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12835 | 35.25 | 92.80 | 51.09 | 0.082 | 0.080 | 0.060 | 0.070 |
| 0.25 | offset | 4875 | 12835 | 34.79 | 91.59 | 50.42 | 0.093 | 0.090 | -0.083 | -0.090 |
| 0.25 | all | 9750 | 25670 | 35.02 | 92.19 | 50.76 | 0.088 | 0.080 | -0.011 | -0.010 |
| 0.50 | onset | 4875 | 12835 | 36.21 | 95.32 | 52.48 | 0.089 | 0.080 | 0.066 | 0.070 |
| 0.50 | offset | 4875 | 12835 | 36.65 | 96.49 | 53.12 | 0.105 | 0.100 | -0.091 | -0.090 |
| 0.50 | all | 9750 | 25670 | 36.43 | 95.91 | 52.80 | 0.097 | 0.090 | -0.013 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.11 | 16.34 | 11.40 | 11.85 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.60 | 20.79 | 15.38 | 17.50 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.11 | 16.80 | 10.04 | 11.31 | 4 | 4 |
| R8004_M8006__far_ch1 | 23.05 | 25.68 | 18.03 | 20.32 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.00 | 24.59 | 16.24 | 16.43 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.32 | 12.93 | 10.01 | 9.10 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.29 | 28.07 | 25.33 | 24.69 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.28 | 16.73 | 10.83 | 10.93 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.71 | 16.42 | 11.78 | 12.29 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.52 | 22.31 | 17.86 | 18.23 | 3 | 3 |
| R8008_M8016__far_ch1 | 18.92 | 22.15 | 13.52 | 16.86 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.50 | 16.75 | 12.18 | 12.76 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.08 | 16.01 | 3.85 | 3.71 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.15 | 15.29 | 2.44 | 2.81 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.94 | 18.04 | 3.08 | 4.34 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.62 | 13.56 | 1.52 | 1.53 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.27 | 13.93 | 2.32 | 2.15 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.29 | 17.41 | 3.16 | 3.22 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.89 | 15.81 | 4.18 | 4.07 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.28 | 13.02 | 2.19 | 2.16 | 2 | 2 |
