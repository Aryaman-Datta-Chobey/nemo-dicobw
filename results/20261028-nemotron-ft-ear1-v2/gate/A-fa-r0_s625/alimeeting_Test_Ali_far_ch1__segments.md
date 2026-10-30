# Diarization scores: A-fa-r0_s625/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0_s625/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s625/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T17:46:59+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0_s625`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7892-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 19.14 | 17.76 | 0.87 | 0.52 | 19.97 | 100.00 | 0.00 |
| 0.25 | 10.90 | 10.48 | 0.24 | 0.18 | 13.04 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.91 (IoU 89.86) | 9.05 (IoU 9.08) |
| silence | 0.30 (IoU 0.33) | 7.74 (IoU 45.26) |

Speech P/R/F1: 99.63 / 90.16 / 94.66; miss 9.84 of ref speech, FA 3.78 of ref silence, SAD error 10.18.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13083 | 34.33 | 92.12 | 50.02 | 0.097 | 0.090 | 0.083 | 0.090 |
| 0.25 | offset | 4875 | 13083 | 34.96 | 93.83 | 50.94 | 0.074 | 0.060 | -0.051 | -0.050 |
| 0.25 | all | 9750 | 26166 | 34.64 | 92.97 | 50.48 | 0.085 | 0.080 | 0.015 | 0.010 |
| 0.50 | onset | 4875 | 13083 | 35.48 | 95.22 | 51.70 | 0.104 | 0.100 | 0.088 | 0.090 |
| 0.50 | offset | 4875 | 13083 | 35.84 | 96.18 | 52.22 | 0.080 | 0.070 | -0.054 | -0.050 |
| 0.50 | all | 9750 | 26166 | 35.66 | 95.70 | 51.96 | 0.092 | 0.080 | 0.016 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.86 | 18.32 | 11.53 | 12.12 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.58 | 20.94 | 15.03 | 17.18 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.27 | 17.06 | 10.20 | 11.61 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.46 | 25.03 | 17.86 | 20.16 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.11 | 24.65 | 16.80 | 17.00 | 4 | 4 |
| R8005_M8008__far_ch1 | 14.26 | 14.12 | 10.54 | 10.06 | 4 | 4 |
| R8005_M8009__far_ch1 | 43.40 | 44.35 | 39.42 | 40.36 | 4 | 4 |
| R8006_M8012__far_ch1 | 18.10 | 18.85 | 11.86 | 12.44 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.04 | 16.84 | 11.91 | 12.51 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.99 | 22.83 | 18.00 | 18.36 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.57 | 23.10 | 13.35 | 16.74 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.39 | 16.73 | 12.18 | 12.82 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.40 | 15.33 | 3.74 | 3.60 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.45 | 13.48 | 1.81 | 2.20 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.23 | 15.89 | 1.81 | 2.33 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.71 | 12.62 | 1.22 | 1.21 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.60 | 13.15 | 2.13 | 1.89 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.19 | 16.32 | 2.55 | 2.60 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.69 | 14.61 | 3.68 | 3.56 | 2 | 2 |
| R8009_M8028__far_ch1 | 11.93 | 11.79 | 1.44 | 1.46 | 2 | 2 |
