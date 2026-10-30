# Diarization scores: C-fa_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `C-fa_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-fa_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T23:41:04+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `C-fa_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7683-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.85 | 16.24 | 1.07 | 0.54 | 18.58 | 100.00 | 0.00 |
| 0.25 | 10.11 | 9.53 | 0.41 | 0.17 | 11.86 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.29 (IoU 90.29) | 8.67 (IoU 8.69) |
| silence | 0.29 (IoU 0.32) | 7.75 (IoU 46.37) |

Speech P/R/F1: 99.65 / 90.58 / 94.90; miss 9.42 of ref speech, FA 3.66 of ref silence, SAD error 9.74.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12651 | 35.57 | 92.31 | 51.35 | 0.080 | 0.070 | 0.062 | 0.070 |
| 0.25 | offset | 4875 | 12651 | 35.44 | 91.98 | 51.17 | 0.085 | 0.080 | -0.067 | -0.070 |
| 0.25 | all | 9750 | 25302 | 35.51 | 92.14 | 51.26 | 0.083 | 0.070 | -0.002 | 0.000 |
| 0.50 | onset | 4875 | 12651 | 36.63 | 95.06 | 52.88 | 0.088 | 0.080 | 0.068 | 0.070 |
| 0.50 | offset | 4875 | 12651 | 37.10 | 96.27 | 53.55 | 0.096 | 0.080 | -0.074 | -0.070 |
| 0.50 | all | 9750 | 25302 | 36.86 | 95.66 | 53.22 | 0.092 | 0.080 | -0.004 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.97 | 17.30 | 11.41 | 11.90 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.56 | 21.00 | 15.16 | 17.43 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.73 | 16.41 | 9.97 | 11.27 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.33 | 24.94 | 17.51 | 19.62 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.40 | 23.99 | 16.28 | 16.50 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.03 | 12.67 | 9.71 | 8.89 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.61 | 28.49 | 25.57 | 25.04 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.52 | 16.91 | 10.86 | 10.90 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.00 | 16.78 | 11.86 | 12.43 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.81 | 22.68 | 17.79 | 18.11 | 3 | 3 |
| R8008_M8016__far_ch1 | 18.94 | 22.38 | 13.18 | 16.56 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.15 | 16.51 | 11.97 | 12.64 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.09 | 15.01 | 3.51 | 3.37 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.05 | 14.15 | 2.03 | 2.40 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.78 | 16.74 | 2.55 | 3.45 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.27 | 12.20 | 1.00 | 1.00 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.66 | 13.19 | 2.22 | 2.00 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.72 | 16.86 | 3.10 | 3.17 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.08 | 15.06 | 4.03 | 3.94 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.99 | 13.32 | 4.05 | 3.75 | 2 | 2 |
