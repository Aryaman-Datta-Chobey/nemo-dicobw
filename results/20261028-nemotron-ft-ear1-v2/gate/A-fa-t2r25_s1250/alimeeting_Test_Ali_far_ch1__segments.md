# Diarization scores: A-fa-t2r25_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r25_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T12:27:25+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r25_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7843-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.16 | 16.53 | 1.05 | 0.58 | 18.86 | 95.00 | 0.05 |
| 0.25 | 10.24 | 9.76 | 0.31 | 0.17 | 11.97 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.80 (IoU 89.76) | 9.16 (IoU 9.19) |
| silence | 0.29 (IoU 0.32) | 7.75 (IoU 45.06) |

Speech P/R/F1: 99.65 / 90.04 / 94.60; miss 9.96 of ref speech, FA 3.59 of ref silence, SAD error 10.28.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12733 | 35.09 | 91.65 | 50.75 | 0.087 | 0.080 | 0.067 | 0.070 |
| 0.25 | offset | 4875 | 12733 | 34.78 | 90.85 | 50.31 | 0.091 | 0.090 | -0.074 | -0.080 |
| 0.25 | all | 9750 | 25466 | 34.94 | 91.25 | 50.53 | 0.089 | 0.080 | -0.003 | 0.000 |
| 0.50 | onset | 4875 | 12733 | 36.11 | 94.32 | 52.23 | 0.094 | 0.090 | 0.072 | 0.080 |
| 0.50 | offset | 4875 | 12733 | 36.61 | 95.63 | 52.95 | 0.102 | 0.090 | -0.083 | -0.090 |
| 0.50 | all | 9750 | 25466 | 36.36 | 94.97 | 52.59 | 0.098 | 0.090 | -0.006 | -0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.33 | 16.63 | 11.23 | 11.69 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.54 | 20.92 | 15.20 | 17.35 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.99 | 16.67 | 10.08 | 11.33 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.30 | 24.82 | 17.41 | 19.45 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.45 | 24.06 | 16.13 | 16.32 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.93 | 12.56 | 9.78 | 8.90 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.98 | 27.87 | 24.97 | 24.38 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.21 | 16.66 | 10.68 | 10.81 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.09 | 16.84 | 12.16 | 12.72 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.10 | 22.96 | 18.29 | 18.72 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.45 | 22.89 | 13.59 | 16.97 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.76 | 17.05 | 12.50 | 13.10 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.78 | 16.68 | 4.38 | 4.21 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.95 | 15.04 | 2.52 | 2.87 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.43 | 18.57 | 3.37 | 4.76 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.05 | 13.94 | 1.80 | 1.76 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.34 | 14.08 | 2.42 | 2.30 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.60 | 17.70 | 3.21 | 3.25 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.41 | 16.36 | 4.70 | 4.61 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.62 | 13.32 | 2.54 | 2.49 | 2 | 3 |
