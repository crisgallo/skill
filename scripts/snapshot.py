#!/usr/bin/env python3
"""Fotografia delle fonti delle skill.

  scripts/snapshot.py --init     crea snapshots/state.json (primo giro, nessun confronto)
  scripts/snapshot.py --check    confronta con lo stato salvato e stampa gli URL cambiati
  scripts/snapshot.py --update   come --check, e poi salva il nuovo stato

Per ogni URL citato in skills/*/SKILL.md scarica la pagina, toglie script, stili e tag,
normalizza gli spazi e calcola un hash. Firma = insieme degli hash delle frasi; cambiata = almeno 3 frasi e il 5% diverse.
Lo stato tiene anche il codice HTTP: 403/404/timeout sono "non leggibili", non "cambiati".
"""
import concurrent.futures as cf, hashlib, json, os, re, ssl, sys, time, urllib.request, urllib.error
from datetime import date
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
STATE = os.path.join(ROOT, "snapshots", "state.json")
URL_RE = re.compile(r"https?://[^\s<>()\[\]\"'`]+")
CA = "/root/.ccr/ca-bundle.crt"

class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.out=[]; self.skip=0
    def handle_starttag(self, tag, attrs):
        if tag in ("script","style","noscript","svg"): self.skip+=1
    def handle_endtag(self, tag):
        if tag in ("script","style","noscript","svg") and self.skip: self.skip-=1
    def handle_data(self, d):
        if not self.skip: self.out.append(d)

def urls_per_skill():
    m={}
    for name in sorted(os.listdir(SKILLS)):
        p=os.path.join(SKILLS,name,"SKILL.md")
        if not os.path.isfile(p): continue
        t=open(p,encoding="utf-8").read()
        for u in URL_RE.findall(t):
            u=u.rstrip(".,;:*_")
            if u.endswith(")"): u=u[:-1]
            m.setdefault(u,set()).add(name)
    return m

BREVO_RE=re.compile(r"https://help\.brevo\.com/hc/[a-z-]+/articles/(\d+)")

def fetch(u):
    ctx=ssl.create_default_context(cafile=CA if os.path.exists(CA) else None)
    # help.brevo.com risponde 403 alle pagine HTML: si legge il corpo dall'API Zendesk (stesso contenuto).
    m=BREVO_RE.match(u)
    url=f"https://help.brevo.com/api/v2/help_center/en-us/articles/{m.group(1)}.json" if m else u
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (skill-snapshot)","Accept-Language":"en-US,en;q=0.9"})
    try:
        with urllib.request.urlopen(req,timeout=25,context=ctx) as r:
            body=r.read(2_000_000).decode(r.headers.get_content_charset() or "utf-8","replace")
            code=r.status
            if m:
                try: body=json.loads(body)["article"]["body"]
                except Exception: return u,"ERR",None
    except urllib.error.HTTPError as e:
        return u,e.code,None
    except Exception as e:
        return u,"ERR",None
    p=Text(); p.feed(body)
    txt=re.sub(r"\s+"," "," ".join(p.out)).strip()
    if len(txt)<200: return u,code,None   # pagina vuota o solo JS: non affidabile
    return u,code,sentences(txt)

def sentences(txt):
    """Firma della pagina: hash delle frasi lunghe almeno 40 caratteri.
    Le pagine Google inseriscono a ogni richiesta token numerici casuali: un hash unico
    dell'intera pagina cambia sempre. Confrontando le frasi, quel rumore resta confinato
    a una o due frasi e non fa scattare il segnale."""
    out=set()
    for s_ in re.split(r"(?<=[.!?])\s+", txt):
        s_=s_.strip()
        if len(s_)>=40: out.add(hashlib.sha256(s_.encode()).hexdigest()[:10])
    return sorted(out)

def differs(old, new, min_sent=3, min_frac=0.05):
    """Cambiata davvero se almeno 3 frasi E almeno il 5% delle frasi sono diverse."""
    if not old or not new: return False
    o,n=set(old),set(new); d=len(o^n); tot=max(len(o|n),1)
    return d>=min_sent and d/tot>=min_frac

def run(mode):
    m=urls_per_skill()
    old=json.load(open(STATE)) if os.path.exists(STATE) else {"urls":{}, "locali":{}}
    today=date.today().isoformat()
    new={"created":old.get("created",today),"updated":today,"locali":old.get("locali",{}),"urls":{}}
    changed=[]; unreadable=[]
    with cf.ThreadPoolExecutor(12) as ex:
        for u,code,h in ex.map(fetch, sorted(m)):
            rec={"skills":sorted(m[u]),"status":code,"hash":h,"checked":today}
            prev=old["urls"].get(u)
            if h is None:
                unreadable.append((u,code)); rec["hash"]=prev.get("hash") if prev else None
            elif prev and prev.get("hash") and differs(prev["hash"] if isinstance(prev["hash"],list) else [], h):
                changed.append(u); rec["changed"]=today
            new["urls"][u]=rec
    if mode in ("--init","--update"):
        os.makedirs(os.path.dirname(STATE),exist_ok=True)
        json.dump(new,open(STATE,"w"),indent=1,ensure_ascii=False)
    print(f"URL: {len(m)}  leggibili: {len(m)-len(unreadable)}  non leggibili: {len(unreadable)}  cambiati: {len(changed)}")
    for u in changed: print("CAMBIATO",u,";".join(m[u]))
    for u,c in unreadable: print("NONLEGGIBILE",c,u)

if __name__=="__main__":
    run(sys.argv[1] if len(sys.argv)>1 else "--check")
