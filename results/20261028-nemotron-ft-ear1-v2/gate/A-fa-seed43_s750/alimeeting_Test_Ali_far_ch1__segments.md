# Diarization scores: A-fa-seed43_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-seed43_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-seed43_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T15:12:35+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-seed43_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7737-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.18 | 16.56 | 1.05 | 0.57 | 18.90 | 100.00 | 0.00 |
| 0.25 | 10.26 | 9.75 | 0.32 | 0.19 | 12.03 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.91 (IoU 89.86) | 9.05 (IoU 9.08) |
| silence | 0.30 (IoU 0.33) | 7.74 (IoU 45.26) |

Speech P/R/F1: 99.64 / 90.15 / 94.66; miss 9.85 of ref speech, FA 3.78 of ref silence, SAD error 10.18.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12726 | 34.90 | 91.10 | 50.46 | 0.080 | 0.070 | 0.060 | 0.060 |
| 0.25 | offset | 4875 | 12726 | 34.63 | 90.40 | 50.08 | 0.094 | 0.090 | -0.076 | -0.080 |
| 0.25 | all | 9750 | 25452 | 34.76 | 90.75 | 50.27 | 0.087 | 0.080 | -0.008 | 0.000 |
| 0.50 | onset | 4875 | 12726 | 36.01 | 93.99 | 52.07 | 0.088 | 0.080 | 0.065 | 0.070 |
| 0.50 | offset | 4875 | 12726 | 36.63 | 95.61 | 52.96 | 0.107 | 0.090 | -0.086 | -0.090 |
| 0.50 | all | 9750 | 25452 | 36.32 | 94.80 | 52.51 | 0.098 | 0.080 | -0.011 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.59 | 16.89 | 11.26 | 11.73 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.80 | 21.30 | 15.27 | 17.57 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.09 | 16.95 | 10.15 | 11.70 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.29 | 24.85 | 17.43 | 19.58 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.52 | 24.12 | 16.21 | 16.44 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.99 | 12.61 | 9.77 | 8.92 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.57 | 28.41 | 25.49 | 24.90 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.33 | 16.77 | 10.76 | 10.91 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.02 | 16.82 | 12.00 | 12.62 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.94 | 22.77 | 18.04 | 18.46 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.54 | 22.93 | 13.46 | 16.80 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.60 | 16.92 | 12.36 | 12.98 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.24 | 16.15 | 4.09 | 3.93 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.71 | 14.78 | 2.41 | 2.76 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.96 | 18.00 | 3.18 | 4.41 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.49 | 13.42 | 1.45 | 1.44 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.52 | 14.17 | 2.77 | 2.64 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.74 | 17.86 | 3.43 | 3.50 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.31 | 16.28 | 4.70 | 4.62 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.63 | 13.23 | 2.90 | 2.78 | 2 | 2 |
