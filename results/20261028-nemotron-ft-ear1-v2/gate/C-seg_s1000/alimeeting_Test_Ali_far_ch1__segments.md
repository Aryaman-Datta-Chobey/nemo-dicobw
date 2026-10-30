# Diarization scores: C-seg_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `C-seg_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-seg_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T18:12:57+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `C-seg_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8082-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 16.97 | 14.70 | 1.68 | 0.59 | 17.52 | 100.00 | 0.00 |
| 0.25 | 8.98 | 8.20 | 0.60 | 0.18 | 10.64 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 84.05 (IoU 90.91) | 7.90 (IoU 7.94) |
| silence | 0.50 (IoU 0.55) | 7.54 (IoU 47.26) |

Speech P/R/F1: 99.40 / 91.40 / 95.24; miss 8.60 of ref speech, FA 6.28 of ref silence, SAD error 9.14.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11956 | 37.63 | 92.29 | 53.46 | 0.087 | 0.080 | 0.052 | 0.060 |
| 0.25 | offset | 4875 | 11958 | 37.21 | 91.28 | 52.87 | 0.094 | 0.090 | -0.063 | -0.070 |
| 0.25 | all | 9750 | 23914 | 37.42 | 91.78 | 53.17 | 0.091 | 0.090 | -0.005 | -0.010 |
| 0.50 | onset | 4875 | 11956 | 38.58 | 94.63 | 54.82 | 0.094 | 0.090 | 0.056 | 0.060 |
| 0.50 | offset | 4875 | 11958 | 39.05 | 95.79 | 55.49 | 0.105 | 0.090 | -0.069 | -0.080 |
| 0.50 | all | 9750 | 23914 | 38.82 | 95.21 | 55.15 | 0.099 | 0.090 | -0.007 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.74 | 17.05 | 11.39 | 11.87 | 4 | 4 |
| R8002_M8003__far_ch1 | 18.48 | 19.60 | 14.22 | 16.32 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.76 | 16.39 | 9.89 | 11.18 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.39 | 23.84 | 16.31 | 18.45 | 4 | 4 |
| R8005_M8007__far_ch1 | 22.78 | 23.40 | 15.45 | 15.72 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.87 | 12.51 | 9.61 | 8.77 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.05 | 26.88 | 24.11 | 23.57 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.49 | 16.82 | 11.06 | 11.12 | 4 | 4 |
| R8008_M8014__far_ch1 | 14.78 | 15.55 | 10.65 | 11.18 | 3 | 3 |
| R8008_M8015__far_ch1 | 13.32 | 14.90 | 7.87 | 8.73 | 3 | 3 |
| R8008_M8016__far_ch1 | 17.36 | 20.47 | 12.07 | 14.90 | 3 | 3 |
| R8008_M8017__far_ch1 | 11.12 | 12.03 | 5.09 | 5.70 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.99 | 15.92 | 3.86 | 3.72 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.54 | 14.68 | 2.25 | 2.66 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.69 | 17.53 | 3.06 | 3.91 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.28 | 13.22 | 1.37 | 1.37 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.39 | 14.06 | 2.54 | 2.39 | 2 | 2 |
| R8009_M8026__far_ch1 | 15.83 | 16.05 | 2.66 | 2.77 | 2 | 2 |
| R8009_M8027__far_ch1 | 12.58 | 12.58 | 3.12 | 3.06 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.90 | 14.02 | 5.01 | 4.55 | 2 | 2 |
