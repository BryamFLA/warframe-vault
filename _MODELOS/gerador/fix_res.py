import lua,os,re,sys
V=os.path.expanduser('~/mnt/warframe-vault')
_s=open(os.path.expanduser('~/resources.lua'),encoding='utf-8').read(); _m=re.search(r'^local ResourceData = \{',_s,re.M); R=lua.parse_table_at(_s,_m.end()-1)
PL={'Earth':'Terra','Mars':'Marte','Mercury':'Mercúrio','Venus':'Vênus','Jupiter':'Júpiter','Saturn':'Saturno','Uranus':'Urano','Neptune':'Netuno','Pluto':'Plutão','Moon':'Lua','the Void':'Void','Void':'Void','and':'e','Missions in':'missões em','missions':'missões','Excavation':'Excavation','Kuva Fortress':'Kuva Fortress'}
PT={'Ferrite':'Ferrita','Alloy Plate':'Placa de Liga','Polymer Bundle':'Pacote de Polímeros','Circuits':'Circuitos','Salvage':'Sucata','Nano Spores':'Nanoesporos','Morphics':'Mórficos','Neural Sensors':'Sensores Neurais','Orokin Cell':'Célula Orokin','Control Module':'Módulo de Controle','Gallium':'Gálio','Neurodes':'Neurodos','Argon Crystal':'Cristal de Argônio','Tellurium':'Telúrio','Plastids':'Plastídios','Oxium':'Óxio','Detonite Ampule':'Ampola de Detonite','Fieldron Sample':'Amostra de Fieldron','Mutagen Sample':'Amostra de Mutágeno','Nitain Extract':'Extrato de Nitain','Kuva':'Kuva','Forma':'Forma','Endo':'Endo'}
def loc_pt(s):
    for k,v in PL.items(): s=re.sub(r'\b'+re.escape(k)+r'\b',v,s)
    return s
changed=0; nolocs=[]
for dp,dn,fn in os.walk(os.path.join(V,'recursos')):
    for f in fn:
        if not f.endswith('.md') or f.startswith('_'): continue
        p=os.path.join(dp,f); t=open(p,encoding='utf-8').read()
        if re.search(r'^rag:\s*false',t,re.M): continue
        title=re.search(r'^title:\s*"?(.*?)"?\s*$',t,re.M).group(1)
        r=R.get(title)
        if not isinstance(r,dict): nolocs.append(title); continue
        desc=r.get('Description','') or ''
        m=re.search(r'Locations?:\s*(.+)$',desc.replace('\r',''),re.S)
        loc=loc_pt(m.group(1).strip().rstrip('.')) if m else None
        rar={'Common':'comum','Uncommon':'incomum','Rare':'raro'}.get(r.get('Rarity',''),'')
        head=re.search(r'^## 🌍 Onde Conseguir — .*$',t,re.M)
        if not head or not loc: nolocs.append(title); continue
        if '**Como conseguir ' in t[head.end():head.end()+400]: continue
        ptn=PT.get(title)
        lead=f"\n\n**Como conseguir {title}{' ('+ptn+')' if ptn and ptn!=title else ''}:** recurso {rar+' ' if rar else ''}que aparece em **{loc}**."
        if re.search(r'\b(Terra|Marte|Mercúrio|Vênus|Júpiter|Saturno|Urano|Netuno|Plutão|Lua|Eris|Sedna|Ceres|Europa|Phobos|Void|Deimos)\b',loc) and 'Excavation' not in loc:
            lead+=" Recursos de planeta caem de **inimigos e containers em qualquer missão** desses planetas — missões **endless** (Survival, Defense, Excavation) e Dark Sectors rendem mais; leve **Resource Booster** e um pet com Vacuum/Fetch."
        t=t[:head.end()]+lead+t[head.end():]
        if ptn and ptn not in t.split('---')[1]:
            t=re.sub(r'^aliases: \[(.*?)\]',lambda mm:'aliases: ['+mm.group(1)+', '+ptn+']',t,1,flags=re.M)
        # remove frase automatica enganosa de "melhor rota" baseada em maior chance de bounty/conclave
        t=re.sub(r'^\*\*Melhor rota:\*\* a fonte de maior chance na tabela acima é \*\*[^*]*(Bounty|Conclave)[^\n]*\n','',t,flags=re.M)
        open(p,'w',encoding='utf-8').write(t); changed+=1
print('alterados',changed,'sem local',len(nolocs)); print(nolocs[:60])
