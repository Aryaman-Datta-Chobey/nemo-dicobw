# Diarization scores: 20261026-nemotron-zeroshot/ear1_dev_R1

- name: `20261026-nemotron-zeroshot/ear1_dev_R1`
- manifest: `/mnt/data/manifests/nemo/ear1_dev_R1.jsonl`
- ref: `7 files under /mnt/data/refs/ear1/dev/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/ear1_dev_R1`
- uem: `7 files under /mnt/data/refs/ear1/dev/uem`
- seg_merge_gap: `0.0`
- git_commit: `d87d4bdc6476a710ee4195f2401f921cf5f6d5b5-dirty`
- created: `2026-10-27T14:05:21+00:00`
- condition: `ear1_dev_R1`
- ref_type: `segments`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 37.71 | 26.66 | 5.64 | 5.40 | 47.17 | 57.14 | 1.00 |
| 0.25 | 27.27 | 18.80 | 3.75 | 4.72 | 40.00 | 57.14 | 1.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 68.96 (IoU 77.07) | 16.08 (IoU 16.82) |
| silence | 4.44 (IoU 5.30) | 10.52 (IoU 33.89) |

Speech P/R/F1: 93.95 / 81.10 / 87.05; miss 18.90 of ref speech, FA 29.70 of ref silence, SAD error 24.13.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 2529 | 4311 | 35.40 | 60.34 | 44.62 | 0.123 | 0.120 | 0.034 | 0.070 |
| 0.25 | offset | 2527 | 4312 | 23.10 | 39.41 | 29.13 | 0.127 | 0.130 | -0.088 | -0.110 |
| 0.25 | all | 5056 | 8623 | 29.25 | 49.88 | 36.87 | 0.125 | 0.120 | -0.014 | -0.010 |
| 0.50 | onset | 2529 | 4311 | 48.09 | 81.97 | 60.61 | 0.189 | 0.160 | -0.011 | 0.050 |
| 0.50 | offset | 2527 | 4312 | 39.68 | 67.71 | 50.04 | 0.227 | 0.210 | -0.164 | -0.190 |
| 0.50 | all | 5056 | 8623 | 43.88 | 74.84 | 55.33 | 0.206 | 0.180 | -0.080 | -0.100 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| 20260908-1__R1 | 41.29 | 47.87 | 30.99 | 37.52 | 4 | 6 |
| 20260908-2__R1 | 32.31 | 36.70 | 19.64 | 23.89 | 4 | 4 |
| 20260923-1__R1 | 54.13 | 53.83 | 45.45 | 48.48 | 4 | 5 |
| 20260923-2__R1 | 44.92 | 43.30 | 33.22 | 34.83 | 4 | 4 |
| 20260923-5__R1 | 21.56 | 24.49 | 10.88 | 15.35 | 4 | 4 |
| 20260924-2__R1 | 28.02 | 35.32 | 22.75 | 29.59 | 7 | 7 |
| 20260924-5__R1 | 43.54 | 72.37 | 34.35 | 69.07 | 8 | 4 |
