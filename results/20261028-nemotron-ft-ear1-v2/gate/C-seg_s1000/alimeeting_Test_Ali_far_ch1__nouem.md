# Diarization scores: C-seg_s1000/alimeeting_Test_Ali_far_ch1__nouem

- name: `C-seg_s1000/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-seg_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T18:12:55+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `C-seg_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8082-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.92 | 4.77 | 6.44 | 0.71 | 12.39 | 100.00 | 0.00 |
| 0.25 | 1.96 | 0.86 | 1.03 | 0.07 | 2.70 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.64 (IoU 94.27) | 1.70 (IoU 1.76) |
| silence | 3.26 (IoU 3.32) | 13.40 (IoU 72.96) |

Speech P/R/F1: 96.16 / 97.96 / 97.05; miss 2.04 of ref speech, FA 19.58 of ref silence, SAD error 5.96.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13100 | 11940 | 92.86 | 84.64 | 88.56 | 0.051 | 0.040 | -0.012 | -0.010 |
| 0.25 | offset | 13098 | 11942 | 92.61 | 84.44 | 88.34 | 0.054 | 0.040 | 0.018 | 0.020 |
| 0.25 | all | 26198 | 23882 | 92.74 | 84.54 | 88.45 | 0.053 | 0.040 | 0.003 | 0.010 |
| 0.50 | onset | 13100 | 11940 | 94.08 | 85.75 | 89.72 | 0.055 | 0.040 | -0.012 | -0.010 |
| 0.50 | offset | 13098 | 11942 | 94.23 | 85.91 | 89.88 | 0.059 | 0.040 | 0.020 | 0.020 |
| 0.50 | all | 26198 | 23882 | 94.15 | 85.83 | 89.80 | 0.057 | 0.040 | 0.004 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.20 | 11.42 | 1.24 | 1.47 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.84 | 12.98 | 2.37 | 3.82 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.17 | 10.29 | 1.36 | 1.68 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.70 | 21.59 | 5.08 | 7.31 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.25 | 19.16 | 2.79 | 3.11 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.48 | 7.45 | 1.59 | 1.70 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.58 | 18.46 | 7.51 | 7.27 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.92 | 11.25 | 2.65 | 2.75 | 4 | 4 |
| R8008_M8014__far_ch1 | 8.21 | 8.84 | 0.77 | 0.91 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.90 | 20.30 | 1.95 | 2.59 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.78 | 12.18 | 1.48 | 2.53 | 3 | 3 |
| R8008_M8017__far_ch1 | 16.84 | 15.41 | 1.08 | 1.15 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.76 | 7.40 | 0.64 | 0.63 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.14 | 6.73 | 1.17 | 1.48 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.74 | 11.60 | 1.34 | 1.42 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.65 | 4.56 | 0.74 | 0.74 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.46 | 7.16 | 0.86 | 0.79 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.96 | 7.72 | 1.01 | 1.18 | 2 | 2 |
| R8009_M8027__far_ch1 | 8.26 | 7.65 | 1.53 | 1.49 | 2 | 2 |
| R8009_M8028__far_ch1 | 9.18 | 8.44 | 4.61 | 4.20 | 2 | 2 |
