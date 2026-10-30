# Diarization scores: ft_base_head/alimeeting_Test_Ali_far_ch1__segments

- name: `ft_base_head/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/ft_base_head/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:41:49+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `ft_base_head`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/ft_base_head.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.36 | 15.20 | 1.51 | 0.66 | 17.96 | 100.00 | 0.00 |
| 0.25 | 9.23 | 8.69 | 0.36 | 0.19 | 10.96 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 84.00 (IoU 90.80) | 7.96 (IoU 8.00) |
| silence | 0.55 (IoU 0.60) | 7.49 (IoU 46.82) |

Speech P/R/F1: 99.35 / 91.35 / 95.18; miss 8.65 of ref speech, FA 6.83 of ref silence, SAD error 9.25.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12127 | 36.62 | 91.10 | 52.24 | 0.086 | 0.080 | 0.053 | 0.060 |
| 0.25 | offset | 4875 | 12128 | 36.29 | 90.28 | 51.77 | 0.096 | 0.090 | -0.058 | -0.070 |
| 0.25 | all | 9750 | 24255 | 36.45 | 90.69 | 52.00 | 0.091 | 0.090 | -0.003 | -0.010 |
| 0.50 | onset | 4875 | 12127 | 37.68 | 93.72 | 53.75 | 0.093 | 0.080 | 0.058 | 0.060 |
| 0.50 | offset | 4875 | 12128 | 38.13 | 94.87 | 54.40 | 0.107 | 0.100 | -0.064 | -0.080 |
| 0.50 | all | 9750 | 24255 | 37.91 | 94.30 | 54.07 | 0.100 | 0.090 | -0.004 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.44 | 16.70 | 11.58 | 12.09 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.72 | 18.86 | 12.28 | 14.21 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.43 | 17.18 | 10.23 | 11.62 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.86 | 25.68 | 17.75 | 20.25 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.57 | 24.19 | 15.76 | 15.94 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.36 | 13.02 | 9.80 | 8.98 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.84 | 28.68 | 25.75 | 25.15 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.03 | 16.40 | 10.33 | 10.39 | 4 | 4 |
| R8008_M8014__far_ch1 | 13.76 | 14.48 | 9.92 | 10.36 | 3 | 3 |
| R8008_M8015__far_ch1 | 16.36 | 18.05 | 11.55 | 12.47 | 3 | 3 |
| R8008_M8016__far_ch1 | 16.66 | 19.71 | 11.21 | 14.09 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.39 | 13.39 | 7.73 | 8.28 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.39 | 16.31 | 4.24 | 4.09 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.97 | 15.09 | 2.46 | 2.86 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.78 | 17.92 | 3.24 | 4.55 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.02 | 13.97 | 2.16 | 2.18 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.93 | 13.41 | 2.29 | 2.04 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.13 | 16.25 | 2.74 | 2.79 | 2 | 2 |
| R8009_M8027__far_ch1 | 13.92 | 13.94 | 3.47 | 3.42 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.25 | 12.02 | 1.81 | 1.80 | 2 | 2 |
