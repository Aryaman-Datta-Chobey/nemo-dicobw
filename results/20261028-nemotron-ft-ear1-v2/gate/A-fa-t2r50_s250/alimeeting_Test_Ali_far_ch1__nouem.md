# Diarization scores: A-fa-t2r50_s250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-t2r50_s250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T12:54:04+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-t2r50_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7774-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.75 | 5.54 | 4.54 | 0.67 | 11.21 | 100.00 | 0.00 |
| 0.25 | 1.99 | 0.96 | 0.97 | 0.06 | 2.54 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.43 (IoU 95.31) | 1.92 (IoU 1.96) |
| silence | 2.09 (IoU 2.13) | 14.56 (IoU 78.41) |

Speech P/R/F1: 97.50 / 97.69 / 97.60; miss 2.31 of ref speech, FA 12.53 of ref silence, SAD error 4.81.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13095 | 12781 | 92.75 | 90.52 | 91.62 | 0.042 | 0.030 | 0.003 | 0.010 |
| 0.25 | offset | 13097 | 12782 | 92.93 | 90.69 | 91.80 | 0.046 | 0.040 | 0.009 | 0.010 |
| 0.25 | all | 26192 | 25563 | 92.84 | 90.61 | 91.71 | 0.044 | 0.030 | 0.006 | 0.010 |
| 0.50 | onset | 13095 | 12781 | 93.62 | 91.38 | 92.49 | 0.045 | 0.030 | 0.003 | 0.010 |
| 0.50 | offset | 13097 | 12782 | 93.76 | 91.51 | 92.62 | 0.048 | 0.040 | 0.009 | 0.010 |
| 0.50 | all | 26192 | 25563 | 93.69 | 91.44 | 92.56 | 0.047 | 0.030 | 0.006 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.22 | 10.46 | 1.11 | 1.31 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.53 | 12.06 | 1.68 | 2.69 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.85 | 10.05 | 1.23 | 1.56 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.63 | 21.90 | 4.97 | 7.17 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.92 | 19.93 | 2.81 | 3.08 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.38 | 7.43 | 1.59 | 1.70 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.60 | 18.61 | 7.56 | 7.27 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.18 | 10.73 | 1.81 | 1.98 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.04 | 7.72 | 0.64 | 0.74 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.22 | 10.21 | 1.81 | 2.04 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.54 | 10.09 | 1.24 | 2.25 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.11 | 5.98 | 0.45 | 0.56 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.28 | 7.88 | 0.55 | 0.54 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.33 | 6.94 | 1.02 | 1.23 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.55 | 11.65 | 1.27 | 1.49 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.71 | 4.65 | 0.68 | 0.69 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.77 | 7.39 | 0.75 | 0.67 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.24 | 8.09 | 1.10 | 1.26 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.92 | 5.75 | 1.69 | 1.63 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.03 | 10.53 | 7.95 | 6.82 | 2 | 2 |
