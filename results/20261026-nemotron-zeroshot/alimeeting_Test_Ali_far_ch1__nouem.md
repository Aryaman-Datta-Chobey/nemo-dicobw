# Diarization scores: 20261026-nemotron-zeroshot/alimeeting_Test_Ali_far_ch1__nouem

- name: `20261026-nemotron-zeroshot/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `14dba5ba9283b3c5a43d24e874fc385f7285cb11-dirty`
- created: `2026-10-26T15:05:19+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.48 | 5.62 | 4.16 | 0.70 | 11.06 | 100.00 | 0.00 |
| 0.25 | 1.68 | 1.02 | 0.59 | 0.08 | 2.51 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.37 (IoU 95.37) | 1.99 (IoU 2.03) |
| silence | 1.97 (IoU 2.01) | 14.68 (IoU 78.79) |

Speech P/R/F1: 97.64 / 97.62 / 97.63; miss 2.38 of ref speech, FA 11.81 of ref silence, SAD error 4.74.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 12857 | 92.37 | 90.67 | 91.51 | 0.042 | 0.030 | -0.004 | 0.000 |
| 0.25 | offset | 13095 | 12860 | 92.63 | 90.97 | 91.79 | 0.044 | 0.030 | -0.002 | 0.000 |
| 0.25 | all | 26193 | 25717 | 92.50 | 90.82 | 91.65 | 0.043 | 0.030 | -0.003 | 0.000 |
| 0.50 | onset | 13098 | 12857 | 93.30 | 91.59 | 92.44 | 0.045 | 0.030 | -0.003 | 0.000 |
| 0.50 | offset | 13095 | 12860 | 93.48 | 91.80 | 92.63 | 0.046 | 0.030 | -0.002 | 0.000 |
| 0.50 | all | 26193 | 25717 | 93.39 | 91.69 | 92.53 | 0.046 | 0.030 | -0.003 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.61 | 9.91 | 1.21 | 1.47 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.28 | 11.79 | 1.74 | 2.78 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.16 | 10.37 | 1.34 | 1.73 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.93 | 22.34 | 5.37 | 7.99 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.87 | 19.89 | 2.81 | 3.04 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.37 | 7.39 | 1.59 | 1.69 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.97 | 18.99 | 8.02 | 7.94 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.04 | 10.57 | 1.90 | 2.11 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.83 | 7.54 | 0.79 | 0.92 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.20 | 10.48 | 2.05 | 2.31 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.47 | 9.79 | 1.32 | 2.27 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.41 | 6.30 | 0.46 | 0.60 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.23 | 6.92 | 0.61 | 0.60 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.30 | 6.96 | 1.16 | 1.41 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.41 | 12.79 | 0.90 | 1.09 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.42 | 4.34 | 0.72 | 0.72 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.84 | 6.62 | 0.66 | 0.58 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.58 | 8.37 | 1.08 | 1.23 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.05 | 5.86 | 1.75 | 1.68 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.38 | 6.22 | 1.49 | 1.46 | 2 | 2 |
