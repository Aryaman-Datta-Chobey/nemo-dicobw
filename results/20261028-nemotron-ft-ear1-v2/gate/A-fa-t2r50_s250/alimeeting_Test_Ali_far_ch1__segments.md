# Diarization scores: A-fa-t2r50_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r50_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T12:54:06+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r50_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7774-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.21 | 16.50 | 1.19 | 0.52 | 18.78 | 100.00 | 0.00 |
| 0.25 | 10.36 | 9.62 | 0.59 | 0.15 | 11.97 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.92 (IoU 89.92) | 9.04 (IoU 9.07) |
| silence | 0.25 (IoU 0.28) | 7.79 (IoU 45.59) |

Speech P/R/F1: 99.70 / 90.17 / 94.69; miss 9.83 of ref speech, FA 3.13 of ref silence, SAD error 10.11.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12796 | 35.35 | 92.80 | 51.20 | 0.087 | 0.080 | 0.070 | 0.080 |
| 0.25 | offset | 4875 | 12796 | 35.39 | 92.88 | 51.25 | 0.087 | 0.080 | -0.075 | -0.080 |
| 0.25 | all | 9750 | 25592 | 35.37 | 92.84 | 51.23 | 0.087 | 0.080 | -0.002 | 0.000 |
| 0.50 | onset | 4875 | 12796 | 36.38 | 95.49 | 52.69 | 0.095 | 0.090 | 0.075 | 0.080 |
| 0.50 | offset | 4875 | 12796 | 36.80 | 96.59 | 53.30 | 0.096 | 0.080 | -0.081 | -0.080 |
| 0.50 | all | 9750 | 25592 | 36.59 | 96.04 | 52.99 | 0.095 | 0.090 | -0.003 | -0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.47 | 16.72 | 11.42 | 11.87 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.99 | 21.20 | 15.56 | 17.68 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.95 | 16.58 | 9.98 | 11.23 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.37 | 24.95 | 17.32 | 19.41 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.08 | 24.61 | 16.29 | 16.45 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.29 | 12.92 | 9.94 | 9.02 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.93 | 27.77 | 24.89 | 24.32 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.20 | 16.60 | 10.58 | 10.67 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.75 | 16.37 | 11.73 | 12.14 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.48 | 22.04 | 17.77 | 18.03 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.27 | 22.60 | 13.56 | 16.93 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.35 | 16.61 | 12.18 | 12.75 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.88 | 15.82 | 3.74 | 3.60 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.49 | 14.56 | 2.18 | 2.52 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.67 | 17.59 | 2.99 | 3.97 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.25 | 13.20 | 1.32 | 1.33 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.34 | 14.02 | 2.48 | 2.32 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.23 | 17.38 | 3.16 | 3.25 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.69 | 15.62 | 3.98 | 3.88 | 2 | 2 |
| R8009_M8028__far_ch1 | 17.92 | 16.20 | 8.27 | 7.06 | 2 | 2 |
