# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-on__nemotron__zh__fusion_nemotron

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-on__nemotron__zh__fusion_nemotron`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-on__nemotron__zh/hyp_fusion_nemotron.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T06:03:41+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-on__nemotron__zh`
- variant: `fusion_nemotron`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 35.58 | 8.38 | 26.67 | 0.53 |
| cpCER | 36.49 | 8.84 | 26.89 | 0.76 |
| tcpCER (collar 5.0 s) | 37.48 | 8.60 | 27.51 | 1.37 |
| per-speaker CER, pooled over 25 pairs | 36.49 | 8.84 | 26.89 | 0.76 |
| cpCER − ORC-CER (attribution) | 0.92 | | | |
| tcpCER − cpCER (timing) | 0.99 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 3863; traditional-character rate 0.00%; empty 1.76%, repetition_loop 0.10%
- empty: `。`; `。`; `。`
- repetition_loop: `这个东西，你你你你你送你送的是班主任，其他老师没有，你这个`; `我们这回的标题，中秋晚会就不可能只叫中秋晚会了。像我们这回的主题叫让你更好地懂我。我说标题我们这回可以可以标题可以取取取`; `您刚刚说白天嘛，白天其实我觉得我们可以做一整天，也就是星期六星期六。但是我们只提供晚餐走，白天的话只提供。提供饮料这样，`
