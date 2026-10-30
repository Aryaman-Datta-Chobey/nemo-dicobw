# Diarization scores: epoch=15/alimeeting_Test_Ali_far_ch1__nouem

- name: `epoch=15/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/epoch=15/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:44:41+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `epoch=15`
- model: `/mnt/data/exp/nemotron/20261027-nemotron-ft-ear1-nospkw/nemotron_ft_ear1_nospkw/checkpoints/nemotron_ft_ear1_nospkw--val_f1_acc=0.8335-epoch=15.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.12 | 5.27 | 6.08 | 0.77 | 12.72 | 95.00 | 0.05 |
| 0.25 | 1.85 | 0.99 | 0.76 | 0.10 | 2.69 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.56 (IoU 94.17) | 1.76 (IoU 1.82) |
| silence | 3.29 (IoU 3.35) | 13.39 (IoU 72.62) |

Speech P/R/F1: 96.12 / 97.89 / 97.00; miss 2.11 of ref speech, FA 19.73 of ref silence, SAD error 6.06.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 12074 | 92.83 | 85.57 | 89.05 | 0.051 | 0.040 | -0.014 | -0.010 |
| 0.25 | offset | 13097 | 12077 | 92.42 | 85.23 | 88.68 | 0.062 | 0.050 | 0.024 | 0.020 |
| 0.25 | all | 26195 | 24151 | 92.63 | 85.40 | 88.87 | 0.057 | 0.040 | 0.005 | 0.000 |
| 0.50 | onset | 13098 | 12074 | 93.85 | 86.52 | 90.04 | 0.055 | 0.040 | -0.014 | -0.010 |
| 0.50 | offset | 13097 | 12077 | 93.91 | 86.59 | 90.10 | 0.067 | 0.050 | 0.026 | 0.020 |
| 0.50 | all | 26195 | 24151 | 93.88 | 86.55 | 90.07 | 0.061 | 0.050 | 0.006 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.87 | 11.10 | 2.05 | 2.20 | 4 | 4 |
| R8002_M8003__far_ch1 | 15.12 | 15.62 | 1.79 | 2.97 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.42 | 10.57 | 1.30 | 1.64 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.06 | 22.41 | 5.06 | 7.40 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.85 | 19.76 | 2.73 | 2.94 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.60 | 7.63 | 1.70 | 1.81 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.97 | 20.05 | 9.16 | 8.73 | 4 | 4 |
| R8006_M8012__far_ch1 | 11.29 | 11.75 | 2.38 | 2.54 | 4 | 4 |
| R8008_M8014__far_ch1 | 9.17 | 9.70 | 0.61 | 0.79 | 3 | 4 |
| R8008_M8015__far_ch1 | 17.87 | 17.72 | 1.60 | 2.08 | 3 | 3 |
| R8008_M8016__far_ch1 | 12.29 | 14.44 | 1.45 | 2.51 | 3 | 3 |
| R8008_M8017__far_ch1 | 11.21 | 11.14 | 0.66 | 0.79 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.24 | 7.88 | 0.83 | 0.81 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.44 | 7.11 | 1.32 | 1.57 | 2 | 2 |
| R8009_M8023__far_ch1 | 11.14 | 13.67 | 1.17 | 1.44 | 2 | 2 |
| R8009_M8024__far_ch1 | 6.14 | 5.99 | 2.11 | 2.13 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.04 | 8.05 | 1.35 | 1.85 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.75 | 8.52 | 0.65 | 0.72 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.58 | 6.36 | 1.68 | 1.64 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.05 | 6.80 | 0.78 | 0.78 | 2 | 2 |
