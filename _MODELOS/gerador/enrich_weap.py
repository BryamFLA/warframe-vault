import os,re,json,sys
sys.path.insert(0,os.path.expanduser('~/gen'))
import data
from sections import upsert, fm_set
from gen_weap import OVR
V=os.path.expanduser('~/mnt/warframe-vault')
CDX=json.load(open('codex_pt.json'))
def lk(n):
    p=data.TITLE.get(re.sub(r'\s*\(.*?\)$','',n).strip().lower())
    return f"[[{p}\\|{n}]]" if p else n
ELEM={'Tóxico':{'rifle':'Malignant Force','shotgun':'Toxic Barrage','pistol':'Pistol Pestilence','melee':'Virulent Scourge'},
      'Elétrico':{'rifle':'High Voltage','shotgun':'Shell Shock','pistol':'Jolt','melee':'Voltaic Strike'},
      'Calor':{'rifle':'Hellfire','shotgun':'Scattering Inferno','pistol':'Primed Heated Charge','melee':'Primed Fever Strike'},
      'Frio':{'rifle':'Cryo Rounds','shotgun':'Frigid Blast','pistol':'Deep Freeze','melee':'Vicious Frost'}}
def kind(w):
    s=w.get('Slot'); c=w.get('Class','')
    if s=='Melee': return 'melee'
    if s in ('Archgun','Archmelee'): return 'arch'
    if s=='Amp': return 'amp'
    if c in ('Shotgun','Shotgun Sidearm','Dual Shotguns') and s=='Primary': return 'shotgun'
    if s=='Secondary': return 'pistol'
    if c in ('Sniper Rifle',): return 'sniper'
    if c in ('Launcher',): return 'launcher'
    return 'rifle'
def arche(a):
    cc=a.get('CritChance') or 0; cm=a.get('CritMultiplier') or 0; sc=a.get('StatusChance') or 0
    c=cc>=0.24 and cm>=2.0; s=sc>=0.24
    return 'híbrida' if c and s else 'crítico' if c else 'status' if s else 'dano bruto (baseline)', cc,cm,sc
def build(w):
    k=kind(w); a=(w.get('Attacks') or [{}])[0]; ar,cc,cm,sc=arche(a)
    if k=='amp': return None
    if k=='melee':
        mods=['Primed Pressure Point','Primed Reach']
        if ar in ('crítico','híbrida'): mods+=['Blood Rush','Organ Shatter','Gladiator Might','Berserker Fury']
        else: mods+=['Condition Overload','Weeping Wounds','Primed Fury','Berserker Fury']
        el=['Virulent Scourge','Primed Fever Strike'] if ar!='crítico' else ['Primed Fever Strike','Vicious Frost']
        mods+=el; exi='Melee Elementalist? não — use Focused Defense? (exilus melee): Primed Fury'
        arc=['Melee Influence','Melee Duplicate'] if ar!='crítico' else ['Melee Exposure','Melee Influence']
        exi='—'
        return k,ar,cc,cm,sc,mods,arc,exi
    if k=='arch':
        mods=['Rubedo-Lined Barrel','Dual Rounds','Parallax Scope','Critical Focus','Magazine Extension','Ammo Chain','Charged Bullets','Combustion Rounds']
        return k,ar,cc,cm,sc,mods,[],'—'
    base={'rifle':'Serration','sniper':'Serration','launcher':'Serration','shotgun':'Primed Point Blank','pistol':'Hornet Strike'}[k]
    ms={'rifle':'Galvanized Chamber','sniper':'Galvanized Chamber','launcher':'Galvanized Chamber','shotgun':'Galvanized Hell','pistol':'Galvanized Diffusion'}[k]
    if ar in ('crítico','híbrida'):
        crit={'rifle':['Point Strike','Vital Sense'],'sniper':['Point Strike','Vital Sense'],'launcher':['Point Strike','Vital Sense'],'shotgun':['Primed Ravage','Blunderbuss'],'pistol':['Primed Pistol Gambit','Primed Target Cracker']}[k]
    else:
        crit={'rifle':['Galvanized Aptitude','Hammer Shot'],'sniper':['Galvanized Aptitude','Hammer Shot'],'launcher':['Galvanized Aptitude','Hammer Shot'],'shotgun':['Galvanized Savvy','Shotgun Savvy'],'pistol':['Galvanized Shot','Sure Shot']}[k]
    kk='rifle' if k in ('rifle','sniper','launcher') else k
    el=[ELEM['Tóxico'][kk],ELEM['Elétrico'][kk]] if ar=='status' else [ELEM['Tóxico'][kk],ELEM['Frio'][kk]]
    extra={'rifle':['Hammer Shot','Primed Shred'],'sniper':['Hammer Shot','Primed Shred'],'launcher':['Firestorm','Hammer Shot'],'shotgun':['Shotgun Barrage','Seeking Fury'],'pistol':['Lethal Torrent','Augur Pact']}[k]
    extra=[e for e in extra if e not in crit]
    mods=[base,ms+' (ou a versão comum)']+crit+el+extra
    arc={'rifle':['Primary Merciless','Primary Deadhead'],'sniper':['Primary Deadhead','Primary Merciless'],'launcher':['Primary Merciless','Primary Dexterity'],'shotgun':['Primary Merciless','Primary Deadhead'],'pistol':['Secondary Encumber','Secondary Merciless']}[k]
    exi='Vigilante Armaments' if k!='pistol' else 'Hollowed Bullets'
    return k,ar,cc,cm,sc,mods,arc,exi
FACT={'Tenno':'Tenno','Grineer':'Grineer','Corpus':'Corpus','Infested':'Infested','Sentient':'Sentient','Orokin':'Orokin','Prime':'Orokin (versão Prime)','Kuva Lich':'Kuva — criada pelos Kuva Liches','Tenet':'Tenet — das Sisters of Parvos (Corpus)','Technocyte Coda':'Coda — infectada pelo vírus Technocyte (Höllvania, 1999)','Scaldra':'Scaldra (Höllvania, 1999)','Entrati':'Entrati (Deimos)','Zariman':'Zariman (Void)','Duviri':'Duviri','Syndicate':'Sindicato','Wraith':'variante Wraith (de evento/Invasão)','Vandal':'variante Vandal (Tenno customizada)','Prisma':'variante Prisma (Baro Ki\'Teer)','Stalker':'arma do Stalker','Dax':'Dax (Antiga Guerra)'}
cnt=0
for dp,dn,fn in os.walk(os.path.join(V,'armas')):
    for f in fn:
        if not f.endswith('.md') or f.startswith('_'): continue
        p=os.path.join(dp,f); t=open(p,encoding='utf-8').read(); o=t
        title=re.search(r'^title:\s*"?(.*?)"?\s*$',t,re.M).group(1)
        w=data.WEAP.get(OVR.get(title,title.replace(' e ',' & '))) or data.WEAP.get(title)
        if not w: continue
        bt=build(w)
        if bt and (not re.search(r'^## .*Build',t,re.M) or 'Build de referência gerada' in t):
            k,ar,cc,cm,sc,mods,arc,exi=bt
            cmtxt=(str(cm)[:-2] if str(cm).endswith('.0') else str(cm)).replace('.',',')
            mods=[m for m in mods if '?' not in m]
            L=[f"## 🛠️ Build — {title}",'',f"Build de referência gerada pelas estatísticas da arma (perfil **{ar}**: crítico {round(cc*100)}% ×{cmtxt}, status {round(sc*100)}%). Ajuste ao seu conteúdo e aos mods que você tem.",'','| # | Mod |','|---|---|']
            for i,m in enumerate(mods[:8],1): L.append(f"| {i} | {lk(m)} |")
            if exi and exi!='—': L.append(f"| Exilus | {lk(exi)} |")
            L.append('')
            if k!='arch' and k!='melee': L.append("**Elementos:** Viral (Frio + Tóxico) + Calor para conteúdo geral e Steel Path; Corrosivo (Elétrico + Tóxico) contra armadura (Grineer); Magnético ou Tóxico contra escudos (Corpus).")
            if k=='melee': L.append("**Elementos:** Viral + Calor (geral) ou Corrosivo (armadura). Builds de status usam Condition Overload; builds de crítico usam Blood Rush + combo alto.")
            if arc: L.append(f"**Arcanes:** {', '.join(arc)}.")
            if w.get('IncarnonImage'): L.append("**Incarnon:** esta arma tem forma Incarnon (Genesis instalado com o Cavalero ou inata). Ative a forma Incarnon com headshots/acertos e escolha as Evoluções focando o perfil dela.")
            d=w.get('Disposition')
            if d: L.append(f"**Riven:** disposição {d} — " + ('ótima base para Riven.' if d>=1.3 else 'Riven ajuda pouco.' if d<0.8 else 'Riven ajuda moderadamente.'))
            L.append("\n**Sem mods Primed/Galvanized:** troque Primed Point Blank → Point Blank, Galvanized Chamber → Split Chamber, Primed Shred → Shred, Primed Pressure Point → Pressure Point, Primed Reach → Reach.")
            t=upsert(t,'## 🛠️ Build','\n'.join(L))
        if not re.search(r'^## .*Hist',t,re.M):
            tr=[FACT[x] for x in (w.get('Traits') or []) if x in FACT]
            L=[f"## 📖 História e Origem — {title}",'']
            cx=CDX.get(title,'')
            if cx: L.append(f"*Codex:* \"{cx}\"\n")
            if tr: L.append(f"**Origem / facção:** {', '.join(dict.fromkeys(tr))}.")
            if w.get('Introduced'): L.append(f"**Introduzida:** Update {w['Introduced']}.")
            if 'Vaulted' in (w.get('Traits') or []): L.append("**Status:** Prime **vaultada** — as Relíquias não caem mais (só Prime Resurgence ou troca).")
            if 'Never Vaulted' in (w.get('Traits') or []): L.append("**Status:** Prime que **nunca é vaultada**.")
            if len(L)>2: t=upsert(t,'## 📖 História','\n'.join(L))
        if t!=o: open(p,'w',encoding='utf-8').write(t); cnt+=1
print('armas atualizadas',cnt)
