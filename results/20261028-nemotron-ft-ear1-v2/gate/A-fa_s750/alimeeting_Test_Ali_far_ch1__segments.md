# Diarization scores: A-fa_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T20:57:26+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7759-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.05 | 16.39 | 1.07 | 0.59 | 18.77 | 100.00 | 0.00 |
| 0.25 | 10.19 | 9.68 | 0.31 | 0.19 | 11.95 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.92 (IoU 89.88) | 9.04 (IoU 9.06) |
| silence | 0.30 (IoU 0.33) | 7.74 (IoU 45.33) |

Speech P/R/F1: 99.64 / 90.17 / 94.67; miss 9.83 of ref speech, FA 3.72 of ref silence, SAD error 10.15.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12685 | 35.08 | 91.28 | 50.68 | 0.083 | 0.080 | 0.064 | 0.070 |
| 0.25 | offset | 4875 | 12685 | 34.92 | 90.87 | 50.46 | 0.091 | 0.080 | -0.073 | -0.080 |
| 0.25 | all | 9750 | 25370 | 35.00 | 91.08 | 50.57 | 0.087 | 0.080 | -0.004 | 0.000 |
| 0.50 | onset | 4875 | 12685 | 36.11 | 93.95 | 52.16 | 0.090 | 0.080 | 0.069 | 0.070 |
| 0.50 | offset | 4875 | 12685 | 36.73 | 95.57 | 53.06 | 0.102 | 0.090 | -0.081 | -0.080 |
| 0.50 | all | 9750 | 25370 | 36.42 | 94.76 | 52.61 | 0.096 | 0.090 | -0.007 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.56 | 16.86 | 11.22 | 11.70 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.72 | 21.25 | 15.38 | 17.82 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.96 | 16.70 | 10.11 | 11.47 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.04 | 24.55 | 17.23 | 19.30 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.35 | 24.03 | 16.10 | 16.36 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.95 | 12.56 | 9.77 | 8.89 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.98 | 27.82 | 24.98 | 24.37 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.22 | 16.64 | 10.70 | 10.79 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.19 | 16.97 | 12.23 | 12.83 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.07 | 22.93 | 18.25 | 18.69 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.42 | 22.80 | 13.47 | 16.81 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.57 | 16.88 | 12.38 | 12.99 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.20 | 16.11 | 4.08 | 3.93 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.76 | 14.87 | 2.47 | 2.84 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.29 | 18.33 | 3.40 | 4.65 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.44 | 13.37 | 1.43 | 1.42 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.26 | 13.89 | 2.51 | 2.30 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.44 | 17.55 | 3.30 | 3.37 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.11 | 16.06 | 4.57 | 4.47 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.02 | 12.76 | 2.20 | 2.17 | 2 | 2 |
