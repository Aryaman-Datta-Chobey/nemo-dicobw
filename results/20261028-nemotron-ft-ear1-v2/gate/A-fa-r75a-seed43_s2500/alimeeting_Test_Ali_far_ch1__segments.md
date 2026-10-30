# Diarization scores: A-fa-r75a-seed43_s2500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a-seed43_s2500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s2500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T05:52:51+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a-seed43_s2500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7851-epoch=9.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.15 | 16.57 | 1.01 | 0.57 | 18.85 | 100.00 | 0.00 |
| 0.25 | 10.24 | 9.79 | 0.29 | 0.17 | 12.02 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.79 (IoU 89.77) | 9.17 (IoU 9.19) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 45.19) |

Speech P/R/F1: 99.68 / 90.03 / 94.61; miss 9.97 of ref speech, FA 3.27 of ref silence, SAD error 10.26.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12845 | 35.08 | 92.43 | 50.86 | 0.088 | 0.080 | 0.069 | 0.070 |
| 0.25 | offset | 4875 | 12845 | 34.86 | 91.86 | 50.54 | 0.088 | 0.080 | -0.075 | -0.080 |
| 0.25 | all | 9750 | 25690 | 34.97 | 92.14 | 50.70 | 0.088 | 0.080 | -0.003 | -0.010 |
| 0.50 | onset | 4875 | 12845 | 36.16 | 95.28 | 52.43 | 0.095 | 0.090 | 0.074 | 0.080 |
| 0.50 | offset | 4875 | 12845 | 36.55 | 96.31 | 52.99 | 0.099 | 0.090 | -0.083 | -0.080 |
| 0.50 | all | 9750 | 25690 | 36.36 | 95.79 | 52.71 | 0.097 | 0.090 | -0.005 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.22 | 16.48 | 11.42 | 11.87 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.51 | 20.83 | 15.35 | 17.51 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.18 | 16.86 | 10.19 | 11.50 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.87 | 25.44 | 17.93 | 20.05 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.80 | 24.36 | 16.31 | 16.45 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.27 | 12.88 | 10.06 | 9.13 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.12 | 27.97 | 25.20 | 24.55 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.28 | 16.73 | 10.82 | 10.93 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.06 | 16.84 | 12.12 | 12.68 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.95 | 22.94 | 18.14 | 18.64 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.02 | 22.40 | 13.55 | 16.99 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.65 | 16.94 | 12.42 | 13.00 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.25 | 16.16 | 4.01 | 3.86 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.06 | 15.25 | 2.41 | 2.84 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.31 | 18.37 | 3.44 | 4.65 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.81 | 13.74 | 1.64 | 1.63 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.43 | 14.19 | 2.44 | 2.33 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.22 | 17.33 | 3.02 | 3.05 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.83 | 15.74 | 4.19 | 4.06 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.09 | 12.86 | 2.09 | 2.08 | 2 | 2 |
