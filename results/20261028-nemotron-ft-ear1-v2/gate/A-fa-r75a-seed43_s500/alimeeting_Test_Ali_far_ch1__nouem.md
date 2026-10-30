# Diarization scores: A-fa-r75a-seed43_s500/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75a-seed43_s500/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T04:21:23+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75a-seed43_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7752-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.77 | 5.51 | 4.56 | 0.70 | 11.28 | 100.00 | 0.00 |
| 0.25 | 2.05 | 1.02 | 0.96 | 0.06 | 2.67 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.42 (IoU 95.31) | 1.94 (IoU 1.98) |
| silence | 2.07 (IoU 2.11) | 14.58 (IoU 78.45) |

Speech P/R/F1: 97.53 / 97.67 / 97.60; miss 2.33 of ref speech, FA 12.41 of ref silence, SAD error 4.80.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13097 | 12711 | 92.79 | 90.06 | 91.41 | 0.042 | 0.030 | -0.000 | 0.000 |
| 0.25 | offset | 13097 | 12712 | 93.03 | 90.30 | 91.64 | 0.045 | 0.030 | 0.006 | 0.010 |
| 0.25 | all | 26194 | 25423 | 92.91 | 90.18 | 91.52 | 0.043 | 0.030 | 0.003 | 0.010 |
| 0.50 | onset | 13097 | 12711 | 93.67 | 90.91 | 92.27 | 0.045 | 0.030 | 0.000 | 0.000 |
| 0.50 | offset | 13097 | 12712 | 93.86 | 91.10 | 92.46 | 0.048 | 0.030 | 0.006 | 0.010 |
| 0.50 | all | 26194 | 25423 | 93.77 | 91.01 | 92.36 | 0.046 | 0.030 | 0.003 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.39 | 10.63 | 1.25 | 1.52 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.51 | 12.13 | 1.78 | 2.89 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.01 | 10.19 | 1.40 | 1.80 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.64 | 21.92 | 5.19 | 7.39 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.67 | 19.65 | 2.82 | 3.08 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.31 | 7.31 | 1.60 | 1.70 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.70 | 18.71 | 7.67 | 7.44 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.31 | 10.85 | 1.97 | 2.13 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.80 | 7.47 | 0.71 | 0.86 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.34 | 10.49 | 1.89 | 2.14 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.06 | 10.78 | 1.57 | 2.82 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.27 | 6.25 | 0.54 | 0.76 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.65 | 7.30 | 0.60 | 0.59 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.64 | 7.34 | 1.24 | 1.55 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.19 | 12.54 | 1.26 | 1.50 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.50 | 4.42 | 0.63 | 0.63 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.26 | 7.10 | 0.85 | 0.77 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.51 | 8.31 | 1.03 | 1.17 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.04 | 5.87 | 1.71 | 1.65 | 2 | 2 |
| R8009_M8028__far_ch1 | 11.58 | 10.26 | 7.44 | 6.45 | 2 | 2 |
