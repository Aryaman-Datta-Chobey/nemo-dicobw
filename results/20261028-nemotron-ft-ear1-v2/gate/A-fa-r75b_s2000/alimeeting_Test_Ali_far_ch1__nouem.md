# Diarization scores: A-fa-r75b_s2000/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75b_s2000/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s2000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T03:02:26+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75b_s2000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7799-epoch=7.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.59 | 5.54 | 4.31 | 0.73 | 11.21 | 100.00 | 0.00 |
| 0.25 | 1.69 | 1.02 | 0.60 | 0.08 | 2.54 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.39 (IoU 95.33) | 1.95 (IoU 1.99) |
| silence | 2.03 (IoU 2.07) | 14.63 (IoU 78.60) |

Speech P/R/F1: 97.56 / 97.66 / 97.61; miss 2.34 of ref speech, FA 12.20 of ref silence, SAD error 4.78.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 12856 | 92.34 | 90.63 | 91.48 | 0.043 | 0.030 | -0.001 | 0.000 |
| 0.25 | offset | 13097 | 12858 | 92.54 | 90.85 | 91.69 | 0.045 | 0.030 | 0.003 | 0.010 |
| 0.25 | all | 26195 | 25714 | 92.44 | 90.74 | 91.58 | 0.044 | 0.030 | 0.001 | 0.000 |
| 0.50 | onset | 13098 | 12856 | 93.22 | 91.50 | 92.36 | 0.046 | 0.030 | -0.001 | 0.000 |
| 0.50 | offset | 13097 | 12858 | 93.31 | 91.61 | 92.45 | 0.047 | 0.030 | 0.003 | 0.010 |
| 0.50 | all | 26195 | 25714 | 93.27 | 91.56 | 92.40 | 0.047 | 0.030 | 0.001 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.60 | 9.88 | 1.12 | 1.31 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.02 | 12.82 | 2.10 | 3.63 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.33 | 10.52 | 1.42 | 1.80 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.98 | 22.36 | 5.43 | 7.66 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.73 | 19.71 | 2.84 | 3.06 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.44 | 7.43 | 1.60 | 1.69 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.17 | 19.19 | 7.87 | 7.66 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.26 | 10.83 | 2.08 | 2.27 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.91 | 7.72 | 0.86 | 1.03 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.37 | 10.71 | 1.92 | 2.18 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.71 | 10.20 | 1.35 | 2.39 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.44 | 6.38 | 0.66 | 0.85 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.51 | 8.11 | 0.68 | 0.67 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.72 | 7.41 | 1.13 | 1.40 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.00 | 12.41 | 0.91 | 1.12 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.46 | 4.36 | 0.80 | 0.79 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.81 | 6.56 | 0.66 | 0.58 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.99 | 7.81 | 0.90 | 1.00 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.77 | 5.60 | 1.70 | 1.63 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.19 | 6.07 | 1.24 | 1.22 | 2 | 2 |
