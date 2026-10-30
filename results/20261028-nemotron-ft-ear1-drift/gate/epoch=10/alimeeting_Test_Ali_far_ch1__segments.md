# Diarization scores: epoch=10/alimeeting_Test_Ali_far_ch1__segments

- name: `epoch=10/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/epoch=10/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:44:26+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `epoch=10`
- model: `/mnt/data/exp/nemotron/20261027-nemotron-ft-ear1-nospkw/nemotron_ft_ear1_nospkw/checkpoints/nemotron_ft_ear1_nospkw--val_f1_acc=0.8302-epoch=10.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.73 | 15.64 | 1.46 | 0.62 | 18.30 | 95.00 | 0.05 |
| 0.25 | 9.57 | 9.03 | 0.38 | 0.17 | 11.25 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.66 (IoU 90.44) | 8.30 (IoU 8.35) |
| silence | 0.54 (IoU 0.59) | 7.50 (IoU 45.88) |

Speech P/R/F1: 99.35 / 90.97 / 94.98; miss 9.03 of ref speech, FA 6.76 of ref silence, SAD error 9.62.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12240 | 36.11 | 90.67 | 51.65 | 0.084 | 0.080 | 0.050 | 0.060 |
| 0.25 | offset | 4875 | 12241 | 35.56 | 89.29 | 50.86 | 0.099 | 0.090 | -0.065 | -0.080 |
| 0.25 | all | 9750 | 24481 | 35.84 | 89.98 | 51.26 | 0.092 | 0.090 | -0.007 | -0.010 |
| 0.50 | onset | 4875 | 12240 | 37.21 | 93.42 | 53.22 | 0.092 | 0.080 | 0.055 | 0.060 |
| 0.50 | offset | 4875 | 12241 | 37.72 | 94.71 | 53.95 | 0.112 | 0.100 | -0.073 | -0.080 |
| 0.50 | all | 9750 | 24481 | 37.46 | 94.06 | 53.58 | 0.102 | 0.090 | -0.009 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.86 | 17.08 | 11.94 | 12.35 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.80 | 18.89 | 12.39 | 14.33 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.44 | 17.16 | 10.26 | 11.59 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.78 | 25.43 | 17.64 | 19.97 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.67 | 24.28 | 15.85 | 16.04 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.51 | 13.14 | 9.98 | 9.13 | 4 | 4 |
| R8005_M8009__far_ch1 | 29.65 | 29.41 | 26.60 | 25.86 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.34 | 16.77 | 10.83 | 10.96 | 4 | 4 |
| R8008_M8014__far_ch1 | 14.04 | 14.84 | 10.22 | 10.77 | 3 | 4 |
| R8008_M8015__far_ch1 | 17.66 | 18.92 | 13.04 | 13.53 | 3 | 3 |
| R8008_M8016__far_ch1 | 16.86 | 19.91 | 10.77 | 13.55 | 3 | 3 |
| R8008_M8017__far_ch1 | 13.25 | 14.31 | 8.92 | 9.44 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.70 | 16.60 | 4.30 | 4.14 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.55 | 15.74 | 2.72 | 3.14 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.18 | 18.51 | 3.69 | 5.26 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.91 | 14.77 | 3.05 | 2.99 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.10 | 13.62 | 2.31 | 2.06 | 2 | 2 |
| R8009_M8026__far_ch1 | 15.83 | 15.92 | 2.59 | 2.63 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.02 | 15.07 | 4.04 | 4.02 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.81 | 12.56 | 2.04 | 2.02 | 2 | 2 |
