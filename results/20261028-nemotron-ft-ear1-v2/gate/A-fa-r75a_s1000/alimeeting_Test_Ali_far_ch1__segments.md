# Diarization scores: A-fa-r75a_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T23:52:51+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7782-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.04 | 16.44 | 1.04 | 0.56 | 18.71 | 100.00 | 0.00 |
| 0.25 | 10.10 | 9.64 | 0.30 | 0.16 | 11.86 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.85 (IoU 89.83) | 9.11 (IoU 9.13) |
| silence | 0.27 (IoU 0.30) | 7.77 (IoU 45.32) |

Speech P/R/F1: 99.68 / 90.10 / 94.64; miss 9.90 of ref speech, FA 3.35 of ref silence, SAD error 10.20.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12712 | 35.49 | 92.53 | 51.30 | 0.085 | 0.080 | 0.066 | 0.070 |
| 0.25 | offset | 4875 | 12712 | 35.10 | 91.53 | 50.74 | 0.092 | 0.090 | -0.078 | -0.080 |
| 0.25 | all | 9750 | 25424 | 35.29 | 92.03 | 51.02 | 0.089 | 0.080 | -0.006 | -0.010 |
| 0.50 | onset | 4875 | 12712 | 36.52 | 95.24 | 52.80 | 0.093 | 0.080 | 0.071 | 0.070 |
| 0.50 | offset | 4875 | 12712 | 36.97 | 96.39 | 53.44 | 0.103 | 0.090 | -0.087 | -0.090 |
| 0.50 | all | 9750 | 25424 | 36.74 | 95.82 | 53.12 | 0.098 | 0.090 | -0.008 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.13 | 16.42 | 11.30 | 11.74 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.51 | 20.79 | 15.33 | 17.49 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.95 | 16.56 | 10.03 | 11.29 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.54 | 25.03 | 17.58 | 19.63 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.69 | 24.27 | 16.17 | 16.36 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.11 | 12.71 | 9.89 | 8.97 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.76 | 27.65 | 24.82 | 24.26 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.11 | 16.56 | 10.64 | 10.72 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.87 | 16.55 | 11.98 | 12.49 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.69 | 22.57 | 17.97 | 18.45 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.21 | 22.58 | 13.63 | 17.01 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.57 | 16.83 | 12.34 | 12.91 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.14 | 16.06 | 3.85 | 3.71 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.13 | 15.29 | 2.41 | 2.81 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.28 | 18.39 | 3.27 | 4.63 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.59 | 13.54 | 1.40 | 1.40 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.35 | 14.01 | 2.29 | 2.12 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.40 | 17.51 | 3.09 | 3.14 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.98 | 15.90 | 4.14 | 4.03 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.01 | 12.81 | 1.88 | 1.89 | 2 | 2 |
