# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-off__nemotron__zh__agnostic_dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-off__nemotron__zh__agnostic_dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-off__nemotron__zh/hyp_agnostic_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `exact`
- created: `2026-10-27T06:06:00+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-off__nemotron__zh`
- variant: `agnostic_dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 33.11 | 5.81 | 26.04 | 1.27 |
| cpCER | 103.39 | 6.71 | 60.73 | 35.95 |
| tcpCER (collar 5.0 s) | 103.86 | 6.85 | 60.89 | 36.12 |
| per-speaker CER, pooled over 8 pairs | 108.16 | 16.15 | 5.42 | 86.59 |
| cpCER − ORC-CER (attribution) | 70.28 | | | |
| tcpCER − cpCER (timing) | 0.48 | | | |

Missed reference speakers 17, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 552; traditional-character rate 0.00%; repetition_loop 1.63%
- repetition_loop: `刚才说这个搜搜地我觉得咱们可以再张学一下张学然后说平台上咱们线下有的考虑一下线下就是那个店里面线下自己门店或者在店里面肯`; `一次性通知他们过来的话那就可能会能过来对对对对人太多了有可能效率不高我觉得全员工可以找一些有经验的那我们参与完你做过的一`; `千五三千五啊可以可以那试用期的基本工资就三千吧但是然后试用期满了之后我们得看他们表现转正可以可以可以可以可以谈转`
