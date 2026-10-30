# Diarization scores: A-fa_s1250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa_s1250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T21:19:35+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7917-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.72 | 5.42 | 4.58 | 0.72 | 11.35 | 100.00 | 0.00 |
| 0.25 | 1.81 | 1.07 | 0.65 | 0.09 | 2.63 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.36 (IoU 95.14) | 1.97 (IoU 2.01) |
| silence | 2.19 (IoU 2.23) | 14.48 (IoU 77.70) |

Speech P/R/F1: 97.38 / 97.63 / 97.51; miss 2.37 of ref speech, FA 13.12 of ref silence, SAD error 4.99.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13096 | 12683 | 92.43 | 89.52 | 90.95 | 0.042 | 0.030 | 0.001 | 0.010 |
| 0.25 | offset | 13098 | 12682 | 92.71 | 89.76 | 91.21 | 0.048 | 0.040 | 0.012 | 0.020 |
| 0.25 | all | 26194 | 25365 | 92.57 | 89.64 | 91.08 | 0.045 | 0.030 | 0.007 | 0.010 |
| 0.50 | onset | 13096 | 12683 | 93.39 | 90.45 | 91.90 | 0.046 | 0.030 | 0.001 | 0.010 |
| 0.50 | offset | 13098 | 12682 | 93.51 | 90.54 | 92.00 | 0.050 | 0.040 | 0.012 | 0.020 |
| 0.50 | all | 26194 | 25365 | 93.45 | 90.49 | 91.95 | 0.048 | 0.030 | 0.007 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.73 | 10.96 | 1.13 | 1.34 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.86 | 13.40 | 2.96 | 4.10 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.26 | 10.49 | 1.53 | 2.04 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.13 | 21.39 | 5.12 | 7.30 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.75 | 18.77 | 2.74 | 3.04 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.51 | 7.47 | 1.56 | 1.66 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.98 | 18.92 | 8.46 | 7.99 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.52 | 10.97 | 2.28 | 2.42 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.25 | 8.03 | 0.89 | 1.07 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.77 | 11.05 | 1.98 | 2.24 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.00 | 11.47 | 1.35 | 2.33 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.62 | 6.52 | 0.65 | 0.83 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.56 | 7.25 | 0.84 | 0.82 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.61 | 7.21 | 1.21 | 1.39 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.46 | 12.92 | 1.06 | 1.34 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.16 | 5.08 | 1.11 | 1.09 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.32 | 7.03 | 0.79 | 0.73 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.33 | 8.15 | 0.98 | 1.08 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.39 | 6.23 | 1.96 | 1.89 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.42 | 6.29 | 1.19 | 1.18 | 2 | 2 |
