# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__per_speaker__ts-on__nemotron__zh__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__per_speaker__ts-on__nemotron__zh__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__per_speaker__ts-on__nemotron__zh/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T06:14:39+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3__per_speaker__ts-on__nemotron__zh`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 32.75 | 15.16 | 16.24 | 1.35 |
| cpCER | 34.14 | 14.22 | 17.41 | 2.51 |
| tcpCER (collar 5.0 s) | 37.11 | 13.00 | 19.50 | 4.60 |
| per-speaker CER, pooled over 25 pairs | 34.14 | 14.22 | 17.41 | 2.51 |
| cpCER − ORC-CER (attribution) | 1.38 | | | |
| tcpCER − cpCER (timing) | 2.97 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 9802; traditional-character rate 2.67%; repetition_loop 0.02%, traditional 2.13%
- traditional: `對`; `響鐘`; `這個也不用換`
- repetition_loop: `对,对对对`; `有一些想画画画画画的人`
