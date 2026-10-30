# Diarization scores: A-fa-r0_s375/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0_s375/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s375/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T17:24:35+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0_s375`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7741-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.13 | 16.77 | 0.87 | 0.49 | 18.91 | 100.00 | 0.00 |
| 0.25 | 10.10 | 9.70 | 0.25 | 0.16 | 12.01 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.29 (IoU 90.30) | 8.67 (IoU 8.69) |
| silence | 0.28 (IoU 0.31) | 7.76 (IoU 46.43) |

Speech P/R/F1: 99.66 / 90.58 / 94.90; miss 9.42 of ref speech, FA 3.53 of ref silence, SAD error 9.73.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12851 | 35.48 | 93.54 | 51.45 | 0.098 | 0.100 | 0.085 | 0.090 |
| 0.25 | offset | 4875 | 12851 | 36.00 | 94.89 | 52.19 | 0.073 | 0.060 | -0.053 | -0.050 |
| 0.25 | all | 9750 | 25702 | 35.74 | 94.22 | 51.82 | 0.085 | 0.080 | 0.016 | 0.010 |
| 0.50 | onset | 4875 | 12851 | 36.55 | 96.35 | 53.00 | 0.105 | 0.100 | 0.090 | 0.100 |
| 0.50 | offset | 4875 | 12851 | 36.84 | 97.11 | 53.41 | 0.079 | 0.070 | -0.056 | -0.050 |
| 0.50 | all | 9750 | 25702 | 36.69 | 96.73 | 53.20 | 0.092 | 0.080 | 0.017 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.58 | 17.90 | 11.43 | 11.90 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.88 | 21.30 | 15.22 | 17.43 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.05 | 16.87 | 10.06 | 11.52 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.29 | 24.77 | 17.55 | 19.60 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.13 | 24.68 | 16.72 | 16.95 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.47 | 13.09 | 9.99 | 9.20 | 4 | 4 |
| R8005_M8009__far_ch1 | 32.89 | 33.02 | 29.06 | 28.94 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.86 | 17.30 | 11.01 | 11.18 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.05 | 16.80 | 11.84 | 12.40 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.82 | 22.52 | 17.86 | 18.10 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.40 | 22.89 | 13.31 | 16.70 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.34 | 16.63 | 12.07 | 12.67 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.18 | 15.12 | 3.57 | 3.44 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.33 | 13.38 | 1.71 | 2.10 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.22 | 15.89 | 1.71 | 2.19 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.57 | 12.49 | 0.92 | 0.91 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.56 | 13.10 | 2.12 | 1.88 | 2 | 2 |
| R8009_M8026__far_ch1 | 15.56 | 15.71 | 2.24 | 2.29 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.14 | 14.05 | 3.15 | 3.03 | 2 | 2 |
| R8009_M8028__far_ch1 | 11.58 | 11.45 | 1.19 | 1.22 | 2 | 2 |
