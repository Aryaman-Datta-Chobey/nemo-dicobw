# Diarization scores: A-fa-r75a_s1750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a_s1750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s1750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T00:26:24+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a_s1750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7783-epoch=6.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.22 | 16.66 | 0.99 | 0.57 | 18.93 | 100.00 | 0.00 |
| 0.25 | 10.26 | 9.81 | 0.28 | 0.17 | 12.05 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.73 (IoU 89.71) | 9.23 (IoU 9.25) |
| silence | 0.26 (IoU 0.28) | 7.78 (IoU 45.07) |

Speech P/R/F1: 99.69 / 89.97 / 94.58; miss 10.03 of ref speech, FA 3.20 of ref silence, SAD error 10.31.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12858 | 35.04 | 92.41 | 50.81 | 0.087 | 0.080 | 0.069 | 0.080 |
| 0.25 | offset | 4875 | 12858 | 34.79 | 91.75 | 50.45 | 0.090 | 0.080 | -0.077 | -0.080 |
| 0.25 | all | 9750 | 25716 | 34.91 | 92.08 | 50.63 | 0.089 | 0.080 | -0.004 | -0.010 |
| 0.50 | onset | 4875 | 12858 | 36.11 | 95.24 | 52.37 | 0.095 | 0.090 | 0.075 | 0.080 |
| 0.50 | offset | 4875 | 12858 | 36.57 | 96.45 | 53.03 | 0.101 | 0.090 | -0.085 | -0.090 |
| 0.50 | all | 9750 | 25716 | 36.34 | 95.85 | 52.70 | 0.098 | 0.090 | -0.006 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.42 | 16.70 | 11.48 | 11.95 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.70 | 21.08 | 15.45 | 17.69 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.07 | 16.75 | 10.07 | 11.37 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.95 | 25.48 | 18.00 | 20.06 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.75 | 24.28 | 16.32 | 16.48 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.31 | 12.91 | 10.09 | 9.16 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.12 | 28.05 | 25.10 | 24.57 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.36 | 16.85 | 10.93 | 11.09 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.23 | 16.96 | 12.25 | 12.77 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.09 | 22.98 | 18.26 | 18.65 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.33 | 22.79 | 13.68 | 17.15 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.75 | 17.08 | 12.53 | 13.16 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.34 | 16.25 | 3.97 | 3.82 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.18 | 15.40 | 2.50 | 2.95 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.22 | 18.40 | 3.30 | 4.66 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.69 | 13.62 | 1.47 | 1.46 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.45 | 14.22 | 2.38 | 2.28 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.31 | 17.41 | 3.01 | 3.04 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.85 | 15.77 | 4.10 | 3.98 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.22 | 12.99 | 2.04 | 2.03 | 2 | 2 |
