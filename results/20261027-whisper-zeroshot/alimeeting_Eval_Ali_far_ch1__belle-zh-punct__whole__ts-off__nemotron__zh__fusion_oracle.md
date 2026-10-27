# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-off__nemotron__zh__fusion_oracle

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-off__nemotron__zh__fusion_oracle`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-off__nemotron__zh/hyp_fusion_oracle.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:26:24+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-off__nemotron__zh`
- variant: `fusion_oracle`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 35.11 | 8.28 | 26.22 | 0.61 |
| cpCER | 36.59 | 9.31 | 26.45 | 0.84 |
| tcpCER (collar 5.0 s) | 37.64 | 8.98 | 27.14 | 1.52 |
| per-speaker CER, pooled over 25 pairs | 36.59 | 9.31 | 26.45 | 0.84 |
| cpCER − ORC-CER (attribution) | 1.48 | | | |
| tcpCER − cpCER (timing) | 1.05 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 3083; traditional-character rate 0.00%; empty 1.30%, repetition_loop 0.16%
- empty: `。`; `。`; `，`
- repetition_loop: `那你这个东西你你你你送你送的是班主任，其他老师没有，你这个这个这个你你要知道是哪个家长送的，也是一个问题啊，对吧，不能所`; `，对，对，对，对，`; `我们这回的标题，中秋晚会就不可能只叫中秋晚会了，像我们这回的主题叫让你更好地懂我，我说标题我们这回可以可以标题可以取取取`
