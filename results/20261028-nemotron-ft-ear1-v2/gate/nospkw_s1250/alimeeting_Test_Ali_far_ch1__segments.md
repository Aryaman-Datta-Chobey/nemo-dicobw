# Diarization scores: nospkw_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `nospkw_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/nospkw_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T13:51:29+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `nospkw_s1250`
- model: `/mnt/data/exp/nemotron/20261027-nemotron-ft-ear1-nospkw/nemotron_ft_ear1_nospkw/checkpoints/nemotron_ft_ear1_nospkw--val_f1_acc=0.8548-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.30 | 15.16 | 1.51 | 0.64 | 17.92 | 100.00 | 0.00 |
| 0.25 | 9.27 | 8.69 | 0.40 | 0.18 | 11.01 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.96 (IoU 90.76) | 8.00 (IoU 8.04) |
| silence | 0.55 (IoU 0.60) | 7.49 (IoU 46.70) |

Speech P/R/F1: 99.35 / 91.31 / 95.16; miss 8.69 of ref speech, FA 6.87 of ref silence, SAD error 9.30.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12169 | 36.60 | 91.36 | 52.26 | 0.084 | 0.070 | 0.051 | 0.060 |
| 0.25 | offset | 4875 | 12169 | 36.19 | 90.34 | 51.68 | 0.095 | 0.090 | -0.059 | -0.070 |
| 0.25 | all | 9750 | 24338 | 36.40 | 90.85 | 51.97 | 0.090 | 0.080 | -0.004 | -0.010 |
| 0.50 | onset | 4875 | 12169 | 37.64 | 93.95 | 53.74 | 0.091 | 0.080 | 0.056 | 0.060 |
| 0.50 | offset | 4875 | 12169 | 38.16 | 95.26 | 54.49 | 0.107 | 0.100 | -0.064 | -0.080 |
| 0.50 | all | 9750 | 24338 | 37.90 | 94.61 | 54.12 | 0.099 | 0.090 | -0.004 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.58 | 16.88 | 11.62 | 12.14 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.73 | 18.93 | 12.50 | 14.56 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.28 | 16.97 | 10.20 | 11.53 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.48 | 25.16 | 17.44 | 19.77 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.69 | 24.33 | 15.89 | 16.10 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.32 | 12.97 | 9.82 | 9.01 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.60 | 28.45 | 25.75 | 25.11 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.25 | 16.68 | 10.74 | 10.85 | 4 | 4 |
| R8008_M8014__far_ch1 | 13.80 | 14.54 | 9.91 | 10.39 | 3 | 3 |
| R8008_M8015__far_ch1 | 16.44 | 17.87 | 11.73 | 12.38 | 3 | 3 |
| R8008_M8016__far_ch1 | 17.74 | 20.76 | 12.34 | 15.20 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.25 | 13.30 | 7.31 | 7.97 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.18 | 16.10 | 4.10 | 3.96 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.94 | 15.08 | 2.45 | 2.85 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.35 | 17.61 | 3.15 | 4.51 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.89 | 13.80 | 1.98 | 1.97 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.02 | 13.48 | 2.35 | 2.08 | 2 | 2 |
| R8009_M8026__far_ch1 | 15.71 | 15.84 | 2.62 | 2.69 | 2 | 2 |
| R8009_M8027__far_ch1 | 13.31 | 13.39 | 3.35 | 3.33 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.20 | 11.94 | 1.85 | 1.83 | 2 | 2 |
