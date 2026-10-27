# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-on__nemotron__auto__agnostic_seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-on__nemotron__auto__agnostic_seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-on__nemotron__auto/hyp_agnostic_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `exact`
- created: `2026-10-27T05:52:36+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-on__nemotron__auto`
- variant: `agnostic_seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 40.64 | 5.94 | 33.85 | 0.85 |
| cpCER | 99.18 | 10.37 | 60.90 | 27.91 |
| tcpCER (collar 5.0 s) | 102.07 | 7.01 | 64.03 | 31.03 |
| per-speaker CER, pooled over 8 pairs | 98.03 | 25.05 | 5.60 | 67.38 |
| cpCER − ORC-CER (attribution) | 58.54 | | | |
| tcpCER − cpCER (timing) | 2.89 | | | |

Missed reference speakers 17, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 987; traditional-character rate 0.00%; empty 5.37%, repetition_loop 3.24%
- repetition_loop: `这个主要还是看手续，这分级还是看手续费的。因为有些银行它这个手续费比较高。所以对客户吸引力。对对对。对对对，开过一些新的`; `对品牌影响不好。这个地方没谈一些，就是咱们专门的专属给咱们这一个地方，这样它又显得很线练。找了专业之后，然后多找几个品牌`; `给老师送过去，老师也乐意收。因为咱们现在关系到一个什么样，因为有的时候你家长送过去，那老师很尴尬，那不可能很尴尬。然后呢`
- empty: `.`; `.`; `.`
