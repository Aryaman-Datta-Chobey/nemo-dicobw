# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__per_speaker__ts-off__oracle__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__per_speaker__ts-off__oracle__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__per_speaker__ts-off__oracle__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T06:05:42+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh__per_speaker__ts-off__oracle__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 33.50 | 16.86 | 11.81 | 4.82 |
| cpCER | 35.27 | 14.99 | 13.63 | 6.65 |
| tcpCER (collar 5.0 s) | 40.43 | 12.61 | 17.40 | 10.42 |
| per-speaker CER, pooled over 25 pairs | 35.27 | 14.99 | 13.63 | 6.65 |
| cpCER − ORC-CER (attribution) | 1.78 | | | |
| tcpCER − cpCER (timing) | 5.16 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 7839; traditional-character rate 0.00%; empty 0.03%, repetition_loop 1.02%
- repetition_loop: `嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯`; `嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯`; `嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯`
- empty: `, , , , , , , , , , , , , , ,`; `, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , `
