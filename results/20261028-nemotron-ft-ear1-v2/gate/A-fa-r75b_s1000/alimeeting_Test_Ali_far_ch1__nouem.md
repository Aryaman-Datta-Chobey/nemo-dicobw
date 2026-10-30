# Diarization scores: A-fa-r75b_s1000/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75b_s1000/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T02:18:03+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75b_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7866-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.66 | 5.58 | 4.36 | 0.72 | 11.25 | 100.00 | 0.00 |
| 0.25 | 1.83 | 1.02 | 0.73 | 0.08 | 2.65 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.36 (IoU 95.31) | 1.98 (IoU 2.02) |
| silence | 2.03 (IoU 2.07) | 14.63 (IoU 78.52) |

Speech P/R/F1: 97.57 / 97.63 / 97.60; miss 2.37 of ref speech, FA 12.16 of ref silence, SAD error 4.80.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13097 | 12856 | 92.35 | 90.65 | 91.50 | 0.042 | 0.030 | 0.000 | 0.000 |
| 0.25 | offset | 13096 | 12857 | 92.59 | 90.90 | 91.74 | 0.045 | 0.030 | 0.004 | 0.010 |
| 0.25 | all | 26193 | 25713 | 92.47 | 90.78 | 91.62 | 0.044 | 0.030 | 0.002 | 0.010 |
| 0.50 | onset | 13097 | 12856 | 93.24 | 91.52 | 92.37 | 0.045 | 0.030 | 0.001 | 0.000 |
| 0.50 | offset | 13096 | 12857 | 93.39 | 91.68 | 92.53 | 0.048 | 0.030 | 0.004 | 0.010 |
| 0.50 | all | 26193 | 25713 | 93.31 | 91.60 | 92.45 | 0.047 | 0.030 | 0.002 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.87 | 10.12 | 1.16 | 1.36 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.98 | 12.58 | 2.49 | 4.15 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.15 | 10.35 | 1.35 | 1.73 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.74 | 22.08 | 5.02 | 7.10 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.73 | 19.72 | 2.84 | 3.07 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.33 | 7.36 | 1.56 | 1.67 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.14 | 19.28 | 8.10 | 8.19 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.28 | 10.82 | 2.18 | 2.31 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.89 | 7.64 | 0.79 | 0.93 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.44 | 10.73 | 1.95 | 2.21 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.63 | 10.13 | 1.33 | 2.32 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.28 | 6.25 | 0.60 | 0.82 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.46 | 8.07 | 0.69 | 0.68 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.84 | 7.54 | 1.20 | 1.47 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.34 | 12.85 | 1.05 | 1.36 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.65 | 4.55 | 0.99 | 1.00 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.89 | 6.67 | 0.70 | 0.62 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.06 | 7.89 | 0.97 | 1.10 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.91 | 5.74 | 1.70 | 1.63 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.73 | 7.33 | 3.11 | 2.93 | 2 | 2 |
