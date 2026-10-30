# Diarization scores: A-fa_s750/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa_s750/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T20:57:24+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7759-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.66 | 5.47 | 4.46 | 0.73 | 11.31 | 100.00 | 0.00 |
| 0.25 | 1.75 | 1.04 | 0.62 | 0.09 | 2.56 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.41 (IoU 95.20) | 1.95 (IoU 1.99) |
| silence | 2.16 (IoU 2.21) | 14.48 (IoU 77.90) |

Speech P/R/F1: 97.41 / 97.67 / 97.54; miss 2.33 of ref speech, FA 12.99 of ref silence, SAD error 4.93.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13096 | 12670 | 92.65 | 89.64 | 91.12 | 0.042 | 0.030 | -0.000 | 0.000 |
| 0.25 | offset | 13098 | 12670 | 93.05 | 90.01 | 91.50 | 0.047 | 0.040 | 0.011 | 0.020 |
| 0.25 | all | 26194 | 25340 | 92.85 | 89.82 | 91.31 | 0.045 | 0.030 | 0.006 | 0.010 |
| 0.50 | onset | 13096 | 12670 | 93.66 | 90.62 | 92.11 | 0.045 | 0.030 | 0.000 | 0.000 |
| 0.50 | offset | 13098 | 12670 | 93.85 | 90.78 | 92.29 | 0.050 | 0.040 | 0.011 | 0.020 |
| 0.50 | all | 26194 | 25340 | 93.76 | 90.70 | 92.20 | 0.048 | 0.030 | 0.006 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.06 | 11.28 | 1.13 | 1.37 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.36 | 13.19 | 2.11 | 3.62 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.06 | 10.28 | 1.61 | 2.07 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.01 | 21.27 | 5.23 | 7.26 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.79 | 18.95 | 2.80 | 3.15 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.44 | 7.41 | 1.58 | 1.68 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.63 | 18.66 | 7.59 | 7.32 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.44 | 10.93 | 2.16 | 2.29 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.24 | 8.00 | 0.93 | 1.11 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.83 | 11.21 | 1.98 | 2.29 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.83 | 11.35 | 1.40 | 2.35 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.54 | 6.47 | 0.69 | 0.86 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.89 | 7.54 | 0.73 | 0.72 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.63 | 7.25 | 1.19 | 1.39 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.34 | 12.71 | 1.11 | 1.39 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.41 | 4.32 | 0.65 | 0.64 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.38 | 7.05 | 0.85 | 0.75 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.64 | 8.45 | 1.09 | 1.22 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.59 | 6.43 | 2.12 | 2.06 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.28 | 6.11 | 1.23 | 1.22 | 2 | 2 |
