# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-on__nemotron__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-on__nemotron__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-on__nemotron__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T05:57:51+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-on__nemotron__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 28.83 | 13.25 | 14.07 | 1.51 |
| cpCER | 29.97 | 12.72 | 14.90 | 2.35 |
| tcpCER (collar 5.0 s) | 33.22 | 12.00 | 16.89 | 4.33 |
| per-speaker CER, pooled over 25 pairs | 29.97 | 12.72 | 14.90 | 2.35 |
| cpCER − ORC-CER (attribution) | 1.14 | | | |
| tcpCER − cpCER (timing) | 3.25 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 7654; traditional-character rate 0.00%; empty 2.64%, repetition_loop 0.47%
- empty: `。`; `，`; `，`
- repetition_loop: `找找找找`; `找找找找找找找找找找找找找找找找找找找找找找找找找找找找找找找找找找找找找找找找找找找找找找`; `找找找找找找找找找找找找找找找找找找找找`
