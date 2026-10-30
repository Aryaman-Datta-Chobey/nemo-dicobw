# Diarization scores: A-fa-r75a-seed43_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a-seed43_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T04:21:25+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a-seed43_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7752-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.26 | 16.48 | 1.21 | 0.56 | 18.85 | 100.00 | 0.00 |
| 0.25 | 10.44 | 9.69 | 0.57 | 0.17 | 12.07 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.87 (IoU 89.85) | 9.09 (IoU 9.12) |
| silence | 0.27 (IoU 0.29) | 7.78 (IoU 45.38) |

Speech P/R/F1: 99.68 / 90.11 / 94.65; miss 9.89 of ref speech, FA 3.30 of ref silence, SAD error 10.18.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12726 | 35.36 | 92.31 | 51.13 | 0.085 | 0.080 | 0.066 | 0.070 |
| 0.25 | offset | 4875 | 12726 | 35.13 | 91.71 | 50.80 | 0.090 | 0.080 | -0.077 | -0.080 |
| 0.25 | all | 9750 | 25452 | 35.25 | 92.01 | 50.97 | 0.087 | 0.080 | -0.005 | -0.010 |
| 0.50 | onset | 4875 | 12726 | 36.36 | 94.91 | 52.58 | 0.092 | 0.080 | 0.071 | 0.080 |
| 0.50 | offset | 4875 | 12726 | 36.83 | 96.14 | 53.26 | 0.101 | 0.090 | -0.085 | -0.090 |
| 0.50 | all | 9750 | 25452 | 36.59 | 95.53 | 52.92 | 0.096 | 0.090 | -0.007 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.42 | 16.69 | 11.47 | 11.92 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.76 | 21.02 | 15.52 | 17.68 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.00 | 16.62 | 10.15 | 11.43 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.47 | 25.03 | 17.52 | 19.66 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.82 | 24.39 | 16.27 | 16.48 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.11 | 12.71 | 9.90 | 8.98 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.86 | 27.71 | 24.88 | 24.27 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.19 | 16.63 | 10.66 | 10.74 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.80 | 16.46 | 11.88 | 12.38 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.65 | 22.33 | 17.89 | 18.17 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.29 | 22.63 | 13.67 | 17.03 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.43 | 16.74 | 12.25 | 12.87 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.09 | 16.02 | 3.82 | 3.68 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.07 | 15.25 | 2.50 | 2.95 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.13 | 18.19 | 3.31 | 4.50 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.45 | 13.40 | 1.36 | 1.36 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.68 | 14.42 | 2.65 | 2.52 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.46 | 17.57 | 3.21 | 3.28 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.78 | 15.71 | 4.07 | 3.97 | 2 | 2 |
| R8009_M8028__far_ch1 | 17.65 | 16.07 | 7.83 | 6.76 | 2 | 2 |
