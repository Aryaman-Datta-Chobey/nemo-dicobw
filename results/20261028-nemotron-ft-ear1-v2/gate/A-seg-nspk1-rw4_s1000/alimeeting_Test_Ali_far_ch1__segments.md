# Diarization scores: A-seg-nspk1-rw4_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-seg-nspk1-rw4_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1-rw4_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T04:18:59+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-seg-nspk1-rw4_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1-rw4/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8374-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.58 | 15.24 | 1.68 | 0.66 | 18.10 | 95.00 | 0.05 |
| 0.25 | 9.26 | 8.55 | 0.48 | 0.23 | 10.87 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.94 (IoU 90.72) | 8.02 (IoU 8.06) |
| silence | 0.57 (IoU 0.62) | 7.47 (IoU 46.50) |

Speech P/R/F1: 99.32 / 91.28 / 95.13; miss 8.72 of ref speech, FA 7.13 of ref silence, SAD error 9.34.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11906 | 36.86 | 90.03 | 52.31 | 0.086 | 0.080 | 0.051 | 0.060 |
| 0.25 | offset | 4875 | 11906 | 36.32 | 88.70 | 51.53 | 0.103 | 0.100 | -0.060 | -0.080 |
| 0.25 | all | 9750 | 23812 | 36.59 | 89.36 | 51.92 | 0.094 | 0.090 | -0.004 | -0.010 |
| 0.50 | onset | 4875 | 11906 | 38.00 | 92.80 | 53.92 | 0.094 | 0.080 | 0.057 | 0.060 |
| 0.50 | offset | 4875 | 11906 | 38.59 | 94.24 | 54.75 | 0.116 | 0.100 | -0.068 | -0.080 |
| 0.50 | all | 9750 | 23812 | 38.29 | 93.52 | 54.34 | 0.105 | 0.090 | -0.006 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.71 | 17.02 | 11.48 | 11.99 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.92 | 19.06 | 11.17 | 13.09 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.62 | 17.32 | 10.41 | 11.70 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.56 | 25.10 | 17.32 | 19.36 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.59 | 24.16 | 15.84 | 15.99 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.29 | 12.93 | 9.78 | 8.95 | 4 | 4 |
| R8005_M8009__far_ch1 | 29.03 | 29.03 | 25.82 | 25.36 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.30 | 16.74 | 10.78 | 10.93 | 4 | 4 |
| R8008_M8014__far_ch1 | 13.84 | 14.49 | 9.98 | 10.39 | 3 | 3 |
| R8008_M8015__far_ch1 | 15.28 | 16.69 | 9.98 | 10.79 | 3 | 4 |
| R8008_M8016__far_ch1 | 16.38 | 19.27 | 10.56 | 13.06 | 3 | 3 |
| R8008_M8017__far_ch1 | 11.82 | 12.76 | 6.12 | 6.70 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.53 | 16.45 | 4.13 | 3.99 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.46 | 15.60 | 2.63 | 3.03 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.94 | 18.13 | 3.33 | 4.73 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.44 | 14.39 | 2.30 | 2.31 | 2 | 2 |
| R8009_M8025__far_ch1 | 15.23 | 15.84 | 3.54 | 4.85 | 2 | 2 |
| R8009_M8026__far_ch1 | 15.99 | 16.09 | 2.66 | 2.70 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.17 | 15.18 | 3.92 | 3.87 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.77 | 13.86 | 5.09 | 4.60 | 2 | 2 |
