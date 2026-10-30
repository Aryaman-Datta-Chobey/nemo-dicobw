# Diarization scores: A-fa-t2r50-seed43_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r50-seed43_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50-seed43_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T21:10:18+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r50-seed43_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7884-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.25 | 16.47 | 1.18 | 0.59 | 18.88 | 100.00 | 0.00 |
| 0.25 | 10.44 | 9.69 | 0.54 | 0.21 | 12.10 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.87 (IoU 89.85) | 9.09 (IoU 9.12) |
| silence | 0.27 (IoU 0.30) | 7.77 (IoU 45.36) |

Speech P/R/F1: 99.68 / 90.11 / 94.65; miss 9.89 of ref speech, FA 3.35 of ref silence, SAD error 10.18.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12715 | 35.17 | 91.73 | 50.85 | 0.085 | 0.080 | 0.066 | 0.070 |
| 0.25 | offset | 4875 | 12715 | 35.11 | 91.57 | 50.76 | 0.090 | 0.080 | -0.075 | -0.080 |
| 0.25 | all | 9750 | 25430 | 35.14 | 91.65 | 50.80 | 0.087 | 0.080 | -0.005 | -0.000 |
| 0.50 | onset | 4875 | 12715 | 36.26 | 94.58 | 52.43 | 0.093 | 0.080 | 0.071 | 0.080 |
| 0.50 | offset | 4875 | 12715 | 36.81 | 96.00 | 53.21 | 0.100 | 0.090 | -0.083 | -0.080 |
| 0.50 | all | 9750 | 25430 | 36.54 | 95.29 | 52.82 | 0.096 | 0.090 | -0.007 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.23 | 16.51 | 11.27 | 11.72 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.47 | 20.82 | 15.27 | 17.47 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.91 | 16.58 | 10.06 | 11.31 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.35 | 24.97 | 17.44 | 19.57 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.59 | 24.23 | 16.20 | 16.43 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.93 | 12.57 | 9.73 | 8.86 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.93 | 27.82 | 24.96 | 24.41 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.28 | 16.72 | 10.78 | 10.91 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.98 | 16.72 | 11.99 | 12.53 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.70 | 22.53 | 17.87 | 18.22 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.18 | 22.50 | 13.54 | 16.87 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.58 | 16.87 | 12.40 | 13.02 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.14 | 16.06 | 3.96 | 3.82 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.86 | 14.95 | 2.41 | 2.77 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.10 | 18.02 | 3.01 | 4.12 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.73 | 13.70 | 1.55 | 1.57 | 2 | 2 |
| R8009_M8025__far_ch1 | 15.59 | 16.06 | 3.69 | 4.63 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.57 | 17.68 | 3.25 | 3.32 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.96 | 15.92 | 4.25 | 4.17 | 2 | 2 |
| R8009_M8028__far_ch1 | 17.06 | 15.67 | 7.22 | 6.31 | 2 | 2 |
