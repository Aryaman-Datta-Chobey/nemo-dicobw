# Diarization scores: C-fa_s750/alimeeting_Test_Ali_far_ch1__nouem

- name: `C-fa_s750/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-fa_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T23:18:49+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `C-fa_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7925-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.67 | 5.51 | 4.44 | 0.73 | 11.31 | 100.00 | 0.00 |
| 0.25 | 1.71 | 0.91 | 0.70 | 0.10 | 2.61 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.61 (IoU 95.28) | 1.73 (IoU 1.78) |
| silence | 2.31 (IoU 2.35) | 14.35 (IoU 78.00) |

Speech P/R/F1: 97.25 / 97.92 / 97.58; miss 2.08 of ref speech, FA 13.88 of ref silence, SAD error 4.86.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13096 | 12733 | 92.95 | 90.37 | 91.64 | 0.042 | 0.030 | 0.003 | 0.010 |
| 0.25 | offset | 13099 | 12733 | 93.32 | 90.71 | 91.99 | 0.049 | 0.040 | 0.017 | 0.020 |
| 0.25 | all | 26195 | 25466 | 93.13 | 90.54 | 91.82 | 0.046 | 0.040 | 0.010 | 0.010 |
| 0.50 | onset | 13096 | 12733 | 93.91 | 91.30 | 92.59 | 0.045 | 0.030 | 0.003 | 0.010 |
| 0.50 | offset | 13099 | 12733 | 94.03 | 91.40 | 92.70 | 0.052 | 0.040 | 0.018 | 0.020 |
| 0.50 | all | 26195 | 25466 | 93.97 | 91.35 | 92.64 | 0.048 | 0.040 | 0.010 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.24 | 11.50 | 1.19 | 1.42 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.22 | 13.01 | 2.96 | 5.18 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.68 | 9.91 | 1.34 | 1.69 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.34 | 21.71 | 5.27 | 7.27 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.85 | 19.01 | 2.88 | 3.24 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.43 | 7.50 | 1.59 | 1.73 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.95 | 19.07 | 8.00 | 7.74 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.41 | 11.01 | 2.23 | 2.41 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.50 | 8.16 | 0.75 | 0.87 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.06 | 11.69 | 1.78 | 2.14 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.10 | 10.66 | 1.33 | 2.31 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.51 | 6.43 | 0.47 | 0.67 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.64 | 8.17 | 0.46 | 0.46 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.33 | 6.94 | 0.84 | 1.06 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.05 | 10.99 | 0.61 | 0.74 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.78 | 4.66 | 0.45 | 0.44 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.63 | 7.11 | 0.65 | 0.58 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.61 | 8.36 | 0.81 | 0.93 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.82 | 5.57 | 1.57 | 1.50 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.05 | 6.69 | 2.28 | 2.18 | 2 | 2 |
