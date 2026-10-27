# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-on__nemotron__zh__agnostic_seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-on__nemotron__zh__agnostic_seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-on__nemotron__zh/hyp_agnostic_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `exact`
- created: `2026-10-27T06:03:08+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-on__nemotron__zh`
- variant: `agnostic_seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 62.47 | 3.01 | 59.09 | 0.37 |
| cpCER | 91.73 | 14.95 | 67.75 | 9.03 |
| tcpCER (collar 5.0 s) | 99.71 | 5.16 | 76.64 | 17.92 |
| per-speaker CER, pooled over 8 pairs | 80.08 | 35.99 | 22.34 | 21.75 |
| cpCER − ORC-CER (attribution) | 29.26 | | | |
| tcpCER − cpCER (timing) | 7.98 | | | |

Missed reference speakers 17, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 698; traditional-character rate 0.00%; repetition_loop 0.43%
- repetition_loop: `这个送这个送给老师，但是又怕比如说对老师上课的时候，他不能接电话，这也是一个问题，是吧，那你这个东西，你你你你你送你送的`; `我们这回的标题，中秋晚会就不可能只叫中秋晚会了。像我们这回的主题叫让你更好地懂我。我说标题我们这回可以可以标题可以取取取`; `提供饮料这样，因为白天会口渴嘛，提供饮料，但是餐补的话就没有了。就是没有吃的，有下午茶这种。然后白天因为我们是在草地嘛，`
