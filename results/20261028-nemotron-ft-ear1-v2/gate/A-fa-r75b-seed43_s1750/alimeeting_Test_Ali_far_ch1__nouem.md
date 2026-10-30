# Diarization scores: A-fa-r75b-seed43_s1750/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75b-seed43_s1750/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s1750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T07:38:28+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75b-seed43_s1750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7812-epoch=6.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.76 | 5.66 | 4.38 | 0.71 | 11.34 | 100.00 | 0.00 |
| 0.25 | 1.94 | 1.09 | 0.79 | 0.07 | 2.72 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.30 (IoU 95.24) | 2.04 (IoU 2.08) |
| silence | 2.03 (IoU 2.07) | 14.63 (IoU 78.25) |

Speech P/R/F1: 97.57 / 97.55 / 97.56; miss 2.45 of ref speech, FA 12.18 of ref silence, SAD error 4.88.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 12790 | 92.30 | 90.13 | 91.20 | 0.042 | 0.030 | 0.001 | 0.000 |
| 0.25 | offset | 13097 | 12791 | 92.58 | 90.42 | 91.49 | 0.045 | 0.030 | 0.004 | 0.010 |
| 0.25 | all | 26195 | 25581 | 92.44 | 90.27 | 91.34 | 0.044 | 0.030 | 0.003 | 0.010 |
| 0.50 | onset | 13098 | 12790 | 93.22 | 91.03 | 92.11 | 0.045 | 0.030 | 0.001 | 0.000 |
| 0.50 | offset | 13097 | 12791 | 93.35 | 91.17 | 92.25 | 0.048 | 0.030 | 0.004 | 0.010 |
| 0.50 | all | 26195 | 25581 | 93.29 | 91.10 | 92.18 | 0.047 | 0.030 | 0.003 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.95 | 10.23 | 1.09 | 1.31 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.08 | 12.68 | 2.51 | 4.18 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.13 | 10.27 | 1.37 | 1.75 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.78 | 22.15 | 5.23 | 7.52 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.57 | 19.54 | 2.85 | 3.06 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.36 | 7.38 | 1.60 | 1.70 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.85 | 18.90 | 7.95 | 7.80 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.38 | 10.93 | 2.11 | 2.29 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.90 | 7.64 | 0.82 | 0.95 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.62 | 11.04 | 2.00 | 2.34 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.85 | 10.45 | 1.34 | 2.33 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.51 | 6.49 | 0.66 | 0.87 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.48 | 8.09 | 0.84 | 0.82 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.82 | 7.53 | 1.23 | 1.54 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.51 | 13.00 | 1.23 | 1.50 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.57 | 4.48 | 0.82 | 0.81 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.09 | 6.84 | 0.74 | 0.64 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.29 | 8.11 | 1.02 | 1.13 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.33 | 6.19 | 2.06 | 2.00 | 2 | 2 |
| R8009_M8028__far_ch1 | 8.84 | 8.24 | 4.35 | 4.02 | 2 | 2 |
