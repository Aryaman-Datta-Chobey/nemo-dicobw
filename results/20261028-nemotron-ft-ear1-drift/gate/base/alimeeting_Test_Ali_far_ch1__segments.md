# Diarization scores: base/alimeeting_Test_Ali_far_ch1__segments

- name: `base/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/base/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:38:48+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `base`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/ckpts/base.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.23 | 16.70 | 0.99 | 0.55 | 18.89 | 100.00 | 0.00 |
| 0.25 | 10.27 | 9.80 | 0.30 | 0.17 | 12.05 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.74 (IoU 89.74) | 9.22 (IoU 9.24) |
| silence | 0.25 (IoU 0.27) | 7.79 (IoU 45.16) |

Speech P/R/F1: 99.70 / 89.97 / 94.59; miss 10.03 of ref speech, FA 3.05 of ref silence, SAD error 10.29.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12872 | 35.23 | 93.03 | 51.11 | 0.082 | 0.080 | 0.062 | 0.070 |
| 0.25 | offset | 4875 | 12872 | 34.77 | 91.82 | 50.44 | 0.094 | 0.090 | -0.085 | -0.090 |
| 0.25 | all | 9750 | 25744 | 35.00 | 92.42 | 50.77 | 0.088 | 0.080 | -0.011 | -0.010 |
| 0.50 | onset | 4875 | 12872 | 36.15 | 95.45 | 52.44 | 0.089 | 0.080 | 0.067 | 0.070 |
| 0.50 | offset | 4875 | 12872 | 36.59 | 96.62 | 53.08 | 0.105 | 0.100 | -0.093 | -0.090 |
| 0.50 | all | 9750 | 25744 | 36.37 | 96.03 | 52.76 | 0.097 | 0.090 | -0.013 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.24 | 16.49 | 11.47 | 11.93 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.89 | 21.10 | 15.60 | 17.75 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.15 | 16.81 | 10.12 | 11.41 | 4 | 4 |
| R8004_M8006__far_ch1 | 23.06 | 25.64 | 18.11 | 20.33 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.09 | 24.66 | 16.42 | 16.60 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.33 | 12.94 | 10.07 | 9.15 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.19 | 27.93 | 25.27 | 24.60 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.53 | 16.95 | 10.96 | 11.09 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.10 | 16.76 | 12.10 | 12.57 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.00 | 22.86 | 18.27 | 18.63 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.17 | 22.40 | 13.69 | 17.08 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.64 | 16.90 | 12.30 | 12.90 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.96 | 15.89 | 3.79 | 3.65 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.16 | 15.30 | 2.43 | 2.80 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.93 | 18.00 | 3.08 | 4.30 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.60 | 13.55 | 1.44 | 1.45 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.30 | 13.98 | 2.28 | 2.13 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.40 | 17.51 | 3.26 | 3.33 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.97 | 15.87 | 4.13 | 4.00 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.46 | 13.19 | 2.36 | 2.32 | 2 | 2 |
