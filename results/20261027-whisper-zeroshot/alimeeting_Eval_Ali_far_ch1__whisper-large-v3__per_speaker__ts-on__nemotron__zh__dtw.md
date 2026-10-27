# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__per_speaker__ts-on__nemotron__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__per_speaker__ts-on__nemotron__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__per_speaker__ts-on__nemotron__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T06:13:58+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3__per_speaker__ts-on__nemotron__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 33.69 | 15.79 | 15.62 | 2.29 |
| cpCER | 35.24 | 14.46 | 17.06 | 3.73 |
| tcpCER (collar 5.0 s) | 39.34 | 13.19 | 19.74 | 6.41 |
| per-speaker CER, pooled over 25 pairs | 35.24 | 14.46 | 17.06 | 3.73 |
| cpCER − ORC-CER (attribution) | 1.55 | | | |
| tcpCER − cpCER (timing) | 4.10 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 7560; traditional-character rate 2.63%; empty 0.09%, english_dominant 0.01%, repetition_loop 1.07%, traditional 2.31%
- repetition_loop: `好好好好好`; `好好好好好好好好好好好好好`; `好好好好好`
- traditional: `以後`; `響`; `鐘`
- empty: `,`; `。`; `,`
- english_dominant: `D TA空`
