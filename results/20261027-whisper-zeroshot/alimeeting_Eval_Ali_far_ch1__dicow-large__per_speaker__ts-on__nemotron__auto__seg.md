# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__dicow-large__per_speaker__ts-on__nemotron__auto__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__dicow-large__per_speaker__ts-on__nemotron__auto__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__dicow-large__per_speaker__ts-on__nemotron__auto/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:22:16+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__dicow-large__per_speaker__ts-on__nemotron__auto`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 27.87 | 16.84 | 7.36 | 3.67 |
| cpCER | 28.42 | 16.39 | 7.86 | 4.17 |
| tcpCER (collar 5.0 s) | 29.39 | 15.06 | 9.01 | 5.32 |
| per-speaker CER, pooled over 25 pairs | 28.42 | 16.39 | 7.86 | 4.17 |
| cpCER − ORC-CER (attribution) | 0.55 | | | |
| tcpCER − cpCER (timing) | 0.97 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 7952; traditional-character rate 0.11%; english_dominant 4.31%, repetition_loop 0.73%, traditional 0.15%
- english_dominant: `so you are following that idea as well`; `good idea`; `yeah con yeah clearly clearly look on`
- repetition_loop: `先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 `; `出款的就得得得得得`; `三二三二 三二 三二`
- traditional: `也許`; `這樣的話會會不會不好這個想法`; `人家長的家這個這個信義啊和這個`
