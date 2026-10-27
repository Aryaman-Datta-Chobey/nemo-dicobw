# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__whisper-large-v3-turbo__per_speaker__ts-on__oracle__zh__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__whisper-large-v3-turbo__per_speaker__ts-on__oracle__zh__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__whisper-large-v3-turbo__per_speaker__ts-on__oracle__zh/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T11:49:28+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_near__whisper-large-v3-turbo__per_speaker__ts-on__oracle__zh`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 14.03 | 4.00 | 9.01 | 1.02 |
| cpCER | 14.26 | 3.76 | 9.25 | 1.26 |
| tcpCER (collar 5.0 s) | 15.27 | 4.03 | 9.61 | 1.63 |
| per-speaker CER, pooled over 25 pairs | 14.26 | 3.76 | 9.25 | 1.26 |
| cpCER − ORC-CER (attribution) | 0.23 | | | |
| tcpCER − cpCER (timing) | 1.01 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 9142; traditional-character rate 1.59%; english_dominant 0.01%, repetition_loop 0.25%, traditional 1.37%
- repetition_loop: `操作不了,是吧?也操作不了,对对对对`; `对对对对就是同时换手机`; `我觉得像像像我觉得上一二小级的那种的那就由由由由家长来带去送索伊克卡这种的就可以`
- traditional: `但是我覺得要專門設計的話`; `然後就會`; `不 我覺得這樣的話`
- english_dominant: `优优独播剧场——YoYo Television Series Exclusive`
