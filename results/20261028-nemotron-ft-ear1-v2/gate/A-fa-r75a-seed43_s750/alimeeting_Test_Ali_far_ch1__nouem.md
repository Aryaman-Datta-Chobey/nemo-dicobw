# Diarization scores: A-fa-r75a-seed43_s750/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75a-seed43_s750/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T04:32:44+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75a-seed43_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7851-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.58 | 5.57 | 4.31 | 0.70 | 11.17 | 100.00 | 0.00 |
| 0.25 | 1.64 | 0.97 | 0.60 | 0.06 | 2.45 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.36 (IoU 95.27) | 1.99 (IoU 2.03) |
| silence | 2.05 (IoU 2.09) | 14.61 (IoU 78.34) |

Speech P/R/F1: 97.54 / 97.62 / 97.58; miss 2.38 of ref speech, FA 12.32 of ref silence, SAD error 4.85.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13096 | 12721 | 92.86 | 90.20 | 91.51 | 0.043 | 0.030 | 0.001 | 0.000 |
| 0.25 | offset | 13097 | 12723 | 93.12 | 90.46 | 91.77 | 0.046 | 0.040 | 0.004 | 0.010 |
| 0.25 | all | 26193 | 25444 | 92.99 | 90.33 | 91.64 | 0.044 | 0.030 | 0.002 | 0.010 |
| 0.50 | onset | 13096 | 12721 | 93.79 | 91.10 | 92.43 | 0.046 | 0.030 | 0.001 | 0.000 |
| 0.50 | offset | 13097 | 12723 | 93.95 | 91.27 | 92.59 | 0.049 | 0.040 | 0.004 | 0.010 |
| 0.50 | all | 26193 | 25444 | 93.87 | 91.18 | 92.51 | 0.047 | 0.030 | 0.002 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.27 | 10.54 | 1.20 | 1.45 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.50 | 12.10 | 1.78 | 2.84 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.04 | 10.24 | 1.39 | 1.80 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.61 | 21.83 | 5.29 | 7.62 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.37 | 19.35 | 2.78 | 3.02 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.32 | 7.34 | 1.57 | 1.68 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.72 | 18.76 | 7.72 | 7.43 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.27 | 10.84 | 1.87 | 2.01 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.92 | 7.66 | 0.77 | 0.92 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.50 | 10.77 | 1.90 | 2.17 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.65 | 10.22 | 1.35 | 2.38 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.24 | 6.23 | 0.53 | 0.76 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.13 | 7.76 | 0.68 | 0.67 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.58 | 7.29 | 1.07 | 1.34 | 2 | 2 |
| R8009_M8023__far_ch1 | 12.26 | 14.67 | 0.91 | 1.20 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.30 | 4.22 | 0.63 | 0.62 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.01 | 6.89 | 0.73 | 0.70 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.40 | 8.24 | 0.93 | 1.05 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.86 | 5.71 | 1.69 | 1.62 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.30 | 6.16 | 1.27 | 1.25 | 2 | 2 |
