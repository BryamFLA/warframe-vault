import os,re,sys,subprocess
V=os.path.expanduser('~/mnt/warframe-vault'); os.chdir(V)
dels=[l.strip() for l in open(sys.argv[1]) if l.strip()]
ren={}  # old->new
if len(sys.argv)>2:
    for l in open(sys.argv[2]):
        a,b=l.split(); ren[a]=b
for p in dels:
    if os.path.exists(p): os.remove(p)
for a,b in ren.items():
    if os.path.exists(a): os.rename(a,b)
D=set(dels); n=0
for dp,dn,fn in os.walk('.'):
    if '/.' in dp: continue
    for f in fn:
        if not f.endswith('.md'): continue
        p=os.path.join(dp,f); t=open(p,encoding='utf-8').read(); o=t
        def rep(m):
            tgt=m.group(1); alias=m.group(3)
            if tgt in ren: return '[['+ren[tgt]+(m.group(2)+alias if alias else '')+']]'
            if tgt in D: return alias or os.path.basename(tgt)[:-3].replace('_',' ').title()
            return m.group(0)
        t=re.sub(r'\[\[([^\]|\\#]+)(?:(\\?\|)([^\]]*))?\]\]',lambda m:rep(m) ,t)
        if t!=o: open(p,'w',encoding='utf-8').write(t); n+=1
print('links ajustados em',n,'arquivos')
