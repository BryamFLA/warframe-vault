import json,os,re,wiki
S=json.load(open('stubs.json'))
SKIP=re.compile(r'^(This section is transcluded|All drop rates|See Mission Rewards|For more detailed|visit here|Drop tables outdated|Lith, Meso|It can be sold for|Readers can update|Location data)')
out={}
for o in S:
    fn='cache/'+re.sub(r'[^A-Za-z0-9_-]','_',o['title'].replace(' e ',' & '))+'.txt'
    t=open(fn,encoding='utf-8').read()
    sec=wiki.section(t,'Acquisition')
    lines=[]
    for l in sec.split('\n'):
        l=l.strip().replace('\xa0',' ')
        if not l or l.startswith('[edit') or SKIP.match(l): continue
        if l.startswith('Item') or l.startswith('|') or ' | ' in l: break
        if len(l.split())<5: continue
        l=re.sub(r'(Credits|Standing|Platinum|Ducats) ([\d,]+)\b',r'\1',l)  # remove duplicated icon numbers
        lines.append(l)
        if len(lines)>=4: break
    out[o['title']]=' '.join(lines)
json.dump(out,open('acq_en.json','w'),ensure_ascii=False,indent=0)
L=[len(v) for v in out.values()]; print(len(out), sum(L), sum(1 for v in L if v==0))
