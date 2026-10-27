# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-on__oracle__zh__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-on__oracle__zh__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-on__oracle__zh/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T05:50:30+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-on__oracle__zh`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 37.75 | 9.79 | 27.18 | 0.77 |
| cpCER | 39.05 | 10.34 | 27.56 | 1.15 |
| tcpCER (collar 5.0 s) | 51.92 | 14.62 | 31.85 | 5.44 |
| per-speaker CER, pooled over 25 pairs | 39.05 | 10.34 | 27.56 | 1.15 |
| cpCER − ORC-CER (attribution) | 1.30 | | | |
| tcpCER − cpCER (timing) | 12.87 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 1741; traditional-character rate 0.00%; empty 16.37%, repetition_loop 5.05%
- empty: `.`; `.`; `.`
- repetition_loop: `嗯嗯嗯嗯嗯嗯嗯嗯，嗯嗯嗯，嗯嗯。`; `就是开脱，不在不在不在不在不在不在不在不在不在不在不在不在。`; `就是买一个手机周边产品对吧？对，对，对，对。`
