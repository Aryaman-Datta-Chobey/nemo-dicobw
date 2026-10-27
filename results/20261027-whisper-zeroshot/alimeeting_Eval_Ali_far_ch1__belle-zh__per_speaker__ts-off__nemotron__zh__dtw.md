# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__per_speaker__ts-off__nemotron__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__per_speaker__ts-off__nemotron__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__per_speaker__ts-off__nemotron__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T06:04:59+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh__per_speaker__ts-off__nemotron__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 30.33 | 12.52 | 15.44 | 2.37 |
| cpCER | 31.49 | 11.96 | 16.30 | 3.23 |
| tcpCER (collar 5.0 s) | 35.14 | 11.31 | 18.45 | 5.38 |
| per-speaker CER, pooled over 25 pairs | 31.49 | 11.96 | 16.30 | 3.23 |
| cpCER − ORC-CER (attribution) | 1.16 | | | |
| tcpCER − cpCER (timing) | 3.65 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 7477; traditional-character rate 0.00%; repetition_loop 0.58%
- repetition_loop: `找找找找`; `找找找找找找找找`; `找找找找`
