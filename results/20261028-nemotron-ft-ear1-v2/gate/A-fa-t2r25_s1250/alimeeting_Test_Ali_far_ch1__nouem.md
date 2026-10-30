# Diarization scores: A-fa-t2r25_s1250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-t2r25_s1250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T12:27:23+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-t2r25_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7843-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.67 | 5.57 | 4.38 | 0.71 | 11.29 | 95.00 | 0.05 |
| 0.25 | 1.75 | 1.07 | 0.61 | 0.07 | 2.48 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.35 (IoU 95.20) | 2.01 (IoU 2.05) |
| silence | 2.09 (IoU 2.13) | 14.55 (IoU 78.02) |

Speech P/R/F1: 97.49 / 97.59 / 97.54; miss 2.41 of ref speech, FA 12.56 of ref silence, SAD error 4.92.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13096 | 12718 | 92.52 | 89.85 | 91.17 | 0.043 | 0.030 | 0.002 | 0.010 |
| 0.25 | offset | 13097 | 12718 | 92.78 | 90.10 | 91.42 | 0.046 | 0.040 | 0.009 | 0.010 |
| 0.25 | all | 26193 | 25436 | 92.65 | 89.97 | 91.29 | 0.045 | 0.030 | 0.005 | 0.010 |
| 0.50 | onset | 13096 | 12718 | 93.45 | 90.75 | 92.08 | 0.046 | 0.030 | 0.002 | 0.010 |
| 0.50 | offset | 13097 | 12718 | 93.60 | 90.89 | 92.23 | 0.049 | 0.040 | 0.009 | 0.010 |
| 0.50 | all | 26193 | 25436 | 93.52 | 90.82 | 92.15 | 0.047 | 0.030 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.51 | 10.75 | 1.10 | 1.31 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.91 | 12.53 | 1.78 | 2.70 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.19 | 10.36 | 1.46 | 1.79 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.32 | 21.65 | 5.14 | 7.18 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.02 | 19.05 | 2.82 | 3.04 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.45 | 7.44 | 1.58 | 1.69 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.88 | 18.90 | 7.71 | 7.41 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.41 | 10.93 | 2.07 | 2.26 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.08 | 7.84 | 0.87 | 1.02 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.73 | 11.10 | 1.92 | 2.16 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.42 | 11.01 | 1.42 | 2.40 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.51 | 6.46 | 0.68 | 0.87 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.38 | 8.02 | 0.86 | 0.84 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.74 | 7.37 | 1.25 | 1.44 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.22 | 12.71 | 1.07 | 1.39 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.78 | 4.65 | 0.93 | 0.91 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.20 | 7.00 | 0.76 | 0.71 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.37 | 8.19 | 1.00 | 1.11 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.61 | 6.48 | 2.11 | 2.05 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.72 | 6.55 | 1.59 | 1.57 | 2 | 3 |
