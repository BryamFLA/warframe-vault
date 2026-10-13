#!/usr/bin/env python3
"""Regenera as seções '## 📋 Lista' de todos os _* _Indice.md a partir do frontmatter (rodar na raiz do vault)."""
import os,re,glob,yaml,collections
V=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
def fm(p):
    t=open(p,encoding='utf-8').read(); m=re.match(r'---\n(.*?)\n---\n',t,re.S)
    try: return (yaml.safe_load(m.group(1)) or {}) if m else {}
    except Exception: return {}
idx=[p for p in glob.glob(V+'/**/_*_Indice.md',recursive=True) if '/_MODELOS/' not in p]
idx_dirs={os.path.dirname(p):p for p in idx}
def cell(s): return str(s).replace('|','\\|').replace('\n',' ')
for ip in sorted(idx):
    d=os.path.dirname(ip); title=fm(ip).get('title') or os.path.basename(ip)[:-3]
    groups=collections.OrderedDict(); subidx=[]
    for root,dirs,files in os.walk(d):
        dirs.sort()
        if root!=d and root in idx_dirs:
            n=sum(1 for r,_,fs in os.walk(root) for f in fs if f.endswith('.md') and not f.startswith('_'))
            subidx.append((idx_dirs[root],n)); dirs[:]=[]; continue
        for f in sorted(files):
            if not f.endswith('.md') or f.startswith('_'): continue
            p=os.path.join(root,f); m=fm(p)
            if m.get('rag') is False: continue
            g=os.path.relpath(root,d)
            g='geral' if g=='.' else g
            if len([1 for r,_,fs in os.walk(d) for x in fs])>250 and m.get('subtipo'): g=f"{g} · {m['subtipo']}"
            groups.setdefault(g,[]).append((p,m))
    total=sum(len(v) for v in groups.values())+sum(n for _,n in subidx)
    out=[]
    if subidx:
        out+=[f'## 📋 Lista — {title} — Sub-índices','','| Sub-índice | Notas |','|---|---|']
        for p,n in subidx:
            out.append(f"| [[{os.path.relpath(p,V)}\\|{cell(fm(p).get('title',os.path.basename(p)[:-3]))}]] | {n} |")
        out.append('')
    for g,items in groups.items():
        out+=[f'## 📋 Lista — {title} — {g} ({len(items)})','','| Nome | Tipo | MR | Resumo |','|---|---|---|---|']
        for p,m in sorted(items,key=lambda x:str(x[1].get('title','')).lower()):
            r=re.sub(r'\s+',' ',str(m.get('resumo','')))
            r=r[:140]+('…' if len(r)>140 else '')
            out.append(f"| [[{os.path.relpath(p,V)}\\|{cell(m.get('title',os.path.basename(p)[:-3]))}]] | {cell(m.get('subtipo') or m.get('categoria') or m.get('tipo',''))} | {m.get('mastery_rank','—')} | {cell(r)} |")
        out.append('')
    t=open(ip,encoding='utf-8').read()
    # remove seções geradas antigas
    t=re.sub(r'\n## 📋 Lista — .*?(?=\n## (?!📋 Lista)|\Z)','\n',t,flags=re.S)
    block='\n'.join(out)
    anchor=re.search(r'\n## (🔗 Relacionados|📚 Fontes)',t)
    t=(t[:anchor.start()]+'\n\n'+block+t[anchor.start():]) if anchor else (t.rstrip()+'\n\n'+block)
    t=re.sub(r'^(atualizado:).*$',r'\1 2026-10-13',t,1,flags=re.M)
    if re.search(r'^total-notas:',t,re.M): t=re.sub(r'^total-notas:.*$',f'total-notas: {total}',t,1,flags=re.M)
    else: t=t.replace('\n---\n',f'\ntotal-notas: {total}\n---\n',1)
    t=re.sub(r'\n{3,}','\n\n',t)
    open(ip,'w',encoding='utf-8').write(t)
    print(f'{os.path.relpath(ip,V)}: {total}')
