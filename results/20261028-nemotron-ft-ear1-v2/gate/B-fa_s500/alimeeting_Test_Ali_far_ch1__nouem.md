# Diarization scores: B-fa_s500/alimeeting_Test_Ali_far_ch1__nouem

- name: `B-fa_s500/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-fa_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T21:55:41+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `B-fa_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7806-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.69 | 5.89 | 4.10 | 0.69 | 11.33 | 100.00 | 0.00 |
| 0.25 | 1.71 | 0.97 | 0.67 | 0.07 | 2.55 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.53 (IoU 95.32) | 1.81 (IoU 1.85) |
| silence | 2.19 (IoU 2.23) | 14.47 (IoU 78.35) |

Speech P/R/F1: 97.39 / 97.83 / 97.61; miss 2.17 of ref speech, FA 13.13 of ref silence, SAD error 4.80.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13095 | 12899 | 92.26 | 90.87 | 91.56 | 0.042 | 0.030 | 0.004 | 0.010 |
| 0.25 | offset | 13099 | 12897 | 92.58 | 91.15 | 91.86 | 0.048 | 0.040 | 0.014 | 0.020 |
| 0.25 | all | 26194 | 25796 | 92.42 | 91.01 | 91.71 | 0.045 | 0.030 | 0.009 | 0.010 |
| 0.50 | onset | 13095 | 12899 | 93.20 | 91.81 | 92.50 | 0.045 | 0.030 | 0.005 | 0.010 |
| 0.50 | offset | 13099 | 12897 | 93.29 | 91.85 | 92.57 | 0.050 | 0.040 | 0.014 | 0.020 |
| 0.50 | all | 26194 | 25796 | 93.25 | 91.83 | 92.53 | 0.047 | 0.030 | 0.010 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.04 | 11.33 | 1.19 | 1.40 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.96 | 12.81 | 2.07 | 3.40 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.67 | 9.95 | 1.32 | 1.69 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.88 | 22.47 | 5.48 | 7.69 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.54 | 19.73 | 3.02 | 3.36 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.46 | 7.54 | 1.76 | 1.93 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.18 | 19.40 | 8.06 | 7.93 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.26 | 10.87 | 2.03 | 2.24 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.38 | 8.05 | 0.76 | 0.90 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.67 | 11.04 | 1.74 | 1.96 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.91 | 10.59 | 1.35 | 2.31 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.30 | 6.22 | 0.51 | 0.67 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.56 | 8.12 | 0.45 | 0.45 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.06 | 6.65 | 0.87 | 1.07 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.94 | 10.66 | 0.65 | 0.76 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.74 | 4.63 | 0.40 | 0.40 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.55 | 7.11 | 0.63 | 0.57 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.48 | 8.23 | 0.83 | 0.94 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.49 | 5.27 | 1.43 | 1.36 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.60 | 7.16 | 2.92 | 2.74 | 2 | 2 |
