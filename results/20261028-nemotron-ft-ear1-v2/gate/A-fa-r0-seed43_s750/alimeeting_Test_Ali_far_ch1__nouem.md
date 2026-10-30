# Diarization scores: A-fa-r0-seed43_s750/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r0-seed43_s750/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T19:23:02+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r0-seed43_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7834-epoch=5.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.80 | 6.71 | 4.41 | 0.69 | 12.42 | 100.00 | 0.00 |
| 0.25 | 2.03 | 1.39 | 0.56 | 0.09 | 3.23 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.11 (IoU 94.52) | 2.24 (IoU 2.29) |
| silence | 2.46 (IoU 2.52) | 14.19 (IoU 75.12) |

Speech P/R/F1: 97.05 / 97.32 / 97.18; miss 2.68 of ref speech, FA 14.79 of ref silence, SAD error 5.64.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13093 | 13045 | 90.33 | 89.99 | 90.16 | 0.046 | 0.040 | 0.019 | 0.020 |
| 0.25 | offset | 13100 | 13038 | 90.60 | 90.18 | 90.39 | 0.056 | 0.050 | 0.034 | 0.040 |
| 0.25 | all | 26193 | 26083 | 90.47 | 90.09 | 90.27 | 0.051 | 0.040 | 0.027 | 0.030 |
| 0.50 | onset | 13093 | 13045 | 91.31 | 90.97 | 91.14 | 0.050 | 0.040 | 0.020 | 0.020 |
| 0.50 | offset | 13100 | 13038 | 91.51 | 91.08 | 91.29 | 0.059 | 0.050 | 0.035 | 0.040 |
| 0.50 | all | 26193 | 26083 | 91.41 | 91.02 | 91.22 | 0.054 | 0.040 | 0.027 | 0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 12.67 | 12.95 | 1.19 | 1.44 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.72 | 13.54 | 2.05 | 3.42 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.95 | 10.19 | 1.44 | 1.78 | 4 | 4 |
| R8004_M8006__far_ch1 | 18.51 | 20.94 | 5.16 | 7.39 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.47 | 18.65 | 2.97 | 3.37 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.26 | 8.20 | 1.98 | 2.14 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.23 | 28.74 | 15.86 | 16.71 | 4 | 4 |
| R8006_M8012__far_ch1 | 11.80 | 12.36 | 3.01 | 3.39 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.62 | 8.33 | 0.79 | 0.93 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.08 | 11.36 | 1.88 | 2.12 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.72 | 12.39 | 1.36 | 2.34 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.77 | 6.64 | 0.56 | 0.74 | 3 | 3 |
| R8009_M8021__far_ch1 | 11.03 | 10.37 | 0.61 | 0.60 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.32 | 7.98 | 0.84 | 1.11 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.08 | 9.60 | 0.72 | 0.93 | 2 | 2 |
| R8009_M8024__far_ch1 | 7.67 | 7.50 | 1.82 | 1.81 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.47 | 7.87 | 0.76 | 0.63 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.84 | 7.79 | 0.86 | 0.96 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.52 | 6.31 | 1.75 | 1.68 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.18 | 6.07 | 0.79 | 0.78 | 2 | 2 |
