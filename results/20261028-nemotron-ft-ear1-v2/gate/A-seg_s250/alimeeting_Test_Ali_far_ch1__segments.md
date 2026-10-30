# Diarization scores: A-seg_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-seg_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T15:14:31+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-seg_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8201-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 15.30 | 12.60 | 2.06 | 0.65 | 15.95 | 100.00 | 0.00 |
| 0.25 | 7.47 | 6.81 | 0.49 | 0.17 | 9.11 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 85.89 (IoU 92.56) | 6.06 (IoU 6.12) |
| silence | 0.84 (IoU 0.89) | 7.21 (IoU 51.08) |

Speech P/R/F1: 99.04 / 93.40 / 96.14; miss 6.60 of ref speech, FA 10.39 of ref silence, SAD error 7.50.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 10793 | 41.10 | 90.99 | 56.62 | 0.089 | 0.080 | 0.038 | 0.040 |
| 0.25 | offset | 4875 | 10795 | 40.95 | 90.69 | 56.43 | 0.086 | 0.080 | -0.037 | -0.050 |
| 0.25 | all | 9750 | 21588 | 41.03 | 90.84 | 56.53 | 0.087 | 0.080 | 0.001 | -0.010 |
| 0.50 | onset | 4875 | 10793 | 42.15 | 93.31 | 58.07 | 0.095 | 0.090 | 0.040 | 0.050 |
| 0.50 | offset | 4875 | 10795 | 42.31 | 93.68 | 58.29 | 0.093 | 0.080 | -0.037 | -0.050 |
| 0.50 | all | 9750 | 21588 | 42.23 | 93.50 | 58.18 | 0.094 | 0.080 | 0.002 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 15.96 | 16.15 | 11.06 | 11.42 | 4 | 4 |
| R8002_M8003__far_ch1 | 16.67 | 18.01 | 10.93 | 12.98 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.54 | 16.15 | 9.62 | 10.83 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.88 | 23.60 | 15.59 | 17.95 | 4 | 4 |
| R8005_M8007__far_ch1 | 22.40 | 23.04 | 14.12 | 14.38 | 4 | 4 |
| R8005_M8008__far_ch1 | 11.70 | 11.59 | 7.46 | 6.87 | 4 | 4 |
| R8005_M8009__far_ch1 | 26.14 | 26.09 | 23.16 | 22.66 | 4 | 4 |
| R8006_M8012__far_ch1 | 14.96 | 15.23 | 8.47 | 8.47 | 4 | 4 |
| R8008_M8014__far_ch1 | 9.96 | 10.52 | 5.67 | 6.00 | 3 | 3 |
| R8008_M8015__far_ch1 | 12.13 | 13.81 | 6.41 | 7.33 | 3 | 3 |
| R8008_M8016__far_ch1 | 15.56 | 18.73 | 10.04 | 12.70 | 3 | 3 |
| R8008_M8017__far_ch1 | 10.51 | 11.52 | 5.10 | 5.72 | 3 | 3 |
| R8009_M8021__far_ch1 | 14.50 | 14.44 | 3.46 | 3.33 | 2 | 2 |
| R8009_M8022__far_ch1 | 11.48 | 12.38 | 1.58 | 1.94 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.10 | 15.86 | 2.00 | 2.62 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.42 | 12.35 | 1.05 | 1.06 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.71 | 13.21 | 2.12 | 1.87 | 2 | 2 |
| R8009_M8026__far_ch1 | 12.70 | 12.90 | 1.52 | 1.58 | 2 | 2 |
| R8009_M8027__far_ch1 | 7.35 | 7.06 | 1.13 | 1.11 | 2 | 2 |
| R8009_M8028__far_ch1 | 8.74 | 8.56 | 1.04 | 1.04 | 2 | 2 |
