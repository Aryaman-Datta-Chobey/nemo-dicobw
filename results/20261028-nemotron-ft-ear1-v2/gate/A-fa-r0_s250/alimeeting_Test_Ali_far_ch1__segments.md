# Diarization scores: A-fa-r0_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T17:13:36+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7701-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.48 | 17.20 | 0.79 | 0.50 | 19.24 | 100.00 | 0.00 |
| 0.25 | 10.20 | 9.79 | 0.22 | 0.19 | 12.12 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.10 (IoU 90.12) | 8.86 (IoU 8.88) |
| silence | 0.24 (IoU 0.27) | 7.80 (IoU 46.13) |

Speech P/R/F1: 99.71 / 90.36 / 94.81; miss 9.64 of ref speech, FA 3.04 of ref silence, SAD error 9.90.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12977 | 35.42 | 94.28 | 51.49 | 0.096 | 0.100 | 0.082 | 0.090 |
| 0.25 | offset | 4875 | 12977 | 35.72 | 95.08 | 51.93 | 0.079 | 0.070 | -0.065 | -0.070 |
| 0.25 | all | 9750 | 25954 | 35.57 | 94.68 | 51.71 | 0.088 | 0.080 | 0.008 | 0.000 |
| 0.50 | onset | 4875 | 12977 | 36.41 | 96.92 | 52.94 | 0.103 | 0.100 | 0.086 | 0.090 |
| 0.50 | offset | 4875 | 12977 | 36.63 | 97.50 | 53.25 | 0.085 | 0.070 | -0.069 | -0.070 |
| 0.50 | all | 9750 | 25954 | 36.52 | 97.21 | 53.09 | 0.094 | 0.080 | 0.008 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.59 | 17.86 | 11.83 | 12.30 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.79 | 22.13 | 15.89 | 18.22 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.73 | 17.48 | 10.29 | 11.66 | 4 | 4 |
| R8004_M8006__far_ch1 | 23.81 | 26.45 | 18.41 | 20.49 | 4 | 4 |
| R8005_M8007__far_ch1 | 25.43 | 25.92 | 17.13 | 17.29 | 4 | 4 |
| R8005_M8008__far_ch1 | 14.05 | 13.68 | 10.17 | 9.33 | 4 | 4 |
| R8005_M8009__far_ch1 | 30.88 | 30.75 | 27.04 | 26.55 | 4 | 4 |
| R8006_M8012__far_ch1 | 17.01 | 17.38 | 11.05 | 11.21 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.07 | 16.71 | 11.80 | 12.26 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.60 | 22.18 | 17.63 | 17.89 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.87 | 23.35 | 13.64 | 17.05 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.45 | 16.72 | 12.18 | 12.75 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.71 | 15.66 | 3.59 | 3.46 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.59 | 13.64 | 1.71 | 2.10 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.61 | 16.24 | 1.80 | 2.35 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.85 | 12.77 | 0.90 | 0.90 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.81 | 15.22 | 3.24 | 4.26 | 2 | 2 |
| R8009_M8026__far_ch1 | 15.87 | 16.01 | 2.33 | 2.37 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.00 | 13.92 | 2.83 | 2.71 | 2 | 2 |
| R8009_M8028__far_ch1 | 11.94 | 11.81 | 1.24 | 1.27 | 2 | 2 |
