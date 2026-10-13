import json,os,re,sys
sys.path.insert(0,os.path.expanduser('~/gen'))
from sections import upsert, fm_set
V=os.path.expanduser('~/mnt/warframe-vault')
U25=json.load(open('u2025.json'))['ALL']; U24=json.load(open('u2024.json'))['ALL']
CATPT={'Warframe':'Warframes','Primary':'armas primárias','Secondary':'armas secundárias','Melee':'armas melee'}
def ranks(U):
    R={}
    for cat,v in U.items():
        for i,(k,x) in enumerate(sorted(v.items(),key=lambda kv:-kv[1]['ALL']),1): R[(cat,k)]=(i,x,len(v))
    return R
R25=ranks(U25); R24=ranks(U24)
IDX={}
for (cat,k) in R25: IDX.setdefault(k.lower(),[]).append(cat)
def pc(x): 
    v=x*100
    return (f"{v:.2f}" if v>=0.1 else f"{v:.3f}").replace('.',',')+'%'
def band(x,a,b): 
    vals=[x[str(i)] for i in range(a,b+1) if str(i) in x]; return sum(vals)/len(vals) if vals else 0
def tier(r,tot):
    p=r/tot
    return 'muito popular (top 5%)' if p<=.05 else 'popular (top 15%)' if p<=.15 else 'uso médio (top 40%)' if p<=.40 else 'pouco usado' if p<=.75 else 'raramente usado'
def section(name,title,cat):
    r,x,tot=R25[(cat,name)]
    L=[f'## ⭐ Avaliação Popular — {title}','',f'Dados **oficiais** da Digital Extremes ([Global Community Stats](https://www.warframe.com/en/community/stats)): % do tempo equipado entre todos os {CATPT[cat]} **rank 30+** em 2025.','',
       '| Métrica | Valor |','|---|---|',f'| Uso em 2025 | **{pc(x["ALL"])}** do tempo equipado |',f'| Posição em 2025 | **#{r} de {tot}** {CATPT[cat]} — {tier(r,tot)} |']
    if (cat,name) in R24:
        r4,x4,t4=R24[(cat,name)]; d=r4-r
        L.append(f'| Posição em 2024 | #{r4} de {t4} ({pc(x4["ALL"])}) → ' + ('subiu '+str(d)+' posições' if d>0 else 'caiu '+str(-d)+' posições' if d<0 else 'mesma posição') + ' |')
    else: L.append('| Posição em 2024 | sem dado (item novo ou sem uso registrado) |')
    L.append(f'| Uso por faixa de MR | MR 0–10: {pc(band(x,0,10))} · MR 11–20: {pc(band(x,11,20))} · MR 21–30: {pc(band(x,21,30))} · Legendary: {pc(band(x,31,36))} |')
    hi=max([(band(x,0,10),'iniciantes (MR 0–10)'),(band(x,11,20),'intermediários (MR 11–20)'),(band(x,21,30),'veteranos (MR 21–30)'),(band(x,31,36),'Legendary')])[1]
    L+=['',f'**Leitura:** {title} é {tier(r,tot)} entre os {CATPT[cat]}, e o público que mais usa são os jogadores **{hi}**. A DE avisa que uso **não é tier list**: mede preferência e conveniência, não poder.']
    return '\n'.join(L), r, tot, x['ALL']
done=0; data_out={}
for dp,dn,fn in os.walk(V):
    if '/.' in dp or '_MODELOS' in dp: continue
    top=os.path.relpath(dp,V).split('/')[0]
    if top not in ('warframes','armas'): continue
    for f in fn:
        if not f.endswith('.md') or f.startswith('_'): continue
        p=os.path.join(dp,f); t=open(p,encoding='utf-8').read()
        m=re.search(r'^title:\s*"?(.*?)"?\s*$',t,re.M)
        if not m: continue
        title=m.group(1); key=title.replace(' e ',' & ')
        cands=[key,title,key+' (Secondary)',key+' (Dual Swords)',key+' (Melee)']
        hit=None
        for c in cands:
            for cat in (['Warframe'] if top=='warframes' else ['Primary','Secondary','Melee']):
                if (cat,c) in R25: hit=(c,cat); break
            if hit: break
        if not hit: continue
        body,r,tot,share=section(hit[0],title,hit[1])
        t=upsert(t,'## ⭐ Avaliação Popular',body)
        t=fm_set(t,'uso_2025_rank',f'"{r}/{tot}"'); t=fm_set(t,'uso_2025_pct',round(share*100,3))
        open(p,'w',encoding='utf-8').write(t); done+=1; data_out[os.path.relpath(p,V)]=(hit[1],r,tot,share)
json.dump(data_out,open('pop_done.json','w'),indent=0)
print('atualizados',done)
