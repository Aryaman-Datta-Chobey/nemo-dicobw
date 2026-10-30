# Diarization scores: A-fa-r75b_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T02:18:05+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7866-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.25 | 16.59 | 1.08 | 0.57 | 18.91 | 100.00 | 0.00 |
| 0.25 | 10.33 | 9.75 | 0.40 | 0.18 | 12.07 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.79 (IoU 89.77) | 9.17 (IoU 9.19) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 45.18) |

Speech P/R/F1: 99.68 / 90.03 / 94.61; miss 9.97 of ref speech, FA 3.29 of ref silence, SAD error 10.26.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12871 | 35.25 | 93.07 | 51.13 | 0.086 | 0.080 | 0.067 | 0.070 |
| 0.25 | offset | 4875 | 12871 | 34.81 | 91.92 | 50.50 | 0.091 | 0.090 | -0.079 | -0.080 |
| 0.25 | all | 9750 | 25742 | 35.03 | 92.49 | 50.82 | 0.089 | 0.080 | -0.005 | -0.010 |
| 0.50 | onset | 4875 | 12871 | 36.24 | 95.69 | 52.58 | 0.093 | 0.080 | 0.072 | 0.080 |
| 0.50 | offset | 4875 | 12871 | 36.63 | 96.72 | 53.14 | 0.102 | 0.090 | -0.087 | -0.090 |
| 0.50 | all | 9750 | 25742 | 36.44 | 96.21 | 52.86 | 0.098 | 0.090 | -0.008 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.22 | 16.49 | 11.41 | 11.88 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.95 | 21.23 | 15.89 | 18.08 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.16 | 16.86 | 10.11 | 11.40 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.70 | 25.24 | 17.60 | 19.63 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.93 | 24.53 | 16.45 | 16.65 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.17 | 12.81 | 9.95 | 9.07 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.31 | 28.16 | 25.40 | 24.84 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.35 | 16.79 | 10.88 | 10.96 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.09 | 16.82 | 12.10 | 12.63 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.71 | 22.49 | 17.99 | 18.28 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.10 | 22.39 | 13.56 | 16.86 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.61 | 16.93 | 12.38 | 13.02 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.35 | 16.26 | 4.02 | 3.87 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.12 | 15.29 | 2.46 | 2.88 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.19 | 18.37 | 3.29 | 4.65 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.91 | 13.87 | 1.77 | 1.78 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.41 | 14.10 | 2.36 | 2.21 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.41 | 17.52 | 3.03 | 3.07 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.85 | 15.75 | 4.05 | 3.93 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.47 | 13.89 | 3.79 | 3.56 | 2 | 2 |
