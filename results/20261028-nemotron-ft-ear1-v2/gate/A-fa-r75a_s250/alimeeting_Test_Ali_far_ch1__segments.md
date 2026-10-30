# Diarization scores: A-fa-r75a_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T23:19:21+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7686-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.21 | 16.61 | 1.06 | 0.54 | 18.85 | 100.00 | 0.00 |
| 0.25 | 10.29 | 9.74 | 0.40 | 0.16 | 12.00 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.73 (IoU 89.72) | 9.23 (IoU 9.25) |
| silence | 0.24 (IoU 0.27) | 7.80 (IoU 45.14) |

Speech P/R/F1: 99.71 / 89.96 / 94.58; miss 10.04 of ref speech, FA 3.03 of ref silence, SAD error 10.30.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12883 | 35.16 | 92.92 | 51.02 | 0.087 | 0.080 | 0.070 | 0.080 |
| 0.25 | offset | 4875 | 12883 | 34.95 | 92.37 | 50.72 | 0.090 | 0.080 | -0.079 | -0.080 |
| 0.25 | all | 9750 | 25766 | 35.06 | 92.65 | 50.87 | 0.089 | 0.080 | -0.004 | -0.010 |
| 0.50 | onset | 4875 | 12883 | 36.19 | 95.65 | 52.52 | 0.094 | 0.090 | 0.075 | 0.080 |
| 0.50 | offset | 4875 | 12883 | 36.61 | 96.76 | 53.13 | 0.101 | 0.090 | -0.086 | -0.090 |
| 0.50 | all | 9750 | 25766 | 36.40 | 96.21 | 52.82 | 0.097 | 0.090 | -0.006 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.49 | 16.73 | 11.47 | 11.93 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.16 | 21.39 | 15.71 | 17.87 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.93 | 16.56 | 10.06 | 11.31 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.49 | 25.00 | 17.54 | 19.58 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.90 | 24.45 | 16.26 | 16.45 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.22 | 12.83 | 10.00 | 9.08 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.97 | 27.81 | 24.99 | 24.39 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.32 | 16.76 | 10.81 | 10.89 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.09 | 16.70 | 12.08 | 12.54 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.01 | 22.80 | 18.24 | 18.58 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.42 | 22.69 | 13.77 | 17.11 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.57 | 16.83 | 12.38 | 12.96 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.08 | 16.01 | 3.81 | 3.67 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.80 | 14.92 | 2.28 | 2.66 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.98 | 17.91 | 3.17 | 4.20 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.63 | 13.59 | 1.46 | 1.48 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.45 | 14.09 | 2.49 | 2.30 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.46 | 17.60 | 3.25 | 3.33 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.91 | 15.81 | 4.03 | 3.90 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.73 | 14.11 | 4.02 | 3.76 | 2 | 2 |
