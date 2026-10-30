# Diarization scores: A-fa-r75a-seed43_s1000/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75a-seed43_s1000/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T04:43:44+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75a-seed43_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7934-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.54 | 5.54 | 4.30 | 0.70 | 11.15 | 100.00 | 0.00 |
| 0.25 | 1.72 | 1.03 | 0.62 | 0.06 | 2.50 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.39 (IoU 95.31) | 1.97 (IoU 2.01) |
| silence | 2.04 (IoU 2.08) | 14.61 (IoU 78.48) |

Speech P/R/F1: 97.56 / 97.64 / 97.60; miss 2.36 of ref speech, FA 12.24 of ref silence, SAD error 4.80.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13096 | 12784 | 92.55 | 90.34 | 91.43 | 0.042 | 0.030 | 0.002 | 0.010 |
| 0.25 | offset | 13098 | 12784 | 92.85 | 90.62 | 91.72 | 0.045 | 0.030 | 0.007 | 0.010 |
| 0.25 | all | 26194 | 25568 | 92.70 | 90.48 | 91.58 | 0.044 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13096 | 12784 | 93.44 | 91.21 | 92.31 | 0.045 | 0.030 | 0.003 | 0.010 |
| 0.50 | offset | 13098 | 12784 | 93.61 | 91.37 | 92.47 | 0.048 | 0.040 | 0.007 | 0.010 |
| 0.50 | all | 26194 | 25568 | 93.52 | 91.29 | 92.39 | 0.046 | 0.030 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.14 | 10.41 | 1.21 | 1.47 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.59 | 12.21 | 1.80 | 2.87 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.12 | 10.32 | 1.43 | 1.84 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.68 | 22.06 | 5.26 | 7.52 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.34 | 19.31 | 2.83 | 3.07 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.32 | 7.32 | 1.60 | 1.70 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.64 | 18.70 | 7.72 | 7.44 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.22 | 10.77 | 2.02 | 2.18 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.98 | 7.68 | 0.83 | 0.98 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.53 | 10.79 | 1.84 | 2.11 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.64 | 10.17 | 1.32 | 2.33 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.37 | 6.34 | 0.62 | 0.83 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.38 | 7.98 | 0.66 | 0.65 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.82 | 7.54 | 1.24 | 1.54 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.08 | 12.52 | 1.02 | 1.31 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.38 | 4.30 | 0.69 | 0.67 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.07 | 6.92 | 0.69 | 0.66 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.18 | 8.02 | 0.99 | 1.11 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.07 | 5.93 | 1.85 | 1.79 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.74 | 6.53 | 1.81 | 1.76 | 2 | 2 |
