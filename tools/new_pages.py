"""Landings de patologías nuevas (noviembre 2026), cargadas desde tools/new_pages/*.json."""
import json
import re
from pathlib import Path

DIR = Path(__file__).parent / "new_pages"
OLD_LUMBAR = "lumbalgia-cervicalgia-cronica"

EYEBROW = {
    "fatiga-cronica-agotamiento": "Sistema nervioso · Energía", "agotamiento-fisico-emocional": "Sistema nervioso · Energía", "cortisol-estres-cronico": "Sistema nervioso · Estrés", "dolor-pelvico-barcelona": "Salud pélvica", "dolor-coxis-coccigodinia": "Salud pélvica", "ejercicios-suelo-pelvico": "Salud pélvica", "nervio-vago": "Osteopatía · Sistema nervioso", "osteopatia-fascia-barcelona": "Osteopatía", "osteopatia-bebes-ninos": "Osteopatía · Pediatría", "cicatrices-adherencias": "Osteopatía visceral", "vertigo-mareo": "Cabeza y cuello", "acufenos": "Cabeza y cuello", "lesiones-deportivas": "Deporte · Aparato locomotor", "osteopatia-trauma": "Osteopatía", "neuralgia-trigemino": "Dolor · Sistema nervioso",
    "intolerancias-alimentarias": "Salud digestiva", "intolerancia-histamina": "Salud digestiva", "intolerancia-fructosa": "Salud digestiva", "intolerancia-lactosa": "Salud digestiva", "intolerancia-gluten": "Salud digestiva", "diarrea-cronica": "Salud digestiva", "estrenimiento": "Salud digestiva", "gases-hinchazon-abdominal": "Salud digestiva", "digestiones-pesadas-gastritis": "Salud digestiva", "alergias-asma-infecciones": "Inflamación e inmunidad",
    "salud-digestiva-microbiota": "Salud digestiva · PNIE", "colon-irritable-sibo": "Salud digestiva",
    "reflujo-acidez": "Salud digestiva", "enfermedad-inflamatoria-intestinal": "Salud digestiva",
    "inflamacion-cronica-autoinmunes": "Inflamación e inmunidad", "hipotiroidismo-hashimoto": "Sistema endocrino",
    "sindrome-ovario-poliquistico": "Salud de la mujer", "candidiasis-vaginal-repeticion": "Salud de la mujer",
    "salud-metabolica": "Metabolismo · Prevención",
}


def load():
    out = {}
    for f in sorted(DIR.glob("batch*.json")):
        for d in json.loads(f.read_text()):
            out.pop(d["slug"], None)
            out[d["slug"]] = d  # la versión más reciente (lotes M = reescritura médica) prevalece
    return list(out.values())


def _page(d):
    ev = d["evidence"]
    # primero «¿Qué es…?», después los síntomas (petición de Rosa, 25 nov 2026)
    blocks = [
        {"type": "explain", "eyebrow": "Qué es", "h2": d["explain"]["h2"], "paras": d["explain"]["paras"]},
        {"type": "mirror", "eyebrow": "", "h2": d["mirror"]["h2"], "qs": d["mirror"]["qs"], "close": d["mirror"].get("close", "")},
    ]
    if d.get("explain2"):
        blocks.append({"type": "explain", "eyebrow": "", "h2": d["explain2"]["h2"], "paras": d["explain2"]["paras"]})
    for sec in d.get("sections", []):
        blk = {"type": "explain", "eyebrow": "", "h2": sec["h2"], "paras": sec.get("paras", [])}
        if sec.get("list"):
            blk["list_title"] = sec.get("list_title", ""); blk["list"] = sec["list"]
        blocks.append(blk)
    if d.get("cards"):
        blocks.append({"type": "cards", "eyebrow": "Cómo lo abordamos", "h2": d["cards"]["h2"], "items": d["cards"]["items"]})
    blocks += [
        {"type": "evidence", "h2": ev.get("h2", "Qué dice la evidencia"), "items": [tuple(x) for x in ev["items"]], "refs": ev.get("refs", [])},
    ]
    return {"slug": d["slug"], "group": d.get("group", "motivo"), "wave": 3, "nav": d["nav"], "card": d["card"], "title": d["title"], "desc": d["desc"],
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
            old = PAGES[pos[d["slug"]]]
            # conserva la ficha de precios y el grupo (servicio) de las páginas existentes
            keep = [b for b in old["blocks"] if b.get("type") in ("pro", "pack")]
            if keep:
                ev = next((k for k, b in enumerate(p["blocks"]) if b.get("type") == "evidence"), len(p["blocks"]))
                p["blocks"][ev:ev] = keep
            p["group"] = d.get("group", old["group"])
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
        if d.get("url_path"):
            URLS[d["slug"]] = d["url_path"]
        elif d["slug"] not in URLS:
            URLS[d["slug"]] = f"{H}/{d['slug']}"
        if d.get("url_path"):
            CA_SLUG[d["slug"]] = d["ca_slug"]
        else:
            CA_SLUG.setdefault(d["slug"], d["ca_slug"])


def integrate_research(RESEARCH):
    for d in load():
        r = d["research"]
        RESEARCH[d["slug"]] = (r[0], r[1], r[2], r[3])


# Áreas (mismo orden que «Te puedo ayudar en las siguientes situaciones» de walambcn.com/sobre-mi)
AREAS = [
    ("Dolor y aparato locomotor", "02", ["trocanteritis-dolor-lateral-cadera", "bursitis-subacromial-hombro", "tendinitis-rotuliana", "tenosinovitis-de-quervain", "lumbalgia-dolor-lumbar", "cervicalgia-dolor-cuello", "dorsalgia-dolor-espalda-alta", "ciatica",
                                         "artrosis", "hombro-doloroso", "dolor-rodilla-condromalacia", "contracturas-desgarros-musculares",
                                         "bruxismo-dolor-mandibular-atm", "osteopatia-fascia-barcelona", "lesiones-deportivas", "cicatrices-adherencias", "vertigo-mareo", "acufenos", "osteopatia-bebes-ninos", "neuralgia-trigemino", "hernia-disco-incipiente", "torticolis", "esguinces", "fascitis-plantar", "tunel-carpiano", "osteoporosis", "fibromialgia", "dolor-persistente-cronico", "dolor-neuropatico", "cefaleas-migrana"]),
    ("Inflamación e inmunidad", "03", ["inflamacion-cronica-autoinmunes", "alergias-asma-infecciones"]),
    ("Salud digestiva", "01", ["salud-digestiva-microbiota", "colon-irritable-sibo", "reflujo-acidez", "digestiones-pesadas-gastritis", "gases-hinchazon-abdominal", "estrenimiento", "diarrea-cronica", "enfermedad-inflamatoria-intestinal", "intolerancias-alimentarias", "intolerancia-gluten", "intolerancia-lactosa", "intolerancia-fructosa", "intolerancia-histamina"]),
    ("Metabolismo", "04", ["salud-metabolica", "perdida-de-peso-sarria-sant-gervasi", "dejar-de-fumar-acupuntura"]),
    ("Energía, estrés y sueño", "05", ["nervio-vago", "osteopatia-trauma", "agotamiento-fisico-emocional", "cortisol-estres-cronico", "fatiga-cronica-agotamiento", "estres-ansiedad", "sueno-insomnio"]),
    ("Salud de la mujer", "06", ["salud-mujer-menopausia", "sindrome-ovario-poliquistico", "candidiasis-vaginal-repeticion",
                                 "suelo-pelvico-dolor-pelvico", "dolor-pelvico-barcelona", "ejercicios-suelo-pelvico", "cistitis-repeticion-vejiga-dolorosa", "acompanamiento-fertilidad", "congestion-pelvica-sindrome-premenstrual", "trompas-salpingitis", "dolor-ovarico-quistes-ovario", "retroversion-utero", "vejiga-hiperactiva-urgencia", "cicatrices-episiotomia-cesarea", "sindrome-lacomme-dolor-pelvis-embarazo", "sindrome-ligamento-redondo", "posparto-recuperacion", "dolor-ingle-neuralgia-obturador", "lumbalgia-ciatica-origen-visceral"]),
    ("Sistema endocrino", "07", ["hipotiroidismo-hashimoto"]),
]


def integrate_areas(PAGES):
    known = {p["slug"]: p for p in PAGES}
    groups = [{"h": t, "links": [s for s in sl if s in known]} for t, _, sl in AREAS]
    groups = [g for g in groups if g["links"]]
    for p in PAGES:
        if p["slug"] == "medicina-integrativa-barcelona" and not any(b.get("type") == "linkgroups" for b in p["blocks"]):
            i = next((k for k, b in enumerate(p["blocks"]) if b.get("_id") == "te-ayudamos"), 0) + 1
            p["blocks"].insert(i, {"type": "linkgroups", "eyebrow": "", "h2": "¿En qué te puedo ayudar?", "_id": "en-que-te-puedo-ayudar",
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


# Lista completa de «Te puedo ayudar en las siguientes situaciones» (walambcn.com/sobre-mi), con enlace cuando hay página
HOME_LIST = [
    # Lista exacta de «Sobre mí» de walambcn.com (25 nov 2026): no añadir motivos que no estén en la web de Rosa
    ("Patologías musculoesqueléticas y osteoarticulares", [
        ("Artrosis", "artrosis"), ("Bursitis", "hombro-doloroso"), ("Capsulitis", "hombro-doloroso"), ("Tendinitis", "hombro-doloroso"), ("Cervicalgia", "cervicalgia-dolor-cuello"),
        ("Dolor de rodilla y condromalacia rotuliana", "dolor-rodilla-condromalacia"), ("Contracturas y desgarros musculares", "contracturas-desgarros-musculares"),
        ("Dorsalgia", "dorsalgia-dolor-espalda-alta"), ("Esguinces", "esguinces"), ("Esguince cervical", "cervicalgia-dolor-cuello"),
        ("Fascitis plantar", "fascitis-plantar"), ("Fibromialgia", "fibromialgia"), ("Hernias de disco incipientes y protrusión", "hernia-disco-incipiente"),
        ("Lumbalgia", "lumbalgia-dolor-lumbar"), ("Neuralgia de Arnold", "cervicalgia-dolor-cuello"), ("Osteoporosis y salud ósea", "osteoporosis"),
        ("Problemas de la ATM", "bruxismo-dolor-mandibular-atm"), ("Bruxismo y dolor mandibular", "bruxismo-dolor-mandibular-atm"), ("Sarcopenia", "osteoporosis"), ("Síndrome del túnel carpiano", "tunel-carpiano"),
        ("Hombro doloroso", "hombro-doloroso"), ("Tortícolis", "torticolis"),
        # añadidos por Rosa (25 nov 2026)
        ("Ciática", "ciatica"), ("Neuralgia del trigémino", "neuralgia-trigemino"),
        ("Dolor neuropático", "dolor-neuropatico"), ("Vértigo y mareo", "vertigo-mareo"), ("Acúfenos", "acufenos"),
        ("Cicatrices y adherencias", "cicatrices-adherencias"), ("Lesiones deportivas", "lesiones-deportivas"),
        # Rosa (25 nov 2026): migrañas y dolor crónico van en musculoesquelético, no en inflamación
        ("Migrañas", "cefaleas-migrana"), ("Migraña y dolor de cabeza", "cefaleas-migrana"),
        ("Síndrome del dolor crónico", "dolor-persistente-cronico"), ("Dolor persistente y crónico", "dolor-persistente-cronico")]),
    ("Patologías inflamatorias crónicas y autoinmunes", [
        ("Alergias", "alergias-asma-infecciones"), ("Artritis y artritis reumatoide", "inflamacion-cronica-autoinmunes"), ("Asma", "alergias-asma-infecciones"),
        ("Candidiasis", "candidiasis-vaginal-repeticion"), ("Colitis y gastritis", "digestiones-pesadas-gastritis"),
        ("Infecciones de repetición", "alergias-asma-infecciones"),
        ("Problemas autoinmunes de la piel: eccemas, atopia", "inflamacion-cronica-autoinmunes"),
        ("Inflamación crónica y enfermedades autoinmunes", "inflamacion-cronica-autoinmunes")]),
    ("Patologías intestinales", [
        ("Diarrea", "diarrea-cronica"), ("Estreñimiento", "estrenimiento"), ("Disbiosis intestinal", "salud-digestiva-microbiota"), ("Microbiota intestinal", "salud-digestiva-microbiota"),
        ("Digestiones pesadas", "digestiones-pesadas-gastritis"), ("Enfermedad inflamatoria intestinal: Crohn, colitis ulcerosa", "enfermedad-inflamatoria-intestinal"),
        ("Gases, hinchazón y distensión abdominal", "gases-hinchazon-abdominal"), ("Colon irritable", "colon-irritable-sibo"),
        ("Intolerancias alimentarias: caseína y lácteos", "intolerancias-alimentarias"), ("SIBO y LIBO", "colon-irritable-sibo"),
        # añadidos del material de la Dra. de la Puerta y Xevi Verdaguer (25 nov 2026)
        ("Reflujo y acidez", "reflujo-acidez"), ("Permeabilidad intestinal", "salud-digestiva-microbiota"),
        ("Cándida intestinal", "salud-digestiva-microbiota"), ("Sensibilidad al gluten", "intolerancia-gluten"),
        ("Intolerancia a la lactosa", "intolerancia-lactosa"), ("Intolerancia a la fructosa", "intolerancia-fructosa"),
        ("Intolerancia a la histamina y déficit de DAO", "intolerancia-histamina")]),
    ("Patologías metabólicas y cardiovasculares", [
        ("Adicción al chocolate o a los refrescos", None), ("Alcoholismo", None), ("Déficit de hierro, vitaminas, minerales y oligoelementos", None),
        ("Hígado graso", "salud-metabolica"), ("Hipertensión", "salud-metabolica"), ("Prevención cardiovascular", "salud-metabolica"),
        ("Resistencia a la insulina", "salud-metabolica"), ("Síndrome metabólico", "salud-metabolica"), ("Sobrepeso y obesidad", "perdida-de-peso-sarria-sant-gervasi"),
        ("Tabaquismo", "dejar-de-fumar-acupuntura"),
        ("Pérdida de peso", "perdida-de-peso-sarria-sant-gervasi"), ("Dejar de fumar", "dejar-de-fumar-acupuntura")]),
    ("Agotamiento, ansiedad, estrés y sueño", [
        ("Estrés", "estres-ansiedad"), ("Ansiedad", "estres-ansiedad"), ("Cortisol y estrés crónico", "cortisol-estres-cronico"), ("Shock emocional", "agotamiento-fisico-emocional"),
        ("Insomnio", "sueno-insomnio"), ("Trastornos del sueño", "sueno-insomnio"), ("Cansancio extremo", "fatiga-cronica-agotamiento"),
        ("Fatiga crónica", "fatiga-cronica-agotamiento"), ("Estado de ánimo bajo", "agotamiento-fisico-emocional"),
        ("Agotamiento físico y emocional", "agotamiento-fisico-emocional")]),
    ("Ginecología", [
        ("Acné en mujeres", "sindrome-ovario-poliquistico"), ("Candidiasis vaginal recurrente", "candidiasis-vaginal-repeticion"),
        ("Cistitis recurrente", "cistitis-repeticion-vejiga-dolorosa"), ("Infertilidad y abortos recurrentes", "acompanamiento-fertilidad"),
        ("Menopausia", "salud-mujer-menopausia"), ("Ovarios poliquísticos", "sindrome-ovario-poliquistico"), ("Sofocos", "salud-mujer-menopausia")]),
    ("Problemas endocrinos", [
        ("Enfermedad de Hashimoto temprana", "hipotiroidismo-hashimoto"), ("Hipertiroidismo", None), ("Hipotiroidismo leve", "hipotiroidismo-hashimoto"),
        ("Trastornos de la prolactina", None)]),
]


def integrate_home_list(PAGES):
    known = {p["slug"] for p in PAGES}
    for p in PAGES:
        if p["slug"] == "medicina-integrativa-barcelona":
            for b in p["blocks"]:
                if b.get("type") == "linkgroups":
                    b["groups"] = [{"h": t, "links": [(lab, s if s in known else None) for lab, s in items]} for t, items in HOME_LIST]
                    b.pop("all", None)
                    b["intro"] = "Esta lista orienta sobre los motivos de consulta más frecuentes. Si tu caso no aparece, escríbenos y te diremos si podemos ayudarte."
    PAGES[:] = [p for p in PAGES if p["slug"] != "en-que-podemos-ayudarte"]
    for p in PAGES:
        if p.get("related"):
            p["related"] = [x for x in p["related"] if x != "en-que-podemos-ayudarte"]


# Portada: «En qué te puedo ayudar» con indicaciones (lista de Sobre mí) y nuestro abordaje, por áreas
RT = "Nuestro abordaje es el [método re:trace](programas-re-trace)"
AREA_BLOCKS = [
    ("01 · Aparato locomotor", "Sistema musculoesquelético y dolor", "Dolor articular y vertebral, agudo o persistente.",
     "%s, que integra la osteopatía, el ejercicio adaptado y la PNIE." % RT,
     ["[Método re:trace](programas-re-trace)", "[Osteopatía](osteopatia-sarria-sant-gervasi)", "[PNIE](pni-pnie-barcelona)"]),
    ("02 · Inflamación e inmunidad", "Inflamación crónica, inmunidad y piel", "Procesos en los que la inflamación y la inmunidad desempeñan un papel central.",
     "%s, con la PNIE, la nutrición y la microbiota como pilares." % RT,
     ["[Método re:trace](programas-re-trace)", "[PNIE](pni-pnie-barcelona)", "[Microbiota](salud-digestiva-microbiota)", "[Nutrición y salud intestinal](nutricion-salud-intestinal)"]),
    ("03 · Aparato digestivo", "Aparato digestivo", "Uno de los motivos de consulta más frecuentes.",
     "%s, con la PNIE, la microbiota, la nutrición y la osteopatía visceral." % RT,
     ["[Método re:trace](programas-re-trace)", "[PNIE](pni-pnie-barcelona)", "[Microbiota](salud-digestiva-microbiota)", "[Nutrición y salud intestinal](nutricion-salud-intestinal)", "[Osteopatía visceral](osteopatia-visceral-barcelona)"]),
    ("04 · Metabolismo", "Metabolismo y salud cardiovascular", "Factores de riesgo que dependen en gran medida del estilo de vida.",
     "%s, con la nutrición, el ejercicio y la prevención." % RT,
     ["[Método re:trace](programas-re-trace)", "[Nutrición y salud intestinal](nutricion-salud-intestinal)", "[Longevidad y prevención](prevencion-longevidad)"]),
    ("05 · Sistema nervioso", "Agotamiento, ansiedad, estrés y sueño", "Cuando el sistema nervioso, el sueño y la capacidad de adaptación están comprometidos.",
     "%s, con el mindfulness para la salud, la osteopatía y la PNIE." % RT,
     ["[Método re:trace](programas-re-trace)", "[Mindfulness para la salud](mindfulness-barcelona)", "[Osteopatía](osteopatia-sarria-sant-gervasi)", "[PNIE](pni-pnie-barcelona)"]),
    ("06 · Salud de la mujer", "Ginecología", "Etapas y procesos específicos de la salud femenina.",
     "%s, con la PNIE, la nutrición y la osteopatía urogenital de abordaje externo." % RT,
     ["[Método re:trace](programas-re-trace)", "[PNIE](pni-pnie-barcelona)", "[Osteopatía urogenital](suelo-pelvico-dolor-pelvico)"]),
    ("07 · Sistema endocrino", "Sistema endocrino", "Alteraciones hormonales en las que el estilo de vida tiene un papel importante.",
     "%s, con la PNIE y la nutrición." % RT,
     ["[Método re:trace](programas-re-trace)", "[PNIE](pni-pnie-barcelona)", "[Nutrición y salud intestinal](nutricion-salud-intestinal)"]),
]

WORK_STEPS = [
    ("Antes de la primera visita", "Me envías los análisis y las pruebas médicas recientes que consideres relevantes para tu problema."),
    ("Primera consulta", "Dura unos 60 minutos. Si lo considero necesario, solicito pruebas más específicas, como un estudio de microbiota, para centrar el diagnóstico."),
    ("Tratamiento por fases", "Organizo el tratamiento en fases, normalmente dos o tres, adaptándome a cada paciente."),
    ("Recomendaciones", "Al terminar cada consulta, presencial u online, recibes las recomendaciones para la fase que iniciamos."),
    ("Dudas entre sesiones", "Si te surgen dudas, puedes escribirme antes de la siguiente sesión."),
    ("Mantenimiento", "Al terminar el tratamiento, recibes las pautas de mantenimiento para consolidar la mejoría."),
]


# Rosa (25 nov 2026): los botones del directorio pasan también a la lista de su área en medicina integrativa
AREA_EXTRA = [
    ["lumbalgia-dolor-lumbar", "cervicalgia-dolor-cuello", "dorsalgia-dolor-espalda-alta", "ciatica", "hernia-disco-incipiente", "artrosis", "hombro-doloroso",
     "dolor-rodilla-condromalacia", "torticolis", "tunel-carpiano", "fascitis-plantar", "osteoporosis",
     "trocanteritis-dolor-lateral-cadera", "bursitis-subacromial-hombro", "tendinitis-rotuliana", "tenosinovitis-de-quervain",
     "dolor-persistente-cronico", "dolor-musculoesqueletico", "dolor-articular-miofascial", "contracturas-desgarros-musculares", "esguinces",
     "lesiones-deportivas", "fibromialgia", "cicatrices-adherencias", "dolor-postquirurgico", "dolor-oncologico",
     "cefaleas-migrana", "neuralgia-trigemino", "dolor-neuropatico", "bruxismo-dolor-mandibular-atm", "vertigo-mareo", "acufenos"],
    ["inflamacion-cronica-autoinmunes", "alergias-asma-infecciones"],
    ["salud-digestiva-microbiota", "colon-irritable-sibo", "reflujo-acidez", "digestiones-pesadas-gastritis", "gases-hinchazon-abdominal", "estrenimiento",
     "diarrea-cronica", "enfermedad-inflamatoria-intestinal", "intolerancias-alimentarias", "intolerancia-gluten", "intolerancia-lactosa",
     "intolerancia-fructosa", "intolerancia-histamina"],
    ["salud-metabolica", "perdida-de-peso-sarria-sant-gervasi", "dejar-de-fumar-acupuntura"],
    ["estres-ansiedad", "cortisol-estres-cronico", "sueno-insomnio", "fatiga-cronica-agotamiento", "agotamiento-fisico-emocional"],
    ["salud-mujer-menopausia", "sindrome-ovario-poliquistico", "acompanamiento-fertilidad", "dolor-menstrual-endometriosis", "candidiasis-vaginal-repeticion",
     "osteopatia-embarazo-posparto", "suelo-pelvico-dolor-pelvico", "dolor-pelvico-barcelona", "ejercicios-suelo-pelvico", "incontinencia-urinaria-esfuerzo",
     "prolapso-organos-pelvicos", "cistitis-repeticion-vejiga-dolorosa", "dispareunia-dolor-relaciones", "neuralgia-pudendo", "dolor-coxis-coccigodinia", "congestion-pelvica-sindrome-premenstrual", "trompas-salpingitis", "dolor-ovarico-quistes-ovario", "retroversion-utero", "vejiga-hiperactiva-urgencia", "cicatrices-episiotomia-cesarea", "sindrome-lacomme-dolor-pelvis-embarazo", "sindrome-ligamento-redondo", "posparto-recuperacion", "dolor-ingle-neuralgia-obturador", "lumbalgia-ciatica-origen-visceral"],
    ["hipotiroidismo-hashimoto"],
]


# «Nuestro abordaje» redactado por Rosa, área por área (n = índice en AREA_BLOCKS); un solo botón: re:trace
ABORD_ROSA = {
    0: ("Cómo abordamos el dolor musculoesquelético", [
        "En WA LAM abordamos el dolor musculoesquelético con nuestro método de medicina integrativa [re:trace](programas-re-trace). En la primera visita valoramos la localización del dolor, la movilidad de la zona afectada y cómo los síntomas repercuten en sus actividades cotidianas. Cuando su historia clínica lo indica, ampliamos la valoración a aspectos como la calidad del sueño, la presencia de insomnio, el estrés, la salud digestiva y la alimentación.",
        "A partir de esta valoración, diseñamos un tratamiento personalizado. En algunos casos, una sola sesión puede ser suficiente. Si el dolor persiste, reaparece o sigue limitando su movilidad, le proponemos un plan de tratamiento que ajustamos según su evolución."]),
    1: ("Cómo lo abordamos", [
        "La nutrición y la microbiota intestinal son dos pilares de la valoración desde la **[psiconeuroinmunoendocrinología (PNIE)](pni-pnie-barcelona)**. En el método **[re:trace](programas-re-trace)**, la historia clínica y los antecedentes familiares orientan qué pruebas pueden ayudar a precisar la valoración. Según su caso, podemos complementarla con análisis de marcadores inflamatorios o, cuando exista una indicación clínica, con estudios genéticos. Estos resultados, junto con la valoración inicial, guían el plan personalizado."]),
    2: ("Cómo lo abordamos", [
        "En **[RE:TRACE](programas-re-trace)**, el cuidado digestivo sigue un recorrido en tres etapas. Primero, **entender**: una historia clínica detallada y, si procede, pruebas como el estudio de la microbiota para identificar qué está alterado. Después, **restablecer**: un plan personalizado de alimentación y hábitos saludables para recuperarse. Por último, **consolidar**: pautas de mantenimiento para que la mejoría se sostenga en el tiempo."]),
    3: ("Cómo lo abordamos", [
        "**[re:trace](programas-re-trace)** integra la valoración de su perfil cardiometabólico con la salud digestiva, la microbiota intestinal, la nutrición y el movimiento. A partir de esa valoración, definimos con usted qué hábitos priorizar y si el ayuno tiene cabida en su plan de prevención cardiovascular y longevidad."]),
    4: ("Cómo lo abordamos", [
        "El agotamiento no se resuelve solo descansando más. En **[RE:TRACE](programas-re-trace)** valoramos su estilo de vida y, a partir de ahí, trabajamos en tres tiempos. **Soltar** lo que le desgasta. **Recuperar** con alimentación, descanso y movimiento consciente, junto con terapias con respaldo científico que ayudan a regular el sistema nervioso. **Reconectar** con herramientas para gestionar el estrés en su día a día. Así recupera la energía, la claridad y el vigor, y aprende a mantenerlos."],
        ["[Método re:trace](programas-re-trace)", "[Curso MBSR de 8 semanas, en directo por Zoom](curso-mindfulness-mbsr-barcelona)", "[Mindfulness: sesiones semanales en directo por Zoom](mindfulness-barcelona)", "[Formación RE:TRACE de 9 meses](formacion-re-trace)"]),
    5: ("Cómo lo abordamos", [
        "Muchas mujeres llegan después de años conviviendo con síntomas que se han normalizado: dolor menstrual, sofocos, cistitis de repetición o cansancio. En **[RE:TRACE](programas-re-trace)** empezamos por escuchar su historia completa, porque cada etapa de la vida deja huella. Una valoración global nos permite entender qué hay detrás y acompañarla con un plan que respeta su cuerpo y sus tiempos."]),
    6: ("Cómo lo abordamos", [
        "**[re:trace](programas-re-trace)** integra todo lo que la ciencia ha demostrado eficaz para optimizar la salud y el rendimiento en un único método, nacido de más de veinte años de experiencia clínica en WA LAM. A través de programas hiperpersonalizados, diagnósticos avanzados y un cuidado experto, logra una transformación medible y duradera en un tiempo récord."]),
}


def integrate_home_areas(PAGES, primer_contacto=None):
    known = {p["slug"] for p in PAGES}
    for p in PAGES:
        if p["slug"] != "medicina-integrativa-barcelona":
            continue
        bl = p["blocks"]
        i = next((k for k, b in enumerate(bl) if b.get("type") == "linkgroups"), None)
        if i is None:
            return
        bl.pop(i)
        new = [{"type": "steps", "eyebrow": "", "h2": "Mi forma de trabajar", "intro": "Un enfoque integrativo", "_id": "mi-forma-de-trabajar", "items": WORK_STEPS}]
        if primer_contacto:
            new.append(primer_contacto)
        new.append({"type": "explain", "eyebrow": "", "h2": "¿En qué te puedo ayudar?", "_id": "en-que-te-puedo-ayudar",
                    "paras": ["Esta lista orienta sobre los motivos de consulta más frecuentes. Si tu caso no aparece, escríbenos y te diremos si podemos ayudarte."]})
        navs = {q["slug"]: q["nav"] for q in PAGES}
        for n, ((ey, h2, intro, ptxt, li), (_, items)) in enumerate(zip(AREA_BLOCKS, HOME_LIST)):
            have = {s for _, s in items if s}
            extra = [(navs[s], s) for s in AREA_EXTRA[n] if s in known and s not in have]
            import unicodedata as _ud
            _key = lambda t: _ud.normalize("NFD", t[0]).encode("ascii", "ignore").decode().lower()
            ind = [f"[{lab}]({s})" if s in known else lab for lab, s in sorted(items + extra, key=_key)]
            abord = {"k": "Nuestro abordaje", "h": "Cómo lo abordamos", "p": ptxt, "li": [x for x in li if x.split("](")[1][:-1] in known]}
            if n in ABORD_ROSA:
                abord = {"k": "Nuestro abordaje", "h": ABORD_ROSA[n][0], "paras": ABORD_ROSA[n][1], "li": (ABORD_ROSA[n][2] if len(ABORD_ROSA[n]) > 2 else ["[Método re:trace](programas-re-trace)"])}
            if n == 0:
                half = (len(ind) + 1) // 2
                its = [{"k": "Indicaciones", "h": "Motivos de consulta frecuentes", "li": ind[:half]},
                       {"k": "", "h": "", "li": ind[half:], "post": abord}]
            else:
                its = [{"k": "Indicaciones", "h": "Motivos de consulta frecuentes", "li": ind}, abord]
            new.append({"type": "cards", "eyebrow": ey, "h2": h2, "intro": intro, "items": its})
        bl[i:i] = new
