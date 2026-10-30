# Diarization scores: D-seg_s250/alimeeting_Test_Ali_far_ch1__nouem

- name: `D-seg_s250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-seg_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T18:36:20+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `D-seg_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7851-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.19 | 3.86 | 6.59 | 0.75 | 11.57 | 100.00 | 0.00 |
| 0.25 | 1.59 | 0.61 | 0.92 | 0.06 | 2.60 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.36 (IoU 94.99) | 0.95 (IoU 0.98) |
| silence | 3.40 (IoU 3.43) | 13.29 (IoU 75.35) |

Speech P/R/F1: 96.04 / 98.86 / 97.43; miss 1.14 of ref speech, FA 20.37 of ref silence, SAD error 5.22.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13101 | 12350 | 93.71 | 88.34 | 90.94 | 0.052 | 0.040 | -0.037 | -0.030 |
| 0.25 | offset | 13098 | 12352 | 93.94 | 88.59 | 91.18 | 0.052 | 0.040 | 0.027 | 0.030 |
| 0.25 | all | 26199 | 24702 | 93.82 | 88.46 | 91.06 | 0.052 | 0.040 | -0.005 | 0.000 |
| 0.50 | onset | 13101 | 12350 | 94.71 | 89.28 | 91.92 | 0.056 | 0.040 | -0.038 | -0.030 |
| 0.50 | offset | 13098 | 12352 | 94.74 | 89.34 | 91.96 | 0.055 | 0.040 | 0.028 | 0.030 |
| 0.50 | all | 26199 | 24702 | 94.73 | 89.31 | 91.94 | 0.055 | 0.040 | -0.005 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.86 | 9.95 | 1.15 | 1.36 | 4 | 4 |
| R8002_M8003__far_ch1 | 12.21 | 13.04 | 4.13 | 6.56 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.77 | 10.84 | 1.23 | 1.64 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.88 | 22.00 | 4.68 | 7.02 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.87 | 19.63 | 2.62 | 2.84 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.18 | 8.00 | 1.55 | 1.68 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.55 | 19.28 | 8.00 | 7.81 | 4 | 4 |
| R8006_M8012__far_ch1 | 11.41 | 11.59 | 2.32 | 2.41 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.13 | 7.65 | 0.59 | 0.72 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.66 | 12.00 | 2.01 | 2.44 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.80 | 11.59 | 1.53 | 2.80 | 3 | 3 |
| R8008_M8017__far_ch1 | 6.71 | 7.25 | 0.34 | 0.41 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.33 | 7.78 | 0.47 | 0.46 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.18 | 6.72 | 0.77 | 1.05 | 2 | 2 |
| R8009_M8023__far_ch1 | 12.03 | 13.44 | 0.49 | 0.67 | 2 | 2 |
| R8009_M8024__far_ch1 | 6.09 | 5.80 | 0.43 | 0.42 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.69 | 6.25 | 0.40 | 0.35 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.40 | 8.06 | 0.62 | 0.71 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.75 | 6.29 | 1.07 | 1.01 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.60 | 6.24 | 1.08 | 1.05 | 2 | 2 |
