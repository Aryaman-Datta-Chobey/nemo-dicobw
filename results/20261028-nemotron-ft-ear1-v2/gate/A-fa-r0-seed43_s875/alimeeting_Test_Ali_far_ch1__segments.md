# Diarization scores: A-fa-r0-seed43_s875/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0-seed43_s875/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s875/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T19:34:11+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0-seed43_s875`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7721-epoch=6.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 19.60 | 18.10 | 0.92 | 0.58 | 20.37 | 100.00 | 0.00 |
| 0.25 | 11.24 | 10.76 | 0.25 | 0.23 | 13.39 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.60 (IoU 89.51) | 9.36 (IoU 9.39) |
| silence | 0.32 (IoU 0.35) | 7.72 (IoU 44.37) |

Speech P/R/F1: 99.61 / 89.82 / 94.47; miss 10.18 of ref speech, FA 3.98 of ref silence, SAD error 10.53.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13239 | 33.39 | 90.67 | 48.80 | 0.100 | 0.100 | 0.085 | 0.100 |
| 0.25 | offset | 4875 | 13239 | 34.30 | 93.15 | 50.14 | 0.073 | 0.060 | -0.050 | -0.050 |
| 0.25 | all | 9750 | 26478 | 33.84 | 91.91 | 49.47 | 0.086 | 0.080 | 0.017 | 0.010 |
| 0.50 | onset | 4875 | 13239 | 34.66 | 94.11 | 50.66 | 0.108 | 0.110 | 0.091 | 0.100 |
| 0.50 | offset | 4875 | 13239 | 35.21 | 95.63 | 51.47 | 0.080 | 0.070 | -0.052 | -0.050 |
| 0.50 | all | 9750 | 26478 | 34.93 | 94.87 | 51.07 | 0.094 | 0.080 | 0.019 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 18.78 | 19.35 | 12.08 | 12.80 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.94 | 21.52 | 15.38 | 17.83 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.36 | 17.07 | 10.10 | 11.40 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.35 | 24.72 | 17.80 | 19.89 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.86 | 24.44 | 16.54 | 16.72 | 4 | 4 |
| R8005_M8008__far_ch1 | 14.04 | 13.75 | 10.26 | 9.59 | 4 | 4 |
| R8005_M8009__far_ch1 | 46.86 | 47.57 | 43.47 | 44.25 | 4 | 4 |
| R8006_M8012__far_ch1 | 18.39 | 19.19 | 11.88 | 12.60 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.07 | 16.88 | 11.97 | 12.60 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.27 | 22.99 | 18.31 | 18.63 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.98 | 23.41 | 13.55 | 16.90 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.47 | 16.78 | 12.22 | 12.83 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.58 | 15.50 | 3.90 | 3.76 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.69 | 13.76 | 1.92 | 2.32 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.47 | 16.13 | 1.93 | 2.44 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.05 | 12.97 | 1.37 | 1.36 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.78 | 13.27 | 2.29 | 2.01 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.74 | 16.87 | 2.82 | 2.90 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.18 | 15.13 | 3.94 | 3.84 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.36 | 12.19 | 1.58 | 1.60 | 2 | 2 |
