from build import *
PLAY={'Damage':'dano','Survival':'sobrevivência','Crowd Control':'controle de grupo','Support':'suporte','Stealth':'furtividade','Tank':'tanque'}
def gen_warframe(title,path):
    w=data.WF.get(title)
    if not w: return None
    name=w['Name']; prime='Prime' in name; umbra='Umbra' in name
    base=name.replace(' Prime','').replace(' Umbra','')
    acq=ACQ.get(title,'')
    play=', '.join(PLAY.get(p,p) for p in w.get('Playstyle',[]) or [])
    bp=data.BP.get(name) or data.BP_BY_RESULT.get(name)
    comps=['Neuroptics','Chassis','Systems']
    # resumo
    if prime and not acq:
        s0,na,nv=relics(name,'Blueprint')
        how=f"peças Prime saem de Relíquias do Void ({'disponíveis' if na else 'todas vaultadas no momento'})"
    else:
        how=strip_md(acq.split('. ')[0]).rstrip('.') if acq else 'ver Onde Conseguir'
    resumo=f"{name} — Warframe" + (f" de {play}" if play else '') + f". Como conseguir: {how}."
    L=[]
    L.append('---'); L.append(f'title: {name}')
    al=[name,f'warframe {name}']
    if prime: al.append(f'{base} P')
    L.append('aliases: ['+', '.join(al)+']'); L.append('tipo: warframe')
    if prime: L.append('variante: prime')
    if umbra: L.append('variante: umbra')
    L.append(f'resumo: "{esc(resumo)}"'); L.append('status: parcial'); L.append('rag: true')
    L.append('tags: [warframe'+(', prime' if prime else '')+']')
    if w.get('Progenitor'): L.append(f"progenitor: {w['Progenitor']}")
    L.append(f'fontes: ["https://wiki.warframe.com/w/{name.replace(" ","_")}", "https://wiki.warframe.com/w/Module:Warframes/data", "https://wiki.warframe.com/w/Module:Blueprints/data", "https://wiki.warframe.com/w/Module:DropTables/data", "https://wiki.warframe.com/w/Module:Void/data"]')
    L.append(f'atualizado: {TODAY}'); L.append('verificado: true'); L.append('agente: opus'); L.append('gerado_de: modulos-da-wiki')
    L.append('---'); L.append(''); L.append(f'# {name}'); L.append('')
    L.append('> [!info] Resumo')
    L.append(f"> Warframe{' Prime' if prime else ''}" + (f" de **{play}**" if play else '') + (f", lançada no **Update {w['Introduced']}**" if w.get('Introduced') else '') + '.')
    if w.get('Description'): L.append(f"> *Descrição no jogo (inglês):* \"{w['Description']}\"")
    L.append('')
    # Onde conseguir
    L.append(f'## 🌍 Onde Conseguir — {name}'); L.append('')
    L.append(f'Como conseguir a Warframe {name}:'); L.append('')
    if acq: L.append(acq); L.append('')
    rows=[]
    for c in (['Blueprint']+comps):
        item=f"{name} {c} Blueprint" if c!='Blueprint' else f"{name} Blueprint"
        ds,more=drops(item,4)
        for lab,ch in ds: rows.append((c,lab,ch))
    if rows:
        L.append('| Peça | Fonte (drop) | Chance |'); L.append('|---|---|---|')
        for c,lab,ch in rows: L.append(f'| {c} | {lab} | {pct(ch)} |')
        L.append('')
    if prime:
        L.append('| Peça Prime | Relíquias ativas (raridade) | Ativas / vaultadas |'); L.append('|---|---|---|')
        anyr=False
        for c in ['Blueprint']+[x+' Blueprint' for x in comps]:
            s,na,nv=relics(name,c)
            if na or nv: anyr=True
            L.append(f'| {c} | {s} | {na} / {nv} |')
        L.append('')
        L.append('> Relíquias **vaultadas** não caem mais em missões; só voltam no **Prime Resurgence** (Varzia) ou por troca entre jogadores.' if anyr else '> Sem dados de Relíquia no módulo da wiki.')
        L.append('')
    if bp and bp.get('MarketCost'): L.append(f"**Platina:** pronta no Mercado por **{n(bp['MarketCost'])} platina**."); L.append('')
    # Como construir
    if bp:
        L.append(f'## 🏗️ Como Construir — {name} (passo a passo)'); L.append('')
        prow=parts_table(bp,name)
        cs=[nm for k,nm,c in prow if k=='comp']
        L.append(f"1. **Consiga o blueprint principal** de {name} (seção anterior).")
        if cs: L.append(f"2. **Consiga os blueprints dos componentes:** {', '.join(cs)}.")
        L.append(f"3. **Forje cada componente** na Foundry (tabela abaixo).")
        L.append(f"4. **Forje a Warframe:** {n(bp.get('Credits',0))} créditos + {', '.join(cs)}" + (f" + {resource_line(prow)}" if resource_line(prow) else '') + f". Tempo: **{tempo(bp.get('Time'))}**" + (f" (pular: {bp['Rush']} platina)" if bp.get('Rush') else '') + '.')
        L.append(''); L.append('| Componente | Créditos | Recursos | Tempo |'); L.append('|---|---|---|---|')
        for c in cs:
            cb=comp_bp(name,c)
            if cb: L.append(f"| {c} | {n(cb.get('Credits',0))} | {resource_line(parts_table(cb,name)) or '—'} | {tempo(cb.get('Time'))} |")
            else: L.append(f"| {c} | — | ⚠️ sem dado no módulo | — |")
        L.append(f"| **{name}** (montagem) | {n(bp.get('Credits',0))} | {', '.join(cs)}{(' + '+resource_line(prow)) if resource_line(prow) else ''} | {tempo(bp.get('Time'))} |")
        L.append('')
    # stats
    L.append(f'## 📊 Stats Base — {name}'); L.append('')
    L.append('| Atributo | Valor |'); L.append('|---|---|')
    for k,lab in [('Health','Vida'),('Shield','Escudo'),('Armor','Armadura'),('Energy','Energia'),('InitialEnergy','Energia inicial'),('Sprint','Velocidade de corrida')]:
        if w.get(k) is not None: L.append(f"| {lab} | {n(w[k]) if not isinstance(w[k],float) else str(w[k]).replace('.',',')} |")
    if w.get('AuraPolarity'): L.append(f"| Polaridade de Aura | {w['AuraPolarity']} |")
    if w.get('Polarities'): L.append(f"| Polaridades | {', '.join(w['Polarities'])} |")
    if w.get('Progenitor'): L.append(f"| Elemento progenitor (Kuva Lich) | {w['Progenitor']} |")
    if w.get('Sex'): L.append(f"| Gênero | {'Feminino' if w['Sex']=='Female' else 'Masculino' if w['Sex']=='Male' else w['Sex']} |")
    if w.get('Introduced'): L.append(f"| Introduzida | Update {w['Introduced']} |")
    L.append('')
    # habilidades
    abl=w.get('Abilities') or []
    if abl:
        L.append(f'## 🔮 Habilidades — {name}'); L.append('')
        if w.get('Passive'): L.append(f"**Passiva (inglês):** {w['Passive']}"); L.append('')
        L.append('| # | Habilidade | Energia | Descrição (inglês) |'); L.append('|---|---|---|---|')
        for i,a in enumerate(abl,1):
            d=data.AB.get(a,{})
            L.append(f"| {i} | **{a}** | {d.get('Cost','—')} | {(d.get('Description') or '').replace('|','/').replace(chr(10),' ')} |")
        L.append('')
        if w.get('Subsumed'): L.append(f"**Helminth:** a habilidade **{w['Subsumed']}** pode ser subsumida (doada ao Helminth)."); L.append('')
        if w.get('AugmentShop'): L.append(f"**Augments** vendidos por: {', '.join(link(x,False) for x in w['AugmentShop'])}."); L.append('')
    # relacionados
    rel=[]
    for other in ([base] if (prime or umbra) else [f'{name} Prime']):
        p=data.TITLE.get(other.lower())
        if p and p!=path: rel.append(f"- [[{p}|{other}]]")
    rel.append('- [[mecanicas/forja.md|Forja]] — como funciona a Foundry')
    if prime: rel.append('- [[mecanicas/trading.md|Trading]] — peças Prime são negociáveis')
    L.append(f'## 🔗 Relacionados — {name}'); L.append(''); L += rel; L.append('')
    return '\n'.join(re.sub(r'(\[\[[^\]]*?)\\\|',r'\1|',l) if not l.lstrip().startswith('|') else l for l in L)
if __name__=='__main__':
    print(gen_warframe(sys.argv[1],'x'))

def _fixpipes(): pass
