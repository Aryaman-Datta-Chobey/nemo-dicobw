# Diarization scores: C-fa_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `C-fa_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-fa_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T22:56:56+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `C-fa_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7797-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.40 | 17.05 | 0.86 | 0.50 | 19.12 | 100.00 | 0.00 |
| 0.25 | 10.21 | 9.83 | 0.24 | 0.14 | 12.06 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.88 (IoU 89.89) | 9.08 (IoU 9.10) |
| silence | 0.24 (IoU 0.27) | 7.80 (IoU 45.53) |

Speech P/R/F1: 99.71 / 90.13 / 94.67; miss 9.87 of ref speech, FA 3.04 of ref silence, SAD error 10.14.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13051 | 35.19 | 94.22 | 51.24 | 0.090 | 0.090 | 0.073 | 0.080 |
| 0.25 | offset | 4875 | 13051 | 35.12 | 94.03 | 51.14 | 0.087 | 0.080 | -0.075 | -0.080 |
| 0.25 | all | 9750 | 26102 | 35.16 | 94.12 | 51.19 | 0.089 | 0.080 | -0.001 | 0.000 |
| 0.50 | onset | 4875 | 13051 | 36.14 | 96.76 | 52.63 | 0.096 | 0.090 | 0.078 | 0.080 |
| 0.50 | offset | 4875 | 13051 | 36.43 | 97.52 | 53.04 | 0.095 | 0.080 | -0.081 | -0.080 |
| 0.50 | all | 9750 | 26102 | 36.28 | 97.14 | 52.83 | 0.096 | 0.090 | -0.002 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.32 | 17.60 | 11.88 | 12.40 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.49 | 21.84 | 15.81 | 18.04 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.46 | 17.15 | 10.23 | 11.53 | 4 | 4 |
| R8004_M8006__far_ch1 | 23.68 | 26.31 | 18.39 | 20.46 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.87 | 25.36 | 16.85 | 16.96 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.93 | 13.50 | 10.38 | 9.50 | 4 | 4 |
| R8005_M8009__far_ch1 | 29.28 | 29.13 | 25.99 | 25.44 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.57 | 17.01 | 10.83 | 10.94 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.16 | 16.70 | 11.89 | 12.25 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.86 | 22.61 | 17.76 | 18.21 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.87 | 23.42 | 13.85 | 17.32 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.78 | 17.10 | 12.48 | 13.12 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.06 | 16.00 | 3.73 | 3.59 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.37 | 14.44 | 2.07 | 2.42 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.22 | 17.07 | 2.35 | 3.21 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.34 | 13.26 | 1.36 | 1.34 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.05 | 13.56 | 2.21 | 1.97 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.44 | 16.58 | 2.61 | 2.65 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.71 | 14.62 | 3.13 | 3.00 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.73 | 12.55 | 1.57 | 1.59 | 2 | 2 |
