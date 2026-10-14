"""Segunda bateria: perguntas por template sobre TODAS as entidades.
Uso: python3 _MODELOS/rag_eval2.py"""
import os,re,sys,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import rag_core as R
ROOT=R.ROOT
def meta(rel):
    t=open(os.path.join(ROOT,rel),encoding='utf-8').read()
    title=(re.search(r"^title:\s*(.*)$",t,re.M) or [None,""])[1].strip('" ')
    return t,title
def top(q,k=5): return [(R.chunks[i][0],R.chunks[i][1]) for _,i in R.score(q)[:k]]
res=collections.OrderedDict(); fails=collections.defaultdict(list)
def rec(cat,ok,info):
    a=res.setdefault(cat,[0,0]); a[1]+=1; a[0]+=bool(ok)
    if not ok: fails[cat].append(info)
files=sorted(set(c[0] for c in R.chunks))
quests=[f for f in files if f.startswith('missoes/jornadas/') and '/_' not in f]
for f in quests:
    t,ti=meta(f)
    h=top(f"O que a jornada {ti} faz"); rec('1 jornada: o que faz',f in [x[0] for x in h],(f,h[0][0]))
    h=top(f"Dicas de como terminar a jornada {ti}")
    sec=[x for x in h if x[0]==f and re.search(r'dica|passo|walkthrough|como completar|etapa',x[1],re.I)]
    rec('2 jornada: dicas p/ terminar (seção certa)',sec,(f,[x[1][:30] for x in h if x[0]==f]))
    rec('2b jornada: tem seção Passo a Passo/Dicas',re.search(r'^## .*(Dica|Passo|Etapa|Walkthrough)',t,re.M),f)
for q in ["Qual a história do jogo","Me conte a história do Warframe","Resumo da história do game","Qual é o lore do Warframe","história completa do warframe do começo ao fim"]:
    h=top(q,3); rec('3 história do jogo (top-3)','lore/cronologia/cronologia.md' in [x[0] for x in h],(q,h[0][0]))
for f in files:
    if not (f.startswith('warframes/') or f.startswith('armas/')) or '/_' in f or f.startswith('armas/amps/'): continue
    t,ti=meta(f); cat='4a build warframe' if f.startswith('warframes/') else '4b build arma'
    h=top(f"Qual a melhor build para o {ti}")
    ok=[x for x in h if x[0]==f and 'build' in x[1].lower()]
    rec(cat,ok,(f,h[0]))

sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'gerador'))
import itens_local as IL
HUB={'cetus':['CETUS','Cetus','Plains of Eidolon'],'fortuna':['FORTUNA','Orb Vallis'],'deimos':['Deimos','Cambion Drift','Necralisk'],'zariman':['Zariman'],'duviri':['Duviri'],'hollvania':['Höllvania','Hollvania']}
for loc,names in HUB.items():
    note=IL.LOC[loc]['nota']; txt=open(os.path.join(ROOT,note),encoding='utf-8').read()
    for nm in names:
        for q in [f"Me liste todos os itens que eu posso adquirir em {nm}",f"O que eu posso conseguir em {nm}"]:
            h=top(q); ok=[x for x in h if x[0]==note and ('📦' in x[1] or 'Farmar' in x[1])]
            rec('5a listar itens do hub (seção de itens no top-5)',ok,(q,h[0]))
    it=IL.items(loc); miss=[x[0] for x in it if x[0] not in txt]
    rec(f'5b completude da lista ({loc})',not miss,(loc,len(miss)))
print('\n'.join(f"{k}: {a}/{b} = {100*a/b:.1f}%" for k,(a,b) in res.items()))
for k,v in fails.items():
    print(f"\n-- falhas {k} ({len(v)}):"); [print('  ',x) for x in v[:12]]
