import os,re,json,sys
sys.path.insert(0,os.path.expanduser('~/gen'))
import data
from sections import upsert
V=os.path.expanduser('~/mnt/warframe-vault')
CDX=json.load(open('codex_pt.json'))
def lk(n):
    p=data.TITLE.get(n.lower()); return f"[[{p}\\|{n}]]" if p else n
BUILD={'sentinel':(['Primed Regen','Link Shields? não'],"Sentinels morrem rápido: priorize sobrevivência (Primed Regen para reviver, mods de escudo/vida e armadura) e os precepts próprios. A arma robótica usa mods de rifle/shotgun comuns."),
'kavat':(['Link Health','Link Armor','Link Shields','Bite','Maul','Primed Animal Instinct','Medi-Pet Kit','Hunter Synergy'],"Kavats e Predasites/Vulpaphylas são feras: os mods Link copiam sua vida/armadura/escudo, Bite e Maul aumentam crítico e dano das garras."),
'kubrow':(['Link Health','Link Armor','Link Shields','Bite','Maul','Primed Animal Instinct','Medi-Pet Kit','Hunter Synergy'],"Kubrows tankam bem: Link Health/Armor copiam sua sobrevivência; use os precepts da raça (Dig, Retrieve, Stalk, etc.)."),
'moa':(['Link Health','Link Armor','Link Shields','Primed Animal Instinct','Mecha Empowered','Mecha Overdrive'],"MOAs usam mods de companheiro robótico; Mecha Empowered e Overdrive fazem parte do set Mecha (marcar inimigos/espalhar status)."),
'hound':(['Link Health','Link Armor','Link Shields','Primed Animal Instinct','Mecha Empowered','Mecha Overdrive'],"Hounds são companheiros robóticos montados com peças das Sisters of Parvos; o Model define a arma e o precept exclusivo.")}
cnt=0
for dp,dn,fn in os.walk(os.path.join(V,'companheiros')):
    for f in fn:
        if not f.endswith('.md') or f.startswith('_'): continue
        p=os.path.join(dp,f); t=open(p,encoding='utf-8').read(); o=t
        if 'status: stub' in t: continue
        title=re.search(r'^title:\s*"?(.*?)"?\s*$',t,re.M).group(1)
        sub=os.path.basename(dp)
        if sub in BUILD and not re.search(r'^## .*Build',t,re.M):
            mods,d=BUILD[sub]; mods=[m for m in mods if '?' not in m]
            if sub=='sentinel': mods=['Primed Regen','Guardian','Sacrifice','Link Shields','Link Armor','Primed Animal Instinct']
            L=[f"## 🛠️ Build — {title}",'',d,'','| # | Mod |','|---|---|']+[f"| {i} | {lk(m)} |" for i,m in enumerate(mods,1)]
            L.append('\n> Build de referência (curadoria do agente). Os precepts exclusivos do companheiro vêm equipados de fábrica — mantenha-os.')
            t=upsert(t,'## 🛠️ Build','\n'.join(L))
        if not re.search(r'^## .*Hist',t,re.M):
            cx=CDX.get(title,'')
            if cx: t=upsert(t,'## 📖 História',f"## 📖 História — {title}\n\n*Codex:* \"{cx}\"")
        if t!=o: open(p,'w',encoding='utf-8').write(t); cnt+=1
print('companheiros',cnt)
