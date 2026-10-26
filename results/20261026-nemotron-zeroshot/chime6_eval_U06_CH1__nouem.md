# Diarization scores: 20261026-nemotron-zeroshot/chime6_eval_U06_CH1__nouem

- name: `20261026-nemotron-zeroshot/chime6_eval_U06_CH1__nouem`
- manifest: `/mnt/data/manifests/nemo/chime6_eval_U06_CH1.jsonl`
- ref: `/mnt/data/refs/chime6/eval/rttm/fa/S01.rttm /mnt/data/refs/chime6/eval/rttm/fa/S21.rttm`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/chime6_eval_U06_CH1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `14dba5ba9283b3c5a43d24e874fc385f7285cb11-dirty`
- created: `2026-10-26T15:05:28+00:00`
- condition: `chime6_eval_U06_CH1__nouem`
- ref_type: `fa`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 38.87 | 22.75 | 7.89 | 8.22 | 41.33 | 0.00 | 1.50 |
| 0.25 | 27.37 | 15.34 | 4.54 | 7.48 | 31.96 | 0.00 | 1.50 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 58.37 (IoU 83.00) | 8.15 (IoU 8.47) |
| silence | 3.80 (IoU 4.14) | 29.68 (IoU 71.30) |

Speech P/R/F1: 93.89 / 87.75 / 90.71; miss 12.25 of ref speech, FA 11.35 of ref silence, SAD error 17.97.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 6424 | 7369 | 65.22 | 74.81 | 69.69 | 0.050 | 0.030 | 0.006 | 0.010 |
| 0.25 | offset | 6424 | 7369 | 62.06 | 71.19 | 66.31 | 0.069 | 0.050 | -0.016 | -0.020 |
| 0.25 | all | 12848 | 14738 | 63.64 | 73.00 | 68.00 | 0.059 | 0.040 | -0.005 | 0.000 |
| 0.50 | onset | 6424 | 7369 | 68.83 | 78.95 | 73.54 | 0.067 | 0.040 | 0.010 | 0.010 |
| 0.50 | offset | 6424 | 7369 | 67.72 | 77.68 | 72.36 | 0.093 | 0.060 | -0.021 | -0.020 |
| 0.50 | all | 12848 | 14738 | 68.27 | 78.32 | 72.95 | 0.080 | 0.050 | -0.006 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| S01__U06.CH1 | 42.22 | 42.56 | 31.23 | 33.11 | 4 | 5 |
| S21__U06.CH1 | 34.99 | 40.09 | 23.27 | 30.81 | 4 | 6 |
