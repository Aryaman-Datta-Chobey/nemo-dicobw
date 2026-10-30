# Diarization scores: A-fa-r75b-seed43_s2000/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75b-seed43_s2000/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s2000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T07:47:57+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75b-seed43_s2000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7956-epoch=7.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.68 | 5.69 | 4.28 | 0.71 | 11.30 | 100.00 | 0.00 |
| 0.25 | 1.79 | 1.09 | 0.62 | 0.07 | 2.59 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.26 (IoU 95.21) | 2.08 (IoU 2.12) |
| silence | 2.01 (IoU 2.05) | 14.65 (IoU 78.19) |

Speech P/R/F1: 97.59 / 97.51 / 97.55; miss 2.49 of ref speech, FA 12.06 of ref silence, SAD error 4.90.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 12794 | 92.38 | 90.24 | 91.29 | 0.043 | 0.030 | -0.001 | 0.000 |
| 0.25 | offset | 13096 | 12795 | 92.61 | 90.49 | 91.54 | 0.045 | 0.030 | 0.001 | 0.010 |
| 0.25 | all | 26194 | 25589 | 92.50 | 90.36 | 91.42 | 0.044 | 0.030 | 0.000 | 0.000 |
| 0.50 | onset | 13098 | 12794 | 93.37 | 91.20 | 92.28 | 0.046 | 0.030 | -0.000 | 0.000 |
| 0.50 | offset | 13096 | 12795 | 93.43 | 91.29 | 92.35 | 0.048 | 0.030 | 0.001 | 0.010 |
| 0.50 | all | 26194 | 25589 | 93.40 | 91.25 | 92.31 | 0.047 | 0.030 | 0.001 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.79 | 10.08 | 1.09 | 1.30 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.99 | 12.72 | 1.96 | 3.36 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.25 | 10.43 | 1.41 | 1.82 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.76 | 22.17 | 5.27 | 7.59 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.63 | 19.59 | 2.82 | 3.06 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.40 | 7.43 | 1.57 | 1.67 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.94 | 18.94 | 7.92 | 7.67 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.43 | 11.02 | 2.23 | 2.45 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.89 | 7.67 | 0.83 | 0.97 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.38 | 10.62 | 1.95 | 2.20 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.82 | 10.42 | 1.37 | 2.35 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.56 | 6.52 | 0.65 | 0.86 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.02 | 7.67 | 0.78 | 0.76 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.55 | 7.27 | 1.18 | 1.48 | 2 | 2 |
| R8009_M8023__far_ch1 | 11.75 | 14.21 | 1.21 | 1.45 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.84 | 4.76 | 1.10 | 1.11 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.93 | 6.72 | 0.73 | 0.64 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.20 | 8.05 | 0.90 | 1.01 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.17 | 6.00 | 1.91 | 1.84 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.88 | 6.67 | 2.06 | 2.01 | 2 | 2 |
