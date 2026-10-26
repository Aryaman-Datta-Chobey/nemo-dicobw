# Diarization scores: 20261026-nemotron-zeroshot/chime6_dev_U06_CH1

- name: `20261026-nemotron-zeroshot/chime6_dev_U06_CH1`
- manifest: `/mnt/data/manifests/nemo/chime6_dev_U06_CH1.jsonl`
- ref: `/mnt/data/refs/chime6/dev/rttm/fa/S02.rttm /mnt/data/refs/chime6/dev/rttm/fa/S09.rttm`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/chime6_dev_U06_CH1`
- uem: `/mnt/data/refs/chime6/dev/uem/S02.uem /mnt/data/refs/chime6/dev/uem/S09.uem`
- seg_merge_gap: `0.0`
- git_commit: `14dba5ba9283b3c5a43d24e874fc385f7285cb11-dirty`
- created: `2026-10-26T15:05:22+00:00`
- condition: `chime6_dev_U06_CH1`
- ref_type: `fa`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 31.24 | 18.61 | 8.55 | 4.08 | 31.58 | 0.00 | 1.50 |
| 0.25 | 18.34 | 10.74 | 5.06 | 2.54 | 19.78 | 0.00 | 1.50 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 71.53 (IoU 88.39) | 5.04 (IoU 5.27) |
| silence | 4.35 (IoU 4.58) | 19.08 (IoU 67.02) |

Speech P/R/F1: 94.26 / 93.42 / 93.84; miss 6.58 of ref speech, FA 18.57 of ref silence, SAD error 12.27.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4373 | 4885 | 62.56 | 69.88 | 66.02 | 0.042 | 0.020 | 0.003 | 0.000 |
| 0.25 | offset | 4374 | 4886 | 60.36 | 67.42 | 63.69 | 0.071 | 0.060 | 0.010 | 0.010 |
| 0.25 | all | 8747 | 9771 | 61.46 | 68.65 | 64.86 | 0.056 | 0.040 | 0.007 | 0.000 |
| 0.50 | onset | 4373 | 4885 | 66.33 | 74.09 | 69.99 | 0.059 | 0.030 | 0.005 | 0.000 |
| 0.50 | offset | 4374 | 4886 | 65.62 | 73.30 | 69.24 | 0.094 | 0.060 | 0.003 | 0.010 |
| 0.50 | all | 8747 | 9771 | 65.97 | 73.69 | 69.62 | 0.077 | 0.040 | 0.004 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| S02__U06.CH1 | 30.97 | 30.75 | 18.42 | 19.45 | 4 | 6 |
| S09__U06.CH1 | 31.65 | 32.42 | 18.21 | 20.12 | 4 | 5 |
