# Diarization scores: 20261026-nemotron-zs-chunk2x/ear1_dev_D1

- name: `20261026-nemotron-zs-chunk2x/ear1_dev_D1`
- manifest: `/mnt/data/manifests/nemo/ear1_dev_D1.jsonl`
- ref: `7 files under /mnt/data/refs/ear1/dev/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zs-chunk2x/rttm/ear1_dev_D1`
- uem: `7 files under /mnt/data/refs/ear1/dev/uem`
- seg_merge_gap: `0.0`
- git_commit: `d87d4bdc6476a710ee4195f2401f921cf5f6d5b5-dirty`
- created: `2026-10-27T14:34:07+00:00`
- condition: `ear1_dev_D1`
- ref_type: `segments`
- run: `20261026-nemotron-zs-chunk2x`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":680,"chunk_right_context":40,"spkcache_update_period":680}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 30.38 | 22.98 | 3.13 | 4.27 | 47.60 | 57.14 | 1.14 |
| 0.25 | 19.84 | 12.25 | 3.30 | 4.29 | 40.21 | 57.14 | 1.14 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 72.10 (IoU 82.88) | 13.02 (IoU 13.26) |
| silence | 1.88 (IoU 2.16) | 13.01 (IoU 46.63) |

Speech P/R/F1: 97.46 / 84.71 / 90.64; miss 15.29 of ref speech, FA 12.61 of ref silence, SAD error 17.50.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 2531 | 4310 | 50.09 | 85.30 | 63.12 | 0.113 | 0.110 | 0.096 | 0.110 |
| 0.25 | offset | 2531 | 4310 | 40.74 | 69.38 | 51.34 | 0.134 | 0.130 | -0.126 | -0.130 |
| 0.25 | all | 5062 | 8620 | 45.42 | 77.34 | 57.23 | 0.122 | 0.120 | -0.003 | 0.000 |
| 0.50 | onset | 2531 | 4310 | 54.66 | 93.09 | 68.88 | 0.131 | 0.120 | 0.112 | 0.110 |
| 0.50 | offset | 2531 | 4310 | 52.90 | 90.08 | 66.66 | 0.183 | 0.160 | -0.171 | -0.160 |
| 0.50 | all | 5062 | 8620 | 53.78 | 91.58 | 67.77 | 0.157 | 0.140 | -0.027 | -0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| 20260908-1__D1 | 29.90 | 37.96 | 18.29 | 27.77 | 4 | 4 |
| 20260908-2__D1 | 29.63 | 33.40 | 15.53 | 17.99 | 4 | 4 |
| 20260923-1__D1 | 21.45 | 23.80 | 8.62 | 11.51 | 4 | 4 |
| 20260923-2__D1 | 29.64 | 39.77 | 19.03 | 30.05 | 4 | 4 |
| 20260923-5__D1 | 19.29 | 26.78 | 11.12 | 20.60 | 4 | 5 |
| 20260924-2__D1 | 37.39 | 64.87 | 32.45 | 62.85 | 7 | 4 |
| 20260924-5__D1 | 41.09 | 70.63 | 31.40 | 66.99 | 8 | 4 |
