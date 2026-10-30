# Diarization scores: A-fa-r0-seed43_s875/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r0-seed43_s875/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s875/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T19:34:09+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r0-seed43_s875`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7721-epoch=6.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.75 | 7.57 | 4.39 | 0.79 | 13.43 | 100.00 | 0.00 |
| 0.25 | 2.47 | 1.77 | 0.55 | 0.15 | 4.18 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 80.76 (IoU 94.08) | 2.58 (IoU 2.65) |
| silence | 2.50 (IoU 2.56) | 14.16 (IoU 73.59) |

Speech P/R/F1: 97.00 / 96.90 / 96.95; miss 3.10 of ref speech, FA 15.00 of ref silence, SAD error 6.10.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13093 | 13229 | 88.31 | 89.23 | 88.77 | 0.047 | 0.040 | 0.018 | 0.020 |
| 0.25 | offset | 13099 | 13223 | 88.70 | 89.54 | 89.12 | 0.057 | 0.050 | 0.035 | 0.040 |
| 0.25 | all | 26192 | 26452 | 88.51 | 89.39 | 88.94 | 0.052 | 0.040 | 0.027 | 0.030 |
| 0.50 | onset | 13093 | 13229 | 89.42 | 90.35 | 89.88 | 0.051 | 0.040 | 0.020 | 0.020 |
| 0.50 | offset | 13099 | 13223 | 89.60 | 90.45 | 90.02 | 0.060 | 0.050 | 0.036 | 0.040 |
| 0.50 | all | 26192 | 26452 | 89.51 | 90.40 | 89.95 | 0.055 | 0.040 | 0.028 | 0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 13.56 | 14.05 | 1.78 | 2.18 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.78 | 13.61 | 2.17 | 3.70 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.25 | 10.49 | 1.49 | 1.80 | 4 | 4 |
| R8004_M8006__far_ch1 | 18.59 | 20.91 | 5.32 | 7.28 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.58 | 18.75 | 3.02 | 3.39 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.53 | 8.59 | 1.99 | 2.23 | 4 | 4 |
| R8005_M8009__far_ch1 | 38.96 | 40.28 | 26.51 | 28.94 | 4 | 4 |
| R8006_M8012__far_ch1 | 13.07 | 13.80 | 3.72 | 4.48 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.55 | 8.26 | 0.78 | 0.91 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.11 | 11.32 | 1.97 | 2.21 | 3 | 3 |
| R8008_M8016__far_ch1 | 10.02 | 12.58 | 1.47 | 2.43 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.91 | 6.78 | 0.65 | 0.81 | 3 | 3 |
| R8009_M8021__far_ch1 | 11.07 | 10.40 | 0.62 | 0.61 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.54 | 8.20 | 0.88 | 1.13 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.11 | 9.61 | 0.78 | 0.99 | 2 | 2 |
| R8009_M8024__far_ch1 | 6.86 | 6.72 | 0.78 | 0.77 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.50 | 7.90 | 0.75 | 0.63 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.04 | 7.99 | 0.92 | 1.04 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.70 | 6.50 | 1.80 | 1.73 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.37 | 6.25 | 0.83 | 0.83 | 2 | 2 |
