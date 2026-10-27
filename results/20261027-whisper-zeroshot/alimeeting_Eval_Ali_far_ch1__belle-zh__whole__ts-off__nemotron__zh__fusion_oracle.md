# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-off__nemotron__zh__fusion_oracle

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-off__nemotron__zh__fusion_oracle`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-off__nemotron__zh/hyp_fusion_oracle.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:26:23+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-off__nemotron__zh`
- variant: `fusion_oracle`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 35.34 | 8.82 | 25.65 | 0.88 |
| cpCER | 36.98 | 9.75 | 26.00 | 1.23 |
| tcpCER (collar 5.0 s) | 38.46 | 8.95 | 27.14 | 2.37 |
| per-speaker CER, pooled over 25 pairs | 36.98 | 9.75 | 26.00 | 1.23 |
| cpCER − ORC-CER (attribution) | 1.63 | | | |
| tcpCER − cpCER (timing) | 1.48 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 2815; traditional-character rate 0.00%; repetition_loop 0.25%
- repetition_loop: `下就是那个店里面线下自己门店或者在店里面肯定也会出一些logo像我们要是明星代言的话出一些那种这叫什么呀一百五十对对对对`; `可以可以可以可以谈转`; `对对对对对对对对对对对对对对对对对对对对对`
