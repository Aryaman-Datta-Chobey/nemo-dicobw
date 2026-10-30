# Diarization scores: A-fa-r0_s1125/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r0_s1125/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s1125/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T18:33:12+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r0_s1125`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7885-epoch=8.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 15.77 | 10.79 | 4.19 | 0.79 | 16.39 | 100.00 | 0.00 |
| 0.25 | 4.22 | 3.56 | 0.46 | 0.21 | 7.31 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 78.53 (IoU 91.50) | 4.82 (IoU 4.95) |
| silence | 2.47 (IoU 2.60) | 14.17 (IoU 66.02) |

Speech P/R/F1: 96.95 / 94.21 / 95.56; miss 5.79 of ref speech, FA 14.85 of ref silence, SAD error 8.75.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13092 | 13793 | 84.21 | 88.72 | 86.41 | 0.048 | 0.040 | 0.020 | 0.020 |
| 0.25 | offset | 13099 | 13788 | 84.56 | 89.01 | 86.73 | 0.058 | 0.050 | 0.036 | 0.040 |
| 0.25 | all | 26191 | 27581 | 84.38 | 88.86 | 86.57 | 0.053 | 0.040 | 0.028 | 0.030 |
| 0.50 | onset | 13092 | 13793 | 85.52 | 90.10 | 87.75 | 0.053 | 0.040 | 0.021 | 0.020 |
| 0.50 | offset | 13099 | 13788 | 85.49 | 89.98 | 87.68 | 0.061 | 0.050 | 0.037 | 0.040 |
| 0.50 | all | 26191 | 27581 | 85.50 | 90.04 | 87.71 | 0.057 | 0.050 | 0.029 | 0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 12.99 | 13.44 | 1.40 | 1.72 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.51 | 13.28 | 1.93 | 3.17 | 4 | 4 |
| R8004_M8005__far_ch1 | 10.64 | 11.83 | 2.40 | 2.72 | 4 | 4 |
| R8004_M8006__far_ch1 | 18.55 | 21.00 | 5.27 | 7.43 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.56 | 18.74 | 2.94 | 3.27 | 4 | 4 |
| R8005_M8008__far_ch1 | 9.37 | 9.64 | 2.60 | 3.12 | 4 | 4 |
| R8005_M8009__far_ch1 | 75.53 | 75.69 | 66.89 | 68.95 | 4 | 4 |
| R8006_M8012__far_ch1 | 17.74 | 19.13 | 7.67 | 9.32 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.57 | 8.31 | 0.82 | 0.97 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.22 | 11.54 | 1.98 | 2.24 | 3 | 3 |
| R8008_M8016__far_ch1 | 11.11 | 13.71 | 2.07 | 3.25 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.81 | 6.71 | 0.61 | 0.79 | 3 | 3 |
| R8009_M8021__far_ch1 | 12.16 | 11.39 | 0.72 | 0.71 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.41 | 8.11 | 0.83 | 1.11 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.04 | 9.72 | 0.75 | 0.95 | 2 | 2 |
| R8009_M8024__far_ch1 | 9.09 | 8.99 | 2.58 | 2.73 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.26 | 7.68 | 0.68 | 0.56 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.85 | 7.78 | 0.79 | 0.88 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.29 | 6.10 | 1.52 | 1.46 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.19 | 6.07 | 0.68 | 0.68 | 2 | 2 |
