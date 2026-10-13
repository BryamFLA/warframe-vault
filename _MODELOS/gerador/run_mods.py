import os,sys,re
sys.path.insert(0,os.path.expanduser('~/gen'))
import gen_mods as g, data
V=os.path.expanduser('~/mnt/warframe-vault')
have=set(data.TITLE.keys())
# also aliases
import glob
for f in glob.glob(V+'/**/*.md',recursive=True):
    try: t=open(f).read(2000)
    except: continue
    m=re.search(r'^aliases:\s*\[(.*)\]',t,re.M)
    if m:
        for a in m.group(1).split(','): have.add(a.strip().strip('"\'').lower())
w=sk=0; dry='--dry' in sys.argv
def write(path,txt):
    global w
    if os.path.exists(path): return
    w+=1
    if dry: return
    os.makedirs(os.path.dirname(path),exist_ok=True); open(path,'w').write(txt)
for name,m in g.M.items():
    if not isinstance(m,dict) or m.get('_IgnoreEntry') or m.get('IsFlawed'): sk+=1; continue
    if name.lower() in have: sk+=1; continue
    if m.get('Rarity')=='Riven' or 'Riven Mod' in name: sk+=1; continue
    write(f"{V}/{g.mdir(m.get('Type',''),m.get('IsAbilityAugment'))}/{g.slug(name)}.md", g.gen_mod(name,m))
for name,m in g.A.items():
    if not isinstance(m,dict) or m.get('_IgnoreEntry'): sk+=1; continue
    if name.lower() in have: sk+=1; continue
    write(f"{V}/mods/arcanes/{g.slug(name)}.md", g.gen_mod(name,m,arc=True))
print('written',w,'skipped',sk)
