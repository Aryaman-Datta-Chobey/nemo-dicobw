# Diarization scores: A-seg-nspk1-rw4_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-seg-nspk1-rw4_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1-rw4_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T03:50:05+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-seg-nspk1-rw4_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1-rw4/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8061-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 15.56 | 13.13 | 1.80 | 0.63 | 16.22 | 100.00 | 0.00 |
| 0.25 | 7.75 | 7.18 | 0.40 | 0.17 | 9.43 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 85.39 (IoU 92.18) | 6.57 (IoU 6.61) |
| silence | 0.68 (IoU 0.72) | 7.37 (IoU 50.42) |

Speech P/R/F1: 99.22 / 92.86 / 95.93; miss 7.14 of ref speech, FA 8.40 of ref silence, SAD error 7.88.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11315 | 39.90 | 92.62 | 55.78 | 0.088 | 0.080 | 0.038 | 0.040 |
| 0.25 | offset | 4875 | 11315 | 39.88 | 92.55 | 55.74 | 0.086 | 0.080 | -0.044 | -0.060 |
| 0.25 | all | 9750 | 22630 | 39.89 | 92.58 | 55.76 | 0.087 | 0.080 | -0.003 | -0.010 |
| 0.50 | onset | 4875 | 11315 | 40.85 | 94.81 | 57.10 | 0.094 | 0.090 | 0.042 | 0.050 |
| 0.50 | offset | 4875 | 11315 | 41.09 | 95.36 | 57.43 | 0.093 | 0.080 | -0.046 | -0.060 |
| 0.50 | all | 9750 | 22630 | 40.97 | 95.09 | 57.26 | 0.093 | 0.080 | -0.002 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 15.88 | 16.12 | 11.04 | 11.42 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.13 | 18.32 | 11.91 | 13.89 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.46 | 16.10 | 9.52 | 10.79 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.71 | 23.21 | 15.51 | 17.70 | 4 | 4 |
| R8005_M8007__far_ch1 | 22.18 | 22.83 | 14.50 | 14.74 | 4 | 4 |
| R8005_M8008__far_ch1 | 11.92 | 11.72 | 8.26 | 7.60 | 4 | 4 |
| R8005_M8009__far_ch1 | 26.24 | 26.17 | 23.19 | 22.67 | 4 | 4 |
| R8006_M8012__far_ch1 | 15.47 | 15.91 | 9.63 | 9.75 | 4 | 4 |
| R8008_M8014__far_ch1 | 10.56 | 11.22 | 6.41 | 6.84 | 3 | 3 |
| R8008_M8015__far_ch1 | 13.00 | 14.72 | 7.03 | 8.01 | 3 | 3 |
| R8008_M8016__far_ch1 | 15.58 | 18.72 | 10.02 | 12.67 | 3 | 3 |
| R8008_M8017__far_ch1 | 11.09 | 12.10 | 5.48 | 6.13 | 3 | 3 |
| R8009_M8021__far_ch1 | 14.66 | 14.60 | 3.47 | 3.34 | 2 | 2 |
| R8009_M8022__far_ch1 | 11.78 | 12.72 | 1.65 | 2.03 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.09 | 15.89 | 1.92 | 2.62 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.38 | 12.31 | 0.98 | 0.98 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.40 | 13.05 | 1.93 | 1.79 | 2 | 2 |
| R8009_M8026__far_ch1 | 13.53 | 13.70 | 1.73 | 1.80 | 2 | 2 |
| R8009_M8027__far_ch1 | 9.05 | 9.11 | 1.76 | 1.74 | 2 | 2 |
| R8009_M8028__far_ch1 | 9.50 | 9.36 | 1.06 | 1.07 | 2 | 2 |
