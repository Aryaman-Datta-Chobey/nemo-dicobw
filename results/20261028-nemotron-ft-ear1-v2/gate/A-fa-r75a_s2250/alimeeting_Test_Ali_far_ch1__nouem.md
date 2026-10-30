# Diarization scores: A-fa-r75a_s2250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75a_s2250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s2250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T00:48:42+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75a_s2250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7898-epoch=8.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.54 | 5.49 | 4.33 | 0.72 | 11.16 | 100.00 | 0.00 |
| 0.25 | 1.63 | 0.98 | 0.58 | 0.07 | 2.43 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.43 (IoU 95.34) | 1.93 (IoU 1.97) |
| silence | 2.05 (IoU 2.09) | 14.59 (IoU 78.56) |

Speech P/R/F1: 97.54 / 97.68 / 97.61; miss 2.32 of ref speech, FA 12.33 of ref silence, SAD error 4.78.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13096 | 12764 | 92.74 | 90.39 | 91.55 | 0.042 | 0.030 | 0.001 | 0.000 |
| 0.25 | offset | 13098 | 12764 | 92.99 | 90.62 | 91.79 | 0.046 | 0.040 | 0.006 | 0.010 |
| 0.25 | all | 26194 | 25528 | 92.86 | 90.50 | 91.67 | 0.044 | 0.030 | 0.003 | 0.010 |
| 0.50 | onset | 13096 | 12764 | 93.62 | 91.25 | 92.42 | 0.045 | 0.030 | 0.001 | 0.000 |
| 0.50 | offset | 13098 | 12764 | 93.80 | 91.41 | 92.59 | 0.048 | 0.040 | 0.006 | 0.010 |
| 0.50 | all | 26194 | 25528 | 93.71 | 91.33 | 92.51 | 0.047 | 0.030 | 0.004 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.93 | 10.21 | 1.16 | 1.41 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.62 | 12.22 | 1.78 | 2.80 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.13 | 10.32 | 1.28 | 1.62 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.82 | 22.25 | 5.08 | 7.35 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.52 | 19.50 | 2.78 | 2.99 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.40 | 7.41 | 1.63 | 1.74 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.78 | 18.81 | 7.73 | 7.50 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.34 | 10.92 | 2.00 | 2.18 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.95 | 7.70 | 0.81 | 0.95 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.39 | 10.76 | 1.87 | 2.17 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.72 | 10.33 | 1.29 | 2.31 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.42 | 6.39 | 0.65 | 0.86 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.26 | 7.88 | 0.63 | 0.62 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.91 | 7.62 | 1.15 | 1.42 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.42 | 12.87 | 0.93 | 1.20 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.27 | 4.20 | 0.62 | 0.61 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.72 | 6.61 | 0.64 | 0.60 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.94 | 7.74 | 0.84 | 0.94 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.00 | 5.83 | 1.70 | 1.64 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.29 | 6.15 | 1.29 | 1.27 | 2 | 2 |
