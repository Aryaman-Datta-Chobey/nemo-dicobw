# Diarization scores: A-seg-nspk1-rw4_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-seg-nspk1-rw4_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1-rw4_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T03:59:41+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-seg-nspk1-rw4_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1-rw4/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8346-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.03 | 14.75 | 1.64 | 0.64 | 17.57 | 100.00 | 0.00 |
| 0.25 | 8.93 | 8.25 | 0.48 | 0.19 | 10.53 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 84.06 (IoU 90.88) | 7.90 (IoU 7.94) |
| silence | 0.53 (IoU 0.58) | 7.51 (IoU 47.10) |

Speech P/R/F1: 99.37 / 91.41 / 95.22; miss 8.59 of ref speech, FA 6.62 of ref silence, SAD error 9.17.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11776 | 37.48 | 90.54 | 53.02 | 0.093 | 0.090 | 0.058 | 0.070 |
| 0.25 | offset | 4875 | 11776 | 37.69 | 91.04 | 53.31 | 0.092 | 0.090 | -0.056 | -0.070 |
| 0.25 | all | 9750 | 23552 | 37.58 | 90.79 | 53.16 | 0.093 | 0.090 | 0.001 | -0.000 |
| 0.50 | onset | 4875 | 11776 | 38.67 | 93.42 | 54.70 | 0.101 | 0.090 | 0.063 | 0.070 |
| 0.50 | offset | 4875 | 11776 | 39.27 | 94.85 | 55.54 | 0.102 | 0.090 | -0.060 | -0.070 |
| 0.50 | all | 9750 | 23552 | 38.97 | 94.13 | 55.12 | 0.101 | 0.090 | 0.001 | -0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.61 | 16.94 | 11.33 | 11.82 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.90 | 19.09 | 12.92 | 14.87 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.90 | 16.59 | 9.92 | 11.19 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.33 | 23.85 | 16.27 | 18.30 | 4 | 4 |
| R8005_M8007__far_ch1 | 22.77 | 23.47 | 15.31 | 15.55 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.67 | 12.34 | 9.31 | 8.51 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.43 | 27.34 | 24.34 | 23.81 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.03 | 16.44 | 10.39 | 10.50 | 4 | 4 |
| R8008_M8014__far_ch1 | 13.44 | 14.06 | 9.57 | 9.95 | 3 | 3 |
| R8008_M8015__far_ch1 | 14.52 | 15.93 | 9.33 | 10.15 | 3 | 3 |
| R8008_M8016__far_ch1 | 16.32 | 19.29 | 11.01 | 13.58 | 3 | 3 |
| R8008_M8017__far_ch1 | 11.80 | 12.68 | 5.96 | 6.57 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.21 | 16.13 | 4.08 | 3.93 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.80 | 14.91 | 2.37 | 2.76 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.60 | 17.43 | 2.93 | 3.78 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.84 | 13.74 | 1.67 | 1.65 | 2 | 2 |
| R8009_M8025__far_ch1 | 15.16 | 15.23 | 3.31 | 3.86 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.56 | 16.72 | 2.85 | 2.94 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.47 | 14.47 | 3.66 | 3.60 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.96 | 13.27 | 4.10 | 3.79 | 2 | 2 |
