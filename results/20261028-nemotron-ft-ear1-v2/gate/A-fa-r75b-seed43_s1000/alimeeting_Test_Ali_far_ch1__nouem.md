# Diarization scores: A-fa-r75b-seed43_s1000/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75b-seed43_s1000/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T07:09:37+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75b-seed43_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7939-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.55 | 5.57 | 4.29 | 0.70 | 11.16 | 100.00 | 0.00 |
| 0.25 | 1.71 | 1.03 | 0.62 | 0.06 | 2.49 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.39 (IoU 95.30) | 1.97 (IoU 2.01) |
| silence | 2.04 (IoU 2.08) | 14.60 (IoU 78.44) |

Speech P/R/F1: 97.55 / 97.64 / 97.59; miss 2.36 of ref speech, FA 12.27 of ref silence, SAD error 4.81.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13097 | 12747 | 92.61 | 90.14 | 91.36 | 0.042 | 0.030 | 0.003 | 0.010 |
| 0.25 | offset | 13098 | 12746 | 92.86 | 90.36 | 91.60 | 0.045 | 0.030 | 0.007 | 0.010 |
| 0.25 | all | 26195 | 25493 | 92.74 | 90.25 | 91.48 | 0.044 | 0.030 | 0.005 | 0.010 |
| 0.50 | onset | 13097 | 12747 | 93.53 | 91.03 | 92.26 | 0.045 | 0.030 | 0.003 | 0.010 |
| 0.50 | offset | 13098 | 12746 | 93.69 | 91.17 | 92.42 | 0.048 | 0.040 | 0.007 | 0.010 |
| 0.50 | all | 26195 | 25493 | 93.61 | 91.10 | 92.34 | 0.046 | 0.030 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.18 | 10.45 | 1.10 | 1.30 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.62 | 12.27 | 1.81 | 2.97 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.02 | 10.20 | 1.35 | 1.74 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.49 | 21.79 | 5.17 | 7.30 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.39 | 19.39 | 2.88 | 3.12 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.29 | 7.30 | 1.50 | 1.61 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.85 | 18.89 | 7.94 | 7.70 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.22 | 10.78 | 1.98 | 2.17 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.92 | 7.68 | 0.77 | 0.94 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.50 | 10.84 | 1.83 | 2.10 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.64 | 10.22 | 1.29 | 2.29 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.41 | 6.38 | 0.62 | 0.81 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.52 | 8.11 | 0.67 | 0.65 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.92 | 7.62 | 1.19 | 1.46 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.98 | 12.41 | 1.05 | 1.33 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.62 | 4.56 | 0.87 | 0.87 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.06 | 6.78 | 0.71 | 0.62 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.02 | 7.85 | 0.94 | 1.05 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.06 | 5.89 | 1.78 | 1.71 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.91 | 6.71 | 1.95 | 1.90 | 2 | 2 |
