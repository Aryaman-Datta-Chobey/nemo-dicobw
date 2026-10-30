# Diarization scores: A-fa-r0-seed43_s125/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0-seed43_s125/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s125/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T18:25:11+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0-seed43_s125`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7774-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.34 | 16.91 | 0.92 | 0.51 | 19.04 | 100.00 | 0.00 |
| 0.25 | 10.12 | 9.74 | 0.24 | 0.14 | 11.96 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.96 (IoU 89.96) | 9.00 (IoU 9.03) |
| silence | 0.26 (IoU 0.28) | 7.78 (IoU 45.67) |

Speech P/R/F1: 99.69 / 90.21 / 94.71; miss 9.79 of ref speech, FA 3.19 of ref silence, SAD error 10.07.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13047 | 35.15 | 94.07 | 51.18 | 0.081 | 0.080 | 0.059 | 0.070 |
| 0.25 | offset | 4875 | 13047 | 34.83 | 93.21 | 50.71 | 0.092 | 0.090 | -0.083 | -0.090 |
| 0.25 | all | 9750 | 26094 | 34.99 | 93.64 | 50.94 | 0.087 | 0.080 | -0.011 | -0.010 |
| 0.50 | onset | 4875 | 13047 | 36.05 | 96.47 | 52.48 | 0.088 | 0.080 | 0.064 | 0.070 |
| 0.50 | offset | 4875 | 13047 | 36.38 | 97.35 | 52.96 | 0.102 | 0.090 | -0.090 | -0.090 |
| 0.50 | all | 9750 | 26094 | 36.21 | 96.91 | 52.72 | 0.095 | 0.080 | -0.013 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.52 | 16.78 | 11.72 | 12.23 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.65 | 21.96 | 15.74 | 17.96 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.67 | 17.41 | 10.12 | 11.39 | 4 | 4 |
| R8004_M8006__far_ch1 | 24.23 | 26.97 | 18.40 | 20.53 | 4 | 4 |
| R8005_M8007__far_ch1 | 25.26 | 25.76 | 16.67 | 16.80 | 4 | 4 |
| R8005_M8008__far_ch1 | 14.18 | 13.78 | 10.24 | 9.29 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.87 | 28.73 | 25.52 | 24.99 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.46 | 16.84 | 10.82 | 10.93 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.63 | 16.22 | 11.67 | 12.08 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.67 | 22.46 | 17.80 | 18.23 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.20 | 22.56 | 13.53 | 16.94 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.29 | 16.56 | 12.10 | 12.70 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.60 | 15.54 | 3.62 | 3.48 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.46 | 14.51 | 2.09 | 2.42 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.31 | 17.32 | 2.62 | 3.66 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.08 | 13.02 | 1.17 | 1.17 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.13 | 13.87 | 2.21 | 2.10 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.63 | 16.75 | 2.81 | 2.85 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.81 | 14.72 | 3.36 | 3.24 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.62 | 12.44 | 1.62 | 1.64 | 2 | 2 |
