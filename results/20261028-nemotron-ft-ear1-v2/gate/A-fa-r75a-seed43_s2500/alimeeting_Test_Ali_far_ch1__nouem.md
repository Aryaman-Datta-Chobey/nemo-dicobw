# Diarization scores: A-fa-r75a-seed43_s2500/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75a-seed43_s2500/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s2500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T05:52:49+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75a-seed43_s2500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7851-epoch=9.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.62 | 5.60 | 4.31 | 0.71 | 11.23 | 100.00 | 0.00 |
| 0.25 | 1.72 | 1.08 | 0.58 | 0.06 | 2.51 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.35 (IoU 95.24) | 2.01 (IoU 2.05) |
| silence | 2.06 (IoU 2.10) | 14.59 (IoU 78.19) |

Speech P/R/F1: 97.53 / 97.59 / 97.56; miss 2.41 of ref speech, FA 12.37 of ref silence, SAD error 4.88.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 12830 | 92.24 | 90.36 | 91.29 | 0.043 | 0.030 | 0.001 | 0.000 |
| 0.25 | offset | 13097 | 12830 | 92.54 | 90.65 | 91.59 | 0.046 | 0.040 | 0.006 | 0.010 |
| 0.25 | all | 26195 | 25660 | 92.39 | 90.51 | 91.44 | 0.044 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13098 | 12830 | 93.17 | 91.27 | 92.21 | 0.046 | 0.030 | 0.002 | 0.000 |
| 0.50 | offset | 13097 | 12830 | 93.31 | 91.41 | 92.35 | 0.049 | 0.040 | 0.007 | 0.010 |
| 0.50 | all | 26195 | 25660 | 93.24 | 91.34 | 92.28 | 0.047 | 0.030 | 0.004 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.92 | 10.18 | 1.15 | 1.36 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.54 | 12.13 | 1.74 | 2.84 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.23 | 10.41 | 1.40 | 1.81 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.86 | 22.23 | 5.26 | 7.40 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.58 | 19.56 | 2.83 | 3.05 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.43 | 7.43 | 1.68 | 1.76 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.82 | 18.86 | 7.89 | 7.62 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.28 | 10.86 | 2.09 | 2.27 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.96 | 7.72 | 0.86 | 1.00 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.58 | 11.11 | 2.01 | 2.36 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.65 | 10.20 | 1.35 | 2.38 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.41 | 6.32 | 0.66 | 0.81 | 3 | 3 |
| R8009_M8021__far_ch1 | 9.07 | 8.62 | 0.69 | 0.68 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.89 | 7.59 | 1.14 | 1.42 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.41 | 12.79 | 1.25 | 1.47 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.62 | 4.55 | 0.88 | 0.87 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.03 | 6.86 | 0.73 | 0.68 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.17 | 7.97 | 0.98 | 1.10 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.16 | 5.99 | 1.87 | 1.79 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.23 | 6.11 | 1.20 | 1.19 | 2 | 2 |
