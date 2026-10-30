# Diarization scores: A-fa-seed43_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-seed43_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-seed43_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T15:22:10+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-seed43_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7738-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.03 | 16.35 | 1.09 | 0.59 | 18.74 | 95.00 | 0.05 |
| 0.25 | 10.15 | 9.64 | 0.32 | 0.18 | 11.89 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.00 (IoU 89.95) | 8.96 (IoU 8.99) |
| silence | 0.31 (IoU 0.34) | 7.73 (IoU 45.48) |

Speech P/R/F1: 99.63 / 90.25 / 94.71; miss 9.75 of ref speech, FA 3.83 of ref silence, SAD error 10.08.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12678 | 35.20 | 91.55 | 50.85 | 0.082 | 0.080 | 0.061 | 0.070 |
| 0.25 | offset | 4875 | 12678 | 34.90 | 90.77 | 50.42 | 0.092 | 0.090 | -0.074 | -0.080 |
| 0.25 | all | 9750 | 25356 | 35.05 | 91.16 | 50.64 | 0.087 | 0.080 | -0.006 | 0.000 |
| 0.50 | onset | 4875 | 12678 | 36.22 | 94.19 | 52.32 | 0.089 | 0.080 | 0.066 | 0.070 |
| 0.50 | offset | 4875 | 12678 | 36.72 | 95.49 | 53.04 | 0.103 | 0.090 | -0.082 | -0.090 |
| 0.50 | all | 9750 | 25356 | 36.47 | 94.84 | 52.68 | 0.096 | 0.090 | -0.008 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.46 | 16.78 | 11.17 | 11.65 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.72 | 21.21 | 15.28 | 17.62 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.97 | 16.69 | 10.00 | 11.26 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.23 | 24.78 | 17.30 | 19.42 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.32 | 23.98 | 16.00 | 16.26 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.87 | 12.52 | 9.68 | 8.84 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.10 | 27.85 | 25.06 | 24.34 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.37 | 16.81 | 10.78 | 10.91 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.88 | 16.66 | 11.96 | 12.58 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.73 | 22.56 | 17.84 | 18.21 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.39 | 22.80 | 13.43 | 16.79 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.46 | 16.77 | 12.25 | 12.87 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.35 | 16.26 | 4.16 | 4.00 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.54 | 14.59 | 2.40 | 2.74 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.25 | 18.38 | 3.39 | 4.72 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.81 | 13.72 | 1.84 | 1.80 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.06 | 13.69 | 2.37 | 2.18 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.41 | 17.50 | 3.22 | 3.27 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.84 | 15.78 | 4.39 | 4.29 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.27 | 12.95 | 2.57 | 2.49 | 2 | 3 |
