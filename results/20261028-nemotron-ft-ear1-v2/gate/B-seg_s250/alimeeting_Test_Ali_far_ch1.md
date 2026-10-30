# Diarization scores: B-seg_s250/alimeeting_Test_Ali_far_ch1

- name: `B-seg_s250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-seg_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T16:26:43+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `B-seg_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8070-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.53 | 4.35 | 7.43 | 0.75 | 12.92 | 100.00 | 0.00 |
| 0.25 | 1.62 | 0.62 | 0.94 | 0.07 | 2.54 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.80 (IoU 93.92) | 1.21 (IoU 1.26) |
| silence | 4.09 (IoU 4.14) | 12.90 (IoU 70.88) |

Speech P/R/F1: 95.24 / 98.55 / 96.86; miss 1.45 of ref speech, FA 24.08 of ref silence, SAD error 6.38.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 11472 | 93.70 | 82.03 | 87.48 | 0.058 | 0.050 | -0.025 | -0.020 |
| 0.25 | offset | 13103 | 11474 | 92.70 | 81.17 | 86.55 | 0.059 | 0.050 | 0.025 | 0.020 |
| 0.25 | all | 26206 | 22946 | 93.20 | 81.60 | 87.02 | 0.059 | 0.050 | -0.000 | 0.000 |
| 0.50 | onset | 13103 | 11472 | 94.87 | 83.06 | 88.58 | 0.062 | 0.050 | -0.027 | -0.020 |
| 0.50 | offset | 13103 | 11474 | 94.87 | 83.07 | 88.58 | 0.065 | 0.050 | 0.030 | 0.030 |
| 0.50 | all | 26206 | 22946 | 94.87 | 83.07 | 88.58 | 0.063 | 0.050 | 0.002 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.17 | 10.39 | 1.08 | 1.30 | 4 | 4 |
| R8002_M8003__far_ch1 | 13.38 | 14.19 | 2.58 | 4.19 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.48 | 10.57 | 1.34 | 1.68 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.67 | 22.61 | 5.29 | 7.61 | 4 | 4 |
| R8005_M8007__far_ch1 | 20.35 | 20.10 | 2.60 | 2.85 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.54 | 8.40 | 1.59 | 1.71 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.82 | 18.60 | 7.67 | 7.35 | 4 | 4 |
| R8006_M8012__far_ch1 | 14.96 | 14.88 | 3.59 | 3.75 | 4 | 4 |
| R8008_M8014__far_ch1 | 13.18 | 13.02 | 0.69 | 0.83 | 3 | 3 |
| R8008_M8015__far_ch1 | 24.09 | 21.33 | 2.19 | 2.63 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.46 | 11.91 | 1.07 | 2.04 | 3 | 3 |
| R8008_M8017__far_ch1 | 13.03 | 12.59 | 0.59 | 0.69 | 3 | 3 |
| R8009_M8021__far_ch1 | 9.28 | 8.75 | 0.55 | 0.55 | 2 | 2 |
| R8009_M8022__far_ch1 | 5.17 | 5.78 | 0.77 | 1.04 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.98 | 10.97 | 0.61 | 0.75 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.45 | 4.32 | 0.47 | 0.47 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.87 | 6.53 | 0.51 | 0.44 | 2 | 2 |
| R8009_M8026__far_ch1 | 6.76 | 6.47 | 0.57 | 0.64 | 2 | 2 |
| R8009_M8027__far_ch1 | 12.66 | 10.82 | 1.49 | 1.36 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.32 | 6.05 | 0.67 | 0.67 | 2 | 2 |
