# Diarization scores: A-seg-nspk1_s250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-seg-nspk1_s250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T01:53:16+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-seg-nspk1_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8250-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.57 | 4.00 | 7.83 | 0.74 | 12.91 | 100.00 | 0.00 |
| 0.25 | 1.51 | 0.56 | 0.89 | 0.06 | 2.34 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.17 (IoU 93.78) | 1.18 (IoU 1.23) |
| silence | 4.27 (IoU 4.32) | 12.38 (IoU 69.44) |

Speech P/R/F1: 95.06 / 98.59 / 96.79; miss 1.41 of ref speech, FA 25.64 of ref silence, SAD error 6.53.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13099 | 11185 | 94.45 | 80.65 | 87.00 | 0.060 | 0.050 | -0.024 | -0.020 |
| 0.25 | offset | 13099 | 11186 | 93.70 | 80.01 | 86.32 | 0.062 | 0.050 | 0.033 | 0.030 |
| 0.25 | all | 26198 | 22371 | 94.07 | 80.33 | 86.66 | 0.061 | 0.050 | 0.004 | 0.010 |
| 0.50 | onset | 13099 | 11185 | 95.52 | 81.56 | 87.99 | 0.063 | 0.050 | -0.026 | -0.020 |
| 0.50 | offset | 13099 | 11186 | 95.49 | 81.54 | 87.96 | 0.067 | 0.050 | 0.037 | 0.030 |
| 0.50 | all | 26198 | 22371 | 95.50 | 81.55 | 87.98 | 0.065 | 0.050 | 0.006 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.49 | 10.68 | 1.11 | 1.30 | 4 | 4 |
| R8002_M8003__far_ch1 | 13.37 | 14.13 | 1.68 | 2.66 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.24 | 10.37 | 1.36 | 1.75 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.98 | 21.81 | 4.92 | 7.28 | 4 | 4 |
| R8005_M8007__far_ch1 | 20.11 | 19.94 | 2.70 | 3.03 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.48 | 8.30 | 1.55 | 1.67 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.69 | 18.51 | 7.56 | 7.20 | 4 | 4 |
| R8006_M8012__far_ch1 | 12.99 | 12.99 | 2.47 | 2.57 | 4 | 4 |
| R8008_M8014__far_ch1 | 13.44 | 13.01 | 0.40 | 0.48 | 3 | 3 |
| R8008_M8015__far_ch1 | 24.47 | 21.79 | 2.13 | 2.68 | 3 | 3 |
| R8008_M8016__far_ch1 | 12.26 | 14.09 | 1.15 | 2.22 | 3 | 3 |
| R8008_M8017__far_ch1 | 14.23 | 13.35 | 0.49 | 0.55 | 3 | 3 |
| R8009_M8021__far_ch1 | 9.11 | 8.59 | 0.56 | 0.55 | 2 | 2 |
| R8009_M8022__far_ch1 | 5.57 | 6.18 | 0.90 | 1.25 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.44 | 10.09 | 0.73 | 0.85 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.71 | 4.61 | 0.58 | 0.58 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.63 | 7.22 | 0.65 | 0.58 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.01 | 6.78 | 0.65 | 0.75 | 2 | 2 |
| R8009_M8027__far_ch1 | 11.03 | 9.71 | 1.07 | 1.00 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.94 | 7.34 | 0.77 | 0.76 | 2 | 2 |
