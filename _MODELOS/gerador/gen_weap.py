from build import *
SLOT={'Primary':'primária','Secondary':'secundária','Melee':'melee','Archgun':'Archgun (Archwing)','Archmelee':'Archmelee (Archwing)','Arch-Gun':'Archgun','Arch-Melee':'Archmelee'}
DMG={'Impact':'Impacto','Puncture':'Perfuração','Slash':'Corte','Heat':'Calor','Cold':'Frio','Electricity':'Eletricidade','Toxin':'Tóxico','Blast':'Explosão','Radiation':'Radiação','Gas':'Gás','Magnetic':'Magnético','Viral':'Viral','Corrosive':'Corrosivo','Void':'Void','Tau':'Tau','True':'Verdadeiro'}
OVR={'MK1-Braton':'Mk1-Braton','Twin Grakata':'Twin Grakatas','Dark Split-Sword':'Dark Split-Sword (Dual Swords)','Vermisplicer':'Vermisplicer (Primary)','Catchmoon':'Catchmoon (Secondary)','Tombfinger':'Tombfinger (Secondary)','Rattleguts':'Rattleguts (Secondary)','Gaze':'Gaze (Secondary)'}
def wname(t): return OVR.get(t,t.replace(' e ',' & '))
def gen_weapon(title,path):
    nm=wname(title); w=data.WEAP.get(nm)
    if not w: return None
    name=w['Name'] if title not in OVR else title; prime='Prime' in name
    slot=SLOT.get(w.get('Slot'),w.get('Slot','')); cls=w.get('Class','')
    acq=ACQ.get(title,'')
    bp=data.BP.get(w['Name']) or data.BP_BY_RESULT.get(w['Name']) or data.BP.get(name)
    atk=(w.get('Attacks') or [{}])[0]
    if prime and not acq:
        s0,na,nv=relics(name,'Blueprint'); how=f"peças Prime saem de Relíquias do Void ({'disponíveis' if na else 'todas vaultadas no momento'})"
    else: how=strip_md(acq.split('. ')[0]).rstrip('.') if acq else 'ver Onde Conseguir'
    resumo=f"{name} — arma {slot} ({cls}), MR {w.get('Mastery',0)}. Como conseguir: {how}."
    if bp: resumo+=f" Forja: {n(bp.get('Credits',0))} créditos" + (f" + {', '.join(strip_md(resource_line(parts_table(bp,name))).split(' + '))}" if resource_line(parts_table(bp,name)) else '') + '.'
    resumo=re.sub(r'\[\[[^|\]]*\\?\|([^\]]*)\]\]',r'\1',resumo)
    L=['---',f'title: {name}','aliases: ['+', '.join(dict.fromkeys([name,title,f'arma {name}']))+']','tipo: arma',f"subtipo: {(w.get('Slot') or '').lower()}",f"categoria: {cls.lower()}",
       f'resumo: "{esc(resumo)}"','status: parcial','rag: true','tags: [arma'+(', prime' if prime else '')+']',f"mastery_rank: {w.get('Mastery',0)}",
       f'fontes: ["https://wiki.warframe.com/w/{name.replace(" ","_")}", "https://wiki.warframe.com/w/Module:Weapons/data", "https://wiki.warframe.com/w/Module:Blueprints/data", "https://wiki.warframe.com/w/Module:DropTables/data", "https://wiki.warframe.com/w/Module:Void/data"]',
       f'atualizado: {TODAY}','verificado: true','agente: opus','gerado_de: modulos-da-wiki','---','',f'# {name}','','> [!info] Resumo']
    dmg=atk.get('Damage') or {}
    main=max(dmg,key=dmg.get) if dmg else None
    L.append(f"> Arma **{slot}** ({cls}), **MR {w.get('Mastery',0)}**" + (f", dano principal **{DMG.get(main,main)}**" if main and dmg[main]>0 else '') + (f", introduzida no Update {w['Introduced']}" if w.get('Introduced') else '') + '.')
    L.append('')
    L.append(f'## 🌍 Onde Conseguir — {name}'); L.append(''); L.append(f'Como conseguir a arma {name}:'); L.append('')
    if acq: L.append(acq); L.append('')
    rows=[]
    partnames=[p['Name'] for p in (bp or {}).get('Parts',[]) if p.get('Type') in ('Item','PrimePart')]
    for c in ['Blueprint']+partnames:
        item=f"{name} {c}" if c!='Blueprint' else f"{name} Blueprint"
        ds,more=drops(item,4)
        if not ds and c!='Blueprint': ds,more=drops(f"{name} {c} Blueprint",4)
        for lab,ch in ds: rows.append((c,lab,ch))
    if rows:
        L.append('| Peça | Fonte (drop) | Chance |'); L.append('|---|---|---|')
        for c,lab,ch in rows: L.append(f'| {c} | {lab} | {pct(ch)} |')
        L.append('')
    if prime:
        L.append('| Peça Prime | Relíquias ativas (raridade) | Ativas / vaultadas |'); L.append('|---|---|---|'); anyr=False
        for c in ['Blueprint']+partnames:
            s,na,nv=relics(name,c); anyr|=bool(na or nv)
            L.append(f'| {c} | {s} | {na} / {nv} |')
        L.append('')
        L.append('> Relíquias **vaultadas** não caem mais em missões; só voltam no **Prime Resurgence** (Varzia) ou por troca entre jogadores.' if anyr else '> Sem dados de Relíquia no módulo da wiki.'); L.append('')
    extra=[]
    if bp and bp.get('BPCost'): extra.append(f"blueprint no **Mercado por {n(bp['BPCost'])} créditos**")
    if bp and bp.get('MarketCost'): extra.append(f"arma pronta no Mercado por **{n(bp['MarketCost'])} platina**")
    if extra: L.append('**Mercado:** '+'; '.join(extra)+'.'); L.append('')
    if bp:
        prow=parts_table(bp,name); cs=[(p['Name'],p.get('Count',1),p.get('Cost')) for p in bp.get('Parts',[]) if p.get('Type') in ('Item','PrimePart')]
        L.append(f'## 🏗️ Como Construir — {name} (passo a passo)'); L.append('')
        L.append(f"1. **Consiga o blueprint** de {name} (seção anterior).")
        k=2
        if cs:
            L.append(f"{k}. **Consiga os componentes:** {', '.join(f'{c} ×{q}' if q>1 else c for c,q,_ in cs)}" + (" (Relíquias do Void)" if prime else '') + '.'); k+=1
            if any(cost for _,_,cost in cs): L.append(f"{k}. **Forje os componentes** que têm receita (tabela abaixo)."); k+=1
        rl=resource_line(prow)
        L.append(f"{k}. **Junte os recursos e forje na Foundry:** {n(bp.get('Credits',0))} créditos" + (f" + {rl}" if rl else '') + (f" + {', '.join(c for c,_,_ in cs)}" if cs else '') + f". Tempo: **{tempo(bp.get('Time'))}**" + (f" (pular: {bp['Rush']} platina)" if bp.get('Rush') else '') + '.'); k+=1
        L.append(f"{k}. **Upe a arma até o rank 30** para ganhar Mastery.")
        L.append('')
        L.append('| Item | Créditos | Recursos | Tempo |'); L.append('|---|---|---|---|')
        for c,q,cost in cs:
            if cost: L.append(f"| {c}{' ×'+str(q) if q>1 else ''} | {n(cost.get('Credits',0))} | {resource_line(parts_table(cost,name)) or '—'} | {tempo(cost.get('Time'))} |")
        L.append(f"| **{name}** | {n(bp.get('Credits',0))} | {rl or '—'}{(' + '+', '.join(c for c,_,_ in cs)) if cs else ''} | {tempo(bp.get('Time'))} |")
        L.append('')
    L.append(f'## 📊 Stats Base — {name}'); L.append(''); L.append('| Atributo | Valor |'); L.append('|---|---|')
    L.append(f"| Mastery Rank | {w.get('Mastery',0)} |"); L.append(f"| Slot / classe | {slot} / {cls} |")
    if w.get('Trigger'): L.append(f"| Gatilho | {w['Trigger']} |")
    if dmg and sum(dmg.values())>0:
        tot=sum(dmg.values()); L.append(f"| Dano total ({atk.get('AttackName','ataque principal')}) | {str(round(tot,2)).replace('.',',')} |")
        for k2,v in dmg.items(): L.append(f"| — {DMG.get(k2,k2)} | {str(round(v,2)).replace('.',',')} |")
    for k2,lab,f in [('CritChance','Chance de crítico',lambda v:pct(v*100)),('CritMultiplier','Multiplicador crítico',lambda v:str(v).replace('.',',')+'x'),('StatusChance','Chance de status',lambda v:pct(v*100)),('FireRate','Cadência',lambda v:str(v).replace('.',','))]:
        if atk.get(k2) and sum(dmg.values() or [0])>0: L.append(f"| {lab} | {f(atk[k2])} |")
    for k2,lab in [('Magazine','Pente'),('AmmoMax','Munição máxima'),('Reload','Recarga (s)'),('Range','Alcance'),('FollowThrough','Follow-through'),('Disposition','Disposição de Riven')]:
        if w.get(k2) not in (None,0): L.append(f"| {lab} | {str(w[k2]).replace('.',',')} |")
    if w.get('Polarities'): L.append(f"| Polaridades | {', '.join(w['Polarities'])} |")
    if w.get('Introduced'): L.append(f"| Introduzida | Update {w['Introduced']} |")
    L.append('')
    rel=[]
    fam=w.get('Family')
    if fam:
        for k2,v in data.WEAP.items():
            if isinstance(v,dict) and v.get('Family')==fam and v.get('Name')!=name:
                p=data.TITLE.get(v['Name'].lower()) or data.TITLE.get(v['Name'].replace(' & ',' e ').lower())
                if p and p!=path: rel.append(f"- [[{p}|{v['Name']}]] — mesma família")
    rel.append('- [[mecanicas/forja.md|Forja]] — como funciona a Foundry')
    L.append(f'## 🔗 Relacionados — {name}'); L.append(''); L+=rel[:8]; L.append('')
    return '\n'.join(re.sub(r'(\[\[[^\]]*?)\\\|',r'\1|',l) if not l.lstrip().startswith('|') else l for l in L)
if __name__=='__main__': print(gen_weapon(sys.argv[1],'x'))

def _fixpipes(): pass
