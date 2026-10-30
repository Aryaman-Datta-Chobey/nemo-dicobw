# Diarization scores: A-fa-seed43_s500/alimeeting_Test_Ali_far_ch1

- name: `A-fa-seed43_s500/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-seed43_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T15:02:54+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-seed43_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7960-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.72 | 5.35 | 4.66 | 0.71 | 11.30 | 100.00 | 0.00 |
| 0.25 | 1.86 | 0.95 | 0.84 | 0.08 | 2.58 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.19 (IoU 95.23) | 1.81 (IoU 1.86) |
| silence | 2.25 (IoU 2.30) | 14.74 (IoU 78.37) |

Speech P/R/F1: 97.30 / 97.81 / 97.56; miss 2.19 of ref speech, FA 13.27 of ref silence, SAD error 4.90.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12631 | 93.14 | 89.78 | 91.43 | 0.043 | 0.030 | -0.007 | 0.000 |
| 0.25 | offset | 13103 | 12631 | 93.50 | 90.13 | 91.79 | 0.048 | 0.040 | 0.007 | 0.010 |
| 0.25 | all | 26206 | 25262 | 93.32 | 89.96 | 91.61 | 0.045 | 0.030 | 0.000 | 0.010 |
| 0.50 | onset | 13103 | 12631 | 94.14 | 90.75 | 92.41 | 0.046 | 0.030 | -0.006 | 0.000 |
| 0.50 | offset | 13103 | 12631 | 94.31 | 90.91 | 92.58 | 0.050 | 0.040 | 0.008 | 0.010 |
| 0.50 | all | 26206 | 25262 | 94.22 | 90.83 | 92.50 | 0.048 | 0.030 | 0.001 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.15 | 11.37 | 1.13 | 1.35 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.20 | 12.95 | 2.05 | 3.50 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.73 | 9.96 | 1.36 | 1.69 | 4 | 4 |
| R8004_M8006__far_ch1 | 18.99 | 21.33 | 5.07 | 7.14 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.72 | 18.83 | 2.94 | 3.28 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.36 | 7.35 | 1.56 | 1.67 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.47 | 18.54 | 7.68 | 7.44 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.48 | 10.98 | 2.14 | 2.28 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.28 | 7.99 | 0.75 | 0.91 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.84 | 11.06 | 1.79 | 2.01 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.35 | 10.92 | 1.33 | 2.31 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.50 | 6.41 | 0.62 | 0.81 | 3 | 3 |
| R8009_M8021__far_ch1 | 6.70 | 6.42 | 0.57 | 0.57 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.05 | 6.64 | 0.99 | 1.22 | 2 | 2 |
| R8009_M8023__far_ch1 | 11.79 | 14.04 | 0.96 | 1.20 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.77 | 4.60 | 0.48 | 0.48 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.31 | 6.99 | 0.79 | 0.71 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.67 | 8.47 | 1.06 | 1.19 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.39 | 6.20 | 1.93 | 1.86 | 2 | 2 |
| R8009_M8028__far_ch1 | 9.59 | 8.56 | 4.76 | 4.30 | 2 | 2 |
