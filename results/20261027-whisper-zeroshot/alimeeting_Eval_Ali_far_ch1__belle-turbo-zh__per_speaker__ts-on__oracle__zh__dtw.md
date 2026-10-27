# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-on__oracle__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-on__oracle__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-on__oracle__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T05:49:57+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-on__oracle__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 44.32 | 20.25 | 13.29 | 10.77 |
| cpCER | 47.78 | 16.48 | 16.91 | 14.40 |
| tcpCER (collar 5.0 s) | 51.54 | 12.64 | 20.71 | 18.19 |
| per-speaker CER, pooled over 25 pairs | 47.78 | 16.48 | 16.91 | 14.40 |
| cpCER − ORC-CER (attribution) | 3.47 | | | |
| tcpCER − cpCER (timing) | 3.76 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 7478; traditional-character rate 0.00%; empty 5.22%, english_dominant 0.03%, repetition_loop 2.47%
- empty: `.`; `。。。。。。。。。。。。。。。。。。。。。。。。`; `。`
- repetition_loop: `，对，对。对。对。对。对。对。对。对。对。对。。对。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。`; `嗯嗯嗯嗯嗯嗯嗯，`; `嗯嗯嗯嗯嗯，`
- english_dominant: `. I think . I`; `. I . I . I . I . I . I . I . I . I . I . I . I . I . I . I `
