# Diarization scores: 20261026-nemotron-zeroshot/ear1_dev_D1

- name: `20261026-nemotron-zeroshot/ear1_dev_D1`
- manifest: `/mnt/data/manifests/nemo/ear1_dev_D1.jsonl`
- ref: `7 files under /mnt/data/refs/ear1/dev/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/ear1_dev_D1`
- uem: `7 files under /mnt/data/refs/ear1/dev/uem`
- seg_merge_gap: `0.0`
- git_commit: `d87d4bdc6476a710ee4195f2401f921cf5f6d5b5-dirty`
- created: `2026-10-27T14:06:48+00:00`
- condition: `ear1_dev_D1`
- ref_type: `segments`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 28.73 | 23.23 | 2.57 | 2.94 | 43.62 | 71.43 | 0.86 |
| 0.25 | 17.70 | 12.58 | 2.54 | 2.58 | 35.87 | 71.43 | 0.86 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 71.78 (IoU 82.87) | 13.33 (IoU 13.54) |
| silence | 1.50 (IoU 1.73) | 13.39 (IoU 47.43) |

Speech P/R/F1: 97.95 / 84.33 / 90.63; miss 15.67 of ref speech, FA 10.08 of ref silence, SAD error 17.43.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 2531 | 4335 | 50.03 | 85.70 | 63.18 | 0.114 | 0.110 | 0.098 | 0.110 |
| 0.25 | offset | 2531 | 4335 | 40.88 | 70.01 | 51.62 | 0.134 | 0.130 | -0.124 | -0.130 |
| 0.25 | all | 5062 | 8670 | 45.46 | 77.85 | 57.40 | 0.123 | 0.120 | -0.002 | 0.010 |
| 0.50 | onset | 2531 | 4335 | 54.16 | 92.77 | 68.39 | 0.131 | 0.120 | 0.114 | 0.110 |
| 0.50 | offset | 2531 | 4335 | 52.66 | 90.20 | 66.50 | 0.181 | 0.160 | -0.169 | -0.160 |
| 0.50 | all | 5062 | 8670 | 53.41 | 91.49 | 67.45 | 0.156 | 0.140 | -0.025 | -0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| 20260908-1__D1 | 30.18 | 37.77 | 18.65 | 27.54 | 4 | 4 |
| 20260908-2__D1 | 29.76 | 33.69 | 15.84 | 19.16 | 4 | 4 |
| 20260923-1__D1 | 21.41 | 23.68 | 8.50 | 11.24 | 4 | 4 |
| 20260923-2__D1 | 27.23 | 33.02 | 16.73 | 22.84 | 4 | 4 |
| 20260923-5__D1 | 15.48 | 23.61 | 7.11 | 16.50 | 4 | 4 |
| 20260924-2__D1 | 29.22 | 50.35 | 23.89 | 47.08 | 7 | 5 |
| 20260924-5__D1 | 41.27 | 70.88 | 31.38 | 67.09 | 8 | 4 |
