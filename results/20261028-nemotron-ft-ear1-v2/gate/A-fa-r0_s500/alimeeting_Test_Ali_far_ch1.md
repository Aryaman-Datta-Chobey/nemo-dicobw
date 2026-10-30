# Diarization scores: A-fa-r0_s500/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r0_s500/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T17:35:44+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r0_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7884-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.61 | 6.50 | 4.40 | 0.71 | 12.29 | 100.00 | 0.00 |
| 0.25 | 1.82 | 1.17 | 0.55 | 0.10 | 3.06 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.01 (IoU 94.76) | 1.99 (IoU 2.04) |
| silence | 2.49 (IoU 2.54) | 14.51 (IoU 76.40) |

Speech P/R/F1: 97.02 / 97.60 / 97.31; miss 2.40 of ref speech, FA 14.64 of ref silence, SAD error 5.40.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12932 | 91.49 | 90.30 | 90.89 | 0.046 | 0.040 | 0.019 | 0.020 |
| 0.25 | offset | 13103 | 12932 | 91.56 | 90.37 | 90.96 | 0.056 | 0.050 | 0.035 | 0.040 |
| 0.25 | all | 26206 | 25864 | 91.53 | 90.33 | 90.93 | 0.051 | 0.040 | 0.027 | 0.030 |
| 0.50 | onset | 13103 | 12932 | 92.34 | 91.14 | 91.74 | 0.048 | 0.040 | 0.019 | 0.020 |
| 0.50 | offset | 13103 | 12932 | 92.40 | 91.19 | 91.79 | 0.059 | 0.050 | 0.036 | 0.040 |
| 0.50 | all | 26206 | 25864 | 92.37 | 91.17 | 91.76 | 0.054 | 0.040 | 0.027 | 0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 12.71 | 12.96 | 1.16 | 1.36 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.82 | 13.72 | 2.03 | 3.42 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.81 | 10.17 | 1.48 | 1.99 | 4 | 4 |
| R8004_M8006__far_ch1 | 18.58 | 21.07 | 5.13 | 7.38 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.48 | 18.70 | 2.95 | 3.32 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.02 | 8.14 | 1.72 | 2.00 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.82 | 28.71 | 14.74 | 16.04 | 4 | 4 |
| R8006_M8012__far_ch1 | 11.27 | 11.85 | 2.43 | 2.74 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.52 | 8.16 | 0.71 | 0.84 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.27 | 11.64 | 1.90 | 2.22 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.02 | 11.62 | 1.17 | 2.18 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.78 | 6.65 | 0.56 | 0.73 | 3 | 3 |
| R8009_M8021__far_ch1 | 11.42 | 10.68 | 0.51 | 0.50 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.37 | 8.05 | 0.84 | 1.12 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.86 | 9.40 | 0.59 | 0.75 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.99 | 5.88 | 0.43 | 0.43 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.30 | 7.74 | 0.67 | 0.58 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.46 | 7.39 | 0.76 | 0.86 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.06 | 5.84 | 1.38 | 1.31 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.05 | 5.94 | 0.68 | 0.68 | 2 | 2 |
