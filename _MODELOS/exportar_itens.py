#!/usr/bin/env python3
"""Exporta o frontmatter de todas as notas do vault para _MODELOS/dados/itens.json
(uma linha por entidade) — base para o agente de IA cruzar com o inventário do jogador.
Uso: python3 _MODELOS/exportar_itens.py  (rodar na raiz do vault)"""
import glob, json, os, re, yaml, datetime
V = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMPOS = ['id','title','aliases','tipo','subtipo','categoria','raridade','resumo','status','mastery_rank',
          'negociavel','vaultado','slot','classe','disposicao_riven','elemento_progenitor','fonte_principal',
          'augment_de','rank_max','drenagem_base','polaridade','uso_2025_rank','uso_2025_pct','tags']
out = []
for f in sorted(glob.glob(V + '/**/*.md', recursive=True)):
    rel = os.path.relpath(f, V)
    if rel.startswith('_MODELOS'): continue
    t = open(f, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---\n', t, re.S)
    if not m: continue
    try: d = yaml.safe_load(m.group(1)) or {}
    except Exception: continue
    if d.get('rag') is False: continue
    e = {k: d[k] for k in CAMPOS if k in d and d[k] not in (None, '')}
    e['caminho'] = rel
    if 'id' not in e: e['id'] = re.sub(r'[^a-z0-9:]+', '_', (str(d.get('tipo','nota')) + ':' + os.path.splitext(os.path.basename(rel))[0]).lower())
    for k, v in list(e.items()):
        if isinstance(v, (datetime.date, datetime.datetime)): e[k] = v.isoformat()
    out.append(e)
os.makedirs(V + '/_MODELOS/dados', exist_ok=True)
json.dump(out, open(V + '/_MODELOS/dados/itens.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
from collections import Counter
print(len(out), 'entidades'); print(Counter(str(e.get('tipo')) for e in out).most_common(25))
