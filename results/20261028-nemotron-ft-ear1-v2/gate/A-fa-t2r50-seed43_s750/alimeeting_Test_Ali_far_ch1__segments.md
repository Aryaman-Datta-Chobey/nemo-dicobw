# Diarization scores: A-fa-t2r50-seed43_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r50-seed43_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50-seed43_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T21:21:16+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r50-seed43_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7823-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.09 | 16.35 | 1.15 | 0.59 | 18.76 | 100.00 | 0.00 |
| 0.25 | 10.24 | 9.61 | 0.44 | 0.19 | 11.97 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.87 (IoU 89.85) | 9.09 (IoU 9.11) |
| silence | 0.28 (IoU 0.30) | 7.76 (IoU 45.33) |

Speech P/R/F1: 99.67 / 90.12 / 94.65; miss 9.88 of ref speech, FA 3.43 of ref silence, SAD error 10.18.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12690 | 35.41 | 92.16 | 51.16 | 0.087 | 0.080 | 0.068 | 0.070 |
| 0.25 | offset | 4875 | 12690 | 35.14 | 91.47 | 50.77 | 0.089 | 0.080 | -0.074 | -0.080 |
| 0.25 | all | 9750 | 25380 | 35.27 | 91.82 | 50.96 | 0.088 | 0.080 | -0.003 | 0.000 |
| 0.50 | onset | 4875 | 12690 | 36.48 | 94.95 | 52.71 | 0.095 | 0.090 | 0.073 | 0.080 |
| 0.50 | offset | 4875 | 12690 | 36.97 | 96.23 | 53.41 | 0.101 | 0.090 | -0.083 | -0.080 |
| 0.50 | all | 9750 | 25380 | 36.72 | 95.59 | 53.06 | 0.098 | 0.090 | -0.005 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.23 | 16.53 | 11.24 | 11.71 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.64 | 21.06 | 15.35 | 17.61 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.95 | 16.55 | 10.11 | 11.38 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.21 | 24.85 | 17.36 | 19.63 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.54 | 24.19 | 16.16 | 16.42 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.96 | 12.60 | 9.81 | 8.94 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.75 | 27.68 | 24.85 | 24.31 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.15 | 16.59 | 10.68 | 10.80 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.98 | 16.76 | 12.06 | 12.63 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.52 | 22.32 | 17.84 | 18.16 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.04 | 22.38 | 13.41 | 16.73 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.53 | 16.83 | 12.35 | 12.97 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.27 | 16.18 | 4.02 | 3.87 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.89 | 15.01 | 2.37 | 2.74 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.26 | 18.27 | 3.16 | 4.44 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.62 | 13.56 | 1.37 | 1.37 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.75 | 14.65 | 2.81 | 3.00 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.36 | 17.47 | 3.06 | 3.11 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.00 | 15.93 | 4.21 | 4.11 | 2 | 2 |
| R8009_M8028__far_ch1 | 15.05 | 14.29 | 4.60 | 4.24 | 2 | 2 |
