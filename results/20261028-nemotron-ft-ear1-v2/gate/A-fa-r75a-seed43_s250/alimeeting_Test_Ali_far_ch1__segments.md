# Diarization scores: A-fa-r75a-seed43_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a-seed43_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T04:10:32+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a-seed43_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7693-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.23 | 16.62 | 1.08 | 0.54 | 18.87 | 100.00 | 0.00 |
| 0.25 | 10.31 | 9.72 | 0.44 | 0.16 | 12.00 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.78 (IoU 89.78) | 9.18 (IoU 9.20) |
| silence | 0.25 (IoU 0.27) | 7.79 (IoU 45.26) |

Speech P/R/F1: 99.70 / 90.02 / 94.61; miss 9.98 of ref speech, FA 3.07 of ref silence, SAD error 10.25.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12835 | 35.15 | 92.53 | 50.94 | 0.086 | 0.080 | 0.069 | 0.080 |
| 0.25 | offset | 4875 | 12835 | 35.07 | 92.33 | 50.83 | 0.090 | 0.080 | -0.078 | -0.080 |
| 0.25 | all | 9750 | 25670 | 35.11 | 92.43 | 50.89 | 0.088 | 0.080 | -0.004 | -0.010 |
| 0.50 | onset | 4875 | 12835 | 36.23 | 95.38 | 52.51 | 0.094 | 0.090 | 0.074 | 0.080 |
| 0.50 | offset | 4875 | 12835 | 36.67 | 96.53 | 53.15 | 0.099 | 0.090 | -0.085 | -0.080 |
| 0.50 | all | 9750 | 25670 | 36.45 | 95.96 | 52.83 | 0.097 | 0.090 | -0.006 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.37 | 16.61 | 11.40 | 11.83 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.14 | 21.36 | 15.66 | 17.83 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.98 | 16.59 | 10.04 | 11.31 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.57 | 25.10 | 17.59 | 19.69 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.88 | 24.44 | 16.24 | 16.42 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.25 | 12.90 | 9.96 | 9.07 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.97 | 27.80 | 24.95 | 24.34 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.26 | 16.70 | 10.70 | 10.80 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.17 | 16.85 | 12.10 | 12.58 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.98 | 22.73 | 18.20 | 18.47 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.42 | 22.70 | 13.74 | 17.10 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.53 | 16.79 | 12.35 | 12.91 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.95 | 15.88 | 3.72 | 3.58 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.83 | 14.97 | 2.28 | 2.66 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.71 | 17.68 | 2.90 | 3.97 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.54 | 13.50 | 1.42 | 1.44 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.42 | 14.13 | 2.44 | 2.28 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.49 | 17.64 | 3.26 | 3.35 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.92 | 15.85 | 4.10 | 4.00 | 2 | 2 |
| R8009_M8028__far_ch1 | 15.61 | 14.73 | 5.08 | 4.63 | 2 | 2 |
