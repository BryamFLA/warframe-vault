import json,urllib.request,urllib.parse,re,html,os,time,sys
CACHE=os.path.expanduser('~/gen/cache'); os.makedirs(CACHE,exist_ok=True)
def page_text(title):
    fn=os.path.join(CACHE,re.sub(r'[^A-Za-z0-9_-]','_',title)+'.txt')
    if os.path.exists(fn): return open(fn,encoding='utf-8').read()
    u="https://wiki.warframe.com/api.php?"+urllib.parse.urlencode({"action":"parse","page":title,"prop":"text","format":"json","redirects":1,"disablelimitreport":1})
    for i in range(3):
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"warframe-vault-bot/1.0"}),timeout=60)); break
        except Exception as e:
            time.sleep(2); d=None
    if not d or 'parse' not in d: open(fn,'w').write(''); return ''
    t=d["parse"]["text"]["*"]
    t=re.sub(r'<(script|style)[^>]*>.*?</\1>','',t,flags=re.S)
    t=re.sub(r'<h2[^>]*>(.*?)</h2>',lambda m:'\n@@H2 '+re.sub(r'<[^>]+>','',m.group(1))+'\n',t,flags=re.S)
    t=re.sub(r'<br\s*/?>','\n',t); t=re.sub(r'</(p|tr|li|h\d|div|table)>','\n',t); t=re.sub(r'</t[dh]>',' | ',t)
    t=re.sub(r'<[^>]+>','',t); t=html.unescape(t); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(fn,'w',encoding='utf-8').write(t); return t
def section(t,name):
    m=re.search(r'@@H2 '+re.escape(name)+r'(?:\[edit[^\n]*)?\n(.*?)(?=\n@@H2 |\Z)',t,re.S)
    return m.group(1) if m else ''
if __name__=='__main__':
    t=page_text(sys.argv[1]); print(section(t,sys.argv[2] if len(sys.argv)>2 else 'Acquisition')[:3000])
