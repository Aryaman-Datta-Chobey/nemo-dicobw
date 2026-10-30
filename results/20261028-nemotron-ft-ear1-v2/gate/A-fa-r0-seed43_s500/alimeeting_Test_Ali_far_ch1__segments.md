# Diarization scores: A-fa-r0-seed43_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0-seed43_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T19:00:47+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0-seed43_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7953-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 19.06 | 17.69 | 0.86 | 0.51 | 19.77 | 100.00 | 0.00 |
| 0.25 | 10.82 | 10.42 | 0.23 | 0.18 | 12.80 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.80 (IoU 89.76) | 9.16 (IoU 9.19) |
| silence | 0.29 (IoU 0.32) | 7.75 (IoU 45.06) |

Speech P/R/F1: 99.65 / 90.04 / 94.60; miss 9.96 of ref speech, FA 3.60 of ref silence, SAD error 10.27.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13222 | 34.11 | 92.51 | 49.84 | 0.101 | 0.100 | 0.088 | 0.100 |
| 0.25 | offset | 4875 | 13222 | 34.86 | 94.54 | 50.94 | 0.071 | 0.060 | -0.049 | -0.050 |
| 0.25 | all | 9750 | 26444 | 34.48 | 93.53 | 50.39 | 0.086 | 0.080 | 0.019 | 0.010 |
| 0.50 | onset | 4875 | 13222 | 35.27 | 95.67 | 51.54 | 0.109 | 0.110 | 0.093 | 0.100 |
| 0.50 | offset | 4875 | 13222 | 35.66 | 96.72 | 52.11 | 0.077 | 0.060 | -0.052 | -0.050 |
| 0.50 | all | 9750 | 26444 | 35.47 | 96.19 | 51.83 | 0.093 | 0.080 | 0.020 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 18.15 | 18.64 | 11.71 | 12.32 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.73 | 21.15 | 15.18 | 17.45 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.46 | 17.10 | 10.31 | 11.59 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.27 | 24.74 | 17.58 | 19.74 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.87 | 24.41 | 16.61 | 16.83 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.65 | 13.38 | 10.01 | 9.32 | 4 | 4 |
| R8005_M8009__far_ch1 | 41.95 | 41.38 | 37.91 | 37.05 | 4 | 4 |
| R8006_M8012__far_ch1 | 18.52 | 19.28 | 12.20 | 12.76 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.08 | 16.91 | 11.89 | 12.53 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.73 | 22.41 | 17.83 | 18.07 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.78 | 23.28 | 13.53 | 16.93 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.38 | 16.70 | 12.13 | 12.77 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.49 | 15.42 | 3.76 | 3.62 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.42 | 13.47 | 1.77 | 2.17 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.28 | 15.95 | 1.76 | 2.24 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.46 | 13.38 | 1.87 | 1.87 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.92 | 13.48 | 2.52 | 2.28 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.02 | 16.18 | 2.41 | 2.47 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.51 | 14.44 | 3.42 | 3.32 | 2 | 2 |
| R8009_M8028__far_ch1 | 11.95 | 11.81 | 1.38 | 1.41 | 2 | 2 |
