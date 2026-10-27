# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-on__nemotron__auto__fusion_oracle

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-on__nemotron__auto__fusion_oracle`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-on__nemotron__auto/hyp_fusion_oracle.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:26:21+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-on__nemotron__auto`
- variant: `fusion_oracle`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 35.28 | 8.03 | 26.69 | 0.56 |
| cpCER | 36.70 | 9.04 | 26.90 | 0.76 |
| tcpCER (collar 5.0 s) | 37.75 | 8.77 | 27.56 | 1.42 |
| per-speaker CER, pooled over 25 pairs | 36.70 | 9.04 | 26.90 | 0.76 |
| cpCER − ORC-CER (attribution) | 1.43 | | | |
| tcpCER − cpCER (timing) | 1.05 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 3068; traditional-character rate 0.00%; empty 1.40%, repetition_loop 0.13%
- empty: `。`; `。`; `，`
- repetition_loop: `这个东西，你你你你你送你送的是班主任，其他老师没有，你这个这个这个你你要知道是哪个家长送的，也是一个问题啊，对吧？这个问`; `我们这回的标题，中秋晚会就不可能只叫中秋晚会了。像我们这回的主题叫让你更好地懂我。我说标题我们这回可以可以标题可以取取取`; `天的话只提供。提供饮料这样，因为白天会口渴嘛，提供饮料，但是餐补的话就没有了。就是没有吃的，有下午茶这种。然后白天因为我`
