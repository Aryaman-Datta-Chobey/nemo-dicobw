# Diarization scores: A-fa-r0_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T18:45:46+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7828-epoch=9.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 19.63 | 18.19 | 0.91 | 0.53 | 20.34 | 100.00 | 0.00 |
| 0.25 | 11.29 | 10.87 | 0.24 | 0.18 | 13.35 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.43 (IoU 89.32) | 9.53 (IoU 9.56) |
| silence | 0.32 (IoU 0.35) | 7.72 (IoU 43.94) |

Speech P/R/F1: 99.61 / 89.63 / 94.36; miss 10.37 of ref speech, FA 3.97 of ref silence, SAD error 10.71.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13172 | 33.77 | 91.24 | 49.29 | 0.101 | 0.100 | 0.087 | 0.100 |
| 0.25 | offset | 4875 | 13172 | 34.58 | 93.44 | 50.48 | 0.072 | 0.060 | -0.046 | -0.050 |
| 0.25 | all | 9750 | 26344 | 34.17 | 92.34 | 49.89 | 0.086 | 0.080 | 0.020 | 0.010 |
| 0.50 | onset | 4875 | 13172 | 35.04 | 94.67 | 51.14 | 0.110 | 0.110 | 0.093 | 0.100 |
| 0.50 | offset | 4875 | 13172 | 35.37 | 95.57 | 51.63 | 0.077 | 0.060 | -0.048 | -0.050 |
| 0.50 | all | 9750 | 26344 | 35.20 | 95.12 | 51.39 | 0.093 | 0.080 | 0.022 | 0.020 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 18.32 | 18.80 | 11.64 | 12.21 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.97 | 21.52 | 15.37 | 17.72 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.87 | 17.63 | 10.28 | 11.59 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.29 | 24.69 | 17.73 | 19.85 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.61 | 24.22 | 16.44 | 16.66 | 4 | 4 |
| R8005_M8008__far_ch1 | 14.15 | 13.95 | 10.41 | 9.82 | 4 | 4 |
| R8005_M8009__far_ch1 | 47.39 | 46.06 | 44.51 | 42.80 | 4 | 4 |
| R8006_M8012__far_ch1 | 19.79 | 20.86 | 13.04 | 14.17 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.17 | 17.01 | 12.04 | 12.67 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.37 | 23.26 | 18.33 | 18.74 | 3 | 3 |
| R8008_M8016__far_ch1 | 20.21 | 23.80 | 13.57 | 17.07 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.37 | 16.68 | 12.15 | 12.75 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.72 | 15.63 | 4.01 | 3.86 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.39 | 13.48 | 1.76 | 2.19 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.42 | 16.09 | 1.89 | 2.43 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.61 | 12.52 | 1.14 | 1.13 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.64 | 13.13 | 2.17 | 1.88 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.30 | 16.39 | 2.51 | 2.53 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.67 | 14.60 | 3.58 | 3.47 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.00 | 11.83 | 1.39 | 1.40 | 2 | 2 |
