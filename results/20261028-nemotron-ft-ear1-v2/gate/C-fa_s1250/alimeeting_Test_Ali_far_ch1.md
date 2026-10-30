# Diarization scores: C-fa_s1250/alimeeting_Test_Ali_far_ch1

- name: `C-fa_s1250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-fa_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T23:40:59+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `C-fa_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7683-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.73 | 5.43 | 4.59 | 0.71 | 11.33 | 100.00 | 0.00 |
| 0.25 | 1.75 | 0.92 | 0.76 | 0.07 | 2.50 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.24 (IoU 95.18) | 1.77 (IoU 1.81) |
| silence | 2.35 (IoU 2.39) | 14.64 (IoU 78.06) |

Speech P/R/F1: 97.19 / 97.87 / 97.53; miss 2.13 of ref speech, FA 13.82 of ref silence, SAD error 4.96.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12651 | 92.97 | 89.77 | 91.34 | 0.042 | 0.030 | -0.001 | 0.000 |
| 0.25 | offset | 13103 | 12651 | 93.34 | 90.12 | 91.71 | 0.050 | 0.040 | 0.017 | 0.020 |
| 0.25 | all | 26206 | 25302 | 93.16 | 89.95 | 91.52 | 0.046 | 0.040 | 0.008 | 0.010 |
| 0.50 | onset | 13103 | 12651 | 94.06 | 90.81 | 92.41 | 0.046 | 0.030 | 0.000 | 0.000 |
| 0.50 | offset | 13103 | 12651 | 94.21 | 90.96 | 92.55 | 0.053 | 0.040 | 0.017 | 0.020 |
| 0.50 | all | 26206 | 25302 | 94.13 | 90.88 | 92.48 | 0.049 | 0.040 | 0.009 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.20 | 11.44 | 1.15 | 1.39 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.78 | 12.51 | 1.77 | 2.90 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.67 | 9.89 | 1.36 | 1.74 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.14 | 21.62 | 5.25 | 7.54 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.43 | 18.59 | 2.82 | 3.18 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.46 | 7.47 | 1.57 | 1.70 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.76 | 18.89 | 7.83 | 7.59 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.60 | 11.08 | 2.24 | 2.33 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.41 | 8.07 | 0.75 | 0.85 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.92 | 11.38 | 1.72 | 1.94 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.40 | 10.93 | 1.26 | 2.22 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.74 | 6.60 | 0.56 | 0.74 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.05 | 7.64 | 0.49 | 0.48 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.74 | 7.34 | 0.86 | 1.07 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.71 | 11.70 | 0.75 | 0.89 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.84 | 4.73 | 0.47 | 0.47 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.53 | 7.06 | 0.73 | 0.64 | 2 | 2 |
| R8009_M8026__far_ch1 | 9.09 | 8.81 | 0.90 | 1.02 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.60 | 6.36 | 1.86 | 1.79 | 2 | 2 |
| R8009_M8028__far_ch1 | 8.35 | 7.73 | 3.60 | 3.34 | 2 | 2 |
