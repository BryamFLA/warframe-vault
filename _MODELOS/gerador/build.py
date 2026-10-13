import data,json,re,os,collections,sys
ACQ=json.load(open(os.path.expanduser('~/gen/acq_pt.json')))
TODAY='2026-10-13'
def n(x):
    if isinstance(x,float) and not x.is_integer(): return f"{x:,.2f}".replace(',','X').replace('.',',').replace('X','.')
    return f"{int(x):,}".replace(',','.')
def pct(x): return (f"{x:.2f}".rstrip('0').rstrip('.')).replace('.',',')+'%'
def tempo(s):
    if not s: return '—'
    h=s/3600
    return f"{int(h/24)} dia(s)" if h>=24 and h%24==0 else (f"{h:g} h".replace('.',','))
def link(name,table=True):
    p=data.TITLE.get(name.lower())
    if p: return f"[[{p}\\|{name}]]" if table else f"[[{p}|{name}]]"
    return name
def drops(item,k=6):
    raw=data.DROPS.get(item,[])
    g=collections.OrderedDict()
    for lab,ch,kind in sorted(raw,key=lambda x:-x[1]):
        base,_,rot=lab.partition(' — rot. ')
        key=(base,round(ch,2))
        g.setdefault(key,[]); 
        if rot: g[key].append(rot)
    out=[]
    for (base,ch),rots in g.items():
        out.append((base+(f" — rot. {'/'.join(sorted(set(rots)))}" if rots else ''),ch))
    return out[:k],max(0,len(g)-k)
def relics(item,part):
    r=data.RELIC_IDX.get((item,part),[])
    act=[x for x in r if not x[2]]; vau=[x for x in r if x[2]]
    RAR={'Common':'Comum','Uncommon':'Incomum','Rare':'Rara'}
    s=', '.join(f"{a} ({RAR.get(b,b)})" for a,b,_ in act[:8]) or '—'
    return s,len(act),len(vau)
def parts_table(bp,owner):
    rows=[]
    for p in bp.get('Parts',[]):
        nm=p['Name']; cnt=p.get('Count',1)
        if p.get('Type') in ('Item','PrimePart') or nm in ('Neuroptics','Chassis','Systems','Barrel','Receiver','Stock','Blade','Handle','Hilt','Guard','Grip','String','Lower Limb','Upper Limb','Link','Pouch','Stars','Disc','Head','Ornament','Gauntlet','Chain','Boot','Core','Motor','Carapace','Cerebrum','Aspect'):
            rows.append(('comp',nm,cnt))
        else: rows.append(('res',nm,cnt))
    return rows
def resource_line(rows):
    return ' + '.join(f"{n(c)} {link(nm)}" for k,nm,c in rows if k=='res')
def comp_bp(owner,comp):
    for key in (f"{owner} {comp}", f"{owner} {comp.replace('Prime ','',1)}"):
        if key in data.BP: return data.BP[key]
    return None
def esc(s): return s.replace('"','\\"')
def strip_md(s): return re.sub(r'\*\*|\[\[[^|\]]*\|([^\]]*)\]\]',lambda m:m.group(1) or '',s)
