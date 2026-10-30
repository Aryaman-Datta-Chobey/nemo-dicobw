# Diarization scores: C-seg_s1250/alimeeting_Test_Ali_far_ch1

- name: `C-seg_s1250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-seg_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T18:23:46+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `C-seg_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8074-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.78 | 4.94 | 6.13 | 0.71 | 12.28 | 100.00 | 0.00 |
| 0.25 | 1.90 | 0.91 | 0.92 | 0.07 | 2.62 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.21 (IoU 94.38) | 1.80 (IoU 1.86) |
| silence | 3.04 (IoU 3.10) | 13.95 (IoU 74.25) |

Speech P/R/F1: 96.39 / 97.83 / 97.11; miss 2.17 of ref speech, FA 17.89 of ref silence, SAD error 5.83.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12088 | 92.94 | 85.74 | 89.20 | 0.050 | 0.040 | -0.009 | 0.000 |
| 0.25 | offset | 13103 | 12089 | 92.81 | 85.63 | 89.08 | 0.055 | 0.040 | 0.018 | 0.020 |
| 0.25 | all | 26206 | 24177 | 92.88 | 85.69 | 89.14 | 0.053 | 0.040 | 0.005 | 0.010 |
| 0.50 | onset | 13103 | 12088 | 94.01 | 86.73 | 90.22 | 0.053 | 0.040 | -0.008 | 0.000 |
| 0.50 | offset | 13103 | 12089 | 94.20 | 86.91 | 90.41 | 0.060 | 0.040 | 0.020 | 0.020 |
| 0.50 | all | 26206 | 24177 | 94.11 | 86.82 | 90.32 | 0.057 | 0.040 | 0.006 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.21 | 11.49 | 1.27 | 1.52 | 4 | 4 |
| R8002_M8003__far_ch1 | 12.99 | 13.98 | 1.99 | 3.21 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.25 | 10.37 | 1.36 | 1.67 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.66 | 21.56 | 5.22 | 7.57 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.31 | 19.28 | 2.85 | 3.20 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.48 | 7.46 | 1.57 | 1.69 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.83 | 18.72 | 7.68 | 7.48 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.85 | 11.33 | 2.50 | 2.59 | 4 | 4 |
| R8008_M8014__far_ch1 | 8.14 | 8.86 | 0.73 | 0.87 | 3 | 3 |
| R8008_M8015__far_ch1 | 19.48 | 18.15 | 1.52 | 1.81 | 3 | 3 |
| R8008_M8016__far_ch1 | 10.63 | 12.90 | 1.34 | 2.39 | 3 | 3 |
| R8008_M8017__far_ch1 | 13.12 | 12.69 | 0.70 | 0.87 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.92 | 7.56 | 0.68 | 0.67 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.38 | 6.97 | 1.19 | 1.46 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.79 | 11.67 | 1.35 | 1.40 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.64 | 4.55 | 0.78 | 0.78 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.39 | 7.10 | 0.89 | 0.80 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.12 | 7.87 | 1.00 | 1.17 | 2 | 2 |
| R8009_M8027__far_ch1 | 7.54 | 7.09 | 1.74 | 1.70 | 2 | 2 |
| R8009_M8028__far_ch1 | 8.94 | 8.31 | 4.25 | 3.92 | 2 | 2 |
