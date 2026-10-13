import os,re,json,sys,collections,lua
sys.path.insert(0,os.path.expanduser('~/gen'))
from build import *
M=lua.load_module(os.path.expanduser('~/mods.lua')); M=M.get('Mods',M)
A=lua.load_module(os.path.expanduser('~/arcane.lua'))['Arcanes']
TERMS=[('Critical Damage','Dano Crítico'),('Critical Chance','Chance Crítica'),('Status Chance','Chance de Status'),('Status Duration','Duração de Status'),('Fire Rate','Cadência'),('Attack Speed','Velocidade de Ataque'),('Reload Speed','Velocidade de Recarga'),('Magazine Capacity','Capacidade do Pente'),('Ammo Maximum','Munição Máxima'),('Ammo Max','Munição Máxima'),('Ability Strength','Força de Habilidade'),('Ability Duration','Duração de Habilidade'),('Ability Range','Alcance de Habilidade'),('Ability Efficiency','Eficiência de Habilidade'),('Shield Capacity','Capacidade de Escudo'),('Shield Recharge','Recarga de Escudo'),('Energy Max','Energia Máxima'),('Sprint Speed','Velocidade de Corrida'),('Parkour Velocity','Velocidade de Parkour'),('Combo Duration','Duração do Combo'),('Heavy Attack Efficiency','Eficiência de Heavy Attack'),('Weak Point','Ponto Fraco'),('Damage to','Dano contra'),('Melee Damage','Dano Melee'),('Damage','Dano'),('Health Regen','Regeneração de Vida'),('Health','Vida'),('Armor','Armadura'),('Heat','Calor'),('Cold','Frio'),('Electricity','Eletricidade'),('Toxin','Tóxico'),('Impact','Impacto'),('Puncture','Perfuração'),('Slash','Corte'),('Recoil','Recuo'),('Accuracy','Precisão'),('Range','Alcance'),('On Kill:','Ao matar:'),('On Headshot:','Ao acertar headshot:'),('On Critical Hit:','Ao acertar crítico:'),('On Damaged:','Ao levar dano:'),('On Energy Pickup:','Ao pegar energia:'),('On Health Pickup:','Ao pegar vida:'),('On Ability Cast:','Ao usar habilidade:'),('On Reload:','Ao recarregar:'),('chance for','de chance de'),(' and ',' e '),('Enemies','Inimigos'),('enemies','inimigos'),('Energy','Energia'),('Holster Speed','Velocidade de troca de arma'),('Zoom','Zoom'),('Corpus','Corpus'),('Grineer','Grineer'),('Infested','Infested')]
def tr(desc):
    s=desc.replace('\r','')
    for a,b in TERMS: s=re.sub(r'(?<![A-Za-z])'+re.escape(a)+r'(?![A-Za-z])',b,s)
    s=re.sub(r'for (\d+(?:\.\d+)?)s',r'por \1 s',s); s=re.sub(r'Stacks up to (\d+)x',r'Acumula até \1x',s); s=re.sub(r'Max (\d+) stacks',r'Máx. \1 acúmulos',s)
    eng=len(re.findall(r'\b(the|of|to|with|when|while|that|your|from|each|after|this|will|are|is|on|by|for|per|increases?|reduces?|grants?|gains?|deals?|has|allies|ability|abilities|kills?|hit|hits|cast|damaged|nearby|weapon|instead|into)\b',s,re.I))
    return s.replace('\n',' · '), eng
RAR={'Common':'comum','Uncommon':'incomum','Rare':'raro','Legendary':'lendário','Peculiar':'peculiar','Riven':'riven','Amalgam':'amalgam','Requiem':'requiem'}
def mdir(ty,is_aug):
    w={'Warframe','Aura'}
    if ty in w or is_aug: return 'mods/warframe'
    if ty in ('Rifle','Pistol','Shotgun','Melee','Assault Rifle','Sniper','Bow','Primary','Claws','Thrown Melee','Tome','Secondary','Launcher','Speargun','Crossbow','Dual Pistols','Glaive','Nikana','Heavy Blade','Polearm','Rapier','Scythe','Staff','Sword','Hammer','Whip'): return 'mods/armas'
    if ty in ('Companion','Beast','Hound','Robotic','MOA','Sentinel','Kavat','Kubrow','Vulpaphyla','Predasite'): return 'mods/companheiros'
    if ty in ('Parazon','Archgun','Archmelee','Archwing','Necramech','Plexus','K-Drive','Antique','Mod','Posture','Stance'): return 'mods/especiais'
    if ty in data.WF: return 'mods/warframe'
    return 'mods/armas'
AUGSHOP={}
for k,w in data.WF.items():
    if isinstance(w,dict) and w.get('AugmentShop'): AUGSHOP[k]=w['AugmentShop']
def source_notes(name,m,is_arc=False):
    N=[]
    if name.startswith('Primed '): N.append("Mods **Primed** são vendidos pelo **Baro Ki'Teer** (por Ducats + créditos) quando aparecem no estoque dele.")
    if name.startswith('Galvanized '): N.append("Mods **Galvanized** são comprados com **Vitus Essence** no vendedor de **Arbitration Honors** (qualquer Relay).")
    if name.startswith('Archon '): N.append("Mods **Archon** vêm das **Archon Hunts** semanais.")
    if name.startswith('Umbral '): N.append("Mods **Umbral** vêm da quest **The Sacrifice** e do **Elite Sanctuary Onslaught** (Cephalon Simaris).")
    if m.get('IsAbilityAugment'):
        fr=m.get('Type'); shops=AUGSHOP.get(fr) or AUGSHOP.get(fr+' Prime')
        if shops: N.append(f"**Augment** de {fr}: vendido pelos sindicatos {', '.join(shops)} (exige rank e Standing).")
    return N
def gen_mod(name,m,arc=False):
    ty=m.get('Type','?'); rar=RAR.get(m.get('Rarity',''),m.get('Rarity','')); desc=m.get('Description','')
    pt,eng=tr(desc)
    ds,more=drops(name,8)
    resumo=f"{name} — {'arcane' if arc else 'mod'} de {ty}" + (f" ({rar})" if rar else '') + f". Efeito no rank máximo: {(pt if eng==0 else desc.replace(chr(10),' · ')).rstrip('.')}."
    L=['---',f'title: {name}',f'aliases: [{name}]',f"tipo: {'arcane' if arc else 'mod'}",f'subtipo: {ty.lower()}']
    if rar: L.append(f'raridade: {rar}')
    if m.get('Polarity'): L.append(f"polaridade: {m['Polarity']}")
    L+=[f'resumo: "{esc(resumo)}"','status: parcial','rag: true',f"tags: [{'arcane' if arc else 'mod'}, {re.sub(r'[^a-z0-9]+','-',ty.lower())}]",
        f'fontes: ["https://wiki.warframe.com/w/{name.replace(" ","_")}", "https://wiki.warframe.com/w/Module:{"Arcane" if arc else "Mods"}/data", "https://wiki.warframe.com/w/Module:DropTables/data"]',
        f'atualizado: {TODAY}','verificado: true','agente: opus','gerado_de: modulos-da-wiki','---','',f'# {name}','','> [!info] Resumo',f"> {'Arcane' if arc else 'Mod'} de **{ty}**" + (f", raridade **{rar}**" if rar else '') + '.',
        f"> **Efeito (rank máximo):** {pt}" if eng==0 else f"> **Efeito (rank máximo, texto do jogo):** {desc.replace(chr(10),' · ')}",'',f'## 📊 Ficha — {name}','','| Item | Valor |','|---|---|',f'| Tipo | {ty} |']
    if rar: L.append(f'| Raridade | {rar} |')
    if m.get('Polarity'): L.append(f"| Polaridade | {m['Polarity']} |")
    if m.get('BaseDrain') is not None: L.append(f"| Drenagem base | {m['BaseDrain']} (sobe 1 por rank) |")
    if m.get('MaxRank') is not None: L.append(f"| Rank máximo | {m['MaxRank']} |")
    if m.get('Set'): L.append(f"| Set | {m['Set']} |")
    if m.get('IsExilus'): L.append('| Exilus | Sim (vai no slot Exilus) |')
    if m.get('IsAbilityAugment'): L.append('| Augment | Sim — modifica uma habilidade |')
    if 'Tradable' in m: L.append(f"| Negociável | {'Sim' if m['Tradable'] else 'Não'} |")
    if m.get('Incompatible'): L.append(f"| Incompatível com | {', '.join(m['Incompatible'][:6])} |")
    if m.get('Introduced'): L.append(f"| Introduzido | Update {m['Introduced']} |")
    L+=['',f'## 🌍 Onde Conseguir — {name}','',f'Como conseguir {name}:','']
    for x in source_notes(name,m,arc): L.append('- '+x)
    if ds:
        L+=['','| Fonte | Chance |','|---|---|']+[f'| {a} | {pct(b)} |' for a,b in ds]
        if more: L.append(f'\n> Mais {more} fontes: https://wiki.warframe.com/w/{name.replace(" ","_")}')
    if not ds and not source_notes(name,m,arc): L.append(f"Fonte não listada nas tabelas de drop do módulo da wiki (vendedor, evento ou quest). Ver https://wiki.warframe.com/w/{name.replace(' ','_')}.")
    L+=['',f'## 🛠️ Uso — {name}','']
    if arc: L.append("Arcanes são instalados num slot de Arcane (Warframe tem 2; armas e Amps têm 1) e sobem de rank combinando cópias. Muitos são negociáveis e alguns podem ser dissolvidos em Vosfor (Loid, Sanctum Anatomica).")
    else: L.append(f"Mod de **{ty}**: equipe no slot correspondente; a drenagem diminui pela metade com a polaridade igual ({m.get('Polarity','—')}). Upe com **Endo** e **créditos**.")
    return '\n'.join(L)+'\n'
def slug(s):
    import unicodedata
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','_',s.replace('&','e')).strip('_')
