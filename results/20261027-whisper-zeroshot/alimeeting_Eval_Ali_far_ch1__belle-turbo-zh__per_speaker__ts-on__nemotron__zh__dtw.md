# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-on__nemotron__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-on__nemotron__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-on__nemotron__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T05:48:39+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-on__nemotron__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 42.71 | 21.48 | 12.18 | 9.06 |
| cpCER | 46.11 | 17.55 | 15.84 | 12.72 |
| tcpCER (collar 5.0 s) | 50.73 | 11.97 | 20.94 | 17.82 |
| per-speaker CER, pooled over 25 pairs | 46.11 | 17.55 | 15.84 | 12.72 |
| cpCER − ORC-CER (attribution) | 3.39 | | | |
| tcpCER − cpCER (timing) | 4.62 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 7253; traditional-character rate 0.00%; empty 5.14%, english_dominant 0.11%, repetition_loop 2.52%
- empty: `.`; `.`; `.`
- repetition_loop: `嗯嗯嗯，嗯，嗯，嗯，嗯，嗯，嗯，嗯，嗯，嗯，嗯，嗯，嗯，嗯，嗯，嗯，嗯`; `，嗯，嗯，嗯，嗯`; `，嗯，嗯，嗯，嗯，嗯，嗯，嗯，嗯，嗯，嗯，嗯，嗯，嗯，，嗯，嗯`
- english_dominant: `. I . I . I . I . I . I . I . I . I . I . I . I . I . I . I `; `I . I . I .`; `, C ar p`
