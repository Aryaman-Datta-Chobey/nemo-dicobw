# Diarization scores: A-fa-r75b-seed43_s1500/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75b-seed43_s1500/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s1500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T07:28:59+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75b-seed43_s1500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7953-epoch=5.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.57 | 5.54 | 4.31 | 0.72 | 11.20 | 100.00 | 0.00 |
| 0.25 | 1.71 | 1.02 | 0.61 | 0.07 | 2.52 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.35 (IoU 95.30) | 1.99 (IoU 2.03) |
| silence | 2.02 (IoU 2.06) | 14.64 (IoU 78.50) |

Speech P/R/F1: 97.58 / 97.61 / 97.60; miss 2.39 of ref speech, FA 12.13 of ref silence, SAD error 4.81.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 12770 | 92.56 | 90.24 | 91.39 | 0.042 | 0.030 | 0.001 | 0.000 |
| 0.25 | offset | 13098 | 12771 | 92.80 | 90.49 | 91.63 | 0.045 | 0.030 | 0.004 | 0.010 |
| 0.25 | all | 26196 | 25541 | 92.68 | 90.36 | 91.51 | 0.044 | 0.030 | 0.002 | 0.010 |
| 0.50 | onset | 13098 | 12770 | 93.49 | 91.15 | 92.31 | 0.045 | 0.030 | 0.001 | 0.000 |
| 0.50 | offset | 13098 | 12771 | 93.61 | 91.27 | 92.43 | 0.047 | 0.030 | 0.004 | 0.010 |
| 0.50 | all | 26196 | 25541 | 93.55 | 91.21 | 92.37 | 0.046 | 0.030 | 0.003 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.88 | 10.17 | 1.02 | 1.22 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.85 | 12.56 | 2.06 | 3.40 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.20 | 10.37 | 1.32 | 1.66 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.73 | 22.12 | 5.19 | 7.53 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.57 | 19.49 | 2.80 | 3.02 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.35 | 7.36 | 1.54 | 1.64 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.74 | 18.82 | 7.63 | 7.43 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.39 | 10.97 | 2.03 | 2.23 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.83 | 7.60 | 0.81 | 0.95 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.55 | 11.04 | 1.96 | 2.43 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.66 | 10.27 | 1.36 | 2.35 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.46 | 6.43 | 0.65 | 0.85 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.56 | 8.16 | 0.73 | 0.72 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.72 | 7.43 | 1.20 | 1.49 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.08 | 12.52 | 1.03 | 1.31 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.40 | 4.31 | 0.69 | 0.68 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.07 | 6.78 | 0.75 | 0.65 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.09 | 7.91 | 0.95 | 1.07 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.05 | 5.90 | 1.82 | 1.75 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.52 | 6.35 | 1.74 | 1.70 | 2 | 2 |
