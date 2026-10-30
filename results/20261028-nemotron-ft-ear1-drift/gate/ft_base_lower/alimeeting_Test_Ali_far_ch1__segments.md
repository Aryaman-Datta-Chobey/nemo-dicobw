# Diarization scores: ft_base_lower/alimeeting_Test_Ali_far_ch1__segments

- name: `ft_base_lower/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/ft_base_lower/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:42:18+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `ft_base_lower`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/ft_base_lower.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.01 | 16.25 | 1.17 | 0.58 | 18.67 | 100.00 | 0.00 |
| 0.25 | 10.03 | 9.58 | 0.29 | 0.16 | 11.77 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.03 (IoU 89.97) | 8.93 (IoU 8.96) |
| silence | 0.32 (IoU 0.36) | 7.72 (IoU 45.47) |

Speech P/R/F1: 99.61 / 90.29 / 94.72; miss 9.71 of ref speech, FA 4.04 of ref silence, SAD error 10.06.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12642 | 35.29 | 91.51 | 50.93 | 0.083 | 0.080 | 0.056 | 0.060 |
| 0.25 | offset | 4875 | 12642 | 35.10 | 91.02 | 50.66 | 0.093 | 0.090 | -0.078 | -0.080 |
| 0.25 | all | 9750 | 25284 | 35.19 | 91.26 | 50.80 | 0.088 | 0.080 | -0.011 | -0.010 |
| 0.50 | onset | 4875 | 12642 | 36.39 | 94.36 | 52.52 | 0.091 | 0.080 | 0.062 | 0.070 |
| 0.50 | offset | 4875 | 12642 | 36.87 | 95.61 | 53.22 | 0.104 | 0.090 | -0.086 | -0.090 |
| 0.50 | all | 9750 | 25284 | 36.63 | 94.98 | 52.87 | 0.097 | 0.090 | -0.012 | -0.020 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.06 | 16.33 | 11.46 | 11.93 | 4 | 4 |
| R8002_M8003__far_ch1 | 18.31 | 19.56 | 13.79 | 15.87 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.43 | 17.17 | 10.17 | 11.49 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.80 | 25.32 | 17.51 | 19.69 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.09 | 24.63 | 16.19 | 16.37 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.62 | 13.18 | 10.20 | 9.25 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.63 | 28.46 | 25.45 | 24.83 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.13 | 16.61 | 10.59 | 10.75 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.41 | 16.13 | 11.61 | 12.12 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.30 | 22.16 | 17.69 | 18.12 | 3 | 3 |
| R8008_M8016__far_ch1 | 18.36 | 21.79 | 12.79 | 16.08 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.27 | 16.54 | 12.00 | 12.58 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.21 | 16.12 | 4.02 | 3.86 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.46 | 15.67 | 2.68 | 3.11 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.71 | 17.83 | 2.95 | 4.20 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.80 | 13.73 | 1.77 | 1.78 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.89 | 13.49 | 2.13 | 1.91 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.20 | 17.30 | 3.24 | 3.29 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.12 | 16.13 | 4.42 | 4.37 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.51 | 12.31 | 1.85 | 1.84 | 2 | 2 |
