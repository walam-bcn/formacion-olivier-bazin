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
from seo_map import SEO, BARRIOS  # noqa: E402

SITE.setdefault("og_base", "https://walam-bcn.github.io/formacion-olivier-bazin/landings/og/")
SITE.setdefault("updated", "2026-11-18")
SITE.setdefault("updated_txt", "18 de noviembre de 2026")
# Rellenar cuando se confirme: activa reviewedBy en los datos estructurados
SITE.setdefault("reviewer", None)  # p. ej. {"name": "Nombre Apellido", "title": "Fisioterapeuta y osteópata", "license": "Col. nº 0000"}
PREVIEW = "--preview" in sys.argv

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
            return "./"
        return f"{slug}.html"
    return f"{SITE['base']}/{slug}" if slug else SITE["base"]


def canon(slug):
    return f"{SITE['base']}/{slug}"


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
    return f"""<!DOCTYPE html><html lang="es-ES"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{can}">
<link rel="alternate" hreflang="es-ES" href="{can}"><link rel="alternate" hreflang="x-default" href="{can}">
<meta name="geo.region" content="ES-CT"><meta name="geo.placename" content="Barcelona, Sarrià-Sant Gervasi">
<meta name="author" content="WA LAM · Salud integrativa"><meta name="theme-color" content="#1D3F40">
<meta property="og:type" content="website"><meta property="og:locale" content="es_ES"><meta property="og:site_name" content="WA LAM">
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
           "address": {"@type": "PostalAddress", "addressLocality": "Barcelona", "addressRegion": "Cataluña",
                       "addressCountry": "ES", "streetAddress": SITE.get("street", "")} if SITE.get("street") else
                      {"@type": "PostalAddress", "addressLocality": "Barcelona", "addressRegion": "Cataluña", "addressCountry": "ES"},
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
               "description": plain(S.get("desc", p["desc"])), "inLanguage": "es-ES",
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
<nav>{links}<a href="#contacto">Contacto</a></nav></div></header>"""


def hero(p):
    g = GROUPS.get(p["group"])
    crumbs = ""
    if g:
        crumbs = f'<div class="crumbs"><a href="{url("")}">Inicio</a> › <a href="{url(g["hub"])}">{g["nav"]}</a> › {html.escape(plain(p["nav"]))}</div>'
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
    return f'<section class="faq" id="preguntas-frecuentes"><div class="wrap">{sec_head("Preguntas frecuentes", "Lo que suelen preguntarnos")}<div class="list">{d}</div></div></section>'


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
<footer class="foot"><div class="wrap">WA LAM · Salud integrativa en Barcelona · Sarrià–Sant Gervasi · <a href="{url('')}">walambcn.com</a></div></footer>"""


NOTE = ('<section class="note"><div class="wrap"><p>La información de esta página es orientativa y no sustituye la valoración '
        'ni el seguimiento de tu médico. Si tus síntomas son intensos, cambian de forma brusca o se acompañan de fiebre, pérdida de peso '
        'sin causa aparente, sangrado o pérdida de fuerza, consulta con tu médico o con urgencias.</p></div></section>')


def byline(p):
    n = len(page_refs(p))
    rv = SITE.get("reviewer")
    who = f'{html.escape(rv["name"])}, {html.escape(rv.get("title", ""))} ({html.escape(rv.get("license", ""))})' if rv else '<span class="pend">profesional sanitario/a, titulación y nº de colegiado/a</span>'
    refs = f' · <a href="#{slugify(evid_title(p))}">{n} referencias científicas</a>' if n else ""
    return (f'<div class="byline"><div class="wrap"><span>✔ Contenido revisado por {who}</span>'
            f'<span>Actualizado: <time datetime="{SITE["updated"]}">{SITE["updated_txt"]}</time>{refs}</span></div></div>')


def evid_title(p):
    for b in p["blocks"]:
        if b["type"] == "evidence":
            return b["h2"]
    return ""


def quick(p):
    q = seo(p).get("quick")
    if not q:
        return ""
    return (f'<section class="quick" id="en-resumen"><div class="wrap"><div class="qbox"><span class="k">En resumen</span>'
            f'<h2>{fmt(seo(p).get("q_title", p["nav"]))}</h2><p>{fmt(q)}</p></div></div></section>')


def toc(items):
    if len(items) < 3:
        return ""
    lis = "".join(f'<a href="#{i}">{html.escape(t)}</a>' for i, t in items)
    return f'<nav class="toc" aria-label="En esta página"><div class="wrap"><span class="k">En esta página</span><div class="chips">{lis}</div></div></nav>'


def local(p):
    S = seo(p)
    kw = S.get("kw", plain(p["nav"]))
    barrios = ", ".join(BARRIOS[:-1]) + " y " + BARRIOS[-1]
    return f"""<section class="localsec" id="donde-estamos"><div class="wrap">{sec_head("Dónde estamos", f"{plain(p['nav'])} cerca de ti, en Sarrià–Sant Gervasi")}
<div class="grid g2"><div class="card"><span class="k">Consulta presencial</span><h3>WA LAM · Sarrià–Sant Gervasi, Barcelona</h3>
<p>Atendemos a pacientes de todo el distrito de Sarrià–Sant Gervasi —{html.escape(barrios)}— y de toda Barcelona.</p>
<ul><li>Dirección: <span class="pend">calle y número</span></li><li>Cómo llegar: <span class="pend">FGC / metro / bus más cercanos</span></li><li>Horario: <span class="pend">días y horas</span></li><li>Teléfono y WhatsApp: +34 675 716 409</li></ul></div>
<div class="card"><span class="k">Reserva</span><h3>Pide cita para {html.escape(plain(p['nav']).lower() if p['group'] == 'servicio' else 'tu primera visita')}</h3>
<p>Puedes reservar online o escribirnos por WhatsApp. Si no sabes qué profesional te conviene, cuéntanos tu caso y te orientamos antes de reservar.</p>
<div class="btn-row"><a class="btn btn-tq" href="{wa(p['wa'])}" target="_blank" rel="noopener">WhatsApp</a><a class="btn btn-gh" href="{SITE['booking']}">Reservar online</a></div>
<p style="margin-top:14px;font-size:.85rem"><span class="pend">Insertar mapa de Google de la ficha de Google Business Profile</span></p></div></div></div></section>"""


def page(p):
    parts = [head(p), nav(p), hero(p), byline(p) if p["group"] != "home" or True else ""]
    body, items = [], []
    for blk in p["blocks"]:
        t = blk["type"]
        h = {"mirror": mirror, "explain": explain, "cards": cards, "steps": steps, "evidence": evidence, "hubcards": hubcards}.get(t)
        if t == "pro":
            out = pro(blk, p); sid = "ficha"; label = "Ficha y reserva"
        else:
            out = h(blk); sid = slugify(blk.get("h2", t)); label = plain(blk.get("eyebrow", blk.get("h2", "")))
            if t != "hubcards":
                out = out.replace('<section class="', f'<section id="{sid}" class="', 1)
        if t != "hubcards":
            items.append((sid, label if t != "evidence" else "Evidencia científica"))
        body.append(out)
    if p["group"] in ("motivo", "servicio"):
        body.append(local(p)); items.append(("donde-estamos", "Dónde estamos"))
    if p.get("faq"):
        body.append(faq(p["faq"])); items.append(("preguntas-frecuentes", "Preguntas frecuentes"))
    parts += [quick(p), toc(items)] + body
    if p.get("related"): parts.append(related(p["related"]))
    parts.append(ctaband(p))
    if p["group"] in ("motivo", "servicio"): parts.append(NOTE)
    parts.append(contact(p))
    parts.append(JS + "</body></html>")
    return "\n".join(x for x in parts if x)


def hubcards(b):
    out = []
    for g in b["groups"]:
        G = GROUPS[g]
        cs = "".join(
            f'<a class="card" href="{url(x["slug"])}"><span class="k">{G["label"]}</span><h3>{fmt(x["nav"])}</h3><p>{fmt(x["card"])}</p><span class="go">Ver página →</span></a>'
            for x in PAGES if x["group"] == g)
        out.append(f'<section class="rel" id="{ {"motivo": "motivos", "servicio": "servicios", "academia": "academia"}[g]}"><div class="wrap">{sec_head(G["eyebrow"], G["title"], G["intro"])}<div class="grid">{cs}</div></div></section>')
    return "\n".join(out)


def guide():
    rows = []
    for x in PAGES:
        S = SEO[x["slug"]]
        rows.append(f"""<tr><td><b>{fmt(x['nav'])}</b><br><code>/{x['slug']}</code></td><td>{html.escape(S['title'])}<br><small>{len(S['title'])} caracteres</small></td>
<td>{html.escape(S['desc'])}<br><small>{len(S['desc'])} caracteres</small></td><td><b>{html.escape(S['kw'])}</b><br><small>{html.escape(', '.join(S['kws']))}</small></td><td>{html.escape(S['ca'])}</td></tr>""")
    gp = {"slug": "guia-seo", "group": "home", "title": "Guía SEO · WA LAM", "desc": "", "h1": "Guía SEO"}
    done = ["Una página por intención de búsqueda (motivo de consulta, servicio, curso), sin páginas duplicadas que compitan entre sí.",
            "Title de 60 caracteres o menos y meta description de 160 o menos, con la palabra clave y Sarrià–Sant Gervasi o Barcelona.",
            "Un único H1 por página con la palabra clave, y H2 con las búsquedas secundarias y preguntas reales.",
            "Bloque «En resumen» al inicio: una respuesta de 40 a 60 palabras pensada para los fragmentos destacados de Google y las respuestas de ChatGPT, Perplexity y AI Overviews.",
            "E-E-A-T sanitario (YMYL): firma de revisión clínica con fecha, referencias científicas con DOI verificado y lenguaje prudente sin promesas.",
            "Datos estructurados completos: MedicalClinic, MedicalWebPage (con lastReviewed, about, citation y audience), Service o Course, BreadcrumbList, FAQPage y Speakable.",
            "SEO local: bloque «Dónde estamos» con los barrios del distrito, datos de contacto y llamada a la reserva en cada página de consulta presencial.",
            "Enlazado interno: enlaces dentro del texto con texto ancla descriptivo, páginas relacionadas y migas de pan.",
            "Índice «En esta página» con anclas, que Google puede mostrar como enlaces directos en los resultados.",
            "Etiquetas para redes y WhatsApp (Open Graph y Twitter) con una imagen propia por página (carpeta og/).",
            "Canonical, hreflang es-ES, robots con max-snippet y max-image-preview, geo y preconnect de fuentes.",
            "Versión móvil verificada: sin desplazamiento horizontal y con botones a ancho completo."]
    todo = [("Wix: crear cada página con su URL", "Crea la página en Wix con exactamente la URL de la tabla (Configuración SEO › URL). No cambies las URL una vez publicadas."),
            ("Wix: title y description", "Copia el title y la meta description de la tabla en Configuración SEO de cada página."),
            ("Wix: texto nativo, no solo iframe", "Google no atribuye a tu página el texto de un iframe. Pega al menos el H1, el bloque «En resumen», los primeros párrafos y las preguntas frecuentes como texto de Wix. El iframe puede quedarse para el diseño."),
            ("Wix: datos estructurados", "En Configuración SEO › Avanzado › Marcado estructurado, pega el JSON de la carpeta schema/ correspondiente a cada página."),
            ("Completar los datos pendientes", "Nombre, titulación y nº de colegiado/a del profesional que revisa cada página, dirección, horario y precios. Es lo que más pesa en el E-E-A-T de una web de salud."),
            ("Google Business Profile", "Categoría principal «Centro de medicina integrativa» o «Osteópata», con categorías secundarias para fisioterapia y acupuntura; servicios con el mismo nombre que las páginas, fotos reales, horario y enlace a cada página. El mismo nombre, dirección y teléfono (NAP) en la web y en todos los directorios."),
            ("Reseñas", "Pide reseñas en Google después de cada alta, de forma ética: sin incentivos y respondiendo a todas. Las reseñas que mencionan el servicio y el barrio ayudan al posicionamiento local."),
            ("Directorios que hoy ocupan las primeras posiciones", "En las búsquedas revisadas aparecen sobre todo Doctoralia, Topdoctors y portales de aseguradoras. Crear o completar el perfil de cada profesional en Doctoralia y Topdoctors, enlazando a la web, es la vía más rápida para aparecer en la primera página mientras crece la web."),
            ("Versión en catalán", "En Barcelona una parte importante de las búsquedas se hacen en catalán (osteòpata Sarrià, insomni, deixar de fumar). Con Wix Multilingual, traducir las páginas de la primera tanda y enlazarlas con hreflang ca-ES."),
            ("Magazín (blog) como clúster", "Publicar artículos que respondan preguntas concretas y enlacen a la página de servicio: «¿Por qué me despierto a las 4 de la mañana?» → Sueño e insomnio; «Dolor lumbar con pruebas normales» → Dolor persistente; «¿Funciona la acupuntura para dejar de fumar?» → Dejar de fumar; «Hinchazón y estrés» → Salud digestiva; «Qué es el MBSR» → Curso MBSR."),
            ("Search Console y Keyword Planner", "Dar de alta el dominio en Google Search Console y enviar el sitemap de Wix. Para el volumen de búsquedas, usar Google Keyword Planner con ubicación Barcelona e idiomas español y catalán, y revisar cada mes qué consultas traen impresiones a cada página."),
            ("Medir", "Objetivo por página: impresiones y clics en Search Console, posición media de la palabra clave principal y reservas o WhatsApp recibidos desde la página.")]
    body = f"""<section class="hero"><div class="wrap" style="grid-template-columns:1fr"><div><span class="eyebrow">Guía SEO</span><h1>Plan SEO de las landing pages</h1>
<p class="lead">Qué está hecho en cada página, qué palabra clave trabaja y qué falta hacer en Wix y fuera de la web. Ninguna agencia puede garantizar el primer puesto, pero este es el trabajo que lo hace posible.</p></div></div></section>
<section style="background:#fff"><div class="wrap">{sec_head("Hecho en las páginas", "SEO técnico y de contenido incluido")}<div class="card" style="max-width:900px;margin:0 auto"><ul>{''.join(f'<li>{html.escape(d)}</li>' for d in done)}</ul></div></div></section>
<section style="background:var(--piedra)"><div class="wrap">{sec_head("Mapa de palabras clave", "Title, description y búsquedas de cada página", "Volumen de búsqueda: no disponible. Hay que consultarlo en Google Keyword Planner (ubicación Barcelona, español y catalán, últimos 12 meses) antes de priorizar.")}
<div class="tbl"><table><thead><tr><th>Página / URL</th><th>Title</th><th>Meta description</th><th>Palabra clave y secundarias</th><th>Catalán</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div></div></section>
<section class="steps dark"><div class="wrap">{sec_head("Lo que falta", "Pasos para posicionar, en orden")}<div class="sgrid">{''.join(f'<div class="step"><div class="num">{i+1}</div><h3>{html.escape(a)}</h3><p>{html.escape(b)}</p></div>' for i, (a, b) in enumerate(todo))}</div></div></section>"""
    css = "<style>.tbl{overflow-x:auto;background:#fff;border-radius:16px}.tbl table{border-collapse:collapse;width:100%;min-width:900px;font-size:.82rem}.tbl th{background:#1D3F40;color:#fff;text-align:left;padding:10px}.tbl td{padding:10px;border-bottom:1px solid rgba(29,63,64,.1);vertical-align:top}.tbl small{opacity:.7}code{font-size:.75rem;color:#0a8f91}</style>"
    gp["wa"] = "Hola, tengo una consulta sobre la web de WA LAM."
    return head(gp).replace("</head>", css + "</head>") + nav(gp) + body + contact(gp) + JS + "</body></html>"


def main():
    out = OUT
    if PREVIEW:
        out = Path(sys.argv[sys.argv.index("--preview") + 1]); out.mkdir(parents=True, exist_ok=True)
    for p in PAGES:
        (out / f"{p['slug']}.html").write_text(page(p), encoding="utf-8")
    (out / "guia-seo.html").write_text(guide(), encoding="utf-8")
    if not PREVIEW:
        sd = OUT / "schema"; sd.mkdir(exist_ok=True)
        for p in PAGES:
            (sd / f"{p['slug']}.json").write_text(json.dumps(schema(p), ensure_ascii=False, indent=2), encoding="utf-8")
        import csv
        with open(OUT / "seo-wix.csv", "w", newline="", encoding="utf-8") as f:
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
<div class="btn-row"><a class="btn btn-tq" href="guia-seo.html" target="_self">Ver la guía SEO</a></div></div></div></section>
<section style="background:#fff"><div class="wrap">{''.join(rows)}</div></section>""" + contact(dict(idx, wa="Hola, tengo una consulta sobre WA LAM.")) + JS + "</body></html>"
    (out / "index.html").write_text(doc, encoding="utf-8")
    print(f"{len(PAGES)} páginas + index.html + guia-seo.html en {out}")


if __name__ == "__main__":
    main()
