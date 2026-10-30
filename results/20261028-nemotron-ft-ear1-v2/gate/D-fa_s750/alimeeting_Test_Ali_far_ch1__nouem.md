# Diarization scores: D-fa_s750/alimeeting_Test_Ali_far_ch1__nouem

- name: `D-fa_s750/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-fa_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T00:13:03+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `D-fa_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7691-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.86 | 8.41 | 2.91 | 0.53 | 12.55 | 100.00 | 0.00 |
| 0.25 | 1.99 | 1.58 | 0.37 | 0.04 | 3.06 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.12 (IoU 95.13) | 2.24 (IoU 2.28) |
| silence | 1.91 (IoU 1.96) | 14.73 (IoU 78.00) |

Speech P/R/F1: 97.69 / 97.31 / 97.50; miss 2.69 of ref speech, FA 11.51 of ref silence, SAD error 4.98.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 13602 | 88.67 | 92.08 | 90.34 | 0.042 | 0.030 | -0.003 | 0.000 |
| 0.25 | offset | 13096 | 13605 | 88.83 | 92.29 | 90.53 | 0.046 | 0.030 | -0.003 | 0.000 |
| 0.25 | all | 26194 | 27207 | 88.75 | 92.19 | 90.44 | 0.044 | 0.030 | -0.003 | 0.000 |
| 0.50 | onset | 13098 | 13602 | 89.60 | 93.04 | 91.29 | 0.045 | 0.030 | -0.002 | 0.000 |
| 0.50 | offset | 13096 | 13605 | 89.76 | 93.25 | 91.47 | 0.049 | 0.030 | -0.004 | 0.000 |
| 0.50 | all | 26194 | 27207 | 89.68 | 93.15 | 91.38 | 0.047 | 0.030 | -0.003 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.97 | 11.42 | 1.58 | 1.85 | 4 | 4 |
| R8002_M8003__far_ch1 | 12.08 | 13.96 | 2.01 | 3.18 | 4 | 4 |
| R8004_M8005__far_ch1 | 10.35 | 11.87 | 1.71 | 2.18 | 4 | 4 |
| R8004_M8006__far_ch1 | 24.86 | 27.69 | 8.39 | 10.56 | 4 | 4 |
| R8005_M8007__far_ch1 | 22.76 | 22.79 | 4.15 | 4.34 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.80 | 8.99 | 2.10 | 2.39 | 4 | 4 |
| R8005_M8009__far_ch1 | 23.19 | 23.01 | 9.91 | 9.73 | 4 | 4 |
| R8006_M8012__far_ch1 | 11.51 | 12.08 | 2.57 | 2.93 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.14 | 7.91 | 0.86 | 1.07 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.04 | 11.48 | 1.99 | 2.26 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.83 | 10.58 | 1.36 | 2.33 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.73 | 6.71 | 0.56 | 0.73 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.10 | 6.81 | 0.56 | 0.55 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.39 | 7.09 | 1.04 | 1.27 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.35 | 12.67 | 0.81 | 1.00 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.62 | 4.51 | 0.75 | 0.75 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.07 | 6.92 | 0.67 | 0.62 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.49 | 8.23 | 0.93 | 1.05 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.06 | 5.87 | 1.62 | 1.56 | 2 | 2 |
| R8009_M8028__far_ch1 | 5.96 | 5.84 | 0.98 | 0.98 | 2 | 2 |
