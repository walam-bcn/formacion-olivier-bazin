"""Landings de patologías nuevas (noviembre 2026), cargadas desde tools/new_pages/*.json."""
import json
import re
from pathlib import Path

DIR = Path(__file__).parent / "new_pages"
OLD_LUMBAR = "lumbalgia-cervicalgia-cronica"

EYEBROW = {
    "fatiga-cronica-agotamiento": "Sistema nervioso · Energía", "agotamiento-fisico-emocional": "Sistema nervioso · Energía", "cortisol-estres-cronico": "Sistema nervioso · Estrés", "dolor-pelvico-barcelona": "Salud pélvica", "ejercicios-suelo-pelvico": "Salud pélvica", "nervio-vago": "Osteopatía · Sistema nervioso", "osteopatia-fascia-barcelona": "Osteopatía", "osteopatia-bebes-ninos": "Osteopatía · Pediatría", "cicatrices-adherencias": "Osteopatía visceral", "vertigo-mareo": "Cabeza y cuello", "acufenos": "Cabeza y cuello", "lesiones-deportivas": "Deporte · Aparato locomotor", "osteopatia-trauma": "Osteopatía", "neuralgia-trigemino": "Dolor · Sistema nervioso",
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
    blocks = [
        {"type": "mirror", "eyebrow": "", "h2": d["mirror"]["h2"], "qs": d["mirror"]["qs"], "close": d["mirror"].get("close", "")},
        {"type": "explain", "eyebrow": "Qué es", "h2": d["explain"]["h2"], "paras": d["explain"]["paras"]},
    ]
    if d.get("explain2"):
        blocks.append({"type": "explain", "eyebrow": "", "h2": d["explain2"]["h2"], "paras": d["explain2"]["paras"]})
    for sec in d.get("sections", []):
        blk = {"type": "explain", "eyebrow": "", "h2": sec["h2"], "paras": sec.get("paras", [])}
        if sec.get("list"):
            blk["list_title"] = sec.get("list_title", ""); blk["list"] = sec["list"]
        blocks.append(blk)
    blocks += [
        {"type": "cards", "eyebrow": "Cómo lo abordamos", "h2": d["cards"]["h2"], "items": d["cards"]["items"]},
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
    ("Dolor y aparato locomotor", "02", ["lumbalgia-dolor-lumbar", "cervicalgia-dolor-cuello", "dorsalgia-dolor-espalda-alta", "ciatica",
                                         "artrosis", "hombro-doloroso", "dolor-rodilla-condromalacia", "contracturas-desgarros-musculares",
                                         "bruxismo-dolor-mandibular-atm", "osteopatia-fascia-barcelona", "lesiones-deportivas", "cicatrices-adherencias", "vertigo-mareo", "acufenos", "osteopatia-bebes-ninos", "neuralgia-trigemino", "hernia-disco-incipiente", "torticolis", "esguinces", "fascitis-plantar", "tunel-carpiano", "osteoporosis", "fibromialgia", "dolor-persistente-cronico", "dolor-neuropatico", "cefaleas-migrana"]),
    ("Inflamación e inmunidad", "03", ["inflamacion-cronica-autoinmunes", "alergias-asma-infecciones"]),
    ("Salud digestiva", "01", ["salud-digestiva-microbiota", "colon-irritable-sibo", "reflujo-acidez", "digestiones-pesadas-gastritis", "gases-hinchazon-abdominal", "estrenimiento", "diarrea-cronica", "enfermedad-inflamatoria-intestinal", "intolerancias-alimentarias", "intolerancia-gluten", "intolerancia-lactosa", "intolerancia-fructosa", "intolerancia-histamina"]),
    ("Metabolismo", "04", ["salud-metabolica", "perdida-de-peso-sarria-sant-gervasi", "dejar-de-fumar-acupuntura"]),
    ("Energía, estrés y sueño", "05", ["nervio-vago", "osteopatia-trauma", "agotamiento-fisico-emocional", "cortisol-estres-cronico", "fatiga-cronica-agotamiento", "estres-ansiedad", "sueno-insomnio"]),
    ("Salud de la mujer", "06", ["salud-mujer-menopausia", "sindrome-ovario-poliquistico", "candidiasis-vaginal-repeticion",
                                 "suelo-pelvico-dolor-pelvico", "dolor-pelvico-barcelona", "ejercicios-suelo-pelvico", "cistitis-repeticion-vejiga-dolorosa", "acompanamiento-fertilidad"]),
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
    ("Patologías musculoesqueléticas y osteoarticulares", [
        ("Artrosis", "artrosis"), ("Bursitis", "hombro-doloroso"), ("Capsulitis", "hombro-doloroso"), ("Cervicalgia", "cervicalgia-dolor-cuello"),
        ("Ciática", "ciatica"), ("Condromalacia rotuliana", "dolor-rodilla-condromalacia"), ("Contracturas y desgarros musculares", "contracturas-desgarros-musculares"),
        ("Dorsalgia", "dorsalgia-dolor-espalda-alta"), ("Esguinces", "esguinces"), ("Esguince cervical", "cervicalgia-dolor-cuello"),
        ("Fascitis plantar", "fascitis-plantar"), ("Fibromialgia", "fibromialgia"), ("Hernias de disco incipientes", "hernia-disco-incipiente"),
        ("Lumbalgia", "lumbalgia-dolor-lumbar"), ("Neuralgia de Arnold", "cervicalgia-dolor-cuello"), ("Neuralgia del trigémino", "neuralgia-trigemino"),
        ("Osteoporosis", "osteoporosis"), ("Problemas de la ATM y bruxismo", "bruxismo-dolor-mandibular-atm"), ("Sarcopenia", "osteoporosis"),
        ("Síndrome del túnel carpiano", "tunel-carpiano"), ("Tendinitis", "hombro-doloroso"), ("Tortícolis", "torticolis"),
        ("Dolor neuropático", "dolor-neuropatico"), ("Vértigo y mareo", "vertigo-mareo"), ("Acúfenos (tinnitus)", "acufenos"),
        ("Cicatrices y adherencias", "cicatrices-adherencias"), ("Lesiones deportivas", "lesiones-deportivas"), ("Osteopatía en bebés y niños", "osteopatia-bebes-ninos"),
        ("Fascia y liberación miofascial", "osteopatia-fascia-barcelona"), ("Trauma físico y emocional", "osteopatia-trauma")]),
    ("Patologías inflamatorias crónicas y autoinmunes", [
        ("Alergias", "alergias-asma-infecciones"), ("Artritis y artritis reumatoide", "inflamacion-cronica-autoinmunes"), ("Asma", "alergias-asma-infecciones"),
        ("Candidiasis", "candidiasis-vaginal-repeticion"), ("Colitis y gastritis", "digestiones-pesadas-gastritis"), ("Fibromialgia", "fibromialgia"),
        ("Infecciones de repetición", "alergias-asma-infecciones"), ("Migrañas y cefaleas", "cefaleas-migrana"),
        ("Problemas autoinmunes de la piel: eccemas, atopia", "inflamacion-cronica-autoinmunes"), ("Síndrome de dolor crónico", "dolor-persistente-cronico")]),
    ("Patologías intestinales", [
        ("Diarrea", "diarrea-cronica"), ("Estreñimiento", "estrenimiento"), ("Disbiosis intestinal y estudio de microbiota", "salud-digestiva-microbiota"),
        ("Digestiones pesadas", "digestiones-pesadas-gastritis"), ("Reflujo y acidez", "reflujo-acidez"),
        ("Enfermedad inflamatoria intestinal: Crohn, colitis ulcerosa", "enfermedad-inflamatoria-intestinal"), ("Gases", "gases-hinchazon-abdominal"),
        ("Hinchazón y distensión abdominal", "gases-hinchazon-abdominal"), ("Colon irritable (SII)", "colon-irritable-sibo"), ("SIBO y LIBO", "colon-irritable-sibo"),
        ("Intolerancias alimentarias", "intolerancias-alimentarias"), ("Sensibilidad al gluten", "intolerancia-gluten"), ("Intolerancia a la lactosa", "intolerancia-lactosa"),
        ("Intolerancia a la fructosa", "intolerancia-fructosa"), ("Intolerancia a la histamina", "intolerancia-histamina")]),
    ("Patologías metabólicas y cardiovasculares", [
        ("Adicción al azúcar, chocolate o refrescos", None), ("Alcoholismo", None), ("Déficit de hierro, vitaminas y minerales", None),
        ("Hígado graso", "salud-metabolica"), ("Hipertensión", "salud-metabolica"), ("Prevención cardiovascular", "salud-metabolica"),
        ("Resistencia a la insulina", "salud-metabolica"), ("Síndrome metabólico", "salud-metabolica"), ("Sobrepeso y obesidad", "perdida-de-peso-sarria-sant-gervasi"),
        ("Tabaquismo", "dejar-de-fumar-acupuntura")]),
    ("Agotamiento físico y emocional", [
        ("Agotamiento físico y emocional", "agotamiento-fisico-emocional"), ("Estado de ánimo bajo", "agotamiento-fisico-emocional"),
        ("Fatiga crónica", "fatiga-cronica-agotamiento"), ("Cansancio extremo", "fatiga-cronica-agotamiento"), ("Insomnio y trastornos del sueño", "sueno-insomnio"),
        ("Shock emocional", "agotamiento-fisico-emocional"), ("Estrés y ansiedad", "estres-ansiedad"), ("Cortisol y estrés crónico", "cortisol-estres-cronico"),
        ("Nervio vago", "nervio-vago")]),
    ("Ginecología y salud pélvica", [
        ("Acné en mujeres", "sindrome-ovario-poliquistico"), ("Candidiasis vaginal recurrente", "candidiasis-vaginal-repeticion"),
        ("Cistitis recurrente", "cistitis-repeticion-vejiga-dolorosa"), ("Infertilidad y abortos recurrentes", "acompanamiento-fertilidad"),
        ("Menopausia y sofocos", "salud-mujer-menopausia"), ("Ovarios poliquísticos (SOP)", "sindrome-ovario-poliquistico"),
        ("Suelo pélvico", "suelo-pelvico-dolor-pelvico"), ("Dolor pélvico", "dolor-pelvico-barcelona"), ("Ejercicios de suelo pélvico", "ejercicios-suelo-pelvico"),
        ("Dolor menstrual y endometriosis", "dolor-menstrual-endometriosis"), ("Neuralgia del pudendo", "neuralgia-pudendo"),
        ("Dolor en las relaciones", "dispareunia-dolor-relaciones"), ("Incontinencia urinaria", "incontinencia-urinaria-esfuerzo"),
        ("Prolapso", "prolapso-organos-pelvicos"), ("Embarazo y posparto", "osteopatia-embarazo-posparto"), ("Dolor de coxis", "dolor-coxis-coccigodinia")]),
    ("Problemas endocrinos", [
        ("Tiroiditis de Hashimoto temprana", "hipotiroidismo-hashimoto"), ("Hipotiroidismo leve", "hipotiroidismo-hashimoto"),
        ("Hipertiroidismo", None), ("Trastornos de la prolactina", None)]),
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
AREA_BLOCKS = [
    ("01 · Aparato locomotor", "Sistema musculoesquelético y dolor", "Dolor articular, muscular y vertebral, agudo o persistente.",
     "Combinamos osteopatía, acupuntura, ejercicio adaptado y educación en dolor, y trabajamos los factores que mantienen el dolor: sueño, estrés, sedentarismo e inflamación.",
     ["[Osteopatía](osteopatia-sarria-sant-gervasi)", "[Acupuntura](acupuntura-medicina-tradicional-china)", "[Masaje terapéutico](masajes-sarria-sant-gervasi)"]),
    ("02 · Inflamación e inmunidad", "Inflamación crónica, inmunidad y piel", "Procesos en los que la respuesta inflamatoria y la inmunidad desempeñan un papel central.",
     "Trabajamos desde la PNIE: alimentación antiinflamatoria, salud intestinal y microbiota, regulación del estrés y del sueño.",
     ["[PNIE](pni-pnie-barcelona)", "[Nutrición y salud intestinal](nutricion-salud-intestinal)"]),
    ("03 · Aparato digestivo", "Aparato digestivo", "Los trastornos digestivos son uno de los motivos de consulta más frecuentes en WA LAM.",
     "Analizamos el eje intestino-cerebro, la alimentación, los horarios, el estrés y la microbiota; solicitamos un estudio de microbiota cuando aporta información y diseñamos un plan nutricional, de PNIE y, si procede, de acupuntura y osteopatía visceral.",
     ["[Nutrición y salud intestinal](nutricion-salud-intestinal)", "[PNIE](pni-pnie-barcelona)", "[Osteopatía visceral](osteopatia-visceral-barcelona)"]),
    ("04 · Metabolismo", "Metabolismo y salud cardiovascular", "Factores de riesgo metabólico y cardiovascular que dependen en gran medida del estilo de vida.",
     "Plan de alimentación individualizado, actividad física, acupuntura como apoyo y seguimiento de los parámetros analíticos.",
     ["[Longevidad y prevención](prevencion-longevidad)", "[Nutrición y salud intestinal](nutricion-salud-intestinal)"]),
    ("05 · Sistema nervioso", "Agotamiento, estrés y sueño", "Situaciones en las que el sistema nervioso, el sueño y la capacidad de adaptación están comprometidos.",
     "Regulación del sistema nervioso con mindfulness, respiración, acupuntura, osteopatía craneal y hábitos de sueño, y revisión de los factores físicos que contribuyen a la fatiga.",
     ["[Mindfulness](mindfulness-barcelona)", "[Neurolongevidad y salud cognitiva](neurolongevidad-salud-cognitiva)", "[Curso MBSR](curso-mindfulness-mbsr-barcelona)", "[Yoga terapéutico](yoga-particular-grupos-reducidos)", "[Qigong (chi kung)](qigong-barcelona)", "[Estiramientos](clases-estiramientos)"]),
    ("06 · Salud de la mujer", "Ginecología y salud pélvica", "Etapas y procesos específicos de la salud femenina.",
     "Nutrición, microbiota, regulación del estrés, acupuntura y osteopatía urogenital de abordaje externo.",
     ["[Osteopatía urogenital](suelo-pelvico-dolor-pelvico)", "[Drenaje en el embarazo](drenaje-linfatico-embarazo)"]),
    ("07 · Sistema endocrino", "Sistema endocrino", "Alteraciones hormonales en las que el estilo de vida tiene un papel importante.",
     "Alimentación, salud intestinal, sueño y regulación del estrés.",
     ["[PNIE](pni-pnie-barcelona)", "[Menopausia](salud-mujer-menopausia)"]),
]

WORK_STEPS = [
    ("Antes de la primera visita", "Me envías los análisis y las pruebas médicas recientes que consideres relevantes para tu problema."),
    ("Primera consulta", "Dura unos 60 minutos. Si lo considero necesario, solicito pruebas más específicas, como un estudio de microbiota, para centrar el diagnóstico."),
    ("Tratamiento por fases", "Organizo el tratamiento en fases, normalmente dos o tres, adaptándome a cada paciente."),
    ("Recomendaciones", "Al terminar cada consulta, presencial u online, recibes las recomendaciones para la fase que iniciamos."),
    ("Dudas entre sesiones", "Si te surgen dudas, puedes escribirme antes de la siguiente sesión."),
    ("Mantenimiento", "Al terminar el tratamiento, recibes las pautas de mantenimiento para consolidar la mejoría."),
]


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
        for (ey, h2, intro, ptxt, li), (_, items) in zip(AREA_BLOCKS, HOME_LIST):
            ind = [f"[{lab}]({s})" if s in known else lab for lab, s in items]
            new.append({"type": "cards", "eyebrow": ey, "h2": h2, "intro": intro,
                        "items": [{"k": "Indicaciones", "h": "Motivos de consulta frecuentes", "li": ind},
                                  {"k": "Nuestro abordaje", "h": "Cómo lo abordamos", "p": ptxt, "li": [x for x in li if x.split("](")[1][:-1] in known]}]})
        bl[i:i] = new
