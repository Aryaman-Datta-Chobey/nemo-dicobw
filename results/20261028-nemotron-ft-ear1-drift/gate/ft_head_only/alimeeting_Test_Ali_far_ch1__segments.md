# Diarization scores: ft_head_only/alimeeting_Test_Ali_far_ch1__segments

- name: `ft_head_only/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/ft_head_only/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:41:19+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `ft_head_only`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/ft_head_only.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.33 | 16.83 | 0.97 | 0.54 | 18.99 | 100.00 | 0.00 |
| 0.25 | 10.32 | 9.87 | 0.29 | 0.16 | 12.10 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.62 (IoU 89.61) | 9.34 (IoU 9.36) |
| silence | 0.24 (IoU 0.26) | 7.80 (IoU 44.90) |

Speech P/R/F1: 99.71 / 89.84 / 94.52; miss 10.16 of ref speech, FA 2.95 of ref silence, SAD error 10.41.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12940 | 35.01 | 92.92 | 50.86 | 0.083 | 0.080 | 0.063 | 0.070 |
| 0.25 | offset | 4875 | 12940 | 34.54 | 91.69 | 50.18 | 0.095 | 0.090 | -0.086 | -0.090 |
| 0.25 | all | 9750 | 25880 | 34.78 | 92.31 | 50.52 | 0.089 | 0.080 | -0.011 | -0.010 |
| 0.50 | onset | 4875 | 12940 | 35.97 | 95.47 | 52.25 | 0.090 | 0.080 | 0.069 | 0.070 |
| 0.50 | offset | 4875 | 12940 | 36.40 | 96.62 | 52.88 | 0.107 | 0.100 | -0.095 | -0.090 |
| 0.50 | all | 9750 | 25880 | 36.18 | 96.04 | 52.56 | 0.098 | 0.090 | -0.014 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.35 | 16.60 | 11.54 | 12.01 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.05 | 21.28 | 15.69 | 17.87 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.18 | 16.88 | 10.13 | 11.43 | 4 | 4 |
| R8004_M8006__far_ch1 | 23.02 | 25.49 | 18.06 | 20.12 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.11 | 24.65 | 16.45 | 16.62 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.39 | 13.00 | 10.08 | 9.16 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.39 | 28.11 | 25.41 | 24.71 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.56 | 17.02 | 10.97 | 11.10 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.23 | 16.95 | 12.18 | 12.68 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.21 | 22.97 | 18.46 | 18.80 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.42 | 22.72 | 13.84 | 17.27 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.78 | 17.05 | 12.42 | 13.02 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.13 | 16.05 | 3.85 | 3.70 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.31 | 15.50 | 2.49 | 2.89 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.03 | 18.14 | 3.13 | 4.40 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.72 | 13.65 | 1.46 | 1.45 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.36 | 14.09 | 2.30 | 2.18 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.48 | 17.61 | 3.30 | 3.38 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.01 | 15.93 | 4.10 | 3.98 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.52 | 13.24 | 2.35 | 2.31 | 2 | 2 |
