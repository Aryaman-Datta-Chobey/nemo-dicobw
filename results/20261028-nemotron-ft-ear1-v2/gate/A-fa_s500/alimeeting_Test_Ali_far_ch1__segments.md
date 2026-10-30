# Diarization scores: A-fa_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T20:46:17+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7839-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.06 | 16.36 | 1.14 | 0.57 | 18.76 | 100.00 | 0.00 |
| 0.25 | 10.31 | 9.63 | 0.49 | 0.18 | 12.02 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.14 (IoU 90.12) | 8.82 (IoU 8.84) |
| silence | 0.30 (IoU 0.33) | 7.74 (IoU 45.92) |

Speech P/R/F1: 99.64 / 90.41 / 94.80; miss 9.59 of ref speech, FA 3.73 of ref silence, SAD error 9.91.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12663 | 35.47 | 92.14 | 51.23 | 0.077 | 0.070 | 0.057 | 0.060 |
| 0.25 | offset | 4875 | 12663 | 35.17 | 91.36 | 50.79 | 0.091 | 0.080 | -0.074 | -0.080 |
| 0.25 | all | 9750 | 25326 | 35.32 | 91.75 | 51.01 | 0.084 | 0.080 | -0.008 | 0.000 |
| 0.50 | onset | 4875 | 12663 | 36.45 | 94.69 | 52.64 | 0.085 | 0.070 | 0.062 | 0.060 |
| 0.50 | offset | 4875 | 12663 | 36.94 | 95.96 | 53.35 | 0.102 | 0.090 | -0.082 | -0.080 |
| 0.50 | all | 9750 | 25326 | 36.70 | 95.32 | 52.99 | 0.093 | 0.080 | -0.010 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.74 | 17.07 | 11.31 | 11.80 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.87 | 21.36 | 15.44 | 17.85 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.03 | 16.68 | 10.13 | 11.39 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.16 | 24.77 | 17.29 | 19.45 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.75 | 24.38 | 16.38 | 16.62 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.13 | 12.77 | 9.85 | 9.02 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.42 | 28.33 | 25.37 | 24.84 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.36 | 16.79 | 10.81 | 10.92 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.03 | 16.88 | 11.98 | 12.58 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.67 | 22.45 | 17.89 | 18.27 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.14 | 22.51 | 13.35 | 16.68 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.31 | 16.61 | 12.14 | 12.74 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.51 | 15.44 | 3.75 | 3.61 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.29 | 14.36 | 2.23 | 2.60 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.41 | 17.43 | 2.87 | 3.97 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.74 | 12.69 | 1.16 | 1.17 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.00 | 13.69 | 2.39 | 2.23 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.00 | 17.11 | 3.18 | 3.25 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.59 | 15.55 | 4.34 | 4.25 | 2 | 2 |
| R8009_M8028__far_ch1 | 15.74 | 14.62 | 6.16 | 5.47 | 2 | 2 |
