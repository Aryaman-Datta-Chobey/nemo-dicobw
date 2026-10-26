# Diarization scores: 20261026-nemotron-zeroshot/chime6_dev_U06_CH1__segments

- name: `20261026-nemotron-zeroshot/chime6_dev_U06_CH1__segments`
- manifest: `/mnt/data/manifests/nemo/chime6_dev_U06_CH1.jsonl`
- ref: `/mnt/data/refs/chime6/dev/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/chime6_dev_U06_CH1`
- uem: `/mnt/data/refs/chime6/dev/uem/S02.uem /mnt/data/refs/chime6/dev/uem/S09.uem`
- seg_merge_gap: `0.0`
- git_commit: `14dba5ba9283b3c5a43d24e874fc385f7285cb11-dirty`
- created: `2026-10-26T15:05:25+00:00`
- condition: `chime6_dev_U06_CH1__segments`
- ref_type: `segments`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 41.10 | 37.90 | 1.00 | 2.19 | 41.45 | 0.00 | 1.50 |
| 0.25 | 34.33 | 31.36 | 1.04 | 1.94 | 34.11 | 0.00 | 1.50 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 75.13 (IoU 85.06) | 12.44 (IoU 12.54) |
| silence | 0.75 (IoU 0.86) | 11.68 (IoU 46.95) |

Speech P/R/F1: 99.01 / 85.79 / 91.93; miss 14.21 of ref speech, FA 6.05 of ref silence, SAD error 15.07.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 801 | 4885 | 12.08 | 73.66 | 20.75 | 0.097 | 0.090 | 0.080 | 0.080 |
| 0.25 | offset | 802 | 4886 | 8.86 | 53.99 | 15.23 | 0.120 | 0.110 | -0.094 | -0.110 |
| 0.25 | all | 1603 | 9771 | 10.47 | 63.82 | 17.99 | 0.106 | 0.100 | 0.006 | 0.010 |
| 0.50 | onset | 801 | 4885 | 13.51 | 82.40 | 23.21 | 0.123 | 0.100 | 0.102 | 0.100 |
| 0.50 | offset | 802 | 4886 | 12.71 | 77.43 | 21.84 | 0.190 | 0.160 | -0.158 | -0.150 |
| 0.50 | all | 1603 | 9771 | 13.11 | 79.91 | 22.53 | 0.155 | 0.130 | -0.024 | -0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| S02__U06.CH1 | 42.26 | 42.64 | 36.70 | 37.16 | 4 | 6 |
| S09__U06.CH1 | 39.14 | 40.26 | 29.58 | 31.07 | 4 | 5 |
