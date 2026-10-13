import lua,re,os,json,collections
H=os.path.expanduser('~')
def L(f): return lua.load_module(os.path.join(H,f))
BP={}; _b=L('blueprints.lua')
for sec in ('Blueprints','Suits'): BP.update(_b[sec])
BP_BY_RESULT={v.get('Result',k):v for k,v in BP.items() if isinstance(v,dict)}
WF=L('warframes.lua')['Warframes']
AB=L('ability.lua')['Ability']
WEAP={}
for s in ['primary','secondary','melee','archwing','modular','misc','companion']:
    try: WEAP.update(L(f'w_{s}.lua'))
    except Exception as e: print('weap',s,e)
DT=L('droptables.lua')
MISS=L('missions.lua')['MissionDetails']
RES=L('research.lua')['Research']
_s=open(os.path.join(H,'void.lua'),encoding='utf-8').read(); _m=re.search(r'^RelicData = \{',_s,re.M)
RELICS=lua.parse_table_at(_s,_m.end()-1)
# alias -> nodes
ALIAS_NODES=collections.defaultdict(list)
for n in MISS:
    a=n.get('DropTableAlias')
    if a: ALIAS_NODES[a].append(f"{n['Name']}, {n.get('Planet','')}".strip(', '))
PT_PLANET={'Earth':'Terra','Mars':'Marte','Mercury':'Mercúrio','Venus':'Vênus','Jupiter':'Júpiter','Saturn':'Saturno','Uranus':'Urano','Neptune':'Netuno','Pluto':'Plutão','Moon':'Lua','Lua':'Lua'}
def ptp(s):
    for k,v in PT_PLANET.items(): s=re.sub(r'\b'+k+r'\b',v,s)
    return s
DROPS=collections.defaultdict(list)  # item -> [(label, chance float, note)]
for key,tb in DT['Missions'].items():
    if not isinstance(tb,dict) or tb.get('_IgnoreEntry'): continue
    name=tb.get('Name',key); rw=tb.get('Rewards',{})
    nodes=ALIAS_NODES.get(key,[])
    label=name if not nodes else f"{name} ({'; '.join(ptp(x) for x in nodes[:3])}{'…' if len(nodes)>3 else ''})"
    rots=rw.items() if isinstance(rw,dict) else [('',rw)]
    for rot,items in rots:
        if not isinstance(items,list): continue
        for it in items:
            if isinstance(it,list) and len(it)>=3:
                DROPS[it[0]].append((label+(f' — rot. {rot}' if rot else ''),float(it[2]),'missao'))
for key,e in DT['Enemies'].items():
    if not isinstance(e,dict) or e.get('_IgnoreEntry'): continue
    for pool,chk in [('Blueprints','BlueprintChance'),('Mods','ModChance'),('Items','ItemChance'),('Resources','ResourceChance'),('Relics','RelicChance')]:
        for it in e.get(pool,[]) or []:
            if isinstance(it,list) and len(it)>=3:
                pc=float(e.get(chk,100)); DROPS[it[0]].append((f"{e.get('Name',key)} (inimigo)",pc*float(it[2])/100,'inimigo'))
RELIC_IDX=collections.defaultdict(list) # (item,part) -> [(relic,rarity,vaulted)]
for rn,r in RELICS.items():
    if not isinstance(r,dict): continue
    for d in r.get('Drops',[]):
        RELIC_IDX[(d['Item'],d['Part'])].append((rn,d['Rarity'],bool(r.get('Vaulted'))))
# vault titles
VAULT=os.path.join(H,'mnt','warframe-vault')
TITLE={}
for dp,dn,fn in os.walk(VAULT):
    if '/.' in dp or '_MODELOS' in dp: continue
    for f in fn:
        if f.endswith('.md') and not f.startswith('_'):
            p=os.path.join(dp,f); t=open(p,encoding='utf-8').read(2000)
            m=re.search(r'^title:\s*"?(.*?)"?\s*$',t,re.M)
            if m: TITLE.setdefault(m.group(1).lower(),os.path.relpath(p,VAULT))
