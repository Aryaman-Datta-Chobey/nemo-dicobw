# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-on__nemotron__auto__fusion_oracle

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-on__nemotron__auto__fusion_oracle`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-on__nemotron__auto/hyp_fusion_oracle.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:26:41+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-on__nemotron__auto`
- variant: `fusion_oracle`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 63.26 | 20.03 | 16.26 | 26.98 |
| cpCER | 67.50 | 16.83 | 19.97 | 30.69 |
| tcpCER (collar 5.0 s) | 72.98 | 11.92 | 25.17 | 35.89 |
| per-speaker CER, pooled over 25 pairs | 67.50 | 16.83 | 19.97 | 30.69 |
| cpCER − ORC-CER (attribution) | 4.24 | | | |
| tcpCER − cpCER (timing) | 5.48 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 2826; traditional-character rate 0.00%; repetition_loop 3.86%
- repetition_loop: `是姚调有针对性的我觉得咱们的设计外观还是很时尚还是需要去设定一下比较适合的年龄段啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊`; `哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦`; `对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对`
