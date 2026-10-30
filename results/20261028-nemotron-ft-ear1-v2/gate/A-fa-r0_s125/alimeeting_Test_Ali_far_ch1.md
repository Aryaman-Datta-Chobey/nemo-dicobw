# Diarization scores: A-fa-r0_s125/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r0_s125/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s125/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T17:02:30+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r0_s125`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7689-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.73 | 5.92 | 4.11 | 0.70 | 11.30 | 100.00 | 0.00 |
| 0.25 | 1.54 | 0.96 | 0.52 | 0.06 | 2.35 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.15 (IoU 95.40) | 1.86 (IoU 1.90) |
| silence | 2.05 (IoU 2.09) | 14.94 (IoU 79.26) |

Speech P/R/F1: 97.54 / 97.76 / 97.65; miss 2.24 of ref speech, FA 12.06 of ref silence, SAD error 4.71.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 13031 | 91.90 | 91.39 | 91.64 | 0.042 | 0.030 | -0.008 | 0.000 |
| 0.25 | offset | 13103 | 13031 | 92.16 | 91.66 | 91.91 | 0.045 | 0.030 | -0.002 | 0.000 |
| 0.25 | all | 26206 | 26062 | 92.03 | 91.52 | 91.78 | 0.044 | 0.030 | -0.005 | 0.000 |
| 0.50 | onset | 13103 | 13031 | 92.89 | 92.38 | 92.63 | 0.046 | 0.030 | -0.008 | 0.000 |
| 0.50 | offset | 13103 | 13031 | 92.98 | 92.47 | 92.72 | 0.048 | 0.030 | -0.002 | 0.000 |
| 0.50 | all | 26206 | 26062 | 92.93 | 92.42 | 92.68 | 0.047 | 0.030 | -0.005 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 8.49 | 8.83 | 1.17 | 1.38 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.76 | 12.32 | 1.72 | 2.76 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.86 | 11.07 | 1.25 | 1.60 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.64 | 24.23 | 5.15 | 7.25 | 4 | 4 |
| R8005_M8007__far_ch1 | 21.55 | 21.47 | 2.96 | 3.17 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.19 | 8.24 | 1.77 | 1.85 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.73 | 19.71 | 8.02 | 7.83 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.24 | 10.73 | 1.69 | 1.86 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.92 | 7.62 | 0.66 | 0.78 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.23 | 10.25 | 1.72 | 1.97 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.44 | 9.94 | 1.21 | 2.18 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.28 | 6.14 | 0.45 | 0.56 | 3 | 3 |
| R8009_M8021__far_ch1 | 6.82 | 6.52 | 0.52 | 0.51 | 2 | 2 |
| R8009_M8022__far_ch1 | 5.41 | 6.01 | 0.95 | 1.16 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.99 | 12.30 | 0.76 | 0.93 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.39 | 4.30 | 0.53 | 0.53 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.17 | 6.90 | 0.65 | 0.61 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.07 | 7.85 | 0.79 | 0.90 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.43 | 5.22 | 1.27 | 1.21 | 2 | 2 |
| R8009_M8028__far_ch1 | 5.99 | 5.82 | 0.88 | 0.88 | 2 | 2 |
