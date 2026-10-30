# Diarization scores: A-fa-t2r50_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r50_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T13:23:14+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r50_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8010-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.23 | 16.59 | 1.08 | 0.56 | 18.89 | 95.00 | 0.05 |
| 0.25 | 10.36 | 9.80 | 0.39 | 0.17 | 12.07 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.73 (IoU 89.70) | 9.23 (IoU 9.25) |
| silence | 0.27 (IoU 0.30) | 7.77 (IoU 45.00) |

Speech P/R/F1: 99.68 / 89.96 / 94.57; miss 10.04 of ref speech, FA 3.35 of ref silence, SAD error 10.33.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12794 | 35.00 | 91.86 | 50.69 | 0.086 | 0.080 | 0.068 | 0.070 |
| 0.25 | offset | 4875 | 12794 | 34.85 | 91.47 | 50.47 | 0.090 | 0.080 | -0.076 | -0.080 |
| 0.25 | all | 9750 | 25588 | 34.93 | 91.66 | 50.58 | 0.088 | 0.080 | -0.004 | 0.000 |
| 0.50 | onset | 4875 | 12794 | 36.10 | 94.73 | 52.27 | 0.094 | 0.080 | 0.074 | 0.080 |
| 0.50 | offset | 4875 | 12794 | 36.54 | 95.90 | 52.92 | 0.101 | 0.090 | -0.084 | -0.090 |
| 0.50 | all | 9750 | 25588 | 36.32 | 95.31 | 52.59 | 0.098 | 0.090 | -0.005 | -0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.14 | 16.42 | 11.22 | 11.70 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.34 | 20.66 | 15.13 | 17.27 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.11 | 16.76 | 10.21 | 11.51 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.61 | 25.18 | 17.76 | 19.96 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.61 | 24.18 | 16.26 | 16.43 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.12 | 12.74 | 9.93 | 9.04 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.16 | 28.04 | 25.20 | 24.65 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.34 | 16.74 | 10.84 | 10.93 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.09 | 16.88 | 12.18 | 12.77 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.81 | 22.67 | 17.97 | 18.29 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.20 | 22.59 | 13.59 | 16.97 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.71 | 17.00 | 12.47 | 13.10 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.54 | 16.44 | 4.23 | 4.07 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.08 | 15.24 | 2.53 | 2.92 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.32 | 18.36 | 3.32 | 4.56 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.87 | 13.80 | 1.60 | 1.59 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.44 | 14.16 | 2.52 | 2.41 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.66 | 17.77 | 3.26 | 3.31 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.32 | 16.26 | 4.58 | 4.48 | 2 | 2 |
| R8009_M8028__far_ch1 | 15.02 | 14.38 | 4.39 | 4.11 | 2 | 3 |
