"""Teste de recuperacao do vault para RAG.
Quebra cada .md com rag:true em chunks por heading '## ', prefixa com titulo+aliases,
indexa com BM25 (sem acento, minusculo) e roda as perguntas-alvo.
Uso: python3 _MODELOS/rag_eval.py [k]
BM25 e um limite inferior: embeddings costumam recuperar melhor sinonimos PT/EN."""
import os,re,sys,math,unicodedata,collections
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K=5
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
            if re.match(r"(🔗 Relacionados|📚 Fontes)",head): continue  # secoes so de links: nao indexar
            subs=re.split(r"\n(?=### )",part)
            if len(part)>2500 and len(subs)>1:
                # secao longa: sub-chunks por '### ' mantendo o heading '## ' pai como contexto
                chunks.append((rel,head,f"{title} {al} {subs[0]}"))
                for sp in subs[1:]:
                    chunks.append((rel,head+" > "+sp.split("\n",1)[0].strip("# ").strip(),f"{title} {al} {head} {sp}"))
            else:
                chunks.append((rel,head,f"{title} {al} {part}"))
docs=[norm(c[2]) for c in chunks]; N=len(docs); avg=sum(map(len,docs))/N
df=collections.Counter(w for d in docs for w in set(d)); tfs=[collections.Counter(d) for d in docs]
inv=collections.defaultdict(list)
for _i,_tf in enumerate(tfs):
    for _w,_c in _tf.items(): inv[_w].append((_i,_c))
def score(q):
    # BM25 com indice invertido (mesmo resultado do laco completo, ~100x mais rapido)
    acc=collections.Counter()
    for w in norm(q):
        if w not in df: continue
        idf=math.log(1+(N-df[w]+.5)/(df[w]+.5))
        for i,c in inv[w]:
            L=len(docs[i]); acc[i]+=idf*c*2.2/(c+1.2*(1-.75+.75*L/avg))
    return sorted(((v,i) for i,v in acc.items()),reverse=True)[:K]
