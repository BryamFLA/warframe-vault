#!/usr/bin/env python3
"""Lista itens cuja seção 'Onde Conseguir' (ou fonte_principal) cita um local/hub.
Uso: python3 _MODELOS/gerador/itens_local.py cetus [--write]"""
import re,glob,os,sys,collections
V=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
LOC={'cetus':dict(nota='locais/open-worlds/cetus.md',nome='Cetus / Plains of Eidolon',
     kw=r'Cetus|Ostron|\bQuills\b|Plains of Eidolon|Planícies de Eidolon|Konzu|\bHok\b|Suumbaat|Hai-Luk|Teasonai|Onkko|Eidolon (Teralyst|Gantulyst|Hydrolyst)|Tusk Thumper|Saya|Bounties? (de|das|nas) Plains|Eidolon bount|bounties de Cetus|bounties das Plains',
     excl=r'Father|Necraloid|Rude Zuud|Exige .*Ostron Rank|Ostron Rank \d para',force=r'Onkko|Konzu|\bHok\b|Suumbaat|Hai-Luk|Teasonai|Nakak|Cetus Bounty|Quills')}
def items(loc):
    L=LOC[loc]; out=[]
    for f in sorted(glob.glob(V+'/**/*.md',recursive=True)):
        rel=os.path.relpath(f,V)
        if rel.startswith(('_MODELOS','locais/','lore/','missoes/','mecanicas/','cosmeticos/')) or '/_' in rel: continue
        t=open(f,encoding='utf-8').read()
        m=re.search(r'^## 🌍 Onde Conseguir[^\n]*\n(.*?)(?=\n## |\Z)',t,re.S|re.M)
        fp=re.search(r'^fonte_principal:\s*"?(.*?)"?\s*$',t,re.M)
        src=(m.group(1) if m else '')+' '+(fp.group(1) if fp else '')
        if not re.search(L['kw'],src): continue
        if re.search(L.get('excl','^$'),src) and not re.search(L.get('force','^$'),src): continue
        title=re.search(r'^title:\s*"?(.*?)"?\s*$',t,re.M).group(1)
        tipo=(re.search(r'^tipo:\s*(.*)$',t,re.M) or [0,''])[1].strip()
        # frase-fonte: primeira linha/célula que cita o local
        lines=[re.sub(r'\[\[[^\]|]*\\?\|([^\]]*)\]\]',r'\1',x).strip(' -|*') for x in src.split('\n') if re.search(L['kw'],x)]
        how=re.sub(r'\s*\|\s*',' · ',lines[0])[:160] if lines else ''
        out.append((rel,title,tipo,how))
    return out

LOC.update({
 'fortuna':dict(nota='locais/open-worlds/fortuna.md',nome='Fortuna / Orb Vallis',kw=r'Fortuna|Solaris United|Vox Solaris|Orb Vallis|Eudico|Rude Zuud|\\bLegs\\b|Ticker|The Business|Little Duck|Smokefinger|Profit-Taker|Exploiter Orb|Ventkids|Nightcap|Deepmines'),
 'deimos':dict(nota='locais/open-worlds/deimos.md',nome='Deimos / Cambion Drift',kw=r'Necralisk|Cambion Drift|Necraloid|\bFather\b|\bMother\b|Grandmother|\bOtak\b|Isolation Vault|Deimos|Sanctum Anatomica|Cavia|\bLoid\b'),
 'zariman':dict(nota='locais/open-worlds/zariman.md',nome='Zariman / Chrysalith',kw=r'Zariman|Chrysalith|Holdfasts|Cavalero|Archimedean Yonta|Void Angel|Quinn'),
 'duviri':dict(nota='locais/open-worlds/duviri.md',nome='Duviri / The Circuit',kw=r'Duviri|The Circuit|\\bCircuit\\b|Acrithis|Dormizone|Kaithe|Orowyrm|Undercroft'),
 'hollvania':dict(nota='locais/hollvania.md',nome='Höllvania (1999)',kw=r'Höllvania|Hollvania|\\bThe Hex\\b|Technocyte|Scaldra|Techrot|Calendário do 1999|1999 Calendar|Eleanor|Kaya|Aoi\\b|Quincy|Amir\\b|Lettie|Arthur\\b'),
})
GR=[('Warframes, Armas, Amps e Companheiros',('warframes/','armas/','companheiros/')),('Mods',('mods/warframe/','mods/armas/','mods/companheiros/','mods/especiais/')),('Arcanes',('mods/arcanes/',)),('Recursos, Peixes e Minérios',('recursos/',))]
def write(loc,maxrows=40):
    L=LOC[loc]; it=items(loc); p=os.path.join(V,L['nota']); t=open(p,encoding='utf-8').read()
    t=re.sub(r'\n## 📦 Itens de .*?(?=\n## (?!📦)|\Z)','\n',t,flags=re.S)
    nome=L['nome']; curto=nome.split(' /')[0]
    cats=[(g,[x for x in it if x[0].startswith(pref)]) for g,pref in GR]
    cats=[(g,sorted(sel,key=lambda x:x[1].lower())) for g,sel in cats if sel]
    dest=[x[1] for g,sel in cats if g.startswith('Warframes') for x in sel]
    blk=[f"## 📦 Itens de {nome} — Resumo: tudo o que dá para adquirir",'',
         f"**Todos os itens que você pode adquirir, conseguir ou farmar em {nome}: {len(it)} itens** — "+', '.join(f"{len(sel)} {g.lower()}" for g,sel in cats)+'.','']
    if dest: blk+=[f"**Warframes, armas e equipamentos de {curto}:** "+', '.join(dest)+'.','']
    blk+=[f"A lista completa, item por item e com a forma de conseguir, está nas seções \"📦 Itens de {nome}\" abaixo (geradas da seção Onde Conseguir de cada nota).",'']
    for g,sel in cats:
        parts=[sel[k:k+maxrows] for k in range(0,len(sel),maxrows)]
        for n,part in enumerate(parts,1):
            suf=f" — parte {n}/{len(parts)}" if len(parts)>1 else ''
            blk+=[f"## 📦 Itens de {nome} — {g}{suf} ({part[0][1]} … {part[-1][1]})",'',f"Itens ({g.lower()}) que podem ser adquiridos em {nome}:",'','| Item | Como conseguir |','|---|---|']
            for rel,ti,tp,how in part: blk.append(f"| [[{rel}\\|{ti}]] | {how.replace('|','·')} |")
            blk.append('')
    a=re.search(r'\n## (📖 História|🔗 Relacionados)',t)
    t=t[:a.start()]+'\n\n'+'\n'.join(blk)+t[a.start():] if a else t.rstrip()+'\n\n'+'\n'.join(blk)
    open(p,'w',encoding='utf-8').write(re.sub(r'\n{3,}','\n\n',t)); print('escrito',len(it),'itens em',L['nota'])
if __name__=='__main__' and '--write' in sys.argv:
    for l in (LOC if sys.argv[1]=='all' else [sys.argv[1]]): write(l)

if __name__=='__main__' and '--write' not in sys.argv:
    loc=sys.argv[1]; it=items(loc)
    for x in it: print(x)
    print(len(it))
