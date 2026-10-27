# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__belle-zh__per_speaker__ts-off__oracle__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__belle-zh__per_speaker__ts-off__oracle__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__belle-zh__per_speaker__ts-off__oracle__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T11:49:27+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_near__belle-zh__per_speaker__ts-off__oracle__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 10.85 | 3.23 | 5.90 | 1.71 |
| cpCER | 10.91 | 3.24 | 5.93 | 1.74 |
| tcpCER (collar 5.0 s) | 14.45 | 3.64 | 7.50 | 3.31 |
| per-speaker CER, pooled over 25 pairs | 10.91 | 3.24 | 5.93 | 1.74 |
| cpCER − ORC-CER (attribution) | 0.06 | | | |
| tcpCER − cpCER (timing) | 3.54 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 8627; traditional-character rate 0.00%; repetition_loop 0.34%
- repetition_loop: `说咱们做做做做几个方案刚`; `对对对对`; `对对对对`
