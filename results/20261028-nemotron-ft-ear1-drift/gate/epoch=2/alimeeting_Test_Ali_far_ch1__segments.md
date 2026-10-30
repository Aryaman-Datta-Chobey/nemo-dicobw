# Diarization scores: epoch=2/alimeeting_Test_Ali_far_ch1__segments

- name: `epoch=2/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/epoch=2/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:43:52+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `epoch=2`
- model: `/mnt/data/exp/nemotron/20261027-nemotron-ft-ear1-nospkw/nemotron_ft_ear1_nospkw/checkpoints/nemotron_ft_ear1_nospkw--val_f1_acc=0.8330-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.08 | 14.94 | 1.53 | 0.61 | 17.65 | 100.00 | 0.00 |
| 0.25 | 9.00 | 8.41 | 0.42 | 0.17 | 10.70 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 84.08 (IoU 90.92) | 7.88 (IoU 7.92) |
| silence | 0.52 (IoU 0.57) | 7.52 (IoU 47.23) |

Speech P/R/F1: 99.38 / 91.43 / 95.24; miss 8.57 of ref speech, FA 6.48 of ref silence, SAD error 9.14.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11969 | 37.20 | 91.32 | 52.86 | 0.087 | 0.080 | 0.056 | 0.060 |
| 0.25 | offset | 4875 | 11970 | 36.97 | 90.77 | 52.54 | 0.093 | 0.090 | -0.057 | -0.070 |
| 0.25 | all | 9750 | 23939 | 37.08 | 91.05 | 52.70 | 0.090 | 0.080 | -0.000 | -0.000 |
| 0.50 | onset | 4875 | 11969 | 38.27 | 93.95 | 54.38 | 0.094 | 0.080 | 0.061 | 0.060 |
| 0.50 | offset | 4875 | 11970 | 38.81 | 95.28 | 55.15 | 0.104 | 0.090 | -0.061 | -0.070 |
| 0.50 | all | 9750 | 23939 | 38.54 | 94.62 | 54.77 | 0.099 | 0.090 | -0.000 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.53 | 16.82 | 11.58 | 12.09 | 4 | 4 |
| R8002_M8003__far_ch1 | 18.08 | 19.36 | 12.99 | 15.15 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.07 | 16.70 | 10.10 | 11.42 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.03 | 24.56 | 17.00 | 19.06 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.39 | 23.99 | 15.79 | 15.96 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.13 | 12.78 | 9.69 | 8.85 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.99 | 27.90 | 24.91 | 24.37 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.12 | 16.53 | 10.61 | 10.68 | 4 | 4 |
| R8008_M8014__far_ch1 | 13.41 | 14.11 | 9.34 | 9.74 | 3 | 3 |
| R8008_M8015__far_ch1 | 14.38 | 15.63 | 9.17 | 9.86 | 3 | 3 |
| R8008_M8016__far_ch1 | 17.37 | 20.42 | 12.06 | 14.95 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.12 | 13.11 | 7.21 | 7.75 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.26 | 16.19 | 4.02 | 3.87 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.88 | 15.01 | 2.37 | 2.75 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.23 | 17.26 | 2.76 | 3.84 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.62 | 13.55 | 1.48 | 1.47 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.28 | 13.79 | 2.44 | 2.17 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.60 | 16.75 | 2.85 | 2.93 | 2 | 2 |
| R8009_M8027__far_ch1 | 12.56 | 12.62 | 3.01 | 2.98 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.65 | 12.27 | 2.44 | 2.36 | 2 | 2 |
