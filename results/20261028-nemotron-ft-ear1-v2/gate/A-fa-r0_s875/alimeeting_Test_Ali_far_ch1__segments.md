# Diarization scores: A-fa-r0_s875/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0_s875/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s875/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T18:09:20+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0_s875`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7649-epoch=6.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 19.69 | 18.27 | 0.87 | 0.55 | 20.50 | 100.00 | 0.00 |
| 0.25 | 11.26 | 10.83 | 0.23 | 0.21 | 13.47 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.54 (IoU 89.46) | 9.42 (IoU 9.45) |
| silence | 0.31 (IoU 0.34) | 7.73 (IoU 44.29) |

Speech P/R/F1: 99.63 / 89.76 / 94.44; miss 10.24 of ref speech, FA 3.84 of ref silence, SAD error 10.57.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13424 | 33.23 | 91.51 | 48.76 | 0.099 | 0.100 | 0.086 | 0.090 |
| 0.25 | offset | 4875 | 13424 | 34.03 | 93.70 | 49.93 | 0.073 | 0.060 | -0.049 | -0.050 |
| 0.25 | all | 9750 | 26848 | 33.63 | 92.61 | 49.34 | 0.086 | 0.080 | 0.017 | 0.010 |
| 0.50 | onset | 4875 | 13424 | 34.49 | 94.97 | 50.60 | 0.108 | 0.100 | 0.091 | 0.100 |
| 0.50 | offset | 4875 | 13424 | 34.86 | 95.98 | 51.14 | 0.079 | 0.070 | -0.052 | -0.050 |
| 0.50 | all | 9750 | 26848 | 34.67 | 95.48 | 50.87 | 0.093 | 0.080 | 0.019 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 18.11 | 18.60 | 11.52 | 12.11 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.68 | 21.11 | 15.04 | 17.25 | 4 | 4 |
| R8004_M8005__far_ch1 | 16.35 | 18.11 | 10.64 | 11.95 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.45 | 24.99 | 17.91 | 20.30 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.86 | 24.44 | 16.65 | 16.84 | 4 | 4 |
| R8005_M8008__far_ch1 | 14.53 | 14.56 | 10.69 | 10.42 | 4 | 4 |
| R8005_M8009__far_ch1 | 48.56 | 49.63 | 44.35 | 45.50 | 4 | 4 |
| R8006_M8012__far_ch1 | 18.39 | 19.04 | 11.84 | 12.35 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.08 | 16.90 | 11.99 | 12.59 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.14 | 22.95 | 18.12 | 18.44 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.66 | 23.13 | 13.34 | 16.72 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.48 | 16.83 | 12.26 | 12.92 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.61 | 15.53 | 3.94 | 3.80 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.57 | 13.65 | 1.87 | 2.29 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.41 | 16.06 | 1.87 | 2.39 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.72 | 12.64 | 1.13 | 1.13 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.65 | 13.13 | 2.18 | 1.90 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.43 | 16.55 | 2.64 | 2.70 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.03 | 14.96 | 3.92 | 3.80 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.08 | 11.92 | 1.50 | 1.51 | 2 | 2 |
