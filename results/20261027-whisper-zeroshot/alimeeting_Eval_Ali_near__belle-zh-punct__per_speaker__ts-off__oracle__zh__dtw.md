# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__belle-zh-punct__per_speaker__ts-off__oracle__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__belle-zh-punct__per_speaker__ts-off__oracle__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__belle-zh-punct__per_speaker__ts-off__oracle__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T11:49:15+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_near__belle-zh-punct__per_speaker__ts-off__oracle__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 10.28 | 3.29 | 6.08 | 0.91 |
| cpCER | 10.35 | 3.27 | 6.13 | 0.95 |
| tcpCER (collar 5.0 s) | 13.56 | 3.62 | 7.56 | 2.38 |
| per-speaker CER, pooled over 25 pairs | 10.35 | 3.27 | 6.13 | 0.95 |
| cpCER − ORC-CER (attribution) | 0.07 | | | |
| tcpCER − cpCER (timing) | 3.21 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 8803; traditional-character rate 0.00%; empty 3.98%, repetition_loop 0.28%
- empty: `。`; `？`; `。`
- repetition_loop: `所以说咱们做做做做几个方案，刚`; `对对对对`; `画个那个画画画画。`
