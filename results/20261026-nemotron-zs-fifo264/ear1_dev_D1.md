# Diarization scores: 20261026-nemotron-zs-fifo264/ear1_dev_D1

- name: `20261026-nemotron-zs-fifo264/ear1_dev_D1`
- manifest: `/mnt/data/manifests/nemo/ear1_dev_D1.jsonl`
- ref: `7 files under /mnt/data/refs/ear1/dev/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zs-fifo264/rttm/ear1_dev_D1`
- uem: `7 files under /mnt/data/refs/ear1/dev/uem`
- seg_merge_gap: `0.0`
- git_commit: `d87d4bdc6476a710ee4195f2401f921cf5f6d5b5-dirty`
- created: `2026-10-27T14:41:22+00:00`
- condition: `ear1_dev_D1`
- ref_type: `segments`
- run: `20261026-nemotron-zs-fifo264`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":264,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 29.42 | 23.16 | 2.98 | 3.28 | 45.72 | 71.43 | 1.00 |
| 0.25 | 18.80 | 12.48 | 3.18 | 3.14 | 38.20 | 71.43 | 1.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 71.87 (IoU 82.69) | 13.24 (IoU 13.49) |
| silence | 1.80 (IoU 2.08) | 13.08 (IoU 46.51) |

Speech P/R/F1: 97.55 / 84.44 / 90.52; miss 15.56 of ref speech, FA 12.12 of ref silence, SAD error 17.68.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 2531 | 4325 | 50.10 | 85.62 | 63.21 | 0.113 | 0.110 | 0.096 | 0.110 |
| 0.25 | offset | 2531 | 4325 | 40.79 | 69.70 | 51.46 | 0.133 | 0.130 | -0.124 | -0.130 |
| 0.25 | all | 5062 | 8650 | 45.45 | 77.66 | 57.34 | 0.122 | 0.120 | -0.003 | 0.010 |
| 0.50 | onset | 2531 | 4325 | 54.59 | 93.28 | 68.87 | 0.131 | 0.120 | 0.113 | 0.110 |
| 0.50 | offset | 2531 | 4325 | 52.95 | 90.48 | 66.80 | 0.182 | 0.160 | -0.170 | -0.160 |
| 0.50 | all | 5062 | 8650 | 53.77 | 91.88 | 67.84 | 0.156 | 0.140 | -0.026 | -0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| 20260908-1__D1 | 28.54 | 34.87 | 16.82 | 23.89 | 4 | 4 |
| 20260908-2__D1 | 30.03 | 33.85 | 16.09 | 19.23 | 4 | 4 |
| 20260923-1__D1 | 21.20 | 23.21 | 8.28 | 10.70 | 4 | 4 |
| 20260923-2__D1 | 26.76 | 31.95 | 16.37 | 22.34 | 4 | 4 |
| 20260923-5__D1 | 15.71 | 24.43 | 7.46 | 17.60 | 4 | 4 |
| 20260924-2__D1 | 36.88 | 62.83 | 32.07 | 60.64 | 7 | 4 |
| 20260924-5__D1 | 41.39 | 70.89 | 31.66 | 67.19 | 8 | 4 |
