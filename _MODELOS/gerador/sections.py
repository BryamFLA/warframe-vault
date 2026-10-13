import re
def upsert(text, heading_prefix, body, before=('## 🔗 Relacionados','## 📚 Fontes','## 💡 Curiosidades')):
    """heading_prefix ex: '## ⭐ Avaliação Popular' ; body inclui a linha do heading."""
    pat=re.compile(r'^'+re.escape(heading_prefix)+r'.*?(?=^## |\Z)',re.M|re.S)
    if pat.search(text): return pat.sub(lambda m: body.rstrip()+'\n\n',text,1)
    for b in before:
        m=re.search(r'^'+re.escape(b),text,re.M)
        if m: return text[:m.start()]+body.rstrip()+'\n\n'+text[m.start():]
    return text.rstrip()+'\n\n'+body.rstrip()+'\n'
def fm_set(text,key,value):
    m=re.match(r'---\n(.*?)\n---\n',text,re.S)
    if not m: return text
    fm=m.group(1)
    line=f'{key}: {value}'
    if re.search(r'^'+re.escape(key)+r':.*$',fm,re.M): fm=re.sub(r'^'+re.escape(key)+r':.*$',line.replace('\\','\\\\'),fm,1,flags=re.M)
    else: fm=fm+'\n'+line
    return '---\n'+fm+'\n---\n'+text[m.end():]
