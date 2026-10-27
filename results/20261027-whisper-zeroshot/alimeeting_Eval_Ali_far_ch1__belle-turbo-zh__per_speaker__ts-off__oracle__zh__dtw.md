# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-off__oracle__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-off__oracle__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-off__oracle__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T05:47:49+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-off__oracle__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 34.48 | 15.25 | 14.05 | 5.17 |
| cpCER | 35.75 | 14.73 | 14.95 | 6.07 |
| tcpCER (collar 5.0 s) | 38.56 | 13.10 | 17.17 | 8.29 |
| per-speaker CER, pooled over 25 pairs | 35.75 | 14.73 | 14.95 | 6.07 |
| cpCER − ORC-CER (attribution) | 1.27 | | | |
| tcpCER − cpCER (timing) | 2.81 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 7744; traditional-character rate 0.00%; empty 3.37%, repetition_loop 1.38%
- empty: `？`; `。`; `，`
- repetition_loop: `嗯嗯嗯嗯嗯，`; `嗯嗯嗯，嗯嗯嗯，嗯嗯嗯，嗯嗯嗯，嗯嗯嗯，嗯`; `在不在不在不在不在不在不在不在不在不在不在不在。`
