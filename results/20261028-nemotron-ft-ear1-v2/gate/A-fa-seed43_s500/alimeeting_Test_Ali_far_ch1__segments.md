# Diarization scores: A-fa-seed43_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-seed43_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-seed43_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T15:02:59+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-seed43_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7960-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.94 | 16.21 | 1.16 | 0.57 | 18.63 | 100.00 | 0.00 |
| 0.25 | 10.20 | 9.55 | 0.47 | 0.18 | 11.91 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.14 (IoU 90.11) | 8.82 (IoU 8.85) |
| silence | 0.31 (IoU 0.34) | 7.73 (IoU 45.87) |

Speech P/R/F1: 99.63 / 90.41 / 94.80; miss 9.59 of ref speech, FA 3.81 of ref silence, SAD error 9.92.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12631 | 35.59 | 92.21 | 51.35 | 0.077 | 0.070 | 0.056 | 0.060 |
| 0.25 | offset | 4875 | 12631 | 35.10 | 90.93 | 50.65 | 0.094 | 0.090 | -0.077 | -0.080 |
| 0.25 | all | 9750 | 25262 | 35.34 | 91.57 | 51.00 | 0.086 | 0.080 | -0.010 | 0.000 |
| 0.50 | onset | 4875 | 12631 | 36.52 | 94.63 | 52.70 | 0.084 | 0.070 | 0.061 | 0.060 |
| 0.50 | offset | 4875 | 12631 | 37.07 | 96.04 | 53.49 | 0.107 | 0.100 | -0.086 | -0.090 |
| 0.50 | all | 9750 | 25262 | 36.79 | 95.33 | 53.10 | 0.095 | 0.080 | -0.013 | -0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.52 | 16.81 | 11.18 | 11.64 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.71 | 21.16 | 15.29 | 17.62 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.77 | 16.45 | 9.98 | 11.26 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.08 | 24.62 | 17.33 | 19.50 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.33 | 23.95 | 16.15 | 16.39 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.83 | 12.48 | 9.66 | 8.82 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.87 | 27.74 | 24.94 | 24.38 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.25 | 16.69 | 10.67 | 10.75 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.90 | 16.68 | 11.85 | 12.43 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.68 | 22.44 | 17.84 | 18.17 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.21 | 22.57 | 13.40 | 16.74 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.30 | 16.59 | 12.15 | 12.76 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.59 | 15.52 | 3.71 | 3.58 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.18 | 14.23 | 2.12 | 2.46 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.99 | 18.12 | 3.38 | 4.67 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.96 | 12.90 | 1.26 | 1.25 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.07 | 13.72 | 2.42 | 2.24 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.21 | 17.34 | 3.24 | 3.31 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.58 | 15.52 | 4.20 | 4.09 | 2 | 2 |
| R8009_M8028__far_ch1 | 15.21 | 14.27 | 5.29 | 4.77 | 2 | 2 |
