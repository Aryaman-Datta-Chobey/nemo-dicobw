# Diarization scores: A-fa-r75a-seed43_s2000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a-seed43_s2000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s2000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T05:28:30+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a-seed43_s2000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7861-epoch=7.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.18 | 16.58 | 1.03 | 0.56 | 18.87 | 100.00 | 0.00 |
| 0.25 | 10.25 | 9.77 | 0.31 | 0.17 | 12.02 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.77 (IoU 89.75) | 9.19 (IoU 9.22) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 45.15) |

Speech P/R/F1: 99.69 / 90.00 / 94.60; miss 10.00 of ref speech, FA 3.22 of ref silence, SAD error 10.28.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12846 | 35.16 | 92.66 | 50.98 | 0.088 | 0.080 | 0.070 | 0.080 |
| 0.25 | offset | 4875 | 12846 | 34.84 | 91.82 | 50.52 | 0.089 | 0.080 | -0.076 | -0.080 |
| 0.25 | all | 9750 | 25692 | 35.00 | 92.24 | 50.75 | 0.088 | 0.080 | -0.003 | -0.010 |
| 0.50 | onset | 4875 | 12846 | 36.24 | 95.49 | 52.54 | 0.096 | 0.090 | 0.075 | 0.080 |
| 0.50 | offset | 4875 | 12846 | 36.64 | 96.55 | 53.12 | 0.100 | 0.090 | -0.084 | -0.080 |
| 0.50 | all | 9750 | 25692 | 36.44 | 96.02 | 52.83 | 0.098 | 0.090 | -0.005 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.21 | 16.46 | 11.39 | 11.84 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.54 | 20.85 | 15.34 | 17.47 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.18 | 16.89 | 10.19 | 11.52 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.79 | 25.28 | 17.83 | 19.90 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.76 | 24.35 | 16.28 | 16.48 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.27 | 12.86 | 10.03 | 9.09 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.17 | 28.03 | 25.24 | 24.64 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.25 | 16.69 | 10.82 | 10.92 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.09 | 16.86 | 12.17 | 12.72 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.06 | 22.93 | 18.15 | 18.54 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.16 | 22.63 | 13.56 | 17.03 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.73 | 17.06 | 12.47 | 13.10 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.30 | 16.20 | 4.01 | 3.85 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.16 | 15.37 | 2.45 | 2.90 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.35 | 18.52 | 3.54 | 4.88 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.69 | 13.61 | 1.46 | 1.45 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.22 | 13.91 | 2.29 | 2.13 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.16 | 17.26 | 2.89 | 2.92 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.88 | 15.81 | 4.15 | 4.03 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.60 | 13.25 | 2.64 | 2.56 | 2 | 2 |
