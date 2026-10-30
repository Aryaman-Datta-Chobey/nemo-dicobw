# Diarization scores: avg_e4-5-6-7-8/alimeeting_Test_Ali_far_ch1__segments

- name: `avg_e4-5-6-7-8/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/avg_e4-5-6-7-8/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:43:18+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `avg_e4-5-6-7-8`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/avg_e4-5-6-7-8.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.55 | 15.50 | 1.43 | 0.62 | 18.14 | 95.00 | 0.05 |
| 0.25 | 9.47 | 8.94 | 0.36 | 0.17 | 11.18 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.71 (IoU 90.53) | 8.25 (IoU 8.29) |
| silence | 0.51 (IoU 0.56) | 7.53 (IoU 46.24) |

Speech P/R/F1: 99.40 / 91.03 / 95.03; miss 8.97 of ref speech, FA 6.34 of ref silence, SAD error 9.52.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12344 | 36.03 | 91.24 | 51.66 | 0.086 | 0.080 | 0.055 | 0.060 |
| 0.25 | offset | 4875 | 12344 | 35.78 | 90.61 | 51.30 | 0.095 | 0.090 | -0.062 | -0.070 |
| 0.25 | all | 9750 | 24688 | 35.91 | 90.92 | 51.48 | 0.090 | 0.080 | -0.003 | -0.010 |
| 0.50 | onset | 4875 | 12344 | 37.11 | 93.97 | 53.21 | 0.093 | 0.080 | 0.061 | 0.060 |
| 0.50 | offset | 4875 | 12344 | 37.57 | 95.14 | 53.87 | 0.105 | 0.090 | -0.068 | -0.080 |
| 0.50 | all | 9750 | 24688 | 37.34 | 94.55 | 53.54 | 0.099 | 0.090 | -0.004 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.64 | 16.94 | 11.68 | 12.21 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.72 | 18.86 | 12.55 | 14.51 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.44 | 17.22 | 10.31 | 11.73 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.70 | 25.33 | 17.58 | 19.83 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.65 | 24.26 | 15.87 | 16.07 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.43 | 13.06 | 9.93 | 9.10 | 4 | 4 |
| R8005_M8009__far_ch1 | 29.25 | 29.05 | 26.28 | 25.56 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.22 | 16.60 | 10.68 | 10.76 | 4 | 4 |
| R8008_M8014__far_ch1 | 14.15 | 14.92 | 10.31 | 10.82 | 3 | 3 |
| R8008_M8015__far_ch1 | 17.26 | 18.53 | 12.67 | 13.20 | 3 | 4 |
| R8008_M8016__far_ch1 | 17.56 | 20.59 | 12.11 | 15.01 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.78 | 13.78 | 8.40 | 8.92 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.50 | 16.41 | 4.26 | 4.10 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.14 | 15.31 | 2.52 | 2.93 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.60 | 17.80 | 3.15 | 4.49 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.19 | 14.11 | 2.20 | 2.21 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.06 | 13.52 | 2.34 | 2.08 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.04 | 16.16 | 2.66 | 2.73 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.25 | 14.28 | 3.62 | 3.59 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.43 | 12.18 | 1.85 | 1.83 | 2 | 2 |
