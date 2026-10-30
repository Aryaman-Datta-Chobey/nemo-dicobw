# Diarization scores: epoch=4/alimeeting_Test_Ali_far_ch1__nouem

- name: `epoch=4/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/epoch=4/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:44:07+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `epoch=4`
- model: `/mnt/data/exp/nemotron/20261027-nemotron-ft-ear1-nospkw/nemotron_ft_ear1_nospkw/checkpoints/nemotron_ft_ear1_nospkw--val_f1_acc=0.8548-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.86 | 5.08 | 6.02 | 0.76 | 12.42 | 100.00 | 0.00 |
| 0.25 | 1.76 | 0.92 | 0.78 | 0.07 | 2.62 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.61 (IoU 94.30) | 1.71 (IoU 1.77) |
| silence | 3.23 (IoU 3.28) | 13.46 (IoU 73.17) |

Speech P/R/F1: 96.20 / 97.95 / 97.07; miss 2.05 of ref speech, FA 19.34 of ref silence, SAD error 5.92.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13099 | 12153 | 93.30 | 86.56 | 89.81 | 0.051 | 0.040 | -0.015 | -0.010 |
| 0.25 | offset | 13097 | 12155 | 92.75 | 86.08 | 89.29 | 0.060 | 0.050 | 0.021 | 0.020 |
| 0.25 | all | 26196 | 24308 | 93.03 | 86.32 | 89.55 | 0.056 | 0.040 | 0.003 | 0.000 |
| 0.50 | onset | 13099 | 12153 | 94.26 | 87.45 | 90.73 | 0.054 | 0.040 | -0.015 | -0.010 |
| 0.50 | offset | 13097 | 12155 | 94.42 | 87.63 | 90.90 | 0.065 | 0.050 | 0.024 | 0.020 |
| 0.50 | all | 26196 | 24308 | 94.34 | 87.54 | 90.81 | 0.060 | 0.040 | 0.004 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.45 | 10.78 | 1.43 | 1.75 | 4 | 4 |
| R8002_M8003__far_ch1 | 13.81 | 14.57 | 1.76 | 2.86 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.46 | 10.61 | 1.38 | 1.74 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.13 | 22.43 | 5.27 | 7.72 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.93 | 19.90 | 2.71 | 2.94 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.61 | 7.61 | 1.63 | 1.75 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.35 | 19.35 | 8.98 | 8.47 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.83 | 11.32 | 2.45 | 2.65 | 4 | 4 |
| R8008_M8014__far_ch1 | 8.57 | 9.15 | 0.59 | 0.72 | 3 | 3 |
| R8008_M8015__far_ch1 | 16.92 | 17.15 | 1.69 | 2.13 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.67 | 11.92 | 1.58 | 2.60 | 3 | 3 |
| R8008_M8017__far_ch1 | 13.37 | 12.76 | 1.19 | 1.28 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.89 | 8.45 | 0.75 | 0.74 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.04 | 6.70 | 1.23 | 1.50 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.57 | 12.98 | 1.08 | 1.35 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.17 | 5.07 | 1.20 | 1.19 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.14 | 7.61 | 0.73 | 0.64 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.44 | 8.21 | 0.82 | 0.95 | 2 | 2 |
| R8009_M8027__far_ch1 | 7.46 | 7.05 | 1.53 | 1.50 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.23 | 6.90 | 0.95 | 0.95 | 2 | 2 |
