# Diarization scores: A-fa-r75a_s2000/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75a_s2000/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s2000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T00:37:19+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75a_s2000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7942-epoch=7.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.66 | 5.59 | 4.32 | 0.75 | 11.30 | 100.00 | 0.00 |
| 0.25 | 1.79 | 1.07 | 0.59 | 0.12 | 2.57 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.34 (IoU 95.24) | 2.02 (IoU 2.06) |
| silence | 2.04 (IoU 2.08) | 14.60 (IoU 78.23) |

Speech P/R/F1: 97.55 / 97.58 / 97.56; miss 2.42 of ref speech, FA 12.27 of ref silence, SAD error 4.87.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13097 | 12826 | 92.18 | 90.27 | 91.22 | 0.042 | 0.030 | -0.001 | 0.000 |
| 0.25 | offset | 13097 | 12826 | 92.48 | 90.56 | 91.51 | 0.045 | 0.030 | 0.003 | 0.010 |
| 0.25 | all | 26194 | 25652 | 92.33 | 90.42 | 91.36 | 0.044 | 0.030 | 0.001 | 0.010 |
| 0.50 | onset | 13097 | 12826 | 93.15 | 91.22 | 92.17 | 0.046 | 0.030 | -0.000 | 0.000 |
| 0.50 | offset | 13097 | 12826 | 93.28 | 91.35 | 92.30 | 0.048 | 0.030 | 0.003 | 0.010 |
| 0.50 | all | 26194 | 25652 | 93.21 | 91.28 | 92.24 | 0.047 | 0.030 | 0.001 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.76 | 10.04 | 1.19 | 1.44 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.55 | 12.18 | 1.77 | 2.83 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.20 | 10.33 | 1.35 | 1.73 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.87 | 22.27 | 5.07 | 7.21 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.72 | 19.72 | 2.79 | 3.01 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.44 | 7.45 | 1.59 | 1.69 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.73 | 18.73 | 7.44 | 7.13 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.38 | 10.92 | 2.16 | 2.32 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.86 | 7.58 | 0.82 | 0.97 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.41 | 10.79 | 1.91 | 2.23 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.27 | 11.00 | 1.69 | 3.03 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.54 | 6.51 | 0.65 | 0.84 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.18 | 7.81 | 0.66 | 0.65 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.81 | 7.53 | 1.21 | 1.51 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.55 | 13.01 | 0.97 | 1.25 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.66 | 4.60 | 1.08 | 1.09 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.11 | 8.90 | 1.95 | 3.16 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.27 | 8.06 | 0.99 | 1.11 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.14 | 5.97 | 1.88 | 1.81 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.26 | 6.12 | 1.33 | 1.31 | 2 | 2 |
