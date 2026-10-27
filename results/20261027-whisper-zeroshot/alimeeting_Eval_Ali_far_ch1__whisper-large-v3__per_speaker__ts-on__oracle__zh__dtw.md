# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__per_speaker__ts-on__oracle__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__per_speaker__ts-on__oracle__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__per_speaker__ts-on__oracle__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T06:15:21+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3__per_speaker__ts-on__oracle__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 33.55 | 16.08 | 15.30 | 2.17 |
| cpCER | 34.95 | 15.20 | 16.45 | 3.31 |
| tcpCER (collar 5.0 s) | 39.16 | 14.00 | 19.15 | 6.01 |
| per-speaker CER, pooled over 25 pairs | 34.95 | 15.20 | 16.45 | 3.31 |
| cpCER − ORC-CER (attribution) | 1.40 | | | |
| tcpCER − cpCER (timing) | 4.21 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 7861; traditional-character rate 3.07%; empty 0.04%, repetition_loop 1.13%, traditional 2.52%
- repetition_loop: `好好好好好`; `好好好好好好好好好好好好好`; `好好好好`
- traditional: `響`; `鐘`; `去個`
- empty: `,`; `。`; `,`
