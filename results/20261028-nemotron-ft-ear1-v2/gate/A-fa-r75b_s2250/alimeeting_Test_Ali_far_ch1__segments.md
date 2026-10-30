# Diarization scores: A-fa-r75b_s2250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b_s2250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s2250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T03:13:40+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b_s2250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7837-epoch=8.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.21 | 16.62 | 1.02 | 0.58 | 18.92 | 100.00 | 0.00 |
| 0.25 | 10.25 | 9.76 | 0.30 | 0.18 | 12.04 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.76 (IoU 89.74) | 9.20 (IoU 9.22) |
| silence | 0.26 (IoU 0.28) | 7.78 (IoU 45.14) |

Speech P/R/F1: 99.69 / 90.00 / 94.60; miss 10.00 of ref speech, FA 3.21 of ref silence, SAD error 10.28.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12812 | 35.19 | 92.49 | 50.99 | 0.088 | 0.080 | 0.070 | 0.080 |
| 0.25 | offset | 4875 | 12812 | 34.93 | 91.79 | 50.60 | 0.089 | 0.080 | -0.077 | -0.080 |
| 0.25 | all | 9750 | 25624 | 35.06 | 92.14 | 50.79 | 0.089 | 0.080 | -0.003 | -0.010 |
| 0.50 | onset | 4875 | 12812 | 36.28 | 95.34 | 52.56 | 0.096 | 0.090 | 0.075 | 0.080 |
| 0.50 | offset | 4875 | 12812 | 36.67 | 96.37 | 53.12 | 0.100 | 0.090 | -0.084 | -0.080 |
| 0.50 | all | 9750 | 25624 | 36.47 | 95.86 | 52.84 | 0.098 | 0.090 | -0.005 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.19 | 16.48 | 11.38 | 11.83 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.07 | 21.64 | 15.75 | 18.29 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.15 | 16.86 | 10.10 | 11.40 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.83 | 25.32 | 17.93 | 19.97 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.87 | 24.45 | 16.35 | 16.55 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.24 | 12.82 | 10.01 | 9.08 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.12 | 27.90 | 25.17 | 24.50 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.25 | 16.73 | 10.78 | 10.91 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.22 | 17.00 | 12.21 | 12.78 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.86 | 22.72 | 18.07 | 18.44 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.16 | 22.52 | 13.56 | 16.92 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.69 | 17.01 | 12.42 | 13.07 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.51 | 16.41 | 4.08 | 3.92 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.04 | 15.23 | 2.37 | 2.79 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.04 | 18.24 | 3.20 | 4.58 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.76 | 13.69 | 1.55 | 1.54 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.44 | 14.18 | 2.34 | 2.20 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.52 | 17.63 | 3.06 | 3.10 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.01 | 15.93 | 4.21 | 4.10 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.24 | 12.97 | 2.26 | 2.23 | 2 | 2 |
