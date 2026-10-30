# Diarization scores: A-fa-r75b-seed43_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b-seed43_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T07:19:15+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b-seed43_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7922-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.29 | 16.70 | 1.03 | 0.57 | 18.98 | 100.00 | 0.00 |
| 0.25 | 10.33 | 9.83 | 0.34 | 0.17 | 12.12 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.72 (IoU 89.70) | 9.24 (IoU 9.26) |
| silence | 0.26 (IoU 0.28) | 7.78 (IoU 45.05) |

Speech P/R/F1: 99.69 / 89.95 / 94.57; miss 10.05 of ref speech, FA 3.19 of ref silence, SAD error 10.33.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12848 | 35.18 | 92.72 | 51.01 | 0.086 | 0.080 | 0.067 | 0.070 |
| 0.25 | offset | 4875 | 12849 | 34.79 | 91.69 | 50.44 | 0.092 | 0.090 | -0.080 | -0.080 |
| 0.25 | all | 9750 | 25697 | 34.98 | 92.21 | 50.72 | 0.089 | 0.080 | -0.006 | -0.010 |
| 0.50 | onset | 4875 | 12848 | 36.24 | 95.51 | 52.54 | 0.094 | 0.080 | 0.072 | 0.080 |
| 0.50 | offset | 4875 | 12849 | 36.61 | 96.49 | 53.08 | 0.103 | 0.090 | -0.089 | -0.090 |
| 0.50 | all | 9750 | 25697 | 36.42 | 96.00 | 52.81 | 0.098 | 0.090 | -0.008 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.31 | 16.58 | 11.45 | 11.90 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.05 | 21.36 | 15.97 | 18.19 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.14 | 16.80 | 10.15 | 11.44 | 4 | 4 |
| R8004_M8006__far_ch1 | 23.01 | 25.59 | 18.01 | 20.18 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.83 | 24.40 | 16.36 | 16.54 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.16 | 12.78 | 9.93 | 9.03 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.23 | 28.16 | 25.22 | 24.69 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.42 | 16.88 | 10.90 | 11.03 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.11 | 16.87 | 12.16 | 12.71 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.14 | 23.09 | 18.21 | 18.66 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.26 | 22.60 | 13.70 | 17.07 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.86 | 17.19 | 12.55 | 13.19 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.56 | 16.47 | 4.12 | 3.96 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.13 | 15.31 | 2.49 | 2.93 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.38 | 18.47 | 3.42 | 4.68 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.85 | 13.80 | 1.56 | 1.55 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.55 | 14.19 | 2.44 | 2.27 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.19 | 17.28 | 2.97 | 2.98 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.02 | 15.92 | 4.22 | 4.09 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.67 | 13.30 | 2.77 | 2.68 | 2 | 2 |
