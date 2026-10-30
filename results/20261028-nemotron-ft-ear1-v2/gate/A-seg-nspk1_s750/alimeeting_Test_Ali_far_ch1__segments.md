# Diarization scores: A-seg-nspk1_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-seg-nspk1_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T02:12:31+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-seg-nspk1_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8409-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.68 | 15.43 | 1.64 | 0.61 | 18.17 | 100.00 | 0.00 |
| 0.25 | 9.60 | 8.78 | 0.65 | 0.17 | 11.14 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.63 (IoU 90.43) | 8.33 (IoU 8.38) |
| silence | 0.51 (IoU 0.56) | 7.53 (IoU 45.97) |

Speech P/R/F1: 99.39 / 90.94 / 94.98; miss 9.06 of ref speech, FA 6.38 of ref silence, SAD error 9.62.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12076 | 36.39 | 90.15 | 51.86 | 0.087 | 0.080 | 0.059 | 0.070 |
| 0.25 | offset | 4875 | 12076 | 36.12 | 89.48 | 51.47 | 0.096 | 0.090 | -0.061 | -0.070 |
| 0.25 | all | 9750 | 24152 | 36.26 | 89.82 | 51.66 | 0.092 | 0.090 | -0.001 | -0.000 |
| 0.50 | onset | 4875 | 12076 | 37.44 | 92.74 | 53.34 | 0.094 | 0.080 | 0.064 | 0.070 |
| 0.50 | offset | 4875 | 12076 | 38.18 | 94.58 | 54.40 | 0.108 | 0.100 | -0.066 | -0.080 |
| 0.50 | all | 9750 | 24152 | 37.81 | 93.66 | 53.87 | 0.101 | 0.090 | -0.002 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.07 | 17.29 | 11.94 | 12.34 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.59 | 18.86 | 12.37 | 14.47 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.07 | 16.75 | 10.05 | 11.36 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.90 | 24.48 | 16.78 | 18.98 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.31 | 23.96 | 15.69 | 15.93 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.97 | 12.63 | 9.52 | 8.73 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.35 | 28.19 | 25.43 | 24.79 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.08 | 16.48 | 10.56 | 10.65 | 4 | 4 |
| R8008_M8014__far_ch1 | 14.17 | 14.85 | 10.31 | 10.78 | 3 | 3 |
| R8008_M8015__far_ch1 | 17.09 | 18.12 | 12.63 | 13.09 | 3 | 3 |
| R8008_M8016__far_ch1 | 18.05 | 21.34 | 12.17 | 15.21 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.07 | 13.09 | 7.00 | 7.55 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.70 | 16.62 | 4.19 | 4.05 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.63 | 15.76 | 2.74 | 3.14 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.07 | 18.21 | 3.59 | 4.85 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.02 | 13.93 | 1.72 | 1.72 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.93 | 14.53 | 2.90 | 2.69 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.56 | 17.69 | 3.27 | 3.36 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.54 | 14.61 | 3.72 | 3.71 | 2 | 2 |
| R8009_M8028__far_ch1 | 16.81 | 15.33 | 7.34 | 6.36 | 2 | 2 |
