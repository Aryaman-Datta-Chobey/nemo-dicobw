# Diarization scores: A-seg-nspk1-rw4_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-seg-nspk1-rw4_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1-rw4_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T04:09:14+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-seg-nspk1-rw4_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1-rw4/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8255-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.08 | 14.47 | 1.93 | 0.68 | 17.60 | 100.00 | 0.00 |
| 0.25 | 8.84 | 8.00 | 0.61 | 0.23 | 10.42 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 84.52 (IoU 91.23) | 7.44 (IoU 7.49) |
| silence | 0.68 (IoU 0.74) | 7.36 (IoU 47.52) |

Speech P/R/F1: 99.20 / 91.91 / 95.41; miss 8.09 of ref speech, FA 8.49 of ref silence, SAD error 8.84.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11448 | 38.09 | 89.44 | 53.42 | 0.086 | 0.080 | 0.045 | 0.050 |
| 0.25 | offset | 4875 | 11448 | 37.34 | 87.69 | 52.38 | 0.102 | 0.100 | -0.055 | -0.070 |
| 0.25 | all | 9750 | 22896 | 37.71 | 88.56 | 52.90 | 0.094 | 0.090 | -0.004 | -0.010 |
| 0.50 | onset | 4875 | 11448 | 39.28 | 92.25 | 55.10 | 0.094 | 0.080 | 0.051 | 0.060 |
| 0.50 | offset | 4875 | 11448 | 39.92 | 93.74 | 55.99 | 0.116 | 0.100 | -0.058 | -0.080 |
| 0.50 | all | 9750 | 22896 | 39.60 | 92.99 | 55.55 | 0.105 | 0.090 | -0.004 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.46 | 16.80 | 11.34 | 11.84 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.85 | 18.95 | 11.23 | 13.06 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.31 | 17.01 | 10.16 | 11.44 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.14 | 24.64 | 16.96 | 19.00 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.22 | 23.84 | 15.46 | 15.64 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.01 | 12.66 | 9.56 | 8.76 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.19 | 28.18 | 25.11 | 24.62 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.09 | 16.56 | 10.47 | 10.61 | 4 | 4 |
| R8008_M8014__far_ch1 | 12.89 | 13.57 | 8.98 | 9.39 | 3 | 3 |
| R8008_M8015__far_ch1 | 13.14 | 14.62 | 7.46 | 8.34 | 3 | 3 |
| R8008_M8016__far_ch1 | 15.74 | 18.95 | 9.71 | 12.50 | 3 | 3 |
| R8008_M8017__far_ch1 | 11.34 | 12.14 | 4.53 | 5.12 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.14 | 16.07 | 4.02 | 3.89 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.97 | 15.07 | 2.40 | 2.78 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.15 | 17.35 | 3.08 | 4.36 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.10 | 14.04 | 2.27 | 2.28 | 2 | 2 |
| R8009_M8025__far_ch1 | 15.30 | 15.87 | 3.66 | 4.87 | 2 | 2 |
| R8009_M8026__far_ch1 | 15.96 | 16.07 | 2.68 | 2.74 | 2 | 2 |
| R8009_M8027__far_ch1 | 13.92 | 13.95 | 3.49 | 3.44 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.62 | 13.41 | 6.02 | 5.26 | 2 | 2 |
