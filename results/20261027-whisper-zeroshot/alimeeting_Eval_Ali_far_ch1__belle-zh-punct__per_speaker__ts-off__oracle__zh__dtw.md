# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-off__oracle__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-off__oracle__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-off__oracle__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T05:57:11+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-off__oracle__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 28.42 | 13.81 | 12.95 | 1.65 |
| cpCER | 29.25 | 13.58 | 13.48 | 2.19 |
| tcpCER (collar 5.0 s) | 32.65 | 13.39 | 15.28 | 3.98 |
| per-speaker CER, pooled over 25 pairs | 29.25 | 13.58 | 13.48 | 2.19 |
| cpCER − ORC-CER (attribution) | 0.83 | | | |
| tcpCER − cpCER (timing) | 3.40 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 8113; traditional-character rate 0.00%; empty 2.71%, repetition_loop 0.49%
- empty: `，`; `，`; `，`
- repetition_loop: `啊啊啊啊啊啊`; `啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊`; `啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊。`
