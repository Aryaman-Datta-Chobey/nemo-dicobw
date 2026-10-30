# Diarization scores: A-fa-t2r50-seed43_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r50-seed43_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50-seed43_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T21:32:20+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r50-seed43_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7905-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.31 | 16.64 | 1.11 | 0.56 | 18.94 | 95.00 | 0.05 |
| 0.25 | 10.39 | 9.79 | 0.43 | 0.17 | 12.08 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.71 (IoU 89.68) | 9.25 (IoU 9.28) |
| silence | 0.27 (IoU 0.29) | 7.77 (IoU 44.95) |

Speech P/R/F1: 99.68 / 89.94 / 94.56; miss 10.06 of ref speech, FA 3.32 of ref silence, SAD error 10.35.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12767 | 34.98 | 91.61 | 50.63 | 0.087 | 0.080 | 0.069 | 0.070 |
| 0.25 | offset | 4875 | 12767 | 34.91 | 91.43 | 50.53 | 0.091 | 0.080 | -0.077 | -0.080 |
| 0.25 | all | 9750 | 25534 | 34.95 | 91.52 | 50.58 | 0.089 | 0.080 | -0.004 | -0.010 |
| 0.50 | onset | 4875 | 12767 | 36.16 | 94.69 | 52.33 | 0.096 | 0.090 | 0.074 | 0.080 |
| 0.50 | offset | 4875 | 12767 | 36.66 | 96.02 | 53.07 | 0.102 | 0.090 | -0.086 | -0.090 |
| 0.50 | all | 9750 | 25534 | 36.41 | 95.35 | 52.70 | 0.099 | 0.090 | -0.006 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.25 | 16.54 | 11.29 | 11.77 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.56 | 20.87 | 15.34 | 17.49 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.08 | 16.71 | 10.14 | 11.40 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.44 | 24.99 | 17.52 | 19.64 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.73 | 24.37 | 16.30 | 16.55 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.05 | 12.67 | 9.88 | 9.00 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.05 | 27.91 | 25.06 | 24.45 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.28 | 16.72 | 10.74 | 10.86 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.05 | 16.76 | 12.13 | 12.64 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.72 | 22.49 | 17.96 | 18.27 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.17 | 22.48 | 13.62 | 16.96 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.77 | 17.06 | 12.52 | 13.13 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.72 | 16.63 | 4.22 | 4.06 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.21 | 15.37 | 2.53 | 2.92 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.63 | 18.71 | 3.40 | 4.77 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.95 | 13.90 | 1.58 | 1.57 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.80 | 14.53 | 2.69 | 2.58 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.73 | 17.83 | 3.28 | 3.33 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.42 | 16.35 | 4.47 | 4.38 | 2 | 2 |
| R8009_M8028__far_ch1 | 15.87 | 14.99 | 5.36 | 4.90 | 2 | 3 |
