# Diarization scores: A-fa-t2r25-seed43_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r25-seed43_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25-seed43_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T19:54:48+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r25-seed43_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7886-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.75 | 16.01 | 1.15 | 0.58 | 18.44 | 100.00 | 0.00 |
| 0.25 | 10.02 | 9.41 | 0.42 | 0.19 | 11.76 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.21 (IoU 90.19) | 8.75 (IoU 8.78) |
| silence | 0.30 (IoU 0.33) | 7.74 (IoU 46.08) |

Speech P/R/F1: 99.64 / 90.48 / 94.84; miss 9.52 of ref speech, FA 3.75 of ref silence, SAD error 9.85.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12567 | 35.74 | 92.14 | 51.51 | 0.081 | 0.070 | 0.061 | 0.070 |
| 0.25 | offset | 4875 | 12567 | 35.59 | 91.75 | 51.29 | 0.090 | 0.080 | -0.073 | -0.080 |
| 0.25 | all | 9750 | 25134 | 35.67 | 91.95 | 51.40 | 0.085 | 0.080 | -0.006 | 0.000 |
| 0.50 | onset | 4875 | 12567 | 36.73 | 94.69 | 52.93 | 0.088 | 0.080 | 0.066 | 0.070 |
| 0.50 | offset | 4875 | 12567 | 37.29 | 96.12 | 53.73 | 0.101 | 0.090 | -0.080 | -0.080 |
| 0.50 | all | 9750 | 25134 | 37.01 | 95.41 | 53.33 | 0.094 | 0.080 | -0.008 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.39 | 16.68 | 11.14 | 11.61 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.43 | 20.78 | 15.06 | 17.22 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.79 | 16.44 | 10.02 | 11.29 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.91 | 24.57 | 17.23 | 19.63 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.06 | 23.70 | 15.96 | 16.24 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.84 | 12.46 | 9.66 | 8.80 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.86 | 27.75 | 24.91 | 24.34 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.26 | 16.72 | 10.76 | 10.88 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.72 | 16.48 | 11.76 | 12.32 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.01 | 21.66 | 17.39 | 17.66 | 3 | 3 |
| R8008_M8016__far_ch1 | 18.75 | 22.05 | 13.14 | 16.40 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.19 | 16.48 | 12.06 | 12.66 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.66 | 15.58 | 3.74 | 3.60 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.33 | 14.40 | 2.18 | 2.52 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.43 | 17.45 | 2.85 | 3.99 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.95 | 12.89 | 1.27 | 1.26 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.92 | 13.51 | 2.29 | 2.08 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.13 | 17.26 | 3.13 | 3.20 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.49 | 15.44 | 4.09 | 3.99 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.00 | 13.42 | 3.66 | 3.43 | 2 | 2 |
