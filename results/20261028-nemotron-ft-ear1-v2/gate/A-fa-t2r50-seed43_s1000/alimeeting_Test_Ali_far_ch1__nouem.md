# Diarization scores: A-fa-t2r50-seed43_s1000/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-t2r50-seed43_s1000/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50-seed43_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T21:32:18+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-t2r50-seed43_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7905-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.72 | 5.64 | 4.38 | 0.70 | 11.28 | 95.00 | 0.05 |
| 0.25 | 1.89 | 1.05 | 0.77 | 0.07 | 2.58 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.30 (IoU 95.23) | 2.05 (IoU 2.10) |
| silence | 2.02 (IoU 2.06) | 14.62 (IoU 78.21) |

Speech P/R/F1: 97.58 / 97.54 / 97.56; miss 2.46 of ref speech, FA 12.14 of ref silence, SAD error 4.89.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13096 | 12752 | 92.39 | 89.97 | 91.16 | 0.042 | 0.030 | 0.002 | 0.010 |
| 0.25 | offset | 13096 | 12753 | 92.81 | 90.38 | 91.58 | 0.046 | 0.030 | 0.006 | 0.010 |
| 0.25 | all | 26192 | 25505 | 92.60 | 90.17 | 91.37 | 0.044 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13096 | 12752 | 93.41 | 90.96 | 92.17 | 0.046 | 0.030 | 0.003 | 0.010 |
| 0.50 | offset | 13096 | 12753 | 93.56 | 91.11 | 92.32 | 0.048 | 0.040 | 0.006 | 0.010 |
| 0.50 | all | 26192 | 25505 | 93.49 | 91.04 | 92.25 | 0.047 | 0.030 | 0.004 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.17 | 10.40 | 1.10 | 1.29 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.75 | 12.34 | 1.87 | 2.96 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.13 | 10.30 | 1.41 | 1.76 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.40 | 21.77 | 4.99 | 7.21 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.38 | 19.45 | 2.92 | 3.28 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.36 | 7.35 | 1.55 | 1.65 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.73 | 18.80 | 7.72 | 7.47 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.35 | 10.91 | 2.02 | 2.20 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.92 | 7.65 | 0.82 | 0.97 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.46 | 10.59 | 1.81 | 2.02 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.68 | 10.25 | 1.36 | 2.34 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.36 | 6.32 | 0.64 | 0.84 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.56 | 8.18 | 0.78 | 0.77 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.89 | 7.56 | 1.22 | 1.48 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.35 | 12.84 | 1.07 | 1.37 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.53 | 4.47 | 0.78 | 0.78 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.43 | 7.25 | 0.80 | 0.74 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.51 | 8.34 | 1.05 | 1.17 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.36 | 6.24 | 1.90 | 1.85 | 2 | 2 |
| R8009_M8028__far_ch1 | 9.33 | 8.69 | 4.67 | 4.29 | 2 | 3 |
