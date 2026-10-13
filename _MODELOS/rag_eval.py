"""Teste de recuperacao do vault para RAG.
Quebra cada .md com rag:true em chunks por heading '## ', prefixa com titulo+aliases,
indexa com BM25 (sem acento, minusculo) e roda as perguntas-alvo.
Uso: python3 _MODELOS/rag_eval.py [k]
BM25 e um limite inferior: embeddings costumam recuperar melhor sinonimos PT/EN."""
import os,re,sys,math,unicodedata,collections
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K=int(sys.argv[1]) if len(sys.argv)>1 else 5
STOP=set("a o as os de da do das dos e em no na nos nas um uma para por com que qual quais como onde posso pode me eu meu minha mais the of to and is in se ao aos sua seu ser ter tem da pra ou".split())
def norm(s):
    s=unicodedata.normalize("NFKD",s.lower()); s="".join(c for c in s if not unicodedata.combining(c))
    return [w for w in re.findall(r"[a-z0-9]+",s) if w not in STOP and len(w)>1]
def fm(t):
    m=re.match(r"---\n(.*?)\n---\n",t,re.S); return (m.group(1) if m else ""), (t[m.end():] if m else t)
chunks=[]
for dp,dn,fn in os.walk(ROOT):
    if "/." in dp or "_MODELOS" in dp: continue
    for f in fn:
        if not f.endswith(".md"): continue
        p=os.path.join(dp,f); t=open(p,encoding="utf-8").read(); h,b=fm(t)
        if re.search(r"^rag:\s*false",h,re.M): continue
        title=(re.search(r"^title:\s*(.*)$",h,re.M) or [None,f])[1]
        al=(re.search(r"^aliases:\s*(.*)$",h,re.M) or [None,""])[1]
        rel=os.path.relpath(p,ROOT)
        for part in re.split(r"\n(?=## )",b):
            head=part.split("\n",1)[0].strip("# ").strip()
            chunks.append((rel,head,f"{title} {al} {part}"))
docs=[norm(c[2]) for c in chunks]; N=len(docs); avg=sum(map(len,docs))/N
df=collections.Counter(w for d in docs for w in set(d)); tfs=[collections.Counter(d) for d in docs]
def score(q):
    qs=norm(q); out=[]
    for i,tf in enumerate(tfs):
        s=0; L=len(docs[i])
        for w in qs:
            if w in tf:
                idf=math.log(1+(N-df[w]+.5)/(df[w]+.5)); s+=idf*tf[w]*2.2/(tf[w]+1.2*(1-.75+.75*L/avg))
        out.append((s,i))
    return sorted(out,reverse=True)[:K]
Q=[("Onde posso conseguir o warframe Excalibur","warframes/regular/excalibur.md"),
("O que posso farmar em CETUS","locais/open-worlds/cetus.md"),
("Me liste tudo o que posso fazer em FORTUNA","locais/open-worlds/fortuna.md"),
("Qual a historia dos Corpus","lore/faccoes/corpus.md"),
("Crie um passo a passo de como criar a arma Alternox","armas/primarias/alternox.md"),
("Como posso conseguir CRIOTICO","recursos/raridades/raro/cryotic.md"),
("Me conte um resumo da historia do game","lore/cronologia/cronologia.md"),
("O que da pra fazer e farmar na terra, como missoes, itens e tudo o mais que tiver","locais/planetas/terra.md")]
if "--geral" in sys.argv:
    # perguntas geradas para TODA entidade indexavel de warframes/, armas/ e recursos/
    import random
    tmpl={"warframes":"Onde posso conseguir o warframe {t}","armas":"Crie um passo a passo de como criar a arma {t}","recursos":"Como posso conseguir {t}"}
    G=collections.defaultdict(lambda:[0,0]); falhas=[]
    for rel in sorted(set(c[0] for c in chunks)):
        top=rel.split("/")[0]
        if top not in tmpl: continue
        t0=open(os.path.join(ROOT,rel),encoding="utf-8").read(3000)
        title=(re.search(r"^title:\s*(.*)$",t0,re.M) or [None,""])[1].strip('" ')
        if not title or "Indice" in rel: continue
        hit=[chunks[i][0] for _,i in score(tmpl[top].format(t=title))]
        G[top][1]+=1
        if rel in hit: G[top][0]+=1
        else: falhas.append((rel,hit[0]))
    for k,(a,b) in G.items(): print(f"{k}: {a}/{b} = {100*a/b:.1f}% no top-{K}")
    print("exemplos de falha:"); [print("  ",f,"->",h) for f,h in falhas[:25]]
    sys.exit()
ok=0
print(f"chunks indexados: {N}\n")
for q,exp in Q:
    r=score(q); hit=[chunks[i][0] for _,i in r]
    pos=hit.index(exp)+1 if exp in hit else None; ok+=bool(pos)
    print(("OK " if pos else "FALHA ")+f"[{pos or '-'}] {q}\n   esperado: {exp}")
    for s,i in r: print(f"   {s:6.2f}  {chunks[i][0]} :: {chunks[i][1][:60]}")
    print()
print(f"RESULTADO: {ok}/{len(Q)} com o arquivo esperado no top-{K}")
