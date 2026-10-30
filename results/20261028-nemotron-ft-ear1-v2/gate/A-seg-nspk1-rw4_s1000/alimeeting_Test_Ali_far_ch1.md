# Diarization scores: A-seg-nspk1-rw4_s1000/alimeeting_Test_Ali_far_ch1

- name: `A-seg-nspk1-rw4_s1000/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1-rw4_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T04:18:54+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-seg-nspk1-rw4_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1-rw4/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8374-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.49 | 5.32 | 6.37 | 0.80 | 13.02 | 95.00 | 0.05 |
| 0.25 | 1.99 | 0.95 | 0.90 | 0.14 | 2.74 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.19 (IoU 94.04) | 1.82 (IoU 1.88) |
| silence | 3.33 (IoU 3.39) | 13.67 (IoU 72.65) |

Speech P/R/F1: 96.06 / 97.81 / 96.93; miss 2.19 of ref speech, FA 19.58 of ref silence, SAD error 6.20.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 11906 | 93.03 | 84.53 | 88.58 | 0.051 | 0.040 | -0.015 | -0.010 |
| 0.25 | offset | 13103 | 11906 | 92.39 | 83.95 | 87.97 | 0.064 | 0.050 | 0.020 | 0.020 |
| 0.25 | all | 26206 | 23812 | 92.71 | 84.24 | 88.27 | 0.058 | 0.040 | 0.003 | 0.000 |
| 0.50 | onset | 13103 | 11906 | 94.11 | 85.51 | 89.61 | 0.055 | 0.040 | -0.014 | -0.010 |
| 0.50 | offset | 13103 | 11906 | 94.25 | 85.64 | 89.74 | 0.069 | 0.050 | 0.023 | 0.020 |
| 0.50 | all | 26206 | 23812 | 94.18 | 85.58 | 89.68 | 0.062 | 0.050 | 0.005 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.30 | 10.64 | 1.20 | 1.47 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.34 | 17.51 | 2.06 | 3.49 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.52 | 10.70 | 1.38 | 1.71 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.10 | 22.29 | 5.16 | 7.16 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.90 | 19.81 | 2.76 | 2.94 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.68 | 7.68 | 1.59 | 1.71 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.44 | 19.60 | 8.11 | 7.99 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.50 | 10.99 | 2.22 | 2.39 | 4 | 4 |
| R8008_M8014__far_ch1 | 8.38 | 8.98 | 0.56 | 0.69 | 3 | 3 |
| R8008_M8015__far_ch1 | 18.98 | 18.09 | 1.43 | 1.72 | 3 | 4 |
| R8008_M8016__far_ch1 | 12.43 | 14.58 | 1.46 | 2.75 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.60 | 14.58 | 1.00 | 1.10 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.17 | 7.81 | 0.71 | 0.70 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.21 | 6.86 | 1.32 | 1.59 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.61 | 13.00 | 1.12 | 1.42 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.60 | 5.53 | 1.48 | 1.48 | 2 | 2 |
| R8009_M8025__far_ch1 | 9.16 | 9.94 | 1.91 | 3.47 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.56 | 8.31 | 0.78 | 0.90 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.97 | 6.74 | 1.62 | 1.59 | 2 | 2 |
| R8009_M8028__far_ch1 | 10.74 | 9.67 | 4.50 | 4.10 | 2 | 2 |
