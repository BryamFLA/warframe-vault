import os,re,json,sys
sys.path.insert(0,os.path.expanduser('~/gen'))
import data
from sections import upsert
V=os.path.expanduser('~/mnt/warframe-vault')
B=json.load(open('builds_wf.json')); H=json.load(open('hist_wf.json'))
AB=json.load(open('abil_pt.json')); PS=json.load(open('passive_pt.json'))
def lk(n):
    base=re.sub(r'\s*\(.*?\)$','',n).strip()
    p=data.TITLE.get(base.lower())
    return f"[[{p}\\|{n}]]" if p else n
def base_of(t): return t.replace(' Prime','').replace(' Umbra','')
cnt=0
for dp,dn,fn in os.walk(os.path.join(V,'warframes')):
    for f in fn:
        if not f.endswith('.md') or f.startswith('_'): continue
        p=os.path.join(dp,f); t=open(p,encoding='utf-8').read(); o=t
        title=re.search(r'^title:\s*"?(.*?)"?\s*$',t,re.M).group(1)
        b=base_of(title); gen='gerado_de: modulos-da-wiki' in t
        w=data.WF.get(title,{})
        # Habilidades em PT (só gerados)
        if gen and w.get('Abilities'):
            rows=['| # | Habilidade | Energia | O que faz |','|---|---|---|---|']
            for i,a in enumerate(w['Abilities'],1):
                d=data.AB.get(a,{})
                rows.append(f"| {i} | **{a}** | {d.get('Cost','—')} | {AB.get(a,(d.get('Description') or '')).replace('|','/')} |")
            sec=f"## 🔮 Habilidades — {title}\n\n"
            pas=PS.get(title) or PS.get(b)
            if pas: sec+=f"**Passiva:** {pas}\n\n"
            sec+='\n'.join(rows)+'\n'
            if w.get('Subsumed'): sec+=f"\n**Helminth:** a habilidade **{w['Subsumed']}** pode ser subsumida (doada ao Helminth para outros Warframes).\n"
            if w.get('AugmentShop'): sec+=f"\n**Augments** vendidos por: {', '.join(lk(x).replace(chr(92)+'|','|') for x in w['AugmentShop'])}.\n"
            t=upsert(t,'## 🔮 Habilidades',sec)
        # Build
        if b in B and not re.search(r'^## .*Build',t,re.M):
            x=B[b]
            L=[f"## 🛠️ Build — {title}",'',f"Build de referência para **{title}** (curadoria do agente com base no meta 2025–2026 — ajuste ao conteúdo e aos mods que você tem).",'',f"**Foco:** {x['foco']}.",'','| Slot | Mod |','|---|---|',f"| Aura | {lk(x['aura'])} |"]
            for i,m in enumerate(x['mods'],1): L.append(f"| {i} | {lk(m)} |")
            L.append(f"| Exilus | {lk(x['exilus'])} |")
            L+=['',f"**Helminth:** {x['helminth']}.",f"**Arcanes:** {', '.join(x['arcanes'])}.",f"**Dica:** {x['dica']}"]
            if 'Prime' in title: L.append(f"\n**Versão Prime:** mesma build base; a {title} tem mais vida/escudo/armadura ou energia e polaridades extras, o que exige menos Forma.")
            L.append('\n**Iniciante sem Umbral/Primed:** troque Umbral Intensify → Intensify, Umbral Vitality → Vitality, Umbral Fiber → Steel Fiber, Primed Continuity → Continuity, Primed Flow → Flow.')
            t=upsert(t,'## 🛠️ Build','\n'.join(L))
        # História
        if b in H and not re.search(r'^## .*Hist',t,re.M):
            L=[f"## 📖 História — {title}",'',H[b]]
            if 'Prime' in title:
                L.append(f"\n**{title}:** versão Prime, feita na era Orokin com materiais nobres (ouro e Orokin Cells) — o 'modelo original de luxo' da Warframe, com estética dourada e atributos melhores." + (f" *Codex:* \"{w['Description']}\"" if w.get('Description') else ''))
            if 'Umbra' in title: L.append(f"\n**{title}:** versão Umbra — um Warframe que guarda memórias da pessoa que foi, criado por Ballas. Ver a quest The Sacrifice.")
            t=upsert(t,'## 📖 História','\n'.join(L))
        if t!=o: open(p,'w',encoding='utf-8').write(t); cnt+=1
print('warframes atualizados',cnt)
