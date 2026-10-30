# Diarization scores: A-fa-r75b_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T02:29:11+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7939-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.20 | 16.50 | 1.13 | 0.56 | 18.83 | 100.00 | 0.00 |
| 0.25 | 10.35 | 9.71 | 0.47 | 0.17 | 12.03 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.85 (IoU 89.84) | 9.11 (IoU 9.13) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 45.36) |

Speech P/R/F1: 99.69 / 90.10 / 94.65; miss 9.90 of ref speech, FA 3.25 of ref silence, SAD error 10.19.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12799 | 35.28 | 92.62 | 51.09 | 0.087 | 0.080 | 0.069 | 0.080 |
| 0.25 | offset | 4875 | 12799 | 35.03 | 91.98 | 50.74 | 0.088 | 0.080 | -0.075 | -0.080 |
| 0.25 | all | 9750 | 25598 | 35.16 | 92.30 | 50.92 | 0.088 | 0.080 | -0.003 | 0.000 |
| 0.50 | onset | 4875 | 12799 | 36.31 | 95.32 | 52.59 | 0.095 | 0.090 | 0.074 | 0.080 |
| 0.50 | offset | 4875 | 12799 | 36.73 | 96.43 | 53.20 | 0.099 | 0.090 | -0.083 | -0.080 |
| 0.50 | all | 9750 | 25598 | 36.52 | 95.88 | 52.89 | 0.097 | 0.090 | -0.005 | -0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.22 | 16.50 | 11.35 | 11.80 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.68 | 20.98 | 15.38 | 17.52 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.06 | 16.75 | 10.10 | 11.38 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.76 | 25.34 | 17.86 | 19.99 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.81 | 24.37 | 16.32 | 16.50 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.09 | 12.72 | 9.90 | 9.00 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.08 | 27.86 | 25.14 | 24.48 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.16 | 16.61 | 10.62 | 10.71 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.00 | 16.72 | 12.06 | 12.59 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.66 | 22.42 | 18.00 | 18.34 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.04 | 22.37 | 13.52 | 16.89 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.61 | 16.89 | 12.39 | 12.99 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.26 | 16.17 | 3.96 | 3.81 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.07 | 15.21 | 2.46 | 2.84 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.11 | 18.24 | 3.33 | 4.61 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.58 | 13.52 | 1.51 | 1.51 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.31 | 13.98 | 2.36 | 2.18 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.39 | 17.50 | 3.02 | 3.07 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.80 | 15.72 | 4.08 | 3.97 | 2 | 2 |
| R8009_M8028__far_ch1 | 15.67 | 14.69 | 5.51 | 4.97 | 2 | 2 |
