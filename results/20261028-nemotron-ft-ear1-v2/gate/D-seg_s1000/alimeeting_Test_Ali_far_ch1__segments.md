# Diarization scores: D-seg_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `D-seg_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-seg_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T19:04:34+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `D-seg_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7988-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 15.43 | 13.45 | 1.38 | 0.60 | 16.58 | 100.00 | 0.00 |
| 0.25 | 8.54 | 8.07 | 0.31 | 0.16 | 10.56 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 86.85 (IoU 93.66) | 5.11 (IoU 5.15) |
| silence | 0.77 (IoU 0.82) | 7.27 (IoU 55.26) |

Speech P/R/F1: 99.12 / 94.44 / 96.72; miss 5.56 of ref speech, FA 9.62 of ref silence, SAD error 6.40.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11899 | 39.22 | 95.73 | 55.65 | 0.063 | 0.050 | -0.001 | 0.000 |
| 0.25 | offset | 4875 | 11900 | 39.03 | 95.26 | 55.37 | 0.062 | 0.050 | -0.018 | -0.020 |
| 0.25 | all | 9750 | 23799 | 39.12 | 95.50 | 55.51 | 0.062 | 0.050 | -0.010 | -0.010 |
| 0.50 | onset | 4875 | 11899 | 39.61 | 96.68 | 56.19 | 0.065 | 0.050 | -0.001 | 0.000 |
| 0.50 | offset | 4875 | 11900 | 39.72 | 96.96 | 56.36 | 0.067 | 0.050 | -0.020 | -0.020 |
| 0.50 | all | 9750 | 23799 | 39.67 | 96.82 | 56.28 | 0.066 | 0.050 | -0.010 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 15.35 | 15.73 | 10.10 | 10.66 | 4 | 4 |
| R8002_M8003__far_ch1 | 18.27 | 19.87 | 12.99 | 15.59 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.44 | 16.50 | 8.72 | 10.34 | 4 | 4 |
| R8004_M8006__far_ch1 | 24.05 | 27.10 | 18.49 | 21.09 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.20 | 24.85 | 15.83 | 16.04 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.47 | 12.44 | 8.14 | 7.80 | 4 | 4 |
| R8005_M8009__far_ch1 | 29.56 | 29.04 | 26.26 | 25.27 | 4 | 4 |
| R8006_M8012__far_ch1 | 15.75 | 16.48 | 9.47 | 9.99 | 4 | 4 |
| R8008_M8014__far_ch1 | 12.93 | 14.09 | 8.88 | 9.84 | 3 | 3 |
| R8008_M8015__far_ch1 | 19.52 | 21.06 | 15.09 | 15.90 | 3 | 3 |
| R8008_M8016__far_ch1 | 15.43 | 19.08 | 10.01 | 13.73 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.79 | 14.25 | 8.87 | 9.77 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.97 | 8.91 | 2.11 | 2.03 | 2 | 2 |
| R8009_M8022__far_ch1 | 8.32 | 9.18 | 0.93 | 1.24 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.39 | 11.33 | 0.98 | 1.56 | 2 | 2 |
| R8009_M8024__far_ch1 | 7.27 | 7.09 | 0.60 | 0.61 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.98 | 8.28 | 0.54 | 0.53 | 2 | 2 |
| R8009_M8026__far_ch1 | 10.26 | 10.33 | 1.20 | 1.23 | 2 | 2 |
| R8009_M8027__far_ch1 | 8.16 | 8.23 | 1.52 | 1.48 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.32 | 7.13 | 0.75 | 0.74 | 2 | 2 |
