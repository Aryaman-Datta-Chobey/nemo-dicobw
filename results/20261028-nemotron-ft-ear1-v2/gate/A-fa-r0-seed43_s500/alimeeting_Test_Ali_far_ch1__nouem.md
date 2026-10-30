# Diarization scores: A-fa-r0-seed43_s500/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r0-seed43_s500/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T19:00:45+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r0-seed43_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7953-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.17 | 7.12 | 4.34 | 0.71 | 12.76 | 100.00 | 0.00 |
| 0.25 | 2.10 | 1.48 | 0.52 | 0.10 | 3.36 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 80.96 (IoU 94.31) | 2.40 (IoU 2.46) |
| silence | 2.49 (IoU 2.55) | 14.16 (IoU 74.34) |

Speech P/R/F1: 97.02 / 97.12 / 97.07; miss 2.88 of ref speech, FA 14.93 of ref silence, SAD error 5.86.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13092 | 13212 | 89.40 | 90.22 | 89.80 | 0.047 | 0.040 | 0.020 | 0.020 |
| 0.25 | offset | 13099 | 13205 | 89.65 | 90.37 | 90.01 | 0.057 | 0.050 | 0.035 | 0.040 |
| 0.25 | all | 26191 | 26417 | 89.52 | 90.29 | 89.91 | 0.052 | 0.040 | 0.027 | 0.030 |
| 0.50 | onset | 13092 | 13212 | 90.34 | 91.17 | 90.75 | 0.051 | 0.040 | 0.021 | 0.020 |
| 0.50 | offset | 13099 | 13205 | 90.47 | 91.21 | 90.84 | 0.060 | 0.050 | 0.036 | 0.040 |
| 0.50 | all | 26191 | 26417 | 90.41 | 91.19 | 90.80 | 0.055 | 0.040 | 0.028 | 0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 12.75 | 13.15 | 1.34 | 1.63 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.54 | 13.31 | 1.97 | 3.30 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.18 | 10.42 | 1.65 | 1.97 | 4 | 4 |
| R8004_M8006__far_ch1 | 18.76 | 21.13 | 4.97 | 7.01 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.65 | 18.82 | 3.03 | 3.41 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.03 | 8.14 | 1.82 | 2.07 | 4 | 4 |
| R8005_M8009__far_ch1 | 32.30 | 32.37 | 18.00 | 18.45 | 4 | 4 |
| R8006_M8012__far_ch1 | 12.71 | 13.50 | 3.73 | 4.36 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.66 | 8.38 | 0.73 | 0.88 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.99 | 11.12 | 1.74 | 1.94 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.43 | 12.08 | 1.35 | 2.31 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.74 | 6.62 | 0.54 | 0.73 | 3 | 3 |
| R8009_M8021__far_ch1 | 11.63 | 10.89 | 0.54 | 0.53 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.22 | 7.88 | 0.85 | 1.12 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.23 | 9.59 | 0.63 | 0.82 | 2 | 2 |
| R8009_M8024__far_ch1 | 7.78 | 7.61 | 1.38 | 1.38 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.71 | 8.18 | 1.03 | 0.95 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.47 | 7.44 | 0.75 | 0.84 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.38 | 6.16 | 1.47 | 1.41 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.17 | 6.06 | 0.74 | 0.74 | 2 | 2 |
