# Diarization scores: A-fa-r75a-seed43_s1250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75a-seed43_s1250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T04:55:11+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75a-seed43_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7883-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.59 | 5.53 | 4.36 | 0.70 | 11.19 | 100.00 | 0.00 |
| 0.25 | 1.72 | 1.03 | 0.62 | 0.07 | 2.51 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.38 (IoU 95.28) | 1.98 (IoU 2.02) |
| silence | 2.05 (IoU 2.09) | 14.59 (IoU 78.36) |

Speech P/R/F1: 97.54 / 97.63 / 97.58; miss 2.37 of ref speech, FA 12.33 of ref silence, SAD error 4.83.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13097 | 12786 | 92.57 | 90.37 | 91.46 | 0.042 | 0.030 | 0.000 | 0.000 |
| 0.25 | offset | 13097 | 12786 | 92.83 | 90.62 | 91.71 | 0.046 | 0.030 | 0.005 | 0.010 |
| 0.25 | all | 26194 | 25572 | 92.70 | 90.50 | 91.59 | 0.044 | 0.030 | 0.003 | 0.010 |
| 0.50 | onset | 13097 | 12786 | 93.46 | 91.24 | 92.34 | 0.045 | 0.030 | 0.001 | 0.000 |
| 0.50 | offset | 13097 | 12786 | 93.64 | 91.42 | 92.52 | 0.048 | 0.040 | 0.005 | 0.010 |
| 0.50 | all | 26194 | 25572 | 93.55 | 91.33 | 92.43 | 0.047 | 0.030 | 0.003 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.91 | 10.17 | 1.22 | 1.48 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.67 | 12.31 | 1.88 | 3.06 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.21 | 10.40 | 1.39 | 1.78 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.70 | 22.00 | 5.03 | 7.19 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.61 | 19.56 | 2.78 | 3.02 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.39 | 7.39 | 1.63 | 1.71 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.84 | 18.87 | 7.74 | 7.57 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.27 | 10.83 | 2.04 | 2.22 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.91 | 7.66 | 0.77 | 0.93 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.37 | 10.55 | 1.85 | 2.09 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.84 | 10.44 | 1.40 | 2.42 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.46 | 6.43 | 0.63 | 0.84 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.17 | 7.79 | 0.65 | 0.64 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.77 | 7.49 | 1.22 | 1.51 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.87 | 13.29 | 1.26 | 1.47 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.38 | 4.28 | 0.66 | 0.64 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.84 | 6.68 | 0.66 | 0.62 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.16 | 7.99 | 1.02 | 1.15 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.14 | 6.00 | 1.89 | 1.83 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.67 | 6.48 | 1.85 | 1.80 | 2 | 2 |
