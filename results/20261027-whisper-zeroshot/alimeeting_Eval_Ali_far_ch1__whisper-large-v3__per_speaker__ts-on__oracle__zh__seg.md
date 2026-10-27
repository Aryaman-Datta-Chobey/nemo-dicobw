# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__per_speaker__ts-on__oracle__zh__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__per_speaker__ts-on__oracle__zh__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__per_speaker__ts-on__oracle__zh/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T06:16:03+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3__per_speaker__ts-on__oracle__zh`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 32.68 | 15.01 | 16.16 | 1.51 |
| cpCER | 33.90 | 14.54 | 17.00 | 2.36 |
| tcpCER (collar 5.0 s) | 37.01 | 14.11 | 18.78 | 4.13 |
| per-speaker CER, pooled over 25 pairs | 33.90 | 14.54 | 17.00 | 2.36 |
| cpCER − ORC-CER (attribution) | 1.22 | | | |
| tcpCER − cpCER (timing) | 3.11 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 10027; traditional-character rate 3.11%; repetition_loop 0.02%, traditional 2.16%
- traditional: `去個`; `我認為作為老師來講`; `他不應該輕視`
- repetition_loop: `对,对对对`; `有一些想画画画画画的人也可以去画画`
