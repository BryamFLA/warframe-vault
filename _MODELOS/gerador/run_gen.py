import json,os,sys,re
from gen_wf import gen_warframe
from gen_weap import gen_weapon
import data
S=json.load(open('stubs.json')); out=os.path.expanduser('~/gen/out'); os.makedirs(out,exist_ok=True)
ok=[];miss=[]
for o in S:
    p=o['path']; t=o['title']
    md=gen_warframe(t,p) if p.startswith('warframes') else gen_weapon(t,p)
    if not md: miss.append((p,t)); continue
    dst=os.path.join(out,p); os.makedirs(os.path.dirname(dst),exist_ok=True); open(dst,'w',encoding='utf-8').write(md); ok.append(p)
json.dump({'ok':ok,'miss':miss},open('gen_result.json','w'),indent=0)
print(len(ok),len(miss)); print(miss)
