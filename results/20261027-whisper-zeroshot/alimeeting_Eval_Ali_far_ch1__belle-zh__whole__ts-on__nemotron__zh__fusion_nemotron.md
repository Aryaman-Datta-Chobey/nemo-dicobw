# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-on__nemotron__zh__fusion_nemotron

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-on__nemotron__zh__fusion_nemotron`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-on__nemotron__zh/hyp_fusion_nemotron.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T07:07:25+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-on__nemotron__zh`
- variant: `fusion_nemotron`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 63.52 | 20.91 | 15.95 | 26.67 |
| cpCER | 67.27 | 17.28 | 19.63 | 30.35 |
| tcpCER (collar 5.0 s) | 72.40 | 11.48 | 25.10 | 35.82 |
| per-speaker CER, pooled over 25 pairs | 67.27 | 17.28 | 19.63 | 30.35 |
| cpCER − ORC-CER (attribution) | 3.75 | | | |
| tcpCER − cpCER (timing) | 5.12 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 3689; traditional-character rate 0.00%; repetition_loop 2.93%
- repetition_loop: `是姚调有针对性的我觉得咱们的设计外观还是很时尚还是需要去设定一下比较适合的年龄段啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊`; `哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦`; `对对对对对`
