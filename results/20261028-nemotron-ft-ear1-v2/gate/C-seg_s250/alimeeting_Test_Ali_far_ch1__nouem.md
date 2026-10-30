# Diarization scores: C-seg_s250/alimeeting_Test_Ali_far_ch1__nouem

- name: `C-seg_s250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-seg_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T17:39:46+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `C-seg_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7948-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.26 | 4.33 | 7.19 | 0.73 | 12.65 | 100.00 | 0.00 |
| 0.25 | 1.58 | 0.61 | 0.90 | 0.06 | 2.46 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.11 (IoU 94.07) | 1.23 (IoU 1.28) |
| silence | 3.94 (IoU 3.99) | 12.72 (IoU 71.09) |

Speech P/R/F1: 95.42 / 98.52 / 96.95; miss 1.48 of ref speech, FA 23.66 of ref silence, SAD error 6.21.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13100 | 11597 | 93.75 | 82.99 | 88.04 | 0.057 | 0.040 | -0.024 | -0.020 |
| 0.25 | offset | 13100 | 11598 | 92.96 | 82.30 | 87.30 | 0.057 | 0.050 | 0.024 | 0.020 |
| 0.25 | all | 26200 | 23195 | 93.35 | 82.65 | 87.67 | 0.057 | 0.040 | -0.000 | 0.000 |
| 0.50 | onset | 13100 | 11597 | 94.83 | 83.95 | 89.06 | 0.060 | 0.040 | -0.026 | -0.020 |
| 0.50 | offset | 13100 | 11598 | 94.82 | 83.95 | 89.05 | 0.063 | 0.050 | 0.028 | 0.020 |
| 0.50 | all | 26200 | 23195 | 94.83 | 83.95 | 89.06 | 0.062 | 0.050 | 0.001 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.22 | 10.40 | 1.11 | 1.31 | 4 | 4 |
| R8002_M8003__far_ch1 | 12.51 | 13.43 | 2.29 | 3.70 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.47 | 10.54 | 1.37 | 1.72 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.55 | 22.44 | 5.19 | 7.43 | 4 | 4 |
| R8005_M8007__far_ch1 | 20.16 | 19.91 | 2.60 | 2.84 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.46 | 8.32 | 1.58 | 1.72 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.85 | 18.63 | 7.68 | 7.41 | 4 | 4 |
| R8006_M8012__far_ch1 | 14.12 | 14.12 | 3.08 | 3.23 | 4 | 4 |
| R8008_M8014__far_ch1 | 11.77 | 11.92 | 0.59 | 0.70 | 3 | 3 |
| R8008_M8015__far_ch1 | 23.94 | 21.23 | 2.30 | 2.73 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.04 | 11.47 | 1.10 | 2.07 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.20 | 11.89 | 0.43 | 0.54 | 3 | 3 |
| R8009_M8021__far_ch1 | 9.13 | 8.61 | 0.55 | 0.54 | 2 | 2 |
| R8009_M8022__far_ch1 | 5.18 | 5.79 | 0.82 | 1.10 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.00 | 11.05 | 0.63 | 0.79 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.46 | 4.32 | 0.50 | 0.49 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.96 | 6.61 | 0.53 | 0.46 | 2 | 2 |
| R8009_M8026__far_ch1 | 6.73 | 6.46 | 0.59 | 0.66 | 2 | 2 |
| R8009_M8027__far_ch1 | 11.97 | 10.31 | 1.32 | 1.20 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.20 | 5.95 | 0.67 | 0.67 | 2 | 2 |
