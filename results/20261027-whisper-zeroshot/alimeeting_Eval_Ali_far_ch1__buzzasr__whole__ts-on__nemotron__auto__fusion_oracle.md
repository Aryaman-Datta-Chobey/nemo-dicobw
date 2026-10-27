# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-on__nemotron__auto__fusion_oracle

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-on__nemotron__auto__fusion_oracle`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-on__nemotron__auto/hyp_fusion_oracle.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:27:14+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-on__nemotron__auto`
- variant: `fusion_oracle`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 52.13 | 27.04 | 21.14 | 3.94 |
| cpCER | 56.35 | 24.92 | 24.31 | 7.11 |
| tcpCER (collar 5.0 s) | 62.17 | 14.87 | 32.25 | 15.05 |
| per-speaker CER, pooled over 25 pairs | 56.35 | 24.92 | 24.31 | 7.11 |
| cpCER − ORC-CER (attribution) | 4.22 | | | |
| tcpCER − cpCER (timing) | 5.82 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 2747; traditional-character rate 0.27%; empty 0.55%, english_dominant 0.04%, repetition_loop 2.15%, traditional 0.18%
- empty: `。`; `。`; `。`
- repetition_loop: `对对对对对对对对对对对对对对对对对对对对对对时间就看年性大大的对嘛你这种有时种觉得分期很大长可能人就不喜欢就吧这个`; `提供企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业`; `我们这个确定然后我们这个确然后我们这个确然后我们这个确然后我们这个确然后我们这个确然后我们这个确然后我们这个确然后我们这`
- traditional: `吧能夠提出他那個教師的這個價值現在這個環`; `然後我們`; `開班`
- english_dominant: `需要A ust ral`
