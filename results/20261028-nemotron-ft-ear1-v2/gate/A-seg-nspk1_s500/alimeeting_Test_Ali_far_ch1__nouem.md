# Diarization scores: A-seg-nspk1_s500/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-seg-nspk1_s500/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T02:02:54+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-seg-nspk1_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8078-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.84 | 4.91 | 6.21 | 0.73 | 12.32 | 100.00 | 0.00 |
| 0.25 | 1.87 | 0.84 | 0.96 | 0.06 | 2.57 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.62 (IoU 94.36) | 1.71 (IoU 1.77) |
| silence | 3.17 (IoU 3.23) | 13.50 (IoU 73.44) |

Speech P/R/F1: 96.26 / 97.95 / 97.10; miss 2.05 of ref speech, FA 19.02 of ref silence, SAD error 5.86.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13100 | 11855 | 93.77 | 84.85 | 89.09 | 0.050 | 0.040 | -0.011 | -0.010 |
| 0.25 | offset | 13097 | 11858 | 93.45 | 84.61 | 88.81 | 0.056 | 0.040 | 0.020 | 0.020 |
| 0.25 | all | 26197 | 23713 | 93.61 | 84.73 | 88.95 | 0.053 | 0.040 | 0.004 | 0.010 |
| 0.50 | onset | 13100 | 11855 | 94.85 | 85.84 | 90.12 | 0.054 | 0.040 | -0.011 | -0.010 |
| 0.50 | offset | 13097 | 11858 | 95.00 | 86.01 | 90.28 | 0.061 | 0.050 | 0.023 | 0.020 |
| 0.50 | all | 26197 | 23713 | 94.93 | 85.93 | 90.20 | 0.057 | 0.040 | 0.006 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.80 | 11.07 | 1.34 | 1.65 | 4 | 4 |
| R8002_M8003__far_ch1 | 12.57 | 13.66 | 1.96 | 3.31 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.08 | 10.25 | 1.33 | 1.64 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.56 | 21.57 | 4.97 | 7.14 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.43 | 19.39 | 2.69 | 3.01 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.66 | 7.59 | 1.52 | 1.64 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.69 | 18.74 | 7.53 | 7.31 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.85 | 11.29 | 2.38 | 2.57 | 4 | 4 |
| R8008_M8014__far_ch1 | 8.89 | 9.40 | 0.50 | 0.59 | 3 | 3 |
| R8008_M8015__far_ch1 | 19.89 | 18.79 | 1.59 | 1.95 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.28 | 11.66 | 1.39 | 2.46 | 3 | 3 |
| R8008_M8017__far_ch1 | 13.55 | 12.85 | 0.92 | 0.92 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.96 | 8.51 | 0.67 | 0.66 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.16 | 6.78 | 1.16 | 1.40 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.31 | 11.37 | 1.13 | 1.27 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.59 | 4.52 | 0.68 | 0.68 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.12 | 7.77 | 0.93 | 0.83 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.50 | 8.30 | 1.01 | 1.16 | 2 | 2 |
| R8009_M8027__far_ch1 | 7.68 | 7.24 | 1.43 | 1.40 | 2 | 2 |
| R8009_M8028__far_ch1 | 9.70 | 8.80 | 4.71 | 4.28 | 2 | 2 |
