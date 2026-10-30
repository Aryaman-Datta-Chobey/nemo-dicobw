# Diarization scores: A-fa-r75b-seed43_s250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75b-seed43_s250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T06:40:55+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75b-seed43_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7797-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.42 | 5.45 | 4.28 | 0.69 | 11.00 | 100.00 | 0.00 |
| 0.25 | 1.63 | 0.91 | 0.66 | 0.06 | 2.38 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.50 (IoU 95.45) | 1.86 (IoU 1.90) |
| silence | 2.02 (IoU 2.06) | 14.62 (IoU 79.02) |

Speech P/R/F1: 97.58 / 97.77 / 97.67; miss 2.23 of ref speech, FA 12.14 of ref silence, SAD error 4.66.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 12849 | 92.71 | 90.95 | 91.82 | 0.042 | 0.030 | -0.000 | 0.000 |
| 0.25 | offset | 13096 | 12850 | 92.82 | 91.08 | 91.94 | 0.044 | 0.030 | 0.004 | 0.010 |
| 0.25 | all | 26194 | 25699 | 92.77 | 91.01 | 91.88 | 0.043 | 0.030 | 0.002 | 0.010 |
| 0.50 | onset | 13098 | 12849 | 93.52 | 91.74 | 92.62 | 0.044 | 0.030 | 0.000 | 0.000 |
| 0.50 | offset | 13096 | 12850 | 93.67 | 91.91 | 92.78 | 0.047 | 0.030 | 0.004 | 0.010 |
| 0.50 | all | 26194 | 25699 | 93.59 | 91.82 | 92.70 | 0.046 | 0.030 | 0.002 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.24 | 10.49 | 1.17 | 1.40 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.45 | 12.03 | 1.73 | 2.82 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.92 | 10.12 | 1.27 | 1.63 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.80 | 22.13 | 4.98 | 7.18 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.85 | 19.85 | 2.75 | 2.99 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.31 | 7.37 | 1.54 | 1.66 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.64 | 18.62 | 7.66 | 7.37 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.09 | 10.69 | 1.81 | 2.01 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.91 | 7.56 | 0.70 | 0.80 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.23 | 10.53 | 1.90 | 2.19 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.35 | 9.88 | 1.21 | 2.25 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.09 | 5.96 | 0.42 | 0.53 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.77 | 7.41 | 0.55 | 0.54 | 2 | 2 |
| R8009_M8022__far_ch1 | 5.88 | 6.48 | 1.02 | 1.26 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.25 | 11.49 | 0.88 | 1.07 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.37 | 4.30 | 0.59 | 0.59 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.32 | 6.96 | 0.70 | 0.60 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.10 | 7.90 | 0.95 | 1.08 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.56 | 5.37 | 1.49 | 1.42 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.88 | 6.58 | 2.26 | 2.17 | 2 | 2 |
