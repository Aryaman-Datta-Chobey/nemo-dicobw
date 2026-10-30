# Diarization scores: B-fa_s750/alimeeting_Test_Ali_far_ch1__nouem

- name: `B-fa_s750/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-fa_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T22:06:42+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `B-fa_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7709-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.85 | 5.76 | 4.38 | 0.70 | 11.45 | 100.00 | 0.00 |
| 0.25 | 1.84 | 0.96 | 0.80 | 0.08 | 2.61 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.51 (IoU 95.17) | 1.83 (IoU 1.87) |
| silence | 2.30 (IoU 2.35) | 14.36 (IoU 77.64) |

Speech P/R/F1: 97.25 / 97.80 / 97.53; miss 2.20 of ref speech, FA 13.82 of ref silence, SAD error 4.96.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13095 | 12811 | 92.44 | 90.43 | 91.42 | 0.043 | 0.030 | 0.007 | 0.010 |
| 0.25 | offset | 13100 | 12807 | 92.79 | 90.71 | 91.74 | 0.050 | 0.040 | 0.020 | 0.020 |
| 0.25 | all | 26195 | 25618 | 92.61 | 90.57 | 91.58 | 0.047 | 0.040 | 0.014 | 0.020 |
| 0.50 | onset | 13095 | 12811 | 93.38 | 91.36 | 92.36 | 0.046 | 0.030 | 0.008 | 0.010 |
| 0.50 | offset | 13100 | 12807 | 93.55 | 91.46 | 92.49 | 0.053 | 0.040 | 0.020 | 0.020 |
| 0.50 | all | 26195 | 25618 | 93.47 | 91.41 | 92.42 | 0.049 | 0.040 | 0.014 | 0.020 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.33 | 11.60 | 1.19 | 1.41 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.22 | 13.09 | 2.12 | 3.53 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.63 | 9.85 | 1.35 | 1.71 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.50 | 22.01 | 5.50 | 7.60 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.80 | 19.00 | 2.94 | 3.32 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.51 | 7.56 | 1.68 | 1.85 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.93 | 19.11 | 7.95 | 7.79 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.43 | 11.03 | 2.11 | 2.32 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.52 | 8.13 | 0.76 | 0.90 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.14 | 11.63 | 1.83 | 2.17 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.34 | 10.93 | 1.35 | 2.30 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.61 | 6.50 | 0.48 | 0.68 | 3 | 3 |
| R8009_M8021__far_ch1 | 9.02 | 8.53 | 0.46 | 0.45 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.70 | 7.31 | 0.85 | 1.08 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.25 | 10.94 | 0.71 | 0.83 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.28 | 5.17 | 0.45 | 0.44 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.61 | 7.13 | 0.65 | 0.57 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.41 | 8.19 | 0.87 | 1.00 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.87 | 5.64 | 1.61 | 1.54 | 2 | 2 |
| R8009_M8028__far_ch1 | 9.23 | 8.43 | 4.86 | 4.39 | 2 | 2 |
