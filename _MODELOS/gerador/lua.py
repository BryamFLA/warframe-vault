import re
TOK=re.compile(r'''\s+|--\[\[.*?\]\]|--[^\n]*|(?P<s>"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')|(?P<n>-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)|(?P<p>[{}\[\]=,;])|(?P<w>[A-Za-z_][A-Za-z_0-9.]*)''',re.S)
def tokens(s):
    for m in TOK.finditer(s):
        k=m.lastgroup
        if k: yield k,m.group(k)
def unq(s):
    s=s[1:-1]
    return re.sub(r'\\(.)',lambda m:{'n':'\n','t':'\t'}.get(m.group(1),m.group(1)),s)
def parse_table_at(src,start):
    """parse lua table literal beginning at src[start]=='{'"""
    toks=list(tokens(src[start:]))
    pos=[0]
    def val():
        k,v=toks[pos[0]]; pos[0]+=1
        if k=='s': return unq(v)
        if k=='n': return float(v) if ('.' in v or 'e' in v.lower()) else int(v)
        if k=='w':
            return {'true':True,'false':False,'nil':None}.get(v,v)
        if v=='{': return table()
        raise ValueError(v)
    def table():
        d={}; arr=[]
        while True:
            k,v=toks[pos[0]]
            if v=='}': pos[0]+=1; break
            if v in ',;': pos[0]+=1; continue
            if v=='[':
                pos[0]+=1; key=val(); pos[0]+=1  # ]
                pos[0]+=1  # =
                d[key]=val(); continue
            if k=='w' and toks[pos[0]+1][1]=='=':
                pos[0]+=2; d[v]=val(); continue
            arr.append(val())
        if arr and not d: return arr
        if arr: d['_arr']=arr
        return d
    assert toks[0][1]=='{'
    pos[0]=1
    return table()
def load_module(path):
    s=open(path,encoding='utf-8').read()
    # find 'return {' or first 'local ... = {'
    m=re.search(r'\breturn\s*\{',s)
    i=s.index('{',m.start()) if m else s.index('{')
    return parse_table_at(s,i)
