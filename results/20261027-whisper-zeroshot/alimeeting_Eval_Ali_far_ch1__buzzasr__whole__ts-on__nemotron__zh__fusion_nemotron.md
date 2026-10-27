# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-on__nemotron__zh__fusion_nemotron

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-on__nemotron__zh__fusion_nemotron`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-on__nemotron__zh/hyp_fusion_nemotron.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:22:06+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-on__nemotron__zh`
- variant: `fusion_nemotron`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 52.21 | 27.32 | 21.04 | 3.85 |
| cpCER | 56.19 | 25.87 | 23.76 | 6.57 |
| tcpCER (collar 5.0 s) | 61.92 | 14.96 | 32.07 | 14.88 |
| per-speaker CER, pooled over 25 pairs | 56.19 | 25.87 | 23.76 | 6.57 |
| cpCER − ORC-CER (attribution) | 3.98 | | | |
| tcpCER − cpCER (timing) | 5.72 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 3471; traditional-character rate 0.27%; empty 0.63%, repetition_loop 1.67%, traditional 0.14%
- repetition_loop: `对对对对对对对对对对对对对对对对对对对对对对时间就看年性大大的对嘛你这种有时种觉得分期很大长可能人就不喜欢就吧`; `提供企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业`; `我们这个确定然后我们这个确然后我们这个确然后我们这个确然后我们这个确然后我们这个确然后我们这个确然后我们这个确然后我们这`
- empty: `。`; `。`; `。`
- traditional: `這個`; `環`; `然後我們`
