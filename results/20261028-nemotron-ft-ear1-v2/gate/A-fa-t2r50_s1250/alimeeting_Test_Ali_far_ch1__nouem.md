# Diarization scores: A-fa-t2r50_s1250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-t2r50_s1250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T13:33:03+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-t2r50_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7782-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.77 | 5.51 | 4.53 | 0.72 | 11.35 | 95.00 | 0.05 |
| 0.25 | 1.94 | 1.03 | 0.84 | 0.08 | 2.67 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.33 (IoU 95.24) | 2.01 (IoU 2.05) |
| silence | 2.05 (IoU 2.10) | 14.60 (IoU 78.24) |

Speech P/R/F1: 97.54 / 97.59 / 97.56; miss 2.41 of ref speech, FA 12.34 of ref silence, SAD error 4.87.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 12749 | 92.66 | 90.19 | 91.41 | 0.043 | 0.030 | 0.003 | 0.010 |
| 0.25 | offset | 13096 | 12751 | 92.93 | 90.49 | 91.69 | 0.046 | 0.040 | 0.007 | 0.010 |
| 0.25 | all | 26194 | 25500 | 92.80 | 90.34 | 91.55 | 0.045 | 0.030 | 0.005 | 0.010 |
| 0.50 | onset | 13098 | 12749 | 93.58 | 91.09 | 92.32 | 0.046 | 0.030 | 0.003 | 0.010 |
| 0.50 | offset | 13096 | 12751 | 93.66 | 91.19 | 92.41 | 0.049 | 0.040 | 0.007 | 0.010 |
| 0.50 | all | 26194 | 25500 | 93.62 | 91.14 | 92.36 | 0.047 | 0.030 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.01 | 10.24 | 1.09 | 1.29 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.16 | 12.87 | 2.11 | 3.52 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.26 | 10.45 | 1.48 | 1.87 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.52 | 21.92 | 5.11 | 7.52 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.36 | 19.36 | 2.80 | 3.06 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.41 | 7.42 | 1.61 | 1.71 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.86 | 18.87 | 7.93 | 7.67 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.38 | 10.92 | 2.13 | 2.27 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.96 | 7.71 | 0.88 | 1.04 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.66 | 11.08 | 1.88 | 2.21 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.90 | 10.51 | 1.32 | 2.33 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.38 | 6.35 | 0.61 | 0.81 | 3 | 3 |
| R8009_M8021__far_ch1 | 9.14 | 8.70 | 0.75 | 0.74 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.67 | 7.37 | 1.14 | 1.40 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.02 | 12.46 | 1.08 | 1.39 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.51 | 4.42 | 0.73 | 0.72 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.17 | 6.90 | 0.66 | 0.59 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.21 | 8.08 | 1.00 | 1.12 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.16 | 6.03 | 1.91 | 1.85 | 2 | 2 |
| R8009_M8028__far_ch1 | 9.78 | 8.98 | 5.23 | 4.75 | 2 | 3 |
