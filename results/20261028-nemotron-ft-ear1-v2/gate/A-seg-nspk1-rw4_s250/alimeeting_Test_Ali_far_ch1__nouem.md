# Diarization scores: A-seg-nspk1-rw4_s250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-seg-nspk1-rw4_s250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1-rw4_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T03:50:04+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-seg-nspk1-rw4_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1-rw4/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8061-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.36 | 3.98 | 7.65 | 0.73 | 12.73 | 100.00 | 0.00 |
| 0.25 | 1.44 | 0.58 | 0.79 | 0.07 | 2.29 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.20 (IoU 93.86) | 1.15 (IoU 1.20) |
| silence | 4.23 (IoU 4.27) | 12.42 (IoU 69.79) |

Speech P/R/F1: 95.11 / 98.62 / 96.83; miss 1.38 of ref speech, FA 25.38 of ref silence, SAD error 6.45.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13100 | 11297 | 94.57 | 81.56 | 87.58 | 0.059 | 0.050 | -0.028 | -0.020 |
| 0.25 | offset | 13101 | 11297 | 93.87 | 80.94 | 86.93 | 0.064 | 0.050 | 0.038 | 0.040 |
| 0.25 | all | 26201 | 22594 | 94.22 | 81.25 | 87.25 | 0.062 | 0.050 | 0.005 | 0.010 |
| 0.50 | onset | 13100 | 11297 | 95.59 | 82.44 | 88.53 | 0.062 | 0.050 | -0.028 | -0.020 |
| 0.50 | offset | 13101 | 11297 | 95.63 | 82.46 | 88.56 | 0.069 | 0.050 | 0.041 | 0.040 |
| 0.50 | all | 26201 | 22594 | 95.61 | 82.45 | 88.54 | 0.066 | 0.050 | 0.006 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.34 | 10.48 | 1.29 | 1.43 | 4 | 4 |
| R8002_M8003__far_ch1 | 13.68 | 14.49 | 1.64 | 2.69 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.34 | 10.49 | 1.30 | 1.72 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.78 | 21.50 | 4.82 | 7.21 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.58 | 19.40 | 2.58 | 2.91 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.54 | 8.31 | 1.44 | 1.61 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.89 | 18.69 | 7.54 | 7.27 | 4 | 4 |
| R8006_M8012__far_ch1 | 11.47 | 11.80 | 2.16 | 2.37 | 4 | 4 |
| R8008_M8014__far_ch1 | 12.39 | 12.21 | 0.42 | 0.53 | 3 | 3 |
| R8008_M8015__far_ch1 | 23.37 | 21.08 | 1.76 | 2.25 | 3 | 3 |
| R8008_M8016__far_ch1 | 12.01 | 14.03 | 1.10 | 2.19 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.11 | 13.92 | 0.45 | 0.47 | 3 | 3 |
| R8009_M8021__far_ch1 | 9.05 | 8.51 | 0.54 | 0.53 | 2 | 2 |
| R8009_M8022__far_ch1 | 5.91 | 6.49 | 0.97 | 1.32 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.43 | 10.13 | 0.64 | 0.82 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.70 | 4.59 | 0.49 | 0.48 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.48 | 7.09 | 0.58 | 0.56 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.33 | 7.06 | 0.57 | 0.67 | 2 | 2 |
| R8009_M8027__far_ch1 | 9.89 | 8.86 | 0.88 | 0.85 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.53 | 7.03 | 0.78 | 0.77 | 2 | 2 |
