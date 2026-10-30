# Diarization scores: A-fa-r75b_s2000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b_s2000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s2000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T03:02:28+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b_s2000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7799-epoch=7.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.17 | 16.54 | 1.03 | 0.59 | 18.86 | 100.00 | 0.00 |
| 0.25 | 10.22 | 9.73 | 0.30 | 0.18 | 12.01 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.82 (IoU 89.80) | 9.14 (IoU 9.16) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 45.27) |

Speech P/R/F1: 99.68 / 90.06 / 94.63; miss 9.94 of ref speech, FA 3.29 of ref silence, SAD error 10.22.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12871 | 35.23 | 93.01 | 51.10 | 0.086 | 0.080 | 0.067 | 0.070 |
| 0.25 | offset | 4875 | 12872 | 34.84 | 91.98 | 50.53 | 0.091 | 0.090 | -0.079 | -0.080 |
| 0.25 | all | 9750 | 25743 | 35.03 | 92.49 | 50.82 | 0.089 | 0.080 | -0.006 | -0.010 |
| 0.50 | onset | 4875 | 12871 | 36.21 | 95.61 | 52.53 | 0.093 | 0.080 | 0.071 | 0.080 |
| 0.50 | offset | 4875 | 12872 | 36.54 | 96.47 | 53.00 | 0.101 | 0.090 | -0.086 | -0.090 |
| 0.50 | all | 9750 | 25743 | 36.37 | 96.04 | 52.77 | 0.097 | 0.090 | -0.008 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.15 | 16.41 | 11.43 | 11.87 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.92 | 21.38 | 15.62 | 18.01 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.19 | 16.87 | 10.16 | 11.45 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.98 | 25.54 | 17.99 | 20.07 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.88 | 24.47 | 16.30 | 16.48 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.22 | 12.83 | 9.99 | 9.07 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.25 | 28.02 | 25.25 | 24.57 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.34 | 16.80 | 10.88 | 10.98 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.23 | 17.00 | 12.24 | 12.80 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.76 | 22.60 | 18.04 | 18.45 | 3 | 3 |
| R8008_M8016__far_ch1 | 18.99 | 22.30 | 13.50 | 16.84 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.70 | 16.99 | 12.45 | 13.07 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.38 | 16.29 | 4.02 | 3.86 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.93 | 15.10 | 2.35 | 2.76 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.96 | 18.08 | 3.08 | 4.34 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.80 | 13.73 | 1.60 | 1.58 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.23 | 13.91 | 2.27 | 2.11 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.19 | 17.29 | 2.94 | 2.97 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.67 | 15.57 | 3.99 | 3.86 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.05 | 12.80 | 2.06 | 2.05 | 2 | 2 |
