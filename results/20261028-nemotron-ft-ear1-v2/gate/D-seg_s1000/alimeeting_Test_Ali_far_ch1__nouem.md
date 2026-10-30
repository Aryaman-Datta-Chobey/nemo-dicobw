# Diarization scores: D-seg_s1000/alimeeting_Test_Ali_far_ch1__nouem

- name: `D-seg_s1000/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-seg_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T19:04:32+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `D-seg_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7988-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.71 | 4.59 | 7.38 | 0.74 | 12.81 | 100.00 | 0.00 |
| 0.25 | 1.42 | 0.68 | 0.68 | 0.06 | 2.34 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.74 (IoU 93.49) | 0.56 (IoU 0.60) |
| silence | 5.20 (IoU 5.23) | 11.50 (IoU 66.61) |

Speech P/R/F1: 94.09 / 99.32 / 96.63; miss 0.68 of ref speech, FA 31.14 of ref silence, SAD error 6.92.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 11880 | 93.23 | 84.53 | 88.67 | 0.070 | 0.060 | -0.061 | -0.060 |
| 0.25 | offset | 13101 | 11882 | 93.43 | 84.73 | 88.87 | 0.077 | 0.070 | 0.061 | 0.070 |
| 0.25 | all | 26204 | 23762 | 93.33 | 84.63 | 88.77 | 0.074 | 0.070 | -0.000 | 0.000 |
| 0.50 | onset | 13103 | 11880 | 94.56 | 85.74 | 89.93 | 0.074 | 0.060 | -0.063 | -0.060 |
| 0.50 | offset | 13101 | 11882 | 94.56 | 85.76 | 89.95 | 0.081 | 0.070 | 0.063 | 0.070 |
| 0.50 | all | 26204 | 23762 | 94.56 | 85.75 | 89.94 | 0.077 | 0.070 | -0.000 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.29 | 10.35 | 0.94 | 1.14 | 4 | 4 |
| R8002_M8003__far_ch1 | 12.17 | 13.03 | 1.72 | 2.77 | 4 | 4 |
| R8004_M8005__far_ch1 | 10.21 | 11.27 | 1.15 | 1.55 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.99 | 23.83 | 5.50 | 7.80 | 4 | 4 |
| R8005_M8007__far_ch1 | 20.50 | 20.50 | 2.86 | 3.04 | 4 | 4 |
| R8005_M8008__far_ch1 | 9.24 | 9.01 | 1.60 | 1.87 | 4 | 4 |
| R8005_M8009__far_ch1 | 20.65 | 20.50 | 8.42 | 8.22 | 4 | 4 |
| R8006_M8012__far_ch1 | 11.59 | 11.75 | 2.02 | 2.24 | 4 | 4 |
| R8008_M8014__far_ch1 | 8.89 | 8.94 | 0.51 | 0.63 | 3 | 3 |
| R8008_M8015__far_ch1 | 12.51 | 13.96 | 1.87 | 2.41 | 3 | 3 |
| R8008_M8016__far_ch1 | 12.03 | 12.99 | 1.40 | 2.38 | 3 | 3 |
| R8008_M8017__far_ch1 | 8.97 | 8.93 | 0.24 | 0.35 | 3 | 3 |
| R8009_M8021__far_ch1 | 11.73 | 10.60 | 0.46 | 0.46 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.87 | 8.23 | 0.59 | 0.87 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.26 | 15.04 | 0.33 | 0.50 | 2 | 2 |
| R8009_M8024__far_ch1 | 9.47 | 8.76 | 0.55 | 0.56 | 2 | 2 |
| R8009_M8025__far_ch1 | 9.10 | 7.78 | 0.28 | 0.23 | 2 | 2 |
| R8009_M8026__far_ch1 | 10.07 | 9.42 | 0.37 | 0.42 | 2 | 2 |
| R8009_M8027__far_ch1 | 9.76 | 8.70 | 0.75 | 0.70 | 2 | 2 |
| R8009_M8028__far_ch1 | 8.91 | 8.18 | 0.62 | 0.61 | 2 | 2 |
