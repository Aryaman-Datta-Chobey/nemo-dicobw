# Diarization scores: A-fa-r75b-seed43_s2250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75b-seed43_s2250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s2250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T07:57:32+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75b-seed43_s2250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7882-epoch=8.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.59 | 5.60 | 4.27 | 0.72 | 11.21 | 100.00 | 0.00 |
| 0.25 | 1.71 | 1.05 | 0.59 | 0.07 | 2.52 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.34 (IoU 95.30) | 2.01 (IoU 2.05) |
| silence | 2.00 (IoU 2.04) | 14.66 (IoU 78.52) |

Speech P/R/F1: 97.60 / 97.59 / 97.60; miss 2.41 of ref speech, FA 12.02 of ref silence, SAD error 4.81.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13099 | 12837 | 92.37 | 90.52 | 91.43 | 0.042 | 0.030 | 0.001 | 0.000 |
| 0.25 | offset | 13097 | 12839 | 92.59 | 90.76 | 91.66 | 0.045 | 0.030 | 0.003 | 0.010 |
| 0.25 | all | 26196 | 25676 | 92.48 | 90.64 | 91.55 | 0.044 | 0.030 | 0.002 | 0.010 |
| 0.50 | onset | 13099 | 12837 | 93.24 | 91.37 | 92.30 | 0.045 | 0.030 | 0.001 | 0.000 |
| 0.50 | offset | 13097 | 12839 | 93.35 | 91.51 | 92.42 | 0.047 | 0.030 | 0.004 | 0.010 |
| 0.50 | all | 26196 | 25676 | 93.29 | 91.44 | 92.36 | 0.046 | 0.030 | 0.002 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.77 | 10.05 | 1.12 | 1.34 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.83 | 12.48 | 1.83 | 2.97 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.32 | 10.48 | 1.40 | 1.80 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.80 | 22.13 | 5.25 | 7.41 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.72 | 19.70 | 2.89 | 3.12 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.39 | 7.39 | 1.57 | 1.67 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.07 | 19.10 | 7.92 | 7.69 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.40 | 10.97 | 2.13 | 2.35 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.84 | 7.58 | 0.89 | 1.01 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.56 | 11.00 | 2.09 | 2.44 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.66 | 10.23 | 1.33 | 2.33 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.44 | 6.42 | 0.66 | 0.86 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.63 | 8.23 | 0.74 | 0.72 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.61 | 7.34 | 1.16 | 1.47 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.98 | 12.44 | 1.00 | 1.29 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.52 | 4.43 | 0.85 | 0.85 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.90 | 6.64 | 0.69 | 0.61 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.96 | 7.78 | 0.85 | 0.95 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.95 | 5.78 | 1.78 | 1.71 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.42 | 6.30 | 1.42 | 1.41 | 2 | 2 |
