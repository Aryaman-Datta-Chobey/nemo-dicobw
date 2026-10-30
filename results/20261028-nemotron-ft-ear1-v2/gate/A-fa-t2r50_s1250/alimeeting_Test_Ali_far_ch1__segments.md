# Diarization scores: A-fa-t2r50_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r50_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T13:33:05+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r50_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7782-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.24 | 16.47 | 1.18 | 0.59 | 18.90 | 95.00 | 0.05 |
| 0.25 | 10.37 | 9.71 | 0.48 | 0.18 | 12.08 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.78 (IoU 89.75) | 9.18 (IoU 9.20) |
| silence | 0.27 (IoU 0.30) | 7.77 (IoU 45.10) |

Speech P/R/F1: 99.67 / 90.02 / 94.60; miss 9.98 of ref speech, FA 3.41 of ref silence, SAD error 10.28.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12764 | 35.27 | 92.35 | 51.05 | 0.088 | 0.080 | 0.070 | 0.070 |
| 0.25 | offset | 4875 | 12765 | 35.04 | 91.75 | 50.71 | 0.090 | 0.080 | -0.076 | -0.080 |
| 0.25 | all | 9750 | 25529 | 35.16 | 92.05 | 50.88 | 0.089 | 0.080 | -0.003 | 0.000 |
| 0.50 | onset | 4875 | 12764 | 36.31 | 95.06 | 52.54 | 0.096 | 0.090 | 0.074 | 0.080 |
| 0.50 | offset | 4875 | 12765 | 36.72 | 96.14 | 53.14 | 0.100 | 0.090 | -0.083 | -0.080 |
| 0.50 | all | 9750 | 25529 | 36.51 | 95.60 | 52.84 | 0.098 | 0.090 | -0.005 | -0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.02 | 16.29 | 11.21 | 11.67 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.62 | 21.02 | 15.37 | 17.66 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.11 | 16.79 | 10.15 | 11.45 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.42 | 25.07 | 17.53 | 19.85 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.63 | 24.24 | 16.25 | 16.45 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.08 | 12.71 | 9.88 | 8.98 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.95 | 27.85 | 24.98 | 24.42 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.26 | 16.69 | 10.78 | 10.86 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.15 | 16.90 | 12.25 | 12.81 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.79 | 22.74 | 18.02 | 18.43 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.22 | 22.62 | 13.56 | 16.94 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.70 | 17.02 | 12.46 | 13.10 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.57 | 16.47 | 4.19 | 4.03 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.00 | 15.17 | 2.38 | 2.80 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.28 | 18.36 | 3.24 | 4.53 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.88 | 13.80 | 1.55 | 1.53 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.28 | 13.95 | 2.34 | 2.17 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.55 | 17.65 | 3.10 | 3.14 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.11 | 16.05 | 4.37 | 4.26 | 2 | 2 |
| R8009_M8028__far_ch1 | 16.26 | 15.21 | 5.93 | 5.34 | 2 | 3 |
