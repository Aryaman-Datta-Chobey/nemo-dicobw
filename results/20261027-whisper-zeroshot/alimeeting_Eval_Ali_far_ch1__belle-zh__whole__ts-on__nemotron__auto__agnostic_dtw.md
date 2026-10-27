# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-on__nemotron__auto__agnostic_dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-on__nemotron__auto__agnostic_dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-on__nemotron__auto/hyp_agnostic_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `exact`
- created: `2026-10-27T10:20:44+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-on__nemotron__auto`
- variant: `agnostic_dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 64.70 | 11.77 | 21.11 | 31.83 |
| cpCER | 138.08 | 6.61 | 60.37 | 71.09 |
| tcpCER (collar 5.0 s) | 145.61 | 14.64 | 60.13 | 70.85 |
| per-speaker CER, pooled over 8 pairs | 191.69 | 15.91 | 4.57 | 171.21 |
| cpCER − ORC-CER (attribution) | 73.38 | | | |
| tcpCER − cpCER (timing) | 7.54 | | | |

Missed reference speakers 17, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 516; traditional-character rate 0.00%; repetition_loop 15.70%
- repetition_loop: `好那么今天就是咱们公司新出的一款手机产品进行一下这个研讨会首先咱们确定一下咱们这个产品的目标这个人群客户群这一块首先谈大`; `推销你比方说他们现在搞这个地推呀是吧DJ如果早点晚上的我觉得有一个方向吧可以看一下自己不同的一个我感觉DJ这个不太适合手`; `感觉就是还可以用客户就每日活跃人数嘛像抖音这种它日活跃人数可能有超过三亿嘛快手这种日活跃人数咱们在这个平台上面还可以做一`
