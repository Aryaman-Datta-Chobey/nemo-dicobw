# Diarization scores: A-fa-r75b_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T01:45:05+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7683-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.16 | 16.58 | 1.04 | 0.54 | 18.83 | 100.00 | 0.00 |
| 0.25 | 10.21 | 9.69 | 0.36 | 0.16 | 11.96 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.75 (IoU 89.75) | 9.21 (IoU 9.23) |
| silence | 0.25 (IoU 0.27) | 7.79 (IoU 45.19) |

Speech P/R/F1: 99.70 / 89.99 / 94.60; miss 10.01 of ref speech, FA 3.06 of ref silence, SAD error 10.28.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12847 | 35.37 | 93.21 | 51.28 | 0.086 | 0.080 | 0.069 | 0.080 |
| 0.25 | offset | 4875 | 12847 | 35.00 | 92.23 | 50.74 | 0.092 | 0.090 | -0.081 | -0.080 |
| 0.25 | all | 9750 | 25694 | 35.18 | 92.72 | 51.01 | 0.089 | 0.080 | -0.006 | -0.010 |
| 0.50 | onset | 4875 | 12847 | 36.34 | 95.75 | 52.68 | 0.093 | 0.090 | 0.073 | 0.080 |
| 0.50 | offset | 4875 | 12847 | 36.74 | 96.82 | 53.27 | 0.102 | 0.090 | -0.088 | -0.090 |
| 0.50 | all | 9750 | 25694 | 36.54 | 96.29 | 52.97 | 0.098 | 0.090 | -0.008 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.50 | 16.74 | 11.47 | 11.90 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.10 | 21.36 | 15.70 | 17.90 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.94 | 16.58 | 10.04 | 11.33 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.39 | 24.97 | 17.44 | 19.63 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.83 | 24.39 | 16.20 | 16.38 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.18 | 12.80 | 9.94 | 9.03 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.83 | 27.65 | 24.86 | 24.25 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.30 | 16.72 | 10.75 | 10.81 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.08 | 16.68 | 12.04 | 12.47 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.17 | 23.09 | 18.38 | 18.84 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.39 | 22.70 | 13.76 | 17.14 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.65 | 16.89 | 12.45 | 13.02 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.16 | 16.09 | 3.81 | 3.67 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.79 | 14.89 | 2.27 | 2.64 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.70 | 17.67 | 2.80 | 3.90 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.69 | 13.65 | 1.47 | 1.49 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.55 | 14.22 | 2.46 | 2.29 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.30 | 17.45 | 3.14 | 3.21 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.77 | 15.66 | 3.88 | 3.74 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.20 | 13.71 | 3.28 | 3.12 | 2 | 2 |
