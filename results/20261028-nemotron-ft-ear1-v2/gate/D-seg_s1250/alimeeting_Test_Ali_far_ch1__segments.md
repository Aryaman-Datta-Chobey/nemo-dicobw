# Diarization scores: D-seg_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `D-seg_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-seg_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T19:13:58+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `D-seg_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8106-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 15.16 | 13.08 | 1.47 | 0.61 | 16.29 | 100.00 | 0.00 |
| 0.25 | 8.36 | 7.87 | 0.33 | 0.16 | 10.36 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 87.08 (IoU 93.85) | 4.88 (IoU 4.92) |
| silence | 0.83 (IoU 0.87) | 7.21 (IoU 55.81) |

Speech P/R/F1: 99.06 / 94.69 / 96.83; miss 5.31 of ref speech, FA 10.31 of ref silence, SAD error 6.21.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11683 | 39.79 | 95.36 | 56.15 | 0.063 | 0.050 | -0.004 | 0.000 |
| 0.25 | offset | 4875 | 11684 | 39.57 | 94.83 | 55.84 | 0.062 | 0.050 | -0.015 | -0.010 |
| 0.25 | all | 9750 | 23367 | 39.68 | 95.10 | 56.00 | 0.063 | 0.050 | -0.009 | -0.010 |
| 0.50 | onset | 4875 | 11683 | 40.22 | 96.39 | 56.76 | 0.066 | 0.050 | -0.004 | 0.000 |
| 0.50 | offset | 4875 | 11684 | 40.27 | 96.51 | 56.83 | 0.067 | 0.050 | -0.015 | -0.010 |
| 0.50 | all | 9750 | 23367 | 40.24 | 96.45 | 56.79 | 0.066 | 0.050 | -0.009 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 15.29 | 15.75 | 10.02 | 10.62 | 4 | 4 |
| R8002_M8003__far_ch1 | 18.11 | 19.66 | 12.92 | 15.52 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.13 | 16.17 | 8.52 | 10.16 | 4 | 4 |
| R8004_M8006__far_ch1 | 23.57 | 26.62 | 17.97 | 20.62 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.86 | 24.55 | 15.64 | 15.87 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.30 | 12.25 | 7.92 | 7.60 | 4 | 4 |
| R8005_M8009__far_ch1 | 29.00 | 28.49 | 25.81 | 24.77 | 4 | 4 |
| R8006_M8012__far_ch1 | 15.54 | 16.26 | 9.19 | 9.72 | 4 | 4 |
| R8008_M8014__far_ch1 | 12.75 | 13.81 | 8.63 | 9.54 | 3 | 3 |
| R8008_M8015__far_ch1 | 18.99 | 20.27 | 14.71 | 15.36 | 3 | 3 |
| R8008_M8016__far_ch1 | 15.23 | 18.84 | 9.81 | 13.47 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.59 | 14.00 | 8.62 | 9.49 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.79 | 8.73 | 2.05 | 1.97 | 2 | 2 |
| R8009_M8022__far_ch1 | 8.10 | 8.94 | 0.91 | 1.21 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.20 | 11.18 | 0.97 | 1.55 | 2 | 2 |
| R8009_M8024__far_ch1 | 7.10 | 6.93 | 0.60 | 0.62 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.74 | 8.07 | 0.53 | 0.51 | 2 | 2 |
| R8009_M8026__far_ch1 | 9.97 | 10.04 | 1.16 | 1.18 | 2 | 2 |
| R8009_M8027__far_ch1 | 7.91 | 7.98 | 1.43 | 1.38 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.10 | 6.92 | 0.76 | 0.74 | 2 | 2 |
