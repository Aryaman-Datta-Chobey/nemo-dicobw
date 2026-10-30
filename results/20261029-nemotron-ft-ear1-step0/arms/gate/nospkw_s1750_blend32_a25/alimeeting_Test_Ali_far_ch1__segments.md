# Diarization scores: nospkw_s1750_blend32_a25/alimeeting_Test_Ali_far_ch1__segments

- name: `nospkw_s1750_blend32_a25/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/nospkw_s1750_blend32_a25/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T09:19:44+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `nospkw_s1750_blend32_a25`
- model: `/mnt/data/exp/nemotron/20261029-nemotron-ft-ear1-step0/ckpts32/nospkw_s1750_blend32_a25.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.16 | 16.62 | 1.00 | 0.54 | 18.82 | 100.00 | 0.00 |
| 0.25 | 10.21 | 9.76 | 0.29 | 0.16 | 11.97 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.79 (IoU 89.78) | 9.17 (IoU 9.20) |
| silence | 0.26 (IoU 0.28) | 7.78 (IoU 45.23) |

Speech P/R/F1: 99.69 / 90.03 / 94.61; miss 9.97 of ref speech, FA 3.18 of ref silence, SAD error 10.25.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12831 | 35.29 | 92.88 | 51.15 | 0.082 | 0.080 | 0.061 | 0.070 |
| 0.25 | offset | 4875 | 12831 | 34.80 | 91.59 | 50.43 | 0.094 | 0.090 | -0.083 | -0.090 |
| 0.25 | all | 9750 | 25662 | 35.04 | 92.24 | 50.79 | 0.088 | 0.080 | -0.011 | -0.010 |
| 0.50 | onset | 4875 | 12831 | 36.25 | 95.41 | 52.54 | 0.089 | 0.080 | 0.066 | 0.070 |
| 0.50 | offset | 4875 | 12831 | 36.70 | 96.59 | 53.19 | 0.105 | 0.100 | -0.092 | -0.090 |
| 0.50 | all | 9750 | 25662 | 36.47 | 96.00 | 52.86 | 0.097 | 0.090 | -0.013 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.13 | 16.36 | 11.42 | 11.86 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.74 | 20.94 | 15.48 | 17.61 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.15 | 16.85 | 10.06 | 11.36 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.93 | 25.44 | 17.93 | 20.04 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.00 | 24.54 | 16.32 | 16.49 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.34 | 12.94 | 10.02 | 9.11 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.13 | 27.95 | 25.14 | 24.49 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.38 | 16.82 | 10.88 | 11.00 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.88 | 16.58 | 11.93 | 12.44 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.72 | 22.60 | 18.04 | 18.50 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.04 | 22.30 | 13.60 | 16.98 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.57 | 16.81 | 12.25 | 12.83 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.07 | 16.00 | 3.84 | 3.69 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.21 | 15.35 | 2.47 | 2.84 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.97 | 18.07 | 3.09 | 4.35 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.63 | 13.58 | 1.51 | 1.51 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.27 | 13.94 | 2.31 | 2.14 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.33 | 17.44 | 3.20 | 3.26 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.98 | 15.90 | 4.20 | 4.09 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.39 | 13.12 | 2.28 | 2.25 | 2 | 2 |
