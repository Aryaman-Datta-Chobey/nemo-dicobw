# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__auto__agnostic_dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__auto__agnostic_dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__auto/hyp_agnostic_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `exact`
- created: `2026-10-27T10:21:59+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__auto`
- variant: `agnostic_dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 35.86 | 8.45 | 25.53 | 1.87 |
| cpCER | 105.49 | 7.67 | 60.74 | 37.08 |
| tcpCER (collar 5.0 s) | 106.73 | 8.47 | 60.96 | 37.30 |
| per-speaker CER, pooled over 8 pairs | 113.22 | 18.46 | 5.45 | 89.30 |
| cpCER − ORC-CER (attribution) | 69.63 | | | |
| tcpCER − cpCER (timing) | 1.24 | | | |

Missed reference speakers 17, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 517; traditional-character rate 5.34%; empty 0.19%, english_dominant 0.97%, repetition_loop 4.26%, traditional 1.74%
- english_dominant: `people buy the phone , they just look at the color . Especia`; `in the housing fund It 's also more needed to make housing f`; `這個Let 's see if we can count it . It 's about 60 % of the`
- empty: `?`
- repetition_loop: `The color is the color . I think the color is the color . Th`; `的产品推出去对不是说这个时候能挣多少钱而是把咱们这个产品的量先把报告打开对把报告打开反正我们肯定首先要制作一套完整方案就`; `按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按`
- traditional: `我們還說這個連續那個大`; `眼燈`; `訓也可以學習`
