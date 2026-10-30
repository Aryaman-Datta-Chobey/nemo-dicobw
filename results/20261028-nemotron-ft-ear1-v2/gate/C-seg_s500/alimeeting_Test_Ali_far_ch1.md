# Diarization scores: C-seg_s500/alimeeting_Test_Ali_far_ch1

- name: `C-seg_s500/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-seg_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T17:50:42+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `C-seg_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8201-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.14 | 4.52 | 6.85 | 0.78 | 12.66 | 100.00 | 0.00 |
| 0.25 | 1.88 | 0.75 | 1.01 | 0.11 | 2.86 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.55 (IoU 94.03) | 1.46 (IoU 1.52) |
| silence | 3.72 (IoU 3.77) | 13.27 (IoU 71.93) |

Speech P/R/F1: 95.64 / 98.24 / 96.92; miss 1.76 of ref speech, FA 21.89 of ref silence, SAD error 6.24.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 11726 | 93.19 | 83.40 | 88.03 | 0.054 | 0.040 | -0.018 | -0.010 |
| 0.25 | offset | 13103 | 11728 | 92.56 | 82.84 | 87.43 | 0.056 | 0.040 | 0.021 | 0.020 |
| 0.25 | all | 26206 | 23454 | 92.88 | 83.12 | 87.73 | 0.055 | 0.040 | 0.001 | 0.010 |
| 0.50 | onset | 13103 | 11726 | 94.50 | 84.57 | 89.26 | 0.058 | 0.040 | -0.020 | -0.010 |
| 0.50 | offset | 13103 | 11728 | 94.50 | 84.58 | 89.27 | 0.062 | 0.040 | 0.025 | 0.020 |
| 0.50 | all | 26206 | 23454 | 94.50 | 84.58 | 89.26 | 0.060 | 0.040 | 0.003 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.06 | 11.28 | 1.15 | 1.40 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.88 | 13.86 | 3.36 | 6.09 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.20 | 10.32 | 1.43 | 1.77 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.84 | 21.87 | 5.39 | 8.02 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.34 | 19.33 | 2.84 | 3.17 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.49 | 7.47 | 1.55 | 1.65 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.58 | 18.54 | 7.61 | 7.43 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.87 | 11.24 | 2.47 | 2.56 | 4 | 4 |
| R8008_M8014__far_ch1 | 9.45 | 9.87 | 0.54 | 0.62 | 3 | 3 |
| R8008_M8015__far_ch1 | 23.64 | 21.62 | 2.83 | 3.91 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.65 | 12.10 | 1.32 | 2.28 | 3 | 3 |
| R8008_M8017__far_ch1 | 18.14 | 16.24 | 1.09 | 1.12 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.21 | 7.78 | 0.56 | 0.55 | 2 | 2 |
| R8009_M8022__far_ch1 | 5.62 | 6.22 | 1.08 | 1.44 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.49 | 11.52 | 1.21 | 1.23 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.60 | 4.48 | 0.65 | 0.65 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.53 | 7.15 | 0.84 | 0.73 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.36 | 7.13 | 0.82 | 0.96 | 2 | 2 |
| R8009_M8027__far_ch1 | 12.06 | 10.52 | 1.61 | 1.50 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.81 | 7.29 | 2.68 | 2.53 | 2 | 2 |
