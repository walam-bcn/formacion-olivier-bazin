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
from landings_content import PAGES, GROUPS, SITE, R  # noqa: E402
from seo_map import SEO, BARRIOS, URLS, CA_SLUG  # noqa: E402
from urllib.parse import quote as _q

SITE.setdefault("cv_url", "https://www.walambcn.com/curriculum")
SITE.setdefault("og_base", "https://walam-bcn.github.io/formacion-olivier-bazin/landings/og/")
SITE.setdefault("updated", "2026-11-18")
SITE.setdefault("updated_txt", "18 de noviembre de 2026")
# Rellenar cuando se confirme: activa reviewedBy en los datos estructurados
SITE.setdefault("reviewer", None)  # p. ej. {"name": "Nombre Apellido", "title": "Fisioterapeuta y osteópata", "license": "Col. nº 0000"}
PREVIEW = "--preview" in sys.argv
LANG = "ca" if "--ca" in sys.argv else "es"
CA = {}
if LANG == "ca":
    CA = json.loads((ROOT / "tools" / "i18n_ca.json").read_text(encoding="utf-8"))


def tr(t):
    if LANG != "ca":
        return t
    return CA.get(t, t)


SKIP_KEYS = {"slug", "type", "group", "related", "refs", "wave", "doi"}


def tr_deep(o, key=None):
    if key in SKIP_KEYS:
        return o
    if isinstance(o, str):
        return tr(o)
    if isinstance(o, list):
        return [tr_deep(x) for x in o]
    if isinstance(o, tuple):
        return tuple(tr_deep(x) for x in o)
    if isinstance(o, dict):
        return {k: tr_deep(v, k) for k, v in o.items()}
    return o

LOGO = (ROOT / "tools" / "logo.b64").read_text().strip()
OUT = ROOT / "landings"
OUT.mkdir(exist_ok=True)
BYSLUG = {p["slug"]: p for p in PAGES}


LINK_RE = re.compile(r"(?<!\[)\[([^\[\]]+)\]\(([A-Za-z0-9#:/._\-]+)\)")


def fmt(s):
    """Escapa y convierte **negrita**, *turquesa*, [texto](slug) y [[pendiente]]."""
    s = html.escape(s, quote=False)
    s = LINK_RE.sub(lambda m: f'<a class="inl" href="{m.group(2) if m.group(2).startswith(("http", "#")) else url(m.group(2))}">{m.group(1)}</a>', s)
    s = re.sub(r"\[\[(.+?)\]\]", r'<span class="pend">\1</span>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r'<span class="tq">\1</span>', s)
    return s


def plain(s):
    s = LINK_RE.sub(lambda m: m.group(1), s)
    return re.sub(r"\[\[|\]\]|\*", "", s)


def url(slug):
    if PREVIEW:
        if slug in ("", "tratamientos", "healthy-lifestyle-academy"):
            return "index.html" if LANG == "ca" else "./"
        return f"{slug}.html"
    return canon(slug)


def wixpath(slug):
    path = URLS.get(slug, slug)
    if LANG == "ca" and slug in URLS:
        parts = path.split("/") if path else []
        if slug in CA_SLUG:
            parts[-1] = CA_SLUG[slug]
        CA_HUB = {"tratamientos-sarrià-sant-gervasi-barcelona": "tractaments-sarria-sant-gervasi-barcelona",
                  "academia-vida-saludable-barcelona": "academia-vida-saludable-barcelona"}
        if parts:
            parts[0] = CA_HUB.get(parts[0], parts[0])
        path = "ca" + ("/" + "/".join(parts) if parts else "")
    return path


def canon_lang(slug, lang):
    global LANG
    old, LANG = LANG, lang
    try:
        return canon(slug)
    finally:
        LANG = old


def canon(slug):
    path = wixpath(slug)
    return f"{SITE['base']}/{_q(path, safe='/')}" if path else SITE["base"]


def slugify(t):
    import unicodedata
    t = unicodedata.normalize("NFKD", plain(t)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:48]


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
/* SEO: firma, resumen, índice, local */
.byline{background:#163536;color:rgba(255,255,255,.85);font-size:.8rem;padding:10px 0}
.byline .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;gap:6px 20px}
.byline a{color:var(--tq)}
.quick{background:#fff;padding:40px 0 10px}
.qbox{max-width:900px;margin:0 auto;border:1px solid rgba(12,191,194,.45);border-left:5px solid var(--tq);border-radius:0 18px 18px 0;padding:22px 26px;background:linear-gradient(90deg,rgba(12,191,194,.08),#fff)}
.qbox h2{color:var(--pet);font-size:1.25rem;margin:6px 0 8px}
.qbox p{font-size:1rem;text-align:left}
.toc{background:#fff;padding:18px 0 6px}
.toc .wrap{max-width:900px}
.toc .chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}
.toc a{font-size:.8rem;font-weight:500;color:var(--pet);text-decoration:none;background:var(--piedra);border:1px solid rgba(29,63,64,.12);border-radius:999px;padding:6px 13px}
.toc a:hover{border-color:var(--tq);color:#0a8f91}
a.inl{color:#0a8f91;font-weight:600;text-decoration:underline;text-underline-offset:3px}
.dark a.inl,.hero a.inl{color:var(--tq)}
.localsec{background:#fff}
.localsec .card:hover{transform:none}
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
   if(embedded&&!a.target&&/^https?:/.test(h)){a.target='_top';}
 },false);
})();
</script>
"""


def seo(p):
    return SEO.get(p["slug"], {})


def head(p):
    S = seo(p)
    title = plain(S.get("title", p["title"]))
    desc = plain(S.get("desc", p["desc"]))
    ld = schema(p)
    can = canon(p["slug"]) if p["slug"] != "index" else SITE["base"]
    og = SITE["og_base"] + p["slug"] + ".png"
    robots = "noindex,nofollow" if p["slug"] in ("index", "guia-seo") else "index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1"
    return f"""<!DOCTYPE html><html lang="{"ca-ES" if LANG == "ca" else "es-ES"}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{can}">
<link rel="alternate" hreflang="es-ES" href="{canon_lang(p['slug'], 'es')}"><link rel="alternate" hreflang="ca-ES" href="{canon_lang(p['slug'], 'ca')}"><link rel="alternate" hreflang="x-default" href="{canon_lang(p['slug'], 'es')}">
<meta name="geo.region" content="ES-CT"><meta name="geo.placename" content="Barcelona, Sarrià-Sant Gervasi">
<meta name="author" content="WA LAM · Salud integrativa"><meta name="theme-color" content="#1D3F40">
<meta property="og:type" content="website"><meta property="og:locale" content="{"ca_ES" if LANG == "ca" else "es_ES"}"><meta property="og:site_name" content="WA LAM">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{can}"><meta property="og:image" content="{og}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{html.escape(plain(p.get('h1') or title))} · WA LAM">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{html.escape(title)}"><meta name="twitter:description" content="{html.escape(desc)}"><meta name="twitter:image" content="{og}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head><body>"""


def page_refs(p):
    out, seen = [], set()
    for b in p.get("blocks", []):
        for r in b.get("refs", []):
            if r["doi"] not in seen:
                seen.add(r["doi"]); out.append(r)
    return out


def schema(p):
    if p["slug"] in ("index", "guia-seo"):
        return {"@context": "https://schema.org", "@type": "WebPage", "name": plain(p.get("title", ""))}
    S = seo(p)
    clinic_id = SITE["base"] + "/#clinica"
    org = {"@type": ["MedicalClinic", "MedicalBusiness"], "@id": clinic_id, "name": "WA LAM · Salud integrativa",
           "url": SITE["base"], "telephone": "+34675716409", "email": SITE["email"],
           "image": SITE["og_base"] + "medicina-integrativa-barcelona.png", "priceRange": "€€",
           "address": {"@type": "PostalAddress", "streetAddress": "Carrer del Bisbe Sivilla, 44, local", "postalCode": SITE["postal"],
                       "addressLocality": "Barcelona", "addressRegion": "Cataluña", "addressCountry": "ES"},
           "openingHours": SITE["opening"], "founder": {"@type": "Person", "name": SITE.get("owner", "Rosa"), "url": SITE["cv_url"]}, "foundingDate": "2004",
           "areaServed": [{"@type": "Place", "name": f"{b}, Barcelona"} for b in BARRIOS] + [{"@type": "City", "name": "Barcelona"}],
           "medicalSpecialty": ["Physiotherapy", "Musculoskeletal"],
           "availableService": [{"@type": "MedicalTherapy", "name": plain(x["nav"]), "url": canon(x["slug"])} for x in PAGES if x["group"] == "servicio"],
           "sameAs": SITE.get("same_as", [])}
    g = GROUPS.get(p["group"], {})
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE["base"]}]
    if p["group"] != "home":
        crumbs.append({"@type": "ListItem", "position": 2, "name": g["nav"], "item": canon(g["hub"])})
        crumbs.append({"@type": "ListItem", "position": 3, "name": plain(p["nav"]), "item": canon(p["slug"])})
    graph = [org, {"@type": "BreadcrumbList", "@id": canon(p["slug"]) + "#breadcrumb", "itemListElement": crumbs}]
    webpage = {"@type": "MedicalWebPage" if p["group"] in ("motivo", "servicio", "home") else "WebPage",
               "@id": canon(p["slug"]) + "#webpage", "url": canon(p["slug"]), "name": plain(S.get("title", p["title"])),
               "description": plain(S.get("desc", p["desc"])), "inLanguage": "ca-ES" if LANG == "ca" else "es-ES",
               "isPartOf": {"@type": "WebSite", "name": "WA LAM", "url": SITE["base"]},
               "breadcrumb": {"@id": canon(p["slug"]) + "#breadcrumb"}, "publisher": {"@id": clinic_id},
               "lastReviewed": SITE["updated"], "dateModified": SITE["updated"],
               "keywords": ", ".join([S.get("kw", "")] + S.get("kws", [])),
               "primaryImageOfPage": SITE["og_base"] + p["slug"] + ".png",
               "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".quick p", "h1"]}}
    if p["group"] in ("motivo", "servicio"):
        webpage["audience"] = {"@type": "Patient"}
    if SITE.get("reviewer"):
        rv = SITE["reviewer"]
        webpage["reviewedBy"] = {"@type": "Person", "name": rv["name"], "jobTitle": rv.get("title", ""), "worksFor": {"@id": clinic_id}}
    if S.get("entity"):
        t, n = S["entity"]
        webpage["about"] = {"@type": t, "name": n}
        if t == "MedicalCondition":
            webpage["about"]["possibleTreatment"] = [{"@type": "MedicalTherapy", "name": plain(BYSLUG[r]["nav"])} for r in p.get("related", []) if BYSLUG[r]["group"] == "servicio"]
    refs = page_refs(p)
    if refs:
        webpage["citation"] = [{"@type": "ScholarlyArticle", "name": r["t"].split("«")[-1].split("»")[0] if "«" in r["t"] else r["t"],
                                "url": "https://doi.org/" + r["doi"], "sameAs": "https://doi.org/" + r["doi"]} for r in refs]
    graph.append(webpage)
    if p["group"] == "servicio":
        graph.append({"@type": "Service", "@id": canon(p["slug"]) + "#servicio", "name": plain(p["h1"]), "serviceType": plain(p["nav"]),
                      "provider": {"@id": clinic_id}, "areaServed": org["areaServed"], "url": canon(p["slug"]),
                      "description": plain(S.get("desc", p["desc"]))})
    if p["group"] == "academia":
        graph.append({"@type": "Course", "@id": canon(p["slug"]) + "#curso", "name": plain(p["h1"]), "description": plain(S.get("desc", p["desc"])),
                      "provider": {"@type": "Organization", "name": "WA LAM · Healthy Lifestyle Academy", "url": SITE["base"]},
                      "inLanguage": "es", "url": canon(p["slug"])})
    if p.get("faq"):
        graph.append({"@type": "FAQPage", "@id": canon(p["slug"]) + "#faq", "mainEntity": [
            {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}}
            for q, a in p["faq"] if "[[" not in a]})
    return {"@context": "https://schema.org", "@graph": graph}


def nav(p):
    links = "".join(f'<a href="{url(GROUPS[g]["hub"])}">{GROUPS[g]["nav"]}</a>' for g in ("motivo", "servicio", "academia"))
    return f"""<header class="topnav"><div class="wrap"><a href="{url('')}"><img src="{LOGO}" alt="WA LAM" style="height:30px;display:block"></a>
<nav>{links}<a href="#contacto">{tr("Contacto")}</a>{langlink(p)}</nav></div></header>"""


def langlink(p):
    slug = p.get("slug", "")
    if slug in ("guia-seo",):
        return ""
    target = "es" if LANG == "ca" else "ca"
    if PREVIEW:
        href = (f"../{slug}.html" if LANG == "ca" else f"ca/{slug}.html")
    else:
        href = canon_lang(slug, target) if slug != "index" else (SITE["base"] + ("/ca" if target == "ca" else ""))
    return f'<a href="{href}" hreflang="{target}" style="font-weight:700;color:var(--tq)">{"Castellano" if LANG == "ca" else "Català"}</a>'


def hero(p):
    g = GROUPS.get(p["group"])
    crumbs = ""
    if g and p["group"] != "home":
        crumbs = f'<div class="crumbs"><a href="{url("")}">{tr("Inicio")}</a> › <a href="{url(g["hub"])}">{g["nav"]}</a> › {html.escape(plain(p["nav"]))}</div>'
    b1 = p.get("cta1", (tr("Escríbenos por WhatsApp"), wa(p["wa"])))
    b2 = p.get("cta2", (tr("Reservar primera visita"), wa(tr("Hola, me gustaría reservar una primera visita."))))
    if not b2[1].startswith(("http", "#", "[[")):
        b2 = (b2[0], url(b2[1]))
    facts = "".join(f"<li>{fmt(f)}</li>" for f in p["facts"])
    return f"""<section class="hero"><div class="wrap">
<div>{crumbs}<span class="eyebrow">{fmt(p['eyebrow'])}</span><h1>{fmt(p['h1'])}</h1>
<div class="hs">{fmt(p['sub'])}</div><p class="lead">{fmt(p['lead'])}</p>
<div class="btn-row"><a class="btn btn-tq" href="{b1[1]}" target="_blank" rel="noopener">{b1[0]}</a><a class="btn btn-gh" href="{b2[1]}">{b2[0]}</a></div></div>
<aside class="hcard"><span class="k">{fmt(p.get('facts_title', tr('En WA LAM')))}</span><ul>{facts}</ul></aside>
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


def pack(b):
    its = b["items"]; h = (len(its) + 1) // 2
    col = lambda xs: "<ul>" + "".join(f"<li>{fmt(x)}</li>" for x in xs) + "</ul>"
    extra = "".join(f'<p style="margin-top:14px;font-size:.92rem"><b>{fmt(k)}:</b> {fmt(v)}</p>' for k, v in b.get("notes", []))
    btn = f'<div class="btn-row"><a class="btn btn-tq" href="{wa(b["wa"])}" target="_blank" rel="noopener">{tr("Solicitar información")}</a></div>'
    return (f'<section class="cards"><div class="wrap">{sec_head(b["eyebrow"], b["h2"], b.get("intro"))}'
            f'<div class="grid g2"><div class="card"><span class="k">{tr("Incluye")}</span>{col(its[:h])}</div>'
            f'<div class="card"><span class="k">{tr("Incluye")}</span>{col(its[h:])}</div></div>'
            f'<div style="max-width:820px;margin:0 auto;text-align:center">{extra}</div>{btn}</div></section>')


def steps(s):
    its = "".join(f'<div class="step"><div class="num">{i+1}</div><h3>{fmt(h)}</h3><p>{fmt(t)}</p></div>' for i, (h, t) in enumerate(s["items"]))
    cls = "sgrid s4" if len(s["items"]) == 4 else "sgrid"
    note = f'<p class="snote">{fmt(s["note"])}</p>' if s.get("note") else ""
    return f'<section class="steps dark"><div class="wrap">{sec_head(s["eyebrow"], s["h2"], s.get("intro"))}<div class="{cls}">{its}</div>{note}</div></section>'


def pro(f, p):
    rows = "".join(f"<li><span>{fmt(a)}</span><b>{fmt(b)}</b></li>" for a, b in f["rows"])
    btn = f.get("btn", (tr("Reservar por WhatsApp"), wa(p["wa"])))
    who = p.get("pro_who", "")
    cv = f'<p style="margin-top:14px"><b>{tr("Quién te atiende")}:</b> {fmt(who)}<br><a class="inl" href="{SITE["cv_url"]}">{tr("Ver currículum")}</a></p>' if who else ""
    return f"""<section class="pro" id="ficha"><div class="wrap"><div class="pcard">
<div class="l"><span class="k">{fmt(f['k'])}</span><h3>{fmt(f['h'])}</h3><p>{fmt(f['p'])}</p>{cv}</div>
<div class="r"><ul class="rows">{rows}</ul><a class="btn btn-tq" href="{btn[1]}" target="_blank" rel="noopener">{btn[0]}</a></div>
</div></div></section>"""


def evidence(e):
    its = "".join(f'<div class="evi"><span class="lv">{fmt(lv)}</span><p>{fmt(t)}</p></div>' for lv, t in e["items"])
    refs = ""
    if e.get("refs"):
        refs = '<div class="refs">' + "".join(
            f'<p>{fmt(r["t"])} DOI: <a href="https://doi.org/{r["doi"]}" target="_blank" rel="noopener">{r["doi"]}</a></p>' for r in e["refs"]) + "</div>"
    return f'<section class="evid"><div class="wrap">{sec_head(e.get("eyebrow", tr("Con honestidad")), e["h2"], e.get("intro"))}<div class="ev">{its}</div>{refs}</div></section>'


def faq(items):
    d = "".join(f"<details><summary>{fmt(q)}</summary><p>{fmt(a)}</p></details>" for q, a in items)
    return f'<section class="faq" id="preguntas-frecuentes"><div class="wrap">{sec_head(tr("Preguntas frecuentes"), tr("Lo que suelen preguntarnos"))}<div class="list">{d}</div></div></section>'


def related(slugs, h2=None):
    h2 = h2 or tr("También puede interesarte")
    cs = []
    for s in slugs:
        r = BYSLUG[s]
        cs.append(f'<a class="card" href="{url(s)}"><span class="k">{GROUPS[r["group"]]["label"]}</span><h3>{fmt(r["nav"])}</h3><p>{fmt(r["card"])}</p><span class="go">{tr("Ver página →")}</span></a>')
    g = "grid g2" if len(cs) in (2, 4) else "grid"
    return f'<section class="rel"><div class="wrap">{sec_head(tr("Páginas relacionadas"), h2)}<div class="{g}">{"".join(cs)}</div></div></section>'


def ctaband(p):
    c = p["cta"]
    b2 = c.get("b2", (tr("Llamar al 675 716 409"), "tel:+34675716409"))
    return f"""<section class="ctaband"><div class="wrap"><h2>{fmt(c['h2'])}</h2><p>{fmt(c['p'])}</p>
<div class="btn-row"><a class="btn btn-dk" href="{wa(p['wa'])}" target="_blank" rel="noopener">{tr("Escríbenos por WhatsApp")}</a><a class="btn btn-gh" href="{b2[1]}">{b2[0]}</a></div></div></section>"""


def contact(p):
    return f"""<section class="cont" id="contacto"><div class="wrap">
<span class="eyebrow" style="justify-content:center">{tr("¿Tienes dudas?")}</span><h2>{tr("Estamos aquí para orientarte")}</h2>
<p>{tr("Cuéntanos brevemente qué te ocurre o qué te interesa y te diremos con sinceridad si podemos ayudarte y con qué profesional.")}</p>
<div class="datos"><span>📍 {fmt(SITE['address_short'])}</span><span>📧 {SITE['email']}</span><span>📞 +34 675 716 409</span></div>
<a class="btn btn-tq" href="{wa(p['wa'])}" target="_blank" rel="noopener">{tr("Escríbenos por WhatsApp")}</a>
</div></section>
<footer class="foot"><div class="wrap">WA LAM · {tr("Salud integrativa en Barcelona")} · Sarrià–Sant Gervasi · <a href="{url('')}">walambcn.com</a></div></footer>"""


NOTE_ES = ('La información de esta página es orientativa y no sustituye la valoración '
           'ni el seguimiento de tu médico. Si tus síntomas son intensos, cambian de forma brusca o se acompañan de fiebre, pérdida de peso '
           'sin causa aparente, sangrado o pérdida de fuerza, consulta con tu médico o con urgencias.')


def note():
    return f'<section class="note"><div class="wrap"><p>{tr(NOTE_ES)}</p></div></section>'


def byline(p):
    n = len(page_refs(p))
    who = fmt(SITE["reviewer_md"])
    cv = f' · <a href="{SITE["cv_url"]}">{tr("Ver currículum")}</a>'
    refs = f' · <a href="#{slugify(evid_title(p))}">{n} {tr("referencias científicas")}</a>' if n else ""
    return (f'<div class="byline"><div class="wrap"><span>✔ {tr("Contenido revisado por")} {who}{cv}</span>'
            f'<span>{tr("Actualizado")}: <time datetime="{SITE["updated"]}">{tr(SITE["updated_txt"])}</time>{refs}</span></div></div>')


def evid_title(p):
    for b in p["blocks"]:
        if b["type"] == "evidence":
            return b.get("_id") or b["h2"]
    return ""


def quick(p):
    q = seo(p).get("quick")
    if not q:
        return ""
    return (f'<section class="quick" id="en-resumen"><div class="wrap"><div class="qbox"><span class="k">{tr("En resumen")}</span>'
            f'<h2>{fmt(seo(p).get("q_title", p["nav"]))}</h2><p>{fmt(q)}</p></div></div></section>')


def toc(items):
    if len(items) < 3:
        return ""
    lis = "".join(f'<a href="#{i}">{html.escape(t)}</a>' for i, t in items)
    return f'<nav class="toc" aria-label="{tr('En esta página')}"><div class="wrap"><span class="k">{tr('En esta página')}</span><div class="chips">{lis}</div></div></nav>'


def local(p):
    barrios = ", ".join(BARRIOS[:-1]) + f" {tr('y')} " + BARRIOS[-1]
    what = plain(p["nav"])
    return f"""<section class="localsec" id="donde-estamos"><div class="wrap">{sec_head(tr("Dónde estamos"), f"{what} · {tr('cerca de ti, en Sarrià–Sant Gervasi')}")}
<div class="grid g2"><div class="card"><span class="k">{tr("Consulta presencial")}</span><h3>WA LAM · {html.escape(SITE['street'])}, {SITE['postal']} Barcelona</h3>

<ul><li>{tr("Dirección")}: {html.escape(SITE['street'])}, {SITE['postal']} Barcelona</li><li>{tr("Horario")}: {tr(SITE['hours'])}</li><li>{tr("Teléfono y WhatsApp")}: +34 675 716 409</li></ul></div>
<div class="card"><span class="k">{tr("Reserva")}</span><h3>{tr("Quién te atiende")}</h3>
<p>{fmt(p.get("pro_who", "").rstrip("."))}. <a class="inl" href="{SITE['cv_url']}">{tr("Ver currículum")}</a></p>
<p>{tr("La reserva se realiza por WhatsApp y el pago, mediante Bizum. Si no sabes qué servicio te conviene, cuéntanos tu caso y te orientamos antes de reservar.")}</p>
<div class="btn-row"><a class="btn btn-tq" href="{wa(p['wa'])}" target="_blank" rel="noopener">WhatsApp</a><a class="btn btn-gh" href="tel:+34675716409">{tr("Llamar")}</a></div></div></div></div></section>"""


def page(p):
    parts = [head(p), nav(p), hero(p), byline(p) if p["group"] != "home" or True else ""]
    body, items = [], []
    for blk in p["blocks"]:
        t = blk["type"]
        h = {"mirror": mirror, "explain": explain, "cards": cards, "steps": steps, "evidence": evidence, "hubcards": hubcards, "pack": pack}.get(t)
        if t == "pro":
            out = pro(blk, p); sid = "ficha"; label = tr("Ficha y reserva")
        else:
            out = h(blk); sid = blk.get("_id") or slugify(blk.get("h2", t)); label = plain(blk.get("eyebrow", blk.get("h2", "")))
            if t != "hubcards":
                out = out.replace('<section class="', f'<section id="{sid}" class="', 1)
        if t != "hubcards":
            items.append((sid, label if t != "evidence" else tr("Evidencia científica")))
        body.append(out)
    if p["group"] in ("motivo", "servicio"):
        body.append(local(p)); items.append(("donde-estamos", tr("Dónde estamos")))
    if p.get("faq"):
        body.append(faq(p["faq"])); items.append(("preguntas-frecuentes", tr("Preguntas frecuentes")))
    parts += [quick(p), toc(items)] + body
    if p.get("related"): parts.append(related(p["related"]))
    parts.append(ctaband(p))
    if p["group"] in ("motivo", "servicio"): parts.append(note())
    parts.append(contact(p))
    parts.append(JS + "</body></html>")
    return "\n".join(x for x in parts if x)


def hubcards(b):
    out = []
    for g in b["groups"]:
        G = GROUPS[g]
        cs = "".join(
            f'<a class="card" href="{url(x["slug"])}"><span class="k">{G["label"]}</span><h3>{fmt(x["nav"])}</h3><p>{fmt(x["card"])}</p><span class="go">{tr("Ver página →")}</span></a>'
            for x in PAGES if x["group"] == g)
        out.append(f'<section class="rel" id="{ {"motivo": "motivos", "servicio": "servicios", "academia": "academia"}[g]}"><div class="wrap">{sec_head(G["eyebrow"], G["title"], G["intro"])}<div class="grid">{cs}</div></div></section>')
    return "\n".join(out)


def _pending(p):
    out = []
    for m in re.findall(r"\[\[(.+?)\]\]", json.dumps(p, ensure_ascii=False)):
        if m not in out:
            out.append(m)
    return out


def _links_out(p):
    found = re.findall(r"\]\(([a-z0-9\-]+)\)", json.dumps(p, ensure_ascii=False))
    return list(dict.fromkeys(found + p.get("related", [])))


def _wixurl(slug, lang="es"):
    return canon_lang(slug, lang).replace(SITE["base"], "") or "/"


def guide():
    from seo_plan import RESEARCH, AI_PROMPTS, OFFPAGE, MEASURE, GOAL, ASK, OBS_NOTE, VISIBILITY
    from seo_map import EXISTING, REDIRECTS, BOOKING, BLOG
    from urllib.parse import unquote
    inl = {x["slug"]: [] for x in PAGES}
    for x in PAGES:
        for t in _links_out(x):
            if t in inl and x["slug"] not in inl[t]:
                inl[t].append(x["slug"])
    st = lambda k: f'<span class="st st-{k}">{k}</span>'
    def lab(slug):
        return html.escape(plain(BYSLUG[slug]["nav"])) if slug in BYSLUG else slug
    # 1 investigación
    r1 = "".join(f"<tr><td><b>{lab(x['slug'])}</b></td><td>{html.escape(RESEARCH[x['slug']][0])}</td><td>{'<br>'.join(html.escape(t) for t in RESEARCH[x['slug']][1])}</td><td>{'<br>'.join(html.escape(t) for t in RESEARCH[x['slug']][2])}</td><td><span class='tag2'>OBS</span> {html.escape(RESEARCH[x['slug']][3])}</td><td><span class='tag2'>VOL</span> no disponible</td></tr>" for x in PAGES)
    # 2 mapa
    def hub(x):
        return "Tratamientos" if x["group"] in ("motivo", "servicio") else ("Healthy Lifestyle Academy" if x["group"] == "academia" else "Menú principal")
    r2 = []
    for x in PAGES:
        sl = x["slug"]; S = SEO[sl]
        src = [hub(x)] + [lab(t) for t in inl[sl]] + [f"Magazín: {html.escape(unquote(b))}" for b in BLOG.get(sl, [])] + ([f"Página de reserva {html.escape(unquote(BOOKING[sl]))} (añadir enlace)"] if sl in BOOKING else [])
        dst = [lab(t) for t in x.get("related", [])] + ["Botón: " + ("Inscripción" if x["group"] == "academia" else "WhatsApp / Reservar")]
        r2.append(f"<tr><td><b>{html.escape(S['kw'])}</b><br><small>{html.escape(S['ca'])}</small></td><td><b>{lab(sl)}</b><br><code>{html.escape(unquote(_wixurl(sl)))}</code><br>{'<span class=tag2>REUTILIZA</span>' if sl in EXISTING else '<span class=tag2>NUEVA</span>'}<br><small>CA: <code>{html.escape(unquote(_wixurl(sl, 'ca')))}</code></small></td><td>{'<br>'.join(src)}</td><td>{'<br>'.join(dst)}</td></tr>")
    red = "".join(f"<li><code>{html.escape(a)}</code> → <code>{html.escape(b)}</code>: {html.escape(c)}</li>" for a, b, c in REDIRECTS)
    # 3 contenido propio
    r3 = []
    for x in PAGES:
        pend = _pending(x)
        has_steps = any(b["type"] == "steps" for b in x["blocks"])
        r3.append(f"<tr><td><b>{lab(x['slug'])}</b></td><td>{fmt(x.get('pro_who', ''))}</td><td>{'Sí' if has_steps else 'En la ficha'}</td><td>{html.escape(SITE['street'])} (presencial) {'· formato de cada edición' if x['group'] == 'academia' else ''}</td><td>{'Inscripción' if x['group'] == 'academia' else 'WhatsApp y reserva online'}</td><td>{'Sí: «Qué dice la evidencia» separado de «Lo que ofrecemos»' if any(b['type'] == 'evidence' for b in x['blocks']) else 'Sin bloque de evidencia (servicio de bienestar o formación)'}</td><td><b>{len(pend)}</b><br><small>{html.escape(' · '.join(pend[:6]))}{' …' if len(pend) > 6 else ''}</small></td></tr>")
    # 4 fichas Wix
    cards = []
    for x in PAGES:
        sl = x["slug"]; S = SEO[sl]
        types = {"home": "Datos de empresa de Wix (LocalBusiness) completados + WebSite. No duplicar con un segundo MedicalClinic.",
                 "motivo": "MedicalWebPage (con about: MedicalCondition), BreadcrumbList, FAQPage",
                 "servicio": "MedicalWebPage, Service, BreadcrumbList, FAQPage",
                 "academia": "Course, BreadcrumbList, FAQPage; Event en cada edición (ya lo genera Wix Eventos)"}[x["group"]]
        btn = plain(x.get("cta1", (tr("Escríbenos por WhatsApp"), ""))[0])
        cards.append(f"""<details class="wix"><summary><b>{lab(sl)}</b> <code>{html.escape(unquote(_wixurl(sl)))}</code></summary>
<table class="kv"><tr><th>URL (ES)</th><td><code>{html.escape(unquote(_wixurl(sl)))}</code> {'(ya existe)' if sl in EXISTING else '(crear)'}</td></tr>
<tr><th>URL (CA)</th><td><code>{html.escape(unquote(_wixurl(sl, 'ca')))}</code> (Wix Multilingual)</td></tr>
<tr><th>Título SEO</th><td>{html.escape(S['title'])} <small>({len(S['title'])} car.)</small></td></tr>
<tr><th>Metadescripción</th><td>{html.escape(S['desc'])} <small>({len(S['desc'])} car.)</small></td></tr>
<tr><th>Encabezado H1</th><td>{html.escape(plain(x['h1']))}</td></tr>
<tr><th>Enlaces internos que salen</th><td>{html.escape(', '.join(lab(t) for t in _links_out(x)))}</td></tr>
<tr><th>Enlaces que recibe</th><td>{html.escape(', '.join([lab(t) for t in inl[sl]] + [unquote(b) for b in BLOG.get(sl, [])]))}</td></tr>
<tr><th>Botón principal</th><td>{html.escape(btn)}{' + Llamar' if x['group'] != 'academia' else ''}</td></tr>
<tr><th>Datos estructurados</th><td>{types}. JSON listo en <code>landings/schema/{sl}.json</code>. FAQPage solo si las preguntas se ven en la página.</td></tr>
<tr><th>Cambios en Wix</th><td>{'Editar la página existente (no cambiar la URL).' if sl in EXISTING else 'Crear página hija de ' + ('Tratamientos' if x['group'] in ('motivo', 'servicio') else 'Academia') + ' con esa URL.'} Pegar título y descripción (Configuración SEO), H1 y texto como elementos nativos de Wix, marcado estructurado en SEO › Avanzado, imagen para redes og/{sl}.png.{' En la página de reserva ' + html.escape(unquote(BOOKING[sl])) + ': cambiar el título SEO a «Reservar…» y enlazar a esta página.' if sl in BOOKING else ''}</td></tr>
<tr><th>Verificar tras publicar</th><td>Móvil · Inspección de URL e indexación en Search Console · canonical = URL de arriba · aparece en sitemap.xml · Rich Results Test · enlaces internos funcionan</td></tr></table></details>""")
    # 5 fuera de la web
    r5 = "".join(f"<tr><td><b>{html.escape(a)}</b></td><td>{html.escape(b)}</td><td>{st(c)}</td></tr>" for a, b, c in OFFPAGE)
    r5b = "".join(f"<tr><td>{html.escape(q)}</td><td>{lab(sl)}<br><code>{html.escape(unquote(_wixurl(sl)))}</code></td></tr>" for sl, q in AI_PROMPTS)
    # 6 medición
    r6 = "".join(f"<tr><td><b>{html.escape(a)}</b></td><td>{html.escape(b)}</td><td>{html.escape(c)}</td><td>{st(d)}</td></tr>" for a, b, c, d in MEASURE)
    r6b = "".join(f"<tr><td>{lab(x['slug'])}</td><td>{GOAL[x['group']]}</td><td>Impresiones, clics, CTR y posición de «{html.escape(SEO[x['slug']]['kw'])}»</td></tr>" for x in PAGES)
    ask = "".join(f"<li>{html.escape(a)}</li>" for a in ASK)
    rv = "".join(f"<tr><td><span class='tag2'>{html.escape(a)}</span></td><td><b>{html.escape(b)}</b></td><td>{html.escape(c)}</td><td><span class='st st-{d.split()[0]}'>{html.escape(d)}</span></td></tr>" for a, b, c, d in VISIBILITY)
    states = {"verificado": sum(1 for *_, c in OFFPAGE if c == "verificado") + sum(1 for *_, d in MEASURE if d == "verificado"),
              "preparado": len(PAGES), "pendiente": sum(1 for *_, c in OFFPAGE if c == "pendiente") + sum(1 for *_, d in MEASURE if d == "pendiente")}
    gp = {"slug": "guia-seo", "group": "home", "title": "Plan SEO WA LAM", "desc": "", "h1": "Plan SEO", "wa": "Hola, tengo una consulta sobre la web de WA LAM."}
    T = lambda h: f'<div class="tbl"><table>{h}</table></div>'
    body = f"""<section class="hero"><div class="wrap" style="grid-template-columns:1fr"><div><span class="eyebrow">Plan SEO y visibilidad en IA</span><h1>Plan SEO de WA LAM</h1>
<p class="lead">{len(PAGES)} páginas en castellano y catalán. Investigación, mapa de URL, contenido propio, fichas para Wix, trabajo fuera de la web y medición. Ninguna acción garantiza el primer puesto; este plan reúne lo que más influye.</p>
<div class="btn-row"><span class="st st-preparado">preparado: {len(PAGES)} páginas</span><span class="st st-verificado">verificado: {states['verificado']} comprobaciones</span><span class="st st-pendiente">pendiente: {states['pendiente']} tareas</span></div></div></div></section>
<nav class="toc"><div class="wrap"><span class="k">Fases</span><div class="chips"><a href="#f1">1 · Investigación</a><a href="#f2">2 · Mapa de URL</a><a href="#f3">3 · Contenido propio</a><a href="#f4">4 · Fichas Wix</a><a href="#f5">5 · Fuera de la web e IA</a><a href="#f6">6 · Medición</a><a href="#visibilidad">Servicios ocultos</a><a href="#pido">Lo que te pido</a></div></div></nav>
<section id="f1" style="background:#fff"><div class="wrap">{sec_head("Fase 1", "Investigación de búsquedas", OBS_NOTE + " Los volúmenes (VOL) no están disponibles sin Keyword Planner o Search Console.")}
{T('<thead><tr><th>Página</th><th>Qué quiere encontrar</th><th>Términos en castellano</th><th>Términos en catalán</th><th>Resultados observados</th><th>Volumen</th></tr></thead><tbody>' + r1 + '</tbody>')}</div></section>
<section id="f2" style="background:var(--piedra)"><div class="wrap">{sec_head("Fase 2", "Una URL principal por intención", "Se reutiliza la estructura que ya existe en Wix (Tratamientos y Academia). Acupuntura explica el servicio general; Pérdida de peso explica tu consulta con cambios alimentarios y acupuntura; Retiros reúne mindfulness, meditación y silencio en una sola página.")}
{T('<thead><tr><th>Búsqueda objetivo</th><th>URL</th><th>Recibe enlaces de</th><th>Lleva al visitante a</th></tr></thead><tbody>' + ''.join(r2) + '</tbody>')}
<div class="card" style="margin-top:20px"><h3>Redirecciones 301</h3><ul>{red}</ul><p>Si alguna URL existente cambia, crear la redirección en Wix › Configuración SEO › Redirecciones URL antes de borrar nada.</p></div></div></section>
<section id="f3" style="background:#fff"><div class="wrap">{sec_head("Fase 3", "Información propia de WA LAM", "Quién atiende sale de tu currículum publicado y de tus confirmaciones: Rosa María Rodríguez Valls, osteópata D.O. y máster en medicina integrativa, con el detalle de formación en cada página y enlace al currículum. Solo la fisioterapeuta queda pendiente de nombre y colegiación.")}
{T('<thead><tr><th>Página</th><th>Quién atiende</th><th>Primera visita / programa</th><th>Dónde</th><th>Cómo reservar</th><th>Oferta frente a eficacia</th><th>Datos por confirmar</th></tr></thead><tbody>' + ''.join(r3) + '</tbody>')}</div></section>
<section id="f4" style="background:var(--piedra)"><div class="wrap">{sec_head("Fase 4", "Ficha técnica de Wix por página", "Pulsa cada página para ver su ficha.")}{''.join(cards)}</div></section>
<section id="f5" style="background:#fff"><div class="wrap">{sec_head("Fase 5", "Visibilidad fuera de las páginas")}
{T('<thead><tr><th>Tarea</th><th>Detalle</th><th>Estado</th></tr></thead><tbody>' + r5 + '</tbody>')}
<h3 style="color:var(--pet);margin:30px 0 10px">Preguntas para medir la presencia en respuestas de IA (sin mencionar WA LAM)</h3>
{T('<thead><tr><th>Pregunta</th><th>Página que debería citarse</th></tr></thead><tbody>' + r5b + '</tbody>')}</div></section>
<section id="f6" style="background:var(--piedra)"><div class="wrap">{sec_head("Fase 6", "Plan de medición")}
{T('<thead><tr><th>Qué</th><th>Cómo</th><th>Cuándo / qué hace falta</th><th>Estado</th></tr></thead><tbody>' + r6 + '</tbody>')}
<h3 style="color:var(--pet);margin:30px 0 10px">Objetivo por página</h3>
{T('<thead><tr><th>Página</th><th>Objetivo</th><th>Search Console</th></tr></thead><tbody>' + r6b + '</tbody>')}</div></section>
<section id="visibilidad" style="background:#fff"><div class="wrap">{sec_head("Servicios ocultos", "Lo que ya ofreces y casi no se ve", "Detectado en tu web (páginas de reserva, eventos y Academia). Las prestaciones nuevas son ideas observadas en otras consultas de longevidad de Barcelona; solo se publican si las confirmas.")}
{T('<thead><tr><th>Tipo</th><th>Servicio</th><th>Propuesta</th><th>Estado</th></tr></thead><tbody>' + rv + '</tbody>')}</div></section>
<section id="pido" style="background:var(--piedra)"><div class="wrap">{sec_head("Para seguir", "Lo que te pido")}<div class="card" style="max-width:900px;margin:0 auto"><ol style="padding-left:20px">{ask}</ol></div></div></section>"""
    css = """<style>.tbl{overflow-x:auto;background:#fff;border-radius:16px;border:1px solid rgba(29,63,64,.1)}.tbl table{border-collapse:collapse;width:100%;min-width:980px;font-size:.8rem}
.tbl th{background:#1D3F40;color:#fff;text-align:left;padding:10px;position:sticky;top:0}.tbl td{padding:10px;border-bottom:1px solid rgba(29,63,64,.1);vertical-align:top}
.tbl small,.kv small{opacity:.7}code{font-size:.74rem;color:#0a8f91;word-break:break-all}.tag2{display:inline-block;font-size:.62rem;font-weight:800;letter-spacing:.05em;background:rgba(12,191,194,.18);border-radius:6px;padding:2px 6px;margin:2px 0}
.st{display:inline-block;font-size:.75rem;font-weight:700;border-radius:999px;padding:5px 12px}.st-verificado{background:#0CBFC2;color:#1D3F40}.st-preparado{background:#fff;color:#1D3F40;border:1px solid #0CBFC2}.st-pendiente{background:#F2F1EE;color:#1D3F40;border:1px dashed #1D3F40}
details.wix{background:#fff;border:1px solid rgba(29,63,64,.12);border-radius:14px;margin-bottom:10px;padding:0 18px}details.wix summary{cursor:pointer;padding:14px 0;color:#1D3F40}
.kv{width:100%;border-collapse:collapse;font-size:.84rem;margin-bottom:14px}.kv th{width:190px;text-align:left;vertical-align:top;padding:8px;color:#1D3F40;background:#F2F1EE}.kv td{padding:8px;border-bottom:1px solid rgba(29,63,64,.08)}
@media(max-width:640px){.kv th{width:110px}}</style>"""
    return head(gp).replace("</head>", css + "</head>") + nav(gp) + body + contact(gp) + JS + "</body></html>"


def main():
    global BYSLUG
    for p in PAGES:
        for b in p["blocks"]:
            b["_id"] = slugify(b.get("h2", b["type"]))
    if LANG == "ca":
        PAGES[:] = [tr_deep(p) for p in PAGES]
        for k in list(GROUPS):
            GROUPS[k] = tr_deep(GROUPS[k])
        for k in list(SEO):
            SEO[k] = tr_deep(SEO[k])
        SITE["reviewer_md"] = tr(SITE["reviewer_md"])
        BYSLUG = {p["slug"]: p for p in PAGES}
    out = OUT / "ca" if LANG == "ca" else OUT
    if PREVIEW:
        out = Path(sys.argv[sys.argv.index("--preview") + 1]) / ("ca" if LANG == "ca" else "")
    out.mkdir(parents=True, exist_ok=True)
    for p in PAGES:
        (out / f"{p['slug']}.html").write_text(page(p), encoding="utf-8")
    if LANG == "es":
        (out / "guia-seo.html").write_text(guide(), encoding="utf-8")
    if not PREVIEW:
        sd = out / "schema"; sd.mkdir(exist_ok=True)
        for p in PAGES:
            (sd / f"{p['slug']}.json").write_text(json.dumps(schema(p), ensure_ascii=False, indent=2), encoding="utf-8")
        import csv
        with open(out / ("seo-wix-ca.csv" if LANG == "ca" else "seo-wix.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f); w.writerow(["url", "title", "meta_description", "h1", "palabra_clave", "secundarias", "catalan"])
            for p in PAGES:
                S = SEO[p["slug"]]; w.writerow(["/" + p["slug"], S["title"], S["desc"], plain(p["h1"]), S["kw"], "; ".join(S["kws"]), S["ca"]])
    rows = []
    for g in ("home", "motivo", "servicio", "academia"):
        G = GROUPS[g]
        cs = "".join(
            f'<a class="card" href="{x["slug"]}.html" target="_self"><span class="k">/{x["slug"]}</span><h3>{fmt(x["nav"])}'
            f'{"<span class=tag>1ª tanda</span>" if x.get("wave") == 1 else ""}</h3><p>{fmt(x["card"])}</p></a>'
            for x in PAGES if x["group"] == g)
        rows.append(f'<div class="hubgrp" id="{ {"home": "portada", "motivo": "motivos", "servicio": "servicios", "academia": "academia"}[g]}"><span class="k">{G["label"]}</span><h2>{G["title"]}</h2><div class="grid">{cs}</div></div>')
    idx = {"slug": "index", "group": "home", "title": "WA LAM · Landing pages", "desc": "Índice de revisión.", "h1": "", "faq": []}
    doc = head(idx) + nav(idx) + f"""<section class="hero"><div class="wrap" style="grid-template-columns:1fr"><div>
<span class="eyebrow">Revisión</span><h1>Landing pages WA LAM</h1><p class="lead">{len(PAGES)} páginas. Pulsa cualquiera para verla. Lo resaltado así: <span class="pend">dato pendiente</span> hay que completarlo antes de publicar.</p>
<div class="btn-row"><a class="btn btn-tq" href="{"../" if LANG == "ca" else ""}guia-seo.html" target="_self">{"Pla SEO (castellà)" if LANG == "ca" else "Ver el plan SEO"}</a></div></div></div></section>
<section style="background:#fff"><div class="wrap">{''.join(rows)}</div></section>""" + contact(dict(idx, wa="Hola, tengo una consulta sobre WA LAM.")) + JS + "</body></html>"
    (out / "index.html").write_text(doc, encoding="utf-8")
    print(f"{len(PAGES)} páginas + index.html + guia-seo.html en {out}")


if __name__ == "__main__":
    main()
