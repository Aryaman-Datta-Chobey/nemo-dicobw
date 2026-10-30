# Diarization scores: B-fa_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `B-fa_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-fa_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T21:44:48+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `B-fa_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7744-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.44 | 17.09 | 0.86 | 0.50 | 19.16 | 100.00 | 0.00 |
| 0.25 | 10.22 | 9.84 | 0.24 | 0.14 | 12.06 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.86 (IoU 89.86) | 9.10 (IoU 9.12) |
| silence | 0.25 (IoU 0.27) | 7.79 (IoU 45.47) |

Speech P/R/F1: 99.70 / 90.10 / 94.66; miss 9.90 of ref speech, FA 3.05 of ref silence, SAD error 10.16.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13027 | 35.19 | 94.03 | 51.21 | 0.089 | 0.090 | 0.072 | 0.080 |
| 0.25 | offset | 4875 | 13027 | 35.07 | 93.70 | 51.03 | 0.088 | 0.080 | -0.076 | -0.080 |
| 0.25 | all | 9750 | 26054 | 35.13 | 93.87 | 51.12 | 0.089 | 0.080 | -0.002 | 0.000 |
| 0.50 | onset | 4875 | 13027 | 36.17 | 96.66 | 52.64 | 0.096 | 0.090 | 0.077 | 0.080 |
| 0.50 | offset | 4875 | 13027 | 36.44 | 97.37 | 53.03 | 0.097 | 0.080 | -0.083 | -0.080 |
| 0.50 | all | 9750 | 26054 | 36.31 | 97.02 | 52.84 | 0.096 | 0.090 | -0.003 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.30 | 17.58 | 11.87 | 12.39 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.56 | 21.92 | 15.84 | 18.10 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.52 | 17.21 | 10.22 | 11.50 | 4 | 4 |
| R8004_M8006__far_ch1 | 23.72 | 26.36 | 18.40 | 20.43 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.93 | 25.40 | 16.80 | 16.91 | 4 | 4 |
| R8005_M8008__far_ch1 | 14.00 | 13.56 | 10.40 | 9.50 | 4 | 4 |
| R8005_M8009__far_ch1 | 29.32 | 29.16 | 26.00 | 25.46 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.58 | 17.02 | 10.82 | 10.95 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.17 | 16.65 | 11.81 | 12.08 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.67 | 22.47 | 17.66 | 18.17 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.85 | 23.39 | 13.82 | 17.26 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.86 | 17.18 | 12.55 | 13.18 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.13 | 16.06 | 3.74 | 3.60 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.40 | 14.47 | 2.06 | 2.41 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.29 | 17.20 | 2.45 | 3.39 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.39 | 13.30 | 1.40 | 1.38 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.17 | 13.70 | 2.26 | 2.04 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.53 | 16.67 | 2.66 | 2.70 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.79 | 14.70 | 3.17 | 3.05 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.82 | 12.61 | 1.65 | 1.67 | 2 | 2 |
