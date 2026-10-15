#!/usr/bin/env python3
"""Gera a seção '## 🔢 Contagem — <índice>' em todos os _* _Indice.md (rodar depois de indices.py).
Responde perguntas como "quantos warframes tem no jogo?" — o frontmatter não entra no RAG, então os números
precisam estar no corpo da nota. Também adiciona aliases ("quantos warframes", "lista de armas"...) e
atualiza os campos total-* do frontmatter.   Uso: python3 _MODELOS/gerador/contagens.py"""
import os, re, glob, collections, datetime
import yaml

V = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
HOJE = datetime.date.today().isoformat()
ROTULO = {  # pasta -> como falar dela
    'regular': 'Warframes base', 'primes': 'Warframes Prime', 'umbra': 'Umbra',
    'primarias': 'armas primárias', 'secundarias': 'armas secundárias', 'brancas': 'armas corpo a corpo (melee)',
    'archwing': 'armas de Archwing', 'amps': 'Amps', 'robotica': 'armas de companheiros robóticos',
    'geral': 'gerais', 'principais': 'principais', 'secundarios': 'secundárias',
}
ROTULO_POR_INDICE = {'Mods': {'arcanes': 'Arcanes', 'armas': 'mods de armas', 'companheiros': 'mods de companheiros',
                              'especiais': 'mods especiais', 'warframe': 'mods de Warframe'}}
ORDEM = {'regular': 0, 'primes': 1, 'umbra': 2}

def fm(t):
    m = re.match(r'---\n(.*?)\n---\n', t, re.S)
    try:
        return (yaml.safe_load(m.group(1)) or {}) if m else {}
    except Exception:
        return {}

def notas(d):
    """Notas de conteúdo (sem índices/_ e sem rag: false) abaixo de d, agrupadas pela 1ª subpasta."""
    g = collections.OrderedDict()
    for root, dirs, files in os.walk(d):
        dirs.sort()
        for f in sorted(files):
            if not f.endswith('.md') or f.startswith('_'):
                continue
            p = os.path.join(root, f)
            m = fm(open(p, encoding='utf-8').read(4000))
            if m.get('rag') is False:
                continue
            rel = os.path.relpath(root, d)
            g.setdefault('geral' if rel == '.' else rel.split(os.sep)[0], []).append((p, m))
    return g

def nome_base(title):
    return re.sub(r'\s*[—-]\s*[ÍI]ndice.*$', '', title).strip()

def bloco(title, grupos):
    base = nome_base(title)
    rot = lambda k: ROTULO_POR_INDICE.get(base, {}).get(k) or ROTULO.get(k, k)
    grupos = collections.OrderedDict(sorted(grupos.items(), key=lambda kv: (ORDEM.get(kv[0], 9), -len(kv[1]))))
    total = sum(len(v) for v in grupos.values())
    linhas = [f'## 🔢 Contagem — {title}', '']
    if base == 'Warframes':
        reg = [m.get('title') for _, m in grupos.get('regular', [])]
        pri = {m.get('title') for _, m in grupos.get('primes', [])}
        sem = sorted(n for n in reg if f'{n} Prime' not in pri)
        nu = len(grupos.get('umbra', []))
        linhas += [f'O jogo tem **{len(reg)} Warframes base** (cada personagem jogável diferente), '
                   f'**{len(pri)} versões Prime** e **{nu} Umbra** (Excalibur Umbra e Excalibur Umbra Prime): '
                   f'**{len(reg) + len(pri) + nu} Warframes no total** contando as variantes. '
                   f'{len(reg) - len(sem)} dos {len(reg)} Warframes base já têm versão Prime.',
                   '',
                   f'Sem versão Prime ainda ({len(sem)}): ' + ', '.join(sem) + '.',
                   '',
                   f'(A wiki oficial pode mostrar um total ligeiramente diferente por contar só alguns modelos; contagem feita sobre as notas do vault em {HOJE}.)']
    else:
        arc = len(grupos.get('arcanes', [])) if base == 'Mods' else 0   # Arcanes ficam na pasta de mods mas não são mods
        partes = [f'{len(v)} {rot(k)}' for k, v in grupos.items() if not (arc and k == 'arcanes')]
        linhas += [f'Total de {base.lower()} no vault: **{total - arc}**' + (' — ' + ', '.join(partes) + '.' if len(partes) > 1 else '.')
                   + (f' Além disso, **{arc} Arcanes** (não são mods, mas ficam nesta seção do vault).' if arc else '')]
    linhas += ['', '| Grupo | Quantidade |', '|---|---|']
    linhas += [f'| {rot(k)} | {len(v)} |' for k, v in grupos.items()]
    linhas += [f'| **Total** | **{total}** |', '']
    return '\n'.join(linhas), total, grupos

def aliases_novos(title):
    b = nome_base(title).lower()
    return [f'quantos {b}', f'quantas {b}', f'quantidade de {b}', f'número de {b}', f'lista de {b}',
            f'todos os {b}', f'todas as {b}', f'total de {b}']

for ip in sorted(p for p in glob.glob(V + '/**/_*_Indice.md', recursive=True) if '/_MODELOS/' not in p):
    t = open(ip, encoding='utf-8').read()
    title = fm(t).get('title') or os.path.basename(ip)[:-3]
    grupos = notas(os.path.dirname(ip))
    if not grupos:
        continue
    txt, total, grupos = bloco(title, grupos)
    t = re.sub(r'\n## 🔢 Contagem — .*?(?=\n## |\Z)', '\n', t, flags=re.S)       # tira a versão antiga
    ancora = re.search(r'\n## (?!📊 Visão Geral)', t[t.find('\n## '):])            # logo depois da Visão Geral
    pos = t.find('\n## ') + ancora.start() if ancora else len(t)
    t = t[:pos] + '\n\n' + txt + t[pos:]
    # aliases
    m = re.search(r'^aliases:\s*\[(.*)\]\s*$', t, re.M)
    if m:
        atuais = [a.strip().strip('"\'') for a in m.group(1).split(',') if a.strip()]
        novos = [a for a in aliases_novos(title) if a not in atuais]
        if novos:
            t = t[:m.start()] + 'aliases: [' + ', '.join(atuais + novos) + ']' + t[m.end():]
    # frontmatter total-*
    if nome_base(title) == 'Warframes':
        nr, np_, nu = (len(grupos.get(k, [])) for k in ('regular', 'primes', 'umbra'))
        for k, v in (('total-warframes', nr + np_ + nu), ('total-base', nr), ('total-prime', np_), ('total-umbra', nu)):
            t = re.sub(rf'^{k}:.*$', f'{k}: {v}', t, count=1, flags=re.M)
    t = re.sub(r'^(atualizado:).*$', rf'\g<1> {HOJE}', t, count=1, flags=re.M)
    t = re.sub(r'\n{3,}', '\n\n', t)
    open(ip, 'w', encoding='utf-8').write(t)
    print(f'{os.path.relpath(ip, V)}: {total}')
