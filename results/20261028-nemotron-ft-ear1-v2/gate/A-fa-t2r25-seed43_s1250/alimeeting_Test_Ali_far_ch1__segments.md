# Diarization scores: A-fa-t2r25-seed43_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r25-seed43_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25-seed43_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T20:30:16+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r25-seed43_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7717-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.98 | 16.28 | 1.09 | 0.61 | 18.74 | 95.00 | 0.05 |
| 0.25 | 10.15 | 9.63 | 0.32 | 0.20 | 11.97 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.92 (IoU 89.88) | 9.04 (IoU 9.07) |
| silence | 0.30 (IoU 0.33) | 7.74 (IoU 45.33) |

Speech P/R/F1: 99.64 / 90.17 / 94.67; miss 9.83 of ref speech, FA 3.68 of ref silence, SAD error 10.16.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12726 | 35.23 | 91.96 | 50.94 | 0.087 | 0.080 | 0.068 | 0.070 |
| 0.25 | offset | 4875 | 12726 | 34.94 | 91.20 | 50.52 | 0.089 | 0.080 | -0.072 | -0.080 |
| 0.25 | all | 9750 | 25452 | 35.08 | 91.58 | 50.73 | 0.088 | 0.080 | -0.002 | 0.000 |
| 0.50 | onset | 4875 | 12726 | 36.24 | 94.61 | 52.41 | 0.094 | 0.080 | 0.072 | 0.080 |
| 0.50 | offset | 4875 | 12726 | 36.63 | 95.63 | 52.97 | 0.100 | 0.090 | -0.080 | -0.080 |
| 0.50 | all | 9750 | 25452 | 36.44 | 95.12 | 52.69 | 0.097 | 0.090 | -0.004 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.22 | 16.52 | 11.19 | 11.66 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.10 | 22.04 | 15.80 | 18.76 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.83 | 16.46 | 10.00 | 11.26 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.83 | 24.48 | 17.03 | 19.32 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.11 | 23.75 | 15.94 | 16.18 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.78 | 12.43 | 9.69 | 8.83 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.88 | 27.76 | 24.86 | 24.26 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.21 | 16.60 | 10.71 | 10.78 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.09 | 16.87 | 12.13 | 12.71 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.08 | 23.00 | 18.24 | 18.69 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.11 | 22.46 | 13.47 | 16.83 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.58 | 16.89 | 12.42 | 13.05 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.73 | 16.62 | 4.41 | 4.24 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.65 | 14.71 | 2.37 | 2.71 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.26 | 18.38 | 3.31 | 4.64 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.87 | 13.77 | 1.72 | 1.69 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.00 | 13.62 | 2.23 | 2.04 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.22 | 17.32 | 3.06 | 3.10 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.94 | 15.87 | 4.41 | 4.29 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.24 | 12.99 | 2.27 | 2.25 | 2 | 3 |
