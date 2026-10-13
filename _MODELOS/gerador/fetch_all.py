import json,os,wiki,time
S=json.load(open(os.path.expanduser('~/gen/stubs.json')))
def wname(t): return t.replace(' e ',' & ')
n=0
for o in S:
    t=wiki.page_text(wname(o['title'])); n+=1
    if n%25==0: print(n,flush=True)
print('DONE',flush=True)
