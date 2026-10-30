# Diarization scores: A-fa-r75b-seed43_s500/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75b-seed43_s500/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T06:50:34+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75b-seed43_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7842-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.99 | 5.57 | 4.71 | 0.70 | 11.43 | 100.00 | 0.00 |
| 0.25 | 2.33 | 1.06 | 1.21 | 0.06 | 2.74 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.34 (IoU 95.24) | 2.02 (IoU 2.06) |
| silence | 2.05 (IoU 2.09) | 14.59 (IoU 78.20) |

Speech P/R/F1: 97.54 / 97.58 / 97.56; miss 2.42 of ref speech, FA 12.31 of ref silence, SAD error 4.88.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13097 | 12606 | 92.96 | 89.48 | 91.19 | 0.042 | 0.030 | -0.000 | 0.000 |
| 0.25 | offset | 13096 | 12607 | 93.27 | 89.79 | 91.50 | 0.045 | 0.030 | 0.005 | 0.010 |
| 0.25 | all | 26193 | 25213 | 93.12 | 89.63 | 91.34 | 0.043 | 0.030 | 0.003 | 0.010 |
| 0.50 | onset | 13097 | 12606 | 93.91 | 90.39 | 92.11 | 0.045 | 0.030 | 0.001 | 0.000 |
| 0.50 | offset | 13096 | 12607 | 94.13 | 90.62 | 92.34 | 0.048 | 0.030 | 0.005 | 0.010 |
| 0.50 | all | 26193 | 25213 | 94.02 | 90.50 | 92.23 | 0.046 | 0.030 | 0.003 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.36 | 10.64 | 1.12 | 1.35 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.75 | 12.41 | 1.75 | 2.86 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.97 | 10.14 | 1.27 | 1.65 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.38 | 21.66 | 5.01 | 7.31 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.52 | 19.51 | 2.72 | 2.92 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.22 | 7.24 | 1.45 | 1.57 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.67 | 18.68 | 7.58 | 7.30 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.34 | 10.95 | 1.89 | 2.06 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.97 | 7.63 | 0.69 | 0.82 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.51 | 10.87 | 1.85 | 2.09 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.96 | 10.59 | 1.36 | 2.34 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.41 | 6.28 | 0.61 | 0.71 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.23 | 6.93 | 0.70 | 0.68 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.85 | 7.50 | 1.35 | 1.63 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.89 | 13.18 | 1.65 | 2.04 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.99 | 4.95 | 1.08 | 1.11 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.24 | 7.02 | 0.77 | 0.69 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.69 | 8.53 | 1.14 | 1.30 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.40 | 6.28 | 1.91 | 1.86 | 2 | 2 |
| R8009_M8028__far_ch1 | 15.77 | 13.12 | 12.22 | 9.81 | 2 | 2 |
