# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__whisper-large-v3__per_speaker__ts-on__oracle__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__whisper-large-v3__per_speaker__ts-on__oracle__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__whisper-large-v3__per_speaker__ts-on__oracle__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T11:49:27+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_near__whisper-large-v3__per_speaker__ts-on__oracle__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 13.56 | 3.97 | 7.82 | 1.77 |
| cpCER | 13.76 | 3.72 | 8.04 | 2.00 |
| tcpCER (collar 5.0 s) | 17.18 | 4.12 | 9.55 | 3.51 |
| per-speaker CER, pooled over 25 pairs | 13.76 | 3.72 | 8.04 | 2.00 |
| cpCER − ORC-CER (attribution) | 0.20 | | | |
| tcpCER − cpCER (timing) | 3.42 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 8450; traditional-character rate 0.57%; empty 0.07%, english_dominant 0.01%, repetition_loop 0.38%, traditional 0.96%
- english_dominant: `t rad`
- repetition_loop: `嗯嗯嗯嗯嗯嗯`; `嗯嗯嗯嗯嗯嗯嗯嗯嗯`; `對,有有有有`
- traditional: `不會`; `不會`; `對的對`
- empty: `。`; `。`; `。`
