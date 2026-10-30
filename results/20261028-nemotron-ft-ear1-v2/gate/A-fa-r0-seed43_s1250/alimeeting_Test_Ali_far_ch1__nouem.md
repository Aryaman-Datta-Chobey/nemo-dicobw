# Diarization scores: A-fa-r0-seed43_s1250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r0-seed43_s1250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T20:10:45+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r0-seed43_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7734-epoch=9.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.54 | 7.40 | 4.42 | 0.72 | 13.15 | 100.00 | 0.00 |
| 0.25 | 2.40 | 1.75 | 0.55 | 0.11 | 3.77 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 80.71 (IoU 94.00) | 2.64 (IoU 2.70) |
| silence | 2.52 (IoU 2.58) | 14.14 (IoU 73.30) |

Speech P/R/F1: 96.98 / 96.84 / 96.91; miss 3.16 of ref speech, FA 15.10 of ref silence, SAD error 6.18.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13093 | 13147 | 88.59 | 88.96 | 88.77 | 0.048 | 0.040 | 0.021 | 0.020 |
| 0.25 | offset | 13098 | 13141 | 89.03 | 89.32 | 89.17 | 0.058 | 0.050 | 0.036 | 0.040 |
| 0.25 | all | 26191 | 26288 | 88.81 | 89.14 | 88.97 | 0.053 | 0.050 | 0.029 | 0.030 |
| 0.50 | onset | 13093 | 13147 | 89.88 | 90.25 | 90.06 | 0.053 | 0.040 | 0.022 | 0.020 |
| 0.50 | offset | 13098 | 13141 | 89.99 | 90.29 | 90.14 | 0.061 | 0.050 | 0.037 | 0.040 |
| 0.50 | all | 26191 | 26288 | 89.93 | 90.27 | 90.10 | 0.057 | 0.050 | 0.029 | 0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 12.88 | 13.20 | 1.20 | 1.45 | 4 | 4 |
| R8002_M8003__far_ch1 | 12.05 | 13.88 | 2.29 | 3.64 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.22 | 10.44 | 1.42 | 1.78 | 4 | 4 |
| R8004_M8006__far_ch1 | 18.49 | 20.84 | 5.18 | 7.23 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.21 | 18.39 | 2.92 | 3.28 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.31 | 8.29 | 1.87 | 2.06 | 4 | 4 |
| R8005_M8009__far_ch1 | 33.13 | 32.85 | 21.84 | 21.48 | 4 | 4 |
| R8006_M8012__far_ch1 | 15.70 | 16.53 | 5.05 | 6.04 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.66 | 8.35 | 0.82 | 0.98 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.07 | 11.18 | 1.89 | 2.09 | 3 | 3 |
| R8008_M8016__far_ch1 | 10.44 | 13.10 | 1.56 | 2.64 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.99 | 6.84 | 0.61 | 0.79 | 3 | 3 |
| R8009_M8021__far_ch1 | 11.42 | 10.74 | 0.67 | 0.66 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.55 | 8.22 | 0.85 | 1.11 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.23 | 9.71 | 0.77 | 0.99 | 2 | 2 |
| R8009_M8024__far_ch1 | 9.12 | 8.91 | 2.68 | 2.69 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.52 | 7.94 | 0.70 | 0.58 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.07 | 8.01 | 0.84 | 0.93 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.74 | 6.55 | 1.67 | 1.61 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.42 | 6.31 | 0.78 | 0.78 | 2 | 2 |
