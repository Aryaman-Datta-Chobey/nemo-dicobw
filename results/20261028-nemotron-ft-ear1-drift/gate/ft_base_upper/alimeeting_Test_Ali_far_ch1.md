# Diarization scores: ft_base_upper/alimeeting_Test_Ali_far_ch1

- name: `ft_base_upper/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/ft_base_upper/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:42:43+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `ft_base_upper`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/ft_base_upper.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.15 | 5.67 | 4.78 | 0.70 | 11.76 | 100.00 | 0.00 |
| 0.25 | 1.71 | 1.02 | 0.63 | 0.07 | 2.53 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.04 (IoU 94.72) | 1.96 (IoU 2.02) |
| silence | 2.55 (IoU 2.61) | 14.44 (IoU 76.17) |

Speech P/R/F1: 96.94 / 97.63 / 97.29; miss 2.37 of ref speech, FA 15.03 of ref silence, SAD error 5.44.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12614 | 92.34 | 88.90 | 90.59 | 0.047 | 0.040 | -0.004 | 0.000 |
| 0.25 | offset | 13103 | 12615 | 92.07 | 88.64 | 90.32 | 0.051 | 0.040 | 0.008 | 0.010 |
| 0.25 | all | 26206 | 25229 | 92.20 | 88.77 | 90.45 | 0.049 | 0.040 | 0.002 | 0.000 |
| 0.50 | onset | 13103 | 12614 | 93.25 | 89.77 | 91.47 | 0.050 | 0.040 | -0.004 | 0.000 |
| 0.50 | offset | 13103 | 12615 | 93.40 | 89.93 | 91.63 | 0.055 | 0.040 | 0.009 | 0.010 |
| 0.50 | all | 26206 | 25229 | 93.33 | 89.85 | 91.55 | 0.053 | 0.040 | 0.003 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.50 | 10.80 | 1.20 | 1.44 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.93 | 12.41 | 1.76 | 2.80 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.01 | 10.19 | 1.22 | 1.55 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.71 | 22.21 | 5.22 | 7.72 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.54 | 19.57 | 2.85 | 3.07 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.37 | 7.43 | 1.63 | 1.74 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.90 | 18.98 | 7.93 | 7.73 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.12 | 10.64 | 1.98 | 2.12 | 4 | 4 |
| R8008_M8014__far_ch1 | 8.81 | 9.29 | 0.61 | 0.65 | 3 | 3 |
| R8008_M8015__far_ch1 | 16.52 | 16.95 | 2.19 | 2.94 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.05 | 10.42 | 1.55 | 2.46 | 3 | 3 |
| R8008_M8017__far_ch1 | 7.83 | 8.39 | 0.60 | 0.80 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.73 | 7.40 | 0.69 | 0.68 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.54 | 7.19 | 1.10 | 1.34 | 2 | 2 |
| R8009_M8023__far_ch1 | 11.40 | 13.80 | 1.40 | 1.55 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.84 | 4.75 | 0.92 | 0.92 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.01 | 7.62 | 0.78 | 0.71 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.10 | 7.95 | 1.04 | 1.19 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.04 | 5.72 | 1.57 | 1.51 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.64 | 6.42 | 1.38 | 1.36 | 2 | 2 |
