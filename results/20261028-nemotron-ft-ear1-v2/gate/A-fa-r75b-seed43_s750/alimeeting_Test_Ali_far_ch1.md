# Diarization scores: A-fa-r75b-seed43_s750/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r75b-seed43_s750/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T07:00:05+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r75b-seed43_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7766-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.56 | 5.60 | 4.25 | 0.71 | 11.19 | 100.00 | 0.00 |
| 0.25 | 1.70 | 1.03 | 0.60 | 0.07 | 2.48 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 80.97 (IoU 95.30) | 2.04 (IoU 2.08) |
| silence | 1.96 (IoU 2.00) | 15.04 (IoU 79.01) |

Speech P/R/F1: 97.64 / 97.55 / 97.59; miss 2.45 of ref speech, FA 11.52 of ref silence, SAD error 4.81.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12791 | 92.65 | 90.44 | 91.53 | 0.042 | 0.030 | 0.004 | 0.010 |
| 0.25 | offset | 13103 | 12792 | 92.77 | 90.57 | 91.65 | 0.045 | 0.030 | 0.005 | 0.010 |
| 0.25 | all | 26206 | 25583 | 92.71 | 90.51 | 91.59 | 0.044 | 0.030 | 0.005 | 0.010 |
| 0.50 | onset | 13103 | 12791 | 93.53 | 91.30 | 92.40 | 0.045 | 0.030 | 0.005 | 0.010 |
| 0.50 | offset | 13103 | 12792 | 93.65 | 91.43 | 92.53 | 0.048 | 0.030 | 0.005 | 0.010 |
| 0.50 | all | 26206 | 25583 | 93.59 | 91.36 | 92.46 | 0.046 | 0.030 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.34 | 10.61 | 1.10 | 1.31 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.72 | 12.38 | 1.80 | 2.92 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.00 | 10.19 | 1.34 | 1.71 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.54 | 21.79 | 5.12 | 7.34 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.49 | 19.47 | 2.79 | 3.02 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.24 | 7.28 | 1.58 | 1.69 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.99 | 18.97 | 7.78 | 7.53 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.12 | 10.70 | 1.97 | 2.13 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.88 | 7.61 | 0.81 | 0.95 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.76 | 11.26 | 2.04 | 2.39 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.78 | 10.43 | 1.35 | 2.39 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.26 | 6.24 | 0.62 | 0.84 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.40 | 8.03 | 0.75 | 0.73 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.74 | 7.44 | 1.21 | 1.48 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.17 | 12.68 | 1.06 | 1.36 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.47 | 4.40 | 0.86 | 0.87 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.99 | 6.73 | 0.73 | 0.63 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.23 | 8.10 | 1.03 | 1.16 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.09 | 5.95 | 1.83 | 1.77 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.33 | 6.21 | 1.39 | 1.37 | 2 | 2 |
