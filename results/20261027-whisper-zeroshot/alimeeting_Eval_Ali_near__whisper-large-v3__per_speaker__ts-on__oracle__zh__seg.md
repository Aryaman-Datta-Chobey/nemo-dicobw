# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__whisper-large-v3__per_speaker__ts-on__oracle__zh__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__whisper-large-v3__per_speaker__ts-on__oracle__zh__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__whisper-large-v3__per_speaker__ts-on__oracle__zh/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T11:49:28+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_near__whisper-large-v3__per_speaker__ts-on__oracle__zh`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 12.62 | 3.66 | 8.12 | 0.84 |
| cpCER | 12.75 | 3.51 | 8.26 | 0.98 |
| tcpCER (collar 5.0 s) | 14.43 | 3.95 | 8.88 | 1.60 |
| per-speaker CER, pooled over 25 pairs | 12.75 | 3.51 | 8.26 | 0.98 |
| cpCER − ORC-CER (attribution) | 0.13 | | | |
| tcpCER − cpCER (timing) | 1.69 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 10367; traditional-character rate 0.57%; repetition_loop 0.14%, traditional 0.70%
- repetition_loop: `对对对对就是同时货手机`; `對,有有有有`; `30 30 30 31`
- traditional: `不會不會`; `對的`; `對的`
