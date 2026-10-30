# Diarization scores: A-fa-t2r50-seed43_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r50-seed43_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50-seed43_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T21:43:25+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r50-seed43_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7913-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.36 | 16.57 | 1.19 | 0.60 | 19.00 | 95.00 | 0.05 |
| 0.25 | 10.53 | 9.80 | 0.52 | 0.21 | 12.20 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.73 (IoU 89.69) | 9.23 (IoU 9.26) |
| silence | 0.28 (IoU 0.30) | 7.77 (IoU 44.96) |

Speech P/R/F1: 99.67 / 89.96 / 94.57; miss 10.04 of ref speech, FA 3.42 of ref silence, SAD error 10.34.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12797 | 34.98 | 91.84 | 50.67 | 0.086 | 0.080 | 0.066 | 0.070 |
| 0.25 | offset | 4875 | 12797 | 34.77 | 91.28 | 50.36 | 0.091 | 0.090 | -0.077 | -0.080 |
| 0.25 | all | 9750 | 25594 | 34.88 | 91.56 | 50.51 | 0.088 | 0.080 | -0.005 | -0.000 |
| 0.50 | onset | 4875 | 12797 | 36.13 | 94.83 | 52.32 | 0.094 | 0.080 | 0.072 | 0.070 |
| 0.50 | offset | 4875 | 12797 | 36.55 | 95.94 | 52.93 | 0.102 | 0.090 | -0.085 | -0.090 |
| 0.50 | all | 9750 | 25594 | 36.34 | 95.38 | 52.63 | 0.098 | 0.090 | -0.007 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.20 | 16.48 | 11.26 | 11.73 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.63 | 21.04 | 15.36 | 17.60 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.06 | 16.72 | 10.13 | 11.38 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.33 | 24.85 | 17.48 | 19.59 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.50 | 24.10 | 16.10 | 16.29 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.05 | 12.66 | 9.91 | 9.02 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.99 | 27.87 | 25.08 | 24.53 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.36 | 16.83 | 10.84 | 10.98 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.07 | 16.85 | 12.16 | 12.74 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.98 | 22.82 | 18.18 | 18.54 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.29 | 22.64 | 13.66 | 17.01 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.74 | 17.05 | 12.50 | 13.13 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.76 | 16.66 | 4.34 | 4.17 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.99 | 15.13 | 2.43 | 2.83 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.71 | 18.82 | 3.69 | 5.06 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.99 | 13.93 | 1.79 | 1.77 | 2 | 2 |
| R8009_M8025__far_ch1 | 15.20 | 15.53 | 3.35 | 4.16 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.60 | 17.69 | 3.23 | 3.28 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.31 | 16.24 | 4.49 | 4.38 | 2 | 2 |
| R8009_M8028__far_ch1 | 17.05 | 15.78 | 6.84 | 6.06 | 2 | 3 |
