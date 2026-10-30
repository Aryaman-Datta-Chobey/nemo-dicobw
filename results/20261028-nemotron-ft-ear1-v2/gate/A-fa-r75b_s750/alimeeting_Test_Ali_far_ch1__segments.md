# Diarization scores: A-fa-r75b_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T02:06:59+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7699-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.30 | 16.60 | 1.13 | 0.57 | 18.92 | 100.00 | 0.00 |
| 0.25 | 10.39 | 9.76 | 0.45 | 0.17 | 12.08 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.73 (IoU 89.71) | 9.23 (IoU 9.25) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 45.04) |

Speech P/R/F1: 99.68 / 89.96 / 94.57; miss 10.04 of ref speech, FA 3.25 of ref silence, SAD error 10.32.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12727 | 35.23 | 91.98 | 50.95 | 0.088 | 0.080 | 0.070 | 0.070 |
| 0.25 | offset | 4875 | 12727 | 35.05 | 91.51 | 50.69 | 0.090 | 0.080 | -0.077 | -0.080 |
| 0.25 | all | 9750 | 25454 | 35.14 | 91.74 | 50.82 | 0.089 | 0.080 | -0.003 | 0.000 |
| 0.50 | onset | 4875 | 12727 | 36.31 | 94.79 | 52.51 | 0.096 | 0.090 | 0.075 | 0.080 |
| 0.50 | offset | 4875 | 12727 | 36.87 | 96.27 | 53.32 | 0.102 | 0.090 | -0.085 | -0.080 |
| 0.50 | all | 9750 | 25454 | 36.59 | 95.53 | 52.91 | 0.099 | 0.090 | -0.006 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.25 | 16.53 | 11.27 | 11.73 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.67 | 21.01 | 15.39 | 17.60 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.97 | 16.60 | 10.10 | 11.40 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.54 | 25.16 | 17.56 | 19.80 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.72 | 24.28 | 16.29 | 16.45 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.98 | 12.61 | 9.83 | 8.94 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.17 | 28.02 | 25.22 | 24.63 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.29 | 16.72 | 10.78 | 10.88 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.12 | 16.83 | 12.13 | 12.63 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.72 | 22.45 | 18.00 | 18.34 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.26 | 22.56 | 13.60 | 16.91 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.54 | 16.77 | 12.36 | 12.91 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.45 | 16.36 | 4.03 | 3.88 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.26 | 15.40 | 2.48 | 2.87 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.56 | 18.83 | 3.71 | 5.16 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.87 | 13.84 | 1.76 | 1.79 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.63 | 14.37 | 2.49 | 2.40 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.84 | 17.97 | 3.22 | 3.31 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.28 | 16.22 | 4.33 | 4.24 | 2 | 2 |
| R8009_M8028__far_ch1 | 15.82 | 14.91 | 5.35 | 4.87 | 2 | 2 |
