from build import *
import lua
C=lua.load_module(os.path.expanduser('~/companions.lua'))['Companions']
KAV="Kavats nascem da **Incubadora** do Orbiter: (1) conclua a quest **Howl of the Kubrow** para liberar a Incubadora; (2) instale o **Kavat Incubator Upgrade Segment** — pesquisa no **Tenno Lab** do Dojo, drop dos **Hyekka Masters** ou 175 platina no Mercado; (3) junte **10 Kavat Genetic Codes** escaneando **Feral Kavats** no tileset Orokin Derelict (Deimos) com Codex/Synthesis Scanner; (4) forje um **Incubator Power Core** (blueprint no Mercado). A raça sai por sorteio na incubação aleatória, ou é escolhida usando **Genetic Code Templates** (imprints) de um Kavat dessa raça."
KUB="Kubrows nascem da **Incubadora** do Orbiter: (1) conclua a quest **Howl of the Kubrow**; (2) consiga um **Kubrow Egg** nas **tocas de Kubrow (Kubrow Dens)** do tileset Grineer Forest, na **Terra**; (3) forje um **Incubator Power Core** (blueprint no Mercado). A raça sai por sorteio na incubação aleatória, ou é escolhida aplicando dois **Genetic Code Templates** (Mercado) de um Kubrow dessa raça."
REV="Obtido por **Revivificação** com o **Son** no **Necralisk (Deimos)**: capture um **Weakened {n}** com as ferramentas de **Conservação** no Cambion Drift (depois que ele for atacado por Infested), compre **Mutagen** e **Antigen** do Son com Standing **Entrati** e pague **5.000 créditos**. Recém-revivido, não pode ser renomeado, customizado, polarizado nem dar Mastery até ser **gilded** (rank 30)."
SENT2=" Exige **2 slots de companheiro** livres (o Sentinel e a arma robótica que vem com ele)."
PRIME_S="As peças vêm de **Relíquias do Void** (ver tabela)."+SENT2
A={
'Smeeta Kavat':KAV+" A **Smeeta** é famosa pelo precept **Charm**, que pode dobrar recursos e afinidade — a Kavat preferida para farm.",
'Adarza Kavat':KAV+" A **Adarza** é a Kavat de crítico (precept Cat's Eye).",
'Vasca Kavat':"Primeiro prepare a Incubadora como para qualquer Kavat (quest **Howl of the Kubrow**, Kavat Incubator Upgrade Segment, 10 Kavat Genetic Codes de Deimos e Incubator Power Core). Depois, leve um Kavat seu às **Plains of Eidolon à noite** para ser **infectado por um Vasca selvagem** (atraia com o **Vasca Kavat Lure** e a **Pheromone Oota** do Master Teasonai, em Cetus). No Orbiter, use um **Genetic Code Template** no Kavat infectado para criar um **Vasca Imprint**; repita para ter **2 imprints** e incube.",
'Venari':"**Venari** é a Kavat pessoal da Warframe **[[warframes/regular/khora.md|Khora]]** — faz parte da **passiva** dela e não se obtém separadamente: vem junto ao forjar a Khora e só aparece quando a Khora está equipada.",
'Panzer Vulpaphyla':REV.format(n='Panzer Vulpaphyla')+" Aparece no ciclo **Fass**.",
'Crescent Vulpaphyla':REV.format(n='Crescent Vulpaphyla')+" Aparece no ciclo **Vome**.",
'Vizier Predasite':REV.format(n='Vizier Predasite'),
'Medjay Predasite':REV.format(n='Medjay Predasite')+" Aparece no ciclo **Vome**.",
'Pharaoh Predasite':REV.format(n='Pharaoh Predasite'),
'Sahasa Kubrow':KUB+" O **Sahasa** desenterra itens (precept **Dig**).",
'Raksa Kubrow':KUB,
'Sunika Kubrow':KUB,
'Huras Kubrow':KUB+" O **Huras** dá furtividade ao dono (precept **Stalk**).",
'Chesa Kubrow':KUB+" O **Chesa** recolhe itens e munição (precept **Retrieve**).",
'Helminth Charger':KUB.split(' A raça')[0]+" Diferente das outras raças, exige um **Helminth Cyst**: deixe o **Helminth** do Orbiter infectar sua Warframe (ou use a **Nidus**) até aparecer o cisto, e então use-o na incubação.",
'Shade':"Blueprint no **Mercado**."+SENT2+" O Shade dá **invisibilidade** ao dono quando um inimigo se aproxima (precept Ghost).",
'Wyrm':"Blueprint no **Mercado**."+SENT2,
'Dethcube':"Blueprint no **Mercado**."+SENT2,
'Carrier':"Blueprint no **Mercado**."+SENT2,
'Diriga':"Blueprint no **Mercado**."+SENT2,
'Taxon':"Blueprint ganho ao cumprir 3 de 4 objetivos da **Junção de Vênus** (na Terra); também no **Mercado** por 5.000 créditos."+SENT2,
'Oxylus':"Blueprint comprado do **The Business** (Fortuna) por **20.000 de Standing** no **Rank 5** do Solaris United."+SENT2,
'Djinn':"Pesquisado no **Bio Lab** do **Dojo do clã**."+SENT2,
'Helios':"Pesquisado no **Energy Lab** do **Dojo do clã**."+SENT2,
'Nautilus':"Blueprint e componentes nos **Points of Interest** e no **Arva Vector Defense** (rotações B/C) das missões de Railjack da **Neptune Proxima**. Peças negociáveis.",
'Wyrm Prime':"**Vaultado desde 17/05/2016** — Relíquias só no **Prime Resurgence** ou por troca."+SENT2,
'Dethcube Prime':"**Vaultado desde 08/09/2021** — Relíquias só no **Prime Resurgence** ou por troca."+SENT2,
'Shade Prime':PRIME_S,'Carrier Prime':PRIME_S,'Helios Prime':PRIME_S,'Nautilus Prime':PRIME_S,
}
HOUND="As peças de Hound (Model, Core, Bracket e Stabilizer) vêm de **derrotar (vanquish) Sisters of Parvos** — cada Sister traz um Hound — ou de troca com jogadores. Forje as peças na Foundry (algumas pedem **Spectral Debris**, dos Errant Specters no Granum Void) e monte o Hound com **Legs**, em **Fortuna**, por **4.000 créditos**. Exige 2 slots de companheiro."
MOA="Os blueprints das peças de MOA (Model, Core, Gyro e Bracket) são comprados de **Legs**, em **Fortuna**, com Standing do **Solaris United**. Forje as peças na Foundry (24 h cada) e monte o MOA com Legs por **4.000 créditos**."
for h,mdl in [('Bhaira Hound','Lacerten / Null Audit'),('Dorma Hound','Batoten / Repo Audit'),('Hec Hound','Akaten / Equilibrium Audit')]: A[h]=HOUND+f" O **Model {h.split()[0]}** é a cabeça do Hound e define a arma e o precept exclusivo ({mdl})."
for m in ['Lambeo Moa','Oloro Moa','Para Moa']: A[m]=MOA+f" O **Model {m.split()[0]}** é a cabeça do MOA e traz 2 precepts exclusivos."
TIPO={'Kavat':'Kavat','Kubrow':'Kubrow','Sentinel':'Sentinel','Hound':'Hound','MOA':'MOA','Moa':'MOA','Predasite':'Predasite (Infested)','Vulpaphyla':'Vulpaphyla (Infested)'}
def gen_comp(title,path,modname=None):
    nm=modname or title; c=C.get(nm)
    if nm not in A and nm in ACQ: A[nm]=ACQ[nm]
    if nm=='Prisma Shade': A[nm]='Vendido pelo **Baro Ki\'Teer** por 300.000 créditos e 500 Ducats (estoque varia), junto com a arma Prisma Burst Laser. Exige 2 slots de companheiro.'
    if not c or nm not in A: return None
    prime='Prime' in nm; ty=TIPO.get(c.get('Type',''),c.get('Type',''))
    acq=A[nm]; how=strip_md(acq.split('. ')[0]).rstrip('.')
    al=[nm]+([title] if title!=nm else [])+[f'companheiro {nm}']
    L=['---',f'title: {nm}','aliases: ['+', '.join(dict.fromkeys(al))+']','tipo: companheiro',f'subtipo: {ty.split()[0].lower()}',
       f'resumo: "{esc(nm+" — companheiro "+ty+". Como conseguir: "+how+".")}"','status: parcial','rag: true',f'tags: [companheiro, {ty.split()[0].lower()}]',
       f'fontes: ["https://wiki.warframe.com/w/{nm.replace(" ","_")}", "https://wiki.warframe.com/w/Module:Companions/data", "https://wiki.warframe.com/w/Module:Blueprints/data", "https://wiki.warframe.com/w/Module:Void/data"]',
       f'atualizado: {TODAY}','verificado: true','agente: opus','gerado_de: modulos-da-wiki','---','',f'# {nm}','','> [!info] Resumo',f'> Companheiro do tipo **{ty}**' + (f", introduzido em {c['Introduced']}" if c.get('Introduced') else '')+'.']
    if c.get('Description'): L.append(f"> *Descrição no jogo (inglês):* \"{c['Description']}\"")
    L+=['',f'## 🌍 Onde Conseguir — {nm}','',f'Como conseguir o companheiro {nm}:','',acq,'']
    bp=data.BP.get(nm)
    if prime:
        L+=['| Peça Prime | Relíquias ativas (raridade) | Ativas / vaultadas |','|---|---|---|']
        parts=[x['Name'].replace('Prime ','') for x in bp.get('Parts',[]) if x.get('Type')=='PrimePart'] if bp else ['Carapace','Cerebrum','Systems']
        for p in ['Blueprint']+parts:
            s,na,nv=relics(nm,p); L.append(f'| {p} | {s} | {na} / {nv} |')
        L.append('')
    if bp:
        L+=[f'## 🏗️ Como Construir — {nm}','',f"Forja: **{n(bp.get('Credits',0))} créditos** + "+', '.join(f"{n(p.get('Count',1))} {link(p['Name']) if p.get('Type')=='Resource' else p['Name']}" for p in bp.get('Parts',[]))+f". Tempo: **{tempo(bp.get('Time'))}**."+(f" Pronto no Mercado por **{bp['MarketCost']} platina**." if bp.get('MarketCost') else ''),'']
    L+=[f'## 📊 Stats Base — {nm}','','| Atributo | Valor |','|---|---|']
    for k,lab in [('Health','Vida'),('Shield','Escudo'),('Armor','Armadura'),('Energy','Energia')]:
        if c.get(k): L.append(f'| {lab} | {n(c[k])} |')
    if c.get('Polarities'): L.append(f"| Polaridades | {', '.join(c['Polarities'])} |")
    atk=(c.get('Attacks') or [{}])[0]
    if atk.get('Damage'): L.append(f"| Ataque ({atk.get('AttackName','')}) | "+', '.join(f"{DMG.get(k,k)} {v}" for k,v in atk['Damage'].items())+" |")
    L+=['',f'## 🔗 Relacionados — {nm}','','- [[mecanicas/forja.md|Forja]]','']
    return '\n'.join(L)
DMG={'Impact':'Impacto','Puncture':'Perfuração','Slash':'Corte','Heat':'Calor','Cold':'Frio','Electricity':'Eletricidade','Toxin':'Tóxico'}
