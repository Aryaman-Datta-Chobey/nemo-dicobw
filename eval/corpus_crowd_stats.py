#!/usr/bin/env python
"""Crowdedness of the open training splits: per-session participants (>= 30 s of speech), hours, gender mix.

Sources: AISHELL-4 train RTTMs (train_M extracted in corpora/; train_L/train_S RTTMs extracted to
--a4-extra with  tar -xzf train_{L,S}.tar.gz --wildcards 'train_*/TextGrid/*.rttm'), AliMeeting train
forced-alignment RTTMs, AISHELL-5 train DX01C01 TextGrids, CHiME-6 train JSON, EgoCom train
conversations (video_info.csv), ICSI NXT segments (all meetings). Gender: AISHELL-4 / AliMeeting labels,
EgoCom video_info.csv, ICSI speakers.xml; none for AISHELL-5 and CHiME-6.
Writes <out>/corpus_crowd.{json,md}.

    python eval/corpus_crowd_stats.py --a4-extra <dir> --out results/20261028-corpus-crowd
"""
import argparse
import json, re, glob, csv, xml.etree.ElementTree as ET
from collections import defaultdict, Counter
from pathlib import Path
ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--a4-extra', type=Path, required=True)
ap.add_argument('--out', type=Path, required=True)
args = ap.parse_args()
args.out.mkdir(parents=True, exist_ok=True)
C = Path('/mnt/data/corpora')
sess = {}  # (corpus, session) -> {spk: [airtime_s, gender]}, dur

def rttm(path, gender_fn, corpus):
    d = defaultdict(float); end = 0
    for l in open(path):
        p = l.split()
        if not p or p[0] != 'SPEAKER': continue
        d[p[7]] += float(p[4]); end = max(end, float(p[3]) + float(p[4]))
        sid = p[1]
    sess[(corpus, sid)] = ({k: [v, gender_fn(k)] for k, v in d.items()}, end)

for f in sorted(glob.glob(str(args.a4_extra / '*/TextGrid/*.rttm')) + glob.glob(str(C / 'aishell4/train_M/TextGrid/*.rttm'))):
    rttm(f, lambda k: k.split('-')[-1], 'aishell4_train')
for f in sorted(glob.glob('/mnt/data/refs/alimeeting/forced_alignment/AliMeeting/Train_Ali_far/*.rttm')):
    rttm(f, lambda k: k[0], 'alimeeting_train')
# AISHELL-5 train: tiers of the near-field/headset TextGrids per session (no gender metadata)
for d in sorted(glob.glob(str(C / 'aishell5/train/*'))):
    spk = defaultdict(float); end = 0
    for tg in glob.glob(d + '/DX01C01.TextGrid'):
        t = open(tg, encoding='utf-8', errors='ignore').read()
        for item in re.split(r'item \[\d+\]:', t)[1:]:
            name = re.search(r'name = "([^"]*)"', item).group(1)
            for xmin, xmax, text in re.findall(r'xmin = ([\d.]+)\s+xmax = ([\d.]+)\s+text = "([^"]*)"', item):
                if text.strip():
                    spk[name] += float(xmax) - float(xmin); end = max(end, float(xmax))
    sess[('aishell5_train', Path(d).name)] = ({k: [v, '?'] for k, v in spk.items()}, end)
# CHiME-6 train: JSON transcripts
for f in sorted(glob.glob(str(C / 'chime6/CHiME6_transcriptions/transcriptions/transcriptions/train/*.json'))):
    spk = defaultdict(float); end = 0
    def ts(x):
        h, m, s = x.split(':'); return int(h) * 3600 + int(m) * 60 + float(s)
    for u in json.load(open(f)):
        if 'speaker' in u and 'start_time' in u:
            s, e = ts(u['start_time']), ts(u['end_time']); spk[u['speaker']] += e - s; end = max(end, e)
    sess[('chime6_train', Path(f).stem)] = ({k: [v, '?'] for k, v in spk.items()}, end)
# EgoCom: conversations (parts concatenated by conversation) -> train split only, gender from video_info
info = list(csv.DictReader(open(C / 'egocom/annotations/video_info.csv')))
g = {(r['conversation_id'], r['video_speaker_id']): r['speaker_gender'][0].upper() for r in info}
train_conv = {r['conversation_id'] for r in info if r['train'] == 'True'}
spk = defaultdict(lambda: defaultdict(float)); ends = defaultdict(float)
for r in csv.DictReader(open(C / 'egocom/annotations/ground_truth_transcriptions.csv')):
    if r['conversation_id'] in train_conv and r['startTime'] and r['endTime']:
        spk[r['conversation_id']][r['speaker_id']] += float(r['endTime']) - float(r['startTime'])
        ends[r['conversation_id']] = max(ends[r['conversation_id']], float(r['endTime']))
for cid, d in spk.items():
    sess[('egocom_train', cid)] = ({k: [v, g.get((cid, k), '?')] for k, v in d.items()}, ends[cid])
# ICSI: NXT segments; gender from speakers.xml
gx = {s.get('tag'): s.get('gender', '?')[0] for s in ET.parse(C / 'icsi/ICSI/speakers.xml').getroot().iter('speaker')}
by = defaultdict(lambda: defaultdict(float)); ends = defaultdict(float)
for f in glob.glob(str(C / 'icsi/ICSI/Segments/*.segs.xml')):
    m = Path(f).name.split('.')[0]
    for s in ET.parse(f).getroot().iter('segment'):
        p = s.get('participant')
        if not s.get('starttime') or not s.get('endtime'): continue
        a, b = float(s.get('starttime')), float(s.get('endtime'))
        by[m][p] += b - a; ends[m] = max(ends[m], b)
for m, d in by.items():
    sess[('icsi', m)] = ({k: [v, gx.get(k, '?')] for k, v in d.items()}, ends[m])

rows = defaultdict(list)
for (c, s), (spk, dur) in sess.items():
    real = {k: v for k, v in spk.items() if v[0] >= 30}  # participants with >= 30 s of speech
    gs = Counter(v[1] for v in real.values())
    rows[c].append(dict(n_all=len(spk), n=len(real), dur=dur, f=gs.get('F', 0), m=gs.get('M', 0),
                        maxsame=max(gs.get('F', 0), gs.get('M', 0)) if '?' not in gs else None))
json.dump({c: r for c, r in rows.items()}, open(args.out / 'corpus_crowd.json', 'w'))
md = ['# Crowdedness of the open training splits', '', 'Participants = speakers with >= 30 s of speech. Generated by eval/corpus_crowd_stats.py.', '',
      '| corpus | sessions | hours | participants: sessions | 5-8 sessions | 5-8 hours | 5-8 with >= 3 same-gender | 5-8 with >= 3 female | > 8 |',
      '|---|---|---|---|---|---|---|---|---|']
for c, r in sorted(rows.items()):
    h = sum(x['dur'] for x in r) / 3600
    cnt = Counter(min(x['n'], 9) for x in r)
    c58 = [x for x in r if 5 <= x['n'] <= 8]
    s3 = [x for x in c58 if x['maxsame'] is not None and x['maxsame'] >= 3]
    f3 = [x for x in c58 if x['f'] >= 3]
    md.append(f"| {c} | {len(r)} | {h:.1f} | {', '.join(f'{k}: {v}' for k, v in sorted(cnt.items()))} | {len(c58)} | "
              f"{sum(x['dur'] for x in c58) / 3600:.1f} | {len(s3) if c58 and c58[0]['maxsame'] is not None else '–'} | "
              f"{len(f3) if c58 and c58[0]['maxsame'] is not None else '–'} | {sum(x['n'] > 8 for x in r)} |")
    print(f"{c}: {len(r)} sessions {h:.1f} h | n_spk(>=30s) dist {sorted(cnt.items())} | 5-8: {len(c58)} sess "
          f"{sum(x['dur'] for x in c58)/3600:.1f} h | >=3 same-gender: {len(s3)} | >=3 female: {len(f3)} | >8: {sum(x['n']>8 for x in r)}")
(args.out / 'corpus_crowd.md').write_text('\n'.join(md) + '\n')
