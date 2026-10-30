# Diarization scores: A-fa-r75a-seed43_s2250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a-seed43_s2250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s2250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T05:39:56+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a-seed43_s2250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7881-epoch=8.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.11 | 16.49 | 1.05 | 0.57 | 18.80 | 100.00 | 0.00 |
| 0.25 | 10.19 | 9.72 | 0.30 | 0.17 | 11.96 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.80 (IoU 89.78) | 9.16 (IoU 9.18) |
| silence | 0.27 (IoU 0.30) | 7.77 (IoU 45.17) |

Speech P/R/F1: 99.67 / 90.04 / 94.61; miss 9.96 of ref speech, FA 3.37 of ref silence, SAD error 10.25.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12804 | 35.17 | 92.37 | 50.94 | 0.087 | 0.080 | 0.069 | 0.080 |
| 0.25 | offset | 4875 | 12804 | 34.90 | 91.67 | 50.56 | 0.089 | 0.080 | -0.076 | -0.080 |
| 0.25 | all | 9750 | 25608 | 35.04 | 92.02 | 50.75 | 0.088 | 0.080 | -0.003 | -0.010 |
| 0.50 | onset | 4875 | 12804 | 36.27 | 95.26 | 52.54 | 0.095 | 0.090 | 0.074 | 0.080 |
| 0.50 | offset | 4875 | 12804 | 36.66 | 96.29 | 53.10 | 0.100 | 0.090 | -0.083 | -0.080 |
| 0.50 | all | 9750 | 25608 | 36.47 | 95.77 | 52.82 | 0.098 | 0.090 | -0.005 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.11 | 16.38 | 11.34 | 11.80 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.53 | 20.80 | 15.36 | 17.48 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.12 | 16.76 | 10.14 | 11.43 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.80 | 25.33 | 17.85 | 19.96 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.68 | 24.28 | 16.21 | 16.40 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.18 | 12.81 | 9.99 | 9.07 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.00 | 27.84 | 25.07 | 24.47 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.23 | 16.68 | 10.74 | 10.83 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.95 | 16.67 | 12.08 | 12.62 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.96 | 22.95 | 18.10 | 18.60 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.20 | 22.55 | 13.57 | 16.96 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.62 | 16.94 | 12.40 | 13.02 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.20 | 16.11 | 3.95 | 3.80 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.09 | 15.28 | 2.44 | 2.88 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.33 | 18.39 | 3.40 | 4.65 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.67 | 13.60 | 1.47 | 1.47 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.36 | 14.13 | 2.35 | 2.26 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.25 | 17.37 | 3.04 | 3.10 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.88 | 15.80 | 4.18 | 4.07 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.03 | 12.81 | 2.01 | 2.00 | 2 | 2 |
