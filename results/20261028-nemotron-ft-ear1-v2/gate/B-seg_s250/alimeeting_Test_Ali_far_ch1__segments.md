# Diarization scores: B-seg_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `B-seg_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-seg_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T16:26:48+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `B-seg_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8070-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 16.06 | 13.63 | 1.81 | 0.62 | 16.75 | 100.00 | 0.00 |
| 0.25 | 8.06 | 7.43 | 0.46 | 0.17 | 9.83 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 85.20 (IoU 91.96) | 6.76 (IoU 6.81) |
| silence | 0.69 (IoU 0.74) | 7.35 (IoU 49.67) |

Speech P/R/F1: 99.20 / 92.65 / 95.81; miss 7.35 of ref speech, FA 8.58 of ref silence, SAD error 8.10.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11472 | 39.52 | 93.01 | 55.47 | 0.088 | 0.080 | 0.041 | 0.050 |
| 0.25 | offset | 4875 | 11474 | 38.85 | 91.45 | 54.54 | 0.090 | 0.080 | -0.053 | -0.060 |
| 0.25 | all | 9750 | 22946 | 39.19 | 92.23 | 55.00 | 0.089 | 0.080 | -0.006 | -0.010 |
| 0.50 | onset | 4875 | 11472 | 40.31 | 94.85 | 56.57 | 0.092 | 0.080 | 0.043 | 0.050 |
| 0.50 | offset | 4875 | 11474 | 40.48 | 95.28 | 56.82 | 0.099 | 0.090 | -0.056 | -0.070 |
| 0.50 | all | 9750 | 22946 | 40.39 | 95.07 | 56.70 | 0.096 | 0.080 | -0.007 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 15.99 | 16.27 | 11.10 | 11.59 | 4 | 4 |
| R8002_M8003__far_ch1 | 18.13 | 19.22 | 13.16 | 15.15 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.66 | 16.26 | 9.63 | 10.85 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.83 | 24.54 | 16.46 | 18.93 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.09 | 23.68 | 14.99 | 15.20 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.51 | 12.24 | 8.77 | 8.01 | 4 | 4 |
| R8005_M8009__far_ch1 | 26.62 | 26.58 | 23.65 | 23.17 | 4 | 4 |
| R8006_M8012__far_ch1 | 15.86 | 16.20 | 9.30 | 9.30 | 4 | 4 |
| R8008_M8014__far_ch1 | 11.35 | 11.72 | 6.51 | 6.70 | 3 | 3 |
| R8008_M8015__far_ch1 | 12.67 | 14.40 | 6.80 | 7.74 | 3 | 3 |
| R8008_M8016__far_ch1 | 17.33 | 20.81 | 11.60 | 14.74 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.61 | 13.71 | 7.42 | 8.09 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.14 | 15.08 | 3.59 | 3.46 | 2 | 2 |
| R8009_M8022__far_ch1 | 11.50 | 12.37 | 1.48 | 1.78 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.28 | 16.23 | 2.09 | 2.92 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.35 | 12.25 | 0.96 | 0.95 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.52 | 13.01 | 1.83 | 1.60 | 2 | 2 |
| R8009_M8026__far_ch1 | 13.49 | 13.69 | 1.70 | 1.74 | 2 | 2 |
| R8009_M8027__far_ch1 | 8.49 | 8.27 | 1.06 | 1.02 | 2 | 2 |
| R8009_M8028__far_ch1 | 10.70 | 10.56 | 1.10 | 1.13 | 2 | 2 |
