# Diarization scores: B-seg_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `B-seg_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-seg_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T16:49:03+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `B-seg_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8297-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 16.56 | 14.11 | 1.83 | 0.62 | 17.11 | 100.00 | 0.00 |
| 0.25 | 8.60 | 7.76 | 0.64 | 0.19 | 10.26 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 84.74 (IoU 91.49) | 7.22 (IoU 7.27) |
| silence | 0.66 (IoU 0.71) | 7.39 (IoU 48.39) |

Speech P/R/F1: 99.23 / 92.15 / 95.56; miss 7.85 of ref speech, FA 8.15 of ref silence, SAD error 8.57.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11555 | 38.77 | 91.90 | 54.53 | 0.086 | 0.080 | 0.046 | 0.060 |
| 0.25 | offset | 4875 | 11557 | 37.99 | 90.07 | 53.44 | 0.094 | 0.090 | -0.053 | -0.070 |
| 0.25 | all | 9750 | 23112 | 38.38 | 90.98 | 53.99 | 0.090 | 0.080 | -0.003 | -0.010 |
| 0.50 | onset | 4875 | 11555 | 39.71 | 94.13 | 55.86 | 0.092 | 0.080 | 0.049 | 0.060 |
| 0.50 | offset | 4875 | 11557 | 40.06 | 94.97 | 56.35 | 0.106 | 0.090 | -0.058 | -0.070 |
| 0.50 | all | 9750 | 23112 | 39.89 | 94.55 | 56.11 | 0.099 | 0.090 | -0.004 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.70 | 17.02 | 11.39 | 11.87 | 4 | 4 |
| R8002_M8003__far_ch1 | 18.21 | 19.47 | 13.03 | 15.23 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.77 | 16.39 | 9.91 | 11.19 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.59 | 24.19 | 16.60 | 19.05 | 4 | 4 |
| R8005_M8007__far_ch1 | 22.92 | 23.55 | 15.52 | 15.79 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.37 | 12.11 | 8.98 | 8.26 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.22 | 27.07 | 24.29 | 23.74 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.11 | 16.50 | 10.43 | 10.48 | 4 | 4 |
| R8008_M8014__far_ch1 | 13.63 | 14.29 | 9.47 | 9.90 | 3 | 3 |
| R8008_M8015__far_ch1 | 12.57 | 14.30 | 7.30 | 8.30 | 3 | 3 |
| R8008_M8016__far_ch1 | 16.27 | 19.29 | 10.64 | 13.08 | 3 | 3 |
| R8008_M8017__far_ch1 | 10.41 | 11.34 | 4.08 | 4.77 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.59 | 15.52 | 3.71 | 3.58 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.87 | 13.90 | 1.99 | 2.38 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.58 | 17.43 | 2.94 | 3.78 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.93 | 12.87 | 1.19 | 1.19 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.58 | 14.19 | 2.72 | 2.64 | 2 | 2 |
| R8009_M8026__far_ch1 | 15.11 | 15.34 | 2.47 | 2.58 | 2 | 2 |
| R8009_M8027__far_ch1 | 9.61 | 9.45 | 1.90 | 1.86 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.06 | 13.18 | 4.99 | 4.49 | 2 | 2 |
