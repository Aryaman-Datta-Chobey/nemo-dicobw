# Diarization scores: A-fa-r75b_s2250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75b_s2250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s2250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T03:13:38+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75b_s2250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7837-epoch=8.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.65 | 5.63 | 4.29 | 0.73 | 11.28 | 100.00 | 0.00 |
| 0.25 | 1.71 | 1.03 | 0.60 | 0.08 | 2.57 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.32 (IoU 95.25) | 2.02 (IoU 2.06) |
| silence | 2.03 (IoU 2.07) | 14.63 (IoU 78.30) |

Speech P/R/F1: 97.56 / 97.58 / 97.57; miss 2.42 of ref speech, FA 12.20 of ref silence, SAD error 4.86.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13096 | 12797 | 92.51 | 90.39 | 91.44 | 0.043 | 0.030 | 0.003 | 0.010 |
| 0.25 | offset | 13096 | 12798 | 92.80 | 90.69 | 91.74 | 0.046 | 0.040 | 0.006 | 0.010 |
| 0.25 | all | 26192 | 25595 | 92.65 | 90.54 | 91.59 | 0.044 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13096 | 12797 | 93.48 | 91.35 | 92.40 | 0.046 | 0.030 | 0.003 | 0.010 |
| 0.50 | offset | 13096 | 12798 | 93.59 | 91.46 | 92.52 | 0.048 | 0.040 | 0.006 | 0.010 |
| 0.50 | all | 26192 | 25595 | 93.54 | 91.41 | 92.46 | 0.047 | 0.030 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.87 | 10.14 | 1.14 | 1.33 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.10 | 12.99 | 2.05 | 3.68 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.25 | 10.44 | 1.38 | 1.75 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.71 | 21.99 | 5.30 | 7.50 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.61 | 19.61 | 2.84 | 3.06 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.38 | 7.36 | 1.64 | 1.73 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.97 | 19.04 | 8.03 | 7.94 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.27 | 10.87 | 2.08 | 2.32 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.98 | 7.79 | 0.84 | 1.02 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.44 | 10.79 | 1.95 | 2.25 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.71 | 10.27 | 1.36 | 2.37 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.43 | 6.39 | 0.65 | 0.86 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.77 | 8.36 | 0.69 | 0.67 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.04 | 7.75 | 1.10 | 1.37 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.39 | 12.90 | 0.95 | 1.25 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.45 | 4.37 | 0.76 | 0.76 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.98 | 6.76 | 0.65 | 0.59 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.17 | 8.02 | 0.92 | 1.04 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.12 | 5.97 | 1.80 | 1.73 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.57 | 6.41 | 1.41 | 1.38 | 2 | 2 |
