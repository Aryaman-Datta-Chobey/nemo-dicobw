# Diarization scores: C-fa_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `C-fa_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-fa_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T23:08:01+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `C-fa_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7827-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.19 | 16.73 | 0.93 | 0.53 | 18.95 | 100.00 | 0.00 |
| 0.25 | 10.24 | 9.73 | 0.34 | 0.17 | 12.11 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.21 (IoU 90.22) | 8.75 (IoU 8.77) |
| silence | 0.27 (IoU 0.29) | 7.77 (IoU 46.29) |

Speech P/R/F1: 99.68 / 90.49 / 94.86; miss 9.51 of ref speech, FA 3.34 of ref silence, SAD error 9.81.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12849 | 35.45 | 93.44 | 51.40 | 0.083 | 0.080 | 0.066 | 0.070 |
| 0.25 | offset | 4875 | 12850 | 35.42 | 93.35 | 51.35 | 0.085 | 0.080 | -0.070 | -0.070 |
| 0.25 | all | 9750 | 25699 | 35.43 | 93.39 | 51.38 | 0.084 | 0.080 | -0.002 | 0.000 |
| 0.50 | onset | 4875 | 12849 | 36.43 | 96.02 | 52.82 | 0.090 | 0.080 | 0.071 | 0.070 |
| 0.50 | offset | 4875 | 12850 | 36.84 | 97.11 | 53.42 | 0.094 | 0.080 | -0.076 | -0.070 |
| 0.50 | all | 9750 | 25699 | 36.64 | 96.56 | 53.12 | 0.092 | 0.080 | -0.003 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.33 | 17.63 | 11.73 | 12.22 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.72 | 22.26 | 16.05 | 18.58 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.26 | 16.98 | 10.21 | 11.53 | 4 | 4 |
| R8004_M8006__far_ch1 | 23.24 | 25.86 | 18.16 | 20.24 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.56 | 25.12 | 16.86 | 17.09 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.53 | 13.13 | 10.07 | 9.26 | 4 | 4 |
| R8005_M8009__far_ch1 | 29.38 | 29.23 | 26.20 | 25.68 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.57 | 17.07 | 10.96 | 11.13 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.13 | 16.88 | 11.90 | 12.47 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.05 | 22.92 | 17.98 | 18.36 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.43 | 22.89 | 13.60 | 17.07 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.20 | 16.59 | 12.02 | 12.72 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.27 | 15.21 | 3.48 | 3.35 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.85 | 13.89 | 1.91 | 2.25 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.74 | 16.57 | 2.28 | 3.06 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.29 | 12.22 | 0.93 | 0.92 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.63 | 13.18 | 2.14 | 1.93 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.51 | 16.65 | 2.93 | 3.00 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.49 | 14.40 | 3.46 | 3.33 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.44 | 12.95 | 3.26 | 3.07 | 2 | 2 |
