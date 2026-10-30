# Diarization scores: D-fa_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `D-fa_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-fa_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T23:53:57+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `D-fa_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7695-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 19.09 | 17.95 | 0.71 | 0.43 | 19.80 | 100.00 | 0.00 |
| 0.25 | 10.75 | 10.43 | 0.19 | 0.12 | 12.68 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.80 (IoU 89.80) | 9.16 (IoU 9.18) |
| silence | 0.25 (IoU 0.27) | 7.79 (IoU 45.31) |

Speech P/R/F1: 99.70 / 90.04 / 94.63; miss 9.96 of ref speech, FA 3.08 of ref silence, SAD error 10.23.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13233 | 34.50 | 93.64 | 50.42 | 0.078 | 0.070 | 0.056 | 0.060 |
| 0.25 | offset | 4875 | 13233 | 34.07 | 92.47 | 49.79 | 0.092 | 0.090 | -0.083 | -0.090 |
| 0.25 | all | 9750 | 26466 | 34.28 | 93.06 | 50.10 | 0.085 | 0.080 | -0.013 | -0.010 |
| 0.50 | onset | 4875 | 13233 | 35.34 | 95.94 | 51.66 | 0.084 | 0.070 | 0.061 | 0.060 |
| 0.50 | offset | 4875 | 13233 | 35.75 | 97.05 | 52.25 | 0.103 | 0.090 | -0.091 | -0.090 |
| 0.50 | all | 9750 | 26466 | 35.55 | 96.49 | 51.95 | 0.093 | 0.080 | -0.016 | -0.020 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.42 | 17.67 | 12.07 | 12.57 | 4 | 4 |
| R8002_M8003__far_ch1 | 21.13 | 22.59 | 16.01 | 18.35 | 4 | 4 |
| R8004_M8005__far_ch1 | 16.21 | 18.04 | 10.61 | 12.04 | 4 | 4 |
| R8004_M8006__far_ch1 | 26.23 | 28.85 | 20.91 | 23.06 | 4 | 4 |
| R8005_M8007__far_ch1 | 26.12 | 26.57 | 17.81 | 17.92 | 4 | 4 |
| R8005_M8008__far_ch1 | 14.43 | 13.96 | 10.58 | 9.70 | 4 | 4 |
| R8005_M8009__far_ch1 | 31.23 | 30.70 | 27.77 | 26.85 | 4 | 4 |
| R8006_M8012__far_ch1 | 17.64 | 18.07 | 11.65 | 11.89 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.39 | 17.17 | 12.08 | 12.65 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.69 | 23.47 | 18.52 | 18.94 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.64 | 23.09 | 13.80 | 17.34 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.84 | 17.15 | 12.35 | 13.00 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.48 | 15.42 | 3.62 | 3.49 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.91 | 15.08 | 2.35 | 2.75 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.42 | 17.63 | 2.93 | 4.15 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.02 | 12.95 | 1.27 | 1.27 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.05 | 13.87 | 2.22 | 2.13 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.97 | 17.09 | 3.16 | 3.23 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.31 | 15.24 | 3.91 | 3.79 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.77 | 12.56 | 1.89 | 1.88 | 2 | 2 |
