# Diarization scores: ft_base_upper/alimeeting_Test_Ali_far_ch1__segments

- name: `ft_base_upper/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/ft_base_upper/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:42:48+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `ft_base_upper`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/ft_base_upper.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.91 | 16.30 | 1.08 | 0.54 | 18.55 | 100.00 | 0.00 |
| 0.25 | 9.78 | 9.33 | 0.30 | 0.16 | 11.59 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.24 (IoU 90.16) | 8.72 (IoU 8.76) |
| silence | 0.36 (IoU 0.39) | 7.68 (IoU 45.81) |

Speech P/R/F1: 99.57 / 90.51 / 94.83; miss 9.49 of ref speech, FA 4.48 of ref silence, SAD error 9.88.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12614 | 35.86 | 92.80 | 51.74 | 0.084 | 0.080 | 0.061 | 0.060 |
| 0.25 | offset | 4875 | 12615 | 35.37 | 91.53 | 51.02 | 0.095 | 0.090 | -0.075 | -0.080 |
| 0.25 | all | 9750 | 25229 | 35.62 | 92.16 | 51.38 | 0.089 | 0.080 | -0.006 | -0.010 |
| 0.50 | onset | 4875 | 12614 | 36.87 | 95.41 | 53.19 | 0.091 | 0.080 | 0.066 | 0.070 |
| 0.50 | offset | 4875 | 12615 | 37.37 | 96.70 | 53.91 | 0.107 | 0.100 | -0.082 | -0.090 |
| 0.50 | all | 9750 | 25229 | 37.12 | 96.05 | 53.55 | 0.099 | 0.090 | -0.009 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.80 | 17.08 | 11.57 | 12.04 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.99 | 21.26 | 15.54 | 17.76 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.06 | 16.75 | 10.06 | 11.38 | 4 | 4 |
| R8004_M8006__far_ch1 | 23.04 | 25.62 | 18.22 | 20.41 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.86 | 24.44 | 16.31 | 16.49 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.50 | 13.12 | 10.10 | 9.20 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.69 | 28.46 | 25.62 | 24.98 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.55 | 16.92 | 11.02 | 11.07 | 4 | 4 |
| R8008_M8014__far_ch1 | 14.29 | 14.95 | 10.05 | 10.47 | 3 | 3 |
| R8008_M8015__far_ch1 | 16.93 | 18.31 | 11.93 | 12.55 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.35 | 22.46 | 13.75 | 16.98 | 3 | 3 |
| R8008_M8017__far_ch1 | 14.24 | 15.53 | 10.48 | 11.18 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.42 | 16.34 | 3.99 | 3.84 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.91 | 15.06 | 2.35 | 2.72 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.40 | 18.55 | 3.74 | 5.10 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.77 | 13.71 | 1.65 | 1.66 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.63 | 14.22 | 2.59 | 2.42 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.91 | 17.08 | 2.95 | 3.02 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.41 | 14.33 | 3.38 | 3.26 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.32 | 13.03 | 2.32 | 2.29 | 2 | 2 |
