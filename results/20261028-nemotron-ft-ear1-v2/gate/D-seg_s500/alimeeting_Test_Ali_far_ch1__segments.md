# Diarization scores: D-seg_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `D-seg_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-seg_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T18:45:49+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `D-seg_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7987-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 16.31 | 14.59 | 1.16 | 0.55 | 17.44 | 100.00 | 0.00 |
| 0.25 | 9.09 | 8.66 | 0.28 | 0.15 | 11.18 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 85.88 (IoU 92.79) | 6.08 (IoU 6.12) |
| silence | 0.59 (IoU 0.63) | 7.45 (IoU 52.73) |

Speech P/R/F1: 99.31 / 93.39 / 96.26; miss 6.61 of ref speech, FA 7.39 of ref silence, SAD error 7.26.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12565 | 37.26 | 96.04 | 53.69 | 0.063 | 0.050 | 0.011 | 0.010 |
| 0.25 | offset | 4875 | 12566 | 36.89 | 95.08 | 53.15 | 0.066 | 0.060 | -0.039 | -0.040 |
| 0.25 | all | 9750 | 25131 | 37.07 | 95.56 | 53.42 | 0.065 | 0.050 | -0.014 | -0.010 |
| 0.50 | onset | 4875 | 12565 | 37.65 | 97.05 | 54.25 | 0.066 | 0.060 | 0.012 | 0.010 |
| 0.50 | offset | 4875 | 12566 | 37.74 | 97.27 | 54.38 | 0.072 | 0.060 | -0.041 | -0.040 |
| 0.50 | all | 9750 | 25131 | 37.69 | 97.16 | 54.32 | 0.069 | 0.060 | -0.015 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.10 | 16.54 | 10.73 | 11.32 | 4 | 4 |
| R8002_M8003__far_ch1 | 18.96 | 20.63 | 13.92 | 16.49 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.11 | 17.19 | 9.35 | 10.97 | 4 | 4 |
| R8004_M8006__far_ch1 | 24.66 | 27.70 | 18.93 | 21.49 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.99 | 25.60 | 16.61 | 16.79 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.10 | 12.97 | 9.00 | 8.52 | 4 | 4 |
| R8005_M8009__far_ch1 | 30.04 | 30.30 | 26.60 | 26.47 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.15 | 16.86 | 10.01 | 10.50 | 4 | 4 |
| R8008_M8014__far_ch1 | 13.74 | 14.85 | 9.80 | 10.67 | 3 | 3 |
| R8008_M8015__far_ch1 | 20.15 | 21.35 | 15.92 | 16.55 | 3 | 3 |
| R8008_M8016__far_ch1 | 16.46 | 20.11 | 11.08 | 14.78 | 3 | 3 |
| R8008_M8017__far_ch1 | 13.38 | 14.83 | 9.72 | 10.55 | 3 | 3 |
| R8009_M8021__far_ch1 | 10.22 | 10.14 | 2.43 | 2.33 | 2 | 2 |
| R8009_M8022__far_ch1 | 9.50 | 10.48 | 1.14 | 1.47 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.60 | 12.46 | 1.25 | 1.97 | 2 | 2 |
| R8009_M8024__far_ch1 | 8.46 | 8.27 | 0.64 | 0.64 | 2 | 2 |
| R8009_M8025__far_ch1 | 9.24 | 9.47 | 0.74 | 0.76 | 2 | 2 |
| R8009_M8026__far_ch1 | 11.91 | 11.99 | 1.61 | 1.65 | 2 | 2 |
| R8009_M8027__far_ch1 | 9.66 | 9.74 | 1.99 | 1.94 | 2 | 2 |
| R8009_M8028__far_ch1 | 8.53 | 8.32 | 0.87 | 0.86 | 2 | 2 |
