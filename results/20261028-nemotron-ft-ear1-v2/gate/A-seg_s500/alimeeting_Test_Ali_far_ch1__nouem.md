# Diarization scores: A-seg_s500/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-seg_s500/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T15:25:52+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-seg_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8231-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.29 | 4.75 | 6.81 | 0.74 | 12.73 | 100.00 | 0.00 |
| 0.25 | 1.90 | 0.80 | 1.04 | 0.07 | 2.61 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.70 (IoU 94.05) | 1.63 (IoU 1.69) |
| silence | 3.54 (IoU 3.60) | 13.13 (IoU 71.74) |

Speech P/R/F1: 95.84 / 98.05 / 96.93; miss 1.95 of ref speech, FA 21.25 of ref silence, SAD error 6.21.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13100 | 11651 | 93.45 | 83.11 | 87.98 | 0.055 | 0.040 | -0.020 | -0.010 |
| 0.25 | offset | 13097 | 11654 | 93.31 | 83.03 | 87.87 | 0.058 | 0.050 | 0.017 | 0.020 |
| 0.25 | all | 26197 | 23305 | 93.38 | 83.07 | 87.92 | 0.056 | 0.040 | -0.002 | 0.000 |
| 0.50 | onset | 13100 | 11651 | 94.73 | 84.25 | 89.18 | 0.059 | 0.040 | -0.021 | -0.020 |
| 0.50 | offset | 13097 | 11654 | 94.79 | 84.35 | 89.27 | 0.062 | 0.050 | 0.019 | 0.020 |
| 0.50 | all | 26197 | 23305 | 94.76 | 84.30 | 89.22 | 0.061 | 0.040 | -0.001 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.48 | 10.73 | 1.17 | 1.42 | 4 | 4 |
| R8002_M8003__far_ch1 | 14.41 | 15.41 | 1.90 | 3.19 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.15 | 10.30 | 1.31 | 1.65 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.53 | 21.56 | 4.86 | 7.13 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.68 | 19.65 | 2.69 | 3.00 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.70 | 7.63 | 1.56 | 1.67 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.61 | 18.60 | 7.45 | 7.26 | 4 | 4 |
| R8006_M8012__far_ch1 | 11.12 | 11.43 | 2.45 | 2.56 | 4 | 4 |
| R8008_M8014__far_ch1 | 10.49 | 10.67 | 0.50 | 0.60 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.59 | 20.44 | 2.00 | 2.36 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.59 | 11.90 | 1.38 | 2.47 | 3 | 3 |
| R8008_M8017__far_ch1 | 16.40 | 15.05 | 2.23 | 2.16 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.80 | 7.45 | 0.66 | 0.65 | 2 | 2 |
| R8009_M8022__far_ch1 | 5.75 | 6.37 | 1.15 | 1.41 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.84 | 12.13 | 0.99 | 1.19 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.48 | 4.39 | 0.65 | 0.65 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.06 | 7.68 | 0.82 | 0.71 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.36 | 8.14 | 0.94 | 1.08 | 2 | 2 |
| R8009_M8027__far_ch1 | 9.42 | 8.68 | 1.36 | 1.33 | 2 | 2 |
| R8009_M8028__far_ch1 | 10.39 | 9.25 | 4.60 | 4.17 | 2 | 2 |
