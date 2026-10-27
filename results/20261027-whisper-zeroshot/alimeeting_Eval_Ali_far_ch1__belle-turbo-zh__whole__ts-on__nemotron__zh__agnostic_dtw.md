# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-on__nemotron__zh__agnostic_dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-on__nemotron__zh__agnostic_dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-on__nemotron__zh/hyp_agnostic_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `exact`
- created: `2026-10-27T05:54:14+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-on__nemotron__zh`
- variant: `agnostic_dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 38.91 | 8.72 | 25.66 | 4.54 |
| cpCER | 107.60 | 7.52 | 60.60 | 39.48 |
| tcpCER (collar 5.0 s) | 109.99 | 8.72 | 61.19 | 40.07 |
| per-speaker CER, pooled over 8 pairs | 118.36 | 18.16 | 4.87 | 95.32 |
| cpCER − ORC-CER (attribution) | 68.69 | | | |
| tcpCER − cpCER (timing) | 2.39 | | | |

Missed reference speakers 17, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 430; traditional-character rate 0.00%; empty 1.63%, repetition_loop 10.70%
- repetition_loop: `代言，这是另外一个方面。然后我觉得就比如说他不买着一些什么移动啊，这些运营商，然后他的一些产品，然后其他的这样还能带有更`; `级还是看手续费的。因为有些银行它这个手续费比较高。所以对客户吸引力。对对对。对对`; `牌影响不好。这个地方没谈一些，就是咱们专门的专属给咱们这一个地方，这样它又显得很线练。找了专业之后，然后多找几个品牌，我`
- empty: `.`; `。`; `. .`
