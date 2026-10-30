# Diarization scores: A-fa-r75b_s1750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b_s1750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s1750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T02:51:19+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b_s1750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7883-epoch=6.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.29 | 16.66 | 1.05 | 0.57 | 18.96 | 100.00 | 0.00 |
| 0.25 | 10.36 | 9.84 | 0.34 | 0.18 | 12.11 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.71 (IoU 89.69) | 9.25 (IoU 9.27) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 44.99) |

Speech P/R/F1: 99.68 / 89.95 / 94.56; miss 10.05 of ref speech, FA 3.28 of ref silence, SAD error 10.34.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12826 | 35.12 | 92.41 | 50.90 | 0.086 | 0.080 | 0.067 | 0.070 |
| 0.25 | offset | 4875 | 12826 | 34.72 | 91.34 | 50.31 | 0.090 | 0.080 | -0.078 | -0.080 |
| 0.25 | all | 9750 | 25652 | 34.92 | 91.88 | 50.61 | 0.088 | 0.080 | -0.005 | -0.010 |
| 0.50 | onset | 4875 | 12826 | 36.18 | 95.20 | 52.44 | 0.094 | 0.080 | 0.072 | 0.080 |
| 0.50 | offset | 4875 | 12826 | 36.59 | 96.27 | 53.03 | 0.102 | 0.090 | -0.087 | -0.090 |
| 0.50 | all | 9750 | 25652 | 36.39 | 95.73 | 52.73 | 0.098 | 0.090 | -0.008 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.19 | 16.46 | 11.36 | 11.82 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.72 | 20.99 | 15.44 | 17.61 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.21 | 16.91 | 10.13 | 11.44 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.85 | 25.37 | 17.94 | 20.05 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.88 | 24.48 | 16.37 | 16.58 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.24 | 12.85 | 10.00 | 9.08 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.30 | 28.11 | 25.35 | 24.74 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.30 | 16.74 | 10.86 | 10.95 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.16 | 16.96 | 12.21 | 12.78 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.99 | 22.88 | 18.18 | 18.63 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.25 | 22.60 | 13.71 | 17.09 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.75 | 17.05 | 12.50 | 13.13 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.55 | 16.46 | 4.15 | 3.99 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.20 | 15.38 | 2.54 | 2.94 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.32 | 18.49 | 3.55 | 4.88 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.11 | 14.06 | 1.97 | 1.98 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.45 | 14.20 | 2.43 | 2.29 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.52 | 17.63 | 3.10 | 3.15 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.09 | 16.00 | 4.33 | 4.20 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.95 | 13.51 | 3.13 | 3.00 | 2 | 2 |
