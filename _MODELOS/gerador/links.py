#!/usr/bin/env python3
"""Valida wikilinks. --fix converte links quebrados em texto simples."""
import os,re,glob,sys,collections
V=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
files={os.path.relpath(p,V) for p in glob.glob(V+'/**/*.md',recursive=True)}
base={}
for f in files: base.setdefault(os.path.basename(f)[:-3].lower(),[]).append(f)
R=re.compile(r'\[\[([^\]|\\#]+)(#[^\]|\\]*)?(?:(\\?\|)([^\]]*))?\]\]')
bad=collections.Counter(); fix='--fix' in sys.argv; nfix=0
for f in sorted(files):
    if f.startswith('_MODELOS'): continue
    p=os.path.join(V,f); t=open(p,encoding='utf-8').read()
    def rep(m):
        global nfix
        tgt=m.group(1).strip(); t2=tgt if tgt.endswith('.md') else tgt+'.md'
        if t2 in files or tgt in files: return m.group(0)
        b=base.get(os.path.basename(tgt).replace('.md','').lower())
        if b and len(b)==1:
            nfix+=1; return f"[[{b[0]}{m.group(2) or ''}{(m.group(3)+m.group(4)) if m.group(3) else ''}]]"
        bad[(f,tgt)]+=1
        if fix: nfix+=1; return m.group(4) or os.path.basename(tgt).replace('.md','')
        return m.group(0)
    t2=R.sub(rep,t)
    if t2!=t and (fix or True): open(p,'w',encoding='utf-8').write(t2)
print('quebrados',sum(bad.values()),'arquivos',len({f for f,_ in bad}),'corrigidos',nfix)
for (f,tgt),n in list(bad.items())[:25]: print(f,'->',tgt)
