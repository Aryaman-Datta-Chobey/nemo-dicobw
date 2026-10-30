# Diarization scores: A-fa-r75b_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T01:56:05+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7774-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.19 | 16.62 | 1.03 | 0.55 | 18.83 | 100.00 | 0.00 |
| 0.25 | 10.22 | 9.72 | 0.33 | 0.16 | 11.95 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.75 (IoU 89.74) | 9.21 (IoU 9.23) |
| silence | 0.25 (IoU 0.28) | 7.79 (IoU 45.15) |

Speech P/R/F1: 99.69 / 89.99 / 94.59; miss 10.01 of ref speech, FA 3.16 of ref silence, SAD error 10.29.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12695 | 35.48 | 92.39 | 51.27 | 0.082 | 0.080 | 0.064 | 0.070 |
| 0.25 | offset | 4875 | 12695 | 35.08 | 91.36 | 50.70 | 0.095 | 0.090 | -0.083 | -0.090 |
| 0.25 | all | 9750 | 25390 | 35.28 | 91.88 | 50.98 | 0.089 | 0.080 | -0.009 | -0.000 |
| 0.50 | onset | 4875 | 12695 | 36.52 | 95.10 | 52.77 | 0.090 | 0.080 | 0.070 | 0.070 |
| 0.50 | offset | 4875 | 12695 | 36.98 | 96.31 | 53.44 | 0.107 | 0.100 | -0.092 | -0.090 |
| 0.50 | all | 9750 | 25390 | 36.75 | 95.70 | 53.11 | 0.098 | 0.090 | -0.012 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.40 | 16.65 | 11.34 | 11.78 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.74 | 21.00 | 15.45 | 17.58 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.97 | 16.62 | 10.05 | 11.32 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.53 | 25.03 | 17.64 | 19.82 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.76 | 24.31 | 16.29 | 16.45 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.05 | 12.66 | 9.86 | 8.97 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.10 | 27.92 | 25.14 | 24.52 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.25 | 16.67 | 10.71 | 10.79 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.10 | 16.85 | 12.03 | 12.56 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.58 | 22.21 | 17.84 | 18.09 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.26 | 22.63 | 13.66 | 17.06 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.63 | 16.94 | 12.40 | 13.03 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.28 | 16.20 | 3.86 | 3.72 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.35 | 15.50 | 2.57 | 2.97 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.09 | 18.12 | 3.08 | 4.32 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.74 | 13.70 | 1.46 | 1.47 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.57 | 14.24 | 2.44 | 2.28 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.64 | 17.75 | 3.13 | 3.19 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.24 | 16.17 | 4.31 | 4.21 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.01 | 13.61 | 3.05 | 2.93 | 2 | 2 |
