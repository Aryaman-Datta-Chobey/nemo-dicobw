# Diarization scores: epoch=15/alimeeting_Test_Ali_far_ch1__segments

- name: `epoch=15/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/epoch=15/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:44:43+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `epoch=15`
- model: `/mnt/data/exp/nemotron/20261027-nemotron-ft-ear1-nospkw/nemotron_ft_ear1_nospkw/checkpoints/nemotron_ft_ear1_nospkw--val_f1_acc=0.8335-epoch=15.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.50 | 15.32 | 1.55 | 0.63 | 18.08 | 95.00 | 0.05 |
| 0.25 | 9.32 | 8.74 | 0.39 | 0.19 | 11.01 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.95 (IoU 90.71) | 8.01 (IoU 8.06) |
| silence | 0.59 (IoU 0.64) | 7.45 (IoU 46.44) |

Speech P/R/F1: 99.31 / 91.29 / 95.13; miss 8.71 of ref speech, FA 7.28 of ref silence, SAD error 9.35.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12090 | 36.53 | 90.58 | 52.06 | 0.087 | 0.080 | 0.052 | 0.060 |
| 0.25 | offset | 4875 | 12091 | 36.10 | 89.54 | 51.46 | 0.097 | 0.090 | -0.057 | -0.070 |
| 0.25 | all | 9750 | 24181 | 36.31 | 90.06 | 51.76 | 0.092 | 0.090 | -0.002 | -0.010 |
| 0.50 | onset | 4875 | 12090 | 37.60 | 93.25 | 53.59 | 0.094 | 0.080 | 0.057 | 0.060 |
| 0.50 | offset | 4875 | 12091 | 38.09 | 94.48 | 54.30 | 0.109 | 0.100 | -0.064 | -0.080 |
| 0.50 | all | 9750 | 24181 | 37.85 | 93.87 | 53.94 | 0.101 | 0.090 | -0.004 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.15 | 17.37 | 12.16 | 12.56 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.70 | 18.72 | 11.99 | 13.83 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.43 | 17.13 | 10.26 | 11.59 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.62 | 25.27 | 17.45 | 19.70 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.50 | 24.06 | 15.75 | 15.90 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.56 | 13.16 | 10.05 | 9.16 | 4 | 4 |
| R8005_M8009__far_ch1 | 29.69 | 29.45 | 26.68 | 25.96 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.24 | 16.59 | 10.48 | 10.51 | 4 | 4 |
| R8008_M8014__far_ch1 | 13.47 | 14.24 | 9.54 | 10.08 | 3 | 4 |
| R8008_M8015__far_ch1 | 15.90 | 17.54 | 10.89 | 11.75 | 3 | 3 |
| R8008_M8016__far_ch1 | 16.54 | 19.71 | 10.59 | 13.38 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.85 | 13.92 | 8.36 | 8.93 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.61 | 16.51 | 4.27 | 4.11 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.43 | 15.60 | 2.66 | 3.08 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.00 | 18.26 | 3.50 | 4.97 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.81 | 14.70 | 2.91 | 2.90 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.39 | 14.24 | 2.83 | 3.11 | 2 | 2 |
| R8009_M8026__far_ch1 | 14.85 | 14.92 | 2.16 | 2.18 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.80 | 14.83 | 3.84 | 3.80 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.08 | 11.86 | 1.66 | 1.65 | 2 | 2 |
