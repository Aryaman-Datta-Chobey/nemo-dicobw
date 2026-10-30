# Diarization scores: A-fa-r0-seed43_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0-seed43_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T20:10:47+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0-seed43_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7734-epoch=9.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 19.39 | 17.93 | 0.92 | 0.53 | 20.12 | 100.00 | 0.00 |
| 0.25 | 11.08 | 10.64 | 0.25 | 0.19 | 13.07 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.56 (IoU 89.46) | 9.40 (IoU 9.43) |
| silence | 0.33 (IoU 0.36) | 7.71 (IoU 44.23) |

Speech P/R/F1: 99.61 / 89.78 / 94.44; miss 10.22 of ref speech, FA 4.05 of ref silence, SAD error 10.58.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13157 | 33.53 | 90.48 | 48.92 | 0.102 | 0.100 | 0.088 | 0.100 |
| 0.25 | offset | 4875 | 13157 | 34.42 | 92.88 | 50.22 | 0.073 | 0.060 | -0.048 | -0.050 |
| 0.25 | all | 9750 | 26314 | 33.97 | 91.68 | 49.57 | 0.087 | 0.080 | 0.019 | 0.010 |
| 0.50 | onset | 4875 | 13157 | 34.88 | 94.13 | 50.90 | 0.111 | 0.110 | 0.094 | 0.100 |
| 0.50 | offset | 4875 | 13157 | 35.31 | 95.30 | 51.53 | 0.079 | 0.070 | -0.051 | -0.050 |
| 0.50 | all | 9750 | 26314 | 35.10 | 94.72 | 51.21 | 0.095 | 0.080 | 0.021 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 18.02 | 18.45 | 11.37 | 11.90 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.26 | 21.86 | 15.56 | 18.02 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.30 | 17.01 | 10.03 | 11.36 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.23 | 24.63 | 17.68 | 19.76 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.59 | 24.18 | 16.49 | 16.69 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.76 | 13.40 | 10.09 | 9.33 | 4 | 4 |
| R8005_M8009__far_ch1 | 42.16 | 41.32 | 39.09 | 37.92 | 4 | 4 |
| R8006_M8012__far_ch1 | 20.47 | 21.44 | 12.99 | 13.98 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.19 | 16.95 | 12.09 | 12.70 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.29 | 22.99 | 18.22 | 18.54 | 3 | 3 |
| R8008_M8016__far_ch1 | 20.32 | 23.88 | 13.76 | 17.27 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.49 | 16.79 | 12.23 | 12.85 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.87 | 15.79 | 4.04 | 3.89 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.72 | 13.78 | 1.91 | 2.31 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.65 | 16.29 | 1.98 | 2.50 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.83 | 14.76 | 3.32 | 3.32 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.69 | 13.21 | 2.20 | 1.93 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.75 | 16.85 | 2.69 | 2.74 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.17 | 15.11 | 3.85 | 3.75 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.36 | 12.19 | 1.57 | 1.58 | 2 | 2 |
