# Diarization scores: B-fa_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `B-fa_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-fa_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T22:06:44+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `B-fa_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7709-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.17 | 16.64 | 1.00 | 0.53 | 18.91 | 100.00 | 0.00 |
| 0.25 | 10.33 | 9.70 | 0.45 | 0.18 | 12.13 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.20 (IoU 90.21) | 8.76 (IoU 8.78) |
| silence | 0.27 (IoU 0.30) | 7.77 (IoU 46.26) |

Speech P/R/F1: 99.68 / 90.48 / 94.85; miss 9.52 of ref speech, FA 3.37 of ref silence, SAD error 9.82.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12823 | 35.37 | 93.05 | 51.26 | 0.087 | 0.080 | 0.072 | 0.080 |
| 0.25 | offset | 4875 | 12824 | 35.52 | 93.44 | 51.47 | 0.081 | 0.070 | -0.064 | -0.060 |
| 0.25 | all | 9750 | 25647 | 35.45 | 93.24 | 51.37 | 0.084 | 0.080 | 0.004 | 0.000 |
| 0.50 | onset | 4875 | 12823 | 36.41 | 95.77 | 52.76 | 0.094 | 0.090 | 0.078 | 0.080 |
| 0.50 | offset | 4875 | 12824 | 36.83 | 96.88 | 53.37 | 0.089 | 0.070 | -0.070 | -0.070 |
| 0.50 | all | 9750 | 25647 | 36.62 | 96.33 | 53.07 | 0.092 | 0.080 | 0.003 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.34 | 17.64 | 11.69 | 12.17 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.60 | 22.10 | 15.93 | 18.41 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.02 | 16.71 | 10.12 | 11.44 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.97 | 25.55 | 18.18 | 20.24 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.01 | 24.58 | 16.72 | 16.95 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.40 | 13.03 | 10.01 | 9.21 | 4 | 4 |
| R8005_M8009__far_ch1 | 29.20 | 29.06 | 26.08 | 25.56 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.62 | 17.16 | 10.95 | 11.16 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.18 | 16.92 | 11.94 | 12.50 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.33 | 23.13 | 18.17 | 18.51 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.49 | 22.92 | 13.57 | 17.00 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.14 | 16.52 | 11.92 | 12.62 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.35 | 15.28 | 3.53 | 3.40 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.87 | 13.95 | 1.93 | 2.30 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.61 | 16.45 | 2.28 | 3.04 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.29 | 12.21 | 0.98 | 0.97 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.62 | 13.17 | 2.16 | 1.95 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.54 | 16.71 | 2.91 | 2.99 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.65 | 14.59 | 3.59 | 3.47 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.86 | 13.95 | 5.17 | 4.66 | 2 | 2 |
