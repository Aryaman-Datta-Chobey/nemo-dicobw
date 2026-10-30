# Diarization scores: A-fa-t2r25-seed43_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r25-seed43_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25-seed43_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T20:19:06+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r25-seed43_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7775-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.98 | 16.27 | 1.12 | 0.60 | 18.67 | 95.00 | 0.05 |
| 0.25 | 10.18 | 9.64 | 0.36 | 0.19 | 11.93 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.91 (IoU 89.88) | 9.05 (IoU 9.07) |
| silence | 0.29 (IoU 0.32) | 7.75 (IoU 45.34) |

Speech P/R/F1: 99.65 / 90.16 / 94.67; miss 9.84 of ref speech, FA 3.63 of ref silence, SAD error 10.16.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12723 | 35.18 | 91.82 | 50.87 | 0.086 | 0.080 | 0.067 | 0.070 |
| 0.25 | offset | 4875 | 12723 | 35.02 | 91.38 | 50.63 | 0.089 | 0.080 | -0.073 | -0.080 |
| 0.25 | all | 9750 | 25446 | 35.10 | 91.60 | 50.75 | 0.087 | 0.080 | -0.003 | 0.000 |
| 0.50 | onset | 4875 | 12723 | 36.21 | 94.50 | 52.36 | 0.093 | 0.080 | 0.071 | 0.070 |
| 0.50 | offset | 4875 | 12723 | 36.69 | 95.75 | 53.05 | 0.100 | 0.090 | -0.080 | -0.080 |
| 0.50 | all | 9750 | 25446 | 36.45 | 95.13 | 52.70 | 0.096 | 0.090 | -0.005 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.20 | 16.49 | 11.14 | 11.60 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.07 | 21.43 | 15.97 | 18.17 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.84 | 16.47 | 10.04 | 11.27 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.84 | 24.42 | 17.02 | 19.18 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.19 | 23.87 | 16.02 | 16.29 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.82 | 12.45 | 9.70 | 8.85 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.75 | 27.64 | 24.82 | 24.23 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.29 | 16.70 | 10.80 | 10.88 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.02 | 16.75 | 12.10 | 12.66 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.83 | 22.56 | 18.13 | 18.51 | 3 | 3 |
| R8008_M8016__far_ch1 | 18.98 | 22.31 | 13.40 | 16.75 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.53 | 16.84 | 12.38 | 13.00 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.64 | 16.54 | 4.33 | 4.17 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.69 | 14.76 | 2.41 | 2.76 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.12 | 18.22 | 3.28 | 4.56 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.68 | 13.58 | 1.63 | 1.60 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.09 | 13.72 | 2.35 | 2.16 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.41 | 17.51 | 3.16 | 3.20 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.94 | 15.88 | 4.39 | 4.28 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.65 | 13.32 | 2.79 | 2.72 | 2 | 3 |
