# Diarization scores: D-fa_s1250/alimeeting_Test_Ali_far_ch1__nouem

- name: `D-fa_s1250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-fa_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T00:32:05+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `D-fa_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7850-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.34 | 7.54 | 3.22 | 0.58 | 12.04 | 100.00 | 0.00 |
| 0.25 | 1.86 | 1.41 | 0.41 | 0.05 | 2.88 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.34 (IoU 95.25) | 2.02 (IoU 2.06) |
| silence | 2.04 (IoU 2.08) | 14.60 (IoU 78.27) |

Speech P/R/F1: 97.56 / 97.58 / 97.57; miss 2.42 of ref speech, FA 12.25 of ref silence, SAD error 4.87.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 13322 | 90.16 | 91.70 | 90.92 | 0.042 | 0.030 | -0.005 | 0.000 |
| 0.25 | offset | 13096 | 13325 | 90.43 | 92.01 | 91.22 | 0.046 | 0.030 | 0.001 | 0.010 |
| 0.25 | all | 26194 | 26647 | 90.30 | 91.86 | 91.07 | 0.044 | 0.030 | -0.002 | 0.000 |
| 0.50 | onset | 13098 | 13322 | 91.10 | 92.66 | 91.87 | 0.045 | 0.030 | -0.004 | 0.000 |
| 0.50 | offset | 13096 | 13325 | 91.22 | 92.81 | 92.01 | 0.048 | 0.030 | 0.001 | 0.010 |
| 0.50 | all | 26194 | 26647 | 91.16 | 92.73 | 91.94 | 0.047 | 0.030 | -0.001 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.65 | 11.06 | 1.45 | 1.72 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.33 | 13.09 | 1.82 | 2.91 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.95 | 11.49 | 1.56 | 2.02 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.83 | 25.89 | 7.28 | 9.66 | 4 | 4 |
| R8005_M8007__far_ch1 | 21.89 | 21.99 | 3.76 | 3.95 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.35 | 8.54 | 2.00 | 2.30 | 4 | 4 |
| R8005_M8009__far_ch1 | 21.65 | 21.51 | 9.45 | 9.20 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.99 | 11.54 | 2.43 | 2.76 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.03 | 7.69 | 0.78 | 0.96 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.53 | 10.65 | 1.99 | 2.24 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.87 | 10.68 | 1.44 | 2.72 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.68 | 6.63 | 0.50 | 0.66 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.19 | 6.88 | 0.55 | 0.54 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.39 | 7.07 | 0.99 | 1.23 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.14 | 12.43 | 0.75 | 0.95 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.54 | 4.44 | 0.61 | 0.60 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.06 | 6.83 | 0.64 | 0.59 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.42 | 8.18 | 0.96 | 1.10 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.93 | 5.73 | 1.53 | 1.47 | 2 | 2 |
| R8009_M8028__far_ch1 | 5.95 | 5.84 | 0.98 | 0.98 | 2 | 2 |
