# Diarization scores: A-fa-t2r50-seed43_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r50-seed43_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50-seed43_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T20:59:19+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r50-seed43_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7756-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.06 | 16.45 | 1.08 | 0.53 | 18.71 | 100.00 | 0.00 |
| 0.25 | 10.16 | 9.58 | 0.43 | 0.15 | 11.86 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.96 (IoU 89.96) | 9.00 (IoU 9.02) |
| silence | 0.25 (IoU 0.28) | 7.79 (IoU 45.69) |

Speech P/R/F1: 99.69 / 90.21 / 94.72; miss 9.79 of ref speech, FA 3.17 of ref silence, SAD error 10.06.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12816 | 35.44 | 93.17 | 51.35 | 0.086 | 0.080 | 0.068 | 0.070 |
| 0.25 | offset | 4875 | 12816 | 35.34 | 92.90 | 51.20 | 0.089 | 0.080 | -0.077 | -0.080 |
| 0.25 | all | 9750 | 25632 | 35.39 | 93.04 | 51.27 | 0.087 | 0.080 | -0.004 | -0.000 |
| 0.50 | onset | 4875 | 12816 | 36.43 | 95.77 | 52.78 | 0.093 | 0.080 | 0.072 | 0.080 |
| 0.50 | offset | 4875 | 12816 | 36.84 | 96.84 | 53.37 | 0.099 | 0.090 | -0.083 | -0.080 |
| 0.50 | all | 9750 | 25632 | 36.63 | 96.31 | 53.08 | 0.096 | 0.090 | -0.006 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.44 | 16.69 | 11.34 | 11.79 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.06 | 21.25 | 15.59 | 17.67 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.00 | 16.65 | 10.00 | 11.23 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.38 | 24.94 | 17.37 | 19.47 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.80 | 24.33 | 16.08 | 16.20 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.17 | 12.80 | 9.87 | 8.99 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.93 | 27.79 | 24.87 | 24.32 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.21 | 16.65 | 10.66 | 10.74 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.86 | 16.50 | 11.85 | 12.29 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.63 | 22.41 | 17.92 | 18.38 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.27 | 22.63 | 13.51 | 16.88 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.42 | 16.67 | 12.24 | 12.80 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.95 | 15.89 | 3.74 | 3.61 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.42 | 14.46 | 2.14 | 2.48 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.44 | 17.36 | 2.67 | 3.68 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.15 | 13.10 | 1.20 | 1.20 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.26 | 13.90 | 2.40 | 2.22 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.12 | 17.26 | 3.07 | 3.14 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.42 | 15.32 | 3.71 | 3.59 | 2 | 2 |
| R8009_M8028__far_ch1 | 15.18 | 14.36 | 4.82 | 4.40 | 2 | 2 |
