# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-on__oracle__zh__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-on__oracle__zh__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-on__oracle__zh/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:20:52+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-on__oracle__zh`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 56.97 | 10.58 | 45.81 | 0.58 |
| cpCER | 58.55 | 10.97 | 46.40 | 1.18 |
| tcpCER (collar 5.0 s) | 64.01 | 10.67 | 49.28 | 4.05 |
| per-speaker CER, pooled over 25 pairs | 58.55 | 10.97 | 46.40 | 1.18 |
| cpCER − ORC-CER (attribution) | 1.58 | | | |
| tcpCER − cpCER (timing) | 5.46 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 2171; traditional-character rate 0.08%; repetition_loop 0.46%
- repetition_loop: `这 不 是 快 到 教 师 节 了 嘛 那 个 看 看 看 看 都 给 孩 子 的 就 是 老 师 送 点 什么 呀 就`; `中 层 房 和 送 房 之 间 可 以 可 以 可 以 可 以 对 还 还 还 好 找 不 错 大 会 还 方 便`; `火气的影对是一个很严重的事情新上年在接触到网络之后接触到这些乱像他们会认为这是一个价值观是被影对的影对会影响了他们的三观`
