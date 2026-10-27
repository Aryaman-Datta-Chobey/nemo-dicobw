# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__dicow-large__per_speaker__ts-on__oracle__zh__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__dicow-large__per_speaker__ts-on__oracle__zh__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__dicow-large__per_speaker__ts-on__oracle__zh/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T11:49:12+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_near__dicow-large__per_speaker__ts-on__oracle__zh`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 10.59 | 4.34 | 5.22 | 1.04 |
| cpCER | 10.64 | 4.29 | 5.27 | 1.08 |
| tcpCER (collar 5.0 s) | 10.65 | 4.28 | 5.28 | 1.10 |
| per-speaker CER, pooled over 25 pairs | 10.64 | 4.29 | 5.27 | 1.08 |
| cpCER − ORC-CER (attribution) | 0.05 | | | |
| tcpCER − cpCER (timing) | 0.02 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 7935; traditional-character rate 0.08%; english_dominant 0.14%, repetition_loop 0.42%, traditional 0.11%
- repetition_loop: `操作不了是吧 因为操作不了对对对对`; `影响力大一些的 好吧 现在咱们就说 说说说这个`; `不过所以说咱们做 做 做 做几个方案`
- english_dominant: `A A B C象`; `bouquet bouquet`; `to yosh yosh yosh`
- traditional: `把這個東西給你`; `預算`; `因為他們`
