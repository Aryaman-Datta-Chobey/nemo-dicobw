# Diarization scores: A-fa-r0-seed43_s1125/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r0-seed43_s1125/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s1125/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T19:58:34+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r0-seed43_s1125`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7843-epoch=8.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.12 | 6.81 | 4.54 | 0.76 | 12.79 | 100.00 | 0.00 |
| 0.25 | 2.24 | 1.52 | 0.58 | 0.14 | 3.58 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.01 (IoU 94.30) | 2.33 (IoU 2.40) |
| silence | 2.56 (IoU 2.62) | 14.10 (IoU 74.22) |

Speech P/R/F1: 96.94 / 97.20 / 97.07; miss 2.80 of ref speech, FA 15.38 of ref silence, SAD error 5.87.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13093 | 13092 | 89.63 | 89.62 | 89.62 | 0.048 | 0.040 | 0.020 | 0.020 |
| 0.25 | offset | 13099 | 13086 | 89.88 | 89.79 | 89.84 | 0.058 | 0.050 | 0.037 | 0.040 |
| 0.25 | all | 26192 | 26178 | 89.75 | 89.71 | 89.73 | 0.053 | 0.040 | 0.029 | 0.030 |
| 0.50 | onset | 13093 | 13092 | 90.67 | 90.66 | 90.66 | 0.051 | 0.040 | 0.021 | 0.020 |
| 0.50 | offset | 13099 | 13086 | 90.80 | 90.71 | 90.75 | 0.061 | 0.050 | 0.038 | 0.040 |
| 0.50 | all | 26192 | 26178 | 90.73 | 90.68 | 90.71 | 0.056 | 0.050 | 0.029 | 0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 12.86 | 13.19 | 1.33 | 1.61 | 4 | 4 |
| R8002_M8003__far_ch1 | 12.24 | 13.98 | 3.30 | 4.96 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.20 | 10.46 | 1.47 | 1.80 | 4 | 4 |
| R8004_M8006__far_ch1 | 18.47 | 20.77 | 5.09 | 7.00 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.19 | 18.39 | 2.81 | 3.18 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.05 | 8.06 | 1.76 | 1.97 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.58 | 29.20 | 17.24 | 18.22 | 4 | 4 |
| R8006_M8012__far_ch1 | 14.36 | 15.07 | 4.40 | 5.23 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.64 | 8.34 | 0.84 | 1.01 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.02 | 11.19 | 1.92 | 2.16 | 3 | 3 |
| R8008_M8016__far_ch1 | 10.84 | 13.61 | 1.92 | 3.15 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.95 | 6.82 | 0.57 | 0.77 | 3 | 3 |
| R8009_M8021__far_ch1 | 11.65 | 10.94 | 0.67 | 0.66 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.50 | 8.17 | 0.84 | 1.11 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.15 | 9.61 | 0.73 | 0.94 | 2 | 2 |
| R8009_M8024__far_ch1 | 8.85 | 8.66 | 2.40 | 2.41 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.44 | 7.87 | 0.69 | 0.57 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.75 | 7.70 | 0.78 | 0.87 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.58 | 6.38 | 1.58 | 1.52 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.26 | 6.14 | 0.77 | 0.77 | 2 | 2 |
