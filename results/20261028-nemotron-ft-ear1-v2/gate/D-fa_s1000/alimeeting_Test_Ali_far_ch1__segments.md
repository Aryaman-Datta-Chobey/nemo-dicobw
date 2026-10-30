# Diarization scores: D-fa_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `D-fa_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-fa_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T00:22:32+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `D-fa_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7747-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 19.99 | 19.08 | 0.55 | 0.36 | 20.76 | 100.00 | 0.00 |
| 0.25 | 11.28 | 11.04 | 0.15 | 0.09 | 13.38 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.68 (IoU 89.68) | 9.28 (IoU 9.30) |
| silence | 0.23 (IoU 0.26) | 7.81 (IoU 45.08) |

Speech P/R/F1: 99.72 / 89.91 / 94.56; miss 10.09 of ref speech, FA 2.90 of ref silence, SAD error 10.34.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13427 | 34.02 | 93.70 | 49.92 | 0.079 | 0.070 | 0.060 | 0.070 |
| 0.25 | offset | 4875 | 13427 | 33.71 | 92.84 | 49.46 | 0.090 | 0.080 | -0.081 | -0.080 |
| 0.25 | all | 9750 | 26854 | 33.86 | 93.27 | 49.69 | 0.085 | 0.080 | -0.010 | -0.010 |
| 0.50 | onset | 4875 | 13427 | 34.83 | 95.94 | 51.11 | 0.086 | 0.080 | 0.065 | 0.070 |
| 0.50 | offset | 4875 | 13427 | 35.22 | 97.01 | 51.68 | 0.100 | 0.090 | -0.089 | -0.090 |
| 0.50 | all | 9750 | 26854 | 35.03 | 96.47 | 51.39 | 0.093 | 0.080 | -0.012 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 18.57 | 18.90 | 12.61 | 13.14 | 4 | 4 |
| R8002_M8003__far_ch1 | 22.51 | 24.22 | 16.69 | 19.28 | 4 | 4 |
| R8004_M8005__far_ch1 | 17.28 | 19.27 | 11.21 | 12.78 | 4 | 4 |
| R8004_M8006__far_ch1 | 28.94 | 31.57 | 23.24 | 25.45 | 4 | 4 |
| R8005_M8007__far_ch1 | 27.96 | 28.36 | 19.33 | 19.41 | 4 | 4 |
| R8005_M8008__far_ch1 | 15.48 | 15.11 | 11.18 | 10.46 | 4 | 4 |
| R8005_M8009__far_ch1 | 34.09 | 33.28 | 30.33 | 29.15 | 4 | 4 |
| R8006_M8012__far_ch1 | 18.68 | 19.15 | 12.26 | 12.59 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.70 | 17.55 | 12.24 | 12.88 | 3 | 3 |
| R8008_M8015__far_ch1 | 23.17 | 23.97 | 18.77 | 19.16 | 3 | 3 |
| R8008_M8016__far_ch1 | 20.40 | 24.16 | 14.20 | 17.96 | 3 | 3 |
| R8008_M8017__far_ch1 | 16.06 | 17.43 | 12.47 | 13.14 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.45 | 15.37 | 3.63 | 3.49 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.71 | 14.90 | 2.25 | 2.64 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.99 | 17.23 | 2.74 | 3.94 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.01 | 12.92 | 1.26 | 1.25 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.89 | 13.81 | 2.20 | 2.18 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.66 | 16.79 | 3.00 | 3.07 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.02 | 14.98 | 3.79 | 3.69 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.70 | 12.49 | 1.84 | 1.84 | 2 | 2 |
