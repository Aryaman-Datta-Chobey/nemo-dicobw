# Diarization scores: C-seg_s750/alimeeting_Test_Ali_far_ch1__nouem

- name: `C-seg_s750/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-seg_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T18:01:48+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `C-seg_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8148-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.13 | 4.68 | 6.72 | 0.73 | 12.52 | 100.00 | 0.00 |
| 0.25 | 2.00 | 0.80 | 1.13 | 0.07 | 2.67 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.72 (IoU 94.10) | 1.62 (IoU 1.68) |
| silence | 3.50 (IoU 3.56) | 13.16 (IoU 71.98) |

Speech P/R/F1: 95.89 / 98.06 / 96.96; miss 1.94 of ref speech, FA 21.02 of ref silence, SAD error 6.15.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13099 | 11888 | 92.78 | 84.20 | 88.29 | 0.053 | 0.040 | -0.014 | -0.010 |
| 0.25 | offset | 13100 | 11889 | 92.52 | 83.97 | 88.04 | 0.057 | 0.040 | 0.021 | 0.020 |
| 0.25 | all | 26199 | 23777 | 92.65 | 84.09 | 88.16 | 0.055 | 0.040 | 0.003 | 0.010 |
| 0.50 | onset | 13099 | 11888 | 94.09 | 85.40 | 89.53 | 0.058 | 0.040 | -0.015 | -0.010 |
| 0.50 | offset | 13100 | 11889 | 94.20 | 85.50 | 89.64 | 0.062 | 0.050 | 0.024 | 0.020 |
| 0.50 | all | 26199 | 23777 | 94.15 | 85.45 | 89.59 | 0.060 | 0.040 | 0.004 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.15 | 11.40 | 1.18 | 1.42 | 4 | 4 |
| R8002_M8003__far_ch1 | 13.52 | 14.27 | 2.39 | 3.79 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.19 | 10.31 | 1.40 | 1.72 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.68 | 21.58 | 5.13 | 7.33 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.37 | 19.34 | 2.84 | 3.18 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.58 | 7.55 | 1.57 | 1.69 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.50 | 18.43 | 7.31 | 7.05 | 4 | 4 |
| R8006_M8012__far_ch1 | 11.08 | 11.44 | 2.58 | 2.69 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.99 | 8.59 | 0.67 | 0.76 | 3 | 3 |
| R8008_M8015__far_ch1 | 17.61 | 17.02 | 1.81 | 2.10 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.87 | 12.30 | 1.41 | 2.47 | 3 | 3 |
| R8008_M8017__far_ch1 | 17.23 | 15.68 | 1.06 | 1.13 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.11 | 7.71 | 0.59 | 0.58 | 2 | 2 |
| R8009_M8022__far_ch1 | 5.69 | 6.28 | 1.10 | 1.41 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.72 | 11.76 | 1.16 | 1.22 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.61 | 4.51 | 0.66 | 0.65 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.04 | 7.60 | 0.99 | 0.89 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.84 | 7.60 | 0.90 | 1.05 | 2 | 2 |
| R8009_M8027__far_ch1 | 13.42 | 11.70 | 1.79 | 1.68 | 2 | 2 |
| R8009_M8028__far_ch1 | 10.72 | 9.52 | 5.94 | 5.25 | 2 | 2 |
