# Diarization scores: A-fa-r75b_s1500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b_s1500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s1500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T02:40:16+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b_s1500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7932-epoch=5.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.09 | 16.53 | 0.99 | 0.57 | 18.78 | 100.00 | 0.00 |
| 0.25 | 10.17 | 9.72 | 0.28 | 0.17 | 11.96 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.90 (IoU 89.89) | 9.06 (IoU 9.09) |
| silence | 0.27 (IoU 0.29) | 7.77 (IoU 45.46) |

Speech P/R/F1: 99.68 / 90.15 / 94.67; miss 9.85 of ref speech, FA 3.30 of ref silence, SAD error 10.14.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12788 | 35.40 | 92.86 | 51.26 | 0.087 | 0.080 | 0.069 | 0.070 |
| 0.25 | offset | 4875 | 12788 | 35.13 | 92.14 | 50.86 | 0.089 | 0.080 | -0.075 | -0.080 |
| 0.25 | all | 9750 | 25576 | 35.26 | 92.50 | 51.06 | 0.088 | 0.080 | -0.003 | -0.000 |
| 0.50 | onset | 4875 | 12788 | 36.40 | 95.49 | 52.71 | 0.094 | 0.090 | 0.074 | 0.080 |
| 0.50 | offset | 4875 | 12788 | 36.79 | 96.51 | 53.28 | 0.099 | 0.090 | -0.082 | -0.080 |
| 0.50 | all | 9750 | 25576 | 36.60 | 96.00 | 52.99 | 0.097 | 0.090 | -0.005 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.27 | 16.54 | 11.36 | 11.81 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.67 | 20.99 | 15.41 | 17.58 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.06 | 16.74 | 10.10 | 11.39 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.92 | 25.50 | 17.94 | 20.08 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.77 | 24.33 | 16.31 | 16.47 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.13 | 12.77 | 9.90 | 9.02 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.19 | 28.10 | 25.22 | 24.67 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.26 | 16.76 | 10.79 | 10.93 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.09 | 16.82 | 12.13 | 12.67 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.67 | 22.47 | 17.98 | 18.38 | 3 | 3 |
| R8008_M8016__far_ch1 | 18.99 | 22.31 | 13.48 | 16.83 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.53 | 16.83 | 12.34 | 12.97 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.20 | 16.12 | 3.97 | 3.82 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.91 | 15.06 | 2.32 | 2.73 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.01 | 18.16 | 3.14 | 4.45 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.59 | 13.53 | 1.52 | 1.52 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.16 | 13.83 | 2.30 | 2.12 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.25 | 17.36 | 3.01 | 3.05 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.76 | 15.66 | 4.07 | 3.94 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.90 | 12.69 | 1.90 | 1.90 | 2 | 2 |
