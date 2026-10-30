# Diarization scores: A-fa-t2r25_s750/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-t2r25_s750/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T12:04:47+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-t2r25_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7886-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.57 | 5.53 | 4.35 | 0.70 | 11.18 | 100.00 | 0.00 |
| 0.25 | 1.74 | 1.04 | 0.64 | 0.07 | 2.50 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.40 (IoU 95.26) | 1.95 (IoU 1.99) |
| silence | 2.10 (IoU 2.14) | 14.55 (IoU 78.22) |

Speech P/R/F1: 97.49 / 97.66 / 97.57; miss 2.34 of ref speech, FA 12.60 of ref silence, SAD error 4.86.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13096 | 12719 | 92.48 | 89.82 | 91.13 | 0.042 | 0.030 | -0.001 | 0.000 |
| 0.25 | offset | 13096 | 12718 | 92.92 | 90.23 | 91.55 | 0.046 | 0.030 | 0.008 | 0.010 |
| 0.25 | all | 26192 | 25437 | 92.70 | 90.03 | 91.34 | 0.044 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13096 | 12719 | 93.50 | 90.81 | 92.13 | 0.045 | 0.030 | -0.000 | 0.000 |
| 0.50 | offset | 13096 | 12718 | 93.71 | 91.00 | 92.34 | 0.048 | 0.040 | 0.008 | 0.010 |
| 0.50 | all | 26192 | 25437 | 93.60 | 90.91 | 92.23 | 0.047 | 0.030 | 0.004 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.63 | 10.89 | 1.15 | 1.35 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.74 | 12.30 | 1.72 | 2.61 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.13 | 10.29 | 1.46 | 1.80 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.11 | 21.46 | 5.12 | 7.40 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.97 | 19.07 | 2.91 | 3.30 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.50 | 7.46 | 1.65 | 1.74 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.73 | 18.77 | 7.69 | 7.46 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.35 | 10.87 | 2.06 | 2.22 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.99 | 7.77 | 0.79 | 0.95 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.44 | 10.66 | 1.86 | 2.11 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.12 | 10.67 | 1.30 | 2.26 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.49 | 6.43 | 0.70 | 0.90 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.04 | 7.69 | 0.77 | 0.76 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.54 | 7.13 | 1.18 | 1.36 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.85 | 12.18 | 1.06 | 1.36 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.58 | 4.46 | 0.70 | 0.69 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.09 | 6.88 | 0.78 | 0.71 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.51 | 8.31 | 1.03 | 1.15 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.76 | 6.61 | 2.10 | 2.05 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.93 | 6.70 | 1.89 | 1.84 | 2 | 2 |
