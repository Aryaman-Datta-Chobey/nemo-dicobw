# Diarization scores: A-fa_s250_blend32_a25/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa_s250_blend32_a25/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s250_blend32_a25/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T09:10:14+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa_s250_blend32_a25`
- model: `/mnt/data/exp/nemotron/20261029-nemotron-ft-ear1-step0/ckpts32/A-fa_s250_blend32_a25.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.20 | 16.69 | 0.97 | 0.54 | 18.85 | 100.00 | 0.00 |
| 0.25 | 10.23 | 9.78 | 0.29 | 0.16 | 12.01 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.79 (IoU 89.79) | 9.17 (IoU 9.19) |
| silence | 0.25 (IoU 0.27) | 7.79 (IoU 45.29) |

Speech P/R/F1: 99.70 / 90.03 / 94.62; miss 9.97 of ref speech, FA 3.06 of ref silence, SAD error 10.24.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12880 | 35.22 | 93.05 | 51.10 | 0.083 | 0.080 | 0.063 | 0.070 |
| 0.25 | offset | 4875 | 12880 | 34.81 | 91.96 | 50.50 | 0.093 | 0.090 | -0.083 | -0.090 |
| 0.25 | all | 9750 | 25760 | 35.01 | 92.50 | 50.80 | 0.088 | 0.080 | -0.009 | -0.010 |
| 0.50 | onset | 4875 | 12880 | 36.16 | 95.53 | 52.46 | 0.090 | 0.080 | 0.068 | 0.070 |
| 0.50 | offset | 4875 | 12880 | 36.59 | 96.68 | 53.09 | 0.104 | 0.090 | -0.091 | -0.090 |
| 0.50 | all | 9750 | 25760 | 36.37 | 96.10 | 52.77 | 0.097 | 0.090 | -0.012 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.25 | 16.50 | 11.43 | 11.88 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.94 | 21.15 | 15.62 | 17.78 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.11 | 16.77 | 10.08 | 11.37 | 4 | 4 |
| R8004_M8006__far_ch1 | 23.03 | 25.55 | 18.06 | 20.16 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.04 | 24.58 | 16.40 | 16.56 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.37 | 12.96 | 10.07 | 9.15 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.33 | 28.07 | 25.31 | 24.66 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.45 | 16.89 | 10.89 | 11.04 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.06 | 16.72 | 12.06 | 12.54 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.95 | 22.79 | 18.25 | 18.68 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.18 | 22.47 | 13.71 | 17.11 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.57 | 16.83 | 12.28 | 12.87 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.89 | 15.82 | 3.76 | 3.62 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.03 | 15.15 | 2.37 | 2.73 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.80 | 17.84 | 2.93 | 4.11 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.46 | 13.41 | 1.37 | 1.37 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.25 | 13.92 | 2.28 | 2.12 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.32 | 17.44 | 3.20 | 3.27 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.82 | 15.72 | 4.03 | 3.90 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.36 | 13.09 | 2.28 | 2.25 | 2 | 2 |
