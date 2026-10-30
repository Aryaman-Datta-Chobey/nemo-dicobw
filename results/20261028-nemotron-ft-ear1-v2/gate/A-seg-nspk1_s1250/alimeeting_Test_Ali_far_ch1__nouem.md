# Diarization scores: A-seg-nspk1_s1250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-seg-nspk1_s1250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T02:31:21+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-seg-nspk1_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8317-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.83 | 5.23 | 5.86 | 0.74 | 12.37 | 100.00 | 0.00 |
| 0.25 | 1.92 | 1.01 | 0.84 | 0.07 | 2.71 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.44 (IoU 94.39) | 1.86 (IoU 1.92) |
| silence | 2.98 (IoU 3.03) | 13.72 (IoU 73.92) |

Speech P/R/F1: 96.47 / 97.76 / 97.11; miss 2.24 of ref speech, FA 17.83 of ref silence, SAD error 5.81.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 12168 | 93.14 | 86.52 | 89.71 | 0.048 | 0.040 | -0.008 | -0.010 |
| 0.25 | offset | 13097 | 12168 | 92.80 | 86.22 | 89.39 | 0.058 | 0.050 | 0.023 | 0.020 |
| 0.25 | all | 26195 | 24336 | 92.97 | 86.37 | 89.55 | 0.053 | 0.040 | 0.007 | 0.010 |
| 0.50 | onset | 13098 | 12168 | 94.21 | 87.52 | 90.75 | 0.052 | 0.040 | -0.007 | -0.010 |
| 0.50 | offset | 13097 | 12168 | 94.37 | 87.68 | 90.90 | 0.063 | 0.050 | 0.025 | 0.020 |
| 0.50 | all | 26195 | 24336 | 94.29 | 87.60 | 90.82 | 0.057 | 0.040 | 0.009 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.85 | 11.03 | 1.64 | 1.75 | 4 | 4 |
| R8002_M8003__far_ch1 | 16.15 | 16.53 | 1.83 | 3.09 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.47 | 10.71 | 1.42 | 1.92 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.89 | 22.08 | 5.12 | 7.40 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.57 | 19.56 | 2.79 | 3.11 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.57 | 7.55 | 1.58 | 1.69 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.31 | 19.30 | 8.84 | 8.36 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.63 | 11.14 | 2.30 | 2.48 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.75 | 8.47 | 0.71 | 0.87 | 3 | 3 |
| R8008_M8015__far_ch1 | 13.29 | 14.13 | 1.68 | 2.06 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.94 | 12.29 | 1.65 | 2.70 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.14 | 11.92 | 0.97 | 1.08 | 3 | 3 |
| R8009_M8021__far_ch1 | 9.18 | 8.74 | 0.88 | 0.87 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.71 | 7.38 | 1.30 | 1.56 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.04 | 12.18 | 1.00 | 1.16 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.57 | 5.51 | 1.64 | 1.65 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.41 | 7.98 | 0.88 | 0.80 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.80 | 8.61 | 0.96 | 1.10 | 2 | 2 |
| R8009_M8027__far_ch1 | 7.01 | 6.79 | 1.90 | 1.87 | 2 | 2 |
| R8009_M8028__far_ch1 | 8.36 | 7.89 | 2.59 | 2.45 | 2 | 2 |
