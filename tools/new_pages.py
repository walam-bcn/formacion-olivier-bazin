"""Landings de patologías nuevas (noviembre 2026), cargadas desde tools/new_pages/*.json."""
import json
import re
from pathlib import Path

DIR = Path(__file__).parent / "new_pages"
OLD_LUMBAR = "lumbalgia-cervicalgia-cronica"

EYEBROW = {
    "fatiga-cronica-agotamiento": "Sistema nervioso · Energía", "agotamiento-fisico-emocional": "Sistema nervioso · Energía",
    "intolerancias-alimentarias": "Salud digestiva", "alergias-asma-infecciones": "Inflamación e inmunidad",
    "salud-digestiva-microbiota": "Salud digestiva · PNIE", "colon-irritable-sibo": "Salud digestiva",
    "reflujo-acidez": "Salud digestiva", "enfermedad-inflamatoria-intestinal": "Salud digestiva",
    "inflamacion-cronica-autoinmunes": "Inflamación e inmunidad", "hipotiroidismo-hashimoto": "Sistema endocrino",
    "sindrome-ovario-poliquistico": "Salud de la mujer", "candidiasis-vaginal-repeticion": "Salud de la mujer",
    "salud-metabolica": "Metabolismo · Prevención",
}


def load():
    out = []
    for f in sorted(DIR.glob("batch*.json")):
        out += json.loads(f.read_text())
    return out


def _page(d):
    ev = d["evidence"]
    blocks = [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": d["mirror"]["h2"], "qs": d["mirror"]["qs"], "close": d["mirror"].get("close", "")},
        {"type": "explain", "eyebrow": "Qué es", "h2": d["explain"]["h2"], "paras": d["explain"]["paras"]},
        {"type": "cards", "eyebrow": "Cómo lo abordamos", "h2": d["cards"]["h2"], "items": d["cards"]["items"]},
        {"type": "evidence", "h2": ev.get("h2", "Qué dice la evidencia"), "items": [tuple(x) for x in ev["items"]], "refs": ev.get("refs", [])},
    ]
    return {"slug": d["slug"], "group": "motivo", "wave": 3, "nav": d["nav"], "card": d["card"], "title": d["title"], "desc": d["desc"],
            "about": d["seo"]["entity"][1], "eyebrow": EYEBROW.get(d["slug"], "Dolor · Aparato locomotor"),
            "h1": d["h1"], "sub": d["sub"], "lead": d["lead"], "facts_title": d.get("facts_title", "En WA LAM"), "facts": d["facts"],
            "wa": d["wa"], "blocks": blocks, "faq": [tuple(x) for x in d["faq"]], "related": d["related"],
            "cta": {"h2": d["cta_h2"], "p": "Escríbenos por WhatsApp y te orientamos sobre tu caso."}}


def integrate_pages(PAGES):
    new = load()
    if not new:
        return
    slugs = {d["slug"] for d in new}
    known = {p["slug"] for p in PAGES} | slugs
    pos = {p["slug"]: i for i, p in enumerate(PAGES)}
    # la página nueva de microbiota sustituye a la de salud digestiva (misma URL)
    for d in new:
        p = _p = _page(d)
        if d["slug"] in pos:
            PAGES[pos[d["slug"]]] = p
        else:
            PAGES.append(p)
    # lumbalgia y cervicalgia sustituyen a la página conjunta
    if "lumbalgia-dolor-lumbar" in slugs:
        PAGES[:] = [p for p in PAGES if p["slug"] != OLD_LUMBAR]
        rep = lambda s: s.replace(f"]({OLD_LUMBAR})", "](lumbalgia-dolor-lumbar)")
        for p in PAGES:
            if p.get("related"):
                r = ["lumbalgia-dolor-lumbar" if x == OLD_LUMBAR else x for x in p["related"]]
                p["related"] = list(dict.fromkeys(r))
            _walk(p, rep)
    for p in PAGES:
        if p.get("related"):
            p["related"] = [x for x in p["related"] if x in known and x != p["slug"]]


def _walk(o, f):
    if isinstance(o, dict):
        for k, v in o.items():
            if isinstance(v, str):
                o[k] = f(v)
            else:
                _walk(v, f)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            if isinstance(v, str):
                o[i] = f(v)
            elif isinstance(v, tuple):
                o[i] = tuple(f(x) if isinstance(x, str) else x for x in v)
            else:
                _walk(v, f)


def integrate_seo(SEO, URLS, CA_SLUG, H):
    for d in load():
        s = d["seo"]
        SEO[d["slug"]] = {"kw": s["kw"], "kws": s["kws"], "ca": s["ca_kw"], "title": d["title"], "desc": d["desc"],
                          "quick": s["quick"], "entity": tuple(s["entity"])}
        if d["slug"] not in URLS:
            URLS[d["slug"]] = f"{H}/{d['slug']}"
        CA_SLUG[d["slug"]] = d["ca_slug"]


def integrate_research(RESEARCH):
    for d in load():
        r = d["research"]
        RESEARCH[d["slug"]] = (r[0], r[1], r[2], r[3])


# Áreas (mismo orden que «Te puedo ayudar en las siguientes situaciones» de walambcn.com/sobre-mi)
AREAS = [
    ("Dolor y aparato locomotor", "02", ["lumbalgia-dolor-lumbar", "cervicalgia-dolor-cuello", "dorsalgia-dolor-espalda-alta", "ciatica",
                                         "artrosis", "hombro-doloroso", "dolor-rodilla-condromalacia", "contracturas-desgarros-musculares",
                                         "bruxismo-dolor-mandibular-atm", "hernia-disco-incipiente", "torticolis", "esguinces", "fascitis-plantar", "tunel-carpiano", "osteoporosis", "fibromialgia", "dolor-persistente-cronico", "dolor-neuropatico", "cefaleas-migrana"]),
    ("Inflamación e inmunidad", "03", ["inflamacion-cronica-autoinmunes", "alergias-asma-infecciones"]),
    ("Salud digestiva", "01", ["salud-digestiva-microbiota", "colon-irritable-sibo", "reflujo-acidez", "enfermedad-inflamatoria-intestinal", "intolerancias-alimentarias"]),
    ("Metabolismo", "04", ["salud-metabolica", "perdida-de-peso-sarria-sant-gervasi", "dejar-de-fumar-acupuntura"]),
    ("Energía, estrés y sueño", "05", ["agotamiento-fisico-emocional", "fatiga-cronica-agotamiento", "estres-ansiedad", "sueno-insomnio"]),
    ("Salud de la mujer", "06", ["salud-mujer-menopausia", "sindrome-ovario-poliquistico", "candidiasis-vaginal-repeticion",
                                 "cistitis-repeticion-vejiga-dolorosa", "acompanamiento-fertilidad", "suelo-pelvico-dolor-pelvico"]),
    ("Sistema endocrino", "07", ["hipotiroidismo-hashimoto"]),
]


def integrate_areas(PAGES):
    known = {p["slug"]: p for p in PAGES}
    groups = [{"h": t, "links": [s for s in sl if s in known]} for t, _, sl in AREAS]
    groups = [g for g in groups if g["links"]]
    for p in PAGES:
        if p["slug"] == "medicina-integrativa-barcelona" and not any(b.get("type") == "linkgroups" for b in p["blocks"]):
            i = next((k for k, b in enumerate(p["blocks"]) if b.get("_id") == "te-ayudamos"), 0) + 1
            p["blocks"].insert(i, {"type": "linkgroups", "eyebrow": "", "h2": "En qué te puedo ayudar", "_id": "en-que-te-puedo-ayudar",
                                   "intro": "Estos son los motivos de consulta más frecuentes, ordenados por áreas.",
                                   "groups": groups, "all": "en-que-podemos-ayudarte"})
        if p["slug"] == "en-que-podemos-ayudarte":
            for b in p["blocks"]:
                ey = b.get("eyebrow", "")
                for t, num, sl in AREAS:
                    if ey.startswith(num + " ·") and b.get("items"):
                        li = b["items"][-1].setdefault("li", [])
                        have = " ".join(li)
                        for s in sl:
                            if s in known and f"]({s})" not in have:
                                li.append(f"[{known[s]['nav']}]({s})")
