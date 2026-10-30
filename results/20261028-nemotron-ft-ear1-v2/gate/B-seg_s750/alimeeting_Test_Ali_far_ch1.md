# Diarization scores: B-seg_s750/alimeeting_Test_Ali_far_ch1

- name: `B-seg_s750/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-seg_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T16:48:59+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `B-seg_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8297-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.53 | 4.62 | 7.17 | 0.74 | 12.95 | 100.00 | 0.00 |
| 0.25 | 2.02 | 0.78 | 1.16 | 0.08 | 2.79 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.51 (IoU 93.80) | 1.50 (IoU 1.56) |
| silence | 3.89 (IoU 3.94) | 13.11 (IoU 70.88) |

Speech P/R/F1: 95.45 / 98.19 / 96.80; miss 1.81 of ref speech, FA 22.86 of ref silence, SAD error 6.49.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 11555 | 93.00 | 82.01 | 87.16 | 0.053 | 0.040 | -0.017 | -0.010 |
| 0.25 | offset | 13103 | 11557 | 92.00 | 81.14 | 86.23 | 0.061 | 0.050 | 0.024 | 0.020 |
| 0.25 | all | 26206 | 23112 | 92.50 | 81.58 | 86.69 | 0.057 | 0.040 | 0.004 | 0.010 |
| 0.50 | onset | 13103 | 11555 | 94.23 | 83.10 | 88.31 | 0.057 | 0.040 | -0.017 | -0.010 |
| 0.50 | offset | 13103 | 11557 | 94.25 | 83.13 | 88.35 | 0.067 | 0.050 | 0.029 | 0.030 |
| 0.50 | all | 26206 | 23112 | 94.24 | 83.11 | 88.33 | 0.062 | 0.050 | 0.006 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.19 | 11.41 | 1.22 | 1.47 | 4 | 4 |
| R8002_M8003__far_ch1 | 15.51 | 16.20 | 3.58 | 4.82 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.07 | 10.21 | 1.39 | 1.73 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.90 | 21.90 | 5.33 | 7.85 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.25 | 19.26 | 2.83 | 3.18 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.80 | 7.70 | 1.53 | 1.66 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.62 | 18.54 | 7.69 | 7.42 | 4 | 4 |
| R8006_M8012__far_ch1 | 11.21 | 11.60 | 2.42 | 2.57 | 4 | 4 |
| R8008_M8014__far_ch1 | 9.22 | 9.70 | 0.61 | 0.71 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.30 | 20.19 | 2.08 | 2.48 | 3 | 3 |
| R8008_M8016__far_ch1 | 11.32 | 13.64 | 1.38 | 2.40 | 3 | 3 |
| R8008_M8017__far_ch1 | 18.18 | 16.37 | 1.25 | 1.30 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.26 | 7.84 | 0.57 | 0.57 | 2 | 2 |
| R8009_M8022__far_ch1 | 5.57 | 6.17 | 1.05 | 1.36 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.69 | 11.74 | 1.21 | 1.23 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.65 | 4.54 | 0.63 | 0.62 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.55 | 7.30 | 1.08 | 1.11 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.92 | 7.63 | 0.92 | 1.08 | 2 | 2 |
| R8009_M8027__far_ch1 | 12.81 | 11.17 | 1.83 | 1.70 | 2 | 2 |
| R8009_M8028__far_ch1 | 9.62 | 8.65 | 4.84 | 4.37 | 2 | 2 |
