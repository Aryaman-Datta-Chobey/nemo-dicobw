# Diarization scores: 20261028-nemotron-ft-ear1-gate/alimeeting_Test_Ali_far_ch1__segments

- name: `20261028-nemotron-ft-ear1-gate/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-gate/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `fc37f2be83fbf068078ef6c18ed77f86935a0b07-dirty`
- created: `2026-10-28T05:16:06+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `20261028-nemotron-ft-ear1-gate`
- model: `/mnt/data/exp/nemotron/20261027-nemotron-ft-ear1-nospkw/nemotron_ft_ear1_nospkw/checkpoints/nemotron_ft_ear1_nospkw--val_f1_acc=0.8342-epoch=6.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.44 | 15.31 | 1.49 | 0.64 | 18.04 | 100.00 | 0.00 |
| 0.25 | 9.30 | 8.77 | 0.35 | 0.18 | 11.01 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.85 (IoU 90.66) | 8.11 (IoU 8.15) |
| silence | 0.53 (IoU 0.57) | 7.51 (IoU 46.53) |

Speech P/R/F1: 99.38 / 91.18 / 95.10; miss 8.82 of ref speech, FA 6.53 of ref silence, SAD error 9.39.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12206 | 36.36 | 91.04 | 51.96 | 0.086 | 0.080 | 0.054 | 0.060 |
| 0.25 | offset | 4875 | 12206 | 36.04 | 90.24 | 51.51 | 0.096 | 0.090 | -0.060 | -0.080 |
| 0.25 | all | 9750 | 24412 | 36.20 | 90.64 | 51.74 | 0.091 | 0.090 | -0.003 | -0.010 |
| 0.50 | onset | 4875 | 12206 | 37.42 | 93.70 | 53.49 | 0.093 | 0.080 | 0.059 | 0.060 |
| 0.50 | offset | 4875 | 12206 | 37.92 | 94.93 | 54.19 | 0.107 | 0.100 | -0.066 | -0.080 |
| 0.50 | all | 9750 | 24412 | 37.67 | 94.32 | 53.84 | 0.100 | 0.090 | -0.004 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.56 | 16.84 | 11.66 | 12.17 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.73 | 18.88 | 12.31 | 14.26 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.42 | 17.16 | 10.27 | 11.62 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.65 | 25.29 | 17.50 | 19.76 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.59 | 24.19 | 15.73 | 15.92 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.41 | 13.04 | 9.84 | 9.00 | 4 | 4 |
| R8005_M8009__far_ch1 | 29.08 | 28.95 | 25.86 | 25.34 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.11 | 16.50 | 10.45 | 10.54 | 4 | 4 |
| R8008_M8014__far_ch1 | 13.85 | 14.60 | 10.01 | 10.51 | 3 | 3 |
| R8008_M8015__far_ch1 | 16.42 | 17.94 | 11.56 | 12.24 | 3 | 3 |
| R8008_M8016__far_ch1 | 17.00 | 20.08 | 11.49 | 14.40 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.65 | 13.69 | 8.11 | 8.70 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.53 | 16.44 | 4.31 | 4.15 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.09 | 15.25 | 2.50 | 2.92 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.75 | 17.96 | 3.24 | 4.61 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.27 | 14.19 | 2.28 | 2.29 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.04 | 13.48 | 2.34 | 2.07 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.21 | 16.34 | 2.77 | 2.83 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.07 | 14.11 | 3.54 | 3.50 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.39 | 12.14 | 1.86 | 1.84 | 2 | 2 |
