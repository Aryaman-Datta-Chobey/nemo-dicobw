# Diarization scores: ft_base_lower/alimeeting_Test_Ali_far_ch1

- name: `ft_base_lower/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/ft_base_lower/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:42:14+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `ft_base_lower`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/ft_base_lower.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.85 | 5.44 | 4.70 | 0.71 | 11.41 | 100.00 | 0.00 |
| 0.25 | 1.71 | 1.05 | 0.60 | 0.06 | 2.51 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.12 (IoU 95.17) | 1.88 (IoU 1.92) |
| silence | 2.23 (IoU 2.27) | 14.76 (IoU 78.21) |

Speech P/R/F1: 97.32 / 97.73 / 97.53; miss 2.27 of ref speech, FA 13.13 of ref silence, SAD error 4.95.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12642 | 92.71 | 89.45 | 91.05 | 0.044 | 0.030 | -0.011 | -0.010 |
| 0.25 | offset | 13103 | 12642 | 93.05 | 89.77 | 91.38 | 0.046 | 0.030 | 0.003 | 0.010 |
| 0.25 | all | 26206 | 25284 | 92.88 | 89.61 | 91.22 | 0.045 | 0.030 | -0.004 | 0.000 |
| 0.50 | onset | 13103 | 12642 | 93.75 | 90.45 | 92.07 | 0.047 | 0.030 | -0.011 | -0.010 |
| 0.50 | offset | 13103 | 12642 | 93.92 | 90.61 | 92.24 | 0.049 | 0.040 | 0.003 | 0.010 |
| 0.50 | all | 26206 | 25284 | 93.83 | 90.53 | 92.15 | 0.048 | 0.030 | -0.004 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.07 | 9.43 | 1.17 | 1.41 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.75 | 12.93 | 1.64 | 2.63 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.70 | 10.90 | 1.39 | 1.76 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.34 | 22.48 | 5.14 | 7.33 | 4 | 4 |
| R8005_M8007__far_ch1 | 20.53 | 20.38 | 2.90 | 3.14 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.96 | 7.88 | 1.98 | 2.03 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.38 | 19.39 | 7.99 | 7.78 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.64 | 11.15 | 2.07 | 2.33 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.83 | 7.57 | 0.76 | 0.93 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.39 | 10.69 | 1.96 | 2.32 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.76 | 11.17 | 1.35 | 2.27 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.79 | 6.60 | 0.51 | 0.61 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.79 | 7.45 | 0.74 | 0.73 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.15 | 6.86 | 1.36 | 1.64 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.00 | 12.42 | 0.86 | 1.09 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.71 | 4.62 | 1.05 | 1.06 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.82 | 6.54 | 0.65 | 0.56 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.80 | 8.58 | 1.05 | 1.18 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.59 | 6.46 | 1.97 | 1.93 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.47 | 6.33 | 0.94 | 0.94 | 2 | 2 |
