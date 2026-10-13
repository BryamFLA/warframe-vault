import os,sys,re,glob,json
sys.path.insert(0,os.path.expanduser('~/gen'))
import data, build
from sections import fm_set
V=os.path.expanduser('~/mnt/warframe-vault')
import gen_mods as g
def slug(s): return g.slug(s)
def first_sentence(t):
    t=build.strip_md(t) if hasattr(build,'strip_md') else re.sub(r'[*_`\[\]]','',t)
    t=re.sub(r'\s+',' ',t).strip()
    m=re.match(r'(.{20,220}?[.;])(\s|$)',t)
    return (m.group(1) if m else t[:220]).replace('"',"'")
def prime_vaulted(name):
    rs=[v for (it,p),v in data.RELIC_IDX.items() if it==name]
    if not rs: return None
    allr=[x for v in rs for x in v]
    return all(x[2] for x in allr)
ch=0
for f in glob.glob(V+'/**/*.md',recursive=True):
    rel=os.path.relpath(f,V)
    if rel.startswith('_') or '/_' in rel: continue
    top=rel.split('/')[0]
    if top not in ('warframes','armas','companheiros','mods','recursos'): continue
    s=open(f).read()
    if not s.startswith('---'): continue
    fm=s.split('---')[1]
    m=re.search(r'^title:\s*(.+)$',fm,re.M)
    if not m: continue
    title=m.group(1).strip().strip('"')
    tm=re.search(r'^tipo:\s*(.+)$',fm,re.M); tipo=tm.group(1).strip() if tm else top
    o=s
    s=fm_set(s,'id',f'{re.sub("[^a-z]","",tipo)}:{slug(title)}')
    if title in data.WF and isinstance(data.WF[title],dict):
        w=data.WF[title]
        if w.get('Progenitor'): s=fm_set(s,'elemento_progenitor',w['Progenitor'])
        if 'Prime' in title:
            v=w.get('Vaulted'); pv=prime_vaulted(title)
            s=fm_set(s,'vaultado','true' if (pv if pv is not None else bool(v)) else 'false')
    elif title in data.WEAP:
        w=data.WEAP[title]
        if w.get('Mastery') is not None: s=fm_set(s,'mastery_rank',str(w['Mastery']))
        if 'Tradable' in w: s=fm_set(s,'negociavel','true' if w['Tradable'] else 'false')
        if w.get('Slot'): s=fm_set(s,'slot',w['Slot'])
        if w.get('Class'): s=fm_set(s,'classe',w['Class'])
        if w.get('Disposition'): s=fm_set(s,'disposicao_riven',str(w['Disposition']))
        if 'Prime' in title:
            pv=prime_vaulted(title)
            if pv is not None: s=fm_set(s,'vaultado','true' if pv else 'false')
    elif top=='mods':
        mm=g.M.get(title) or g.A.get(title)
        if isinstance(mm,dict):
            if 'Tradable' in mm: s=fm_set(s,'negociavel','true' if mm['Tradable'] else 'false')
            if mm.get('MaxRank') is not None: s=fm_set(s,'rank_max',str(mm['MaxRank']))
            if mm.get('BaseDrain') is not None: s=fm_set(s,'drenagem_base',str(mm['BaseDrain']))
            if mm.get('IsAbilityAugment'): s=fm_set(s,'augment_de',mm.get('Type',''))
    acq=build.ACQ.get(title)
    if acq and 'fonte_principal:' not in s: s=fm_set(s,'fonte_principal','"'+first_sentence(acq)+'"')
    if s!=o: open(f,'w').write(s); ch+=1
print('changed',ch)
