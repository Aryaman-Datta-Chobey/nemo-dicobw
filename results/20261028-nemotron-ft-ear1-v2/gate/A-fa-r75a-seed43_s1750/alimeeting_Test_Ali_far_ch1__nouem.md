# Diarization scores: A-fa-r75a-seed43_s1750/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75a-seed43_s1750/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s1750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T05:17:17+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75a-seed43_s1750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7849-epoch=6.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.61 | 5.68 | 4.21 | 0.71 | 11.23 | 100.00 | 0.00 |
| 0.25 | 1.72 | 1.08 | 0.57 | 0.07 | 2.52 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.29 (IoU 95.26) | 2.06 (IoU 2.11) |
| silence | 1.98 (IoU 2.02) | 14.66 (IoU 78.38) |

Speech P/R/F1: 97.62 / 97.52 / 97.57; miss 2.48 of ref speech, FA 11.90 of ref silence, SAD error 4.85.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13097 | 12821 | 92.25 | 90.30 | 91.26 | 0.042 | 0.030 | -0.001 | 0.000 |
| 0.25 | offset | 13096 | 12823 | 92.56 | 90.63 | 91.59 | 0.045 | 0.030 | 0.001 | 0.010 |
| 0.25 | all | 26193 | 25644 | 92.40 | 90.47 | 91.43 | 0.044 | 0.030 | 0.000 | 0.000 |
| 0.50 | onset | 13097 | 12821 | 93.21 | 91.24 | 92.21 | 0.046 | 0.030 | 0.000 | 0.000 |
| 0.50 | offset | 13096 | 12823 | 93.33 | 91.39 | 92.35 | 0.047 | 0.030 | 0.001 | 0.010 |
| 0.50 | all | 26193 | 25644 | 93.27 | 91.31 | 92.28 | 0.046 | 0.030 | 0.001 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.52 | 9.80 | 1.14 | 1.34 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.47 | 12.11 | 1.76 | 2.83 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.27 | 10.43 | 1.37 | 1.77 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.07 | 22.49 | 5.18 | 7.56 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.70 | 19.68 | 2.75 | 2.97 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.40 | 7.42 | 1.65 | 1.74 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.90 | 18.98 | 7.84 | 7.66 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.31 | 10.89 | 2.04 | 2.20 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.89 | 7.66 | 0.81 | 0.94 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.53 | 11.01 | 2.00 | 2.39 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.64 | 10.22 | 1.33 | 2.35 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.40 | 6.38 | 0.63 | 0.84 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.24 | 7.87 | 0.72 | 0.71 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.88 | 7.60 | 1.26 | 1.54 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.94 | 13.37 | 1.15 | 1.39 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.48 | 4.40 | 0.92 | 0.92 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.69 | 6.51 | 0.67 | 0.59 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.39 | 8.19 | 1.06 | 1.18 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.23 | 6.09 | 1.96 | 1.89 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.37 | 6.23 | 1.36 | 1.34 | 2 | 2 |
