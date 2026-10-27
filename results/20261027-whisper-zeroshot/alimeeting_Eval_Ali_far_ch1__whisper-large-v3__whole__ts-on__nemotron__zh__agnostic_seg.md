# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__whole__ts-on__nemotron__zh__agnostic_seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__whole__ts-on__nemotron__zh__agnostic_seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__whole__ts-on__nemotron__zh/hyp_agnostic_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `exact`
- created: `2026-10-27T06:18:23+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3__whole__ts-on__nemotron__zh`
- variant: `agnostic_seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 34.18 | 6.34 | 26.93 | 0.90 |
| cpCER | 103.53 | 7.47 | 61.04 | 35.01 |
| tcpCER (collar 5.0 s) | 103.93 | 7.40 | 61.28 | 35.25 |
| per-speaker CER, pooled over 8 pairs | 108.50 | 17.99 | 6.18 | 84.32 |
| cpCER − ORC-CER (attribution) | 69.35 | | | |
| tcpCER − cpCER (timing) | 0.40 | | | |

Missed reference speakers 17, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 6602; traditional-character rate 3.83%; english_dominant 0.02%, repetition_loop 0.03%, traditional 2.44%
- traditional: `我覺得這個來說呢`; `也給送給老師`; `就一兩百塊錢`
- english_dominant: `可以在Lunar TNTP上`
- repetition_loop: `有一些想画画画画画的人`; `就像3 4 12 12 12 12个人的字吗`
