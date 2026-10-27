# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-on__nemotron__zh__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-on__nemotron__zh__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-on__nemotron__zh/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:20:50+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-on__nemotron__zh`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 58.00 | 10.29 | 47.07 | 0.64 |
| cpCER | 59.55 | 11.18 | 47.40 | 0.97 |
| tcpCER (collar 5.0 s) | 64.40 | 10.47 | 50.18 | 3.75 |
| per-speaker CER, pooled over 25 pairs | 59.55 | 11.18 | 47.40 | 0.97 |
| cpCER − ORC-CER (attribution) | 1.55 | | | |
| tcpCER − cpCER (timing) | 4.85 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 2028; traditional-character rate 0.22%; repetition_loop 0.35%, traditional 0.15%
- traditional: `能夠體現他那個教師的這個價值現在界的價值`; `我認為作為老師來講 不管誰給他什麼禮品 他不應該輕視 就說給他禮品小 禮物小 他輕視這孩子 因為我覺得在学校 不應該有這`; `這個 大 是`
- repetition_loop: `反 定 不 管 怎 么 吧 就 咱 们 可 定 是 打 包 的 提 前 别 等 着 这 个 班 家 前 一 天 才 急 `; `对对对对`; `对 对 对 对`
