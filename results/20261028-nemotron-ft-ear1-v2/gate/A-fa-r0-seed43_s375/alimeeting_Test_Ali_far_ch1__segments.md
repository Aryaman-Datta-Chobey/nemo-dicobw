# Diarization scores: A-fa-r0-seed43_s375/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0-seed43_s375/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s375/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T18:49:36+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0-seed43_s375`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7947-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.80 | 16.39 | 0.90 | 0.50 | 18.56 | 100.00 | 0.00 |
| 0.25 | 9.87 | 9.44 | 0.26 | 0.17 | 11.72 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.43 (IoU 90.44) | 8.53 (IoU 8.55) |
| silence | 0.29 (IoU 0.32) | 7.75 (IoU 46.76) |

Speech P/R/F1: 99.65 / 90.72 / 94.98; miss 9.28 of ref speech, FA 3.63 of ref silence, SAD error 9.59.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12755 | 35.72 | 93.46 | 51.68 | 0.102 | 0.100 | 0.089 | 0.100 |
| 0.25 | offset | 4875 | 12755 | 36.39 | 95.20 | 52.65 | 0.071 | 0.060 | -0.049 | -0.050 |
| 0.25 | all | 9750 | 25510 | 36.05 | 94.33 | 52.17 | 0.086 | 0.080 | 0.020 | 0.010 |
| 0.50 | onset | 4875 | 12755 | 36.89 | 96.51 | 53.37 | 0.109 | 0.110 | 0.094 | 0.100 |
| 0.50 | offset | 4875 | 12755 | 37.16 | 97.23 | 53.77 | 0.076 | 0.060 | -0.051 | -0.050 |
| 0.50 | all | 9750 | 25510 | 37.02 | 96.87 | 53.57 | 0.092 | 0.080 | 0.021 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.25 | 17.51 | 11.15 | 11.58 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.10 | 21.54 | 15.47 | 17.80 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.83 | 16.51 | 9.96 | 11.29 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.19 | 24.66 | 17.49 | 19.57 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.63 | 24.18 | 16.34 | 16.56 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.11 | 12.73 | 9.74 | 8.94 | 4 | 4 |
| R8005_M8009__far_ch1 | 29.99 | 29.90 | 26.53 | 26.09 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.62 | 17.07 | 10.82 | 10.98 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.92 | 16.67 | 11.73 | 12.30 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.45 | 22.12 | 17.45 | 17.66 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.42 | 22.89 | 13.34 | 16.72 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.28 | 16.61 | 12.01 | 12.67 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.36 | 15.30 | 3.60 | 3.47 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.29 | 13.33 | 1.63 | 2.01 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.19 | 15.79 | 1.63 | 2.06 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.65 | 12.56 | 0.92 | 0.92 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.76 | 13.46 | 2.41 | 2.38 | 2 | 2 |
| R8009_M8026__far_ch1 | 15.42 | 15.57 | 2.11 | 2.16 | 2 | 2 |
| R8009_M8027__far_ch1 | 13.85 | 13.78 | 2.90 | 2.79 | 2 | 2 |
| R8009_M8028__far_ch1 | 11.63 | 11.50 | 1.21 | 1.24 | 2 | 2 |
