# Diarization scores: C-seg_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `C-seg_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-seg_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T18:23:51+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `C-seg_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8074-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.14 | 14.99 | 1.55 | 0.59 | 17.69 | 100.00 | 0.00 |
| 0.25 | 9.12 | 8.41 | 0.53 | 0.18 | 10.76 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.80 (IoU 90.68) | 8.16 (IoU 8.20) |
| silence | 0.45 (IoU 0.49) | 7.59 (IoU 46.84) |

Speech P/R/F1: 99.47 / 91.12 / 95.11; miss 8.88 of ref speech, FA 5.60 of ref silence, SAD error 9.37.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12088 | 37.05 | 91.86 | 52.80 | 0.087 | 0.080 | 0.058 | 0.070 |
| 0.25 | offset | 4875 | 12089 | 36.79 | 91.22 | 52.43 | 0.095 | 0.090 | -0.065 | -0.080 |
| 0.25 | all | 9750 | 24177 | 36.92 | 91.54 | 52.61 | 0.091 | 0.090 | -0.003 | -0.010 |
| 0.50 | onset | 4875 | 12088 | 38.07 | 94.40 | 54.26 | 0.094 | 0.080 | 0.062 | 0.070 |
| 0.50 | offset | 4875 | 12089 | 38.61 | 95.73 | 55.02 | 0.105 | 0.100 | -0.071 | -0.080 |
| 0.50 | all | 9750 | 24177 | 38.34 | 95.07 | 54.64 | 0.100 | 0.090 | -0.005 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.92 | 17.28 | 11.50 | 12.01 | 4 | 4 |
| R8002_M8003__far_ch1 | 18.09 | 19.29 | 13.21 | 15.31 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.93 | 16.58 | 9.97 | 11.26 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.32 | 23.82 | 16.33 | 18.56 | 4 | 4 |
| R8005_M8007__far_ch1 | 22.92 | 23.58 | 15.59 | 15.84 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.97 | 12.61 | 9.69 | 8.86 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.30 | 27.13 | 24.34 | 23.78 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.45 | 16.82 | 10.96 | 10.98 | 4 | 4 |
| R8008_M8014__far_ch1 | 14.87 | 15.63 | 10.81 | 11.30 | 3 | 3 |
| R8008_M8015__far_ch1 | 14.20 | 15.48 | 9.17 | 9.96 | 3 | 3 |
| R8008_M8016__far_ch1 | 16.57 | 19.75 | 11.22 | 13.98 | 3 | 3 |
| R8008_M8017__far_ch1 | 11.85 | 12.96 | 6.94 | 7.60 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.39 | 16.31 | 4.00 | 3.86 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.94 | 15.08 | 2.39 | 2.79 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.08 | 17.88 | 3.24 | 4.10 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.54 | 13.49 | 1.44 | 1.45 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.53 | 14.16 | 2.56 | 2.38 | 2 | 2 |
| R8009_M8026__far_ch1 | 15.91 | 16.14 | 2.70 | 2.81 | 2 | 2 |
| R8009_M8027__far_ch1 | 13.57 | 13.57 | 3.51 | 3.45 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.96 | 14.17 | 4.76 | 4.37 | 2 | 2 |
