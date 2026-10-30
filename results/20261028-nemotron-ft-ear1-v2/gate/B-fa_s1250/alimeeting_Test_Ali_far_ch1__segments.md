# Diarization scores: B-fa_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `B-fa_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-fa_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T22:29:02+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `B-fa_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7726-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.00 | 16.39 | 1.08 | 0.53 | 18.70 | 100.00 | 0.00 |
| 0.25 | 10.25 | 9.60 | 0.47 | 0.17 | 11.97 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.22 (IoU 90.22) | 8.74 (IoU 8.76) |
| silence | 0.28 (IoU 0.31) | 7.76 (IoU 46.24) |

Speech P/R/F1: 99.66 / 90.50 / 94.86; miss 9.50 of ref speech, FA 3.52 of ref silence, SAD error 9.81.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12721 | 35.44 | 92.47 | 51.24 | 0.083 | 0.080 | 0.067 | 0.070 |
| 0.25 | offset | 4875 | 12722 | 35.51 | 92.68 | 51.35 | 0.083 | 0.070 | -0.065 | -0.070 |
| 0.25 | all | 9750 | 25443 | 35.48 | 92.57 | 51.29 | 0.083 | 0.070 | 0.001 | 0.000 |
| 0.50 | onset | 4875 | 12721 | 36.45 | 95.12 | 52.71 | 0.091 | 0.080 | 0.073 | 0.070 |
| 0.50 | offset | 4875 | 12722 | 36.97 | 96.47 | 53.45 | 0.092 | 0.080 | -0.072 | -0.070 |
| 0.50 | all | 9750 | 25443 | 36.71 | 95.79 | 53.08 | 0.092 | 0.080 | 0.000 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.15 | 17.49 | 11.58 | 12.07 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.80 | 21.20 | 15.34 | 17.59 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.80 | 16.51 | 9.94 | 11.30 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.44 | 25.01 | 17.58 | 19.61 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.48 | 24.06 | 16.36 | 16.60 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.15 | 12.78 | 9.83 | 9.00 | 4 | 4 |
| R8005_M8009__far_ch1 | 29.07 | 28.91 | 25.95 | 25.38 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.43 | 16.93 | 10.81 | 10.94 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.12 | 16.88 | 11.92 | 12.50 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.88 | 22.66 | 17.91 | 18.22 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.12 | 22.51 | 13.33 | 16.69 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.08 | 16.45 | 11.89 | 12.58 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.27 | 15.19 | 3.53 | 3.39 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.12 | 14.22 | 2.06 | 2.44 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.79 | 16.68 | 2.48 | 3.32 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.31 | 12.24 | 1.00 | 1.00 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.76 | 13.24 | 2.39 | 2.10 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.64 | 16.78 | 3.02 | 3.10 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.04 | 14.99 | 3.92 | 3.82 | 2 | 2 |
| R8009_M8028__far_ch1 | 15.18 | 14.15 | 5.62 | 5.01 | 2 | 2 |
