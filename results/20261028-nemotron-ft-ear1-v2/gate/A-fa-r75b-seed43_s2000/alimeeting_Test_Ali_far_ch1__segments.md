# Diarization scores: A-fa-r75b-seed43_s2000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b-seed43_s2000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s2000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T07:47:59+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b-seed43_s2000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7956-epoch=7.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.29 | 16.70 | 1.03 | 0.57 | 18.98 | 100.00 | 0.00 |
| 0.25 | 10.34 | 9.85 | 0.32 | 0.17 | 12.11 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.68 (IoU 89.65) | 9.28 (IoU 9.31) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 44.90) |

Speech P/R/F1: 99.68 / 89.90 / 94.54; miss 10.10 of ref speech, FA 3.26 of ref silence, SAD error 10.38.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12808 | 35.16 | 92.37 | 50.93 | 0.085 | 0.080 | 0.065 | 0.070 |
| 0.25 | offset | 4875 | 12809 | 34.73 | 91.24 | 50.31 | 0.093 | 0.090 | -0.081 | -0.090 |
| 0.25 | all | 9750 | 25617 | 34.94 | 91.81 | 50.62 | 0.089 | 0.080 | -0.008 | -0.010 |
| 0.50 | onset | 4875 | 12808 | 36.19 | 95.08 | 52.42 | 0.092 | 0.080 | 0.070 | 0.070 |
| 0.50 | offset | 4875 | 12809 | 36.64 | 96.27 | 53.08 | 0.105 | 0.090 | -0.090 | -0.090 |
| 0.50 | all | 9750 | 25617 | 36.41 | 95.67 | 52.75 | 0.098 | 0.090 | -0.010 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.22 | 16.49 | 11.40 | 11.87 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.96 | 21.35 | 15.57 | 17.89 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.15 | 16.80 | 10.17 | 11.47 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.86 | 25.42 | 17.92 | 20.01 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.77 | 24.33 | 16.32 | 16.51 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.22 | 12.83 | 9.96 | 9.04 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.22 | 28.06 | 25.21 | 24.61 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.40 | 16.87 | 10.93 | 11.05 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.15 | 16.90 | 12.21 | 12.74 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.87 | 22.65 | 18.10 | 18.40 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.30 | 22.73 | 13.68 | 17.11 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.74 | 17.07 | 12.43 | 13.07 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.51 | 16.41 | 4.12 | 3.96 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.05 | 15.24 | 2.44 | 2.89 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.57 | 18.84 | 3.77 | 5.25 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.08 | 14.05 | 1.89 | 1.91 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.64 | 14.33 | 2.49 | 2.32 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.52 | 17.63 | 3.05 | 3.09 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.13 | 16.05 | 4.34 | 4.22 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.80 | 13.46 | 2.82 | 2.75 | 2 | 2 |
