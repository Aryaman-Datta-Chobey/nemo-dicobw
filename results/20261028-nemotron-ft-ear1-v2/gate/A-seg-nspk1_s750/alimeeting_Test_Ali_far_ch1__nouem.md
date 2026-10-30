# Diarization scores: A-seg-nspk1_s750/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-seg-nspk1_s750/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T02:12:29+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-seg-nspk1_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8409-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.01 | 5.24 | 6.03 | 0.74 | 12.49 | 100.00 | 0.00 |
| 0.25 | 2.13 | 0.96 | 1.10 | 0.06 | 2.76 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.43 (IoU 94.30) | 1.89 (IoU 1.95) |
| silence | 3.03 (IoU 3.09) | 13.65 (IoU 73.52) |

Speech P/R/F1: 96.41 / 97.73 / 97.07; miss 2.27 of ref speech, FA 18.15 of ref silence, SAD error 5.90.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13099 | 12059 | 93.19 | 85.79 | 89.34 | 0.049 | 0.040 | -0.009 | -0.010 |
| 0.25 | offset | 13096 | 12062 | 92.81 | 85.48 | 89.00 | 0.058 | 0.050 | 0.019 | 0.020 |
| 0.25 | all | 26195 | 24121 | 93.00 | 85.64 | 89.17 | 0.054 | 0.040 | 0.005 | 0.010 |
| 0.50 | onset | 13099 | 12059 | 94.29 | 86.80 | 90.39 | 0.052 | 0.040 | -0.008 | -0.010 |
| 0.50 | offset | 13096 | 12062 | 94.50 | 87.03 | 90.61 | 0.063 | 0.050 | 0.022 | 0.020 |
| 0.50 | all | 26195 | 24121 | 94.39 | 86.92 | 90.50 | 0.058 | 0.040 | 0.007 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.96 | 11.19 | 1.74 | 1.91 | 4 | 4 |
| R8002_M8003__far_ch1 | 13.82 | 14.69 | 1.74 | 2.96 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.21 | 10.37 | 1.30 | 1.66 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.78 | 21.90 | 4.94 | 7.13 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.64 | 19.64 | 2.83 | 3.16 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.60 | 7.55 | 1.53 | 1.65 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.31 | 19.28 | 8.72 | 8.21 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.65 | 11.08 | 2.17 | 2.30 | 4 | 4 |
| R8008_M8014__far_ch1 | 8.12 | 8.69 | 0.60 | 0.74 | 3 | 3 |
| R8008_M8015__far_ch1 | 15.31 | 15.56 | 1.59 | 1.89 | 3 | 3 |
| R8008_M8016__far_ch1 | 10.37 | 12.83 | 1.59 | 2.71 | 3 | 3 |
| R8008_M8017__far_ch1 | 14.18 | 13.48 | 1.39 | 1.41 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.87 | 8.46 | 0.79 | 0.78 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.47 | 7.12 | 1.34 | 1.60 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.52 | 12.84 | 1.41 | 1.61 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.85 | 4.79 | 0.91 | 0.91 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.43 | 8.05 | 0.92 | 0.84 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.84 | 8.66 | 1.09 | 1.25 | 2 | 2 |
| R8009_M8027__far_ch1 | 7.09 | 6.82 | 1.63 | 1.61 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.10 | 10.65 | 6.88 | 6.00 | 2 | 2 |
