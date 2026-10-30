# Diarization scores: A-fa-r75a-seed43_s1500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a-seed43_s1500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s1500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T05:06:13+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a-seed43_s1500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7943-epoch=5.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.21 | 16.60 | 1.03 | 0.58 | 18.89 | 100.00 | 0.00 |
| 0.25 | 10.30 | 9.78 | 0.32 | 0.20 | 12.07 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.78 (IoU 89.77) | 9.18 (IoU 9.20) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 45.19) |

Speech P/R/F1: 99.69 / 90.02 / 94.61; miss 9.98 of ref speech, FA 3.25 of ref silence, SAD error 10.26.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12822 | 34.99 | 92.02 | 50.70 | 0.089 | 0.090 | 0.071 | 0.080 |
| 0.25 | offset | 4875 | 12822 | 34.95 | 91.92 | 50.64 | 0.087 | 0.080 | -0.074 | -0.080 |
| 0.25 | all | 9750 | 25644 | 34.97 | 91.97 | 50.67 | 0.088 | 0.080 | -0.001 | 0.000 |
| 0.50 | onset | 4875 | 12822 | 36.13 | 95.04 | 52.36 | 0.097 | 0.090 | 0.077 | 0.080 |
| 0.50 | offset | 4875 | 12822 | 36.56 | 96.16 | 52.98 | 0.098 | 0.090 | -0.081 | -0.080 |
| 0.50 | all | 9750 | 25644 | 36.35 | 95.60 | 52.67 | 0.097 | 0.090 | -0.003 | -0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.26 | 16.54 | 11.37 | 11.82 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.67 | 20.98 | 15.45 | 17.65 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.07 | 16.70 | 10.13 | 11.43 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.83 | 25.43 | 17.95 | 20.15 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.74 | 24.29 | 16.32 | 16.48 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.19 | 12.78 | 9.98 | 9.04 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.12 | 27.97 | 25.18 | 24.57 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.27 | 16.65 | 10.77 | 10.83 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.00 | 16.74 | 12.07 | 12.60 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.90 | 22.81 | 18.10 | 18.54 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.20 | 22.59 | 13.55 | 16.96 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.68 | 16.99 | 12.42 | 13.04 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.35 | 16.27 | 4.05 | 3.90 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.21 | 15.42 | 2.52 | 3.00 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.09 | 18.02 | 3.15 | 4.21 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.69 | 13.63 | 1.48 | 1.48 | 2 | 2 |
| R8009_M8025__far_ch1 | 15.37 | 15.74 | 3.57 | 4.41 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.32 | 17.43 | 3.08 | 3.13 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.89 | 15.82 | 4.19 | 4.08 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.39 | 13.11 | 2.39 | 2.35 | 2 | 2 |
