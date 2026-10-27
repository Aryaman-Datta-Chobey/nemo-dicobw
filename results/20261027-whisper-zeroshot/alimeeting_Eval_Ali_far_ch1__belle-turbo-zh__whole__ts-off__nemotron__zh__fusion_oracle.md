# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-off__nemotron__zh__fusion_oracle

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-off__nemotron__zh__fusion_oracle`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-off__nemotron__zh/hyp_fusion_oracle.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:26:26+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-off__nemotron__zh`
- variant: `fusion_oracle`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 36.27 | 10.23 | 25.14 | 0.89 |
| cpCER | 37.89 | 10.91 | 25.62 | 1.37 |
| tcpCER (collar 5.0 s) | 39.10 | 9.81 | 26.77 | 2.52 |
| per-speaker CER, pooled over 25 pairs | 37.89 | 10.91 | 25.62 | 1.37 |
| cpCER − ORC-CER (attribution) | 1.63 | | | |
| tcpCER − cpCER (timing) | 1.20 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 3053; traditional-character rate 0.00%; empty 2.26%, repetition_loop 1.57%
- empty: `。`; `。`; `，`
- repetition_loop: `促销。你包括说咱们现在搞的地灰啊，是吧？滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴`; `滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴`; `滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴`
