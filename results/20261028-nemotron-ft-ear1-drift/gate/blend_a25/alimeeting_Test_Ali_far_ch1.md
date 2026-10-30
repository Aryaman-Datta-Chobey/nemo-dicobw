# Diarization scores: blend_a25/alimeeting_Test_Ali_far_ch1

- name: `blend_a25/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/blend_a25/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:39:43+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `blend_a25`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/blend_a25.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.53 | 5.54 | 4.28 | 0.71 | 11.10 | 100.00 | 0.00 |
| 0.25 | 1.66 | 1.00 | 0.59 | 0.07 | 2.48 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.07 (IoU 95.34) | 1.93 (IoU 1.97) |
| silence | 2.03 (IoU 2.07) | 14.96 (IoU 79.05) |

Speech P/R/F1: 97.56 / 97.67 / 97.61; miss 2.33 of ref speech, FA 11.95 of ref silence, SAD error 4.78.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12835 | 92.57 | 90.68 | 91.62 | 0.043 | 0.030 | -0.006 | 0.000 |
| 0.25 | offset | 13103 | 12835 | 92.78 | 90.88 | 91.82 | 0.044 | 0.030 | -0.001 | 0.000 |
| 0.25 | all | 26206 | 25670 | 92.68 | 90.78 | 91.72 | 0.043 | 0.030 | -0.003 | 0.000 |
| 0.50 | onset | 13103 | 12835 | 93.46 | 91.55 | 92.50 | 0.046 | 0.030 | -0.005 | 0.000 |
| 0.50 | offset | 13103 | 12835 | 93.66 | 91.74 | 92.69 | 0.047 | 0.030 | -0.001 | 0.000 |
| 0.50 | all | 26206 | 25670 | 93.56 | 91.65 | 92.59 | 0.046 | 0.030 | -0.003 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.45 | 9.73 | 1.14 | 1.36 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.37 | 11.83 | 1.74 | 2.76 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.20 | 10.40 | 1.28 | 1.63 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.04 | 22.46 | 5.34 | 7.90 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.93 | 19.91 | 2.80 | 3.04 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.40 | 7.42 | 1.61 | 1.71 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.04 | 19.12 | 8.02 | 7.92 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.00 | 10.55 | 1.90 | 2.08 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.96 | 7.68 | 0.73 | 0.88 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.21 | 10.46 | 1.92 | 2.18 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.62 | 9.98 | 1.30 | 2.25 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.56 | 6.41 | 0.46 | 0.59 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.35 | 7.04 | 0.64 | 0.63 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.23 | 6.88 | 1.18 | 1.41 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.44 | 12.85 | 0.89 | 1.08 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.52 | 4.44 | 0.78 | 0.78 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.01 | 6.75 | 0.69 | 0.61 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.46 | 8.24 | 1.02 | 1.16 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.19 | 6.00 | 1.81 | 1.75 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.35 | 6.19 | 1.28 | 1.26 | 2 | 2 |
