# Diarization scores: epoch=0/alimeeting_Test_Ali_far_ch1

- name: `epoch=0/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/epoch=0/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:43:30+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `epoch=0`
- model: `/mnt/data/exp/nemotron/20261027-nemotron-ft-ear1-nospkw/nemotron_ft_ear1_nospkw/checkpoints/nemotron_ft_ear1_nospkw--val_f1_acc=0.8201-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 13.25 | 3.95 | 8.53 | 0.77 | 13.48 | 100.00 | 0.00 |
| 0.25 | 1.64 | 0.54 | 1.03 | 0.07 | 2.47 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.93 (IoU 93.31) | 1.08 (IoU 1.13) |
| silence | 4.80 (IoU 4.85) | 12.19 (IoU 67.47) |

Speech P/R/F1: 94.46 / 98.70 / 96.54; miss 1.30 of ref speech, FA 28.25 of ref silence, SAD error 7.08.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 10793 | 94.14 | 77.55 | 85.04 | 0.060 | 0.050 | -0.026 | -0.020 |
| 0.25 | offset | 13103 | 10795 | 93.02 | 76.64 | 84.04 | 0.067 | 0.060 | 0.041 | 0.040 |
| 0.25 | all | 26206 | 21588 | 93.58 | 77.09 | 84.54 | 0.064 | 0.050 | 0.008 | 0.010 |
| 0.50 | onset | 13103 | 10793 | 95.52 | 78.68 | 86.28 | 0.064 | 0.050 | -0.028 | -0.020 |
| 0.50 | offset | 13103 | 10795 | 95.45 | 78.64 | 86.23 | 0.074 | 0.060 | 0.047 | 0.040 |
| 0.50 | all | 26206 | 21588 | 95.48 | 78.66 | 86.26 | 0.069 | 0.050 | 0.010 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.51 | 10.62 | 1.29 | 1.40 | 4 | 4 |
| R8002_M8003__far_ch1 | 15.69 | 16.41 | 2.11 | 3.42 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.32 | 10.43 | 1.35 | 1.71 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.13 | 21.98 | 4.92 | 7.35 | 4 | 4 |
| R8005_M8007__far_ch1 | 20.61 | 20.33 | 2.66 | 2.97 | 4 | 4 |
| R8005_M8008__far_ch1 | 10.28 | 9.79 | 1.81 | 1.92 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.66 | 18.46 | 7.53 | 7.20 | 4 | 4 |
| R8006_M8012__far_ch1 | 14.60 | 14.39 | 3.02 | 3.16 | 4 | 4 |
| R8008_M8014__far_ch1 | 13.53 | 13.15 | 0.41 | 0.50 | 3 | 3 |
| R8008_M8015__far_ch1 | 24.14 | 21.40 | 1.91 | 2.39 | 3 | 3 |
| R8008_M8016__far_ch1 | 11.28 | 13.37 | 1.01 | 2.00 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.23 | 14.04 | 0.60 | 0.61 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.94 | 8.40 | 0.54 | 0.53 | 2 | 2 |
| R8009_M8022__far_ch1 | 5.52 | 6.14 | 0.91 | 1.26 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.64 | 10.21 | 0.77 | 0.89 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.94 | 4.83 | 0.58 | 0.58 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.97 | 7.47 | 0.62 | 0.54 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.94 | 7.52 | 0.56 | 0.63 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.38 | 13.73 | 2.27 | 2.09 | 2 | 2 |
| R8009_M8028__far_ch1 | 9.23 | 8.38 | 1.10 | 1.07 | 2 | 2 |
