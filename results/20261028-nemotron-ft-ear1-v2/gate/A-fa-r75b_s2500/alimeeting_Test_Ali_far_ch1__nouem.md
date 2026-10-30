# Diarization scores: A-fa-r75b_s2500/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75b_s2500/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s2500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T03:24:36+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75b_s2500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7936-epoch=9.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.71 | 5.63 | 4.35 | 0.73 | 11.35 | 100.00 | 0.00 |
| 0.25 | 1.76 | 1.06 | 0.62 | 0.08 | 2.66 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.33 (IoU 95.22) | 2.03 (IoU 2.07) |
| silence | 2.05 (IoU 2.10) | 14.59 (IoU 78.12) |

Speech P/R/F1: 97.54 / 97.56 / 97.55; miss 2.44 of ref speech, FA 12.34 of ref silence, SAD error 4.90.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 12819 | 92.24 | 90.27 | 91.25 | 0.043 | 0.030 | 0.002 | 0.000 |
| 0.25 | offset | 13097 | 12819 | 92.45 | 90.49 | 91.46 | 0.046 | 0.040 | 0.006 | 0.010 |
| 0.25 | all | 26195 | 25638 | 92.34 | 90.38 | 91.35 | 0.044 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13098 | 12819 | 93.18 | 91.20 | 92.18 | 0.046 | 0.030 | 0.002 | 0.000 |
| 0.50 | offset | 13097 | 12819 | 93.31 | 91.33 | 92.31 | 0.049 | 0.040 | 0.006 | 0.010 |
| 0.50 | all | 26195 | 25638 | 93.25 | 91.27 | 92.25 | 0.047 | 0.030 | 0.004 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.81 | 10.09 | 1.15 | 1.38 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.43 | 13.35 | 2.30 | 3.96 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.33 | 10.53 | 1.40 | 1.81 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.82 | 22.25 | 5.32 | 7.80 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.65 | 19.63 | 2.83 | 3.06 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.43 | 7.40 | 1.64 | 1.72 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.10 | 19.08 | 7.92 | 7.67 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.35 | 10.93 | 2.08 | 2.27 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.90 | 7.70 | 0.84 | 1.01 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.27 | 10.57 | 1.88 | 2.11 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.52 | 11.23 | 1.90 | 3.48 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.45 | 6.42 | 0.66 | 0.86 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.77 | 8.36 | 0.74 | 0.72 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.95 | 7.66 | 1.19 | 1.49 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.00 | 12.47 | 1.02 | 1.32 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.47 | 4.38 | 0.77 | 0.76 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.11 | 6.90 | 0.69 | 0.61 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.22 | 8.05 | 0.96 | 1.08 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.10 | 5.95 | 1.86 | 1.80 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.57 | 6.42 | 1.41 | 1.39 | 2 | 2 |
