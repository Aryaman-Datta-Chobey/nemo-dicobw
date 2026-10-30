# Diarization scores: A-fa-r75a_s1250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75a_s1250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T00:04:17+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75a_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7908-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.60 | 5.66 | 4.22 | 0.71 | 11.22 | 100.00 | 0.00 |
| 0.25 | 1.73 | 1.07 | 0.59 | 0.06 | 2.54 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.30 (IoU 95.27) | 2.05 (IoU 2.09) |
| silence | 1.98 (IoU 2.03) | 14.66 (IoU 78.41) |

Speech P/R/F1: 97.62 / 97.54 / 97.58; miss 2.46 of ref speech, FA 11.92 of ref silence, SAD error 4.84.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13096 | 12758 | 92.62 | 90.23 | 91.41 | 0.042 | 0.030 | 0.005 | 0.010 |
| 0.25 | offset | 13096 | 12759 | 92.91 | 90.52 | 91.70 | 0.045 | 0.030 | 0.006 | 0.010 |
| 0.25 | all | 26192 | 25517 | 92.76 | 90.37 | 91.55 | 0.044 | 0.030 | 0.005 | 0.010 |
| 0.50 | onset | 13096 | 12758 | 93.55 | 91.13 | 92.33 | 0.045 | 0.030 | 0.005 | 0.010 |
| 0.50 | offset | 13096 | 12759 | 93.71 | 91.30 | 92.49 | 0.048 | 0.040 | 0.006 | 0.010 |
| 0.50 | all | 26192 | 25517 | 93.63 | 91.22 | 92.41 | 0.047 | 0.030 | 0.006 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.15 | 10.45 | 1.15 | 1.39 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.73 | 12.39 | 1.89 | 3.09 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.01 | 10.20 | 1.35 | 1.74 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.64 | 22.07 | 5.24 | 7.62 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.46 | 19.46 | 2.77 | 2.99 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.35 | 7.39 | 1.62 | 1.73 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.81 | 18.89 | 7.97 | 7.74 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.34 | 10.91 | 2.07 | 2.24 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.95 | 7.70 | 0.79 | 0.94 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.53 | 10.83 | 1.89 | 2.15 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.71 | 10.31 | 1.36 | 2.33 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.39 | 6.35 | 0.65 | 0.85 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.41 | 8.02 | 0.68 | 0.67 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.21 | 7.96 | 1.29 | 1.61 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.07 | 12.47 | 1.19 | 1.44 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.46 | 4.40 | 0.80 | 0.81 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.18 | 7.09 | 0.90 | 0.91 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.24 | 8.06 | 1.01 | 1.14 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.28 | 6.15 | 1.91 | 1.84 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.42 | 6.30 | 1.28 | 1.26 | 2 | 2 |
