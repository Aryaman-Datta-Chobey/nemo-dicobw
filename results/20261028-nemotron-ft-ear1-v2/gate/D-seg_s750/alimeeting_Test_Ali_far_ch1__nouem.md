# Diarization scores: D-seg_s750/alimeeting_Test_Ali_far_ch1__nouem

- name: `D-seg_s750/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-seg_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T18:55:09+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `D-seg_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7971-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.44 | 4.91 | 6.80 | 0.73 | 12.65 | 100.00 | 0.00 |
| 0.25 | 1.42 | 0.73 | 0.62 | 0.07 | 2.36 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.64 (IoU 93.79) | 0.67 (IoU 0.70) |
| silence | 4.80 (IoU 4.83) | 11.89 (IoU 68.49) |

Speech P/R/F1: 94.51 / 99.19 / 96.80; miss 0.81 of ref speech, FA 28.76 of ref silence, SAD error 6.57.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12173 | 92.86 | 86.27 | 89.44 | 0.067 | 0.060 | -0.056 | -0.050 |
| 0.25 | offset | 13101 | 12175 | 92.92 | 86.35 | 89.52 | 0.072 | 0.070 | 0.054 | 0.060 |
| 0.25 | all | 26204 | 24348 | 92.89 | 86.31 | 89.48 | 0.069 | 0.060 | -0.001 | 0.000 |
| 0.50 | onset | 13103 | 12173 | 93.99 | 87.32 | 90.53 | 0.070 | 0.060 | -0.057 | -0.050 |
| 0.50 | offset | 13101 | 12175 | 93.98 | 87.34 | 90.54 | 0.075 | 0.070 | 0.055 | 0.060 |
| 0.50 | all | 26204 | 24348 | 93.98 | 87.33 | 90.53 | 0.072 | 0.060 | -0.001 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.30 | 10.44 | 0.98 | 1.19 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.73 | 12.77 | 1.67 | 2.65 | 4 | 4 |
| R8004_M8005__far_ch1 | 10.23 | 11.40 | 1.23 | 1.65 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.25 | 24.09 | 5.50 | 7.71 | 4 | 4 |
| R8005_M8007__far_ch1 | 20.62 | 20.64 | 2.92 | 3.12 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.97 | 8.80 | 1.61 | 1.88 | 4 | 4 |
| R8005_M8009__far_ch1 | 20.87 | 20.76 | 8.57 | 8.42 | 4 | 4 |
| R8006_M8012__far_ch1 | 11.26 | 11.49 | 2.03 | 2.30 | 4 | 4 |
| R8008_M8014__far_ch1 | 8.48 | 8.64 | 0.50 | 0.62 | 3 | 3 |
| R8008_M8015__far_ch1 | 12.08 | 13.77 | 1.87 | 2.44 | 3 | 3 |
| R8008_M8016__far_ch1 | 11.06 | 12.27 | 1.21 | 2.16 | 3 | 3 |
| R8008_M8017__far_ch1 | 8.62 | 8.78 | 0.32 | 0.53 | 3 | 3 |
| R8009_M8021__far_ch1 | 11.11 | 10.11 | 0.45 | 0.44 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.51 | 7.91 | 0.59 | 0.87 | 2 | 2 |
| R8009_M8023__far_ch1 | 14.84 | 14.82 | 0.33 | 0.49 | 2 | 2 |
| R8009_M8024__far_ch1 | 8.72 | 8.13 | 0.46 | 0.47 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.66 | 7.49 | 0.29 | 0.24 | 2 | 2 |
| R8009_M8026__far_ch1 | 9.63 | 9.06 | 0.38 | 0.44 | 2 | 2 |
| R8009_M8027__far_ch1 | 9.27 | 8.29 | 0.81 | 0.76 | 2 | 2 |
| R8009_M8028__far_ch1 | 8.31 | 7.69 | 0.64 | 0.63 | 2 | 2 |
