# Diarization scores: A-fa-r75a-seed43_s250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75a-seed43_s250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T04:10:30+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75a-seed43_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7693-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.58 | 5.58 | 4.32 | 0.68 | 11.12 | 100.00 | 0.00 |
| 0.25 | 1.81 | 0.98 | 0.78 | 0.06 | 2.49 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.38 (IoU 95.34) | 1.98 (IoU 2.02) |
| silence | 2.00 (IoU 2.04) | 14.64 (IoU 78.64) |

Speech P/R/F1: 97.60 / 97.63 / 97.62; miss 2.37 of ref speech, FA 12.01 of ref silence, SAD error 4.77.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 12820 | 92.59 | 90.62 | 91.60 | 0.042 | 0.030 | 0.002 | 0.010 |
| 0.25 | offset | 13096 | 12821 | 92.79 | 90.84 | 91.80 | 0.045 | 0.030 | 0.005 | 0.010 |
| 0.25 | all | 26194 | 25641 | 92.69 | 90.73 | 91.70 | 0.043 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13098 | 12820 | 93.47 | 91.49 | 92.47 | 0.045 | 0.030 | 0.003 | 0.010 |
| 0.50 | offset | 13096 | 12821 | 93.67 | 91.71 | 92.68 | 0.048 | 0.030 | 0.005 | 0.010 |
| 0.50 | all | 26194 | 25641 | 93.57 | 91.60 | 92.57 | 0.046 | 0.030 | 0.004 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.17 | 10.41 | 1.12 | 1.34 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.47 | 12.05 | 1.73 | 2.78 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.86 | 10.05 | 1.28 | 1.66 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.67 | 21.95 | 5.10 | 7.24 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.77 | 19.76 | 2.78 | 3.01 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.30 | 7.35 | 1.56 | 1.67 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.68 | 18.67 | 7.72 | 7.42 | 4 | 4 |
| R8006_M8012__far_ch1 | 9.99 | 10.58 | 1.80 | 1.96 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.92 | 7.63 | 0.74 | 0.86 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.25 | 10.50 | 1.97 | 2.19 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.45 | 9.96 | 1.31 | 2.37 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.18 | 6.06 | 0.53 | 0.64 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.67 | 7.32 | 0.53 | 0.52 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.33 | 6.99 | 1.08 | 1.33 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.72 | 11.97 | 0.93 | 1.11 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.76 | 4.71 | 0.74 | 0.75 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.45 | 7.14 | 0.69 | 0.61 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.50 | 8.32 | 1.11 | 1.27 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.05 | 5.89 | 1.77 | 1.71 | 2 | 2 |
| R8009_M8028__far_ch1 | 8.95 | 8.31 | 4.45 | 4.08 | 2 | 2 |
