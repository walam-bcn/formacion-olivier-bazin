#!/usr/bin/env python3
"""Genera las landing pages de WA LAM en /landings con el estilo de la landing de formación.

Uso:  python3 tools/build_landings.py
Los textos están en tools/landings_content.py. Lo que va entre [[ ]] es un dato
pendiente de completar por WA LAM y se muestra resaltado en la página.
"""
import html, json, re, sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from landings_content import PAGES, GROUPS, SITE  # noqa: E402

LOGO = (ROOT / "tools" / "logo.b64").read_text().strip()
OUT = ROOT / "landings"
OUT.mkdir(exist_ok=True)
BYSLUG = {p["slug"]: p for p in PAGES}


def fmt(s):
    """Escapa y convierte **negrita**, *turquesa* y [[pendiente]]."""
    s = html.escape(s, quote=False)
    s = re.sub(r"\[\[(.+?)\]\]", r'<span class="pend">\1</span>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r'<span class="tq">\1</span>', s)
    return s


def plain(s):
    return re.sub(r"\[\[|\]\]|\*", "", s)


def url(slug):
    return f"{SITE['base']}/{slug}"


def wa(text):
    return f"https://wa.me/{SITE['wa']}?text={quote(text)}"


CSS = """
:root{--pet:#1D3F40;--tq:#0CBFC2;--hueso:#FFFFFF;--piedra:#F2F1EE;--tx:#1D3F40}
*{margin:0;padding:0;box-sizing:border-box}
html{background:#1D3F40;scroll-behavior:smooth}
html,body{overflow-x:hidden;max-width:100%}
body{font-family:'Poppins',system-ui,sans-serif;color:var(--tx);background:#1D3F40;min-height:100vh;font-weight:300;line-height:1.68}
img{max-width:100%}
.wrap{max-width:1150px;margin:0 auto;padding:0 26px}
section{padding:56px 0}
h1,h2,h3,h4{font-weight:700;line-height:1.16;letter-spacing:-.01em}
p{text-align:justify;text-justify:inter-word}
.center,.center p{text-align:center}
.eyebrow{display:inline-flex;align-items:baseline;gap:9px;font-weight:700;font-size:clamp(.95rem,2vw,1.2rem);letter-spacing:.06em;text-transform:uppercase;color:var(--tq)}
.k{font-size:.72rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--tq)}
.tq{color:var(--tq);font-weight:600}
.btn{display:inline-block;text-decoration:none;font-weight:600;font-size:.95rem;padding:14px 26px;border-radius:40px;transition:.2s;cursor:pointer;border:2px solid transparent;text-align:center}
.btn-tq{background:var(--tq);color:#1D3F40;border-color:var(--tq)}.btn-tq:hover{filter:brightness(1.06)}
.btn-gh{background:transparent;color:var(--tq);border-color:var(--tq)}.btn-gh:hover{background:var(--tq);color:#1D3F40}
.btn-dk{background:var(--pet);color:#fff;border-color:var(--pet)}
.btn-row{display:flex;flex-wrap:wrap;gap:13px;margin-top:26px}
.pend{background:rgba(12,191,194,.14);border:1px dashed var(--tq);border-radius:6px;padding:0 6px;font-weight:500;color:inherit;white-space:normal}
/* nav */
.topnav{background:var(--pet);padding:15px 0;border-bottom:1px solid rgba(255,255,255,.08)}
.topnav .wrap{display:flex;justify-content:space-between;align-items:center;gap:16px}
.topnav nav{display:flex;gap:20px;font-size:.8rem}.topnav nav a{color:#fff;opacity:.85;text-decoration:none}.topnav nav a:hover{color:var(--tq);opacity:1}
.crumbs{font-size:.78rem;color:rgba(255,255,255,.7);margin-bottom:14px}.crumbs a{color:rgba(255,255,255,.8);text-decoration:none}.crumbs a:hover{color:var(--tq)}
/* hero */
.hero{background:radial-gradient(1100px 560px at 78% 20%,#22494a,var(--pet));color:#fff}
.hero .wrap{display:grid;grid-template-columns:1.2fr .8fr;gap:52px;align-items:center}
.hero h1{font-size:clamp(2.1rem,5.4vw,3.6rem);color:#fff;margin:14px 0 8px}
.hero .hs{color:var(--tq);font-size:clamp(1rem,2.2vw,1.25rem);font-weight:600}
.hero .lead{margin-top:20px;color:#fff;max-width:56ch;font-size:1.05rem;text-align:left}
.hcard{background:rgba(255,255,255,.05);border:1px solid rgba(12,191,194,.35);border-radius:22px;padding:28px 26px;backdrop-filter:blur(2px)}
.hcard .k{display:block;margin-bottom:14px}
.hcard ul{list-style:none}
.hcard li{position:relative;padding:10px 0 10px 28px;border-bottom:1px solid rgba(255,255,255,.1);font-size:.93rem;color:#fff}
.hcard li:last-child{border-bottom:none}
.hcard li::before{content:"";position:absolute;left:4px;top:19px;width:8px;height:8px;border-radius:50%;background:var(--tq)}
/* espejo */
.mirror{background:#fff}
.head{max-width:780px;margin:0 auto 34px;text-align:center}
.head h2{color:var(--pet);font-size:clamp(1.6rem,3.6vw,2.3rem);margin-top:10px}
.head p{color:#1D3F40;margin-top:14px;text-align:center}
.dark .head h2{color:#fff}.dark .head p{color:#fff}
.qs{display:grid;grid-template-columns:1fr 1fr;gap:14px;max-width:980px;margin:0 auto}
.q{display:flex;gap:14px;align-items:flex-start;background:var(--piedra);border:1px solid rgba(29,63,64,.1);border-radius:16px;padding:18px 20px}
.q i{flex:none;width:26px;height:26px;border-radius:50%;background:var(--tq);color:#1D3F40;font-style:normal;font-weight:800;display:flex;align-items:center;justify-content:center;font-size:.9rem;margin-top:1px}
.q p{text-align:left;font-size:.96rem;font-weight:400}
.mclose{max-width:780px;margin:30px auto 0;text-align:center;font-weight:600;color:var(--pet);font-size:1.08rem}
/* explicación */
.explain{background:var(--piedra)}
.explain .txt{max-width:820px;margin:0 auto}
.explain .txt p{margin-bottom:16px;font-size:1.02rem}
.explain .txt b{font-weight:600}
.quote{max-width:820px;margin:26px auto 0;border-left:4px solid var(--tq);background:#fff;border-radius:0 16px 16px 0;padding:18px 24px;font-weight:600;color:var(--pet);font-size:1.06rem}
/* tarjetas */
.cards{background:#fff}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.grid.g2{grid-template-columns:repeat(2,1fr)}
.card{background:var(--piedra);border:1px solid rgba(29,63,64,.12);border-radius:18px;padding:26px 24px;transition:.2s}
.card:hover{border-color:var(--tq);transform:translateY(-3px);box-shadow:0 24px 50px -30px rgba(29,63,64,.45)}
.card h3{color:var(--pet);font-size:1.12rem;margin:8px 0 10px;line-height:1.3}
.card p{font-size:.93rem;text-align:left}
.card ul{list-style:none;margin-top:10px}
.card li{position:relative;padding-left:22px;font-size:.9rem;margin-bottom:6px}
.card li::before{content:"✓";position:absolute;left:0;color:var(--tq);font-weight:700}
/* pasos */
.steps{background:var(--pet);color:#fff;position:relative}
.sgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:6px}
.sgrid.s4{grid-template-columns:repeat(4,1fr)}
.step{background:rgba(255,255,255,.04);border:1px solid rgba(12,191,194,.35);border-radius:18px;padding:28px 24px}
.num{width:46px;height:46px;border-radius:50%;background:var(--tq);color:#1D3F40;font-weight:800;font-size:1.3rem;display:flex;align-items:center;justify-content:center;margin-bottom:16px}
.step h3{font-size:1.06rem;line-height:1.3;margin-bottom:10px;color:#fff}
.step p{font-size:.92rem;color:rgba(255,255,255,.88);text-align:left}
.snote{max-width:820px;margin:30px auto 0;text-align:center;color:rgba(255,255,255,.85);font-size:.92rem}
/* profesional / ficha */
.pro{background:var(--piedra)}
.pcard{display:grid;grid-template-columns:1fr 1fr;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 24px 60px -34px rgba(29,63,64,.5);max-width:980px;margin:0 auto}
.pcard .l{background:linear-gradient(155deg,var(--pet),#22494a);color:#fff;padding:34px 32px}
.pcard .l h3{color:#fff;font-size:1.35rem;margin:10px 0 12px}
.pcard .l p{color:#fff;font-size:.95rem;text-align:left}
.pcard .r{padding:30px 30px}
.rows{list-style:none}
.rows li{display:flex;justify-content:space-between;gap:16px;padding:11px 0;border-bottom:1px solid rgba(29,63,64,.1);font-size:.92rem}
.rows li:last-child{border-bottom:none}
.rows li span{color:#1D3F40}.rows li b{color:var(--pet);font-weight:600;text-align:right}
.pcard .r .btn{margin-top:20px;width:100%}
/* evidencia */
.evid{background:#fff}
.ev{max-width:900px;margin:0 auto;display:grid;gap:12px}
.evi{display:grid;grid-template-columns:170px 1fr;gap:18px;align-items:start;background:var(--piedra);border-radius:14px;padding:16px 20px}
.evi .lv{font-size:.7rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#1D3F40;background:rgba(12,191,194,.18);border-radius:999px;padding:6px 12px;text-align:center}
.evi p{font-size:.93rem;text-align:left}
.refs{max-width:900px;margin:22px auto 0;font-size:.82rem;color:#1D3F40}
.refs p{text-align:left;margin-bottom:8px}.refs a{color:#0a8f91}
/* faq */
.faq{background:var(--piedra)}
.faq .list{max-width:860px;margin:0 auto}
.faq details{background:#fff;border:1px solid rgba(29,63,64,.1);border-radius:14px;margin-bottom:12px;padding:0 22px}
.faq summary{cursor:pointer;list-style:none;padding:18px 30px 18px 0;font-weight:600;color:var(--pet);position:relative}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";position:absolute;right:0;top:12px;font-size:1.6rem;color:var(--tq);font-weight:400}
.faq details[open] summary::after{content:"–"}
.faq details p{padding:0 0 18px;font-size:.95rem}
/* relacionadas */
.rel{background:#fff}
.rel a.card{text-decoration:none;color:inherit;display:block}
.rel .go{display:inline-block;margin-top:14px;color:#0a8f91;font-weight:600;font-size:.9rem}
/* aviso */
.note{background:#fff;padding:0 0 40px}
.note p{max-width:860px;margin:0 auto;font-size:.8rem;color:#1D3F40;opacity:.8;text-align:center}
/* cta */
.ctaband{background:var(--tq);color:#1D3F40;text-align:center}
.ctaband h2{color:#1D3F40;font-size:clamp(1.5rem,3.6vw,2.2rem)}
.ctaband p{max-width:58ch;margin:12px auto 0;color:#1D3F40;text-align:center}
.ctaband .btn-row{justify-content:center}
.ctaband .btn-gh{color:#1D3F40;border-color:#1D3F40}.ctaband .btn-gh:hover{background:#1D3F40;color:var(--tq)}
/* contacto */
.cont{background:var(--pet);color:#fff;text-align:center;position:relative}
.cont h2{color:#fff;font-size:clamp(1.5rem,3.4vw,2.1rem);margin-top:8px}
.cont p{color:#fff;max-width:56ch;margin:14px auto 22px;text-align:center}
.cont .datos{display:flex;flex-wrap:wrap;gap:8px 24px;justify-content:center;margin-bottom:24px;font-size:.98rem}
.foot{background:#1D3F40;color:rgba(242,241,238,.6);text-align:center;padding:24px 0;font-size:.8rem;border-top:1px solid rgba(255,255,255,.08)}
.foot a{color:rgba(242,241,238,.75)}
/* hub */
.hubgrp{margin-bottom:44px}
.hubgrp h2{color:var(--pet);font-size:1.5rem;margin:6px 0 18px}
.tag{display:inline-block;font-size:.66rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;background:var(--tq);color:#1D3F40;border-radius:999px;padding:3px 9px;margin-left:6px;vertical-align:middle}
/* partículas */
.hero,.steps,.cont{position:relative}
.fxcanvas{position:absolute;inset:0;width:100%;height:100%;z-index:0;pointer-events:none;opacity:.55}
.hero>*:not(canvas),.steps>*:not(canvas),.cont>*:not(canvas){position:relative;z-index:1}
@media (prefers-reduced-motion:reduce){.fxcanvas{display:none}}
@media(max-width:900px){
 .hero .wrap{grid-template-columns:1fr;gap:30px}
 .grid,.sgrid,.sgrid.s4{grid-template-columns:1fr 1fr}
 .topnav nav{display:none}
}
@media(max-width:640px){
 .wrap{padding:0 18px}
 section{padding:44px 0}
 .qs,.grid,.grid.g2,.sgrid,.sgrid.s4,.pcard{grid-template-columns:1fr}
 .evi{grid-template-columns:1fr;gap:8px}.evi .lv{justify-self:start}
 .btn-row .btn{width:100%}
 p{text-align:left}
}
"""

JS = """
<script>
(function(){
 if(window.matchMedia&&window.matchMedia('(prefers-reduced-motion:reduce)').matches)return;
 var TQ='12,191,194',items=[];
 Array.prototype.forEach.call(document.querySelectorAll('.hero,.steps,.cont'),function(sec){
   var cv=document.createElement('canvas');cv.className='fxcanvas';sec.insertBefore(cv,sec.firstChild);
   items.push({el:sec,cv:cv,ctx:cv.getContext('2d'),pts:null,w:0,h:0});});
 function init(o){var r=o.el.getBoundingClientRect();o.w=o.cv.width=Math.max(1,Math.round(r.width));o.h=o.cv.height=Math.max(1,Math.round(r.height));
   var n=Math.max(6,Math.min(42,Math.round(o.w*o.h/30000))),p=[];
   for(var i=0;i<n;i++)p.push({x:Math.random()*o.w,y:Math.random()*o.h,vx:(Math.random()-.5)*.26,vy:(Math.random()-.5)*.26,r:Math.random()*1.5+.8});o.pts=p;}
 function frame(){for(var m=0;m<items.length;m++){var o=items[m],rw=Math.round(o.el.getBoundingClientRect().width);
   if(!o.pts||o.cv.width!==rw)init(o);var ctx=o.ctx,p=o.pts,i,j;ctx.clearRect(0,0,o.w,o.h);
   for(i=0;i<p.length;i++){var a=p[i];a.x+=a.vx;a.y+=a.vy;if(a.x<0||a.x>o.w)a.vx*=-1;if(a.y<0||a.y>o.h)a.vy*=-1;
     for(j=i+1;j<p.length;j++){var b=p[j],dx=a.x-b.x,dy=a.y-b.y,d=dx*dx+dy*dy;
       if(d<16000){ctx.strokeStyle='rgba('+TQ+','+((1-d/16000)*.42).toFixed(3)+')';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke();}}}
   for(i=0;i<p.length;i++){var c=p[i];ctx.fillStyle='rgba('+TQ+',.7)';ctx.beginPath();ctx.arc(c.x,c.y,c.r,0,6.2832);ctx.fill();}}
   requestAnimationFrame(frame);}
 var to;window.addEventListener('resize',function(){clearTimeout(to);to=setTimeout(function(){items.forEach(function(o){o.pts=null;});},200);});
 requestAnimationFrame(frame);
})();
/* Dentro del iframe de Wix, los enlaces internos (#) hacen scroll y los externos abren arriba */
(function(){
 var embedded=(window.self!==window.top);
 document.addEventListener('click',function(e){var a=e.target.closest?e.target.closest('a'):null;if(!a)return;
   var h=a.getAttribute('href')||'';
   if(h.charAt(0)==='#'&&h.length>1){var el=document.querySelector(h);if(el){e.preventDefault();el.scrollIntoView({behavior:'smooth',block:'start'});}return;}
   if(embedded&&!a.target){a.target='_top';}
 },false);
})();
</script>
"""


def head(p):
    title = plain(p["title"])
    desc = plain(p["desc"])
    ld = schema(p)
    return f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url(p['slug']) if p['slug'] != 'index' else SITE['base']}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:type" content="website"><meta property="og:locale" content="es_ES">
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head><body>"""


def schema(p):
    org = {"@type": "MedicalClinic", "name": "WA LAM · Salud integrativa", "url": SITE["base"],
           "telephone": "+34 675 716 409", "email": SITE["email"],
           "address": {"@type": "PostalAddress", "addressLocality": "Barcelona",
                       "addressRegion": "Barcelona", "addressCountry": "ES",
                       "streetAddress": SITE["address"]},
           "areaServed": ["Sarrià-Sant Gervasi", "Barcelona"]}
    graph = []
    if p["group"] == "academia":
        graph.append({"@type": "Course", "name": plain(p["h1"]), "description": plain(p["desc"]),
                      "provider": {"@type": "Organization", "name": "WA LAM · Healthy Lifestyle Academy", "url": SITE["base"]},
                      "inLanguage": "es"})
    elif p["group"] == "home":
        graph.append(org)
    else:
        graph.append({"@type": "MedicalWebPage", "name": plain(p["h1"]), "description": plain(p["desc"]),
                      "url": url(p["slug"]), "inLanguage": "es", "about": plain(p.get("about", p["h1"])),
                      "publisher": org})
    if p.get("faq"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}}
            for q, a in p["faq"]]})
    return {"@context": "https://schema.org", "@graph": graph}


def nav(p):
    links = "".join(f'<a href="{url(GROUPS[g]["hub"])}">{GROUPS[g]["nav"]}</a>' for g in ("motivo", "servicio", "academia"))
    return f"""<header class="topnav"><div class="wrap"><a href="{SITE['base']}"><img src="{LOGO}" alt="WA LAM" style="height:30px;display:block"></a>
<nav>{links}<a href="#contacto">Contacto</a></nav></div></header>"""


def hero(p):
    g = GROUPS.get(p["group"])
    crumbs = ""
    if g:
        crumbs = f'<div class="crumbs"><a href="{SITE["base"]}">Inicio</a> › <a href="{url(g["hub"])}">{g["nav"]}</a> › {html.escape(plain(p["nav"]))}</div>'
    b1 = p.get("cta1", ("Escríbenos por WhatsApp", wa(p["wa"])))
    b2 = p.get("cta2", ("Reservar primera visita", SITE["booking"]))
    facts = "".join(f"<li>{fmt(f)}</li>" for f in p["facts"])
    return f"""<section class="hero"><div class="wrap">
<div>{crumbs}<span class="eyebrow">{fmt(p['eyebrow'])}</span><h1>{fmt(p['h1'])}</h1>
<div class="hs">{fmt(p['sub'])}</div><p class="lead">{fmt(p['lead'])}</p>
<div class="btn-row"><a class="btn btn-tq" href="{b1[1]}" target="_blank" rel="noopener">{b1[0]}</a><a class="btn btn-gh" href="{b2[1]}">{b2[0]}</a></div></div>
<aside class="hcard"><span class="k">{fmt(p.get('facts_title', 'En WA LAM'))}</span><ul>{facts}</ul></aside>
</div></section>"""


def sec_head(eyebrow, h2, intro=None):
    i = f"<p>{fmt(intro)}</p>" if intro else ""
    return f'<div class="head"><span class="eyebrow" style="justify-content:center">{fmt(eyebrow)}</span><h2>{fmt(h2)}</h2>{i}</div>'


def mirror(m):
    qs = "".join(f'<div class="q"><i>?</i><p>{fmt(q)}</p></div>' for q in m["qs"])
    close = f'<p class="mclose">{fmt(m["close"])}</p>' if m.get("close") else ""
    return f'<section class="mirror"><div class="wrap">{sec_head(m["eyebrow"], m["h2"], m.get("intro"))}<div class="qs">{qs}</div>{close}</div></section>'


def explain(e):
    ps = "".join(f"<p>{fmt(x)}</p>" for x in e["paras"])
    q = f'<div class="quote">{fmt(e["quote"])}</div>' if e.get("quote") else ""
    return f'<section class="explain"><div class="wrap">{sec_head(e["eyebrow"], e["h2"])}<div class="txt">{ps}</div>{q}</div></section>'


def cards(c, cls="cards"):
    items = []
    for it in c["items"]:
        k = f'<span class="k">{fmt(it["k"])}</span>' if it.get("k") else ""
        txt = f"<p>{fmt(it['p'])}</p>" if it.get("p") else ""
        li = "".join(f"<li>{fmt(x)}</li>" for x in it.get("li", []))
        li = f"<ul>{li}</ul>" if li else ""
        items.append(f'<div class="card">{k}<h3>{fmt(it["h"])}</h3>{txt}{li}</div>')
    g = "grid g2" if len(c["items"]) in (2, 4) else "grid"
    return f'<section class="{cls}"><div class="wrap">{sec_head(c["eyebrow"], c["h2"], c.get("intro"))}<div class="{g}">{"".join(items)}</div></div></section>'


def steps(s):
    its = "".join(f'<div class="step"><div class="num">{i+1}</div><h3>{fmt(h)}</h3><p>{fmt(t)}</p></div>' for i, (h, t) in enumerate(s["items"]))
    cls = "sgrid s4" if len(s["items"]) == 4 else "sgrid"
    note = f'<p class="snote">{fmt(s["note"])}</p>' if s.get("note") else ""
    return f'<section class="steps dark"><div class="wrap">{sec_head(s["eyebrow"], s["h2"], s.get("intro"))}<div class="{cls}">{its}</div>{note}</div></section>'


def pro(f, p):
    rows = "".join(f"<li><span>{fmt(a)}</span><b>{fmt(b)}</b></li>" for a, b in f["rows"])
    btn = f.get("btn", ("Reservar", SITE["booking"]))
    return f"""<section class="pro" id="ficha"><div class="wrap"><div class="pcard">
<div class="l"><span class="k">{fmt(f['k'])}</span><h3>{fmt(f['h'])}</h3><p>{fmt(f['p'])}</p></div>
<div class="r"><ul class="rows">{rows}</ul><a class="btn btn-tq" href="{btn[1]}" target="_blank" rel="noopener">{btn[0]}</a></div>
</div></div></section>"""


def evidence(e):
    its = "".join(f'<div class="evi"><span class="lv">{fmt(lv)}</span><p>{fmt(t)}</p></div>' for lv, t in e["items"])
    refs = ""
    if e.get("refs"):
        refs = '<div class="refs">' + "".join(
            f'<p>{fmt(r["t"])} DOI: <a href="https://doi.org/{r["doi"]}" target="_blank" rel="noopener">{r["doi"]}</a></p>' for r in e["refs"]) + "</div>"
    return f'<section class="evid"><div class="wrap">{sec_head(e.get("eyebrow", "Con honestidad"), e["h2"], e.get("intro"))}<div class="ev">{its}</div>{refs}</div></section>'


def faq(items):
    d = "".join(f"<details><summary>{fmt(q)}</summary><p>{fmt(a)}</p></details>" for q, a in items)
    return f'<section class="faq"><div class="wrap">{sec_head("Preguntas frecuentes", "Lo que suelen preguntarnos")}<div class="list">{d}</div></div></section>'


def related(slugs, h2="También puede interesarte"):
    cs = []
    for s in slugs:
        r = BYSLUG[s]
        cs.append(f'<a class="card" href="{url(s)}"><span class="k">{GROUPS[r["group"]]["label"]}</span><h3>{fmt(r["nav"])}</h3><p>{fmt(r["card"])}</p><span class="go">Ver página →</span></a>')
    g = "grid g2" if len(cs) in (2, 4) else "grid"
    return f'<section class="rel"><div class="wrap">{sec_head("Páginas relacionadas", h2)}<div class="{g}">{"".join(cs)}</div></div></section>'


def ctaband(p):
    c = p["cta"]
    b2 = c.get("b2", ("Reservar online", SITE["booking"]))
    return f"""<section class="ctaband"><div class="wrap"><h2>{fmt(c['h2'])}</h2><p>{fmt(c['p'])}</p>
<div class="btn-row"><a class="btn btn-dk" href="{wa(p['wa'])}" target="_blank" rel="noopener">Escríbenos por WhatsApp</a><a class="btn btn-gh" href="{b2[1]}">{b2[0]}</a></div></div></section>"""


def contact(p):
    return f"""<section class="cont" id="contacto"><div class="wrap">
<span class="eyebrow" style="justify-content:center">¿Tienes dudas?</span><h2>Estamos aquí para orientarte</h2>
<p>Cuéntanos brevemente qué te ocurre o qué te interesa y te diremos con sinceridad si podemos ayudarte y con qué profesional.</p>
<div class="datos"><span>📍 {fmt(SITE['address_short'])}</span><span>📧 {SITE['email']}</span><span>📞 +34 675 716 409</span></div>
<a class="btn btn-tq" href="{wa(p['wa'])}" target="_blank" rel="noopener">Escríbenos por WhatsApp</a>
</div></section>
<footer class="foot"><div class="wrap">WA LAM · Salud integrativa en Barcelona · Sarrià–Sant Gervasi · <a href="{SITE['base']}">walambcn.com</a></div></footer>"""


NOTE = ('<section class="note"><div class="wrap"><p>La información de esta página es orientativa y no sustituye la valoración '
        'ni el seguimiento de tu médico. Si tus síntomas son intensos, cambian de forma brusca o se acompañan de fiebre, pérdida de peso '
        'sin causa aparente, sangrado o pérdida de fuerza, consulta con tu médico o con urgencias.</p></div></section>')


def page(p):
    parts = [head(p), nav(p), hero(p)]
    for blk in p["blocks"]:
        t = blk["type"]
        if t == "mirror": parts.append(mirror(blk))
        elif t == "explain": parts.append(explain(blk))
        elif t == "cards": parts.append(cards(blk))
        elif t == "steps": parts.append(steps(blk))
        elif t == "pro": parts.append(pro(blk, p))
        elif t == "evidence": parts.append(evidence(blk))
        elif t == "hubcards": parts.append(hubcards(blk))
    if p.get("faq"): parts.append(faq(p["faq"]))
    if p.get("related"): parts.append(related(p["related"]))
    parts.append(ctaband(p))
    if p["group"] in ("motivo", "servicio"): parts.append(NOTE)
    parts.append(contact(p))
    parts.append(JS + "</body></html>")
    return "\n".join(parts)


def hubcards(b):
    out = []
    for g in b["groups"]:
        G = GROUPS[g]
        cs = "".join(
            f'<a class="card" href="{url(x["slug"])}"><span class="k">{G["label"]}</span><h3>{fmt(x["nav"])}</h3><p>{fmt(x["card"])}</p><span class="go">Ver página →</span></a>'
            for x in PAGES if x["group"] == g)
        out.append(f'<section class="rel" id="{G["hub"]}"><div class="wrap">{sec_head(G["eyebrow"], G["title"], G["intro"])}<div class="grid">{cs}</div></div></section>')
    return "\n".join(out)


def main():
    for p in PAGES:
        (OUT / f"{p['slug']}.html").write_text(page(p), encoding="utf-8")
    # índice de revisión para WA LAM (no es para publicar)
    rows = []
    for g in ("home", "motivo", "servicio", "academia"):
        G = GROUPS[g]
        cs = "".join(
            f'<a class="card" href="{x["slug"]}.html" target="_self"><span class="k">/{x["slug"]}</span><h3>{fmt(x["nav"])}'
            f'{"<span class=tag>1ª tanda</span>" if x.get("wave") == 1 else ""}</h3><p>{fmt(x["card"])}</p></a>'
            for x in PAGES if x["group"] == g)
        rows.append(f'<div class="hubgrp"><span class="k">{G["label"]}</span><h2>{G["title"]}</h2><div class="grid">{cs}</div></div>')
    idx = {"slug": "index", "group": "home", "title": "WA LAM · Landing pages (revisión)", "desc": "Índice interno de revisión.", "h1": "", "faq": []}
    doc = head(idx) + nav(idx) + f"""<section class="hero"><div class="wrap" style="grid-template-columns:1fr"><div>
<span class="eyebrow">Revisión interna</span><h1>Landing pages WA LAM</h1><p class="lead">{len(PAGES)} páginas con el estilo de la landing de formación. Lo resaltado así: <span class="pend">dato pendiente</span> hay que completarlo antes de publicar.</p></div></div></section>
<section style="background:#fff"><div class="wrap">{''.join(rows)}</div></section>""" + JS + "</body></html>"
    (OUT / "index.html").write_text(doc, encoding="utf-8")
    print(f"{len(PAGES)} páginas + index.html en {OUT}")


if __name__ == "__main__":
    main()
