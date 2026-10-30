# Diarization scores: A-fa-r75a-seed43_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a-seed43_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T04:43:47+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a-seed43_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7934-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.13 | 16.54 | 1.03 | 0.56 | 18.80 | 100.00 | 0.00 |
| 0.25 | 10.22 | 9.74 | 0.32 | 0.17 | 11.97 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.81 (IoU 89.80) | 9.15 (IoU 9.17) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 45.26) |

Speech P/R/F1: 99.69 / 90.05 / 94.62; miss 9.95 of ref speech, FA 3.25 of ref silence, SAD error 10.23.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12799 | 35.16 | 92.31 | 50.92 | 0.087 | 0.080 | 0.069 | 0.080 |
| 0.25 | offset | 4875 | 12799 | 35.03 | 91.98 | 50.74 | 0.089 | 0.080 | -0.076 | -0.080 |
| 0.25 | all | 9750 | 25598 | 35.10 | 92.14 | 50.83 | 0.088 | 0.080 | -0.004 | -0.000 |
| 0.50 | onset | 4875 | 12799 | 36.24 | 95.14 | 52.48 | 0.094 | 0.090 | 0.074 | 0.080 |
| 0.50 | offset | 4875 | 12799 | 36.69 | 96.33 | 53.14 | 0.100 | 0.090 | -0.084 | -0.080 |
| 0.50 | all | 9750 | 25598 | 36.46 | 95.73 | 52.81 | 0.097 | 0.090 | -0.005 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.34 | 16.61 | 11.46 | 11.91 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.54 | 20.82 | 15.39 | 17.51 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.15 | 16.81 | 10.20 | 11.50 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.75 | 25.29 | 17.82 | 19.89 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.66 | 24.21 | 16.26 | 16.43 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.17 | 12.77 | 10.00 | 9.06 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.01 | 27.86 | 25.07 | 24.46 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.27 | 16.71 | 10.79 | 10.88 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.04 | 16.74 | 12.09 | 12.61 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.62 | 22.46 | 17.89 | 18.29 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.04 | 22.32 | 13.53 | 16.86 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.64 | 16.94 | 12.39 | 13.01 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.20 | 16.12 | 3.95 | 3.80 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.22 | 15.40 | 2.55 | 2.99 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.11 | 18.17 | 3.12 | 4.38 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.56 | 13.50 | 1.43 | 1.42 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.45 | 14.21 | 2.43 | 2.34 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.39 | 17.50 | 3.07 | 3.13 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.96 | 15.87 | 4.22 | 4.12 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.57 | 13.24 | 2.65 | 2.57 | 2 | 2 |
