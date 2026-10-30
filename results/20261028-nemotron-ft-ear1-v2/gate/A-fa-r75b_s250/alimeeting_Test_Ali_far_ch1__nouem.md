# Diarization scores: A-fa-r75b_s250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75b_s250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T01:45:03+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75b_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7683-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.45 | 5.51 | 4.25 | 0.69 | 11.03 | 100.00 | 0.00 |
| 0.25 | 1.70 | 0.95 | 0.68 | 0.06 | 2.45 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.39 (IoU 95.40) | 1.97 (IoU 2.00) |
| silence | 1.96 (IoU 2.00) | 14.69 (IoU 78.93) |

Speech P/R/F1: 97.65 / 97.64 / 97.65; miss 2.36 of ref speech, FA 11.75 of ref silence, SAD error 4.70.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 12832 | 92.69 | 90.81 | 91.74 | 0.042 | 0.030 | 0.002 | 0.010 |
| 0.25 | offset | 13097 | 12833 | 92.87 | 91.00 | 91.92 | 0.044 | 0.030 | 0.003 | 0.010 |
| 0.25 | all | 26195 | 25665 | 92.78 | 90.90 | 91.83 | 0.043 | 0.030 | 0.002 | 0.010 |
| 0.50 | onset | 13098 | 12832 | 93.53 | 91.63 | 92.57 | 0.045 | 0.030 | 0.002 | 0.010 |
| 0.50 | offset | 13097 | 12833 | 93.72 | 91.83 | 92.77 | 0.047 | 0.030 | 0.003 | 0.010 |
| 0.50 | all | 26195 | 25665 | 93.63 | 91.73 | 92.67 | 0.046 | 0.030 | 0.002 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.38 | 10.61 | 1.19 | 1.42 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.50 | 12.07 | 1.74 | 2.81 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.81 | 10.02 | 1.31 | 1.69 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.57 | 21.86 | 4.99 | 7.25 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.64 | 19.65 | 2.77 | 3.05 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.27 | 7.31 | 1.57 | 1.70 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.61 | 18.60 | 7.78 | 7.50 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.11 | 10.68 | 1.90 | 2.04 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.85 | 7.50 | 0.72 | 0.83 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.35 | 10.72 | 2.02 | 2.38 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.49 | 10.02 | 1.32 | 2.36 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.07 | 5.97 | 0.47 | 0.59 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.80 | 7.45 | 0.56 | 0.55 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.20 | 6.83 | 1.08 | 1.32 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.50 | 11.77 | 0.87 | 1.06 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.63 | 4.58 | 0.80 | 0.81 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.21 | 6.93 | 0.72 | 0.63 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.30 | 8.11 | 0.99 | 1.12 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.68 | 5.49 | 1.57 | 1.50 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.13 | 6.83 | 2.56 | 2.44 | 2 | 2 |
