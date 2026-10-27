# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-on__nemotron__zh__fusion_oracle

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-on__nemotron__zh__fusion_oracle`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-on__nemotron__zh/hyp_fusion_oracle.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:26:33+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-on__nemotron__zh`
- variant: `fusion_oracle`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 38.45 | 13.18 | 23.20 | 2.07 |
| cpCER | 40.89 | 13.17 | 24.42 | 3.29 |
| tcpCER (collar 5.0 s) | 43.16 | 9.63 | 27.33 | 6.20 |
| per-speaker CER, pooled over 25 pairs | 40.89 | 13.17 | 24.42 | 3.29 |
| cpCER − ORC-CER (attribution) | 2.44 | | | |
| tcpCER − cpCER (timing) | 2.27 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 3060; traditional-character rate 0.00%; empty 3.04%, repetition_loop 1.83%
- empty: `。`; `. . . . . . . . . . . . . . . . . . .`; `. . . . . . .`
- repetition_loop: `就看购年性大大了，你这种有的时候觉得分期很来常，可能就不会很喜欢。对。对。对。对。对。对。对。对对。对对。对对。对对。对`; `客户吸引力。对对对。对对`; `，然后多找几个品牌，我比较好一点的地方。对对对对，找`
