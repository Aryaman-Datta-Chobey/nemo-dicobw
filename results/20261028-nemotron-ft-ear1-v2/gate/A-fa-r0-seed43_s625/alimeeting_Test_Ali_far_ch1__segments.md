# Diarization scores: A-fa-r0-seed43_s625/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0-seed43_s625/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s625/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T19:11:58+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0-seed43_s625`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7829-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.76 | 17.33 | 0.91 | 0.52 | 19.53 | 100.00 | 0.00 |
| 0.25 | 10.64 | 10.21 | 0.25 | 0.17 | 12.64 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.99 (IoU 89.95) | 8.97 (IoU 8.99) |
| silence | 0.31 (IoU 0.34) | 7.73 (IoU 45.46) |

Speech P/R/F1: 99.63 / 90.25 / 94.71; miss 9.75 of ref speech, FA 3.84 of ref silence, SAD error 10.09.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13024 | 34.53 | 92.25 | 50.25 | 0.096 | 0.100 | 0.082 | 0.090 |
| 0.25 | offset | 4875 | 13024 | 35.22 | 94.09 | 51.25 | 0.074 | 0.060 | -0.052 | -0.050 |
| 0.25 | all | 9750 | 26048 | 34.87 | 93.17 | 50.75 | 0.085 | 0.080 | 0.015 | 0.010 |
| 0.50 | onset | 4875 | 13024 | 35.72 | 95.43 | 51.98 | 0.104 | 0.100 | 0.087 | 0.090 |
| 0.50 | offset | 4875 | 13024 | 36.10 | 96.45 | 52.54 | 0.080 | 0.070 | -0.055 | -0.050 |
| 0.50 | all | 9750 | 26048 | 35.91 | 95.94 | 52.26 | 0.092 | 0.080 | 0.016 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.95 | 18.37 | 11.61 | 12.16 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.76 | 21.15 | 15.28 | 17.55 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.23 | 16.92 | 10.12 | 11.41 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.20 | 24.66 | 17.61 | 19.66 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.63 | 24.20 | 16.38 | 16.61 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.88 | 13.54 | 10.31 | 9.56 | 4 | 4 |
| R8005_M8009__far_ch1 | 39.11 | 39.65 | 35.34 | 35.80 | 4 | 4 |
| R8006_M8012__far_ch1 | 17.40 | 18.02 | 11.37 | 11.75 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.02 | 16.84 | 11.89 | 12.53 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.69 | 22.45 | 17.77 | 18.09 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.37 | 22.85 | 13.28 | 16.65 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.37 | 16.69 | 12.18 | 12.81 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.44 | 15.37 | 3.77 | 3.64 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.49 | 13.54 | 1.83 | 2.22 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.41 | 16.09 | 1.86 | 2.37 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.68 | 13.60 | 2.29 | 2.29 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.58 | 13.10 | 2.15 | 1.88 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.34 | 16.48 | 2.58 | 2.63 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.77 | 14.70 | 3.66 | 3.55 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.00 | 11.84 | 1.45 | 1.47 | 2 | 2 |
