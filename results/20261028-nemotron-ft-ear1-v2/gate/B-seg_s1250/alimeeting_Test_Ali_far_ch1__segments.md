# Diarization scores: B-seg_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `B-seg_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-seg_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T17:11:27+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `B-seg_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8208-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.13 | 14.96 | 1.57 | 0.61 | 17.69 | 100.00 | 0.00 |
| 0.25 | 9.16 | 8.41 | 0.55 | 0.19 | 10.79 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.82 (IoU 90.70) | 8.14 (IoU 8.18) |
| silence | 0.45 (IoU 0.49) | 7.59 (IoU 46.89) |

Speech P/R/F1: 99.46 / 91.14 / 95.12; miss 8.86 of ref speech, FA 5.61 of ref silence, SAD error 9.35.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12106 | 36.98 | 91.84 | 52.73 | 0.086 | 0.080 | 0.058 | 0.070 |
| 0.25 | offset | 4875 | 12108 | 36.86 | 91.55 | 52.56 | 0.094 | 0.090 | -0.063 | -0.070 |
| 0.25 | all | 9750 | 24214 | 36.92 | 91.69 | 52.64 | 0.090 | 0.090 | -0.002 | -0.010 |
| 0.50 | onset | 4875 | 12106 | 37.96 | 94.28 | 54.13 | 0.093 | 0.080 | 0.062 | 0.070 |
| 0.50 | offset | 4875 | 12108 | 38.53 | 95.69 | 54.94 | 0.104 | 0.090 | -0.069 | -0.080 |
| 0.50 | all | 9750 | 24214 | 38.25 | 94.98 | 54.53 | 0.098 | 0.090 | -0.004 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.95 | 17.30 | 11.52 | 12.02 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.98 | 19.22 | 12.85 | 15.07 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.84 | 16.52 | 10.00 | 11.31 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.53 | 24.03 | 16.61 | 18.91 | 4 | 4 |
| R8005_M8007__far_ch1 | 22.90 | 23.54 | 15.55 | 15.82 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.90 | 12.54 | 9.65 | 8.81 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.34 | 27.22 | 24.39 | 23.86 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.48 | 16.85 | 11.05 | 11.13 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.10 | 15.83 | 10.98 | 11.47 | 3 | 3 |
| R8008_M8015__far_ch1 | 13.77 | 15.18 | 8.70 | 9.42 | 3 | 3 |
| R8008_M8016__far_ch1 | 16.45 | 19.52 | 10.98 | 13.59 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.43 | 13.60 | 7.90 | 8.59 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.12 | 16.05 | 3.95 | 3.80 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.75 | 14.88 | 2.34 | 2.74 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.24 | 17.89 | 3.42 | 4.10 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.39 | 13.34 | 1.44 | 1.45 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.50 | 14.15 | 2.55 | 2.39 | 2 | 2 |
| R8009_M8026__far_ch1 | 15.97 | 16.19 | 2.78 | 2.90 | 2 | 2 |
| R8009_M8027__far_ch1 | 13.60 | 13.60 | 3.52 | 3.46 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.90 | 14.07 | 4.97 | 4.54 | 2 | 2 |
