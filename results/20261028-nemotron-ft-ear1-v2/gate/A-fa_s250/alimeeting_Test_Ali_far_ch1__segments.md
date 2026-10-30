# Diarization scores: A-fa_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T20:35:10+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7891-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.81 | 16.39 | 0.92 | 0.50 | 18.52 | 100.00 | 0.00 |
| 0.25 | 9.87 | 9.45 | 0.28 | 0.15 | 11.67 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.25 (IoU 90.27) | 8.71 (IoU 8.73) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 46.44) |

Speech P/R/F1: 99.69 / 90.53 / 94.89; miss 9.47 of ref speech, FA 3.25 of ref silence, SAD error 9.75.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12767 | 35.87 | 93.95 | 51.92 | 0.092 | 0.090 | 0.077 | 0.090 |
| 0.25 | offset | 4875 | 12767 | 36.22 | 94.85 | 52.42 | 0.081 | 0.070 | -0.065 | -0.070 |
| 0.25 | all | 9750 | 25534 | 36.05 | 94.40 | 52.17 | 0.086 | 0.080 | 0.006 | 0.000 |
| 0.50 | onset | 4875 | 12767 | 36.87 | 96.55 | 53.36 | 0.099 | 0.090 | 0.081 | 0.090 |
| 0.50 | offset | 4875 | 12767 | 37.16 | 97.31 | 53.78 | 0.087 | 0.070 | -0.069 | -0.070 |
| 0.50 | all | 9750 | 25534 | 37.01 | 96.93 | 53.57 | 0.093 | 0.080 | 0.006 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.83 | 17.11 | 11.34 | 11.79 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.11 | 21.35 | 15.56 | 17.71 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.04 | 16.67 | 10.02 | 11.27 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.48 | 25.08 | 17.45 | 19.55 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.08 | 24.61 | 16.38 | 16.54 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.21 | 12.83 | 9.87 | 9.01 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.34 | 28.20 | 25.18 | 24.65 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.36 | 16.72 | 10.77 | 10.86 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.92 | 16.62 | 11.79 | 12.28 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.41 | 22.07 | 17.59 | 17.93 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.35 | 22.74 | 13.43 | 16.80 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.19 | 16.44 | 12.02 | 12.58 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.45 | 15.41 | 3.55 | 3.42 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.65 | 13.64 | 1.76 | 2.10 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.65 | 16.32 | 1.97 | 2.64 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.69 | 12.63 | 0.92 | 0.92 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.73 | 13.27 | 2.11 | 1.88 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.11 | 16.22 | 2.46 | 2.49 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.32 | 14.22 | 3.09 | 2.97 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.20 | 12.02 | 1.64 | 1.65 | 2 | 2 |
