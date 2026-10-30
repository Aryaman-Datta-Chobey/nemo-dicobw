# Diarization scores: A-fa-r75a_s2250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a_s2250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s2250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T00:48:44+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a_s2250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7898-epoch=8.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.06 | 16.47 | 1.02 | 0.57 | 18.77 | 100.00 | 0.00 |
| 0.25 | 10.14 | 9.68 | 0.29 | 0.17 | 11.91 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.86 (IoU 89.85) | 9.10 (IoU 9.12) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 45.39) |

Speech P/R/F1: 99.68 / 90.11 / 94.65; miss 9.89 of ref speech, FA 3.27 of ref silence, SAD error 10.18.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12779 | 35.31 | 92.55 | 51.12 | 0.087 | 0.080 | 0.068 | 0.070 |
| 0.25 | offset | 4875 | 12779 | 35.00 | 91.75 | 50.67 | 0.089 | 0.080 | -0.076 | -0.080 |
| 0.25 | all | 9750 | 25558 | 35.16 | 92.15 | 50.89 | 0.088 | 0.080 | -0.004 | -0.010 |
| 0.50 | onset | 4875 | 12779 | 36.36 | 95.32 | 52.65 | 0.094 | 0.090 | 0.073 | 0.080 |
| 0.50 | offset | 4875 | 12779 | 36.76 | 96.37 | 53.22 | 0.100 | 0.090 | -0.084 | -0.090 |
| 0.50 | all | 9750 | 25558 | 36.56 | 95.85 | 52.93 | 0.097 | 0.090 | -0.006 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.19 | 16.46 | 11.42 | 11.88 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.59 | 20.91 | 15.38 | 17.56 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.09 | 16.76 | 10.09 | 11.37 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.74 | 25.35 | 17.72 | 19.77 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.71 | 24.26 | 16.17 | 16.34 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.19 | 12.81 | 10.01 | 9.09 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.93 | 27.87 | 24.97 | 24.43 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.19 | 16.67 | 10.71 | 10.82 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.95 | 16.68 | 12.05 | 12.56 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.76 | 22.67 | 17.99 | 18.45 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.08 | 22.45 | 13.47 | 16.82 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.65 | 16.97 | 12.40 | 13.03 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.15 | 16.06 | 3.90 | 3.75 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.02 | 15.22 | 2.39 | 2.82 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.01 | 18.16 | 3.13 | 4.43 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.54 | 13.47 | 1.38 | 1.37 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.36 | 14.15 | 2.29 | 2.21 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.09 | 17.17 | 2.86 | 2.88 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.75 | 15.66 | 4.04 | 3.92 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.20 | 12.94 | 2.16 | 2.14 | 2 | 2 |
