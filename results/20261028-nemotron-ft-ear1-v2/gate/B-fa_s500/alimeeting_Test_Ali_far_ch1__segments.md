# Diarization scores: B-fa_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `B-fa_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-fa_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T21:55:43+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `B-fa_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7806-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.29 | 16.88 | 0.89 | 0.52 | 19.06 | 100.00 | 0.00 |
| 0.25 | 10.32 | 9.81 | 0.34 | 0.17 | 12.20 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.12 (IoU 90.14) | 8.84 (IoU 8.86) |
| silence | 0.26 (IoU 0.28) | 7.78 (IoU 46.12) |

Speech P/R/F1: 99.69 / 90.39 / 94.81; miss 9.61 of ref speech, FA 3.19 of ref silence, SAD error 9.89.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12912 | 35.31 | 93.52 | 51.26 | 0.085 | 0.080 | 0.069 | 0.070 |
| 0.25 | offset | 4875 | 12913 | 35.41 | 93.81 | 51.42 | 0.084 | 0.080 | -0.070 | -0.070 |
| 0.25 | all | 9750 | 25825 | 35.36 | 93.66 | 51.34 | 0.085 | 0.080 | -0.001 | 0.000 |
| 0.50 | onset | 4875 | 12912 | 36.29 | 96.12 | 52.69 | 0.092 | 0.080 | 0.075 | 0.080 |
| 0.50 | offset | 4875 | 12913 | 36.68 | 97.15 | 53.25 | 0.092 | 0.080 | -0.076 | -0.070 |
| 0.50 | all | 9750 | 25825 | 36.48 | 96.64 | 52.97 | 0.092 | 0.080 | -0.001 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.32 | 17.60 | 11.78 | 12.26 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.84 | 22.35 | 16.12 | 18.64 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.20 | 16.92 | 10.23 | 11.56 | 4 | 4 |
| R8004_M8006__far_ch1 | 23.37 | 26.05 | 18.44 | 20.57 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.59 | 25.15 | 16.92 | 17.12 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.70 | 13.30 | 10.26 | 9.45 | 4 | 4 |
| R8005_M8009__far_ch1 | 29.58 | 29.49 | 26.37 | 25.90 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.69 | 17.22 | 11.01 | 11.20 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.31 | 17.07 | 12.03 | 12.61 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.38 | 23.19 | 18.26 | 18.66 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.62 | 23.10 | 13.70 | 17.18 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.27 | 16.63 | 12.08 | 12.75 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.50 | 15.44 | 3.53 | 3.40 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.96 | 13.98 | 1.94 | 2.26 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.68 | 16.46 | 2.14 | 2.87 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.38 | 12.31 | 0.93 | 0.93 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.62 | 13.23 | 2.13 | 1.95 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.49 | 16.62 | 2.88 | 2.94 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.57 | 14.48 | 3.39 | 3.26 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.61 | 13.10 | 3.38 | 3.18 | 2 | 2 |
