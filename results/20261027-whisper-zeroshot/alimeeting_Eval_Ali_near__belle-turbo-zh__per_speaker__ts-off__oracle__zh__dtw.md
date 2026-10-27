# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__belle-turbo-zh__per_speaker__ts-off__oracle__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__belle-turbo-zh__per_speaker__ts-off__oracle__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__belle-turbo-zh__per_speaker__ts-off__oracle__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T11:49:16+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_near__belle-turbo-zh__per_speaker__ts-off__oracle__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 13.65 | 3.78 | 6.67 | 3.19 |
| cpCER | 13.83 | 3.65 | 6.83 | 3.35 |
| tcpCER (collar 5.0 s) | 15.84 | 3.80 | 7.76 | 4.28 |
| per-speaker CER, pooled over 25 pairs | 13.83 | 3.65 | 6.83 | 3.35 |
| cpCER − ORC-CER (attribution) | 0.18 | | | |
| tcpCER − cpCER (timing) | 2.01 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 8649; traditional-character rate 0.00%; empty 4.84%, repetition_loop 0.94%
- empty: `，`; `。`; `，`
- repetition_loop: `嗯嗯嗯嗯`; `对对对对对，我也觉得是把手手办什么的，我觉得挺不够都`; `嗯嗯嗯嗯嗯`
