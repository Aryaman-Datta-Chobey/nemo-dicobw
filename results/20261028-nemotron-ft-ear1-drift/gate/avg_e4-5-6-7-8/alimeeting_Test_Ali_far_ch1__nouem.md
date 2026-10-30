# Diarization scores: avg_e4-5-6-7-8/alimeeting_Test_Ali_far_ch1__nouem

- name: `avg_e4-5-6-7-8/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/avg_e4-5-6-7-8/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:43:15+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `avg_e4-5-6-7-8`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/avg_e4-5-6-7-8.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.67 | 5.24 | 5.69 | 0.74 | 12.26 | 95.00 | 0.05 |
| 0.25 | 1.75 | 0.97 | 0.72 | 0.07 | 2.60 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.54 (IoU 94.47) | 1.77 (IoU 1.83) |
| silence | 3.00 (IoU 3.05) | 13.68 (IoU 74.15) |

Speech P/R/F1: 96.45 / 97.87 / 97.16; miss 2.13 of ref speech, FA 17.97 of ref silence, SAD error 5.73.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13099 | 12328 | 92.82 | 87.36 | 90.01 | 0.050 | 0.040 | -0.011 | -0.010 |
| 0.25 | offset | 13097 | 12330 | 92.59 | 87.16 | 89.79 | 0.058 | 0.050 | 0.020 | 0.020 |
| 0.25 | all | 26196 | 24658 | 92.70 | 87.26 | 89.90 | 0.054 | 0.040 | 0.004 | 0.010 |
| 0.50 | onset | 13099 | 12328 | 93.75 | 88.23 | 90.90 | 0.053 | 0.040 | -0.011 | -0.010 |
| 0.50 | offset | 13097 | 12330 | 93.84 | 88.35 | 91.01 | 0.062 | 0.050 | 0.022 | 0.020 |
| 0.50 | all | 26196 | 24658 | 93.80 | 88.29 | 90.96 | 0.057 | 0.040 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.47 | 10.77 | 1.52 | 1.85 | 4 | 4 |
| R8002_M8003__far_ch1 | 13.63 | 14.42 | 1.67 | 2.70 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.60 | 10.83 | 1.47 | 1.96 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.06 | 22.37 | 5.16 | 7.65 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.94 | 19.86 | 2.73 | 2.94 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.70 | 7.69 | 1.70 | 1.80 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.66 | 19.70 | 8.90 | 8.46 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.84 | 11.29 | 2.33 | 2.52 | 4 | 4 |
| R8008_M8014__far_ch1 | 8.10 | 8.74 | 0.59 | 0.73 | 3 | 3 |
| R8008_M8015__far_ch1 | 15.42 | 15.95 | 1.62 | 1.96 | 3 | 4 |
| R8008_M8016__far_ch1 | 9.97 | 12.19 | 1.49 | 2.50 | 3 | 3 |
| R8008_M8017__far_ch1 | 11.10 | 11.02 | 0.69 | 0.78 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.94 | 8.52 | 0.83 | 0.82 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.26 | 6.93 | 1.26 | 1.53 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.20 | 12.62 | 1.14 | 1.43 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.30 | 5.21 | 1.38 | 1.38 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.96 | 7.47 | 0.73 | 0.65 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.33 | 8.13 | 0.87 | 1.00 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.68 | 6.39 | 1.66 | 1.63 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.92 | 6.67 | 0.88 | 0.88 | 2 | 2 |
