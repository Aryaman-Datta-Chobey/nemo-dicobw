# Diarization scores: A-fa-r0_s750/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r0_s750/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T17:58:00+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r0_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7802-epoch=5.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.37 | 7.32 | 4.34 | 0.72 | 13.05 | 100.00 | 0.00 |
| 0.25 | 2.22 | 1.59 | 0.53 | 0.10 | 3.83 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 80.93 (IoU 94.30) | 2.43 (IoU 2.49) |
| silence | 2.46 (IoU 2.52) | 14.19 (IoU 74.37) |

Speech P/R/F1: 97.05 / 97.08 / 97.07; miss 2.92 of ref speech, FA 14.77 of ref silence, SAD error 5.86.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13093 | 13208 | 89.20 | 89.99 | 89.59 | 0.046 | 0.040 | 0.018 | 0.020 |
| 0.25 | offset | 13100 | 13203 | 89.46 | 90.17 | 89.81 | 0.056 | 0.050 | 0.033 | 0.040 |
| 0.25 | all | 26193 | 26411 | 89.33 | 90.08 | 89.70 | 0.051 | 0.040 | 0.026 | 0.030 |
| 0.50 | onset | 13093 | 13208 | 90.13 | 90.92 | 90.52 | 0.049 | 0.040 | 0.018 | 0.020 |
| 0.50 | offset | 13100 | 13203 | 90.26 | 90.97 | 90.61 | 0.058 | 0.050 | 0.034 | 0.040 |
| 0.50 | all | 26193 | 26411 | 90.19 | 90.94 | 90.57 | 0.054 | 0.040 | 0.026 | 0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 12.32 | 12.58 | 1.09 | 1.30 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.38 | 13.06 | 1.86 | 2.89 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.10 | 10.54 | 1.54 | 2.08 | 4 | 4 |
| R8004_M8006__far_ch1 | 18.55 | 20.99 | 5.27 | 7.43 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.57 | 18.75 | 2.95 | 3.29 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.34 | 8.52 | 1.90 | 2.26 | 4 | 4 |
| R8005_M8009__far_ch1 | 38.06 | 39.33 | 23.81 | 26.43 | 4 | 4 |
| R8006_M8012__far_ch1 | 12.13 | 12.82 | 3.12 | 3.67 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.42 | 8.12 | 0.75 | 0.88 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.44 | 11.88 | 2.01 | 2.39 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.88 | 11.51 | 1.19 | 2.24 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.64 | 6.52 | 0.58 | 0.75 | 3 | 3 |
| R8009_M8021__far_ch1 | 11.63 | 10.89 | 0.57 | 0.56 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.31 | 7.98 | 0.84 | 1.11 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.93 | 9.59 | 0.70 | 0.91 | 2 | 2 |
| R8009_M8024__far_ch1 | 6.17 | 6.06 | 0.51 | 0.50 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.15 | 7.58 | 0.65 | 0.55 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.60 | 7.53 | 0.78 | 0.87 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.15 | 5.95 | 1.64 | 1.57 | 2 | 2 |
| R8009_M8028__far_ch1 | 5.93 | 5.82 | 0.69 | 0.69 | 2 | 2 |
