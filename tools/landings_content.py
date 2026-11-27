# -*- coding: utf-8 -*-
"""Textos de las landing pages de WA LAM.

Marcado:  **negrita**   *turquesa*   [[dato pendiente de completar]]
"""

SITE = {
    "base": "https://www.walambcn.com",
    "booking": "https://www.walambcn.com/book-online",
    "wa": "34675716409",
    "email": "contacto@walambcn.com",
    "address": "Sarrià-Sant Gervasi",
    "address_short": "Sarrià–Sant Gervasi, Barcelona",
}

# Referencias verificadas (DOI comprobado en PubMed / Cochrane / editorial, nov. 2026)
def _r(t, doi):
    return {"t": t, "doi": doi}


R = {
    "qaseem": _r("Qaseem A, Wilt TJ, McLean RM, Forciea MA, et al., 2017. «Noninvasive Treatments for Acute, Subacute, and Chronic Low Back Pain: A Clinical Practice Guideline From the American College of Physicians». Annals of Internal Medicine.", "10.7326/M16-2367"),
    "hayden": _r("Hayden JA, Ellis J, Ogilvie R, Malmivaara A, van Tulder MW, 2021. «Exercise therapy for chronic low back pain». Cochrane Database of Systematic Reviews.", "10.1002/14651858.CD009790.pub2"),
    "rubinstein": _r("Rubinstein SM, de Zoete A, van Middelkoop M, Assendelft WJJ, de Boer MR, van Tulder MW, 2019. «Benefits and harms of spinal manipulative therapy for the treatment of chronic low back pain: systematic review and meta-analysis of randomised controlled trials». BMJ.", "10.1136/bmj.l689"),
    "vickers": _r("Vickers AJ, et al., 2018. «Acupuncture for Chronic Pain: Update of an Individual Patient Data Meta-Analysis». The Journal of Pain.", "10.1016/j.jpain.2017.11.005"),
    "goyal": _r("Goyal M, et al., 2014. «Meditation Programs for Psychological Stress and Well-being: A Systematic Review and Meta-analysis». JAMA Internal Medicine.", "10.1001/jamainternmed.2013.13018"),
    "cherkin": _r("Cherkin DC, et al., 2016. «Effect of Mindfulness-Based Stress Reduction vs Cognitive Behavioral Therapy or Usual Care on Back Pain and Functional Limitations in Adults With Chronic Low Back Pain: A Randomized Clinical Trial». JAMA.", "10.1001/jama.2016.2323"),
    "hoge": _r("Hoge EA, Bui E, Mete M, Dutton MA, Baker AW, Simon NM, 2023. «Mindfulness-Based Stress Reduction vs Escitalopram for the Treatment of Adults With Anxiety Disorders: A Randomized Clinical Trial». JAMA Psychiatry.", "10.1001/jamapsychiatry.2022.3679"),
    "segerstrom": _r("Segerstrom SC, Miller GE, 2004. «Psychological Stress and the Human Immune System: A Meta-Analytic Study of 30 Years of Inquiry». Psychological Bulletin.", "10.1037/0033-2909.130.4.601"),
    "irwin": _r("Irwin MR, Olmstead R, Carroll JE, 2016. «Sleep Disturbance, Sleep Duration, and Inflammation: A Systematic Review and Meta-Analysis of Cohort Studies and Experimental Sleep Deprivation». Biological Psychiatry.", "10.1016/j.biopsych.2015.05.014"),
    "cryan": _r("Cryan JF, O'Riordan KJ, Cowan CSM, et al., 2019. «The Microbiota-Gut-Brain Axis». Physiological Reviews.", "10.1152/physrev.00018.2018"),
    "black": _r("Black CJ, Staudacher HM, Ford AC, 2022. «Efficacy of a low FODMAP diet in irritable bowel syndrome: systematic review and network meta-analysis». Gut.", "10.1136/gutjnl-2021-325214"),
    "guillaud_v": _r("Guillaud A, Darbois N, Monvoisin R, Pinsault N, 2018. «Reliability of diagnosis and clinical efficacy of visceral osteopathy: a systematic review». BMC Complementary and Alternative Medicine.", "10.1186/s12906-018-2098-8"),
    "guillaud_c": _r("Guillaud A, Darbois N, Monvoisin R, Pinsault N, 2016. «Reliability of Diagnosis and Clinical Efficacy of Cranial Osteopathy: A Systematic Review». PLOS ONE.", "10.1371/journal.pone.0167823"),
    "smith": _r("Smith CA, et al., 2018. «Effect of Acupuncture vs Sham Acupuncture on Live Births Among Women Undergoing In Vitro Fertilization: A Randomized Clinical Trial». JAMA.", "10.1001/jama.2018.5336"),
    "nams": _r("The North American Menopause Society, 2022. «The 2022 hormone therapy position statement of The North American Menopause Society». Menopause.", "10.1097/GME.0000000000002028"),
    "momma": _r("Momma H, Kawakami R, Honda T, Sawada SS, 2022. «Muscle-strengthening activities are associated with lower risk and mortality in major non-communicable diseases: a systematic review and meta-analysis of cohort studies». British Journal of Sports Medicine.", "10.1136/bjsports-2021-105061"),
    "ekelund": _r("Ekelund U, et al., 2019. «Dose-response associations between accelerometry measured physical activity and sedentary time and all cause mortality: systematic review and harmonised meta-analysis». BMJ.", "10.1136/bmj.l4570"),
    "wieland": _r("Wieland LS, Skoetz N, Pilkington K, Harbin S, Vempati R, Berman BM, 2022. «Yoga for chronic non-specific low back pain». Cochrane Database of Systematic Reviews.", "10.1002/14651858.CD010671.pub3"),
    "sherrington": _r("Sherrington C, et al., 2019. «Exercise for preventing falls in older people living in the community». Cochrane Database of Systematic Reviews.", "10.1002/14651858.CD012424.pub2"),
    "white_smoke": _r("White AR, Rampes H, Liu JP, Stead LF, Campbell J, 2014. «Acupuncture and related interventions for smoking cessation». Cochrane Database of Systematic Reviews.", "10.1002/14651858.CD000009.pub4"),
    "lindson": _r("Lindson N, Theodoulou A, Ordóñez-Mena JM, et al., 2023. «Pharmacological and electronic cigarette interventions for smoking cessation in adults: component network meta-analyses». Cochrane Database of Systematic Reviews.", "10.1002/14651858.CD015226.pub2"),
    "qaseem_ins": _r("Qaseem A, Kansagara D, Forciea MA, Cooke M, Denberg TD, 2016. «Management of Chronic Insomnia Disorder in Adults: A Clinical Practice Guideline From the American College of Physicians». Annals of Internal Medicine.", "10.7326/M15-2175"),
    "riemann": _r("Riemann D, et al., 2023. «The European Insomnia Guideline: An update on the diagnosis and treatment of insomnia 2023». Journal of Sleep Research.", "10.1111/jsr.14035"),
    "lancet_dem": _r("Livingston G, Huntley J, Liu KY, et al., 2024. «Dementia prevention, intervention, and care: 2024 report of the Lancet standing Commission». The Lancet.", "10.1016/S0140-6736(24)01296-0"),
    "finger": _r("Ngandu T, et al., 2015. «A 2 year multidomain intervention of diet, exercise, cognitive training, and vascular risk monitoring versus control to prevent cognitive decline in at-risk elderly people (FINGER): a randomised controlled trial». The Lancet.", "10.1016/S0140-6736(15)60461-5"),
    "horvath": _r("Horvath JC, Forte JD, Carter O, 2015. «Quantitative Review Finds No Evidence of Cognitive Effects in Healthy Populations From Single-session Transcranial Direct Current Stimulation (tDCS)». Brain Stimulation.", "10.1016/j.brs.2015.01.400"),
    "ezzo": _r("Ezzo J, Manheimer E, McNeely ML, et al., 2015. «Manual lymphatic drainage for lymphedema following breast cancer treatment». Cochrane Database of Systematic Reviews.", "10.1002/14651858.CD003475.pub2"),
    "chien": _r("Chien TJ, Liu CY, Fang CJ, 2019. «The Effect of Acupuncture in Breast Cancer-Related Lymphedema (BCRL): A Systematic Review and Meta-Analysis». Integrative Cancer Therapies.", "10.1177/1534735419866910"),
    "tens": _r("Johnson MI, Paley CA, Jones G, Mulvey MR, Wittkopf PG, 2022. «Efficacy and safety of transcutaneous electrical nerve stimulation (TENS) for acute and chronic pain in adults: a systematic review and meta-analysis of 381 studies (the meta-TENS study)». BMJ Open.", "10.1136/bmjopen-2021-051073"),
    "fregni": _r("Fregni F, El-Hagrassy MM, Pacheco-Barrios K, et al., 2021. «Evidence-Based Guidelines and Secondary Meta-Analysis for the Use of Transcranial Direct Current Stimulation in Neurological and Psychiatric Disorders». International Journal of Neuropsychopharmacology.", "10.1093/ijnp/pyaa051"),
    "haller": _r("Haller H, Lauche R, Sundberg T, Dobos G, Cramer H, 2020. «Craniosacral therapy for chronic pain: a systematic review and meta-analysis of randomized controlled trials». BMC Musculoskeletal Disorders.", "10.1186/s12891-019-3017-y"),
    "sio_asco": _r("Mao JJ, Ismaila N, Bao T, et al., 2022. «Integrative Medicine for Pain Management in Oncology: Society for Integrative Oncology–ASCO Guideline». Journal of Clinical Oncology.", "10.1200/JCO.22.01357"),
    "klaus": _r("Klaus LC, et al., 2024. «Reflexology in oncological treatment – a systematic review». BMC Complementary Medicine and Therapies.", "10.1186/s12906-023-04220-4"),
}

GROUPS = {
    "home": {"label": "Portada", "nav": "Inicio", "hub": "", "title": "Portada", "eyebrow": "", "intro": ""},
    "motivo": {"label": "Motivo de consulta", "nav": "¿En qué te puedo ayudar?", "hub": "tratamientos",
               "eyebrow": "¿En qué te puedo ayudar?", "title": "Empieza por lo que te ocurre",
               "intro": "Si todavía no sabes qué tratamiento necesitas, empieza aquí. Cada página explica cómo valoramos ese motivo de consulta y qué profesionales pueden acompañarte."},
    "servicio": {"label": "Servicio", "nav": "Servicios y terapias", "hub": "tratamientos",
                 "eyebrow": "Servicios y terapias", "title": "Especialidades y servicios",
                 "intro": "Las disciplinas que combinamos en WA LAM, en Sarrià–Sant Gervasi, dentro de un mismo plan integrativo."},
    "academia": {"label": "Healthy Lifestyle Academy", "nav": "Academia", "hub": "healthy-lifestyle-academy",
                 "eyebrow": "Healthy Lifestyle Academy", "title": "Aprender a cuidarte",
                 "intro": "Programas, clases, formaciones y retiros para incorporar hábitos de salud que se sostienen en el tiempo."},
}


def ficha(k, h, p, rows, btn=None):
    d = {"type": "pro", "k": k, "h": h, "p": p, "rows": rows}
    if btn:
        d["btn"] = btn
    return d


ROWS_SERVICIO = [
    ("Profesional", "[[Nombre y titulación]]"),
    ("Nº de colegiado/a", "[[Nº colegiado/a]]"),
    ("Duración", "[[min]]"),
    ("Precio", "[[€]]"),
    ("Dónde", "Sarrià–Sant Gervasi, Barcelona"),
]

PAGES = []

# ---------------------------------------------------------------- PORTADA
PAGES.append({
    "slug": "medicina-integrativa-barcelona", "group": "home", "wave": 1,
    "nav": "Medicina integrativa en Barcelona",
    "card": "Página principal: qué es la medicina integrativa, la medicina 5P, cómo es el tratamiento y motivos de consulta.",
    "title": "Medicina integrativa en Barcelona · Sarrià–Sant Gervasi | WA LAM",
    "desc": "Medicina integrativa en Sarrià–Sant Gervasi (Barcelona): abordamos tu motivo de consulta mirando más allá del síntoma local. Primera visita: 60 min · 90 €.",
    "eyebrow": "Medicina integrativa · Sarrià–Sant Gervasi",
    "h1": "Medicina integrativa en Barcelona para cuidar tu salud física, mental y emocional",
    "sub": "Un enfoque clínico que mira a la persona entera, no solo al síntoma",
    "lead": "En WA LAM acompañamos a personas que quieren entender su salud y cuidarla. Unimos la osteopatía, la acupuntura, la nutrición y el mindfulness en tratamientos personalizados, con tiempo, escucha activa y rigor clínico.",
    "facts_title": "Te ayudamos a",
    "facts": ["Entender qué le pasa a tu cuerpo y por qué", "Mejorar tu energía, tu equilibrio emocional y tu salud", "Prevenir y tratar desequilibrios desde una visión global e integrativa"],
    "cta2": ("Qué es la medicina integrativa", "#que-es-la-medicina-integrativa"),
    "wa": "Hola, me gustaría información sobre la medicina integrativa en WA LAM.",
    "blocks": [
        {"type": "explain", "eyebrow": "Nuestro enfoque", "h2": "Cómo practicamos la medicina integrativa en WA LAM",
         "paras": ["Si vienes, por ejemplo, por un dolor de hombro, valoramos el hombro, pero también la postura, las vísceras, la digestión, el sueño o el estrés que pueden estar contribuyendo a que el dolor aparezca o no termine de resolverse.",
                   "En WA LAM la practicamos como una **medicina sin prisas** (*slow medicine*): tiempo para escucharte, para entender tu historia y para explicarte qué ocurre y por qué. Una medicina centrada en la persona, no en el reloj."]},
        {"type": "cards", "eyebrow": "Slow medicine", "h2": "Una medicina sin prisas",
         "items": [{"h": "Una primera visita sin prisas", "p": "Sesenta minutos para entender qué te preocupa y revisar tu historia clínica y las pruebas que ya tengas. Si tus analíticas son recientes, las utilizamos: no repetimos pruebas sin motivo."},
                   {"h": "Un plan por orden de impacto", "p": "Recomendaciones claras y priorizadas, con un número orientativo de sesiones desde el principio."},
                   {"h": "Una mirada que integra", "p": "Las distintas disciplinas se combinan en un mismo tratamiento, en lugar de verte por partes."}]},
        {"type": "explain", "eyebrow": "WA LAM", "h2": "¿Qué es WA LAM?",
         "paras": ["WA LAM es un centro de medicina integrativa en Sarrià–Sant Gervasi (Barcelona), en funcionamiento desde 2004, que nace con el propósito de cuidar la salud de las personas desde un enfoque que une ciencia, experiencia clínica y una visión humana. Nuestra misión es acompañarte para que recuperes tu equilibrio y mejores tu calidad de vida. Además, en la [Healthy Lifestyle Academy](https://www.walambcn.com/academia-vida-saludable-barcelona) compartimos formación y actividades para cuidar tu salud en el día a día."]},
        {"type": "cards", "eyebrow": "WA LAM", "h2": "Conoce tu cuerpo, cuida tu mente, toma las riendas de tu salud",
         "items": [{"h": "Un enfoque consciente y preventivo para potenciar tu vitalidad"}, {"h": "Un acompañamiento comprometido con tu evolución"}, {"h": "Una mirada integrativa que conecta cuerpo, mente y emociones"}]},
        {"type": "cards", "eyebrow": "¿Por qué WA LAM?", "h2": "¿Por qué WA LAM?",
         "intro": "Medicina integrativa con más de treinta años de experiencia clínica en Barcelona.",
         "items": [{"h": "Abordaje personalizado", "p": "Cada tratamiento se diseña a partir de tu historia, tu exploración y tus objetivos."},
                   {"h": "Una visión médica integrativa", "p": "Osteopatía, medicina integrativa y PNIE para estudiar la causa, no solo el síntoma: cuerpo, digestión, sueño y estrés se valoran juntos."},
                   {"h": "Más de treinta años de experiencia", "p": "Dirección clínica de Rosa María Rodríguez Valls, osteópata D.O. y máster en medicina integrativa."},
                   {"h": "Terapias con respaldo científico", "p": "Utilizamos las terapias que cuentan con evidencia y explicamos con transparencia sus límites."},
                   {"h": "Método re:trace", "p": "Un plan por fases, con objetivos claros, recomendaciones para casa y seguimiento."},
                   {"h": "Longevidad y salud a largo plazo", "p": "Prevención, neurolongevidad y hábitos que se mantienen en el tiempo."}]},
        {"type": "cards", "eyebrow": "Transformación WA LAM", "h2": "Basada en la medicina 5P",
         "intro": "Una atención en la que distintas disciplinas se combinan para cuidar tu salud y tu equilibrio, basada en los cinco principios de la medicina 5P.",
         "items": [{"k": "P1", "h": "Predicción", "p": "Identificar los factores de riesgo y las señales tempranas antes de que un problema se cronifique."},
                   {"k": "P2", "h": "Prevención", "p": "Actuar sobre los hábitos y los factores que mantienen el desequilibrio para evitar que reaparezca."},
                   {"k": "P3", "h": "Personalización", "p": "Dos personas con el mismo síntoma pueden necesitar tratamientos distintos: el plan se adapta a cada una."},
                   {"k": "P4", "h": "Participación", "p": "Te explicamos qué ocurre y por qué, para que participes activamente en tu proceso."},
                   {"k": "P5", "h": "Precisión", "p": "Las decisiones se basan en tu historia, tu exploración y, cuando aportan información, tus analíticas."}]},

    ],
    "faq": [
        ("¿Qué relación tiene con la medicina convencional?", "La medicina integrativa trabaja junto a la medicina convencional: incorpora las terapias que disponen de respaldo científico y pone a la persona, su historia y sus hábitos en el centro de la atención."),
        ("¿Cuánto dura y cuánto cuesta la primera visita?", "Dura sesenta minutos y cuesta 90 €."),
        ("¿Necesito un diagnóstico para venir?", "No. Puedes venir con un diagnóstico o simplemente porque notas que algo no va bien. En la primera visita revisamos tu historia y las pruebas que ya tengas y, si hace falta alguna más, te lo indicamos."),
    ],
    "related": [],
    "cta": {"h2": "Reserva tu primera visita", "p": "Escríbenos por WhatsApp y te orientamos sobre tu caso."},
})

# ---------------------------------------------------------------- PROGRAMAS re:trace
WA_P = "Hola, me gustaría información sobre los programas re:trace."
P1 = ["Evaluación integral inicial de salud y longevidad, con estudios genéticos, epigenéticos, microbiota intestinal, biomarcadores metabólicos, inflamatorios y hormonales, salud cardiovascular, nutrición, función cognitiva, sueño, estrés y composición corporal.",
 "24 sesiones individuales presenciales de 60 minutos, dos por semana.",
 "Plan personalizado de medicina integrativa y longevidad basado en la evaluación inicial.",
 "Nutrición antiinflamatoria personalizada, adaptada al metabolismo, los síntomas y las necesidades individuales.",
 "Programa de salud intestinal y microbiota, con pautas nutricionales para favorecer una alimentación diversa, la función digestiva y el equilibrio de los hábitos que influyen en el ecosistema intestinal.",
 "Evaluación de síntomas digestivos, tolerancia alimentaria y hábitos intestinales.",
 "Estrategias de alimentación con restricción horaria o ayuno, cuando sean adecuadas y seguras.",
 "Optimización del sueño mediante alimentación, horarios, exposición a la luz y sincronización de ritmos circadianos.",
 "Programa de reducción del estrés crónico y la ansiedad, con estrategias estructuradas de manejo del estrés y entrenamiento de la atención.",
 "Abordaje integrativo del dolor crónico, con evaluación funcional, tratamiento manual cuando corresponda, movimiento adaptado y educación en dolor.",
 "Programa de salud cognitiva y neurolongevidad: atención, memoria, concentración y hábitos de protección de la salud cerebral.",
 "Actividad física personalizada y mejora de la capacidad funcional.",
 "12 sesiones grupales educativas, una por semana.",
 "24 sesiones grupales de prácticas de mindfulness, meditación, yoga o chi kung, dos por semana.",
 "Acceso al curso MBSR grabado.",
 "Seguimiento personalizado durante las 12 semanas.",
 "Informe final de evolución y plan de continuidad."]
P2 = ["La misma evaluación integral avanzada del programa Premium.",
 "Programa individualizado de medicina integrativa, salud de precisión y longevidad.",
 "Tres fines de semana intensivos en Barcelona, uno al mes.",
 "Seis días de atención individual, con cuatro horas diarias: 24 horas de atención individual presencial.",
 "Plan de nutrición antiinflamatoria y optimización metabólica.",
 "Programa personalizado de salud intestinal y microbiota, mediante pautas alimentarias y seguimiento de síntomas digestivos.",
 "Estrategias de alimentación y ayuno cuando estén indicadas.",
 "Programa de optimización del sueño y sincronización de ritmos circadianos.",
 "Intervención sobre estrés crónico, ansiedad y hábitos relacionados con la recuperación.",
 "Abordaje integrativo del dolor crónico y de las limitaciones funcionales.",
 "Programa de salud cognitiva y neurolongevidad.",
 "Actividad física adaptada a la condición de cada participante.",
 "12 sesiones grupales educativas online.",
 "24 sesiones grupales de prácticas online.",
 "Acceso al curso MBSR grabado.",
 "Seguimiento personalizado durante las 12 semanas.",
 "Informe final de evolución y plan de continuidad."]
P3 = ["Evaluación integral avanzada previa de salud y longevidad.",
 "Revisión de resultados y preparación de un programa individualizado.",
 "Seis días consecutivos de intervención privada intensiva, con horario de atención acordado.",
 "Programa personalizado de medicina integrativa, salud de precisión y neurolongevidad.",
 "Plan nutricional antiinflamatorio adaptado a las necesidades individuales.",
 "Programa de salud intestinal y microbiota, con planificación de comidas y pautas digestivas.",
 "Organización de los horarios de alimentación, descanso y actividad según los ritmos circadianos.",
 "Estrategias de ayuno cuando sean adecuadas.",
 "Programa intensivo de manejo del estrés y reducción de la ansiedad.",
 "Abordaje del dolor crónico y de las alteraciones funcionales, cuando formen parte de los objetivos del participante.",
 "Optimización del sueño y de los hábitos de recuperación.",
 "Estrategias personalizadas de salud cognitiva y neurolongevidad.",
 "Actividad física adaptada y entrenamiento de hábitos saludables.",
 "Sesiones individuales de mindfulness y entrenamiento atencional.",
 "Plan personalizado de continuidad al finalizar la experiencia."]
P4 = ["Evaluación individual avanzada de salud y longevidad previa al retiro.",
 "Estudios genéticos, epigenéticos, microbiota intestinal, metabolismo, inflamación, hormonas, nutrición, función cognitiva, sueño y salud cardiovascular.",
 "Programa intensivo de medicina integrativa, salud de precisión y longevidad.",
 "Alimentación antiinflamatoria y pautas nutricionales individualizadas.",
 "Programa de salud intestinal y microbiota, adaptado a las necesidades digestivas de cada participante.",
 "Organización de horarios de alimentación y descanso según los ritmos circadianos.",
 "Estrategias de ayuno cuando sean adecuadas.",
 "Programa de reducción del estrés crónico y la ansiedad.",
 "Abordaje de hábitos relacionados con el dolor crónico y la recuperación funcional.",
 "Optimización del sueño y la recuperación nocturna.",
 "Sesiones de salud cognitiva y neurolongevidad.",
 "Actividad física adaptada, movilidad y mejora de la capacidad funcional.",
 "Sesiones educativas sobre metabolismo, inflamación, nutrición y longevidad.",
 "Prácticas diarias de mindfulness, meditación, yoga o chi kung.",
 "Orientaciones individuales según los resultados de la evaluación.",
 "Informe de recomendaciones y plan de continuidad."]
PROTO = [
 ("Analítica general", "Hemograma completo, función renal, función hepática, electrolitos y análisis de orina."),
 ("Metabolismo", "Glucosa, HbA1c, insulina, HOMA-IR, colesterol total, HDL, LDL, triglicéridos, ApoB, Lp(a) y ácido úrico."),
 ("Salud cardiovascular", "Presión arterial, frecuencia cardíaca, ECG y evaluación cardiovascular avanzada."),
 ("Inflamación", "PCR ultrasensible y otros marcadores inflamatorios."),
 ("Perfil hormonal", "TSH, T4 libre, FSH, LH, estradiol, progesterona, testosterona, SHBG, prolactina, DHEA-S y cortisol."),
 ("Nutrición y micronutrientes", "Hierro, ferritina, transferrina, vitamina B12, folato, vitamina D y otros nutrientes."),
 ("Genética", "Estudio de predisposiciones genéticas relevantes, riesgo metabólico y cardiovascular, farmacogenética y posibilidad de secuenciación genómica."),
 ("Epigenética", "Metilación del ADN, reloj epigenético y estimación exploratoria de la edad biológica."),
 ("Microbiota intestinal", "Estudio metagenómico, diversidad microbiana y composición bacteriana."),
 ("Salud digestiva", "Evaluación digestiva y pruebas específicas de parásitos, patógenos, inflamación intestinal, celiaquía o Helicobacter pylori cuando corresponda."),
 ("Salud cognitiva", "Evaluación de memoria, atención, concentración, velocidad de procesamiento y funciones ejecutivas."),
 ("Sueño", "Calidad del sueño, insomnio, somnolencia, diario de sueño, actigrafía y estudios especializados."),
 ("Estrés y ansiedad", "Cuestionarios validados de estrés, ansiedad y fatiga, y variabilidad de la frecuencia cardíaca como medida complementaria."),
 ("Composición corporal", "Masa muscular, porcentaje de grasa corporal, grasa visceral estimada y medidas antropométricas."),
 ("Longevidad funcional", "Fuerza de agarre, equilibrio, movilidad, velocidad de marcha y capacidad cardiorrespiratoria."),
 ("Salud sensorial", "Evaluación auditiva y visual.")]
PAGE_P = {
    "slug": "programas-re-trace", "group": "servicio", "wave": 1,
    "nav": "Programas re:trace",
    "card": "Cuatro programas de medicina integrativa, salud de precisión y longevidad: Premium, Immersive Weekends, Private Experience y Exclusive Retreats.",
    "title": "Programas re:trace · Medicina integrativa y longevidad en Barcelona | WA LAM",
    "desc": "Programas re:trace de WA LAM: Premium Barcelona (12 semanas), Immersive Weekends, Private Experience (6 días) y Exclusive Retreats. Evaluación avanzada de salud y longevidad.",
    "about": "Programas de medicina integrativa y longevidad",
    "eyebrow": "Clinical Framework for Regulation, Clinical Integration and Healthy Longevity",
    "h1": "Programas re:trace",
    "sub": "Retrace the origins. Reshape the trajectory.",
    "lead": "Cuatro programas construidos sobre el mismo método y el mismo protocolo de evaluación avanzada. Se diferencian en el formato, la intensidad y el grado de personalización, para adaptarse a tu agenda y a tu lugar de residencia.",
    "facts_title": "Programas",
    "facts": ["**re:trace Premium Barcelona** · 6.000 € · 12 semanas", "**re:trace Immersive Weekends** · 7.500 € · 12 semanas",
              "**re:trace Private Experience** · 6.000 € + gastos · 6 días", "**re:trace Exclusive Retreats** · 3.000 € por persona + gastos · 6–7 días",
              "Protocolo de evaluación avanzada común"],
    "cta2": ("Ver el protocolo de evaluación", "#protocolo-de-evaluacion-avanzada-re-trace"),
    "wa": WA_P,
    "blocks": [
        {"type": "explain", "eyebrow": "Qué es re:trace", "h2": "Research · Evidence · Trajectory · Regulation · Awareness · Clinical Integration · Evolution",
         "paras": ["**RE** — Research · Evidence. **TRACE** — Trajectory · Regulation · Awareness · Clinical Integration · Evolution.",
                   "re:trace es el método propio de WA LAM: rastrear los orígenes, es decir, los factores, conexiones y adaptaciones que han configurado tu estado de salud actual, para transformar su trayectoria. Un marco clínico para la regulación, la integración clínica y la longevidad saludable.",
                   "Los programas se complementan con la [Healthy Lifestyle Academy](https://www.walambcn.com/academia-vida-saludable-barcelona), donde se aprenden y se practican los hábitos del método, y con [Vacaciones con sentido](vacaciones-con-sentido), viajes formativos de salud integrativa."],
         "quote": "Retrace the origins. Reshape the trajectory."},
        {"type": "explain", "eyebrow": "Retrace the origins", "h2": "Rastrear los orígenes, transformar la trayectoria",
         "paras": [
             "En la salud, y especialmente en los problemas crónicos, casi nunca existe una única causa. **Rastrear los orígenes** significa volver sobre tu historia clínica, corporal y vital para identificar los factores que han configurado tu estado actual: antecedentes y trayectoria clínica; estrés, trauma y sistema nervioso; estructura, movimiento y dolor; sueño y ritmos circadianos; alimentación, microbiota y metabolismo; entorno, hábitos y exposoma; y capacidad de regulación y adaptación.",
             "No afirmamos haber encontrado «la causa»: comprendemos qué factores, conexiones y adaptaciones han contribuido a la situación actual. No borramos la historia ni prometemos empezar de cero; favorecemos una nueva trayectoria fisiológica y vital.",
             "Ese análisis se apoya en la **salud de precisión**: cada decisión clínica se adapta a tus biomarcadores, tu microbiota, tu perfil genético, tu contexto y tus objetivos. La dirección clínica corresponde a Rosa María Rodríguez Valls, osteópata D.O. y máster en medicina integrativa, con más de treinta años de experiencia clínica.",
         ],
         "quote": "El objetivo no es tratar una enfermedad, sino recuperar la salud de la persona que la padece."},
        {"type": "steps", "eyebrow": "Método propio", "h2": "Los siete principios de re:trace",
         "intro": "**RE** — Research · Evidence. **TRACE** — Trajectory · Regulation · Awareness · Clinical Integration · Evolution. Un marco clínico para la regulación, la integración clínica y la longevidad saludable, que estructura cada programa desde la primera visita hasta el mantenimiento.",
         "items": [("Research", "Investigación clínica individual: historia clínica, antecedentes, analíticas y pruebas previas y, cuando aportan información relevante, estudio de microbiota intestinal y pruebas genéticas."),
                   ("Evidence", "Cada intervención se selecciona según guías de práctica clínica, revisiones sistemáticas y metaanálisis, y se explica con transparencia su grado de evidencia."),
                   ("Trajectory", "La salud se analiza como una trayectoria, no como una imagen fija: de dónde vienes, en qué punto estás y qué factores están condicionando su evolución."),
                   ("Regulation", "Intervención sobre los sistemas reguladores del organismo: sistema nervioso autónomo, sueño y ritmos circadianos, eje intestino-cerebro e inflamación de bajo grado."),
                   ("Awareness", "Educación en salud y entrenamiento de la atención para que comprendas tu proceso y participes activamente en él, con el apoyo de la Healthy Lifestyle Academy."),
                   ("Clinical Integration", "Nutrición, acupuntura, terapias manuales, ejercicio y mindfulness se integran en un único plan terapéutico."),
                   ("Evolution", "Revisiones periódicas con objetivos definidos a lo largo del programa: el plan se adapta a tu evolución y, al finalizar, recibes pautas de mantenimiento.")],
         "note": "*Retrace the origins. Reshape the trajectory.* Rastrear los orígenes. Transformar la trayectoria."},
        {"type": "cards", "eyebrow": "El programa", "h2": "Cómo es un programa re:trace",
         "intro": "re:trace no es una sesión aislada, sino un plan de acción tan único como tu perfil biológico, diseñado según tus objetivos, preferencias y necesidades. Los cambios fisiológicos y de hábitos necesitan tiempo para consolidarse.",
         "items": [{"k": "1 · Primera visita", "h": "Valoración clínica completa", "p": "Sesión de 60 minutos (90 €) con una anamnesis exhaustiva: antecedentes y trayectoria clínica, hábitos, sueño, estrés, digestión, movimiento y entorno, y revisión de tus analíticas y pruebas. Según tu caso, se completa con la [valoración de precisión](prevencion-longevidad)."},
                   {"k": "2 · Propuesta", "h": "Programa y presupuesto personalizados", "p": "Con los datos de la valoración diseñamos tu programa re:trace: qué conviene retirar, qué necesita reequilibrarse y qué incorporar, qué tipo de ejercicio es adecuado para ti y a qué ritmo avanzar, de forma gradual o más intensiva según cómo vivas los cambios. Te recomendamos el [programa re:trace](programas-re-trace) más adecuado."},
                   {"k": "3 · Programa", "h": "12 semanas, en tres fases", "p": "El programa base dura 12 semanas, tres bloques de cuatro semanas, y puede prolongarse según tu evolución.",
                    "li": ["**Retirar**: eliminar los factores que mantienen el desequilibrio, como alimentos mal tolerados, hábitos o exposiciones; la alimentación antiinflamatoria es el eje de esta fase", "**Reequilibrar**: regular la digestión, la microbiota, el sueño, el estrés y la inflamación", "**Incorporar**: consolidar nuevos hábitos de alimentación, movimiento y descanso"]},
                   {"k": "4 · Mantenimiento", "h": "Consolidar los resultados", "p": "Al finalizar recibes un plan de mantenimiento para sostener los cambios en tu día a día."}]},
        {"type": "explain", "eyebrow": "Para quién es", "h2": "Cuando necesitas un cambio de fondo",
         "paras": ["re:trace no es una consulta para un problema puntual. Está pensado para quien llega con varias cosas a la vez (una alimentación que sabe que no es adecuada, mucho estrés, dolores, cansancio, mal descanso) y siente que necesita un cambio profundo, un *reset*.",
                   "En esos casos reunimos todo lo que sabemos, combinamos las terapias y las herramientas más adecuadas y diseñamos un programa para esa persona. Un cambio así necesita tiempo: por eso re:trace es un tratamiento de varios meses, con un número de sesiones definido desde el principio."]},
        {"type": "pack", "eyebrow": "Pack 1", "h2": "re:trace Premium Barcelona", "intro": "**6.000 € · 12 semanas**", "items": P1, "wa": WA_P},
        {"type": "pack", "eyebrow": "Pack 2", "h2": "re:trace Immersive Weekends", "intro": "**7.500 € · 12 semanas**", "items": P2,
         "notes": [("No incluye", "desplazamientos, alojamiento ni manutención en Barcelona.")], "wa": WA_P},
        {"type": "pack", "eyebrow": "Pack 3", "h2": "re:trace Private Experience", "intro": "**6.000 € + gastos · 6 días**", "items": P3,
         "notes": [("Ubicación", "entorno privado, hotel boutique o lugar acordado con el participante."), ("No incluye", "desplazamientos, alojamiento, manutención ni gastos logísticos.")], "wa": WA_P},
        {"type": "pack", "eyebrow": "Pack 4", "h2": "re:trace Exclusive Retreats", "intro": "**3.000 € por persona + gastos · 6–7 días · máximo 10 participantes**", "items": P4,
         "notes": [("Ubicación", "hotel boutique o entorno natural seleccionado."), ("No incluye, salvo presupuesto específico", "alojamiento, manutención, transporte ni desplazamientos.")], "wa": WA_P},
        {"type": "cards", "eyebrow": "Común a los cuatro programas", "h2": "Protocolo de evaluación avanzada re:trace",
         "intro": "No se incluyen densitometría ósea ni pruebas específicas de Alzheimer.",
         "items": [{"k": "%02d" % (i + 1), "h": h, "p": p} for i, (h, p) in enumerate(PROTO)]},
        {"type": "explain", "eyebrow": "Condiciones", "h2": "Condiciones de los programas",
         "paras": ["Los cuatro programas incluyen la coordinación de la evaluación avanzada, la revisión de los resultados aportados y su integración en el plan personalizado de re:trace.",
                   "Los costes de laboratorio, genética, epigenética, microbiota, pruebas de imagen y otras exploraciones externas se presupuestan y abonan por separado.",
                   "Las solicitudes médicas, los diagnósticos y los tratamientos que requieran prescripción se realizan a través de los profesionales sanitarios correspondientes.",
                   "Los estudios de microbiota y los relojes epigenéticos se utilizan teniendo en cuenta sus limitaciones clínicas actuales. Las intervenciones nutricionales, los ayunos y las demás estrategias se adaptan a la seguridad, las necesidades y los objetivos de cada persona."]},
    ],
    "faq": [
        ("¿Qué programa re:trace me conviene?", "Depende de tu disponibilidad y de tu lugar de residencia. Si vives en Barcelona, el Premium es el formato de referencia; si no puedes acudir cada semana, Immersive Weekends concentra el trabajo en tres fines de semana; si buscas una intervención intensiva e individual, Private Experience; y si prefieres una experiencia en grupo reducido, Exclusive Retreats."),
        ("¿Están incluidas las pruebas de laboratorio?", "No. Los programas incluyen la coordinación de la evaluación, la revisión de los resultados y su integración en tu plan. Los costes de laboratorio, genética, epigenética, microbiota, pruebas de imagen y otras exploraciones externas se presupuestan y abonan por separado."),
        ("¿Cómo empiezo?", "Con una primera visita de 60 minutos (90 €), en la que valoramos tu caso y te recomendamos el programa más adecuado."),
    ],
    "related": ["vacaciones-con-sentido", "retiros-mindfulness-meditacion-silencio", "prevencion-longevidad", "curso-mindfulness-mbsr-barcelona"],
    "cta": {"h2": "Empieza tu programa re:trace", "p": "Escríbenos por WhatsApp o reserva tu primera visita y te recomendaremos el programa más adecuado para ti."},
}

PAGES.append(PAGE_P)

# ---------------------------------------------------------------- EN QUÉ PODEMOS AYUDARTE
def grp(eyebrow, h2, intro, indic, abordaje, links, alerta=None):
    p2 = abordaje + (" " + alerta if alerta else "")
    return {"type": "cards", "eyebrow": eyebrow, "h2": h2, "intro": intro,
            "items": [{"k": "Indicaciones", "h": "Motivos de consulta frecuentes", "li": indic},
                      {"k": "Nuestro abordaje", "h": "Cómo lo abordamos", "p": p2, "li": links}]}

BLOCKS = [
 grp("01 · Aparato digestivo", "Aparato digestivo", "Los trastornos digestivos funcionales son uno de los motivos de consulta más frecuentes en WA LAM.",
     ["Acidez y reflujo gastroesofágico", "Gastritis y dispepsia (digestiones pesadas)", "Hinchazón y distensión abdominal", "Gases", "Estreñimiento y diarrea",
      "Síndrome del intestino irritable", "Disbiosis intestinal", "SIBO y LIBO", "Intolerancias alimentarias (lactosa, fructosa) y sensibilidad al gluten no celíaca",
      "Enfermedad inflamatoria intestinal (Crohn, colitis ulcerosa), como complemento del seguimiento digestivo"],
     "Analizamos el eje intestino-cerebro, la alimentación, los horarios, el estrés y la microbiota; solicitamos un estudio de microbiota cuando aporta información y diseñamos un plan nutricional, de PNIE y, si procede, de acupuntura.",
     ["[Salud digestiva y microbiota](salud-digestiva-microbiota)", "[Nutrición y salud intestinal](nutricion-salud-intestinal)", "[PNIE](pni-pnie-barcelona)"],
     "Ante signos de alarma, como dificultad para tragar, sangrado, anemia o pérdida de peso no explicada, es imprescindible una valoración médica previa."),
 grp("02 · Sistema musculoesquelético", "Sistema musculoesquelético y dolor", "Dolor articular, muscular y vertebral, agudo o persistente.",
     ["Lumbalgia, dorsalgia y cervicalgia", "Hernia discal en fase inicial", "Tortícolis y esguince cervical (latigazo)", "Neuralgia occipital (de Arnold)",
      "Trastornos de la articulación temporomandibular (ATM)", "Artrosis", "Tendinopatías, bursitis y capsulitis", "Fascitis plantar", "Condromalacia rotuliana",
      "Esguinces y roturas fibrilares", "Síndrome del túnel carpiano", "Fibromialgia", "Osteoporosis y sarcopenia"],
     "Combinamos técnicas manuales, ejercicio adaptado y educación en dolor, y revisamos los factores que mantienen el dolor: sueño, estrés, sedentarismo e inflamación.",
     ["[Lumbalgia y cervicalgia](lumbalgia-cervicalgia-cronica)", "[Dolor articular y miofascial](dolor-articular-miofascial)", "[Dolor musculoesquelético](dolor-musculoesqueletico)", "[Dolor neuropático](dolor-neuropatico)", "[Dolor persistente](dolor-persistente-cronico)"]),
 grp("03 · Inflamación e inmunidad", "Inflamación crónica, inmunidad y piel", "Procesos en los que la respuesta inflamatoria y la inmunidad desempeñan un papel central.",
     ["Alergias alimentarias y ambientales (pólenes, ácaros, epitelios de animales)", "Asma, como complemento de su tratamiento", "Dermatitis atópica, eccema y otras afecciones inflamatorias de la piel",
      "Migraña", "Infecciones de repetición", "Candidiasis", "Artritis y artritis reumatoide, como complemento del tratamiento reumatológico", "Síndrome de dolor crónico"],
     "Trabajamos desde la PNIE: alimentación antiinflamatoria, salud intestinal, regulación del estrés y del sueño, siempre como complemento del tratamiento médico.",
     ["[PNIE](pni-pnie-barcelona)", "[Salud digestiva y microbiota](salud-digestiva-microbiota)"]),
 grp("04 · Metabolismo", "Metabolismo y salud cardiovascular", "Factores de riesgo metabólico y cardiovascular que dependen en gran medida del estilo de vida.",
     ["Sobrepeso y obesidad", "Resistencia a la insulina", "Síndrome metabólico", "Hígado graso (esteatosis hepática metabólica)", "Hipertensión arterial, junto al tratamiento médico",
      "Prevención cardiovascular", "Déficit de hierro, vitaminas y minerales", "Tabaquismo", "Consumo de riesgo de alcohol, como apoyo complementario",
      "Conducta alimentaria compulsiva (azúcar, chocolate, bebidas azucaradas)"],
     "Intervención nutricional individualizada, actividad física, acupuntura como apoyo y seguimiento de los parámetros analíticos.",
     ["[Pérdida de peso](perdida-de-peso-sarria-sant-gervasi)", "[Dejar de fumar](dejar-de-fumar-acupuntura)", "[Longevidad y prevención](prevencion-longevidad)"]),
 grp("05 · Sistema nervioso", "Fatiga, estado de ánimo y sueño", "Situaciones en las que el sistema nervioso, el sueño y la capacidad de adaptación están comprometidos.",
     ["Fatiga persistente", "Agotamiento físico y emocional", "Estado de ánimo bajo", "Reacción a un acontecimiento vital estresante", "Insomnio", "Otros trastornos del sueño"],
     "Regulación del sistema nervioso autónomo con mindfulness, respiración, acupuntura y hábitos de sueño, y revisión de los factores físicos que contribuyen a la fatiga.",
     ["[Estrés y ansiedad](estres-ansiedad)", "[Sueño e insomnio](sueno-insomnio)", "[Neurolongevidad y salud cognitiva](neurolongevidad-salud-cognitiva)", "[Curso MBSR](curso-mindfulness-mbsr-barcelona)"],
     "Si los síntomas depresivos son intensos o persistentes, realizamos la derivación al profesional de salud mental correspondiente."),
 grp("06 · Salud de la mujer", "Salud de la mujer", "Etapas y procesos específicos de la salud femenina.",
     ["Menopausia y sofocos", "Síndrome de ovario poliquístico", "Acné de origen hormonal", "Candidiasis vaginal de repetición", "Cistitis de repetición",
      "Dolor pélvico y dismenorrea", "Dificultades para concebir y pérdida gestacional recurrente, como complemento del seguimiento ginecológico o de reproducción asistida", "Retención de líquidos en el embarazo y el posparto"],
     "Nutrición, microbiota, regulación del estrés, acupuntura y osteopatía urogenital de abordaje externo.",
     ["[Salud de la mujer y menopausia](salud-mujer-menopausia)", "[Dolor menstrual y endometriosis](dolor-menstrual-endometriosis)", "[Cistitis y vejiga dolorosa](cistitis-repeticion-vejiga-dolorosa)", "[Incontinencia de esfuerzo](incontinencia-urinaria-esfuerzo)", "[Embarazo y posparto](osteopatia-embarazo-posparto)", "[Suelo pélvico](suelo-pelvico-dolor-pelvico)", "[Fertilidad](acompanamiento-fertilidad)", "[Drenaje en el embarazo](drenaje-linfatico-embarazo)"]),
 grp("07 · Sistema endocrino", "Sistema endocrino", "Alteraciones hormonales en las que el estilo de vida puede complementar el tratamiento endocrinológico.",
     ["Hipotiroidismo subclínico o leve", "Tiroiditis de Hashimoto en fases iniciales", "Hipertiroidismo, como complemento del tratamiento endocrinológico",
      "Alteraciones de la prolactina (hiperprolactinemia)", "Otros desequilibrios hormonales"],
     "Como complemento del tratamiento endocrinológico: alimentación, salud intestinal, sueño y regulación del estrés, sin modificar en ningún caso la medicación prescrita.",
     ["[PNIE](pni-pnie-barcelona)", "[Salud de la mujer](salud-mujer-menopausia)"]),
 {"type": "evidence", "eyebrow": "Fundamento científico", "h2": "Por qué abordamos estos procesos de forma integrada",
  "items": [("Eje intestino-cerebro", "La microbiota intestinal se comunica de forma bidireccional con el sistema nervioso a través de vías neurales, endocrinas e inmunitarias (Cryan et al., Physiol Rev, 2019)."),
            ("Estrés e inmunidad", "El estrés crónico se asocia a la supresión de la respuesta inmunitaria celular y humoral (Segerstrom y Miller, Psychol Bull, 2004)."),
            ("Sueño e inflamación", "Las alteraciones del sueño se asocian a concentraciones más elevadas de PCR e IL-6 (Irwin et al., Biol Psychiatry, 2016)."),
            ("Dolor lumbar crónico", "Las intervenciones no farmacológicas, como el ejercicio, la acupuntura y el mindfulness, son el tratamiento de primera línea recomendado (Qaseem et al., Ann Intern Med, 2017).")],
  "refs": [R["cryan"], R["segerstrom"], R["irwin"], R["qaseem"]]},
]

PAGE = {
    "slug": "en-que-podemos-ayudarte", "group": "motivo", "wave": 1,
    "nav": "En qué te puedo ayudar",
    "card": "Indicaciones más frecuentes ordenadas por sistemas: digestivo, musculoesquelético, inmunidad, metabolismo, sueño, mujer y endocrino.",
    "title": "En qué te puedo ayudar · Medicina integrativa en Barcelona | WA LAM",
    "desc": "Acidez, colon irritable, SIBO, migraña, fibromialgia, lumbalgia, menopausia, hipotiroidismo, insomnio o sobrepeso: acompañamiento integrativo en Sarrià–Sant Gervasi.",
    "about": "Motivos de consulta en medicina integrativa",
    "eyebrow": "Motivos de consulta",
    "h1": "En qué te puedo ayudar",
    "sub": "Indicaciones más frecuentes en medicina integrativa · Sarrià–Sant Gervasi",
    "lead": "Estas son las situaciones clínicas por las que se consulta con más frecuencia en WA LAM, ordenadas por sistemas. En cada caso, analizamos los factores que han contribuido al cuadro actual y diseñamos un tratamiento complementario al seguimiento médico. Si tu motivo de consulta no aparece, escríbenos y te orientaremos.",
    "facts_title": "Antes de empezar",
    "facts": ["7 áreas clínicas · más de 60 indicaciones", "Primera visita: 60 min · 90 €", "Complementario al seguimiento médico",
              "Derivación al especialista cuando procede", "Atiende: Rosa María Rodríguez Valls"],
    "cta2": ("Ver aparato digestivo", "#aparato-digestivo"),
    "wa": "Hola, quería consultar si podéis ayudarme con mi caso.",
    "blocks": [{"type": "explain", "eyebrow": "Nuestro enfoque", "h2": "¿Qué es la medicina integrativa y cómo la practicamos en WA LAM?", "paras": ["La medicina integrativa es un enfoque basado en la evidencia científica que contempla a la persona en su globalidad, no solo el síntoma. En WA LAM aunamos el conocimiento científico actual y las terapias que cuentan con respaldo en la evidencia en un único plan terapéutico, diseñado de forma individual para cada paciente.", "Es para ti si llevas tiempo con molestias que no terminan de explicarse, si prefieres prevenir antes que tratar o si buscas un abordaje de [longevidad](prevencion-longevidad) con criterio clínico."]}, {"type": "cards", "eyebrow": "Cómo trabajamos", "h2": "Del primer contacto a un plan claro", "items": [{"k": "Primera visita", "h": "Una primera visita sin prisas", "p": "Sesenta minutos para entender qué te preocupa y revisar tu historia clínica y las pruebas que ya tengas. Si tus analíticas son recientes, las utilizamos: no repetimos pruebas sin motivo."}, {"k": "Plan", "h": "Un plan por orden de impacto", "p": "Recomendaciones claras y priorizadas, y una propuesta de seguimiento adaptada a tu caso."}, {"k": "Visión global", "h": "Una mirada que integra", "p": "Sueño, estrés, nutrición, microbiota, dolor y salud cognitiva se valoran juntos."}]}] + BLOCKS,
    "faq": [
        ("¿Podéis ayudarme con la acidez o el reflujo?", "Sí, como complemento del seguimiento médico. Revisamos la alimentación, los horarios, el estrés y otros factores que influyen en el reflujo, y proponemos un plan nutricional y de hábitos. Si hay dificultad para tragar, sangrado o pérdida de peso, primero debe valorarte tu médico."),
        ("¿Trabajáis el colon irritable y el SIBO?", "Sí. Valoramos la alimentación, el estrés y la microbiota y, cuando aporta información, solicitamos un estudio de microbiota. El plan combina pautas nutricionales, regulación del estrés y, si procede, acupuntura."),
        ("¿Atendéis la fibromialgia?", "Sí. Combinamos ejercicio adaptado, educación en dolor, regulación del sueño y del estrés, acupuntura y terapia manual."),
        ("¿Y el hipotiroidismo o la tiroiditis de Hashimoto?", "Sí, como complemento del tratamiento endocrinológico. Trabajamos la alimentación, la salud intestinal, el sueño y el estrés, sin modificar la medicación prescrita."),
        ("Mi problema no aparece en la lista. ¿Puedo consultar?", "Sí. La lista recoge las indicaciones más frecuentes. Escríbenos por WhatsApp, cuéntanos tu caso y te diremos si podemos ayudarte o a qué especialista conviene acudir."),
        ("¿Sustituye esta consulta a mi médico?", "No. El diagnóstico y el tratamiento médico corresponden a tu médico. Nuestro acompañamiento es complementario."),
    ],
    "related": ["salud-digestiva-microbiota", "dolor-persistente-cronico", "pni-pnie-barcelona", "prevencion-longevidad"],
    "cta": {"h2": "Cuéntanos tu caso", "p": "Reserva tu primera visita o escríbenos por WhatsApp y te orientaremos antes de reservar."},
}

PAGES.append(PAGE)


# ---------------------------------------------------------------- MOTIVOS
PAGES.append({
    "slug": "dolor-persistente-cronico", "group": "motivo", "wave": 1,
    "nav": "Dolor persistente y crónico",
    "card": "Cuando el dolor dura meses o vuelve una y otra vez, aunque las pruebas no lo expliquen todo.",
    "title": "Dolor persistente y crónico en Barcelona · Sarrià–Sant Gervasi | WA LAM",
    "desc": "Valoración integrativa del dolor persistente y crónico en Sarrià–Sant Gervasi, Barcelona. Osteopatía, ejercicio adaptado, educación en dolor, mindfulness y hábitos.",
    "about": "Dolor crónico",
    "eyebrow": "Motivo de consulta",
    "h1": "Dolor persistente y crónico",
    "sub": "Valoración integrativa en Sarrià–Sant Gervasi · Barcelona",
    "lead": "El dolor que dura más de tres meses no es solo un dolor que tarda en irse. Con el tiempo, el sistema nervioso puede volverse más sensible y el dolor empieza a depender también del sueño, el estrés, el movimiento y la historia de cada persona. Por eso lo valoramos desde varios ángulos.",
    "facts": ["Primera consulta de **valoración global**", "Osteopatía, ejercicio adaptado y educación en dolor", "Mindfulness para el dolor (MBSR)",
              "Coordinación con tu médico cuando hace falta", "Plan con objetivos y revisiones"],
    "wa": "Hola, tengo dolor persistente y me gustaría saber si podéis valorar mi caso.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando el dolor ya forma parte del día a día",
         "qs": ["¿Tienes un dolor que vuelve una y otra vez aunque las pruebas no explican todo lo que sientes?",
                "¿Has probado varios tratamientos y mejoras unos días, pero el dolor regresa?",
                "¿Duermes peor por el dolor y, cuando duermes peor, el dolor aumenta?",
                "¿Sientes que tu cuerpo está siempre en guardia y ya no sabe descansar?",
                "¿Te da miedo moverte por si empeoras?",
                "¿El dolor cambia de sitio o aumenta en épocas de más estrés?"],
         "close": "El dolor es real, aunque sus mecanismos puedan ser complejos."},
        {"type": "explain", "eyebrow": "Qué sabemos del dolor persistente", "h2": "El dolor no siempre indica daño",
         "paras": [
             "El dolor es una respuesta de protección que elabora el sistema nervioso. Cuando se mantiene en el tiempo, puede producirse lo que llamamos **sensibilización**: el sistema se vuelve más reactivo y estímulos que antes no dolían empiezan a doler, o duelen más. No significa que el dolor sea imaginario ni que «esté en tu cabeza».",
             "En el dolor persistente suelen influir varios factores a la vez: la estructura de los tejidos, la inflamación, la calidad del sueño, el estrés sostenido, la respiración, el nivel de actividad, experiencias previas de dolor y la sensación de amenaza. La emoción no inventa el dolor, pero puede modularlo a través del sistema nervioso.",
             "Por eso, en la primera consulta no buscamos solo «dónde está el problema», sino **qué está manteniendo el dolor** y qué recursos tienes para recuperar movimiento, descanso y confianza en tu cuerpo.",
         ]},
        {"type": "steps", "eyebrow": "La primera consulta", "h2": "Qué valoramos cuando vienes por dolor",
         "items": [("Tu historia de dolor", "Cuándo empezó, cómo ha evolucionado, qué lo alivia y qué lo empeora, pruebas y tratamientos previos, y cómo afecta a tu vida."),
                   ("Cuerpo y sistema nervioso", "Movilidad, fuerza, tejidos, respiración y diafragma, junto con sueño, estrés y señales de sensibilización."),
                   ("Un plan por fases", "Te explicamos lo que observamos y proponemos un plan combinado: terapia manual, ejercicio, educación en dolor y, si encaja, mindfulness.")],
         "note": "Si identificamos signos que requieren un estudio médico, te derivamos al especialista correspondiente antes de iniciar cualquier tratamiento."},
        {"type": "cards", "eyebrow": "Con qué podemos acompañarte", "h2": "Enfoques que combinamos según tu caso",
         "items": [{"k": "Terapia manual", "h": "Osteopatía", "p": "Para mejorar movilidad, función y percepción corporal, incluyendo el abordaje visceral y craneal cuando está indicado."},
                   {"k": "Movimiento", "h": "Ejercicio adaptado", "p": "Recuperar fuerza y confianza en el movimiento con un programa progresivo y adaptado."},
                   {"k": "Sistema nervioso", "h": "Mindfulness (MBSR)", "p": "Entrenamiento estructurado de la atención y la regulación. Recomendado como tratamiento inicial del dolor lumbar crónico en la guía del American College of Physicians."},
                   {"k": "Hábitos", "h": "Sueño, inflamación y PNIE", "p": "Revisar descanso, alimentación y estrés, que influyen en la sensibilidad al dolor."},
                   {"k": "Medicina tradicional china", "h": "[Acupuntura](acupuntura-medicina-tradicional-china)", "p": "Recomendada como tratamiento inicial del dolor lumbar crónico por el American College of Physicians y con eficacia superior a la simulada en el dolor crónico."}]},
        {"type": "cards", "eyebrow": "Tipos de dolor", "h2": "Dolor crónico, neuropático, musculoesquelético, postquirúrgico y oncológico", "intro": "Cada tipo de dolor tiene su propia página, con su abordaje y la evidencia que lo sustenta.", "items": [{"k": "Columna", "h": "[Lumbalgia y cervicalgia crónicas](lumbalgia-cervicalgia-cronica)", "p": "Dolor de espalda y cuello persistente, hernia discal y artrosis facetaria."}, {"k": "Articular y miofascial", "h": "[Dolor articular y miofascial](dolor-articular-miofascial)", "p": "Artrosis, tendinopatías, fibromialgia y síndromes miofasciales."}, {"k": "Musculoesquelético", "h": "[Dolor musculoesquelético](dolor-musculoesqueletico)", "p": "Contracturas, sobrecargas, roturas fibrilares, esguinces y lesiones deportivas."}, {"k": "Neuropático", "h": "[Dolor neuropático](dolor-neuropatico)", "p": "Ciática, neuralgias, dolor postherpético y neuropatía."}, {"k": "Cefaleas", "h": "[Cefaleas y migraña](cefaleas-migrana)", "p": "Migraña, cefalea tensional y cefalea cervicogénica."}, {"k": "Pélvico", "h": "[Dolor pélvico crónico](suelo-pelvico-dolor-pelvico)", "p": "Dolor pélvico persistente y dismenorrea, con abordaje externo."}, {"k": "Postquirúrgico", "h": "[Dolor postquirúrgico](dolor-postquirurgico)", "p": "Recuperación tras cirugía traumatológica, estética, abdominal u oncológica."}, {"k": "Oncológico", "h": "[Dolor oncológico](dolor-oncologico)", "p": "Acompañamiento con autorización médica firmada."}]},
        {"type": "evidence", "h2": "Qué dice la evidencia",
         "intro": "Tomamos decisiones clínicas a partir de guías de práctica clínica, revisiones sistemáticas y metaanálisis. Estas son las fuentes principales en las que se basa nuestro abordaje del dolor lumbar crónico, el cuadro mejor estudiado.",
         "items": [("Guía clínica", "La guía del American College of Physicians (Annals of Internal Medicine, 2017) recomienda como **tratamiento inicial del dolor lumbar crónico** el ejercicio, la rehabilitación multidisciplinar, la acupuntura y el programa MBSR, antes que los fármacos (evidencia de calidad moderada)."),
                   ("Revisión Cochrane", "La revisión Cochrane de 2021 sobre ejercicio terapéutico (249 ensayos, más de 24.000 participantes) concluye que el ejercicio probablemente reduce el dolor frente a no tratar, a la atención habitual o al placebo."),
                   ("Ensayo clínico (JAMA)", "En un ensayo aleatorizado con 342 adultos, el MBSR y la terapia cognitivo-conductual mejoraron más el dolor y la limitación funcional que la atención habitual a las 26 semanas, sin diferencias entre ambos."),
                   ("Metaanálisis (BMJ)", "La terapia manipulativa vertebral obtiene efectos similares a los de otros tratamientos recomendados para el dolor lumbar crónico (47 ensayos). Por eso la integramos dentro de un plan activo y no como tratamiento aislado."),
                   ("Experiencia clínica", "En consulta observamos que trabajar también el sueño y la carga de estrés mejora la adherencia al ejercicio y la sensación de control sobre el dolor. Es una observación clínica, no un resultado de ensayo.")],
         "refs": [R["qaseem"], R["hayden"], R["cherkin"], R["rubinstein"]]},
    ],
    "faq": [("¿Qué disciplinas intervienen en el abordaje del dolor?", "La [osteopatía](osteopatia-sarria-sant-gervasi) y la [acupuntura](acupuntura-medicina-tradicional-china), integradas en un plan individual. Cuando se requiere un programa de fisioterapia, realizamos la derivación a un fisioterapeuta colegiado."),
            
        ("¿Qué se considera dolor crónico o persistente?", "En general, el dolor que dura más de tres meses o que persiste más allá del tiempo habitual de curación de un tejido. Puede ser continuo o aparecer por episodios."),
        ("Mis pruebas están bien, pero me sigue doliendo. ¿Es normal?", "Es más frecuente de lo que parece. Las pruebas de imagen muestran estructuras, pero no miden la sensibilidad del sistema nervioso. Que no aparezca una lesión no quiere decir que tu dolor no sea real."),
        ("¿Necesito informe médico para venir?", "No es imprescindible, pero si tienes pruebas o informes, tráelos a la primera consulta. Nos ayudan a valorar mejor tu caso."),
        ("¿Cuántas sesiones voy a necesitar?", "Depende de cada caso. Tras la primera valoración te proponemos un plan con objetivos y momentos de revisión, para que sepas en todo momento cómo avanzamos."),
        ("¿Quién me atenderá?", "Te atiende siempre Rosa María Rodríguez Valls, osteópata D.O., desde la primera valoración hasta el seguimiento."),
    ],
    "related": ["lumbalgia-cervicalgia-cronica", "dolor-articular-miofascial", "dolor-neuropatico", "cefaleas-migrana"],
    "cta": {"h2": "Valoremos tu dolor con calma", "p": "Cuéntanos tu caso por WhatsApp o reserva directamente la primera consulta de valoración."},
})

# ---------------------------------------------------------------- PÁGINAS DE DOLOR
R["fransen"] = _r("Fransen M, McConnell S, Harmer AR, Van der Esch M, Simic M, Bennell KL, 2015. «Exercise for osteoarthritis of the knee». Cochrane Database of Systematic Reviews.", "10.1002/14651858.CD004376.pub3")
R["ju_neuro"] = _r("Ju ZY, Wang K, Cui HS, et al., 2017. «Acupuncture for neuropathic pain in adults». Cochrane Database of Systematic Reviews.", "10.1002/14651858.CD012057.pub2")
R["linde_mig"] = _r("Linde K, Allais G, Brinkhaus B, et al., 2016. «Acupuncture for the prevention of episodic migraine». Cochrane Database of Systematic Reviews.", "10.1002/14651858.CD001218.pub3")

R["avis"] = _r("Avis NE, Coeytaux RR, Isom S, Prevette K, Morgan T, 2016. «Acupuncture in Menopause (AIM) study: a pragmatic, randomized controlled trial». Menopause.", "10.1097/GME.0000000000000597")
R["wu_postop"] = _r("Wu MS, Chen KH, Chen IF, et al., 2016. «The Efficacy of Acupuncture in Post-Operative Pain Management: A Systematic Review and Meta-Analysis». PLoS One.", "10.1371/journal.pone.0150367")

PAIN_NOTE = "El acompañamiento de WA LAM es complementario: el diagnóstico y el tratamiento médico del dolor corresponden a tu médico."

PAGES.append({
    "slug": "lumbalgia-cervicalgia-cronica", "group": "motivo", "wave": 1,
    "nav": "Lumbalgia y cervicalgia crónicas",
    "card": "Dolor de espalda y de cuello persistente, hernia discal, artrosis facetaria y dolor de origen vertebral.",
    "title": "Lumbalgia y cervicalgia crónicas en Barcelona · Sarrià–Sant Gervasi | WA LAM",
    "desc": "Lumbalgia y cervicalgia crónicas en Sarrià–Sant Gervasi, Barcelona: dolor de espalda y cuello persistente, hernia discal y artrosis facetaria. Abordaje integrativo.",
    "about": "Lumbalgia y cervicalgia crónicas",
    "eyebrow": "Dolor · Columna vertebral",
    "h1": "Lumbalgia y cervicalgia crónicas",
    "sub": "Dolor de espalda y cuello persistente · Sarrià–Sant Gervasi",
    "lead": "El dolor lumbar y cervical persistente es uno de los motivos de consulta más frecuentes en WA LAM. Cuando se prolonga más de tres meses, en su mantenimiento intervienen factores mecánicos, inflamatorios, del sistema nervioso y del estilo de vida, y el abordaje más eficaz es el que actúa sobre todos ellos.",
    "facts": ["Lumbalgia, dorsalgia y cervicalgia crónicas", "Hernia discal y artrosis facetaria", "Técnicas manuales, ejercicio y educación en dolor", "Primera visita: 60 min · 90 €", "Atiende: Rosa María Rodríguez Valls, osteópata D.O."],
    "wa": "Hola, me gustaría información sobre el abordaje de la lumbalgia o la cervicalgia crónica.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando el dolor de espalda o de cuello no termina de irse",
         "qs": ["¿Tienes dolor lumbar o cervical desde hace más de tres meses?", "¿Te han diagnosticado una hernia discal, una protrusión o artrosis facetaria?",
                "¿El dolor empeora con el estrés, el sedentarismo o el mal descanso?", "¿Has probado varios tratamientos con mejorías que no se mantienen?"],
         "close": "Si el dolor se acompaña de pérdida de fuerza, alteraciones de la sensibilidad, fiebre o problemas para orinar, consulta con tu médico o con urgencias."},
        {"type": "explain", "eyebrow": "Qué sabemos", "h2": "Por qué el dolor vertebral se cronifica",
         "paras": ["En la mayoría de los casos de lumbalgia y cervicalgia crónicas no existe una única lesión que explique la intensidad del dolor. Los hallazgos de imagen, como las protrusiones o la artrosis, son frecuentes también en personas sin dolor.",
                   "En la persistencia del dolor intervienen la sensibilización del sistema nervioso, la pérdida de fuerza y movilidad, el estrés sostenido, la calidad del sueño y el miedo al movimiento. Por eso el abordaje debe ser global y progresivo."]},
        {"type": "cards", "eyebrow": "Cómo lo abordamos", "h2": "Un abordaje integrativo del dolor vertebral",
         "items": [{"k": "Valoración", "h": "Evaluación funcional", "p": "Historia clínica, pruebas previas, movilidad, factores de estrés, sueño y hábitos."},
                   {"k": "Tratamiento", "h": "Técnicas manuales", "p": "Abordaje manual individualizado según la valoración, ajustado en cada fase."},
                   {"k": "Movimiento", "h": "Ejercicio adaptado", "p": "Recuperación progresiva de la fuerza, la movilidad y la confianza en el movimiento."},
                   {"k": "Sistema nervioso", "h": "Educación en dolor y regulación", "p": "Comprender el dolor y reducir la activación sostenida por estrés, con apoyo del [curso MBSR](curso-mindfulness-mbsr-barcelona)."}]},
        {"type": "evidence", "h2": "Qué dice la evidencia",
         "items": [("Guía clínica (ACP)", "La guía del American College of Physicians recomienda como primera línea en el dolor lumbar crónico el ejercicio, la rehabilitación multidisciplinar, la acupuntura y la reducción del estrés basada en mindfulness (Qaseem et al., Ann Intern Med, 2017)."),
                   ("Metaanálisis (J Pain)", "En un metaanálisis con datos individuales de más de 20.000 pacientes, la acupuntura fue superior a la acupuntura simulada y a la ausencia de acupuntura en el dolor lumbar y cervical crónico (Vickers et al., J Pain, 2018)."),
                   ("Ensayo clínico (JAMA)", "El programa MBSR mejoró el dolor lumbar crónico y la limitación funcional frente a la atención habitual (Cherkin et al., JAMA, 2016)."),
                   ("Nuestro criterio", PAIN_NOTE)],
         "refs": [R["qaseem"], R["vickers"], R["cherkin"]]},
    ],
    "faq": [("¿Qué disciplinas intervienen en el abordaje del dolor?", "La [osteopatía](osteopatia-sarria-sant-gervasi) y la [acupuntura](acupuntura-medicina-tradicional-china), integradas en un plan individual. Cuando se requiere un programa de fisioterapia, realizamos la derivación a un fisioterapeuta colegiado."),
            ("¿Tratáis la hernia discal?", "Acompañamos el dolor asociado a la hernia discal con técnicas manuales, ejercicio adaptado y educación en dolor. Si hay pérdida de fuerza o de sensibilidad, primero debe valorarte tu médico."),
            ("¿Necesito una resonancia antes de venir?", "No es imprescindible. Si ya tienes pruebas, tráelas a la primera visita y las revisamos junto con tu historia clínica."),
            ("¿Cuántas sesiones necesitaré?", "Depende de cada caso. En la primera visita valoramos tu situación y te proponemos un plan.")],
    "related": ["dolor-persistente-cronico", "dolor-articular-miofascial", "osteopatia-sarria-sant-gervasi", "acupuntura-medicina-tradicional-china"],
    "cta": {"h2": "Recupera tu espalda con un plan claro", "p": "Reserva tu primera visita o escríbenos por WhatsApp."},
})

PAGES.append({
    "slug": "dolor-articular-miofascial", "group": "motivo", "wave": 1,
    "nav": "Dolor articular y miofascial",
    "card": "Artrosis de rodilla, cadera y hombro, tendinopatías, fibromialgia y síndromes miofasciales.",
    "title": "Dolor articular y miofascial en Barcelona · Sarrià–Sant Gervasi | WA LAM",
    "desc": "Dolor articular y miofascial en Sarrià–Sant Gervasi, Barcelona: artrosis de rodilla, cadera y hombro, tendinopatías, fibromialgia y dolor deportivo.",
    "about": "Dolor articular y miofascial",
    "eyebrow": "Dolor · Musculoesquelético",
    "h1": "Dolor articular y miofascial",
    "sub": "Artrosis, tendinopatías y dolor muscular persistente · Sarrià–Sant Gervasi",
    "lead": "La artrosis de rodilla, cadera u hombro, las tendinopatías, la fibromialgia y los síndromes miofasciales comparten un mismo reto: un dolor que limita el movimiento y la vida diaria. Lo abordamos tanto en su vertiente degenerativa como deportiva, con un plan que combina técnicas manuales, ejercicio y regulación del sistema nervioso.",
    "facts": ["Artrosis de rodilla, cadera y hombro", "Tendinopatías y dolor deportivo", "Fibromialgia y síndromes miofasciales", "Primera visita: 60 min · 90 €", "Atiende: Rosa María Rodríguez Valls, osteópata D.O."],
    "wa": "Hola, me gustaría información sobre el abordaje del dolor articular o miofascial.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando el dolor limita tu movimiento",
         "qs": ["¿Te duele la rodilla, la cadera o el hombro al caminar, subir escaleras o dormir?", "¿Tienes una tendinopatía que reaparece con el deporte?",
                "¿Te han diagnosticado fibromialgia o un dolor muscular generalizado?", "¿Notas puntos dolorosos en la musculatura que irradian el dolor?"]},
        {"type": "explain", "eyebrow": "Qué sabemos", "h2": "Movimiento, carga y sistema nervioso",
         "paras": ["En la artrosis y las tendinopatías, el ejercicio terapéutico adaptado es la intervención con mayor respaldo científico: mejora el dolor y la función, y protege la articulación a largo plazo.",
                   "En la fibromialgia y los síndromes miofasciales predomina la sensibilización del sistema nervioso, por lo que el sueño, el estrés y la actividad física gradual son tan importantes como el tratamiento local."]},
        {"type": "cards", "eyebrow": "Cómo lo abordamos", "h2": "Un plan adaptado a tu articulación y a tu ritmo",
         "items": [{"k": "Valoración", "h": "Evaluación funcional", "p": "Movilidad, fuerza, carga, historia deportiva o degenerativa y factores generales."},
                   {"k": "Tratamiento", "h": "Técnicas manuales", "p": "Abordaje manual individualizado de la articulación y de los tejidos miofasciales."},
                   {"k": "Movimiento", "h": "Ejercicio progresivo", "p": "Fortalecimiento y movilidad adaptados, con progresión de la carga."},
                   {"k": "Regulación", "h": "Sueño, estrés e inflamación", "p": "Nutrición antiinflamatoria y regulación del sistema nervioso cuando el dolor es generalizado."}]},
        {"type": "evidence", "h2": "Qué dice la evidencia",
         "items": [("Revisión Cochrane", "En la artrosis de rodilla, el ejercicio terapéutico reduce el dolor y mejora la función física, con un beneficio que se mantiene entre dos y seis meses tras el tratamiento (Fransen et al., Cochrane, 2015)."),
                   ("Metaanálisis (J Pain)", "La acupuntura fue superior a la acupuntura simulada en el dolor por artrosis y en el dolor musculoesquelético crónico (Vickers et al., J Pain, 2018)."),
                   ("Nuestro criterio", PAIN_NOTE)],
         "refs": [R["fransen"], R["vickers"]]},
    ],
    "faq": [("¿Qué disciplinas intervienen en el abordaje del dolor?", "La [osteopatía](osteopatia-sarria-sant-gervasi) y la [acupuntura](acupuntura-medicina-tradicional-china), integradas en un plan individual. Cuando se requiere un programa de fisioterapia, realizamos la derivación a un fisioterapeuta colegiado."),
            ("¿Puedo hacer ejercicio si tengo artrosis?", "Sí. El ejercicio adaptado es uno de los tratamientos más eficaces en la artrosis. Lo ajustamos a tu articulación, tu nivel y tu dolor."),
            ("¿Atendéis el dolor deportivo?", "Sí: tendinopatías, sobrecargas y dolor muscular relacionado con el deporte, con un plan de vuelta progresiva a la actividad."),
            ("¿Y la fibromialgia?", "Sí, con un abordaje que combina actividad física gradual, regulación del sueño y del estrés, técnicas manuales y nutrición antiinflamatoria.")],
    "related": ["dolor-persistente-cronico", "lumbalgia-cervicalgia-cronica", "osteopatia-sarria-sant-gervasi", "acupuntura-medicina-tradicional-china"],
    "cta": {"h2": "Vuelve a moverte con menos dolor", "p": "Reserva tu primera visita o escríbenos por WhatsApp."},
})
R["cieza"] = _r("Cieza A, Causey K, Kamenov K, Hanson SW, Chatterji S, Vos T, 2020. «Global estimates of the need for rehabilitation based on the Global Burden of Disease study 2019: a systematic analysis for the Global Burden of Disease Study 2019». The Lancet.", "10.1016/S0140-6736(20)32340-0")

PAGES.append({
    "slug": "dolor-musculoesqueletico", "group": "motivo", "wave": 1,
    "nav": "Dolor musculoesquelético",
    "card": "Dolor muscular: contracturas, sobrecargas, roturas fibrilares, esguinces y lesiones deportivas.",
    "title": "Dolor musculoesquelético en Barcelona · Sarrià–Sant Gervasi | WA LAM",
    "desc": "Dolor musculoesquelético en Sarrià–Sant Gervasi, Barcelona: contracturas, sobrecargas, roturas fibrilares, esguinces, tortícolis y lesiones deportivas.",
    "about": "Dolor musculoesquelético",
    "eyebrow": "Dolor · Musculoesquelético",
    "h1": "Dolor musculoesquelético",
    "sub": "Dolor muscular, sobrecargas y lesiones · Sarrià–Sant Gervasi",
    "lead": "El dolor musculoesquelético afecta a los músculos y a las estructuras que los rodean: contracturas, sobrecargas, roturas fibrilares, esguinces, tortícolis o lesiones deportivas. Suele aparecer tras un esfuerzo, una lesión o posturas mantenidas, y cuando no se recupera bien puede volverse recurrente.",
    "facts": ["Contracturas y sobrecargas musculares", "Roturas fibrilares y esguinces", "Tortícolis y dolor por posturas mantenidas", "Lesiones deportivas", "Primera visita: 60 min · 90 €"],
    "wa": "Hola, me gustaría información sobre el dolor muscular o una lesión.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando el dolor muscular te limita",
         "qs": ["¿Tienes una contractura o una sobrecarga que no termina de resolverse?", "¿Te has hecho un esguince o una rotura fibrilar y sigues notando molestias?",
                "¿El dolor reaparece cada vez que retomas el deporte?", "¿Pasas muchas horas en la misma postura y acabas el día con dolor?"],
         "close": "Si tras un traumatismo hay deformidad, incapacidad para apoyar o una inflamación importante, acude a un servicio de urgencias."},
        {"type": "explain", "eyebrow": "Qué es", "h2": "Un dolor muy frecuente",
         "paras": ["Los trastornos musculoesqueléticos son la principal causa de necesidad de rehabilitación en el mundo, según el análisis del Global Burden of Disease publicado en The Lancet en 2020.",
                   "El dolor muscular agudo suele mejorar en días o semanas. Cuando persiste o se repite, intervienen la recuperación incompleta de la lesión, la pérdida de fuerza y movilidad, la sobrecarga mantenida, el estrés y la calidad del descanso."]},
        {"type": "explain", "eyebrow": "Calidad de vida", "h2": "Cómo afecta a la vida diaria",
         "paras": ["El dolor muscular limita el trabajo, el deporte y las actividades cotidianas, altera el sueño y, cuando se repite, genera miedo al movimiento. Una recuperación bien orientada ayuda a volver a la actividad con seguridad y a prevenir recaídas. En el dolor musculoesquelético intervienen la [osteopatía](osteopatia-sarria-sant-gervasi) y la [acupuntura](acupuntura-medicina-tradicional-china) y, cuando se requiere un programa de fisioterapia, la derivación a un fisioterapeuta colegiado.",
                   "Si el dolor afecta a una articulación o es generalizado, consulta también [dolor articular y miofascial](dolor-articular-miofascial)."]},
        {"type": "evidence", "h2": "Estudios de referencia",
         "items": [("Global Burden of Disease (The Lancet)", "2.410 millones de personas en el mundo podrían beneficiarse de la rehabilitación, y los trastornos musculoesqueléticos son el grupo de enfermedades que más contribuye a esa necesidad (Cieza et al., 2020)."),
                   ("Metaanálisis (J Pain)", "La acupuntura fue superior a la acupuntura simulada en el dolor musculoesquelético crónico, en un análisis con datos individuales de más de 20.000 pacientes (Vickers et al., 2018).")],
         "refs": [R["cieza"], R["vickers"]]},
    ],
    "faq": [("¿Cuándo debo consultar por un dolor muscular?", "Si el dolor dura más de unas semanas, se repite o te impide hacer tu actividad habitual."),
            ("¿Atendéis lesiones deportivas?", "Sí: sobrecargas, contracturas, roturas fibrilares y esguinces, con una vuelta progresiva a la actividad."),
            ("¿En qué se diferencia del dolor articular y miofascial?", "El dolor musculoesquelético se centra en el músculo y las lesiones agudas o por sobrecarga; el [dolor articular y miofascial](dolor-articular-miofascial) incluye la artrosis, las tendinopatías, la fibromialgia y los síndromes miofasciales.")],
    "related": ["dolor-persistente-cronico", "dolor-articular-miofascial", "lumbalgia-cervicalgia-cronica", "osteopatia-sarria-sant-gervasi"],
    "cta": {"h2": "Vuelve a moverte sin dolor", "p": "Reserva tu primera visita o escríbenos por WhatsApp."},
})

PAGES.append({
    "slug": "dolor-neuropatico", "group": "motivo", "wave": 2,
    "nav": "Dolor neuropático",
    "card": "Neuralgias, ciática, dolor postherpético, neuropatía diabética y dolor por lesión nerviosa.",
    "title": "Dolor neuropático en Barcelona · Acompañamiento integrativo | WA LAM",
    "desc": "Dolor neuropático en Sarrià–Sant Gervasi, Barcelona: ciática, neuralgias, dolor postherpético y neuropatía. Acompañamiento integrativo complementario al tratamiento médico.",
    "about": "Dolor neuropático",
    "eyebrow": "Dolor · Neuropático",
    "h1": "Dolor neuropático",
    "sub": "Neuralgias, ciática y dolor por lesión nerviosa · Sarrià–Sant Gervasi",
    "lead": "El dolor neuropático se origina por una lesión o una alteración del sistema nervioso: ciática, neuralgias, dolor postherpético, neuropatía diabética o dolor tras una lesión nerviosa. Su diagnóstico y su tratamiento farmacológico corresponden a tu médico; en WA LAM ofrecemos un acompañamiento complementario centrado en la función, el movimiento y la regulación del sistema nervioso.",
    "facts": ["Ciática y radiculopatías", "Neuralgias y dolor postherpético", "Neuropatía diabética", "Complementario al tratamiento médico", "Primera visita: 60 min · 90 €"],
    "wa": "Hola, me gustaría información sobre el acompañamiento del dolor neuropático.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando el dolor tiene origen nervioso",
         "qs": ["¿Sientes quemazón, hormigueo, descargas o dolor que se irradia por una pierna o un brazo?", "¿Te han diagnosticado una ciática, una neuralgia o una neuropatía?",
                "¿El dolor empeora por la noche o con el estrés?", "¿Buscas un acompañamiento que complemente tu tratamiento médico?"],
         "close": "Si aparece pérdida de fuerza, alteraciones del control de esfínteres o un empeoramiento rápido, acude a tu médico o a urgencias."},
        {"type": "explain", "eyebrow": "Qué sabemos", "h2": "Un dolor que requiere un abordaje coordinado",
         "paras": ["El dolor neuropático suele responder peor a los tratamientos habituales del dolor y a menudo requiere fármacos específicos prescritos por el médico.",
                   "Las intervenciones complementarias se orientan a mantener la función y la movilidad, mejorar el sueño, reducir el impacto del estrés y favorecer la adherencia al tratamiento médico. En el síndrome de dolor regional complejo y en el dolor refractario, este acompañamiento se plantea siempre como complemento del seguimiento por la unidad del dolor."]},
        {"type": "cards", "eyebrow": "Cómo lo abordamos", "h2": "Acompañamiento complementario",
         "items": [{"k": "Valoración", "h": "Historia y función", "p": "Revisión de tu diagnóstico, tu tratamiento actual y el impacto del dolor en tu vida diaria."},
                   {"k": "Movimiento", "h": "Movilidad y ejercicio adaptado", "p": "Mantener la actividad y la movilidad de forma segura y progresiva."},
                   {"k": "Regulación", "h": "Sueño y estrés", "p": "Estrategias para mejorar el descanso y reducir la activación del sistema nervioso."},
                   {"k": "Tratamiento", "h": "Técnicas complementarias", "p": "Técnicas manuales y acupuntura cuando están indicadas, con expectativas realistas."}]},
        {"type": "evidence", "h2": "Qué dice la evidencia",
         "items": [("Revisión Cochrane", "En el dolor neuropático periférico, la evidencia sobre la acupuntura es todavía insuficiente para confirmar o descartar su eficacia (Ju et al., Cochrane, 2017). Por eso la ofrecemos con prudencia y como complemento."),
                   ("Metaanálisis (BMJ Open)", "La estimulación eléctrica transcutánea (TENS) redujo la intensidad del dolor frente a placebo en un metaanálisis de 381 estudios (Johnson et al., BMJ Open, 2022)."),
                   ("Nuestro criterio", PAIN_NOTE)],
         "refs": [R["ju_neuro"], R["tens"]]},
    ],
    "faq": [("¿Qué disciplinas intervienen en el abordaje del dolor?", "La [osteopatía](osteopatia-sarria-sant-gervasi) y la [acupuntura](acupuntura-medicina-tradicional-china), integradas en un plan individual. Cuando se requiere un programa de fisioterapia, realizamos la derivación a un fisioterapeuta colegiado."),
            ("¿Sustituye a mi tratamiento médico?", "No. El acompañamiento es complementario y no modifica la medicación prescrita."),
            ("¿Atendéis la ciática?", "Sí, como complemento del seguimiento médico, con movilidad, ejercicio adaptado y técnicas manuales cuando están indicadas."),
            ("¿Y el síndrome de dolor regional complejo?", "Solo como acompañamiento complementario y siempre en paralelo al seguimiento por la unidad del dolor.")],
    "related": ["dolor-persistente-cronico", "lumbalgia-cervicalgia-cronica", "sueno-insomnio", "estres-ansiedad"],
    "cta": {"h2": "Un acompañamiento serio para un dolor complejo", "p": "Escríbenos y valoramos si podemos ayudarte."},
})

PAGES.append({
    "slug": "cefaleas-migrana", "group": "motivo", "wave": 1,
    "nav": "Cefaleas y migraña",
    "card": "Migraña, cefalea tensional, neuralgia occipital y cefalea cervicogénica.",
    "title": "Migraña y cefalea tensional en Barcelona · Sarrià–Sant Gervasi | WA LAM",
    "desc": "Migraña, cefalea tensional, neuralgia occipital y cefalea cervicogénica en Sarrià–Sant Gervasi, Barcelona. Acupuntura, técnicas manuales y regulación del estrés.",
    "about": "Cefaleas y migraña",
    "eyebrow": "Dolor · Cefaleas",
    "h1": "Cefaleas y migraña",
    "sub": "Migraña, cefalea tensional y cefalea cervicogénica · Sarrià–Sant Gervasi",
    "lead": "La migraña y las cefaleas recurrentes afectan de forma importante a la calidad de vida. En WA LAM las abordamos de forma preventiva, actuando sobre los factores que aumentan la frecuencia de las crisis: el estrés, el sueño, la alimentación, la musculatura cervical y la regulación del sistema nervioso.",
    "facts": ["Migraña y cefalea tensional", "Neuralgia occipital y cefalea cervicogénica", "Acupuntura con respaldo Cochrane", "Primera visita: 60 min · 90 €", "Atiende: Rosa María Rodríguez Valls"],
    "wa": "Hola, me gustaría información sobre el abordaje de la migraña o las cefaleas.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando el dolor de cabeza condiciona tu agenda",
         "qs": ["¿Tienes migrañas o dolores de cabeza varias veces al mes?", "¿Las crisis aumentan con el estrés, el mal descanso o determinados alimentos?",
                "¿El dolor empieza en la nuca o en el cuello?", "¿Buscas reducir la frecuencia de las crisis y depender menos de los analgésicos?"],
         "close": "Un dolor de cabeza súbito e intenso, distinto de los habituales o acompañado de fiebre, alteraciones neurológicas o rigidez de nuca requiere atención médica urgente."},
        {"type": "explain", "eyebrow": "Qué sabemos", "h2": "Prevenir las crisis",
         "paras": ["La prevención de la migraña se basa en identificar y modificar los factores que aumentan la frecuencia de las crisis y en mantener una regularidad en el sueño, la alimentación y la actividad física.",
                   "En la cefalea tensional y la cervicogénica, la musculatura cervical y la gestión del estrés desempeñan un papel central."]},
        {"type": "cards", "eyebrow": "Cómo lo abordamos", "h2": "Un plan preventivo",
         "items": [{"k": "Valoración", "h": "Diario de cefaleas", "p": "Frecuencia, intensidad, desencadenantes, sueño, alimentación y medicación."},
                   {"k": "Acupuntura", "h": "Acupuntura preventiva", "p": "Una pauta de al menos seis sesiones, según la evidencia disponible."},
                   {"k": "Cervical", "h": "Técnicas manuales", "p": "Abordaje de la musculatura y la movilidad cervical en la cefalea tensional y cervicogénica."},
                   {"k": "Regulación", "h": "Estrés, sueño y alimentación", "p": "Regularidad de horarios, gestión del estrés y pautas nutricionales."}]},
        {"type": "evidence", "h2": "Qué dice la evidencia",
         "items": [("Revisión Cochrane", "En 22 ensayos con casi 5.000 personas, la acupuntura redujo la frecuencia de la migraña episódica frente a no recibirla y de forma pequeña frente a la acupuntura simulada, con resultados comparables a los fármacos preventivos y menos efectos secundarios (Linde et al., Cochrane, 2016)."),
                   ("Nuestro criterio", "El diagnóstico de la cefalea corresponde a tu médico o neurólogo. Nuestro abordaje es preventivo y complementario.")],
         "refs": [R["linde_mig"]]},
    ],
    "faq": [("¿Qué disciplinas intervienen en el abordaje del dolor?", "La [osteopatía](osteopatia-sarria-sant-gervasi) y la [acupuntura](acupuntura-medicina-tradicional-china), integradas en un plan individual. Cuando se requiere un programa de fisioterapia, realizamos la derivación a un fisioterapeuta colegiado."),
            ("¿La acupuntura sirve para la migraña?", "Según la revisión Cochrane de 2016, una pauta de al menos seis sesiones puede reducir la frecuencia de la migraña episódica, con resultados comparables a los fármacos preventivos."),
            ("¿Tengo que dejar mi medicación?", "No. Cualquier cambio en la medicación lo decide tu médico."),
            ("¿Atendéis la cefalea cervicogénica?", "Sí, con técnicas manuales de la región cervical, ejercicio y regulación del estrés.")],
    "related": ["dolor-persistente-cronico", "acupuntura-medicina-tradicional-china", "estres-ansiedad", "sueno-insomnio"],
    "cta": {"h2": "Menos crisis, más calidad de vida", "p": "Reserva tu primera visita o escríbenos por WhatsApp."},
})
R["beuken"] = _r("van den Beuken-van Everdingen MHJ, Hochstenbach LMJ, Joosten EAJ, Tjan-Heijnen VCG, Janssen DJA, 2016. «Update on Prevalence of Pain in Patients With Cancer: Systematic Review and Meta-Analysis». Journal of Pain and Symptom Management.", "10.1016/j.jpainsymman.2015.12.340")
R["seretny"] = _r("Seretny M, Currie GL, Sena ES, et al., 2014. «Incidence, prevalence, and predictors of chemotherapy-induced peripheral neuropathy: A systematic review and meta-analysis». Pain.", "10.1016/j.pain.2014.09.020")
R["kehlet"] = _r("Kehlet H, Jensen TS, Woolf CJ, 2006. «Persistent postsurgical pain: risk factors and prevention». The Lancet.", "10.1016/S0140-6736(06)68700-X")

PAGES.append({
    "slug": "dolor-oncologico", "group": "motivo", "wave": 1,
    "nav": "Dolor oncológico",
    "card": "El dolor relacionado con el cáncer, sus tratamientos y sus secuelas, y su impacto en la calidad de vida.",
    "title": "Dolor oncológico · Acompañamiento integrativo en Barcelona | WA LAM",
    "desc": "Dolor oncológico en Sarrià–Sant Gervasi, Barcelona: dolor durante y después del tratamiento del cáncer y su impacto en la calidad de vida. Acompañamiento con autorización médica.",
    "about": "Dolor oncológico",
    "eyebrow": "Dolor · Oncológico",
    "h1": "Dolor oncológico",
    "sub": "Durante y después del tratamiento del cáncer · Sarrià–Sant Gervasi",
    "lead": "El dolor es uno de los síntomas más frecuentes y temidos en las personas con cáncer. Puede deberse a la propia enfermedad, a los tratamientos o a sus secuelas, y en muchos casos persiste cuando el tratamiento ya ha terminado. En WA LAM acompañamos a pacientes oncológicos siempre con la autorización firmada de su médico y como complemento de su tratamiento.",
    "facts": ["Requisito: autorización médica firmada", "Dolor durante y después del tratamiento oncológico", "Neuropatía, dolor posquirúrgico y artralgias", "Complementario al tratamiento oncológico", "Atiende: Rosa María Rodríguez Valls"],
    "wa": "Hola, me gustaría información sobre el acompañamiento del dolor oncológico.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando el dolor acompaña al proceso oncológico",
         "qs": ["¿Tienes dolor, hormigueo o quemazón en manos o pies desde la quimioterapia?", "¿Te han quedado secuelas dolorosas tras una cirugía o la radioterapia?",
                "¿Tienes dolor articular desde que tomas hormonoterapia?", "¿El cansancio, la tensión y el mal descanso aumentan tu dolor?"]},
        {"type": "explain", "eyebrow": "Qué es el dolor oncológico", "h2": "Un dolor con múltiples orígenes",
         "paras": ["El dolor oncológico puede tener su origen en el propio tumor, por la afectación de huesos, órganos o nervios, o en los tratamientos. La cirugía puede dejar dolor persistente en la zona intervenida; la quimioterapia, una neuropatía periférica con hormigueo, quemazón o dolor en manos y pies; la radioterapia, fibrosis y rigidez de los tejidos; y la hormonoterapia, dolor articular.",
                   "Es muy frecuente: según una revisión sistemática de 117 estudios, presentan dolor el 55 % de las personas durante el tratamiento oncológico, el 39 % de quienes ya lo han terminado y el 66 % de quienes tienen una enfermedad avanzada. En el caso de la neuropatía por quimioterapia, afecta al 68 % de los pacientes durante el primer mes y persiste en cerca de un 30 % a los seis meses."]},
        {"type": "explain", "eyebrow": "Calidad de vida", "h2": "Cómo afecta el dolor a la vida diaria",
         "paras": ["El dolor oncológico no es solo una sensación física. Altera el sueño, aumenta el cansancio, condiciona el estado de ánimo, limita la actividad y las relaciones sociales y puede dificultar el seguimiento del propio tratamiento. Dolor, insomnio, fatiga y ansiedad se refuerzan entre sí.",
                   "Por eso el abordaje del dolor oncológico requiere una mirada global de la persona, que tenga en cuenta tanto el dolor como su repercusión física, emocional y social."]},
        {"type": "explain", "eyebrow": "Nuestro acompañamiento", "h2": "Siempre con autorización médica",
         "paras": ["Para iniciar el acompañamiento es imprescindible un documento firmado por tu médico que autorice el tratamiento. Sin esa autorización no tratamos a ningún paciente oncológico.",
                   "El acompañamiento se adapta a la fase de tu tratamiento, a tu estado general y a tus prioridades: aliviar el dolor, mejorar el descanso y recuperar bienestar y calidad de vida. Puede incluir [acupuntura](acupuntura-medicina-tradicional-china), recomendada por la guía SIO–ASCO para algunos tipos de dolor oncológico. En ningún caso sustituye el tratamiento oncológico."]},
        {"type": "evidence", "h2": "Estudios de referencia",
         "items": [("Revisión sistemática (J Pain Symptom Manage)", "En 117 estudios y más de 63.000 pacientes, el dolor estuvo presente en el 55 % de las personas durante el tratamiento oncológico, en el 39 % tras finalizarlo y en el 66 % en la enfermedad avanzada; el 38 % refería un dolor moderado o intenso (van den Beuken-van Everdingen et al., 2016)."),
                   ("Metaanálisis (Pain)", "La neuropatía periférica inducida por quimioterapia afectó al 68 % de los pacientes en el primer mes, al 60 % a los tres meses y al 30 % a los seis meses o más (Seretny et al., 2014)."),
                   ("Guía SIO–ASCO (J Clin Oncol)", "La guía de oncología integrativa de la Society for Integrative Oncology y la American Society of Clinical Oncology recomienda la acupuntura para el dolor articular asociado a los inhibidores de la aromatasa en el cáncer de mama (Mao et al., 2022)."),
                   ("Nuestro criterio", "Solo atendemos a pacientes oncológicos con autorización médica firmada y siempre como complemento de su tratamiento.")],
         "refs": [R["beuken"], R["seretny"], R["sio_asco"]]},
    ],
    "faq": [("¿Qué disciplinas intervienen en el abordaje del dolor?", "La [osteopatía](osteopatia-sarria-sant-gervasi) y la [acupuntura](acupuntura-medicina-tradicional-china), integradas en un plan individual. Cuando se requiere un programa de fisioterapia, realizamos la derivación a un fisioterapeuta colegiado."),
            ("¿Qué necesito para empezar?", "Un documento firmado por tu médico que autorice el tratamiento. Sin esa autorización no podemos atenderte."),
            ("¿Puedo venir durante la quimioterapia o la radioterapia?", "Depende de tu situación y de lo que indique tu médico. El acompañamiento se adapta a cada fase del tratamiento."),
            ("¿Y si el tratamiento ya ha terminado pero el dolor continúa?", "Es frecuente: cerca de cuatro de cada diez personas mantienen dolor después del tratamiento. También podemos acompañarte en esa etapa, con autorización médica."),
            ("¿Sustituye a mi tratamiento oncológico?", "No. Es un acompañamiento complementario para aliviar el dolor y mejorar la calidad de vida.")],
    "related": ["dolor-persistente-cronico", "dolor-postquirurgico", "drenaje-linfatico-linfedema", "sueno-insomnio"],
    "cta": {"h2": "Un acompañamiento cuidadoso", "p": "Escríbenos y te explicamos cómo trabajamos con pacientes oncológicos."},
})
PAGES.append({
    "slug": "dolor-postquirurgico", "group": "motivo", "wave": 1,
    "nav": "Dolor postquirúrgico",
    "card": "Dolor que persiste después de una cirugía: por qué ocurre y cómo afecta a la recuperación.",
    "title": "Dolor postquirúrgico en Barcelona · Recuperación tras la cirugía | WA LAM",
    "desc": "Dolor postquirúrgico persistente en Sarrià–Sant Gervasi, Barcelona: por qué el dolor puede mantenerse tras una cirugía y cómo afecta a la recuperación y la calidad de vida.",
    "about": "Dolor postoperatorio",
    "eyebrow": "Dolor · Postquirúrgico",
    "h1": "Dolor postquirúrgico",
    "sub": "Cuando el dolor persiste tras la cirugía · Sarrià–Sant Gervasi",
    "lead": "El dolor después de una operación suele disminuir a medida que los tejidos cicatrizan. En una parte de las personas, sin embargo, se mantiene durante meses y se convierte en un problema en sí mismo. Es el dolor postquirúrgico persistente, distinto del dolor musculoesquelético, y requiere un abordaje específico.",
    "facts": ["Cirugía traumatológica, de columna, abdominal, estética u oncológica", "Dolor persistente tras la intervención", "Edema, cicatriz y pérdida de movilidad", "Pacientes oncológicos con autorización médica", "Atiende: Rosa María Rodríguez Valls"],
    "wa": "Hola, me han operado y me gustaría información sobre el dolor postquirúrgico.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando la recuperación tras la cirugía se alarga",
         "qs": ["¿Sigues con dolor meses después de la operación?", "¿Notas quemazón, hormigueo o hipersensibilidad cerca de la cicatriz?",
                "¿La zona sigue inflamada o te cuesta recuperar el movimiento?", "¿El dolor afecta a tu descanso y a tu vida diaria?"],
         "close": "Fiebre, enrojecimiento intenso, supuración o un dolor que aumenta de forma brusca requieren una valoración médica inmediata."},
        {"type": "explain", "eyebrow": "Qué es", "h2": "El dolor postquirúrgico persistente",
         "paras": ["Se considera persistente el dolor que continúa más allá del tiempo esperado de cicatrización, habitualmente más de tres meses después de la intervención. Tras cirugías frecuentes, como la de hernia inguinal, mama, tórax o bypass coronario, aparece en entre un 10 % y un 50 % de las personas, y en un 2 % a 10 % es intenso.",
                   "Su causa principal es la lesión de pequeños nervios durante la cirugía, que da lugar a un dolor de características neuropáticas. Otros factores de riesgo son el dolor previo a la operación, un dolor agudo postoperatorio intenso y factores emocionales como la ansiedad o el estrés."]},
        {"type": "explain", "eyebrow": "Calidad de vida", "h2": "Cómo afecta a la recuperación",
         "paras": ["El dolor persistente limita la movilidad, retrasa la vuelta a la actividad y al trabajo, altera el sueño y afecta al estado de ánimo. El edema, la rigidez de la cicatriz y el miedo al movimiento pueden mantener el círculo del dolor.",
                   "Un acompañamiento precoz y progresivo, siempre según las indicaciones del cirujano, ayuda a recuperar la función y a evitar que el dolor se cronifique; la [acupuntura](acupuntura-medicina-tradicional-china) puede formar parte de él. En el caso de cirugías oncológicas, solo atendemos con autorización médica firmada."]},
        {"type": "evidence", "h2": "Estudios de referencia",
         "items": [("Revisión (The Lancet)", "El dolor persistente aparece en el 10–50 % de las personas tras cirugías frecuentes y es intenso en el 2–10 %. La lesión nerviosa durante la intervención es su causa más importante, y la intensidad del dolor agudo postoperatorio se relaciona con el riesgo de cronificación (Kehlet, Jensen y Woolf, 2006)."),
                   ("Metaanálisis (BMJ Open)", "La estimulación eléctrica transcutánea (TENS) redujo la intensidad del dolor agudo y crónico frente a placebo en 381 estudios (Johnson et al., 2022)."),
                   ("Metaanálisis (PLoS One)", "En un metaanálisis de ensayos aleatorizados, algunas modalidades de acupuntura mejoraron el dolor el primer día tras la cirugía y redujeron el consumo de opioides (Wu et al., PLoS One, 2016)."),
                   ("Nuestro criterio", "Seguimos siempre las indicaciones del cirujano. El acompañamiento es complementario y no sustituye el control postoperatorio.")],
         "refs": [R["kehlet"], R["tens"], R["wu_postop"]]},
    ],
    "faq": [("¿Qué disciplinas intervienen en el abordaje del dolor?", "La [osteopatía](osteopatia-sarria-sant-gervasi) y la [acupuntura](acupuntura-medicina-tradicional-china), integradas en un plan individual. Cuando se requiere un programa de fisioterapia, realizamos la derivación a un fisioterapeuta colegiado."),
            ("¿Es normal tener dolor meses después de operarme?", "Es más frecuente de lo que se cree: entre un 10 % y un 50 % de las personas mantienen dolor tras cirugías habituales. Conviene valorarlo para evitar que se cronifique."),
            ("¿Cuándo puedo empezar después de la operación?", "Depende de la intervención y de lo que indique tu cirujano."),
            ("¿Y después de una cirugía oncológica?", "Sí, siempre con autorización médica firmada. Más información en [dolor oncológico](dolor-oncologico).")],
    "related": ["dolor-persistente-cronico", "drenaje-linfatico-postoperatorio", "dolor-oncologico", "dolor-neuropatico"],
    "cta": {"h2": "Recupérate con un acompañamiento experto", "p": "Escríbenos por WhatsApp o reserva tu primera visita."},
})


PAGES.append({
    "slug": "estres-ansiedad", "group": "motivo", "wave": 1,
    "nav": "Estrés y gestión de la ansiedad",
    "card": "Cuando el cuerpo vive en alerta: tensión, mal descanso, digestión alterada y mente que no para.",
    "title": "Estrés y gestión de la ansiedad en Barcelona · Sarrià–Sant Gervasi | WA LAM",
    "desc": "Acompañamiento integrativo del estrés y la ansiedad en Sarrià–Sant Gervasi: regulación del sistema nervioso, respiración, terapia manual, mindfulness MBSR y hábitos.",
    "about": "Estrés y ansiedad",
    "eyebrow": "Motivo de consulta",
    "h1": "Estrés y gestión de la ansiedad",
    "sub": "Regulación del sistema nervioso · Sarrià–Sant Gervasi",
    "lead": "El estrés es una respuesta adaptativa: nos prepara para actuar. El problema aparece cuando se mantiene demasiado tiempo y el sistema nervioso deja de volver a la calma. En WA LAM te ayudamos a entender qué está sosteniendo esa alerta y a entrenar recursos concretos para recuperar equilibrio.",
    "facts": ["Valoración del **estrés en el cuerpo**", "Respiración y regulación del sistema nervioso", "Acupuntura para el estrés y la ansiedad",
              "Programa **MBSR** de 8 semanas", "Derivación a psicología o psiquiatría si es necesario"],
    "wa": "Hola, estoy pasando una etapa de mucho estrés/ansiedad y me gustaría saber cómo podéis ayudarme.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando el cuerpo no sabe bajar la guardia",
         "qs": ["¿Sientes que tu cuerpo está siempre en alerta, incluso cuando no pasa nada?",
                "¿Te cuesta parar la mente aunque estés agotada?",
                "¿Tu ansiedad aparece en el pecho, la respiración, el estómago o la tensión muscular?",
                "¿Duermes, pero no descansas?",
                "¿Notas hinchazón, cambios digestivos o dolor de cabeza en épocas de más presión?",
                "¿Te sientes desbordada por cosas que antes gestionabas sin problema?"],
         "close": "La ansiedad no es una debilidad; muchas veces es una señal de sobrecarga."},
        {"type": "explain", "eyebrow": "Qué ocurre en el cuerpo", "h2": "El estrés sostenido tiene una base fisiológica",
         "paras": [
             "Ante una amenaza, el eje hipotálamo-hipófisis-adrenal y el sistema nervioso simpático se activan: aumenta el cortisol, se acelera el corazón, la respiración se vuelve más alta y los músculos se preparan. Es una respuesta útil durante un tiempo limitado.",
             "Cuando la carga se prolonga, esa activación puede mantenerse y afectar al **sueño**, la **digestión**, la **tensión muscular**, la sensibilidad al dolor y el estado de ánimo. No es una falta de voluntad: el estrés sostenido puede desbordar la capacidad de regulación del sistema nervioso.",
             "Nuestro trabajo consiste en ayudarte a identificar qué mantiene esa alerta y a entrenar, paso a paso, recursos que el cuerpo pueda usar: respiración, atención, movimiento, descanso y, cuando hay tensión física, terapia manual. Si el estrés te está quitando el sueño, consulta también nuestra página de [sueño e insomnio](sueno-insomnio); si quieres un programa estructurado, el [curso MBSR de 8 semanas](curso-mindfulness-mbsr-barcelona) es la opción con más evidencia. Muchas personas lo combinan con sesiones de [acupuntura](acupuntura-medicina-tradicional-china) para el estrés y la ansiedad.",
         ]},
        {"type": "cards", "eyebrow": "Cómo te acompañamos", "h2": "Un acompañamiento con recursos concretos",
         "items": [{"k": "Primera consulta", "h": "Valoración integrativa", "p": "Revisamos síntomas físicos, sueño, digestión, hábitos y carga actual para entender cómo se expresa el estrés en tu cuerpo."},
                   {"k": "Sesiones individuales", "h": "Regulación y respiración", "p": "Ejercicios de respiración lenta y atención corporal que puedas aplicar en tu día a día."},
                   {"k": "Terapia manual", "h": "Cuando el estrés se queda en el cuerpo", "p": "Osteopatía para tensión cervical, diafragmática o mandibular asociada al estrés, como complemento al trabajo de regulación."},
                   {"k": "Acupuntura", "h": "Acupuntura para el estrés y la ansiedad", "p": "Una consulta de [acupuntura](acupuntura-medicina-tradicional-china) específica para el estrés y la ansiedad, que en WA LAM solemos combinar con el trabajo de regulación y respiración. Si prefieres no recibir acupuntura, la combinamos con una sesión de [reflexología podal](reflexologia-sarria-sant-gervasi) como alternativa de relajación. La evidencia sobre la acupuntura en ansiedad es todavía preliminar y así te lo explicamos."},
                   {"k": "Programa grupal", "h": "MBSR · 8 semanas", "p": "El programa de reducción del estrés basado en mindfulness, con inscripción propia y la base científica más amplia en este campo."}]},
        {"type": "evidence", "h2": "Lo que podemos y no podemos ofrecer",
         "intro": "Estas son las fuentes científicas en las que se apoya nuestro trabajo, y también sus límites.",
         "items": [("Metaanálisis (Psychological Bulletin)", "Un metaanálisis de 30 años de investigación (casi 300 estudios) muestra que el **estrés crónico** se asocia a la supresión de distintas medidas de la respuesta inmune, mientras que el estrés agudo y breve tiene efectos distintos. Es la base fisiológica de por qué el estrés sostenido nos importa clínicamente."),
                   ("Metaanálisis (JAMA Intern Med)", "Una revisión de 47 ensayos aleatorizados (3.515 participantes) concluye que los programas de meditación producen reducciones de pequeñas a moderadas en ansiedad, depresión y dolor. No fueron superiores a otros tratamientos activos como el ejercicio o la terapia conductual."),
                   ("Ensayo clínico (JAMA Psychiatry)", "En 276 adultos con trastornos de ansiedad (generalizada, social o de pánico), un programa MBSR de 8 semanas resultó **no inferior al escitalopram**, un antidepresivo de primera línea."),
                   ("Límite importante", "No tratamos trastornos de ansiedad graves ni crisis de salud mental. Si lo necesitas, te derivaremos a psicología clínica o psiquiatría, y podemos acompañarte en paralelo.")],
         "refs": [R["segerstrom"], R["goyal"], R["hoge"]]},
    ],
    "faq": [
        ("¿Esto sustituye a la terapia psicológica?", "No. Trabajamos la dimensión corporal y fisiológica del estrés. Si tu situación requiere psicoterapia o tratamiento médico, te derivamos al profesional correspondiente."),
        ("¿Qué diferencia hay entre la consulta individual y el MBSR?", "La consulta individual se adapta a tu situación concreta. El MBSR es un programa grupal estructurado de 8 semanas con fechas e inscripción propias. Muchas personas combinan ambos."),
        ("¿La osteopatía ayuda con el estrés?", "Puede ayudar a aliviar la tensión física asociada y a mejorar la percepción corporal, pero no actúa sobre las causas del estrés. Por eso la proponemos como complemento."),
        ("Tengo crisis de ansiedad. ¿Puedo venir?", "Sí, pero si las crisis son frecuentes o intensas es importante que también te valore un profesional de salud mental. Escríbenos y lo hablamos."),
    ],
    "related": ["sueno-insomnio", "curso-mindfulness-mbsr-barcelona", "acupuntura-medicina-tradicional-china", "osteopatia-sarria-sant-gervasi"],
    "cta": {"h2": "Empecemos por entender qué te está pasando", "p": "Escríbenos por WhatsApp. Sin compromiso, te orientamos sobre la opción más adecuada."},
})

PAGES.append({
    "slug": "salud-digestiva-microbiota", "group": "motivo", "wave": 2,
    "nav": "Salud digestiva y microbiota",
    "card": "Hinchazón, digestiones pesadas, ritmo intestinal alterado o molestias que empeoran con el estrés.",
    "title": "Salud digestiva y microbiota en Barcelona · Sarrià–Sant Gervasi | WA LAM",
    "desc": "Consulta integrativa para molestias digestivas en Barcelona: eje intestino-cerebro, microbiota, alimentación, estrés y osteopatía visceral. PNIE y nutrición intestinal.",
    "about": "Salud digestiva y microbiota intestinal",
    "eyebrow": "Motivo de consulta",
    "h1": "Salud digestiva y microbiota",
    "sub": "Eje intestino-cerebro · Sarrià–Sant Gervasi",
    "lead": "La digestión no depende solo de lo que comes. También influyen el estrés, el sueño, la microbiota, la movilidad del abdomen y la comunicación entre el intestino y el cerebro. Te ayudamos a ordenar esas piezas con una valoración integrativa y un plan realista.",
    "facts": ["Valoración **digestiva integrativa**", "PNIE y nutrición para la salud intestinal", "Osteopatía visceral cuando está indicada",
              "Coordinación con digestivo si hace falta", "Sin dietas restrictivas por defecto"],
    "wa": "Hola, tengo molestias digestivas y me gustaría información sobre la consulta.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando la digestión condiciona tu día",
         "qs": ["¿Te hinchas a lo largo del día aunque comas «bien»?",
                "¿Notas que tu digestión empeora cuando estás estresada?",
                "¿Alternas estreñimiento y diarrea, o tu ritmo intestinal es irregular?",
                "¿Sientes cansancio, niebla mental o peor descanso cuando tu digestión va mal?",
                "¿Has ido quitando alimentos y cada vez comes con más miedo?",
                "¿Te han dicho que es «colon irritable» y no sabes qué más hacer?"]},
        {"type": "explain", "eyebrow": "El eje intestino-cerebro", "h2": "Intestino, sistema nervioso e inmunidad se comunican",
         "paras": [
             "El intestino tiene su propia red nerviosa y se comunica con el cerebro a través del nervio vago, de hormonas y del sistema inmune. La **microbiota intestinal** participa en esa comunicación y en procesos como la digestión, la inflamación y la producción de algunos metabolitos.",
             "Por eso es frecuente que el estrés sostenido altere la digestión, y que una digestión alterada afecte al descanso, la energía o el ánimo. La investigación sobre microbiota avanza rápido, pero todavía hay mucho que no sabemos: desconfía de quien promete que «arreglar la microbiota» lo cura todo.",
             "En consulta revisamos tus síntomas, tu alimentación, tu ritmo de vida y tus pruebas, y te orientamos hacia el profesional adecuado: PNIE, nutrición, osteopatía visceral o derivación médica.",
         ]},
        {"type": "steps", "eyebrow": "La consulta", "h2": "Cómo es la primera visita",
         "items": [("Historia digestiva", "Síntomas, desde cuándo, relación con comidas, estrés y ciclo menstrual, analíticas y pruebas previas."),
                   ("Contexto global", "Sueño, actividad física, carga emocional, medicación y hábitos que influyen en la digestión."),
                   ("Orientación y plan", "Te explicamos qué proponemos y por qué: cambios progresivos, consulta de PNIE o nutrición, terapia manual o derivación.")],
         "note": "Si aparecen señales de alarma (sangrado, pérdida de peso sin causa, anemia, fiebre o síntomas nocturnos que te despiertan), te pediremos que consultes antes con tu médico."},
        {"type": "cards", "eyebrow": "Con qué podemos acompañarte", "h2": "Profesionales y enfoques",
         "items": [{"k": "Consulta", "h": "PNIE", "p": "Una mirada que integra sistema nervioso, inmune y endocrino, estrés, sueño y alimentación."},
                   {"k": "Consulta", "h": "Nutrición y salud intestinal", "p": "Pautas alimentarias individualizadas, progresivas y sostenibles, sin restricciones innecesarias."},
                   {"k": "Terapia manual", "h": "Osteopatía visceral", "p": "Trabajo sobre diafragma, abdomen y cicatrices como complemento cuando hay tensión o restricción de movilidad."}]},
        {"type": "evidence", "h2": "Qué dice la evidencia",
         "items": [("Revisión (Physiological Reviews)", "La revisión de referencia sobre el **eje microbiota-intestino-cerebro** (Cryan y cols., 2019) describe las vías de comunicación —nervio vago, sistema inmune, metabolitos microbianos y eje del estrés— y subraya que buena parte de la evidencia procede todavía de modelos animales."),
                   ("Metaanálisis en red (Gut)", "En el síndrome del intestino irritable, la dieta baja en FODMAP fue la intervención dietética mejor situada en un metaanálisis en red de 13 ensayos (944 pacientes). Los autores advierten que pocos estudios evaluaron la fase de reintroducción, que es la que permite no restringir más de lo necesario."),
                   ("Revisión sistemática", "Las técnicas diagnósticas de la osteopatía visceral no han demostrado ser fiables y faltan ensayos de calidad sobre su eficacia. La proponemos solo como complemento y lo explicamos así a cada paciente.")],
         "refs": [R["cryan"], R["black"], R["guillaud_v"]]},
    ],
    "faq": [
        ("¿Hacéis estudio de microbiota?", "Sí. El estudio de microbiota intestinal, que se deriva a un laboratorio especializado, lo valoramos en la primera visita y lo recomendamos cuando puede cambiar el plan. Sus resultados se integran en el informe de valoración, como explicamos en [longevidad y prevención](prevencion-longevidad). Si se plantea un estudio de parásitos, comprobamos antes qué incluye el perfil elegido para no duplicar pruebas."),
        ("¿Tendré que hacer una dieta muy estricta?", "No por defecto. Algunas personas se benefician de cambios temporales y guiados, pero evitamos restricciones prolongadas sin motivo."),
        ("¿La osteopatía visceral sirve para la digestión?", "Puede ayudar a algunas personas a sentir menos tensión abdominal y mejor movilidad del diafragma. La evidencia científica es todavía limitada, por eso la proponemos como complemento y no como tratamiento único."),
        ("¿Sustituye a la consulta de digestivo?", "No. Si tus síntomas requieren estudio médico, te lo indicaremos. Podemos acompañarte en paralelo."),
    ],
    "related": ["pni-pnie-barcelona", "nutricion-salud-intestinal", "osteopatia-sarria-sant-gervasi", "estres-ansiedad"],
    "cta": {"h2": "Ordenemos juntos lo que le pasa a tu digestión", "p": "Escríbenos por WhatsApp y te orientamos sobre qué consulta encaja mejor contigo."},
})

PAGES.append({
    "slug": "acompanamiento-fertilidad", "group": "motivo", "wave": 2,
    "nav": "Acompañamiento en fertilidad",
    "card": "Un acompañamiento integrativo complementario a tu seguimiento ginecológico o de reproducción asistida.",
    "title": "Acompañamiento integrativo en fertilidad · Barcelona | WA LAM",
    "desc": "Acompañamiento integrativo en fertilidad en Sarrià–Sant Gervasi: hábitos, estrés, nutrición, acupuntura y terapia manual, como complemento de tu seguimiento ginecológico o de reproducción asistida.",
    "about": "Fertilidad",
    "eyebrow": "Motivo de consulta",
    "h1": "Acompañamiento en fertilidad",
    "sub": "Un acompañamiento integrativo y complementario",
    "lead": "Buscar un embarazo puede ser un proceso largo y exigente, física y emocionalmente. En WA LAM ofrecemos un acompañamiento que cuida hábitos, estrés, descanso y bienestar corporal, siempre como complemento del seguimiento ginecológico o de reproducción asistida y nunca en su lugar.",
    "facts": ["Atiende: [[profesional responsable]]", "Hábitos, nutrición y descanso", "Acupuntura y terapia manual de apoyo",
              "Gestión del estrés durante el proceso", "Coordinación con tu ginecóloga o clínica"],
    "wa": "Hola, me gustaría información sobre el acompañamiento en fertilidad.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando el proceso pesa más de lo que esperaba",
         "qs": ["¿Llevas tiempo buscando un embarazo y sientes que todo gira en torno a ello?",
                "¿Estás en un tratamiento de reproducción asistida y quieres cuidarte durante el proceso?",
                "¿Te cuesta gestionar la espera, la incertidumbre y el desgaste emocional?",
                "¿Quieres revisar tus hábitos, pero no sabes qué información es fiable?"]},
        {"type": "explain", "eyebrow": "Nuestro enfoque", "h2": "Acompañar sin prometer",
         "paras": [
             "La fertilidad depende de muchos factores y algunos no se pueden modificar. Por eso no hablamos de «aumentar la fertilidad» como si fuera una garantía. Sí podemos ayudarte a **cuidar los factores modificables** —alimentación, sueño, actividad física, consumo de tóxicos, estrés— y a vivir el proceso con más recursos.",
             "Si estás en seguimiento con una ginecóloga o una clínica de reproducción, adaptamos el acompañamiento a las fases y fechas de tu tratamiento.",
         ]},
        {"type": "cards", "eyebrow": "Qué incluye", "h2": "Un acompañamiento a tu medida",
         "items": [{"k": "Hábitos", "h": "Nutrición y estilo de vida", "p": "Pautas basadas en evidencia sobre alimentación, peso, actividad física, sueño y tóxicos."},
                   {"k": "Cuerpo", "h": "Acupuntura y terapia manual", "p": "Acupuntura, [reflexología podal](reflexologia-sarria-sant-gervasi) o terapia manual como apoyo al bienestar y a la gestión del estrés durante el proceso, no como tratamiento de la infertilidad."},
                   {"k": "Sistema nervioso", "h": "Gestión del estrés", "p": "Recursos de respiración y mindfulness para atravesar la espera y los momentos difíciles."}]},
        {"type": "evidence", "h2": "Lo que dice la evidencia, sin rodeos",
         "items": [("Ensayo clínico (JAMA)", "En el ensayo aleatorizado más amplio sobre acupuntura en fecundación in vitro (848 mujeres, 16 centros), la tasa de nacidos vivos fue prácticamente igual con acupuntura real (18,3 %) que con acupuntura simulada (17,8 %). **La acupuntura no mejora la tasa de nacidos vivos en FIV** y así te lo explicamos."),
                   ("Nuestro criterio", "Por eso no ofrecemos la acupuntura para aumentar las probabilidades de embarazo. La ofrecemos, si la deseas, como apoyo para tu bienestar durante un proceso exigente."),
                   ("Factores modificables", "Peso, tabaco, alcohol, actividad física y sueño sí forman parte de las recomendaciones de las sociedades de ginecología y reproducción, y son el núcleo de nuestro acompañamiento.")],
         "refs": [R["smith"]]},
        ficha("Ficha del servicio", "Acompañamiento en fertilidad", "Primera consulta para conocer tu situación y diseñar el acompañamiento según la fase en la que estés.",
              [("Profesional", "[[Nombre y titulación]]"), ("Formato", "Individual o en pareja"), ("Primera visita", "60 min · 90 €")]),
    ],
    "faq": [
        ("¿Esto sustituye a un tratamiento de fertilidad?", "No. Es un acompañamiento complementario. Las decisiones diagnósticas y de tratamiento corresponden a tu ginecóloga o a tu clínica de reproducción."),
        ("¿La acupuntura mejora las probabilidades de embarazo?", "No hay pruebas de que lo haga. Un ensayo clínico con 848 mujeres publicado en JAMA no encontró diferencias en la tasa de nacidos vivos frente a la acupuntura simulada. Algunas personas la eligen por bienestar y para gestionar el estrés; te lo explicamos para que decidas con información."),
        ("¿Podemos venir en pareja?", "Sí. Atendemos tanto de forma individual como en pareja."),
    ],
    "related": ["acupuntura-medicina-tradicional-china", "salud-mujer-menopausia", "estres-ansiedad"],
    "cta": {"h2": "Hablemos de tu proceso", "p": "Escríbenos con confianza. Te explicaremos cómo podemos acompañarte."},
})

PAGES.append({
    "slug": "salud-mujer-menopausia", "group": "motivo", "wave": 3,
    "nav": "Salud de la mujer y menopausia",
    "card": "Perimenopausia y menopausia: sueño, energía, dolor, suelo pélvico, ánimo y salud a largo plazo.",
    "title": "Salud de la mujer y menopausia en Barcelona · Sarrià–Sant Gervasi | WA LAM",
    "desc": "Acompañamiento integrativo en perimenopausia y menopausia en Barcelona: sueño, fuerza, suelo pélvico, digestión, estrés y hábitos para una salud duradera.",
    "about": "Menopausia y salud de la mujer",
    "eyebrow": "Motivo de consulta",
    "h1": "Salud de la mujer y menopausia",
    "sub": "Perimenopausia, menopausia y salud a largo plazo",
    "lead": "La transición a la menopausia afecta al sueño, la temperatura, el ánimo, la masa muscular, la salud ósea, el suelo pélvico y la digestión. No es algo que «haya que aguantar». Te acompañamos con una mirada integrativa, como complemento del seguimiento ginecológico.",
    "facts": ["Sueño, sofocos y energía", "Fuerza, huesos y movimiento", "Suelo pélvico y dolor pélvico",
              "Digestión, peso y metabolismo", "Coordinación con ginecología"],
    "wa": "Hola, estoy en perimenopausia/menopausia y me gustaría información sobre cómo podéis acompañarme.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando tu cuerpo cambia y no te reconoces",
         "qs": ["¿Te despiertas de madrugada y ya no consigues volver a dormir?",
                "¿Sientes que tu cuerpo ya no se recupera como antes?",
                "¿Han aparecido dolores articulares, cambios de peso o hinchazón sin motivo claro?",
                "¿Notas más irritabilidad, ansiedad o niebla mental?",
                "¿Tienes molestias de suelo pélvico, pérdidas de orina o dolor en las relaciones?"],
         "close": "Tu cuerpo no está fallando; está atravesando una transición que merece atención."},
        {"type": "explain", "eyebrow": "Una etapa con impacto en todo el cuerpo", "h2": "Qué cambia y qué podemos cuidar",
         "paras": [
             "La disminución de estrógenos influye en la regulación de la temperatura, el sueño, el estado de ánimo, la masa muscular, la densidad ósea, los tejidos del suelo pélvico y el metabolismo. Cada mujer lo vive de forma distinta.",
             "El tratamiento médico, incluida la terapia hormonal cuando está indicada, corresponde a tu ginecóloga. Desde WA LAM trabajamos lo que suma a ese seguimiento: **fuerza y movimiento**, sueño, alimentación, gestión del estrés, suelo pélvico y dolor.",
             "Hoy ofrecemos estas consultas dentro de una página conjunta.",
         ]},
        {"type": "cards", "eyebrow": "Cómo te acompañamos", "h2": "Enfoques según lo que necesites",
         "items": [{"k": "Movimiento", "h": "Fuerza y suelo pélvico", "p": "Ejercicio de fuerza adaptado para proteger músculo y hueso. Si necesitas fisioterapia de suelo pélvico, te derivamos a una fisioterapeuta especializada."},
                   {"k": "Hábitos", "h": "Sueño, nutrición y PNIE", "p": "Revisión de descanso, alimentación y estrés con pautas realistas."},
                   {"k": "Cuerpo", "h": "Osteopatía", "p": "Para dolor articular, tensión pélvica o diafragmática como complemento."},
                   {"k": "Embarazo", "h": "Drenaje linfático en el embarazo", "p": "Si estás embarazada, una sesión adaptada para la pesadez y la hinchazón: [drenaje linfático durante el embarazo](drenaje-linfatico-embarazo)."},
                   {"k": "Grupo", "h": "Yoga, qigong y mindfulness", "p": "Prácticas de movimiento y regulación en la Academia."},
                   {"k": "Acupuntura", "h": "[Acupuntura](acupuntura-medicina-tradicional-china)", "p": "Como apoyo para los sofocos, el descanso y el bienestar en esta etapa."}]},
        {"type": "evidence", "h2": "En qué nos basamos",
         "items": [("Posicionamiento (NAMS 2022)", "La North American Menopause Society establece que la terapia hormonal es el tratamiento más eficaz para los síntomas vasomotores y el síndrome genitourinario de la menopausia, y que en mujeres sanas menores de 60 años o en los 10 primeros años tras la menopausia sus beneficios suelen superar a los riesgos. Esa decisión corresponde a tu ginecóloga."),
                   ("Metaanálisis (BJSM)", "Hacer ejercicio de fuerza se asocia a un 10–17 % menos de mortalidad, enfermedad cardiovascular, cáncer y diabetes, con el mayor beneficio en torno a 30–60 minutos semanales. Por eso la fuerza es prioritaria en esta etapa."),
                   ("Ensayo clínico (Menopause)", "En un ensayo pragmático con 209 mujeres, la acupuntura redujo un 36,7 % la frecuencia de los sofocos a los seis meses, frente a un aumento del 6 % en el grupo control. El estudio no tenía grupo de acupuntura simulada, por lo que parte del efecto puede deberse a las expectativas (Avis et al., Menopause, 2016)."),
                   ("Nuestro papel", "Complementamos el seguimiento ginecológico con ejercicio de fuerza, sueño, alimentación, suelo pélvico y gestión del estrés.")],
         "refs": [R["nams"], R["momma"], R["avis"]]},
    ],
    "faq": [
        ("¿Recetáis terapia hormonal?", "No. Esa decisión corresponde a tu ginecóloga. En WA LAM te acompañamos en los aspectos de hábitos, movimiento y bienestar."),
        ("¿Valoráis la microbiota vaginal?", "Ante molestias o infecciones de repetición, valoramos en la primera visita si conviene un estudio dirigido o una consulta con tu ginecóloga. Si conviene un estudio, te derivamos a un centro especializado. Lo explicamos en [longevidad y prevención](prevencion-longevidad)."),
        ("¿Cuándo empieza la perimenopausia?", "Suele empezar entre los 40 y los 50 años, con cambios en el ciclo y síntomas que pueden aparecer años antes de la última regla."),
        ("¿Quién atiende estas consultas?", "Rosa María Rodríguez Valls, osteópata D.O."),
    ],
    "related": ["suelo-pelvico-dolor-pelvico", "pni-pnie-barcelona", "prevencion-longevidad", "yoga-particular-grupos-reducidos"],
    "cta": {"h2": "Cuídate en esta etapa con información y acompañamiento", "p": "Escríbenos y te explicamos qué opción encaja contigo."},
})

PAGES.append({
    "slug": "prevencion-longevidad", "group": "motivo", "wave": 1,
    "nav": "Longevidad y prevención",
    "card": "Un recorrido claro para cuidar tu salud a largo plazo: primera visita, valoración, plan por fases y seguimiento.",
    "title": "Longevidad y prevención en Barcelona · Sarrià–Sant Gervasi | WA LAM",
    "desc": "Longevidad y prevención en Sarrià–Sant Gervasi, Barcelona: primera visita, valoración de hábitos y pruebas, plan por fases y seguimiento.",
    "about": "Envejecimiento saludable y prevención",
    "eyebrow": "Longevidad y prevención",
    "h1": "Longevidad y prevención en Barcelona",
    "sub": "Medicina integrativa para vivir más años con salud · Sarrià–Sant Gervasi",
    "lead": "La medicina de longevidad es un enfoque preventivo que busca prolongar los años vividos con buena salud, no solo los años de vida. Valora cómo envejece tu organismo (metabolismo, inflamación, fuerza, sueño, salud hormonal y cerebral) y diseña un programa para actuar sobre ello antes de que aparezca la enfermedad.",
    "facts_title": "Tu recorrido",
    "facts": ["**1.** Antes de la visita: formulario y analíticas", "**2.** Primera visita: 60 min · 90 €",
              "**3.** Valoración y plan por fases", "**4.** Seguimiento y pautas de mantenimiento", "Atiende: Rosa María Rodríguez Valls, osteópata D.O. y máster en medicina integrativa"],
    "cta2": ("Cómo funciona", "#como-funciona-el-programa-de-longevidad"),
    "wa": "Hola, me interesa la consulta de longevidad y prevención. ¿Cómo es la primera visita?",
    "blocks": [
        {"type": "explain", "eyebrow": "Medicina de longevidad", "h2": "Qué es la medicina de longevidad",
         "paras": [
             "La esperanza de vida no ha dejado de aumentar, pero muchas personas pasan sus últimas décadas con enfermedades crónicas, dolor o pérdida de autonomía. El reto ya no es solo vivir más, sino mantener la energía, la movilidad y la claridad mental durante esos años.",
             "Los factores con más respaldo científico para envejecer con salud son conocidos: **actividad física y fuerza**, sueño suficiente y regular, alimentación de calidad, salud digestiva, gestión del estrés, no fumar, moderar el alcohol y mantener relaciones sociales. No son glamurosos, pero funcionan cuando se sostienen en el tiempo.",
             "La prevención también protege el cerebro: según la Comisión de The Lancet de 2024, cerca de la mitad de los casos de demencia se asocian a 14 factores de riesgo modificables. Por eso la [neurolongevidad y salud cognitiva](neurolongevidad-salud-cognitiva) forma parte de este recorrido.",
             "En WA LAM no vendemos tratamientos «antiaging», sueros ni suplementos sin indicación. Te ayudamos a ver dónde estás en cada pilar, a priorizar y a construir un plan que encaje en tu vida.",
         ]},
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuándo considerar un programa de longevidad",
         "qs": ["¿Te encuentras bien, pero notas que pierdes fuerza, energía o capacidad de recuperación con los años?",
                "¿Quieres saber qué hábitos te conviene priorizar y en qué orden?",
                "¿Te abruma la información sobre longevidad y no sabes qué es fiable?",
                "¿Tienes antecedentes familiares y quieres anticiparte?",
                "¿Te preocupa mantener la memoria y la claridad mental en el futuro?",
                "¿Duermes peor, digieres peor o te notas más tensa que hace unos años?",
                "¿Te cuesta concentrarte o notas niebla mental al final del día?",
                "¿Has ganado peso sin cambios aparentes en tus hábitos?",
                "¿Estás en la perimenopausia o la menopausia y quieres cuidarte en esta etapa?"],
         "close": "Si te reconoces en varias de estas situaciones, una valoración global permite detectar a tiempo desequilibrios metabólicos, hormonales o inflamatorios y actuar sobre ellos."},
        {"type": "cards", "eyebrow": "Áreas del programa", "h2": "Qué incluye el programa de longevidad",
         "intro": "El programa se construye a partir de tu valoración. Estas son las áreas que trabaja, siempre adaptadas a tu caso.",
         "items": [{"k": "01", "h": "Diagnóstico integral", "p": "Historia clínica, hábitos y, si aportan información útil, analíticas avanzadas, microbiota, genética y composición corporal para conocer cómo está envejeciendo tu organismo."},
                   {"k": "02", "h": "Nutrición y salud metabólica", "p": "Alimentación antiinflamatoria y personalizada para mejorar la sensibilidad a la insulina, el perfil lipídico y la salud intestinal. Más en [salud digestiva y microbiota](salud-digestiva-microbiota)."},
                   {"k": "03", "h": "Salud cerebral", "p": "Protección de la memoria, la atención y la función ejecutiva actuando sobre los factores de riesgo modificables. Más en [neurolongevidad](neurolongevidad-salud-cognitiva)."},
                   {"k": "04", "h": "Sueño y ritmos circadianos", "p": "Recuperar un descanso suficiente y regular, clave para la reparación de los tejidos y la memoria. Más en [sueño e insomnio](sueno-insomnio)."},
                   {"k": "05", "h": "Salud hormonal", "p": "Acompañamiento en la perimenopausia y la menopausia, una etapa decisiva para la salud ósea, cardiovascular y cerebral. Más en [salud de la mujer](salud-mujer-menopausia)."},
                   {"k": "06", "h": "Fuerza, movilidad y equilibrio", "p": "Ejercicio adaptado para preservar la masa muscular y la autonomía, con apoyo de [yoga](yoga-particular-grupos-reducidos) y [qigong](qigong-barcelona)."},
                   {"k": "07", "h": "Estrés y equilibrio emocional", "p": "Regulación del sistema nervioso con mindfulness y respiración. Más en [estrés y ansiedad](estres-ansiedad) y en el [curso MBSR](curso-mindfulness-mbsr-barcelona)."}]},
        {"type": "cards", "eyebrow": "Valoración de precisión", "h2": "Diagnóstico: las pruebas de la valoración de longevidad", "intro": "Seleccionamos las pruebas según tu caso: no todas las personas necesitan todas. Se realizan en laboratorios especializados y sus resultados se integran en un informe final con tu plan de acción.", "items": [{"k": "01", "h": "Analítica general y metabolismo", "p": "Panel amplio de biomarcadores: glucosa e insulina, perfil lipídico, función hepática y renal, marcadores de inflamación, vitaminas y minerales."}, {"k": "02", "h": "Salud cardiovascular", "p": "Marcadores avanzados de riesgo cardiovascular, como la lipoproteína(a), la apolipoproteína B o la PCR ultrasensible. Si se requieren pruebas de imagen, se realiza la derivación a cardiología."}, {"k": "03", "h": "Hormonas", "p": "Paneles hormonales: función tiroidea, hormonas sexuales y eje del estrés."}, {"k": "04", "h": "Genética", "p": "Pruebas genéticas individualizadas y farmacogenética. Una predisposición no es un destino: se interpreta junto a tus hábitos y tu historia."}, {"k": "05", "h": "Microbiota intestinal", "p": "Estudio del microbioma intestinal y, según el perfil, marcadores de digestión, inflamación y permeabilidad intestinal."}, {"k": "06", "h": "Epigenética", "p": "Estimación de la edad biológica mediante marcadores epigenéticos. Es una herramienta emergente: se interpreta con cautela y como referencia evolutiva."}, {"k": "07", "h": "Salud cognitiva", "p": "Valoración de la función cognitiva y de los factores de riesgo modificables que influyen en ella."}, {"k": "08", "h": "Composición corporal", "p": "Masa muscular, masa grasa y su distribución, como referencia para el plan de nutrición y ejercicio."}, {"k": "09", "h": "Sueño y estrés", "p": "Valoración de la calidad del sueño, los ritmos circadianos, el nivel de estrés y la capacidad de recuperación."}, {"k": "10", "h": "Informe final", "p": "Informe escrito que integra todos los resultados con tu historia clínica y define tu plan de acción individualizado."}]},
        {"type": "cards", "eyebrow": "Según tu caso", "h2": "Otras valoraciones según tu caso",
         "intro": "En la primera visita valoramos si conviene una prueba dirigida o una consulta con el especialista correspondiente.",
         "items": [{"k": "Intestino", "h": "Estudio de parásitos intestinales", "p": "Si tus síntomas lo justifican, valoramos un estudio de parásitos. Antes comprobamos qué incluye el perfil intestinal elegido, para no duplicar pruebas. Relacionado con [salud digestiva y microbiota](salud-digestiva-microbiota)."},
                   {"k": "Boca", "h": "Salud bucodental y microbiota oral", "p": "La salud de las encías se relaciona con la inflamación general. Si aparece algún signo o conviene un estudio de microbiota oral, te derivamos a tu dentista, a un periodoncista o a un centro especializado."},
                   {"k": "Mujer", "h": "Salud vaginal y microbiota vaginal", "p": "Ante molestias vaginales o infecciones de repetición, valoramos si conviene un estudio de microbiota vaginal y, en ese caso, te derivamos a tu ginecóloga o a un centro especializado. Más información en [salud de la mujer y menopausia](salud-mujer-menopausia)."}]},
        {"type": "steps", "eyebrow": "El proceso", "h2": "Cómo funciona el programa de longevidad",
         "items": [("Antes de la visita", "Rellenas el [formulario de primera cita](https://www.walambcn.com/primera-cita) con tu historia médica, medicación, sueño, alimentación, digestión, actividad física y nivel de estrés, y nos envías tus analíticas y pruebas recientes."),
                   ("Primera visita", "En la primera visita (60 minutos, 90 €) revisamos tu historia, tus pruebas y tus hábitos, y escuchamos qué quieres conseguir. Con esa información preparamos tu tratamiento personalizado."),
                   ("Valoración y plan", "Si puede cambiar el plan, proponemos pruebas complementarias, como el estudio de microbiota intestinal o pruebas genéticas, y sus resultados se integran en tu informe de valoración. Con los resultados diseñamos tu programa de longevidad, centrado en el cambio de hábitos. Al terminar cada consulta recibes por escrito las recomendaciones de la fase en curso."),
                   ("Seguimiento", "Revisamos la evolución en las sesiones de tu tratamiento, puedes escribirnos por correo con tus dudas entre sesiones y, al terminar, recibes unas pautas de mantenimiento para consolidar lo conseguido.")],
         "note": "Esta consulta no sustituye el seguimiento de tu médico de atención primaria ni los controles que te correspondan. Cuando consideramos que un hallazgo requiere una valoración médica complementaria, realizamos la derivación al especialista correspondiente."},
        {"type": "cards", "eyebrow": "Beneficios", "h2": "Beneficios del programa de longevidad", "intro": "El objetivo no es sumar años, sino ganar años con buena salud. Estos son los ámbitos en los que se concentra el plan, siempre a partir de tu valoración y con objetivos medibles.", "items": [
            {"k": "01", "h": "Energía y capacidad de recuperación", "p": "Identificar lo que consume tu energía, como el sueño insuficiente, el sedentarismo, una alimentación desordenada o el estrés sostenido, y corregirlo por orden de prioridad."},
            {"k": "02", "h": "Salud cerebral", "p": "Proteger la memoria, la atención y la función ejecutiva actuando sobre los factores de riesgo modificables de deterioro cognitivo."},
            {"k": "03", "h": "Inflamación de bajo grado", "p": "Reducir los factores que mantienen la inflamación crónica silenciosa, relacionada con la mayoría de las enfermedades asociadas al envejecimiento."},
            {"k": "04", "h": "Salud metabólica y cardiovascular", "p": "Mejorar la sensibilidad a la insulina, el perfil lipídico y la tensión arterial, los marcadores que más predicen la salud a largo plazo."},
            {"k": "05", "h": "Fuerza, masa muscular y movilidad", "p": "Preservar el músculo y el equilibrio, determinantes de la autonomía y del riesgo de caídas en las décadas siguientes."},
            {"k": "06", "h": "Sueño y ritmos circadianos", "p": "Recuperar un descanso suficiente y regular, imprescindible para la reparación de los tejidos, el metabolismo y la consolidación de la memoria."},
            {"k": "07", "h": "Salud digestiva y microbiota", "p": "Equilibrar la digestión y la microbiota intestinal, que intervienen en la inmunidad, el metabolismo y la inflamación."},
            {"k": "08", "h": "Equilibrio emocional y vínculos", "p": "Regular el estrés y cuidar las relaciones sociales, factores con un impacto demostrado en la esperanza de vida saludable."}]},
        ficha("Ficha del servicio", "Consulta de longevidad y prevención", "La primera visita es el punto de partida del programa de longevidad.",
              [("Primera visita", "60 min · 90 €"), ("Incluye", "Anamnesis completa, revisión de tus pruebas y propuesta de programa"), ("Programa", "Cambio de hábitos, con duración según tus objetivos"), ("Precio del programa", "Presupuesto personalizado tras la primera visita"), ("Modalidad", "Presencial en Sarrià–Sant Gervasi")]),
        {"type": "evidence", "h2": "Longevidad basada en datos, no en modas",
         "items": [("Metaanálisis (BMJ)", "En 36.383 adultos con actividad medida por acelerómetro, **cualquier nivel de actividad física**, incluso de intensidad ligera, se asoció a menor mortalidad. El mayor tiempo sentado se asoció a un riesgo claramente más alto."),
                   ("Metaanálisis (BJSM)", "El ejercicio de fuerza se asocia a un 10–17 % menos de mortalidad y enfermedad crónica. Combinado con ejercicio aeróbico, la reducción de la mortalidad por todas las causas llega aproximadamente al 40 %."),
                   ("Metaanálisis (Biol Psychiatry)", "Las alteraciones del sueño se asocian a niveles más altos de marcadores inflamatorios como la PCR y la IL-6 (72 estudios, más de 50.000 personas)."),
                   ("Comisión The Lancet (2024)", "Cerca de la mitad de los casos de demencia se asocian a 14 factores de riesgo modificables a lo largo de la vida, como la inactividad física, la hipertensión, el colesterol LDL elevado, la pérdida de audición o de visión y el aislamiento social."),
                   ("Lo que no hacemos", "No ofrecemos tratamientos «antiaging», sueros ni suplementos sin indicación. Priorizamos lo que ha demostrado impacto: moverse, ganar fuerza, dormir y gestionar el estrés.")],
         "refs": [R["ekelund"], R["momma"], R["irwin"], R["lancet_dem"]]},
    ],
    "faq": [
        ("¿Qué es la medicina de longevidad?", "Es un enfoque preventivo que busca prolongar los años vividos con buena salud. Valora de forma global los factores que determinan cómo envejecemos (metabolismo, inflamación, sueño, actividad física, alimentación, estrés y salud cognitiva) y diseña un plan individual para actuar sobre ellos antes de que aparezca la enfermedad."),
        ("¿Está basada en la evidencia científica?", "Sí, en lo que tiene respaldo: la actividad física, el ejercicio de fuerza, el sueño, la alimentación de calidad y el control de los factores de riesgo cardiovascular y metabólico. Las herramientas emergentes, como los relojes epigenéticos, se interpretan con cautela."),
        ("¿Es seguro?", "El plan se basa en cambios de hábitos y en terapias de bajo riesgo, adaptados a tu historia clínica y a tu medicación. No incluye tratamientos «antiaging» sin respaldo científico."),
        ("¿Cuándo se notan los resultados?", "La energía y el descanso suelen mejorar en las primeras semanas. Los cambios en los marcadores analíticos y en la composición corporal requieren, como mínimo, las 12 semanas del programa."),
        ("¿Quién puede beneficiarse?", "Cualquier persona adulta que quiera anticiparse: quienes tienen antecedentes familiares, notan pérdida de energía o de fuerza, atraviesan la perimenopausia o quieren mejorar su salud metabólica y cognitiva."),
        ("¿Dónde se realiza la consulta?", "En el centro WA LAM, en la calle Bisbe Sivilla, 44, en Sarrià–Sant Gervasi (Barcelona)."),
        ("¿Necesito tener algún problema de salud para venir?", "No. La consulta está pensada precisamente para personas que quieren anticiparse."),
        ("¿Qué tengo que traer a la primera visita?", "Tus analíticas y pruebas médicas recientes. Antes de la visita te pediremos que rellenes el formulario de primera cita."),
        ("¿Pedís pruebas adicionales?", "Solo cuando pueden cambiar el plan. La más habitual es el estudio de microbiota intestinal; según tu caso, valoramos otras pruebas o una consulta con el especialista."),
        ("¿Qué pruebas incluye la valoración?", "Según tu caso: analítica general y metabólica, marcadores cardiovasculares, paneles hormonales, pruebas genéticas, estudio de microbiota, epigenética, valoración cognitiva, composición corporal y valoración del sueño y del estrés. Todo se integra en un informe final con tu plan de acción."),
        ("¿Recomendáis suplementos?", "Solo cuando hay una indicación clara y evidencia que lo respalde. No forman parte del plan por defecto."),
        ("¿Cuánto cuesta?", "La primera visita dura 60 minutos y cuesta 90 €. Después recibes un presupuesto personalizado para tu programa; los costes de laboratorio se abonan aparte."),
        ("¿Cuánto dura el programa?", "El programa base dura 12 semanas, el tiempo mínimo que necesitan los cambios en la alimentación, la microbiota y los hábitos para consolidarse, y puede prolongarse según tu evolución."),
    ],
    "related": ["programas-re-trace", "neurolongevidad-salud-cognitiva", "estres-ansiedad", "sueno-insomnio"],
    "cta": {"h2": "Empieza tu recorrido de longevidad", "p": "Escríbenos por WhatsApp o reserva tu primera visita en Sarrià–Sant Gervasi."},
})

PAGES.append({
    "slug": "neurolongevidad-salud-cognitiva", "group": "motivo", "wave": 2,
    "nav": "Neurolongevidad y salud cognitiva",
    "card": "Cuidar la memoria, la atención y la regulación del sistema nervioso a lo largo de los años.",
    "title": "Neurolongevidad y salud cognitiva en Barcelona | WA LAM",
    "desc": "Neurolongevidad y salud cognitiva en Sarrià–Sant Gervasi, Barcelona: hábitos que protegen el cerebro, regulación del estrés y del sueño, y qué dice la evidencia sobre la neurorregulación y la estimulación transcraneal.",
    "about": "Salud cognitiva",
    "eyebrow": "Motivo de consulta",
    "h1": "Neurolongevidad y salud cognitiva",
    "sub": "Cuidar el cerebro a lo largo de la vida · Sarrià–Sant Gervasi",
    "lead": "La salud cognitiva no depende solo de la edad. El sueño, el estrés sostenido, la actividad física, la salud cardiovascular y metabólica, la audición, los vínculos y la estimulación mental influyen en cómo envejece el cerebro. Esta consulta forma parte de nuestro recorrido de [longevidad y prevención](prevencion-longevidad).",
    "facts": ["Valoración de hábitos que protegen el cerebro", "Regulación del estrés y del sueño", "Primera visita: 90 €", "Próximamente: neurorregulación y estimulación transcraneal",
              "Curso MBSR de 8 semanas", "Atiende: Rosa María Rodríguez Valls"],
    "wa": "Hola, me interesa la consulta de salud cognitiva y neurolongevidad.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando notas que tu mente no responde como antes",
         "qs": ["¿Te cuesta más concentrarte o recordar cosas en épocas de estrés o de mal descanso?",
                "¿Tienes antecedentes familiares de demencia y quieres saber qué puedes hacer?",
                "¿Notas «niebla mental» junto a cansancio, digestiones pesadas o mal sueño?",
                "¿Quieres cuidar tu memoria y tu atención con hábitos que tengan respaldo científico?"],
         "close": "Si los olvidos son frecuentes, progresivos o interfieren en tu vida diaria, consulta primero con tu médico."},
        {"type": "explain", "eyebrow": "Qué sabemos", "h2": "El cerebro también se puede cuidar",
         "paras": [
             "La Comisión de The Lancet de 2024 estima que cerca de la mitad de los casos de demencia se asocian a **14 factores de riesgo modificables** a lo largo de la vida: menor nivel educativo, pérdida de audición, colesterol LDL elevado, depresión, traumatismos craneales, inactividad física, diabetes, tabaquismo, hipertensión, obesidad, consumo excesivo de alcohol, aislamiento social, contaminación del aire y pérdida de visión.",
             "En el ensayo FINGER, una intervención de dos años que combinaba alimentación, ejercicio, entrenamiento cognitivo y control del riesgo vascular mejoró ligeramente el rendimiento cognitivo en personas mayores con riesgo. Es una mejora modesta, pero confirma que los hábitos importan.",
             "En la consulta revisamos esos factores contigo y diseñamos un plan dentro de tu recorrido de longevidad, con apoyo para el [estrés](estres-ansiedad) y el [sueño](sueno-insomnio).",
         ]},
        {"type": "cards", "eyebrow": "Qué ofrecemos", "h2": "Servicios de salud cognitiva en WA LAM",
         "intro": "La neurorregulación y la estimulación transcraneal todavía no están disponibles en WA LAM. Te explicamos qué son y qué dice la evidencia; cuando las incorporemos, lo anunciaremos aquí con su indicación y su precio.",
         "items": [{"k": "Consulta", "h": "Valoración de hábitos", "p": "Sueño, estrés, actividad física, alimentación, salud cardiovascular y vínculos, dentro del recorrido de longevidad."},
                   {"k": "Próximamente", "h": "Neurorregulación", "p": "Estimulación eléctrica de baja intensidad aplicada sobre la piel con electrodos, sin agujas y sin atravesar el cráneo. Pertenece a la misma familia que la TENS, la técnica de este tipo más estudiada: un metaanálisis de 381 estudios mostró que reduce la intensidad del dolor durante el tratamiento o justo después, frente a placebo. Para otros usos, como el estrés o el sueño, la evidencia es todavía escasa."},
                   {"k": "Próximamente", "h": "Estimulación eléctrica transcraneal", "p": "La estimulación transcraneal por corriente continua (tDCS) aplica una corriente muy débil a través de electrodos colocados sobre el cuero cabelludo para modificar la actividad de zonas concretas del cerebro. Las guías la consideran eficaz en la depresión y probablemente eficaz en algunos tipos de dolor, con efectos modestos. Si la incorporamos, se aplicará solo con indicación y en coordinación con tu médico."},
                   {"k": "Programa", "h": "MBSR · 8 semanas", "p": "Entrenamiento de la atención y de la regulación del estrés: el [curso MBSR](curso-mindfulness-mbsr-barcelona)."}]},
        {"type": "evidence", "h2": "Lo que ofrecemos y lo que se sabe",
         "items": [("Comisión The Lancet (2024)", "Cerca de la mitad de los casos de demencia se asocian a 14 factores de riesgo modificables. Actuar sobre ellos es la estrategia preventiva con más respaldo."),
                   ("Ensayo clínico (The Lancet)", "En el ensayo FINGER, una intervención multidominio de dos años mejoró ligeramente la función cognitiva en personas de 60 a 77 años con riesgo, frente a consejos de salud generales."),
                   ("Revisión cuantitativa (Brain Stimulation)", "En adultos sanos, una sesión de estimulación transcraneal por corriente continua (tDCS) no mostró efectos fiables sobre la cognición en 59 análisis. Por eso no la presentamos como un método para «mejorar el cerebro»."),
                   ("Guía y metaanálisis (Int J Neuropsychopharmacol)", "Según las guías basadas en la evidencia de 2021, la tDCS es eficaz en la depresión (nivel A) y probablemente eficaz en el dolor neuropático, la fibromialgia y la migraña (nivel B). Los efectos son modestos y su duración, limitada."),
                   ("Metaanálisis (BMJ Open)", "En 381 estudios, la estimulación eléctrica transcutánea (TENS) redujo la intensidad del dolor durante el tratamiento o justo después, frente a placebo, con certeza moderada. Los efectos adversos fueron leves."),
                   ("Nuestro criterio", "Las técnicas de estimulación las describimos con prudencia y solo como complemento de los hábitos que sí han demostrado proteger la salud cognitiva.")],
         "refs": [R["lancet_dem"], R["finger"], R["horvath"], R["fregni"], R["tens"]]},
    ],
    "faq": [
        ("¿Hacéis diagnóstico de deterioro cognitivo?", "No. Si los olvidos son frecuentes o progresivos, el diagnóstico corresponde a tu médico o a un neurólogo. Podemos acompañarte en los hábitos y en la regulación del estrés y del sueño."),
        ("¿Qué es la neurorregulación?", "Es una forma de estimulación eléctrica de baja intensidad que se aplica sobre la piel con electrodos, sin agujas. Todavía no la ofrecemos; cuando la incorporemos, lo anunciaremos en esta página."),
        ("¿Ofrecéis estimulación transcraneal?", "Todavía no. Si la incorporamos, se aplicará solo cuando haya una indicación respaldada por la evidencia y en coordinación con tu médico."),
        ("¿A partir de qué edad tiene sentido cuidarse?", "Los factores de riesgo actúan a lo largo de toda la vida, y la mediana edad es una etapa clave para la prevención."),
    ],
    "related": ["prevencion-longevidad", "sueno-insomnio", "estres-ansiedad", "curso-mindfulness-mbsr-barcelona"],
    "cta": {"h2": "Cuida tu salud cognitiva con un plan claro", "p": "Escríbenos y te explicamos cómo es la consulta."},
})

PAGES.append({
    "slug": "osteopatia-sarria-sant-gervasi", "group": "servicio", "wave": 1,
    "nav": "Osteopatía",
    "card": "Osteopatía estructural, visceral y craneal con valoración individual.",
    "title": "Osteopatía en Sarrià–Sant Gervasi, Barcelona · Estructural, visceral y craneal | WA LAM",
    "desc": "Osteópata en Sarrià–Sant Gervasi (Barcelona). Osteopatía estructural, visceral y craneal para dolor, tensión, movilidad y regulación. Reserva tu sesión en WA LAM.",
    "about": "Osteopatía",
    "eyebrow": "Servicio · Terapia manual",
    "h1": "Osteopatía en Sarrià–Sant Gervasi",
    "sub": "Osteopatía estructural, visceral, craneosacral y neurovisceral · Barcelona",
    "lead": "La osteopatía es una terapia manual que valora cómo se relacionan las articulaciones, los músculos, las fascias, las vísceras y el sistema nervioso. Su objetivo es mejorar la movilidad, la función y la capacidad de adaptación del cuerpo, siempre a partir de una valoración individual y sin promesas de curación.",
    "facts": ["Atiende: [[nombre, titulación]]", "Sesión de [[duración]] · [[precio]]", "Estructural, visceral y craneal",
              "Valoración en cada sesión", "Reserva por WhatsApp"],
    "wa": "Hola, me gustaría reservar una sesión de osteopatía.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Cuándo consultar?", "h2": "Motivos frecuentes de consulta",
         "qs": ["¿Tienes dolor de espalda, cuello o zona lumbar que se repite?",
                "¿Notas tensión en el diafragma, la mandíbula o la zona cervical en épocas de estrés?",
                "¿Sientes molestias abdominales o pélvicas asociadas a cicatrices o tensión?",
                "¿Tienes dolores de cabeza tensionales?",
                "¿Te has recuperado de una lesión, pero la zona sigue rígida?"]},
        {"type": "explain", "eyebrow": "Origen", "h2": "Qué es la osteopatía", "paras": ["La osteopatía fue fundada en 1874 por el médico estadounidense Andrew Taylor Still, que en 1892 abrió en Kirksville (Misuri) la primera escuela de osteopatía. Su principio central es la relación entre la estructura del cuerpo y su función: la movilidad de articulaciones, músculos, fascias y vísceras influye en el funcionamiento del organismo.", "Con el tiempo se desarrollaron tres grandes enfoques: el estructural, centrado en el sistema musculoesquelético; el visceral, sistematizado por Jean-Pierre Barral; y el craneal, iniciado por William Garner Sutherland y desarrollado después por John Upledger."]},
        {"type": "cards", "eyebrow": "Modalidades", "h2": "Tres enfoques dentro de una misma sesión",
         "intro": "Según tu valoración, la sesión combina las técnicas que tu caso necesita. Cada enfoque tiene su propia página con más detalle.",
         "items": [{"k": "Estructural", "h": "Osteopatía estructural", "p": "Trabajo sobre articulaciones, músculos y fascias para mejorar la movilidad y aliviar la tensión. Es la base de la consulta para el dolor de espalda, cuello, hombro o cadera."},
                   {"k": "Visceral", "h": "[Osteopatía visceral](osteopatia-visceral-barcelona)", "p": "Técnicas suaves sobre el abdomen, el diafragma y la pelvis que valoran la movilidad de las vísceras y sus fascias. La usamos en dolor lumbar o pélvico relacionado con tensión abdominal, cicatrices o estrés."},
                   {"k": "Craneosacral", "h": "[Osteopatía craneosacral](osteopatia-craneosacral-barcelona)", "p": "Técnicas manuales muy suaves en cráneo, región cervical y sacro. La aplicamos como complemento, dentro de una valoración global."}]},
        {"type": "steps", "eyebrow": "La sesión", "h2": "Cómo es una sesión de osteopatía",
         "items": [("Entrevista", "Revisamos tu motivo de consulta, historia médica, pruebas y lo que esperas de la sesión."),
                   ("Valoración", "Exploramos movilidad, postura, respiración y las zonas relacionadas con tus síntomas."),
                   ("Tratamiento y pautas", "Aplicamos las técnicas adecuadas y te damos recomendaciones de movimiento o hábitos para casa.")],
         "note": "Ven con ropa cómoda. Si tienes informes o pruebas recientes, tráelos a la primera sesión."},
        {"type": "evidence", "h2": "La osteopatía, con rigor",
         "intro": "Somos clínicos. Por eso distinguimos entre lo que está demostrado, lo que es razonamiento clínico y lo que todavía no tiene respaldo suficiente.",
         "items": [("Metaanálisis (BMJ)", "La terapia manipulativa vertebral obtiene en el dolor lumbar crónico efectos **similares a los de los tratamientos recomendados** y mejora la función a corto plazo frente a intervenciones no recomendadas (47 ensayos aleatorizados)."),
                   ("Guía clínica (ACP)", "Para el dolor lumbar agudo y subagudo, la guía del American College of Physicians incluye la manipulación vertebral y el masaje entre las opciones no farmacológicas (evidencia de baja calidad), y para el dolor crónico prioriza el ejercicio. Por eso combinamos tratamiento manual y ejercicio."),
                   ("Revisión sistemática", "En osteopatía visceral, las técnicas diagnósticas no han demostrado fiabilidad y faltan ensayos de calidad sobre eficacia. La usamos como **razonamiento clínico complementario**, nunca como diagnóstico."),
                   ("Revisión sistemática", "En osteopatía craneal, la evidencia sobre fiabilidad diagnóstica y eficacia es débil e inconsistente. Si la aplicamos, es con técnicas suaves y explicándote sus límites.")],
         "refs": [R["rubinstein"], R["qaseem"], R["guillaud_v"], R["guillaud_c"]]},
        ficha("Ficha del servicio", "Osteopatía", "Valoración y tratamiento osteopático individual, con técnicas estructurales, viscerales y craneales según tu caso.", ROWS_SERVICIO),
    ],
    "faq": [
        ("¿Cuántas sesiones necesitaré?", "Depende de tu caso. En general revisamos la evolución tras dos o tres sesiones y decidimos juntos si tiene sentido continuar."),
        ("¿Duele?", "La mayoría de técnicas son suaves. Algunas pueden producir una molestia leve o sensación de cansancio durante uno o dos días."),
        ("¿Qué diferencia hay entre osteopatía y fisioterapia?", "Ambas son complementarias. La osteopatía se centra en la valoración y el tratamiento manual global; la fisioterapia pone más peso en el ejercicio, la recuperación funcional y la readaptación."),
        ("¿Puedo venir si estoy embarazada?", "Sí. Atendemos a mujeres embarazadas, adaptando el tratamiento a cada etapa. Más información en [osteopatía en el embarazo y el posparto](osteopatia-embarazo-posparto)."),
        ("¿Necesito prescripción médica?", "No es necesaria. Si durante la valoración detectamos algo que requiere estudio médico, te lo diremos."),
    ],
    "related": ["lumbalgia-cervicalgia-cronica", "dolor-articular-miofascial", "osteopatia-visceral-barcelona", "osteopatia-craneosacral-barcelona"],
    "cta": {"h2": "Reserva tu sesión de osteopatía", "p": "En Sarrià–Sant Gervasi, Barcelona. Si tienes dudas sobre si es para ti, escríbenos antes."},
})

PAGES.append({
    "slug": "osteopatia-visceral-barcelona", "group": "servicio", "wave": 1,
    "nav": "Osteopatía visceral",
    "card": "Osteopatía visceral: abdomen, diafragma, pelvis y cicatrices, con formación del Barral Institute.",
    "title": "Osteopatía visceral en Barcelona · Sarrià–Sant Gervasi | WA LAM",
    "desc": "Osteopatía visceral en Sarrià–Sant Gervasi, Barcelona: técnicas suaves sobre abdomen, diafragma, pelvis y cicatrices. Formación del Barral Institute.",
    "about": "Osteopatía visceral",
    "eyebrow": "Servicio · Osteopatía",
    "h1": "Osteopatía visceral en Barcelona",
    "sub": "Abdomen, diafragma, pelvis y cicatrices · Sarrià–Sant Gervasi",
    "lead": "La osteopatía visceral trabaja con técnicas manuales suaves sobre el abdomen, el diafragma, la pelvis y las fascias que rodean a las vísceras. Se basa en la idea de que la movilidad de los órganos y de sus tejidos de sostén influye en la tensión, la postura y algunas molestias digestivas, lumbares o pélvicas. En WA LAM la realiza Rosa María Rodríguez Valls, formada en manipulación visceral en el Barral Institute.",
    "facts": ["Atiende: Rosa María Rodríguez Valls, osteópata D.O.", "Formación en manipulación visceral (Barral Institute)", "Abdomen, diafragma, pelvis y cicatrices",
              "Sesión de [[duración]] · [[precio]]", "Parte de la [osteopatía](osteopatia-sarria-sant-gervasi) de WA LAM"],
    "wa": "Hola, me gustaría información sobre la osteopatía visceral.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Cuándo consultar?", "h2": "Motivos por los que nos consultan",
         "qs": ["¿Notas tensión abdominal o diafragmática que se acentúa con el estrés?",
                "¿Tienes dolor lumbar que parece relacionado con la digestión o la pelvis?",
                "¿Te han operado del abdomen y la cicatriz sigue tirante o adherida?",
                "¿Tienes digestiones pesadas o hinchazón sin una causa médica que lo explique?"],
         "close": "Si tienes dolor abdominal intenso, fiebre, sangrado o pérdida de peso sin causa, consulta primero con tu médico."},
        {"type": "explain", "eyebrow": "Qué es", "h2": "Una terapia manual sobre las vísceras y sus fascias",
         "paras": [
             "La osteopatía visceral fue desarrollada por el osteópata y fisioterapeuta francés Jean-Pierre Barral (Grenoble, 1944). Trabajando en el hospital de enfermedades pulmonares de Grenoble, se interesó por la movilidad de los órganos y, junto a Pierre Mercier, sistematizó un método de valoración y tratamiento manual que publicaron en 1983 en «Manipulations viscérales». Hoy se enseña en todo el mundo a través del Barral Institute.",
             "Las vísceras están unidas a la pared del cuerpo y entre sí por ligamentos, fascias y el diafragma, que se mueve con cada respiración. El método de Barral distingue la movilidad de los órganos, ligada a la respiración y al movimiento del cuerpo, y valora con la palpación las zonas de restricción para aplicar técnicas suaves de movilización y de inducción.",
             "Se diferencia de las [manipulaciones neuroviscerales](manipulaciones-neuroviscerales), que actúan sobre los nervios que conectan con los órganos. En la práctica, ambas pueden combinarse en una misma sesión de [osteopatía](osteopatia-sarria-sant-gervasi).",
         ]},
        {"type": "steps", "eyebrow": "La sesión", "h2": "Cómo es una sesión de osteopatía visceral",
         "items": [("Entrevista", "Historia digestiva, cirugías previas, dolor, ciclo menstrual, estrés y pruebas realizadas."),
                   ("Valoración", "Palpación del abdomen, el diafragma y la pelvis, y de su relación con la columna y la respiración."),
                   ("Tratamiento", "Técnicas manuales suaves y pautas de respiración o de hábitos para casa.")]},
        ficha("Ficha del servicio", "Osteopatía visceral", "Sesión individual de osteopatía con técnicas viscerales, que puede combinarse con técnicas estructurales o neuroviscerales.", ROWS_SERVICIO),
        {"type": "evidence", "h2": "Lo que ofrecemos y lo que se sabe",
         "items": [("Lo que ofrecemos", "Técnicas viscerales aplicadas con criterio clínico y como complemento, dentro de una valoración global."),
                   ("Revisión sistemática (2018)", "Una revisión sistemática concluyó que las pruebas diagnósticas de la osteopatía visceral no han demostrado ser fiables y que faltan ensayos de calidad sobre su eficacia."),
                   ("Nuestro criterio", "Por eso no la presentamos como tratamiento de enfermedades digestivas. La ofrecemos como terapia manual complementaria y te derivamos al médico si hay signos de alarma.")],
         "refs": [R["guillaud_v"]]},
    ],
    "faq": [("¿Duele la osteopatía visceral?", "No suele doler. Son técnicas suaves; algunas zonas pueden estar más sensibles."),
            ("¿Sirve para el colon irritable?", "Puede ayudar a algunas personas a sentir menos tensión abdominal, pero no hay evidencia sólida de que trate el colon irritable. Lo combinamos con la [salud digestiva](salud-digestiva-microbiota) y la alimentación.")],
    "related": ["osteopatia-sarria-sant-gervasi", "manipulaciones-neuroviscerales", "salud-digestiva-microbiota", "suelo-pelvico-dolor-pelvico"],
    "cta": {"h2": "Reserva tu sesión de osteopatía visceral", "p": "En Sarrià–Sant Gervasi. Si tienes dudas sobre si es para ti, escríbenos antes."},
})

PAGES.append({
    "slug": "osteopatia-craneosacral-barcelona", "group": "servicio", "wave": 1,
    "nav": "Osteopatía craneosacral",
    "card": "Terapia craneosacral: técnicas muy suaves en cráneo, columna y sacro, con formación del Upledger Institute.",
    "title": "Osteopatía craneosacral en Barcelona · Sarrià | WA LAM",
    "desc": "Osteopatía y terapia craneosacral en Sarrià–Sant Gervasi, Barcelona: técnicas muy suaves en cráneo, columna y sacro. Formación del Upledger Institute.",
    "about": "Terapia craneosacral",
    "eyebrow": "Servicio · Osteopatía",
    "h1": "Osteopatía craneosacral en Barcelona",
    "sub": "Terapia craneosacral · Sarrià–Sant Gervasi",
    "lead": "La terapia craneosacral utiliza contactos manuales muy suaves en el cráneo, la columna y el sacro. Muchas personas la buscan por cefaleas, tensión cervical o mandibular, dolor persistente o épocas de estrés, y la describen como una sesión de gran calma. En WA LAM la realiza Rosa María Rodríguez Valls, formada en terapia craneosacral en el Upledger Institute.",
    "facts": ["Atiende: Rosa María Rodríguez Valls, osteópata D.O.", "Formación en terapia craneosacral (Upledger Institute)", "Cráneo, columna, sacro y mandíbula",
              "Sesión de [[duración]] · [[precio]]", "Parte de la [osteopatía](osteopatia-sarria-sant-gervasi) de WA LAM"],
    "wa": "Hola, me gustaría información sobre la osteopatía craneosacral.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Cuándo consultar?", "h2": "Motivos por los que nos consultan",
         "qs": ["¿Tienes cefaleas tensionales o migrañas frecuentes?",
                "¿Aprietas la mandíbula o notas tensión cervical constante?",
                "¿Vives con dolor persistente y buscas una terapia manual muy suave?",
                "¿Atraviesas una etapa de estrés y te cuesta relajar el cuerpo?"]},
        {"type": "explain", "eyebrow": "Qué es", "h2": "Una terapia manual de contacto muy suave",
         "paras": [
             "La osteopatía craneal tiene su origen en William Garner Sutherland, que en la década de 1930 propuso que las suturas del cráneo conservan cierta movilidad durante toda la vida. En 1970, el médico osteópata John E. Upledger observó durante una intervención quirúrgica un movimiento rítmico de las membranas que rodean la médula espinal; entre 1975 y 1983 dirigió en la Universidad Estatal de Míchigan un equipo de investigación sobre este sistema y desarrolló la terapia craneosacral. En 1985 fundó el Upledger Institute, que la enseña en todo el mundo.",
             "Se aplica con la persona tumbada y vestida, mediante contactos muy ligeros en el cráneo, la nuca, la columna y el sacro.",
             "Su modelo tradicional habla de un «ritmo craneosacral»; la ciencia no ha confirmado que se pueda palpar de forma fiable. Por eso la explicamos desde lo que sí se puede observar: es una técnica suave y bien tolerada que muchas personas usan para reducir la tensión y el dolor.",
         ]},
        ficha("Ficha del servicio", "Osteopatía craneosacral", "Sesión individual de terapia craneosacral, sola o combinada con otras técnicas de osteopatía.", ROWS_SERVICIO),
        {"type": "evidence", "h2": "Lo que ofrecemos y lo que se sabe",
         "items": [("Metaanálisis (BMC Musculoskelet Disord)", "En 10 ensayos con 681 pacientes con dolor crónico (cuello, espalda, migraña, fibromialgia), la terapia craneosacral redujo algo el dolor y la discapacidad frente al tratamiento habitual y frente a una técnica simulada, sin efectos adversos graves. Los autores piden más ensayos de calidad."),
                   ("Revisión sistemática (2016)", "La fiabilidad del diagnóstico craneal (palpar el «ritmo») no está demostrada y la evidencia de eficacia es débil e inconsistente."),
                   ("Nuestro criterio", "La ofrecemos como terapia manual suave y complementaria, sin atribuirle mecanismos no demostrados.")],
         "refs": [R["haller"], R["guillaud_c"]]},
    ],
    "faq": [("¿Qué diferencia hay entre osteopatía craneal y terapia craneosacral?", "Tienen el mismo origen. La osteopatía craneal forma parte de la osteopatía; la terapia craneosacral es el método que desarrolló John Upledger a partir de ella."),
            ("¿Se puede hacer en niños o embarazadas?", "Sí. Atendemos a niños, con el consentimiento y la presencia de su madre, padre o tutor, y a embarazadas, adaptando la técnica a cada etapa de la gestación.")],
    "related": ["osteopatia-sarria-sant-gervasi", "estres-ansiedad", "dolor-persistente-cronico", "osteopatia-visceral-barcelona"],
    "cta": {"h2": "Reserva tu sesión craneosacral", "p": "En Sarrià–Sant Gervasi. Escríbenos si quieres saber si es adecuada para ti."},
})

PAGES.append({
    "slug": "manipulaciones-neuroviscerales", "group": "servicio", "wave": 2,
    "nav": "Manipulaciones neuroviscerales",
    "card": "Abordaje osteopático a través de los nervios que conectan con las vísceras del tórax, el abdomen y la pelvis.",
    "title": "Manipulaciones neuroviscerales en Barcelona | WA LAM",
    "desc": "Manipulaciones neuroviscerales en Sarrià–Sant Gervasi, Barcelona: osteopatía sobre los nervios del tórax, el abdomen y la pelvis. Formación Barral y Olivier Bazin.",
    "about": "Manipulaciones neuroviscerales",
    "eyebrow": "Servicio · Osteopatía",
    "h1": "Manipulaciones neuroviscerales",
    "sub": "Osteopatía a través del sistema nervioso visceral · Sarrià–Sant Gervasi",
    "lead": "Las manipulaciones neuroviscerales son técnicas osteopáticas que actúan sobre los nervios que conectan con los órganos del tórax, el abdomen y la pelvis: nervios espinales e intercostales, nervio vago, nervios frénicos y cadena simpática. Buscan influir en la función visceral a través del sistema nervioso. En WA LAM las aplica Rosa María Rodríguez Valls, formada en manipulación neural en el Barral Institute y organizadora en Barcelona de la formación de Olivier Bazin.",
    "facts": ["Atiende: Rosa María Rodríguez Valls, osteópata D.O.", "Formación en manipulación neural (Barral Institute)", "Tórax, abdomen y pelvis menor",
              "Sesión de [[duración]] · [[precio]]", "Para profesionales: [formación con Olivier Bazin](" + "https://www.walambcn.com/olivier-bazin-formaciones-en-osteopatia-neurovisceral-y-urogenital-walam-barcelona" + ")"],
    "wa": "Hola, me gustaría información sobre las manipulaciones neuroviscerales.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Cuándo consultar?", "h2": "Motivos por los que nos consultan",
         "qs": ["¿Tienes molestias digestivas o torácicas funcionales que empeoran con el estrés?",
                "¿Notas tensión en el diafragma o sensación de no poder respirar a fondo?",
                "¿Tienes dolor dorsal o intercostal que se relaciona con la digestión?",
                "¿Ya has probado la osteopatía visceral y buscas un abordaje complementario?"],
         "close": "Ante dolor torácico, dificultad para respirar o síntomas digestivos de alarma, acude primero a tu médico o a urgencias."},
        {"type": "explain", "eyebrow": "Qué es", "h2": "Actuar sobre las vísceras a través de los nervios",
         "paras": [
             "Las manipulaciones viscerales clásicas trabajan sobre los sistemas de fijación de los órganos: ligamentos, fascias y omento. Jean-Pierre Barral y Alain Croibier añadieron después las manipulaciones vasculares y neurales.",
             "El abordaje neurovisceral trabaja por dos vías: una **refleja**, sobre las ramas cutáneas de los nervios relacionados con cada víscera (vagos, frénicos, esplácnicos), los nervios intercostales y las zonas reflejas de la piel; y una **mecánica local**, que busca reducir la sensibilidad de los receptores y los arcos reflejos de dolor.",
             "Es un abordaje distinto de la [osteopatía visceral](osteopatia-visceral-barcelona), y ambos pueden combinarse.",
         ]},
        {"type": "cards", "eyebrow": "Qué se trabaja", "h2": "Estructuras que se abordan",
         "items": [{"k": "Nervios espinales", "h": "Ramas e intercostales", "p": "Nervios espinales, intercostales, intercostobraquiales y cluneales, y su conexión con las vísceras."},
                   {"k": "Parasimpático", "h": "Nervio vago", "p": "A lo largo de su recorrido: cuello, región del hiato, región gástrica y plexo hipogástrico inferior."},
                   {"k": "Simpático y frénico", "h": "Cadena simpática y nervios frénicos", "p": "Cadena laterovertebral, ganglios cervicales y nervios frénicos, relacionados con el diafragma."}]},
        {"type": "cards", "eyebrow": "Para profesionales", "h2": "Formación con Olivier Bazin en Barcelona",
         "items": [{"k": "Formación avanzada", "h": "Manipulaciones neuroviscerales del tórax y del abdomen", "p": "WA LAM organiza en Barcelona la formación de Olivier Bazin, D.O., referente internacional y coautor con Jean-Pierre Barral. [Ver la formación](" + "https://www.walambcn.com/olivier-bazin-formaciones-en-osteopatia-neurovisceral-y-urogenital-walam-barcelona" + ")."}]},
        ficha("Ficha del servicio", "Manipulaciones neuroviscerales", "Sesión individual de osteopatía con técnicas neuroviscerales, que puede combinarse con técnicas viscerales o estructurales.", ROWS_SERVICIO),
        {"type": "evidence", "h2": "Lo que ofrecemos y lo que se sabe",
         "items": [("Lo que ofrecemos", "Técnicas neuroviscerales aplicadas con criterio clínico, dentro de una valoración osteopática global."),
                   ("Lo que se sabe", "Es un modelo terapéutico basado en la anatomía del sistema nervioso visceral y en el razonamiento clínico osteopático. No hemos encontrado ensayos clínicos específicos sobre su eficacia, y la evidencia sobre la osteopatía visceral en general es limitada."),
                   ("Nuestro criterio", "La ofrecemos como terapia manual complementaria, sin prometer resultados sobre enfermedades digestivas o cardiorrespiratorias.")],
         "refs": [R["guillaud_v"]]},
    ],
    "faq": [("¿Es lo mismo que la osteopatía visceral?", "No. La visceral trabaja sobre los órganos y sus fascias; la neurovisceral, sobre los nervios que conectan con ellos. Suelen combinarse."),
            ("Soy profesional, ¿dónde puedo aprenderlo?", "En la [formación de Olivier Bazin](" + "https://www.walambcn.com/olivier-bazin-formaciones-en-osteopatia-neurovisceral-y-urogenital-walam-barcelona" + ") que organizamos en Barcelona.")],
    "related": ["osteopatia-visceral-barcelona", "osteopatia-sarria-sant-gervasi", "salud-digestiva-microbiota", "suelo-pelvico-dolor-pelvico"],
    "cta": {"h2": "Reserva tu sesión", "p": "Escríbenos si quieres saber si el abordaje neurovisceral es adecuado para tu caso."},
})

PAGES.append({
    "slug": "suelo-pelvico-dolor-pelvico", "group": "motivo", "wave": 2,
    "nav": "Suelo pélvico y dolor pélvico",
    "card": "Osteopatía urogenital de abordaje externo para el dolor pélvico, el suelo pélvico y la esfera urogenital.",
    "title": "Suelo pélvico y dolor pélvico en Barcelona · osteopatía | WA LAM",
    "desc": "Dolor pélvico y suelo pélvico en Sarrià–Sant Gervasi, Barcelona: osteopatía urogenital de abordaje externo, complementaria al seguimiento médico.",
    "about": "Dolor pélvico",
    "eyebrow": "Motivo de consulta",
    "h1": "Suelo pélvico y dolor pélvico",
    "sub": "Osteopatía urogenital · Sarrià–Sant Gervasi",
    "lead": "El dolor pélvico, las molestias urinarias, el dolor menstrual o el dolor en las relaciones afectan mucho a la calidad de vida y a menudo tardan en consultarse. En WA LAM los acompañamos con osteopatía urogenital de abordaje externo, siguiendo la línea de trabajo de Jean-Pierre Barral y Olivier Bazin, como complemento del seguimiento ginecológico o urológico.",
    "facts": ["Atiende: Rosa María Rodríguez Valls, osteópata D.O.", "Osteopatía urogenital: abordaje externo", "Coordinación con ginecología y urología",
              "Solo abordaje externo", "Para profesionales: [formación en salud pélvica y manipulaciones urogenitales con Olivier Bazin](" + "https://www.walambcn.com/formacion-avanzada-internacional-osteopatia-urogenital-salud-pelvica" + ")"],
    "wa": "Hola, me gustaría información sobre la osteopatía para el dolor pélvico y el suelo pélvico.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando el dolor está en la pelvis",
         "qs": ["¿Tienes reglas muy dolorosas o dolor pélvico que vuelve cada mes?",
                "¿Sientes dolor en las relaciones sexuales?",
                "¿Tienes pérdidas de orina al toser, reír o hacer ejercicio?",
                "¿Notas dolor en el coxis, en el periné o una sensación de quemazón que nadie te explica?",
                "¿Estás embarazada o en el posparto y notas molestias pélvicas?"],
         "close": "El dolor pélvico es real y merece una valoración. Si aparece sangrado anómalo, fiebre o dolor intenso y brusco, consulta antes con tu médico."},
        {"type": "explain", "eyebrow": "Nuestro enfoque", "h2": "La pelvis, vista en conjunto",
         "paras": [
             "En la pelvis conviven la vejiga, el útero, el recto, el suelo pélvico, ligamentos, fascias y nervios como el pudendo. Una tensión o una cicatriz en una de estas estructuras puede relacionarse con molestias en otra, y también con el dolor lumbar o el estrés.",
             "La osteopatía urogenital valora con la palpación la movilidad de estas estructuras y aplica técnicas manuales suaves sobre su entorno. La combinamos, si encaja, con [manipulaciones neuroviscerales](manipulaciones-neuroviscerales) y con el trabajo de respiración y de regulación del estrés.",
             "Si necesitas fisioterapia de suelo pélvico, te derivamos a una fisioterapeuta especializada.",
         ]},
        {"type": "cards", "eyebrow": "Motivos de consulta", "h2": "Qué acompañamos",
         "items": [{"k": "Dolor", "h": "Dolor menstrual y dolor pélvico", "p": "Dismenorrea, síndrome premenstrual y dolor pélvico persistente, también como complemento en la endometriosis."},
                   {"k": "Vejiga", "h": "Molestias urinarias", "p": "Incontinencia de esfuerzo y molestias vesicales, junto al seguimiento médico y la fisioterapia de suelo pélvico."},
                   {"k": "Nervios", "h": "Coxis, periné y neuralgias", "p": "Coccigodinia y dolor relacionado con los nervios pudendo, obturador o clúneos."},
                   {"k": "Etapas vitales", "h": "Embarazo, posparto y fertilidad", "p": "Adaptación de la pelvis durante el embarazo, recuperación en el posparto y [acompañamiento en fertilidad](acompanamiento-fertilidad)."}]},
        {"type": "cards", "eyebrow": "Para profesionales", "h2": "Formación urogenital con Olivier Bazin",
         "items": [{"k": "Formación completa · 2 seminarios", "h": "Manipulaciones urogenitales: abordaje externo (UGM + VMFPD)", "p": "WA LAM organiza en Barcelona la formación de Olivier Bazin, coautor de «Visceral Manipulations for Female Pelvic Disorders». [Ver la formación](" + "https://www.walambcn.com/formacion-avanzada-internacional-osteopatia-urogenital-salud-pelvica" + ")."}]},
        ficha("Ficha del servicio", "Osteopatía para el dolor pélvico", "Sesión individual de osteopatía urogenital (abordaje externo), con valoración global.", ROWS_SERVICIO),
        {"type": "cards", "eyebrow": "Salud pélvica", "h2": "Motivos de consulta en salud pélvica", "items": [{"h": "[Neuralgia del pudendo](neuralgia-pudendo)"}, {"h": "[Dolor menstrual y endometriosis](dolor-menstrual-endometriosis)"}, {"h": "[Dolor en las relaciones sexuales](dispareunia-dolor-relaciones)"}, {"h": "[Dolor de coxis](dolor-coxis-coccigodinia)"}, {"h": "[Cistitis de repetición y vejiga dolorosa](cistitis-repeticion-vejiga-dolorosa)"}, {"h": "[Embarazo y posparto](osteopatia-embarazo-posparto)"}, {"h": "[Incontinencia urinaria de esfuerzo](incontinencia-urinaria-esfuerzo)"}]},
        {"type": "evidence", "h2": "Lo que ofrecemos y lo que se sabe",
         "items": [("Lo que ofrecemos", "Osteopatía urogenital de abordaje externo como complemento del seguimiento ginecológico, urológico y de la fisioterapia de suelo pélvico."),
                   ("Lo que se sabe", "La fisioterapia de suelo pélvico es el tratamiento de primera línea con más evidencia para la incontinencia de esfuerzo. La evidencia sobre la osteopatía urogenital es limitada y procede sobre todo de la experiencia clínica."),
                   ("Nuestro criterio", "Por eso nuestro acompañamiento es complementario y no sustituye el tratamiento médico.")]},
    ],
    "faq": [("¿Hacéis tratamiento interno?", "No. Nuestro abordaje es siempre externo. Si necesitas un tratamiento intracavitario, te orientamos hacia una fisioterapeuta especializada en suelo pélvico."),
            ("¿Necesito un diagnóstico médico antes?", "Es recomendable, sobre todo si el dolor es reciente, intenso o se acompaña de sangrado o fiebre."),
            ("¿Atendéis a hombres?", "No atendemos el dolor pélvico masculino. Te orientaremos hacia un urólogo o una fisioterapeuta especializada.")],
    "related": ["manipulaciones-neuroviscerales", "acompanamiento-fertilidad", "salud-mujer-menopausia", "dolor-persistente-cronico"],
    "cta": {"h2": "Hablemos de tu dolor pélvico", "p": "Escríbenos con confianza. Te explicaremos cómo podemos acompañarte."},
})

# ---------------------------------------------------------------- SALUD PÉLVICA (UROGENITAL)
R["labat"] = _r("Labat JJ, Riant T, Robert R, Amarenco G, Lefaucheur JP, Rigaud J, 2008. «Diagnostic criteria for pudendal neuralgia by pudendal nerve entrapment (Nantes criteria)». Neurourology and Urodynamics.", "10.1002/nau.20505")
R["zondervan"] = _r("Zondervan KT, Becker CM, Missmer SA, 2020. «Endometriosis». New England Journal of Medicine.", "10.1056/NEJMra1810764")
R["ju_dysm"] = _r("Ju H, Jones M, Mishra G, 2014. «The Prevalence and Risk Factors of Dysmenorrhea». Epidemiologic Reviews.", "10.1093/epirev/mxt009")
R["mitchell"] = _r("Mitchell KR, Geary R, Graham CA, et al., 2017. «Painful sex (dyspareunia) in women: prevalence and associated factors in a British population probability survey». BJOG.", "10.1111/1471-0528.14518")
R["hanno"] = _r("Hanno PM, Erickson D, Moldwin R, Faraday MM, 2015. «Diagnosis and Treatment of Interstitial Cystitis/Bladder Pain Syndrome: AUA Guideline Amendment». Journal of Urology.", "10.1016/j.juro.2015.01.086")
R["franke"] = _r("Franke H, Franke JD, Belz S, Fryer G, 2017. «Osteopathic manipulative treatment for low back and pelvic girdle pain during and after pregnancy: A systematic review and meta-analysis». Journal of Bodywork and Movement Therapies.", "10.1016/j.jbmt.2017.05.014")
R["foye"] = _r("Foye PM, 2017. «Coccydynia: Tailbone Pain». Physical Medicine and Rehabilitation Clinics of North America.", "10.1016/j.pmr.2017.03.006")
R["dumoulin"] = _r("Dumoulin C, Cacciari LP, Hay-Smith EJC, 2018. «Pelvic floor muscle training versus no treatment, or inactive control treatments, for urinary incontinence in women». Cochrane Database of Systematic Reviews.", "10.1002/14651858.CD005654.pub4")

OB_URL = "https://www.walambcn.com/formacion-avanzada-internacional-osteopatia-urogenital-salud-pelvica"
def uro_pro():
    return {"type": "explain", "eyebrow": "Para profesionales", "h2": '¿Busca una formación avanzada en salud pélvica y manipulaciones urogenitales?',
            "paras": ['Formación especializada para **médicos y profesionales sanitarios** que quieren ir más allá en el tratamiento de las disfunciones pélvicas femeninas. La imparte **Olivier Bazin, D.O., MRO(F)**, fisioterapeuta y osteópata, **referente internacional** y coautor de «Visceral Manipulation for Female Pelvic Disorders» (Elsevier). WA LAM la organiza en Barcelona, por primera vez en España.', '[Ver programa, fechas e inscripción](https://www.walambcn.com/formacion-avanzada-internacional-osteopatia-urogenital-salud-pelvica) · [Más información sobre la formación](https://walam-bcn.github.io/formacion-olivier-bazin/).'],
            "list_title": 'La formación incluye:', "list": ['**Seminario 1 · UGM:** manipulación urogenital para los trastornos pélvicos, con abordaje externo', '**Seminario 2 · VMFPD:** manipulación visceral para los trastornos pélvicos femeninos', 'Dos módulos complementarios de una misma formación: 6 días intensivos presenciales en Barcelona', 'Traducción al castellano y certificado de asistencia', 'Próximas fechas: Urogenital I, 5–7 de mayo de 2028 · Urogenital II, 1–3 de septiembre de 2028']}
UG_NOTE = "En WA LAM el abordaje es siempre externo y se dirige a mujeres."

def uro_page(slug, nav, card, title, desc, about, h1, sub, lead, facts, wa, mirror_h2, qs, close, ex1_h2, ex1, ex2_h2, ex2, ev, refs, faq, related, cta_h2):
    blocks = [{"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": mirror_h2, "qs": qs}]
    if close: blocks[0]["close"] = close
    blocks += [{"type": "explain", "eyebrow": "Qué es", "h2": ex1_h2, "paras": ex1},
               {"type": "explain", "eyebrow": "Calidad de vida", "h2": ex2_h2, "paras": ex2 + [UG_NOTE]},
               {"type": "evidence", "h2": "Estudios de referencia", "items": ev, "refs": refs},
               uro_pro()]
    PAGES.append({"slug": slug, "group": "motivo", "wave": 2, "nav": nav, "card": card, "title": title, "desc": desc, "about": about,
                  "eyebrow": "Salud pélvica", "h1": h1, "sub": sub, "lead": lead, "facts": facts, "wa": wa, "blocks": blocks,
                  "faq": faq, "related": related, "cta": {"h2": cta_h2, "p": "Escríbenos por WhatsApp y te orientamos sobre tu caso."}})

uro_page("neuralgia-pudendo", "Neuralgia del pudendo", "Dolor en la zona perineal, genital o anal que empeora al estar sentada.",
  "Neuralgia del pudendo en Barcelona · Dolor perineal | WA LAM",
  "Neuralgia del pudendo y dolor neural pélvico en Sarrià–Sant Gervasi, Barcelona: dolor perineal que empeora al sentarse. Abordaje osteopático externo complementario.",
  "Neuralgia del pudendo", "Neuralgia del pudendo", "Dolor perineal y dolor neural pélvico · Sarrià–Sant Gervasi",
  "La neuralgia del pudendo es un dolor que afecta al territorio del nervio pudendo: periné, genitales, zona anal y uretra. Suele empeorar al estar sentada y aliviarse de pie o tumbada. Es una causa de dolor pélvico crónico poco conocida, que a menudo tarda años en identificarse.",
  ["Dolor perineal, genital o anal", "Empeora al estar sentada", "Nervios pudendo, obturador y clúneos", "Abordaje externo complementario", "Primera visita: 60 min · 90 €"],
  "Hola, me gustaría información sobre la neuralgia del pudendo.",
  "Cuando estar sentada se convierte en un problema",
  ["¿Tienes dolor, ardor o sensación de cuerpo extraño en el periné, la vulva o la zona anal?", "¿El dolor aumenta al estar sentada y mejora de pie o tumbada?", "¿Te han hecho pruebas que no explican tu dolor?", "¿El dolor apareció tras un parto, una cirugía pélvica, una caída o mucho tiempo en bicicleta?"],
  "Si aparecen alteraciones del control de la orina o de las heces, o pérdida de sensibilidad, consulta con tu médico de forma urgente.",
  "Un dolor de origen nervioso en la pelvis",
  ["El nervio pudendo recoge la sensibilidad del periné y de los genitales y participa en el control de los esfínteres. Su irritación o compresión a lo largo de su recorrido por la pelvis puede producir un dolor neuropático con quemazón, hormigueo o sensación de cuerpo extraño.",
   "Su diagnóstico es esencialmente clínico. Los criterios de Nantes describen sus rasgos principales: dolor en el territorio del nervio, que empeora al sentarse, que no despierta por la noche y sin pérdida objetiva de sensibilidad. Otros nervios de la pelvis, como el obturador o los clúneos, pueden producir cuadros parecidos."],
  "Cómo afecta a la vida diaria",
  ["Estar sentada en el trabajo, conducir o mantener relaciones sexuales puede resultar doloroso. El retraso diagnóstico, la incomprensión del entorno y el dolor persistente afectan con frecuencia al sueño y al estado de ánimo."],
  [("Criterios de Nantes (Neurourol Urodyn)", "Establecen cinco criterios esenciales para el diagnóstico clínico de la neuralgia del pudendo por atrapamiento: dolor en el territorio del nervio, que empeora al sentarse, sin despertares nocturnos por el dolor, sin pérdida sensitiva objetiva y con respuesta al bloqueo anestésico del nervio (Labat et al., 2008).")],
  [R["labat"]],
  [("¿Cómo sé si tengo neuralgia del pudendo?", "El diagnóstico lo realiza un médico especialista a partir de tus síntomas y la exploración. En WA LAM el acompañamiento es complementario."),
   ("¿Atendéis a hombres?", "No. Nuestro abordaje del dolor pélvico se dirige a mujeres.")],
  ["suelo-pelvico-dolor-pelvico", "dolor-neuropatico", "dispareunia-dolor-relaciones", "dolor-coxis-coccigodinia"], "Un dolor que merece ser escuchado")

uro_page("dolor-menstrual-endometriosis", "Dolor menstrual y endometriosis", "Dismenorrea, síndrome premenstrual y dolor pélvico asociado a la endometriosis.",
  "Dolor menstrual y endometriosis en Barcelona | WA LAM",
  "Dolor menstrual, síndrome premenstrual y dolor asociado a la endometriosis en Sarrià–Sant Gervasi, Barcelona. Acompañamiento complementario al seguimiento ginecológico.",
  "Dismenorrea y endometriosis", "Dolor menstrual y endometriosis", "Dismenorrea, síndrome premenstrual y dolor pélvico · Sarrià–Sant Gervasi",
  "El dolor menstrual no es algo que haya que aguantar. Cuando es intenso, limita la vida diaria o empeora con los años, puede estar relacionado con la endometriosis u otras causas que merecen valoración ginecológica. En WA LAM acompañamos el dolor como complemento de ese seguimiento.",
  ["Dismenorrea y síndrome premenstrual", "Dolor asociado a la endometriosis", "Complementario al seguimiento ginecológico", "Abordaje externo", "Primera visita: 60 min · 90 €"],
  "Hola, me gustaría información sobre el dolor menstrual o la endometriosis.",
  "Cuando la menstruación condiciona tu vida",
  ["¿Tu dolor menstrual te obliga a faltar al trabajo o a cancelar planes?", "¿El dolor ha ido empeorando con los años o aparece fuera de la regla?", "¿Tienes dolor en las relaciones, al orinar o al defecar durante la menstruación?", "¿Te han diagnosticado endometriosis y buscas un acompañamiento complementario?"],
  None,
  "Dismenorrea y endometriosis",
  ["La dismenorrea es el dolor asociado a la menstruación. Es muy frecuente: según una revisión de estudios internacionales, afecta a entre el 16 % y el 91 % de las mujeres en edad reproductiva, aunque el dolor intenso que limita la actividad diaria es menos habitual.",
   "La endometriosis es una enfermedad inflamatoria crónica en la que tejido similar al endometrio crece fuera del útero. Afecta aproximadamente al 10 % de las mujeres en edad reproductiva y puede causar dolor menstrual intenso, dolor en las relaciones, dolor al orinar, infertilidad y fatiga. Su diagnóstico y tratamiento corresponden a la ginecología."],
  "Cómo afecta a la calidad de vida",
  ["El dolor pélvico recurrente afecta al trabajo, a la vida social, a la sexualidad y al estado de ánimo, y el retraso en el diagnóstico de la endometriosis prolonga este impacto durante años."],
  [("Revisión (NEJM)", "La endometriosis afecta aproximadamente al 10 % de las mujeres en edad reproductiva; puede causar dolor intenso, dismenorrea, dispareunia, disuria, infertilidad y fatiga (Zondervan, Becker y Missmer, 2020)."),
   ("Revisión (Epidemiol Rev)", "La prevalencia de la dismenorrea oscila entre el 16 % y el 91 % según los estudios; el estrés y los antecedentes familiares aumentan el riesgo (Ju, Jones y Mishra, 2014).")],
  [R["zondervan"], R["ju_dysm"]],
  [("¿Tratáis la endometriosis?", "La endometriosis se diagnostica y trata en ginecología. En WA LAM acompañamos el dolor asociado de forma complementaria a ese seguimiento."),
   ("¿Puede ayudar si tengo dolor menstrual sin endometriosis?", "Sí. La dismenorrea primaria es muy frecuente y también puede acompañarse.")],
  ["suelo-pelvico-dolor-pelvico", "salud-mujer-menopausia", "acompanamiento-fertilidad", "dispareunia-dolor-relaciones"], "El dolor menstrual no es normal")

uro_page("dispareunia-dolor-relaciones", "Dolor en las relaciones sexuales", "Dispareunia superficial y profunda: dolor durante o después de las relaciones.",
  "Dispareunia · Dolor en las relaciones sexuales en Barcelona | WA LAM",
  "Dispareunia o dolor en las relaciones sexuales en Sarrià–Sant Gervasi, Barcelona: dolor superficial o profundo. Abordaje osteopático externo complementario.",
  "Dispareunia", "Dolor en las relaciones sexuales", "Dispareunia superficial y profunda · Sarrià–Sant Gervasi",
  "El dolor durante o después de las relaciones sexuales, o dispareunia, es más frecuente de lo que parece y a menudo no se consulta. Puede sentirse en la entrada de la vagina o en la profundidad de la pelvis, y sus causas son variadas: ginecológicas, musculares, nerviosas, hormonales o relacionadas con cicatrices.",
  ["Dispareunia superficial y profunda", "Tras el parto o en la menopausia", "Cicatrices y tensión pélvica", "Abordaje externo complementario", "Primera visita: 60 min · 90 €"],
  "Hola, me gustaría información sobre el dolor en las relaciones sexuales.",
  "Cuando las relaciones duelen",
  ["¿Sientes dolor al inicio de la penetración o en la profundidad de la pelvis?", "¿El dolor apareció tras un parto, una cirugía o en la menopausia?", "¿Notas tensión, ardor o molestias que se prolongan después de las relaciones?", "¿Has empezado a evitar las relaciones por miedo al dolor?"],
  None,
  "Un problema frecuente y poco consultado",
  ["En una encuesta poblacional británica con más de 6.600 mujeres sexualmente activas, el 7,5 % refería dolor en las relaciones durante al menos tres meses en el último año, y en una de cada cuatro era frecuente y causaba malestar.",
   "La dispareunia superficial suele relacionarse con la sequedad, la tensión de la musculatura del suelo pélvico o las cicatrices perineales; la profunda, con causas como la endometriosis o las adherencias pélvicas. Por eso es imprescindible una valoración ginecológica."],
  "Cómo afecta a la vida diaria",
  ["El dolor en las relaciones afecta a la sexualidad, a la pareja y a la autoestima, y se asocia con ansiedad ante las relaciones y pérdida de deseo, lo que puede mantener el círculo del dolor."],
  [("Encuesta poblacional (BJOG)", "El 7,5 % de las mujeres sexualmente activas refería dolor en las relaciones de al menos tres meses de duración; se asociaba a sequedad vaginal, ansiedad ante las relaciones y falta de disfrute (Mitchell et al., 2017).")],
  [R["mitchell"]],
  [("¿Es normal tener dolor en las relaciones después del parto?", "Es frecuente, pero no es algo que haya que aceptar. Conviene valorarlo, especialmente si se prolonga más allá de los primeros meses."),
   ("¿Hacéis tratamiento interno?", "No. Nuestro abordaje es siempre externo.")],
  ["suelo-pelvico-dolor-pelvico", "dolor-menstrual-endometriosis", "neuralgia-pudendo", "salud-mujer-menopausia"], "Recuperar una sexualidad sin dolor")

uro_page("dolor-coxis-coccigodinia", "Dolor de coxis (coccigodinia)", "Dolor en el coxis al sentarse, tras una caída o después del parto.",
  "Dolor de coxis (coccigodinia) en Barcelona | WA LAM",
  "Dolor de coxis o coccigodinia en Sarrià–Sant Gervasi, Barcelona: dolor al sentarse, tras una caída o después del parto. Abordaje osteopático externo complementario.",
  "Coccigodinia", "Dolor de coxis (coccigodinia)", "Dolor al sentarse, tras una caída o después del parto · Sarrià–Sant Gervasi",
  "La coccigodinia es el dolor localizado en el coxis, el último segmento de la columna. Suele empeorar al estar sentada, sobre todo al inclinarse hacia atrás, y al levantarse. Es más frecuente en mujeres y a menudo aparece tras una caída o un parto.",
  ["Dolor al sentarse y al levantarse", "Tras una caída o un parto", "Coccigodinia persistente", "Abordaje externo complementario", "Primera visita: 60 min · 90 €"],
  "Hola, me gustaría información sobre el dolor de coxis.",
  "Cuando sentarse duele",
  ["¿Te duele el coxis al sentarte, especialmente en superficies duras?", "¿El dolor aumenta al pasar de sentada a de pie?", "¿Empezó tras una caída de espaldas o después de un parto?", "¿Llevas meses con dolor a pesar del reposo y los cojines?"],
  "Si el dolor se acompaña de fiebre, pérdida de peso o alteraciones de la orina o las heces, consulta con tu médico.",
  "Qué es la coccigodinia",
  ["El coxis sirve de anclaje a ligamentos, a la musculatura del suelo pélvico y a estructuras nerviosas. Un traumatismo, el parto, la hipermovilidad o la rigidez de la articulación sacrococcígea, la tensión del suelo pélvico o la irritación de los nervios de la zona pueden mantener el dolor.",
   "La mayoría de los casos mejora en semanas o meses, pero en algunas personas el dolor persiste y se vuelve limitante. Las pruebas de imagen dinámicas pueden ayudar a identificar alteraciones de la movilidad del coxis."],
  "Cómo afecta a la vida diaria",
  ["El dolor de coxis dificulta trabajar sentada, conducir o viajar, y puede alterar la postura y el descanso. Cuando se cronifica, condiciona muchas actividades cotidianas."],
  [("Revisión (Phys Med Rehabil Clin N Am)", "La coccigodinia es más frecuente en mujeres y suele relacionarse con caídas o con el parto; la mayoría de los casos responde al tratamiento conservador, y la cirugía se reserva para casos excepcionales (Foye, 2017).")],
  [R["foye"]],
  [("¿Puede aparecer después del parto?", "Sí. El parto es una de las causas más frecuentes de dolor de coxis en la mujer."),
   ("¿Hacéis tratamiento interno del coxis?", "No. Nuestro abordaje es siempre externo.")],
  ["suelo-pelvico-dolor-pelvico", "neuralgia-pudendo", "osteopatia-embarazo-posparto", "lumbalgia-cervicalgia-cronica"], "Volver a sentarte sin dolor")

uro_page("cistitis-repeticion-vejiga-dolorosa", "Cistitis de repetición y vejiga dolorosa", "Cistitis recurrentes, cistalgia y síndrome de vejiga dolorosa.",
  "Cistitis de repetición y vejiga dolorosa en Barcelona | WA LAM",
  "Cistitis de repetición, cistalgia y síndrome de vejiga dolorosa en Sarrià–Sant Gervasi, Barcelona. Acompañamiento complementario al seguimiento urológico y ginecológico.",
  "Síndrome de vejiga dolorosa", "Cistitis de repetición y vejiga dolorosa", "Cistalgia y síndrome de vejiga dolorosa · Sarrià–Sant Gervasi",
  "Las cistitis de repetición y el síndrome de vejiga dolorosa comparten síntomas, pero no son lo mismo. En el síndrome de vejiga dolorosa, o cistitis intersticial, hay dolor o presión en la vejiga y necesidad frecuente de orinar sin una infección que lo explique. Ambos afectan de forma importante a la calidad de vida.",
  ["Cistitis de repetición", "Síndrome de vejiga dolorosa (cistitis intersticial)", "Complementario al seguimiento médico", "Abordaje externo", "Primera visita: 60 min · 90 €"],
  "Hola, me gustaría información sobre las cistitis de repetición o la vejiga dolorosa.",
  "Cuando la vejiga no te deja en paz",
  ["¿Tienes cistitis varias veces al año?", "¿Sientes dolor o presión en la vejiga que mejora al orinar?", "¿Necesitas orinar muy a menudo, también por la noche?", "¿Los cultivos salen negativos pero las molestias continúan?"],
  "Fiebre, dolor lumbar intenso o sangre en la orina requieren valoración médica inmediata.",
  "Dos cuadros distintos",
  ["Las cistitis de repetición son infecciones urinarias recurrentes y su diagnóstico y tratamiento corresponden al médico. El síndrome de vejiga dolorosa es un dolor crónico de la vejiga, con urgencia y frecuencia miccional, en ausencia de infección.",
   "Según la guía de la American Urological Association, el síndrome de vejiga dolorosa afecta a entre el 2,7 % y el 6,5 % de las mujeres adultas, y solo una pequeña parte de ellas ha recibido el diagnóstico. En su mantenimiento intervienen la sensibilización del sistema nervioso y la tensión de la musculatura del suelo pélvico."],
  "Cómo afecta a la vida diaria",
  ["La necesidad constante de orinar, el dolor y los despertares nocturnos afectan al descanso, al trabajo, a la vida social y a la sexualidad."],
  [("Guía clínica (J Urol)", "La guía de la American Urological Association sobre la cistitis intersticial o síndrome de vejiga dolorosa estima una prevalencia de entre el 2,7 % y el 6,5 % en mujeres adultas, y señala que solo el 9,7 % de las afectadas había recibido el diagnóstico (Hanno et al., 2015).")],
  [R["hanno"]],
  [("¿Sustituye al tratamiento antibiótico?", "No. Las infecciones urinarias deben tratarse según indique tu médico. Nuestro acompañamiento es complementario."),
   ("¿Atendéis a hombres?", "No. Nuestro abordaje de la salud pélvica se dirige a mujeres.")],
  ["suelo-pelvico-dolor-pelvico", "incontinencia-urinaria-esfuerzo", "salud-mujer-menopausia", "dolor-menstrual-endometriosis"], "Recuperar la tranquilidad")

uro_page("osteopatia-embarazo-posparto", "Osteopatía en el embarazo y el posparto", "Dolor lumbar y pélvico en el embarazo y recuperación tras el parto.",
  "Osteopatía en el embarazo y el posparto en Barcelona | WA LAM",
  "Osteopatía en el embarazo y el posparto en Sarrià–Sant Gervasi, Barcelona: dolor lumbar y pélvico durante la gestación y recuperación tras el parto.",
  "Embarazo y posparto", "Osteopatía en el embarazo y el posparto", "Dolor lumbar y pélvico y recuperación tras el parto · Sarrià–Sant Gervasi",
  "Durante el embarazo, el cuerpo se adapta al crecimiento del útero: cambian la postura, la respiración, la posición de las vísceras y la carga sobre la columna y la pelvis. Estos cambios pueden producir dolor lumbar y pélvico, y el posparto plantea su propia recuperación.",
  ["Desde el inicio del embarazo", "Dolor lumbar y de cintura pélvica", "Recuperación en el posparto", "Abordaje adaptado a cada etapa", "Primera visita: 60 min · 90 €"],
  "Hola, estoy embarazada (o en el posparto) y me gustaría información sobre la osteopatía.",
  "Cuando el embarazo o el posparto duelen",
  ["¿Tienes dolor lumbar o en la pelvis durante el embarazo?", "¿Te duele el pubis o la zona sacra al caminar o al darte la vuelta en la cama?", "¿Notas tensión, pesadez o dificultad para respirar a medida que avanza el embarazo?", "¿Tras el parto sigues con dolor, molestias en la cicatriz o sensación de falta de sostén?"],
  "Ante sangrado, contracciones, pérdida de líquido o dolor intenso, acude a tu matrona, a tu ginecóloga o a urgencias.",
  "Un cuerpo que se adapta",
  ["El dolor lumbar y de cintura pélvica es muy habitual durante el embarazo. Los cambios hormonales aumentan la laxitud de los ligamentos y el útero modifica la postura y la mecánica de la pelvis, el diafragma y las vísceras abdominales.",
   "En el posparto, la recuperación del suelo pélvico, de la pared abdominal y de las cicatrices, junto a la falta de sueño y la carga del bebé, puede mantener el dolor durante meses."],
  "Cómo afecta a la vida diaria",
  ["El dolor en el embarazo y el posparto dificulta el descanso, la movilidad y el cuidado del bebé, y afecta al bienestar en una etapa especialmente exigente."],
  [("Revisión sistemática (J Bodyw Mov Ther)", "En el dolor lumbar durante y después del embarazo, la osteopatía mostró beneficios clínicamente relevantes en el dolor y la función, con evidencia de calidad todavía limitada que requiere ensayos más amplios (Franke et al., 2017).")],
  [R["franke"]],
  [("¿Desde cuándo puedo venir durante el embarazo?", "Atendemos desde el inicio del embarazo, adaptando el abordaje a cada etapa."),
   ("¿Y después del parto?", "Sí, también en el posparto, cuando tu matrona o ginecóloga lo considere adecuado.")],
  ["drenaje-linfatico-embarazo", "suelo-pelvico-dolor-pelvico", "dolor-coxis-coccigodinia", "acompanamiento-fertilidad"], "Cuidarte en el embarazo y el posparto")

uro_page("incontinencia-urinaria-esfuerzo", "Incontinencia urinaria de esfuerzo", "Pérdidas de orina al toser, reír, saltar o hacer deporte.",
  "Incontinencia urinaria de esfuerzo en Barcelona | WA LAM",
  "Incontinencia urinaria de esfuerzo en Sarrià–Sant Gervasi, Barcelona: pérdidas de orina al toser, reír o hacer deporte. Abordaje osteopático externo complementario.",
  "Incontinencia urinaria de esfuerzo", "Incontinencia urinaria de esfuerzo", "Pérdidas de orina al toser, reír o hacer deporte · Sarrià–Sant Gervasi",
  "La incontinencia urinaria de esfuerzo es la pérdida involuntaria de orina al toser, estornudar, reír, saltar o hacer un esfuerzo. Es muy frecuente en las mujeres, especialmente tras el parto y en la menopausia, y aunque a menudo se vive en silencio, no es una consecuencia inevitable de la edad.",
  ["Pérdidas al toser, reír o saltar", "Tras el parto y en la menopausia", "Sistema de soporte del suelo pélvico", "Abordaje externo complementario", "Primera visita: 60 min · 90 €"],
  "Hola, me gustaría información sobre la incontinencia urinaria de esfuerzo.",
  "Cuando un esfuerzo provoca pérdidas",
  ["¿Se te escapa la orina al toser, estornudar o reír?", "¿Has dejado de correr, saltar o hacer deporte por miedo a las pérdidas?", "¿Las pérdidas empezaron tras un parto o con la menopausia?", "¿Usas protector a diario?"],
  None,
  "Un problema del sistema de soporte",
  ["La continencia depende de un sistema de soporte formado por la musculatura del suelo pélvico, los ligamentos, las fascias y los huesos de la pelvis. El embarazo, el parto, los cambios hormonales de la menopausia, el estreñimiento crónico o los deportes de impacto pueden debilitarlo.",
   "El entrenamiento de la musculatura del suelo pélvico, realizado por una fisioterapeuta especializada, es el tratamiento de primera línea con más evidencia. En WA LAM lo complementamos con un abordaje osteopático externo de la pelvis y su entorno, y derivamos a fisioterapia de suelo pélvico."],
  "Cómo afecta a la vida diaria",
  ["Las pérdidas de orina afectan a la actividad física, a la vida social, a la sexualidad y a la autoestima, y llevan a muchas mujeres a abandonar el deporte."],
  [("Revisión Cochrane", "En mujeres con incontinencia de esfuerzo, el entrenamiento de la musculatura del suelo pélvico multiplicó por cinco la probabilidad de curación frente a no tratar y redujo los episodios de pérdida; se recomienda como tratamiento conservador de primera línea (Dumoulin, Cacciari y Hay-Smith, 2018).")],
  [R["dumoulin"]],
  [("¿Sustituye a la fisioterapia de suelo pélvico?", "No. El entrenamiento del suelo pélvico es el tratamiento de primera elección. Nuestro abordaje es complementario y, si lo necesitas, te derivamos a una fisioterapeuta especializada."),
   ("¿Hacéis tratamiento interno?", "No. Nuestro abordaje es siempre externo.")],
  ["suelo-pelvico-dolor-pelvico", "cistitis-repeticion-vejiga-dolorosa", "osteopatia-embarazo-posparto", "salud-mujer-menopausia"], "Recuperar la confianza")


PAGES.append({
    "slug": "perdida-de-peso-sarria-sant-gervasi", "group": "servicio", "wave": 1,
    "nav": "Pérdida de peso",
    "card": "Cambios alimentarios y acupuntura para perder peso de forma progresiva y sostenible.",
    "title": "Pérdida de peso en Sarrià–Sant Gervasi | WA LAM",
    "desc": "Pérdida de peso en Sarrià–Sant Gervasi, Barcelona: cambios alimentarios individualizados y acupuntura en WA LAM.",
    "about": "Pérdida de peso",
    "eyebrow": "Servicio · Pérdida de peso",
    "h1": "Pérdida de peso en Sarrià–Sant Gervasi",
    "sub": "Cambios alimentarios y acupuntura en WA LAM",
    "lead": "En la consulta de pérdida de peso de WA LAM incorporo la **acupuntura** junto a **cambios alimentarios** individualizados, progresivos y sostenibles: las dos herramientas forman parte del mismo plan desde la primera visita. Puedes leer más sobre la [acupuntura en WA LAM](acupuntura-medicina-tradicional-china). El objetivo no es una dieta temporal, sino un cambio de hábitos que puedas mantener.",
    "facts": ["**Cambios alimentarios** individualizados", "**Acupuntura** como complemento", "Profesional: [[nombre, titulación]]",
              "Primera visita: 90 €", "Sesión de acupuntura: 1 h · 50 €"],
    "wa": "Hola, me gustaría información sobre el programa de pérdida de peso con alimentación y acupuntura.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando perder peso se ha convertido en una lucha",
         "qs": ["¿Has hecho varias dietas, has perdido peso y lo has vuelto a recuperar?",
                "¿Comes más cuando estás cansada, estresada o duermes mal?",
                "¿Te cuesta saber qué comer sin seguir una dieta estricta?",
                "¿Quieres perder peso sin pasar hambre ni eliminar grupos de alimentos?"],
         "close": "El peso no depende solo de la fuerza de voluntad: influyen el sueño, el estrés, el entorno y los hábitos."},
        {"type": "explain", "eyebrow": "Nuestro enfoque", "h2": "Dos herramientas dentro de un mismo plan",
         "paras": [
             "**Cambios alimentarios.** Son la base del plan. Ajustamos la alimentación a tus horarios, tus gustos y tu ritmo de vida, con cambios progresivos que no exigen eliminar alimentos sin motivo.",
             "**Acupuntura.** La incorporamos como complemento de los cambios alimentarios, no como sustituto. La evidencia científica sobre la acupuntura para perder peso es todavía limitada y de calidad variable, y así te lo explicamos. Puedes conocer cómo trabajamos la acupuntura en su [página propia](acupuntura-medicina-tradicional-china).",
             "Antes de empezar revisamos tu historia clínica y tus analíticas si las tienes. Si detectamos algo que requiere valoración médica (por ejemplo, un problema endocrino o un trastorno de la conducta alimentaria), te derivaremos.",
         ]},
        {"type": "steps", "eyebrow": "El proceso", "h2": "Cómo es el programa",
         "items": [("Primera visita", "En la primera visita (90 €) revisamos tu historia, tus hábitos, tu alimentación y tus objetivos, y preparamos tu tratamiento personalizado."),
                   ("Plan alimentario y acupuntura", "Pautas alimentarias individualizadas y dos sesiones de acupuntura por semana."),
                   ("Seguimiento", "Control de peso semanal y ajuste de las pautas nutricionales. La duración del programa depende del objetivo: no es lo mismo perder 5 kilos que 25.")]},
        ficha("Ficha del servicio", "Pérdida de peso: alimentación y acupuntura", "Programa individual que combina cambios alimentarios y acupuntura.",
              [("Profesional", "[[Nombre y titulación]]"), ("Primera visita", "90 €"), ("Sesión de acupuntura", "1 h · 50 €")]),
    ],
    "faq": [
        ("¿Cuánto peso voy a perder?", "No podemos prometerte una cifra: depende de cada persona. Buscamos una pérdida progresiva que puedas mantener en el tiempo."),
        ("¿La acupuntura sirve para adelgazar por sí sola?", "No la planteamos así. En WA LAM la acupuntura acompaña a los cambios alimentarios, que son la base del programa. La evidencia sobre la acupuntura aislada para perder peso es limitada."),
        ("¿Tendré que hacer una dieta estricta?", "No. Trabajamos con cambios progresivos y adaptados a ti, sin eliminar grupos de alimentos sin una indicación clara."),
        ("¿Cómo es el seguimiento?", "Cada semana controlamos el peso y ajustamos las pautas nutricionales. Las sesiones de acupuntura son dos por semana, y la duración total depende de tus objetivos."),
    ],
    "related": ["acupuntura-medicina-tradicional-china", "dejar-de-fumar-acupuntura", "prevencion-longevidad"],
    "cta": {"h2": "Empieza tu plan de pérdida de peso", "p": "Escríbenos por WhatsApp y te explicamos cómo funciona el programa."},
})

R["xie"] = _r("Xie L, Kang H, Xu Q, et al., 2013. «Sleep Drives Metabolite Clearance from the Adult Brain». Science.", "10.1126/science.1241224")
R["miao"] = _r("Miao A, Luo T, Hsieh B, et al., 2024. «Brain clearance is reduced during sleep and anesthesia». Nature Neuroscience.", "10.1038/s41593-024-01638-y")
R["sabia"] = _r("Sabia S, Fayosse A, Dumurgier J, et al., 2021. «Association of sleep duration in middle and old age with incidence of dementia». Nature Communications.", "10.1038/s41467-021-22354-2")
R["hitscherich"] = _r("Hitscherich K, Smith K, Cuoco JA, et al., 2016. «The Glymphatic-Lymphatic Continuum: Opportunities for Osteopathic Manipulative Medicine». Journal of the American Osteopathic Association.", "10.7556/jaoa.2016.033")

PAGES.append({
    "slug": "sueno-insomnio", "group": "motivo", "wave": 1,
    "nav": "Sueño e insomnio",
    "card": "El sueño como pilar de la salud cerebral: insomnio, sueño no reparador y ritmos circadianos.",
    "title": "Insomnio y medicina del sueño en Sarrià–Sant Gervasi | WA LAM",
    "desc": "Insomnio, sueño no reparador y alteraciones del ritmo circadiano en Sarrià–Sant Gervasi, Barcelona. El sueño como pilar de la salud cerebral y la longevidad.",
    "about": "Insomnio",
    "eyebrow": "Sueño y neurolongevidad",
    "h1": "Sueño e insomnio",
    "sub": "Dormir bien es una inversión en tu cerebro · Sarrià–Sant Gervasi",
    "lead": "El sueño no es solo descanso: es uno de los procesos de mantenimiento más importantes del organismo. Durante la noche el cerebro consolida la memoria, regula las emociones y restablece el equilibrio de sistemas como el metabolismo y la inmunidad. En WA LAM abordamos el sueño como un pilar activo de la salud cerebral y de la [longevidad](prevencion-longevidad), no como un síntoma aislado.",
    "facts": ["Valoración del patrón de sueño con cuestionarios validados", "Ritmos circadianos, luz y horarios", "Regulación del sistema nervioso", "Primera visita: 60 min · 90 €", "Derivación a una unidad del sueño cuando procede"],
    "wa": "Hola, tengo problemas para dormir y me gustaría saber cómo podéis ayudarme.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando la noche se convierte en un problema",
         "qs": ["¿Tardas más de media hora en dormirte, aunque estés agotada?", "¿Te despiertas de madrugada y ya no consigues volver a dormir?",
                "¿Duermes siete u ocho horas y te levantas cansada?", "¿Tu mente se activa justo cuando apagas la luz?",
                "¿El dolor, los sofocos o el estrés interrumpen tu descanso?", "¿Tus horarios de sueño cambian mucho entre semana y el fin de semana?"],
         "close": "El insomnio no se resuelve intentando dormir más, sino comprendiendo qué mantiene al sistema nervioso en alerta."},
        {"type": "explain", "eyebrow": "Neurociencia del sueño", "h2": "Lo que ocurre en tu cerebro mientras duermes",
         "paras": ["**Memoria y regulación emocional.** Las fases de sueño profundo y de sueño REM participan en la consolidación de lo aprendido durante el día y en el procesamiento emocional. El sueño fragmentado reduce estas fases, y sus efectos se acumulan.",
                   "**El sistema glinfático.** En 2013, un estudio en ratones publicado en Science observó que durante el sueño el espacio entre las células cerebrales aumentaba alrededor de un 60 % y se aceleraba la eliminación de beta-amiloide, una proteína asociada a la enfermedad de Alzheimer. En 2024, otro estudio en ratones, en Nature Neuroscience, obtuvo el resultado contrario. La investigación sigue abierta y todavía no se ha confirmado en humanos.",
                   "**Sueño y salud cognitiva.** En un seguimiento de casi 8.000 personas durante 25 años, dormir seis horas o menos a los 50 y 60 años se asoció a un mayor riesgo de demencia que dormir siete horas. Es una asociación, no una relación causal demostrada, pero refuerza el sueño como objetivo preventivo.",
                   "**Ritmo circadiano.** El reloj biológico regula el sueño, la secreción hormonal, el metabolismo, la inflamación y la inmunidad. La luz artificial nocturna, las pantallas, los turnos o los horarios irregulares lo desincronizan."]},
        {"type": "cards", "eyebrow": "Qué abordamos", "h2": "Problemas de sueño que valoramos",
         "items": [{"k": "Insomnio", "h": "Insomnio crónico", "p": "Dificultad para conciliar o mantener el sueño al menos tres noches por semana durante tres meses."},
                   {"k": "Calidad", "h": "Sueño no reparador", "p": "Dormir suficientes horas y despertar sin energía: revisamos los factores que lo explican."},
                   {"k": "Ritmo", "h": "Alteraciones del ritmo circadiano", "p": "Jet lag social, trabajo por turnos o tendencia a acostarse y levantarse muy tarde."},
                   {"k": "Mujer", "h": "Sueño en la menopausia", "p": "Sofocos, despertares y cambios hormonales que alteran el descanso. Más en [salud de la mujer](salud-mujer-menopausia)."},
                   {"k": "Estrés", "h": "Sueño y estrés", "p": "Hiperactivación nocturna y pensamientos que impiden desconectar. Más en [estrés y ansiedad](estres-ansiedad)."},
                   {"k": "Derivación", "h": "Apnea y piernas inquietas", "p": "Si los sospechamos, te derivamos a una unidad del sueño para su diagnóstico."}]},
        {"type": "cards", "eyebrow": "Cómo te acompañamos", "h2": "Un plan para recuperar el descanso",
         "items": [{"k": "Valoración", "h": "Historia y diario de sueño", "p": "Horarios, hábitos, medicación, dolor y síntomas hormonales, con cuestionarios validados de calidad del sueño, somnolencia e insomnio."},
                   {"k": "Ritmos", "h": "Luz, horarios y alimentación", "p": "Exposición a la luz natural, regularidad de horarios, cena, cafeína y alcohol."},
                   {"k": "Sistema nervioso", "h": "Regulación", "p": "Técnicas manuales y prácticas de regulación para reducir la activación nocturna, con el apoyo del [curso MBSR](curso-mindfulness-mbsr-barcelona)."}]},
        {"type": "evidence", "h2": "Qué dice la evidencia",
         "items": [("Guía europea (2023)", "La Guía Europea del Insomnio recomienda la terapia cognitivo-conductual para el insomnio (TCC-I) como tratamiento de primera línea en adultos (Riemann et al., J Sleep Res, 2023)."),
                   ("Guía americana (ACP)", "El American College of Physicians recomienda la TCC-I como tratamiento inicial del insomnio crónico y reserva los fármacos para cuando no es suficiente (Qaseem et al., Ann Intern Med, 2016)."),
                   ("Sistema glinfático (Science)", "En ratones, el sueño se asoció a un aumento del 60 % del espacio intersticial cerebral y a una eliminación más rápida de beta-amiloide (Xie et al., Science, 2013)."),
                   ("Debate científico (Nat Neurosci)", "Un estudio de 2024, también en ratones, observó una eliminación cerebral menor durante el sueño, lo que mantiene abierto el debate (Miao et al., Nat Neurosci, 2024)."),
                   ("Cohorte (Nat Commun)", "Dormir seis horas o menos a los 50 y 60 años se asoció a un mayor riesgo de demencia en 7.959 personas seguidas durante 25 años (Sabia et al., Nat Commun, 2021)."),
                   ("Inflamación (Biol Psychiatry)", "Las alteraciones del sueño se asocian a concentraciones más altas de PCR e IL-6 (Irwin et al., Biol Psychiatry, 2016)."),
                   ("Osteopatía craneal", "La relación entre la osteopatía craneal y el sistema glinfático es una hipótesis propuesta en la literatura osteopática, sin ensayos en humanos que la confirmen (Hitscherich et al., J Am Osteopath Assoc, 2016). Por eso ofrecemos la [osteopatía craneosacral](osteopatia-craneosacral-barcelona) como complemento para la relajación, sin atribuirle ese efecto.")],
         "refs": [R["riemann"], R["qaseem_ins"], R["xie"], R["miao"], R["sabia"], R["irwin"], R["hitscherich"]]},
    ],
    "faq": [
        ("¿Cuándo se considera que tengo insomnio crónico?", "Cuando te cuesta dormirte o mantener el sueño al menos tres noches por semana durante tres meses, y eso afecta a tu día."),
        ("Duermo ocho horas y me levanto agotada. ¿Por qué?", "Puede deberse a un sueño fragmentado, a un ritmo circadiano desajustado, al estrés, a cambios hormonales o a un trastorno como la apnea. En la primera visita revisamos estos factores y, si es necesario, te derivamos a una unidad del sueño."),
        ("¿Dormir mal durante años aumenta el riesgo de alzhéimer?", "Los estudios observan una asociación entre dormir poco en la mediana edad y un mayor riesgo de demencia, pero no demuestran una relación causal. Cuidar el sueño es, en cualquier caso, una de las medidas preventivas más razonables."),
        ("¿Tengo que dejar las pastillas para dormir?", "No sin hablarlo con tu médico. Cualquier cambio en la medicación debe hacerse con su supervisión."),
        ("¿Ofrecéis terapia cognitivo-conductual para el insomnio?", "La TCC-I es el tratamiento de primera elección. Si necesitas un programa completo de TCC-I, te derivamos a un psicólogo especializado en sueño."),
        ("¿Cuándo debo ir a una unidad del sueño?", "Si roncas fuerte con pausas en la respiración, tienes mucha somnolencia durante el día o sientes necesidad de mover las piernas por la noche."),
    ],
    "related": ["neurolongevidad-salud-cognitiva", "estres-ansiedad", "osteopatia-craneosacral-barcelona", "salud-mujer-menopausia"],
    "cta": {"h2": "Tu cerebro se repara mientras duermes", "p": "Reserva tu primera visita o escríbenos por WhatsApp y te contamos cómo podemos ayudarte a recuperar el descanso."},
})

PAGES.append({
    "slug": "dejar-de-fumar-acupuntura", "group": "servicio", "wave": 2,
    "nav": "Dejar de fumar con acupuntura",
    "card": "Una consulta de acupuntura como apoyo en tu proceso para dejar el tabaco, sin promesas.",
    "title": "Acupuntura para dejar de fumar en Barcelona | WA LAM",
    "desc": "Acupuntura como apoyo para dejar de fumar en Sarrià–Sant Gervasi, Barcelona: cómo es la consulta, cómo reservar y qué dice la evidencia.",
    "about": "Deshabituación tabáquica",
    "eyebrow": "Servicio · Acupuntura",
    "h1": "Acupuntura como apoyo para dejar de fumar",
    "sub": "Consulta en Sarrià–Sant Gervasi, Barcelona",
    "lead": "Dejar de fumar es una de las decisiones con más impacto en tu salud. En WA LAM ofrecemos la [acupuntura](acupuntura-medicina-tradicional-china) como **apoyo** dentro de tu proceso, no como sustituto de los tratamientos con más eficacia demostrada. Te explicamos con claridad qué puedes esperar.",
    "facts": ["Profesional: [[nombre, titulación]]", "Sesión de [[duración]] · [[precio]]", "Entre 3 y 5 sesiones, habitualmente",
              "Compatible con el tratamiento de tu médico", "Reserva por WhatsApp"],
    "wa": "Hola, quiero dejar de fumar y me gustaría información sobre la consulta de acupuntura.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando has decidido dejarlo",
         "qs": ["¿Has decidido dejar de fumar y buscas apoyo durante las primeras semanas?",
                "¿Lo has intentado otras veces y te gustaría sumar recursos?",
                "¿Te preocupan la ansiedad o la irritabilidad de los primeros días?",
                "¿Quieres combinar la acupuntura con el tratamiento que te ha indicado tu médico?"]},
        {"type": "steps", "eyebrow": "La consulta", "h2": "Cómo es la consulta",
         "items": [("Valoración", "Hablamos de tu consumo, de tus intentos previos, de tu motivación y de tu salud general, y revisamos contraindicaciones."),
                   ("Sesiones de acupuntura", "Agujas finas y estériles de un solo uso, en reposo. Habitualmente son necesarias entre 3 y 5 sesiones."),
                   ("Plan de apoyo", "Pautas para los momentos de más deseo de fumar y recomendación de consultar con tu médico sobre los tratamientos farmacológicos disponibles.")],
         "note": "Para reservar, escríbenos por WhatsApp y te proponemos día y hora. El pago se realiza mediante Bizum."},
        {"type": "evidence", "h2": "Qué dice la evidencia, sin promesas",
         "intro": "No te prometemos que la acupuntura te haga dejar de fumar. Esto es lo que dicen las revisiones Cochrane.",
         "items": [("Revisión Cochrane (2014)", "La acupuntura muestra un posible efecto a corto plazo frente a la acupuntura simulada, pero **no hay evidencia consistente de un beneficio mantenido** a los seis meses o más. Fue menos eficaz que la terapia sustitutiva de nicotina. Los autores la consideran segura si se aplica correctamente."),
                   ("Revisión Cochrane (2023)", "Los tratamientos con más eficacia demostrada para dejar de fumar son farmacológicos, como la vareniclina, la citisina o la combinación de terapias sustitutivas de nicotina. Los prescribe tu médico o tu centro de salud."),
                   ("Nuestro criterio", "Por eso planteamos la acupuntura como un apoyo que puede combinarse con esos tratamientos, y te animamos a hablar con tu médico de cabecera.")],
         "refs": [R["white_smoke"], R["lindson"]]},
        ficha("Ficha del servicio", "Acupuntura como apoyo para dejar de fumar", "Consulta individual de acupuntura como apoyo en el proceso de deshabituación tabáquica.",
              [("Profesional", "[[Nombre y titulación]]"), ("Duración", "[[min]]"), ("Precio", "[[€]]")]),
    ],
    "faq": [
        ("¿Cuántas sesiones necesitaré?", "Generalmente entre 3 y 5 sesiones. Lo valoramos según tu caso."),
        ("¿La acupuntura sustituye a los parches o a la medicación?", "No. Los tratamientos con más eficacia demostrada son farmacológicos y los prescribe tu médico. La acupuntura puede ser un apoyo complementario."),
        ("¿Es seguro?", "Realizada por un profesional formado y con agujas estériles de un solo uso, es una técnica segura. Avísanos si tomas anticoagulantes o estás embarazada."),
    ],
    "related": ["acupuntura-medicina-tradicional-china", "perdida-de-peso-sarria-sant-gervasi", "estres-ansiedad"],
    "cta": {"h2": "Da el paso con apoyo", "p": "Reserva tu consulta o escríbenos por WhatsApp si tienes dudas."},
})

PAGES.append({
    "slug": "acupuntura-medicina-tradicional-china", "group": "servicio", "wave": 2,
    "nav": "Acupuntura y medicina tradicional china",
    "card": "Consulta de acupuntura y MTC con valoración individual.",
    "title": "Acupuntura y medicina tradicional china en Barcelona · Sarrià–Sant Gervasi | WA LAM",
    "desc": "Consulta de acupuntura y medicina tradicional china en Sarrià–Sant Gervasi, Barcelona. Valoración individual, quién la realiza y qué puedes esperar.",
    "about": "Acupuntura",
    "eyebrow": "Servicio · Medicina tradicional china",
    "h1": "Acupuntura y medicina tradicional china",
    "sub": "Consulta individual en Sarrià–Sant Gervasi",
    "lead": "La acupuntura es una de las terapias complementarias más estudiadas en ensayos clínicos, especialmente en dolor crónico y cefalea. En WA LAM la aplicamos con criterio clínico: indicamos la acupuntura cuando la evidencia la respalda, te explicamos qué resultados son realistas y la combinamos con ejercicio y otros tratamientos.",
    "facts": ["Acupuntor/a: [[nombre, formación]]", "Sesión de [[duración]] · [[precio]]", "Agujas estériles de un solo uso",
              "Indicación basada en ensayos clínicos", "Dolor crónico, cefalea y migraña"],
    "wa": "Hola, me gustaría información sobre la consulta de acupuntura.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Cuándo consultar?", "h2": "Motivos por los que nos consultan",
         "qs": ["¿Tienes dolor lumbar, cervical o de rodilla persistente?",
                "¿Sufres cefaleas tensionales o migrañas frecuentes?",
                "¿Tienes artrosis y buscas una opción complementaria a tu tratamiento?",
                "¿Tienes dolor de hombro de larga evolución?"]},
        {"type": "steps", "eyebrow": "La sesión", "h2": "Cómo es una consulta de acupuntura",
         "items": [("Valoración", "Historia clínica, revisión de pruebas y exploración. Descartamos contraindicaciones (anticoagulación, embarazo, marcapasos si se usa electroestimulación)."),
                   ("Tratamiento", "Inserción de agujas finas y estériles en puntos seleccionados, mientras permaneces en reposo."),
                   ("Pautas", "Recomendaciones complementarias y plan de sesiones según tu evolución.")]},
        {"type": "evidence", "h2": "Qué dice la evidencia",
         "items": [("Metaanálisis de datos individuales", "Con datos de 39 ensayos y 20.827 pacientes, la acupuntura fue superior tanto a no recibir acupuntura como a la acupuntura simulada en dolor musculoesquelético crónico, artrosis, cefalea crónica y dolor de hombro, y sus efectos se mantuvieron en el tiempo. La diferencia frente a la simulada es menor (tamaño del efecto de aproximadamente 0,2)."),
                   ("Guía clínica (ACP)", "La guía del American College of Physicians incluye la acupuntura entre los tratamientos iniciales recomendados para el dolor lumbar crónico."),
                   ("Ensayo clínico (JAMA)", "En fecundación in vitro, la acupuntura no mejoró la tasa de nacidos vivos frente a la acupuntura simulada (848 mujeres). No la ofrecemos con ese fin."),
                   ("Otras consultas", "Ofrecemos también acupuntura dentro de la consulta de [pérdida de peso](perdida-de-peso-sarria-sant-gervasi), como apoyo para [dejar de fumar](dejar-de-fumar-acupuntura) y para el [estrés y la ansiedad](estres-ansiedad), donde suele combinarse con el trabajo de regulación del sistema nervioso."),
                   ("Marco tradicional", "Los conceptos de la medicina tradicional china (como los meridianos) son un modelo histórico de interpretación, no estructuras anatómicas demostradas. Nuestra indicación clínica se apoya en los ensayos, no en ese modelo.")],
         "refs": [R["vickers"], R["qaseem"], R["smith"]]},
        ficha("Ficha del servicio", "Acupuntura", "Consulta individual de acupuntura y medicina tradicional china.", ROWS_SERVICIO),
    ],
    "faq": [
        ("¿Duele la acupuntura?", "Las agujas son muy finas. Lo habitual es notar un pinchazo leve o una sensación de pesadez u hormigueo en la zona."),
        ("¿Es segura?", "Realizada por un profesional formado y con agujas estériles de un solo uso, los efectos adversos graves son muy poco frecuentes. Avísanos si tomas anticoagulantes o estás embarazada."),
        ("¿Usáis la acupuntura para perder peso?", "Sí: la incorporamos en la consulta de [pérdida de peso](perdida-de-peso-sarria-sant-gervasi), junto a cambios alimentarios."),
        ("¿Y para dejar de fumar?", "Sí, como apoyo, en una consulta específica. Te explicamos qué dice la evidencia en la página de [acupuntura para dejar de fumar](dejar-de-fumar-acupuntura)."),
        ("¿Quiero aprender MTC, dónde miro?", "La formación en medicina tradicional china tiene su propia página en la Healthy Lifestyle Academy."),
    ],
    "related": ["cefaleas-migrana", "lumbalgia-cervicalgia-cronica", "perdida-de-peso-sarria-sant-gervasi", "dejar-de-fumar-acupuntura"],
    "cta": {"h2": "Reserva tu consulta de acupuntura", "p": "Si tienes dudas sobre si es adecuada para tu caso, escríbenos antes de reservar."},
})

PAGES.append({
    "slug": "pni-pnie-barcelona", "group": "servicio", "wave": 2,
    "nav": "PNIE",
    "card": "Psiconeuroinmunoendocrinología (endocrinología): estrés, sueño, digestión, inflamación y hábitos en una misma consulta.",
    "title": "PNIE en Barcelona · Psiconeuroinmunoendocrinología | WA LAM",
    "desc": "Consulta de PNIE (psiconeuroinmunoendocrinología) en Sarrià–Sant Gervasi, Barcelona: estrés, inflamación, digestión, sueño y hábitos con un enfoque integrativo.",
    "about": "Psiconeuroinmunoendocrinología",
    "eyebrow": "Servicio · Consulta integrativa",
    "h1": "PNIE en Barcelona",
    "sub": "Psiconeuroinmunoendocrinología · Sarrià–Sant Gervasi",
    "lead": "La PNIE estudia cómo se comunican el sistema nervioso, el sistema inmune y el sistema endocrino, y cómo influyen en ellos el estrés, el sueño, la alimentación y las emociones. La PNIE añade de forma explícita la dimensión hormonal. En consulta usamos ese marco para entender tu caso de forma global.",
    "facts": ["Realiza la consulta: [[nombre, titulación]]", "Primera consulta de [[duración]] · [[precio]]", "Revisión de analíticas y hábitos",
              "Plan por fases y realista", "Coordinación con tu médico"],
    "wa": "Hola, me gustaría información sobre la consulta de PNIE.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Cuándo consultar?", "h2": "Motivos por los que nos consultan",
         "qs": ["¿Sientes cansancio persistente aunque tus analíticas «salgan bien»?",
                "¿Tienes molestias digestivas que empeoran con el estrés?",
                "¿Notas que el sueño, el ánimo y la digestión van de la mano?",
                "¿Quieres cambiar hábitos, pero necesitas un plan ordenado y personalizado?"]},
        {"type": "explain", "eyebrow": "Qué es la PNIE", "h2": "Un marco para entender cómo se comunican los sistemas del cuerpo",
         "paras": [
             "La psiconeuroinmunoendocrinología es un campo de investigación sólido. Un metaanálisis de 30 años de estudios publicado en *Psychological Bulletin* mostró que el estrés crónico se asocia a la supresión de la respuesta inmune, y otro metaanálisis de 72 estudios publicado en *Biological Psychiatry* asoció las alteraciones del sueño a niveles más altos de PCR e IL-6, dos marcadores de inflamación. La **PNIE clínica** aplica ese conocimiento para orientar cambios en el estilo de vida.",
             "Es importante distinguir: la base científica de las conexiones entre sistemas es firme, pero no todas las intervenciones que se ofrecen bajo la etiqueta «PNIE» tienen el mismo respaldo. En WA LAM priorizamos lo que tiene evidencia y te explicamos el porqué de cada recomendación.",
         ]},
        {"type": "steps", "eyebrow": "La consulta", "h2": "Cómo es la consulta de PNIE",
         "items": [("Historia clínica amplia", "Síntomas, analíticas, digestión, sueño, estrés, ciclo hormonal, medicación y hábitos."),
                   ("Interpretación", "Te explicamos qué factores pueden estar relacionados y cuáles priorizar."),
                   ("Plan y revisiones", "Cambios progresivos en alimentación, descanso, movimiento y regulación del estrés, con seguimiento.")]},
        {"type": "evidence", "h2": "Referencias científicas",
         "items": [("Metaanálisis", "Estrés crónico y supresión de la respuesta inmune: casi 300 estudios en 30 años de investigación."),
                   ("Metaanálisis", "Alteraciones del sueño y aumento de PCR e IL-6, en 72 estudios con más de 50.000 participantes."),
                   ("Revisión", "El eje microbiota-intestino-cerebro: vías de comunicación conocidas y límites actuales de la evidencia en humanos.")],
         "refs": [R["segerstrom"], R["irwin"], R["cryan"]]},
        ficha("Ficha del servicio", "Consulta de PNIE", "Consulta individual con revisión de hábitos y analíticas, valoración de la microbiota intestinal y pautas alimentarias personalizadas.", ROWS_SERVICIO),
    ],
    "faq": [
        ("¿Qué diferencia hay entre PNI y PNIE?", "Son prácticamente lo mismo. La «E» de PNIE subraya el papel del sistema endocrino (hormonal), que en la práctica ya está incluido en la PNI."),
        ("¿Necesito traer analíticas?", "Si tienes analíticas recientes, tráelas. Si hace falta alguna prueba, te lo indicaremos y te explicaremos para qué."),
        ("¿Es lo mismo que nutrición?", "La alimentación es una parte importante, pero la consulta de PNIE también aborda sueño, estrés, movimiento y ritmos circadianos."),
    ],
    "related": ["salud-digestiva-microbiota", "nutricion-salud-intestinal", "estres-ansiedad", "prevencion-longevidad"],
    "cta": {"h2": "Reserva tu consulta de PNIE", "p": "Una mirada global para entender cómo se relacionan tus síntomas."},
})

PAGES.append({
    "slug": "nutricion-salud-intestinal", "group": "servicio", "wave": 3,
    "nav": "Nutrición y salud intestinal",
    "card": "Consulta de nutrición centrada en la digestión, la microbiota y hábitos alimentarios sostenibles.",
    "title": "Nutrición y salud intestinal en Barcelona · Sarrià–Sant Gervasi | WA LAM",
    "desc": "Consulta de nutrición y salud intestinal en Barcelona: pautas individualizadas para la digestión y la microbiota, sin dietas restrictivas innecesarias.",
    "about": "Nutrición y salud intestinal",
    "eyebrow": "Servicio · Nutrición",
    "h1": "Nutrición y salud intestinal",
    "sub": "Alimentación para tu digestión · Sarrià–Sant Gervasi",
    "lead": "Una consulta de nutrición centrada en tu digestión: qué comes, cómo comes, cuándo comes y cómo influye el estrés. Proponemos una alimentación antiinflamatoria, de base mayoritariamente vegetal, de temporada y de proximidad, con pautas individualizadas, progresivas y sostenibles.",
    "facts": ["Primera visita: 75 min · 70 €", "Seguimiento: 40 min · 60 €", "Pautas personalizadas por escrito", "Clases de cocina saludable y mindful eating", "Atiende: Rosa María Rodríguez Valls, máster en PNIE"],
    "wa": "Hola, me gustaría información sobre la consulta de nutrición y salud intestinal.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Cuándo consultar?", "h2": "Motivos frecuentes",
         "qs": ["¿Te sientan mal muchos alimentos y ya no sabes qué comer?",
                "¿Tienes hinchazón, gases o ritmo intestinal irregular?",
                "¿Te han recomendado una dieta baja en FODMAP y necesitas que te guíen?",
                "¿Comes con prisa, con ansiedad o con culpa?"]},
        {"type": "cards", "eyebrow": "Cómo trabajamos", "h2": "Qué incluye la consulta",
         "items": [{"h": "Valoración alimentaria", "p": "Registro de tu alimentación, síntomas, horarios y contexto."},
                   {"h": "Pautas individualizadas", "p": "Cambios progresivos basados en evidencia, adaptados a tus gustos y tu ritmo de vida."},
                   {"h": "Relación con la comida", "p": "Alimentación consciente para comer con más calma y menos miedo."}]},
        {"type": "cards", "eyebrow": "También en nutrición", "h2": "Clases de cocina saludable y mindful eating", "items": [{"k": "90 min · 120 €", "h": "[Clases de cocina saludable](https://www.walambcn.com/academia-vida-saludable-barcelona/clases-cocina-saludable)", "p": "Talleres prácticos para aprender a preparar recetas sencillas de alimentación antiinflamatoria y aplicarlas en el día a día. Forman parte de la Healthy Lifestyle Academy."}, {"k": "60 min · 70 €", "h": "Mindful eating", "p": "Sesiones individuales para identificar los factores emocionales y conductuales que dificultan los cambios alimentarios y entrenar una relación más consciente y serena con la comida."}]},
        ficha("Ficha del servicio", "Nutrición y salud intestinal", "Consulta individual de nutrición y salud intestinal.",
              [("Profesional", "Rosa María Rodríguez Valls, máster en PNIE"), ("Primera visita", "75 min · 70 €"), ("Seguimiento", "40 min · 60 €"), ("Dónde", "Sarrià–Sant Gervasi, Barcelona")]),
    ],
    "faq": [
        ("¿Es una consulta diferente de la de PNIE?", "Sí. La consulta de nutrición se centra en la alimentación y la salud intestinal; la de [PNIE](pni-pnie-barcelona) aborda de forma más amplia la relación entre el sistema nervioso, las hormonas y la inmunidad. Ambas pueden combinarse."),
        ("¿Cuánto cuesta?", "La primera visita dura 75 minutos y cuesta 70 €; las visitas de seguimiento, 40 minutos y 60 €."),
        ("¿Me vais a quitar muchos alimentos?", "No por defecto. Si alguna restricción temporal es útil, se hace guiada y con un plan de reintroducción."),
    ],
    "related": ["programas-re-trace", "salud-digestiva-microbiota", "pni-pnie-barcelona", "perdida-de-peso-sarria-sant-gervasi"],
    "cta": {"h2": "Vuelve a comer con tranquilidad", "p": "Reserva tu consulta o escríbenos para resolver dudas."},
})

PAGES.append({
    "slug": "drenaje-linfatico-manual", "group": "servicio", "wave": 1,
    "nav": "Drenaje linfático manual",
    "card": "Sesiones de drenaje linfático manual: postoperatorio, embarazo y apoyo en el linfedema con autorización médica.",
    "title": "Drenaje linfático manual en Sarrià–Sant Gervasi | WA LAM",
    "desc": "Drenaje linfático manual en Sarrià–Sant Gervasi, Barcelona: técnica suave para la retención de líquidos, el postoperatorio y el embarazo. Reserva por WhatsApp.",
    "about": "Drenaje linfático manual",
    "eyebrow": "Servicio · Drenaje linfático",
    "h1": "Drenaje linfático manual en Sarrià–Sant Gervasi",
    "sub": "Una técnica suave para la retención de líquidos · Barcelona",
    "lead": "El drenaje linfático manual es una técnica lenta, suave y rítmica que acompaña el movimiento de la linfa. En WA LAM lo ofrecemos como sesión propia para la pesadez y la retención de líquidos, y con páginas específicas para la recuperación tras una [cirugía](drenaje-linfatico-postoperatorio) y para el [embarazo](drenaje-linfatico-embarazo).",
    "facts": ["Atiende: Rosa María Rodríguez Valls, formada en drenaje linfático manual", "Sesión de 1 hora · 70 €", "Bono de 10 + 1 sesiones: 700 €",
              "Postoperatorio, embarazo y linfedema, con página propia", "Pacientes oncológicos solo con autorización médica"],
    "cta2": ("Reservar drenaje", "https://www.walambcn.com/service-page/drenaje-linf%C3%A1tico-desintoxicaci%C3%B3n-y-bienestar"),
    "wa": "Hola, me gustaría información sobre el drenaje linfático manual.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando notas el cuerpo pesado o hinchado",
         "qs": ["¿Notas las piernas pesadas o hinchadas al final del día?",
                "¿Te han operado y necesitas reducir el edema?",
                "¿Estás embarazada y notas pesadez o hinchazón en piernas y tobillos?",
                "¿Tu médico te ha indicado drenaje linfático como parte de tu tratamiento?"]},
        {"type": "cards", "eyebrow": "Según tu situación", "h2": "Drenaje linfático en cada caso",
         "items": [{"k": "Postoperatorio", "h": "[Drenaje linfático postoperatorio](drenaje-linfatico-postoperatorio)", "p": "Tras cirugía estética (liposucción, párpados, cara, lifting) o traumatológica (rodilla, cadera…), siguiendo las indicaciones del equipo que te operó."},
                   {"k": "Embarazo", "h": "[Drenaje linfático en el embarazo](drenaje-linfatico-embarazo)", "p": "Una sesión adaptada para el confort ante la pesadez o la hinchazón gradual del embarazo."},
                   {"k": "Retención de líquidos", "h": "Sesión de drenaje", "p": "Para la pesadez y la retención de líquidos, después de descartar con tu médico causas que necesiten tratamiento, como problemas venosos, cardíacos o renales."}]},
        {"type": "explain", "eyebrow": "Linfedema", "h2": "Si tienes linfedema",
         "paras": [
             "El tratamiento de referencia del linfedema es la **terapia descongestiva compleja**: valoración y medición del miembro afectado, drenaje linfático manual, compresión con vendaje multicapa y después prendas a medida, ejercicio terapéutico, cuidado de la piel y revisiones periódicas. En Barcelona la ofrecen unidades especializadas de hospitales y centros de fisioterapia.",
             "En WA LAM colaboramos con médicos especialistas en linfedema: el especialista realiza la valoración, las mediciones y la indicación de la compresión, y WA LAM se encarga del tratamiento manual, antes o después de la cirugía. Sin autorización médica no tratamos a ningún paciente oncológico. Tenemos un [pack de drenaje linfático para linfedema](drenaje-linfatico-linfedema).",
             "El ejercicio forma parte del tratamiento del linfedema: te pautamos ejercicios de drenaje para hacer en casa entre sesiones.",
             "La acupuntura puede ofrecerse como complemento para el bienestar general, sin pinchar nunca el brazo o la pierna afectados. Los estudios no han demostrado que la acupuntura ni la reflexología reduzcan el volumen del linfedema, por lo que no las presentamos con ese fin.",
         ]},
        ficha("Ficha del servicio", "Drenaje linfático manual", "Sesión individual de drenaje linfático manual. Para el postoperatorio y el embarazo, consulta su página específica.",
              [("Profesional", "Rosa María Rodríguez Valls"), ("Duración", "1 hora"), ("Precio", "70 €"), ("Bono", "10 sesiones + 1 de regalo · 700 €")],
              btn=("Reservar drenaje", "https://www.walambcn.com/service-page/drenaje-linf%C3%A1tico-desintoxicaci%C3%B3n-y-bienestar")),
        {"type": "evidence", "h2": "Lo que ofrecemos y lo que se sabe",
         "items": [("Revisión Cochrane (2015)", "En el linfedema tras cáncer de mama, el drenaje linfático manual es seguro y, añadido al vendaje de compresión, aporta una reducción adicional del volumen, sobre todo en casos leves o moderados. Los ensayos son pequeños."),
                   ("Lo que se sabe", "Fuera del linfedema y del postoperatorio, la evidencia sobre el drenaje para la retención de líquidos es limitada. Lo ofrecemos por confort y bienestar, sin prometer resultados concretos.")],
         "refs": [R["ezzo"]]},
    ],
    "faq": [("¿Es lo mismo que la presoterapia?", "No. La presoterapia aplica compresión con un aparato neumático; el drenaje linfático manual es una técnica realizada con las manos."),
            ("¿Atendéis a pacientes con cáncer?", "Sí, pero siempre con la autorización de su médico."),
            ("¿Cuántas sesiones necesito?", "Depende del motivo. Si tienes linfedema diagnosticado, el número de sesiones se ajusta a lo que indique tu médico especialista."),
            ("¿Cuánto cuesta?", "La sesión de 1 hora cuesta 70 € y el bono de 10 sesiones más 1 de regalo, 700 €.")],
    "related": ["drenaje-linfatico-linfedema", "drenaje-linfatico-postoperatorio", "drenaje-linfatico-embarazo"],
    "cta": {"h2": "Reserva tu sesión de drenaje", "p": "Escríbenos si tienes dudas sobre si el drenaje es adecuado para ti."},
})

PAGES.append({
    "slug": "drenaje-linfatico-embarazo", "group": "servicio", "wave": 2,
    "nav": "Drenaje linfático en el embarazo",
    "card": "Una sesión adaptada al embarazo para el confort ante la pesadez o la hinchazón gradual.",
    "title": "Drenaje linfático en el embarazo en Barcelona | WA LAM",
    "desc": "Drenaje linfático manual durante el embarazo en Sarrià–Sant Gervasi, Barcelona: sesión adaptada para la pesadez y la hinchazón gradual de piernas y tobillos.",
    "about": "Drenaje linfático manual en el embarazo",
    "eyebrow": "Servicio · Embarazo",
    "h1": "Drenaje linfático manual durante el embarazo en Barcelona",
    "sub": "Una sesión adaptada para el confort · Sarrià–Sant Gervasi",
    "lead": "Durante el embarazo es frecuente notar las piernas, los tobillos o los pies más pesados e hinchados, sobre todo al final del día y en el último trimestre. En WA LAM ofrecemos una sesión de drenaje linfático manual adaptada al embarazo, en una postura cómoda y segura, para mejorar el confort ante esa pesadez o hinchazón gradual.",
    "facts": ["Atiende: Rosa María Rodríguez Valls, formada en drenaje linfático manual", "Sesión de 1 hora · 70 €", "Postura adaptada al embarazo",
              "Desde el inicio del embarazo y en el posparto", "Coordinación con tu matrona o ginecóloga si es necesario"],
    "wa": "Hola, estoy embarazada y me gustaría información sobre el drenaje linfático.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando las piernas pesan más cada día",
         "qs": ["¿Notas los tobillos y los pies hinchados al final del día?",
                "¿Sientes las piernas pesadas o cansadas?",
                "¿Te cuesta encontrar una postura cómoda para descansar?",
                "¿Buscas un momento de descanso y cuidado durante el embarazo?"],
         "close": "Antes de reservar: si la hinchazón aparece de forma brusca, afecta a la cara o las manos, o una pierna se hincha y duele, contacta antes con tu matrona, tu ginecóloga o urgencias."},
        {"type": "explain", "eyebrow": "La sesión", "h2": "Un drenaje adaptado a tu embarazo",
         "paras": [
             "Trabajamos con presiones muy suaves sobre piernas, pies y, según el caso, brazos, con la embarazada recostada de lado o semiincorporada, nunca boca abajo, y con pausas cuando lo necesite.",
             "Es una sesión de confort: no sustituye las recomendaciones de tu matrona, como caminar, elevar las piernas al descansar o usar medias de compresión si te las indican.",
             "Te atendemos desde el inicio del embarazo. Si tu embarazo es de riesgo, te pediremos antes la valoración de tu matrona o tu ginecóloga.",
         ]},
        ficha("Ficha del servicio", "Drenaje linfático en el embarazo", "Sesión individual de drenaje linfático manual adaptada al embarazo.",
              [("Profesional", "Rosa María Rodríguez Valls"), ("Duración", "1 hora"), ("Precio", "70 €"), ("Bono", "10 sesiones + 1 de regalo · 700 €"), ("Desde", "El inicio del embarazo")]),
    ],
    "faq": [("¿Desde qué semana puedo hacer drenaje?", "Desde el inicio del embarazo, adaptando la sesión a cada trimestre."),
            ("¿Necesito autorización médica?", "En un embarazo sin complicaciones, no. Si tienes hipertensión, preeclampsia, antecedentes de trombosis o un embarazo de riesgo, te pediremos antes la valoración de tu matrona o tu ginecóloga."),
            ("¿Y después del parto?", "Sí, también te acompañamos en el posparto, para la retención de líquidos y la recuperación tras el parto.")],
    "related": ["drenaje-linfatico-manual", "salud-mujer-menopausia", "acompanamiento-fertilidad"],
    "cta": {"h2": "Un momento de cuidado durante el embarazo", "p": "Escríbenos y te explicamos cómo es la sesión."},
})

PAGES.append({
    "slug": "drenaje-linfatico-postoperatorio", "group": "servicio", "wave": 1,
    "nav": "Drenaje linfático manual postoperatorio",
    "card": "Drenaje linfático manual después de una cirugía: cuándo empezar, qué cirugías atendemos y cómo reservar.",
    "title": "Drenaje linfático postoperatorio en Barcelona | WA LAM",
    "desc": "Drenaje linfático manual postoperatorio en Sarrià–Sant Gervasi (Barcelona): cirugías que atendemos, cuándo empezar y cómo reservar.",
    "about": "Drenaje linfático manual postoperatorio",
    "eyebrow": "Servicio · Postoperatorio",
    "h1": "Drenaje linfático manual postoperatorio",
    "sub": "Recuperación tras cirugía · Sarrià–Sant Gervasi",
    "lead": "Después de una cirugía es habitual que aparezcan inflamación, edema y sensación de tirantez. En WA LAM te acompañamos en esa fase con **drenaje linfático manual** adaptado a tu cirugía, siempre siguiendo las indicaciones de tu cirujano. Colaboramos con varios médicos estéticos y especialistas, y nos ocupamos de la parte manual de la recuperación.",
    "facts": ["Cirugía plástica y estética: liposucción, párpados, cara, lifting…", "Cirugía traumatológica: rodilla, cadera…", "Coordinado con las pautas de tu cirujano",
              "Embarazo y linfedema: ver sus páginas", "Sesión de 1 hora · 70 € · Bono de 10 + 1 sesiones: 700 €"],
    "wa": "Hola, me han operado (o me van a operar) y me gustaría información sobre el drenaje linfático postoperatorio.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando acabas de operarte",
         "qs": ["¿Te han operado hace poco y notas mucha inflamación o hinchazón?",
                "¿Tu cirujano te ha recomendado drenaje linfático y no sabes cuándo empezar?",
                "¿Sientes tirantez, endurecimiento o zonas con poca sensibilidad?",
                "¿Te preocupa la evolución de la cicatriz?"]},
        {"type": "cards", "eyebrow": "Qué atendemos", "h2": "Tipos de postoperatorio",
         "intro": "Atendemos la recuperación de cualquier cirugía que deje edema, tanto estética como traumatológica.",
         "items": [{"k": "Cirugía plástica y estética", "h": "Liposucción y cirugía corporal", "p": "Sobre todo tras una liposucción, cuando el edema es más intenso en las primeras semanas."},
                   {"k": "Cirugía facial", "h": "Párpados, cara y lifting", "p": "Tras una blefaroplastia, un lifting u otras intervenciones faciales, con técnicas muy suaves adaptadas a la zona."},
                   {"k": "Cirugía traumatológica", "h": "Rodilla, cadera y otras", "p": "Para controlar la inflamación tras una intervención de rodilla, cadera u otra articulación, como complemento a la rehabilitación."}]},
        {"type": "cards", "eyebrow": "Otros casos", "h2": "Drenaje en el embarazo y en el linfedema",
         "intro": "Cada situación tiene su propia página, porque la atención depende del caso y del equipo médico que te acompaña.",
         "items": [{"k": "Embarazo", "h": "[Drenaje linfático en el embarazo](drenaje-linfatico-embarazo)", "p": "Una sesión adaptada para la pesadez y la hinchazón gradual del embarazo."},
                   {"k": "Linfedema y oncología", "h": "[Drenaje linfático para linfedema](drenaje-linfatico-linfedema)", "p": "Siempre con la autorización de tu oncólogo o médico rehabilitador. Sin autorización médica no tratamos a ningún paciente oncológico."}]},
        {"type": "cards", "eyebrow": "Qué incluye", "h2": "Drenaje y otros cuidados postoperatorios",
         "intro": "El drenaje linfático manual es el servicio principal, y se completa con el cuidado de la cicatriz y la recuperación de la movilidad.",
         "items": [{"k": "Servicio principal", "h": "Drenaje linfático manual", "p": "Técnica suave y lenta para mejorar el confort y el edema en las semanas posteriores a la cirugía."},
                   {"k": "Cicatriz", "h": "Cuidado de la cicatriz", "p": "Trabajo manual de la cicatriz y los tejidos que la rodean, una vez cerrada y según las indicaciones del cirujano, para favorecer su flexibilidad y reducir adherencias."},
                   {"k": "Movilidad", "h": "Recuperación de la movilidad", "p": "Recuperación progresiva del movimiento de la zona intervenida y de las regiones relacionadas, adaptada a la fase de cicatrización."}]},
        {"type": "steps", "eyebrow": "Antes de empezar", "h2": "¿Es el momento adecuado?",
         "items": [("Consulta tu caso", "Escríbenos con el tipo de cirugía, la fecha y las indicaciones de tu cirujano."),
                   ("Valoramos el momento", "Te confirmamos si es buen momento para empezar o si conviene esperar."),
                   ("Plan de sesiones", "Proponemos frecuencia y número aproximado de sesiones según tu evolución.")],
         "note": "Si tienes fiebre, dolor intenso, enrojecimiento o calor en la zona, o hinchazón repentina en una pierna, contacta con tu cirujano o con urgencias antes de cualquier drenaje."},
        {"type": "evidence", "h2": "Lo que ofrecemos y lo que se sabe",
         "items": [("Lo que ofrecemos", "Drenaje linfático manual adaptado a tu cirugía y a las pautas de tu cirujano."),
                   ("Lo que se sabe", "Tras la cirugía estética, el drenaje linfático manual es una práctica habitual y bien tolerada, pero los estudios disponibles son pequeños y de calidad limitada. La evidencia más sólida procede del linfedema asociado al cáncer, donde se usa junto a la compresión y dentro de un tratamiento supervisado por el equipo oncológico."),
                   ("Nuestro criterio", "Por eso no prometemos resultados concretos: valoramos tu evolución sesión a sesión y te derivamos a tu cirujano ante cualquier signo de alarma.")]},
        ficha("Ficha del servicio", "Drenaje linfático manual postoperatorio", "Sesión individual de drenaje linfático manual adaptada a tu cirugía y fase de recuperación.",
              [("Profesional", "Rosa María Rodríguez Valls"), ("Duración", "1 hora"), ("Precio", "70 €"), ("Bono", "10 sesiones + 1 de regalo · 700 €")]),
    ],
    "faq": [
        ("¿Cuándo puedo empezar después de la operación?", "Depende de la cirugía y de lo que indique tu cirujano. Escríbenos con esa información y te orientamos antes de reservar."),
        ("¿Cuántas sesiones suelen hacer falta?", "Varía según la intervención, la evolución y las indicaciones de tu cirujano. Lo revisamos sesión a sesión. La sesión de 1 hora cuesta 70 € y el bono de 10 sesiones más 1 de regalo, 700 €."),
        ("¿Es lo mismo que un masaje?", "No. El drenaje linfático manual es una técnica específica, muy suave y lenta, distinta del masaje. Por eso tiene su propia página."),
        ("¿Tengo que llevar la faja?", "Sigue las indicaciones de tu cirujano sobre prendas de compresión. Normalmente la retiras durante la sesión y te la vuelves a poner al terminar."),
    ],
    "related": ["drenaje-linfatico-manual", "drenaje-linfatico-embarazo", "osteopatia-sarria-sant-gervasi"],
    "cta": {"h2": "Consúltanos antes de empezar", "p": "Cuéntanos tu cirugía y su fecha. Te diremos si es buen momento y cómo organizar las sesiones."},
})

PAGES.append({
    "slug": "drenaje-linfatico-linfedema", "group": "servicio", "wave": 1,
    "nav": "Drenaje linfático para linfedema",
    "card": "Pack de drenaje linfático manual para el linfedema, con ejercicios de drenaje, alimentación y acupuntura, en colaboración con médicos especialistas en linfedema.",
    "title": "Drenaje linfático para linfedema en Barcelona | WA LAM",
    "desc": "Pack de drenaje linfático manual para el linfedema en Sarrià–Sant Gervasi, Barcelona, en colaboración con médicos especialistas en linfedema.",
    "about": "Linfedema",
    "eyebrow": "Servicio · Linfedema",
    "h1": "Drenaje linfático para linfedema",
    "sub": "Pack para el linfedema en colaboración con médicos especialistas · Sarrià–Sant Gervasi",
    "lead": "El linfedema es una acumulación crónica de linfa que hincha un brazo, una pierna u otra zona. Puede tener varias causas, entre ellas genéticas, y es frecuente tras la cirugía o la radioterapia de un cáncer. Su tratamiento siempre se coordina con un médico especialista en linfedema. En WA LAM colaboramos con médicos especialistas y nos ocupamos de la parte manual, antes o después de la cirugía, con un pack que combina **drenaje linfático manual**, **ejercicios de drenaje**, **alimentación** y **acupuntura** como complemento.",
    "facts": ["**Drenaje linfático manual**: la base del pack", "**Ejercicios de drenaje** pautados para casa", "**Alimentación** y **acupuntura** como complemento",
              "En colaboración con médicos especialistas en linfedema", "Sesión de 1 hora · 70 € · Bono de 10 + 1 sesiones: 700 €"],
    "cta2": ("Reservar drenaje", "https://www.walambcn.com/service-page/drenaje-linf%C3%A1tico-desintoxicaci%C3%B3n-y-bienestar"),
    "wa": "Hola, tengo linfedema y me gustaría información sobre el pack de drenaje linfático.",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Te reconoces?", "h2": "Cuando la hinchazón no se va",
         "qs": ["¿Te operaron de un cáncer y notas el brazo o la pierna más hinchados o pesados?",
                "¿Sientes tirantez, pesadez o que la ropa o los anillos te aprietan más de un lado?",
                "¿Te han diagnosticado linfedema y tu médico te ha indicado drenaje linfático manual?",
                "¿Vas a operarte o te acaban de operar y necesitas la parte manual del tratamiento?"],
         "close": "Si aparece enrojecimiento, calor, fiebre o dolor en la zona, consulta con tu médico antes de cualquier tratamiento: puede ser una infección."},
        {"type": "explain", "eyebrow": "Cómo trabajamos", "h2": "Un tratamiento coordinado con tu médico especialista",
         "paras": [
             "El tratamiento del linfedema combina varias medidas: valoración y medición del miembro afectado, drenaje linfático manual, compresión con vendaje o prendas a medida, ejercicio, cuidado de la piel y revisiones. Por eso siempre se coordina con un médico especialista en linfedema.",
             "En WA LAM colaboramos con médicos especialistas en linfedema. El especialista realiza la valoración, las mediciones y la indicación de la compresión y, si procede, de la cirugía; WA LAM se encarga del drenaje linfático manual, antes o después de la intervención, y de la pauta de ejercicios de drenaje para realizar en casa.",
             "Si eres paciente oncológica, necesitamos la autorización de tu médico: sin autorización médica no tratamos a ningún paciente oncológico.",
         ]},
        {"type": "cards", "eyebrow": "El pack", "h2": "Qué incluye el pack para linfedema",
         "items": [{"k": "La base", "h": "Drenaje linfático manual", "p": "Técnica suave y rítmica que ayuda a movilizar la linfa, adaptada a la zona y a la fase del linfedema. Más información sobre el [drenaje linfático manual](drenaje-linfatico-manual)."},
                   {"k": "En casa", "h": "Ejercicios de drenaje", "p": "Te pautamos ejercicios sencillos que ayudan a drenar y que puedes hacer a diario entre sesiones."},
                   {"k": "Alimentación", "h": "Peso e inflamación", "p": "Revisamos tu alimentación para ayudarte a mantener un peso saludable, porque el exceso de peso empeora el linfedema."},
                   {"k": "Complemento", "h": "Acupuntura", "p": "Como apoyo al bienestar general, sin pinchar nunca el brazo o la pierna afectados. Más información sobre la [acupuntura en WA LAM](acupuntura-medicina-tradicional-china)."}]},
        {"type": "steps", "eyebrow": "El recorrido", "h2": "Cómo funciona el pack",
         "items": [("Valoración", "Revisamos tu historia, el informe y las indicaciones de tu médico especialista, el estado de la piel y la zona afectada."),
                   ("Sesiones", "Sesiones de drenaje linfático manual de 1 hora, con ejercicios de drenaje para casa, pautas de alimentación y, si encaja, acupuntura. El número de sesiones se ajusta a lo que indique tu médico especialista."),
                   ("Seguimiento", "Revisamos tu evolución y nos coordinamos con tu médico especialista para ajustar el plan.")],
         "note": "No empezamos el drenaje si hay infección activa, trombosis o una recidiva del cáncer sin control médico."},
        ficha("Ficha del servicio", "Pack de drenaje linfático para linfedema", "Drenaje linfático manual, ejercicios de drenaje, alimentación y acupuntura, en colaboración con tu médico especialista en linfedema.",
              [("Profesional", "Rosa María Rodríguez Valls"), ("Sesión", "1 hora · 70 €"), ("Bono", "10 sesiones + 1 de regalo · 700 €"), ("Requisito", "Coordinación con tu médico especialista; autorización médica en pacientes oncológicos")],
              btn=("Reservar drenaje", "https://www.walambcn.com/service-page/drenaje-linf%C3%A1tico-desintoxicaci%C3%B3n-y-bienestar")),
        {"type": "evidence", "h2": "Lo que ofrecemos y lo que se sabe",
         "items": [("Revisión Cochrane (2015)", "El drenaje linfático manual es seguro y, añadido al vendaje de compresión, aporta una reducción adicional del volumen del linfedema tras el cáncer de mama, sobre todo en casos leves o moderados. Los ensayos son pequeños."),
                   ("Consenso internacional", "La Sociedad Internacional de Linfología considera la terapia descongestiva compleja (drenaje, compresión, ejercicio y cuidado de la piel) el tratamiento conservador de referencia, y señala la obesidad como un factor que complica el linfedema."),
                   ("Metaanálisis (Integr Cancer Ther, 2019)", "La acupuntura fue segura en los ensayos revisados, pero no redujo de forma significativa el perímetro del brazo. Por eso la ofrecemos como complemento para el bienestar y no para reducir el volumen del linfedema.")],
         "refs": [R["ezzo"], R["chien"]]},
    ],
    "faq": [
        ("¿Sustituye al tratamiento de mi médico?", "No. El tratamiento se realiza en coordinación con tu médico especialista en linfedema: el especialista se encarga de la valoración, las mediciones y la indicación de la compresión, y WA LAM del drenaje linfático manual."),
        ("¿Se puede hacer acupuntura si tengo linfedema?", "Sí, como complemento, pero sin pinchar nunca el brazo o la pierna afectados."),
        ("¿Necesito autorización médica?", "Sí. Sin la autorización de tu médico no tratamos a ningún paciente oncológico, ni con drenaje, ni con reflexología, ni con masaje."),
        ("¿Cuánto cuesta?", "La sesión de 1 hora cuesta 70 € y el bono de 10 sesiones más 1 de regalo, 700 €."),
    ],
    "related": ["drenaje-linfatico-manual", "drenaje-linfatico-postoperatorio", "acupuntura-medicina-tradicional-china"],
    "cta": {"h2": "Hablemos de tu linfedema", "p": "Escríbenos y te explicamos cómo funciona el pack y cómo nos coordinamos con tu médico especialista."},
})

PAGES.append({
    "slug": "masajes-sarria-sant-gervasi", "group": "servicio", "wave": 2,
    "nav": "Masajes",
    "card": "Modalidades de masaje disponibles, duración y cómo reservar cada una.",
    "title": "Masajes en Sarrià–Sant Gervasi, Barcelona | WA LAM",
    "desc": "Masajes en Sarrià–Sant Gervasi (Barcelona): modalidades disponibles, duración, precio y reserva en WA LAM.",
    "about": "Masaje terapéutico",
    "eyebrow": "Servicio · Masaje",
    "h1": "Masajes en Sarrià–Sant Gervasi",
    "sub": "Un tiempo para tu cuerpo · Barcelona",
    "lead": "El masaje puede ayudar a aliviar la tensión muscular, mejorar la sensación de bienestar y favorecer el descanso. Elige la modalidad que mejor se adapta a lo que necesitas hoy.",
    "facts": ["Sesión de 1 hora · 70 €", "Masaje descontracturante o relajante",
              "Tarjetas regalo disponibles", "Reserva por WhatsApp"],
    "wa": "Hola, me gustaría reservar un masaje.",
    "blocks": [
        {"type": "cards", "eyebrow": "Modalidades", "h2": "Elige tu masaje",
         "intro": "Todas las sesiones duran una hora y cuestan 70 €.",
         "items": [{"k": "1 h · 70 €", "h": "Masaje descontracturante", "p": "Trabajo más profundo sobre zonas de tensión muscular de espalda, cuello y hombros."},
                   {"k": "1 h · 70 €", "h": "Masaje relajante", "p": "Ritmo lento y presión suave para favorecer la calma y el descanso."}]},
        {"type": "explain", "eyebrow": "Antes de reservar", "h2": "Cuándo no es un masaje lo que necesitas",
         "paras": ["Si tienes dolor persistente, una lesión reciente o acabas de operarte, te recomendamos empezar por una valoración de osteopatía o de drenaje linfático postoperatorio, para que el tratamiento sea el adecuado."]},
    ],
    "faq": [
        ("¿Tenéis tarjetas regalo?", "Sí. Escríbenos por WhatsApp y te preparamos una tarjeta regalo."),
    ],
    "related": ["drenaje-linfatico-postoperatorio", "reflexologia-sarria-sant-gervasi", "osteopatia-sarria-sant-gervasi"],
    "cta": {"h2": "Reserva tu masaje", "p": "Escríbenos por WhatsApp y te proponemos día y hora."},
})

PAGES.append({
    "slug": "reflexologia-sarria-sant-gervasi", "group": "servicio", "wave": 2,
    "nav": "Reflexología podal",
    "card": "Sesión independiente de reflexología podal: duración, precio y reserva.",
    "title": "Reflexología podal en Sarrià–Sant Gervasi, Barcelona | WA LAM",
    "desc": "Reflexología podal en Sarrià–Sant Gervasi (Barcelona): qué es, cómo es la sesión, duración, precio y reserva en WA LAM.",
    "about": "Reflexología",
    "eyebrow": "Servicio · Reflexología",
    "h1": "Reflexología podal en Sarrià–Sant Gervasi",
    "sub": "Sesión de reflexología podal · Barcelona",
    "lead": "La reflexología podal es una técnica de masaje y presión en los pies. En WA LAM la ofrecemos como una sesión de bienestar y relajación, sin fines diagnósticos ni curativos. Te explicamos qué puedes esperar y qué dice la evidencia.",
    "facts": ["Profesional: [[nombre, formación]]", "Sesión de 1 hora", "Precio: 70 €", "Ambiente tranquilo y sin prisas", "Reserva por WhatsApp"],
    "wa": "Hola, me gustaría reservar una sesión de reflexología.",
    "blocks": [
        {"type": "cards", "eyebrow": "Cuándo la proponemos", "h2": "Una sesión de relajación que combinamos con otros tratamientos",
         "items": [{"k": "Estrés y ansiedad", "h": "Alternativa a la acupuntura", "p": "En la consulta de [estrés y ansiedad](estres-ansiedad), cuando prefieres no recibir acupuntura, la combinamos con el trabajo de respiración y regulación."},
                   {"k": "Fertilidad", "h": "Bienestar durante el proceso", "p": "Durante el [acompañamiento en fertilidad](acompanamiento-fertilidad), como momento de descanso y gestión del estrés. No es un tratamiento de la infertilidad."},
                   {"k": "Sesión independiente", "h": "Relajación", "p": "Como sesión de masaje y relajación por sí misma, cuando necesitas un tiempo de pausa."}]},
        {"type": "steps", "eyebrow": "La sesión", "h2": "Cómo es una sesión de reflexología",
         "items": [("Bienvenida", "Breve entrevista sobre cómo te encuentras y cualquier condición de salud a tener en cuenta."),
                   ("Sesión", "Presión y masaje en distintas zonas de los pies, en posición cómoda y relajada."),
                   ("Cierre", "Unos minutos de reposo antes de volver a tu día.")]},
        {"type": "evidence", "h2": "Qué dice la evidencia",
         "items": [("Guía clínica (SIO–ASCO, 2022)", "La guía de la Society for Integrative Oncology y la American Society of Clinical Oncology indica que se puede ofrecer reflexología o acupresión a personas con dolor durante el tratamiento del cáncer (evidencia intermedia, recomendación moderada). Se refiere al alivio de síntomas, no a la evolución de la enfermedad."),
                   ("Revisión sistemática (2024)", "En 26 estudios con 2.465 pacientes oncológicos, la reflexología mostró beneficios en dolor, calidad de vida y fatiga frente a la atención habitual. Los estudios eran de calidad moderada o baja, y los autores piden compararla con intervenciones activas, como un masaje de pies."),
                   ("Con honestidad", "Cuando se compara con un masaje de pies convencional, parte del beneficio se reduce: el contacto y la relajación explican una parte del efecto. La idea de que cada zona del pie se corresponde con un órgano no está demostrada, y no usamos la reflexología para diagnosticar.")],
         "refs": [R["sio_asco"], R["klaus"]]},
        ficha("Ficha del servicio", "Reflexología podal", "Sesión independiente para relajarte y cuidar tu bienestar.", ROWS_SERVICIO),
    ],
    "faq": [("¿La reflexología sustituye a un tratamiento médico?", "No. La ofrecemos como una técnica de bienestar y relajación, complementaria a tu tratamiento."),
            ("¿Puedo recibir reflexología si estoy en tratamiento oncológico?", "Sí, siempre con la autorización de tu médico. La guía SIO–ASCO contempla la reflexología como apoyo para el dolor durante el tratamiento del cáncer. En WA LAM no tratamos a ningún paciente oncológico sin autorización médica, ni con reflexología, ni con drenaje, ni con masaje."),
            ("¿Hay alguna contraindicación?", "Avísanos si tienes heridas, infecciones o problemas circulatorios en los pies, o si estás embarazada.")],
    "related": ["estres-ansiedad", "acompanamiento-fertilidad", "masajes-sarria-sant-gervasi"],
    "cta": {"h2": "Reserva tu sesión de reflexología", "p": "Un momento de pausa en Sarrià–Sant Gervasi."},
})

# ---------------------------------------------------------------- ACADEMIA
PAGES.append({
    "slug": "curso-mindfulness-mbsr-barcelona", "group": "academia", "wave": 1,
    "nav": "Curso de mindfulness MBSR de 8 semanas",
    "card": "Programa MBSR de reducción del estrés de 8 semanas, online o presencial.",
    "title": "Curso de Mindfulness MBSR de 8 semanas en Barcelona | WA LAM",
    "desc": "Curso MBSR (Mindfulness-Based Stress Reduction) de 8 semanas de WA LAM, en formato online o presencial en Barcelona: programa, evidencia e información.",
    "eyebrow": "Healthy Lifestyle Academy · Programa",
    "h1": "Curso de mindfulness MBSR de 8 semanas en Barcelona",
    "sub": "Mindfulness-Based Stress Reduction · Programa de reducción del estrés",
    "lead": "El MBSR es el programa de mindfulness con mayor respaldo científico. Desarrollado por Jon Kabat-Zinn en la Facultad de Medicina de la Universidad de Massachusetts, entrena la atención, la conciencia corporal y la forma de relacionarte con el estrés, el dolor y las emociones difíciles. No es una técnica de relajación: es un entrenamiento.",
    "facts_title": "El curso",
    "facts": ["8 sesiones semanales + jornada intensiva", "Online o presencial en Sarrià–Sant Gervasi", "Habitualmente, en formato online", "Plazas limitadas"],
    "cta2": ("Ver el programa", "#las-8-semanas"),
    "wa": "Hola, me interesa el curso MBSR de 8 semanas. ¿Me podéis dar información?",
    "blocks": [
        {"type": "mirror", "eyebrow": "¿Es para ti?", "h2": "Personas que suelen inscribirse",
         "qs": ["¿Vives con estrés sostenido y sientes que tu cuerpo ya no sabe descansar?",
                "¿Te cuesta parar la mente, sobre todo por la noche?",
                "¿Convives con dolor crónico y quieres cambiar tu relación con él?",
                "¿Quieres aprender a meditar con un método estructurado y basado en evidencia?"]},
        {"type": "explain", "eyebrow": "Qué es el MBSR", "h2": "Entrenar la atención para responder en lugar de reaccionar",
         "paras": [
             "Durante ocho semanas aprenderás prácticas formales —exploración corporal, meditación sentada, movimiento consciente— y prácticas informales para llevar la atención plena a tu día a día. Trabajamos la **interocepción** (percibir lo que pasa en el cuerpo), la regulación emocional y la reducción de la reactividad ante el estrés.",
             "El programa pide compromiso: unos 30–45 minutos de práctica diaria en casa, con audios guiados. Esa práctica es la que permite que los cambios se consoliden.",
         ]},
        {"type": "steps", "eyebrow": "Programa", "h2": "Las 8 semanas",
         "items": [("Semanas 1–2 · Atención y cuerpo", "Salir del piloto automático. Exploración corporal y percepción de la experiencia."),
                   ("Semanas 3–4 · Estrés y reactividad", "Movimiento consciente, reconocer las reacciones de estrés en el cuerpo y en la mente."),
                   ("Semanas 5–6 · Responder", "Pasar de la reacción a la respuesta. Emociones difíciles y comunicación consciente."),
                   ("Semanas 7–8 · Integrar", "Jornada intensiva de práctica, autocuidado y plan para continuar por tu cuenta.")],
         "note": "Antes de empezar hay una entrevista individual para conocerte y asegurarnos de que el programa es adecuado para ti en este momento."},
        {"type": "evidence", "h2": "Qué dice la evidencia",
         "intro": "El MBSR es el programa de mindfulness más investigado del mundo. Estos son algunos de los estudios clave.",
         "items": [("Ensayo clínico (JAMA Psychiatry)", "En 276 adultos con trastorno de ansiedad generalizada, social o de pánico, el MBSR de 8 semanas fue **no inferior al escitalopram**, un antidepresivo de primera línea."),
                   ("Metaanálisis (JAMA Intern Med)", "En 47 ensayos aleatorizados (3.515 participantes), los programas de meditación redujeron de forma pequeña a moderada la ansiedad, la depresión y el dolor."),
                   ("Ensayo clínico (JAMA)", "En dolor lumbar crónico, el MBSR mejoró dolor y función frente a la atención habitual a las 26 semanas, con resultados equivalentes a la terapia cognitivo-conductual."),
                   ("Guía clínica (ACP)", "El American College of Physicians recomienda el MBSR como tratamiento inicial del dolor lumbar crónico."),
                   ("Límite", "El MBSR no sustituye un tratamiento psicológico o psiquiátrico. En algunas situaciones (depresión grave activa, trauma reciente, crisis) puede no ser el momento; lo valoramos en la entrevista previa.")],
         "refs": [R["hoge"], R["goyal"], R["cherkin"], R["qaseem"]]},
        ficha("Información", "Curso MBSR en WA LAM", "Si te interesa el curso, escríbenos y te informamos de la próxima edición.",
              [("Duración", "8 semanas + jornada intensiva"), ("Formato", "Online o presencial")]),
    ],
    "faq": [
        ("¿Necesito experiencia previa en meditación?", "No. El programa está diseñado para personas sin experiencia."),
        ("¿Cuánto tiempo hay que practicar en casa?", "Entre 30 y 45 minutos al día, con audios guiados. Es una parte esencial del programa."),
        ("¿Es lo mismo que una clase de relajación?", "No. La relajación puede aparecer, pero no es el objetivo. El MBSR entrena la atención y la forma de relacionarte con la experiencia, incluida la incómoda."),
        ("¿Hay ediciones online?", "Sí. El curso puede ser online o presencial, aunque habitualmente se imparte online."),
    ],
    "related": ["programas-re-trace", "estres-ansiedad", "dolor-persistente-cronico", "retiros-mindfulness-meditacion-silencio"],
    "cta": {"h2": "¿Te interesa el curso MBSR?", "p": "Escríbenos por WhatsApp y te informamos de la próxima edición."},
})

PAGES.append({
    "slug": "yoga-particular-grupos-reducidos", "group": "academia", "wave": 2,
    "nav": "Yoga particular y online",
    "card": "Yoga adaptado en clases particulares o con la membresía online.",
    "title": "Yoga particular y online en Barcelona · Sarrià–Sant Gervasi | WA LAM",
    "desc": "Clases de yoga particulares en Sarrià–Sant Gervasi (Barcelona) o con la membresía online de WA LAM. Yoga adaptado: respiración, movilidad, fuerza y regulación.",
    "eyebrow": "Healthy Lifestyle Academy · Clases",
    "h1": "Yoga particular y online",
    "sub": "Yoga adaptado · Sarrià–Sant Gervasi",
    "lead": "Un yoga pensado para la salud, no para la exigencia. Trabajamos respiración, movilidad, fuerza, equilibrio y conciencia corporal, adaptando cada práctica a tu cuerpo y tu momento.",
    "facts_title": "Dos modalidades",
    "facts": ["**Particular**: con cita previa", "**Online**: con la membresía", "Apto para principiantes"],
    "wa": "Hola, me interesan las clases de yoga.",
    "blocks": [
        {"type": "cards", "eyebrow": "Modalidades", "h2": "Elige cómo practicar",
         "items": [{"k": "Particular", "h": "Yoga individual", "p": "Una práctica diseñada para ti: ideal si tienes dolor, una lesión, estás en una etapa vital concreta o quieres avanzar a tu ritmo.", "li": ["Horario flexible", "Adaptación total", "Con cita previa"]},
                   {"k": "Online", "h": "Membresía online", "p": "Clases online para practicar desde casa con la membresía de la Healthy Lifestyle Academy.", "li": ["Desde cualquier lugar", "Membresía desde 25 € al mes"]}]},
        {"type": "explain", "eyebrow": "Nuestro enfoque", "h2": "Yoga como práctica de salud",
         "paras": ["Entendemos el yoga como ejercicio terapéutico adaptado: fuerza, movilidad, equilibrio y respiración, con progresiones y modificaciones para cada persona. No es una práctica espiritual en nuestras clases, sino una forma de movimiento con objetivos de salud.",
                   "La revisión Cochrane de 2022 (21 ensayos, 2.223 participantes) concluye que, en el dolor lumbar crónico, el yoga produce mejoras pequeñas en dolor y función frente a no hacer ejercicio, y resultados similares a otros ejercicios para la espalda. Por eso lo presentamos como una buena opción de ejercicio, no como un tratamiento superior a otros."],
         "quote": "Referencia: Wieland LS, et al., 2022. «Yoga for chronic non-specific low back pain». Cochrane Database of Systematic Reviews. DOI: 10.1002/14651858.CD010671.pub3"},
        ficha("Reserva", "Yoga en WA LAM", "Clases particulares con cita previa o práctica online con la membresía.",
              [("Particular", "Con cita previa"), ("Online", "Membresía desde 25 € al mes")]),
    ],
    "faq": [("¿Necesito experiencia?", "No. Adaptamos la práctica a tu nivel."),
            ("¿Puedo hacer yoga si tengo dolor de espalda?", "En muchos casos sí, con adaptaciones. Si el dolor es reciente o intenso, te recomendamos una valoración previa."),
            ("¿Qué necesito?", "Ropa cómoda.")],
    "related": ["programas-re-trace", "qigong-barcelona", "retiros-mindfulness-meditacion-silencio", "estres-ansiedad"],
    "cta": {"h2": "Reserva tu clase de yoga", "p": "Escríbenos por WhatsApp para reservar una clase particular o informarte de la membresía online."},
})

PAGES.append({
    "slug": "qigong-barcelona", "group": "academia", "wave": 2,
    "nav": "Qigong",
    "card": "Qigong en clases particulares o con la membresía online: movimiento suave, respiración y equilibrio.",
    "title": "Qigong en Barcelona · Clases particulares y en grupo | WA LAM",
    "desc": "Clases de qigong particulares en Barcelona (Sarrià–Sant Gervasi) o con la membresía online de WA LAM: movimiento suave, respiración, equilibrio y calma.",
    "eyebrow": "Healthy Lifestyle Academy · Clases",
    "h1": "Qigong en Barcelona",
    "sub": "Clases particulares y online",
    "lead": "El qigong es una forma de ejercicio de baja intensidad que combina movimientos lentos y coordinados, control postural, respiración y atención. Es accesible a casi cualquier edad y condición física, y lo trabajamos con objetivos concretos: equilibrio, movilidad, coordinación y regulación del estrés.",
    "facts_title": "Clases",
    "facts": ["**Particular**: con cita previa", "**Online**: con la membresía", "Apto para todas las edades"],
    "wa": "Hola, me interesan las clases de qigong.",
    "blocks": [
        {"type": "explain", "eyebrow": "Enfoque clínico", "h2": "Ejercicio suave con objetivos medibles",
         "paras": ["El qigong procede de la tradición china, pero en nuestras clases lo enseñamos como **ejercicio terapéutico**: secuencias lentas que trabajan la transferencia de peso, la estabilidad, la movilidad articular y una respiración lenta y diafragmática.",
                   "Su respaldo más sólido está en el equilibrio. La revisión Cochrane de 2019 sobre prevención de caídas (108 ensayos, 23.407 participantes) concluye que los programas de ejercicio de equilibrio y funcionales reducen la tasa de caídas en personas mayores un 23 %, y que el taichí, una práctica emparentada con el qigong, también podría reducirlas (evidencia de baja certeza). En otros ámbitos, la evidencia es más preliminar."],
         "quote": "Referencia: Sherrington C, et al., 2019. «Exercise for preventing falls in older people living in the community». Cochrane Database of Systematic Reviews. DOI: 10.1002/14651858.CD012424.pub2"},
        {"type": "cards", "eyebrow": "Modalidades", "h2": "Cómo practicar",
         "items": [{"k": "Particular", "h": "Clases individuales", "li": ["Horario flexible", "Adaptado a tu condición", "Con cita previa"]},
                   {"k": "Online", "h": "Membresía online", "li": ["Practica desde casa", "Membresía desde 25 € al mes"]}]},
        ficha("Reserva", "Qigong en WA LAM", "Clases particulares con cita previa o práctica online con la membresía.",
              [("Particular", "Con cita previa"), ("Online", "Membresía desde 25 € al mes")]),
    ],
    "faq": [("¿Necesito estar en forma?", "No. El qigong se adapta a cualquier nivel y se puede practicar incluso sentado."),
            ("¿En qué se diferencia del taichí?", "Comparten raíces. El taichí es una secuencia más larga de movimientos encadenados; el qigong suele trabajar ejercicios más cortos y repetidos.")],
    "related": ["programas-re-trace", "yoga-particular-grupos-reducidos", "retiros-mindfulness-meditacion-silencio", "prevencion-longevidad"],
    "cta": {"h2": "Prueba una clase de qigong", "p": "Escríbenos por WhatsApp para reservar una clase particular o informarte de la membresía online."},
})

PAGES.append({
    "slug": "formacion-re-trace", "group": "academia", "wave": 3,
    "nav": "Formación en el método re:trace",
    "card": "Formación de nueve meses para profesionales de la salud en el método re:trace.",
    "title": "Formación en el método re:trace · Medicina integrativa | WA LAM",
    "desc": "Formación de nueve meses en el método re:trace para profesionales de la salud: medicina integrativa, longevidad y neurolongevidad aplicadas a la práctica clínica.",
    "eyebrow": "Healthy Lifestyle Academy · Formación profesional",
    "h1": "Formación en el método re:trace",
    "sub": "Nueve meses para integrar el método en tu práctica clínica",
    "lead": "Una formación de nueve meses dirigida a profesionales de la salud que quieren aplicar el método re:trace: valorar al paciente en su globalidad, interpretar su trayectoria de salud y diseñar planes integrativos basados en la evidencia.",
    "facts_title": "Datos clave",
    "facts": ["Duración: 9 meses", "Dirigida a profesionales de la salud", "Primera convocatoria: septiembre de 2027"],
    "wa": "Hola, me interesa la formación en el método re:trace.",
    "blocks": [
        {"type": "explain", "eyebrow": "Qué aprenderás", "h2": "El método, de la valoración al seguimiento",
         "paras": ["La formación recorre los siete principios de [re:trace](programas-re-trace) (Research, Evidence, Trajectory, Regulation, Awareness, Clinical Integration y Evolution) y su aplicación a casos reales: la anamnesis integrativa, la lectura de la trayectoria clínica, la regulación del sistema nervioso, el eje intestino-cerebro, la inflamación de bajo grado, la longevidad y la neurolongevidad."]},
    ],
    "faq": [("¿Quién puede inscribirse?", "Profesionales de la salud que quieran incorporar el enfoque integrativo a su práctica clínica.")],
    "related": ["programas-re-trace", "medicina-integrativa-barcelona", "prevencion-longevidad", "neurolongevidad-salud-cognitiva"],
    "cta": {"h2": "Recibe información de la próxima convocatoria", "p": "Escríbenos por WhatsApp y te enviaremos el programa cuando se abra la inscripción."},
})

PAGES.append({
    "slug": "retiros-mindfulness-meditacion-silencio", "group": "academia", "wave": 2,
    "nav": "Retiros de mindfulness y meditación en silencio",
    "card": "Retiros de mindfulness con meditación habitualmente en silencio: próximas fechas y programa de cada edición.",
    "title": "Retiros de mindfulness y meditación en silencio | WA LAM",
    "desc": "Retiros de mindfulness y meditación en silencio organizados por WA LAM. Próximas fechas, programa de cada retiro e inscripción.",
    "eyebrow": "Healthy Lifestyle Academy · Retiros",
    "h1": "Retiros de mindfulness y meditación en silencio",
    "sub": "Próximas fechas y programa de cada retiro",
    "lead": "En WA LAM organizamos retiros de mindfulness, una práctica de meditación que, durante nuestros retiros, habitualmente hacemos en silencio. Consulta las próximas fechas y el programa de cada retiro.",
    "facts_title": "Próximos retiros",
    "facts": ["**Próximas fechas**: por anunciar", "Escríbenos y te avisamos cuando abramos la inscripción",
              "En cada edición indicamos cuándo se practica en silencio", "Plazas limitadas", "No se necesita experiencia previa"],
    "cta2": ("Ver próximas fechas", "#retiros-programados"),
    "wa": "Hola, me gustaría información sobre los próximos retiros de mindfulness.",
    "blocks": [
        {"type": "explain", "eyebrow": "Qué es un retiro de mindfulness", "h2": "Varios días de práctica continuada",
         "paras": ["Un **retiro de mindfulness** permite practicar de forma continuada lo que en el día a día cuesta sostener: atención a la respiración y al cuerpo, meditación sentada y caminando, y movimiento consciente. La práctica es guiada en todo momento por el equipo de WA LAM.",
                   "Es también un **retiro de meditación**: la meditación mindfulness ocupa la mayor parte del día y se alterna con explicaciones, preguntas y tiempo de descanso.",
                   "Y es, en buena parte, un **retiro de silencio**. Durante las prácticas, y habitualmente en otros momentos del día, mantenemos el silencio. No tiene un sentido espiritual: el silencio reduce los estímulos y facilita la atención sostenida y el descanso. En la ficha de cada edición indicamos con exactitud cuándo se practica en silencio."]},
        {"type": "cards", "eyebrow": "Próximas ediciones", "h2": "Retiros programados",
         "intro": "Estamos preparando las próximas ediciones. Escríbenos por WhatsApp y te avisaremos en cuanto abramos la inscripción.",
         "items": [{"k": "Fechas por anunciar", "h": "Próxima edición", "p": "Cuando publiquemos la edición, aquí encontrarás las fechas, el lugar, el programa y qué incluye el precio.", "li": ["En cada edición indicamos cuándo se practica en silencio", "Plazas limitadas", "Aviso por WhatsApp al abrir la inscripción"]}]},
        {"type": "steps", "eyebrow": "Un día de retiro", "h2": "Estructura orientativa",
         "intro": "La estructura concreta se detalla en el programa de cada edición.",
         "items": [("Mañana", "Meditación sentada y movimiento consciente, habitualmente en silencio."),
                   ("Mediodía", "Comida, a menudo también en silencio, y tiempo de descanso."),
                   ("Tarde", "Meditación caminando, prácticas guiadas y un espacio para preguntas al equipo.")]},
        {"type": "evidence", "h2": "Por qué el mindfulness",
         "items": [("Metaanálisis (JAMA Intern Med)", "Los programas de meditación mindfulness producen reducciones de pequeñas a moderadas en ansiedad, depresión y dolor (47 ensayos)."),
                   ("Ensayo clínico (JAMA Psychiatry)", "Un programa MBSR de 8 semanas fue no inferior al escitalopram en adultos con trastornos de ansiedad."),
                   ("Con honestidad", "La evidencia procede sobre todo de programas semanales como el MBSR. Los retiros intensivos están menos estudiados, por eso los recomendamos como profundización, no como tratamiento.")],
         "refs": [R["goyal"], R["hoge"]]},
    ],
    "faq": [("¿Necesito experiencia previa en meditación?", "No, salvo que la ficha de la edición indique lo contrario. Si nunca has meditado, el [curso MBSR de 8 semanas](curso-mindfulness-mbsr-barcelona) es una buena base."),
            ("¿Todo el retiro es en silencio?", "Habitualmente practicamos en silencio, pero no todo el tiempo: hay momentos de explicación y de preguntas. En cada edición indicamos cuándo se practica en silencio."),
            ("¿Qué incluye el precio?", "Depende de cada edición; lo detallamos en su ficha: alojamiento, comidas, sesiones y traslados si los hay."),
            ("¿Hay política de cancelación?", "Sí. Las condiciones de cancelación se indican en la ficha de cada retiro, en la [página de retiros](https://www.walambcn.com/academia-vida-saludable-barcelona/retiros) de la Healthy Lifestyle Academy.")],
    "related": ["programas-re-trace", "curso-mindfulness-mbsr-barcelona", "vacaciones-con-sentido", "estres-ansiedad"],
    "cta": {"h2": "Reserva tu plaza en el próximo retiro", "p": "Escríbenos y te enviamos el programa de la edición que te interese."},
})

PAGES.append({
    "slug": "vacaciones-con-sentido", "group": "academia", "wave": 1,
    "nav": "Vacaciones con sentido",
    "card": "Retiros clínico-terapéuticos de una semana en entornos naturales: tomar conciencia e incorporar nuevos hábitos.",
    "title": "Vacaciones con sentido · Retiros de salud de 7 días | WA LAM",
    "desc": "Vacaciones con sentido de WA LAM: retiros de 7 días en lugares emblemáticos de la naturaleza, con conferencias de salud integrativa y práctica diaria.",
    "eyebrow": "Healthy Lifestyle Academy · Vacaciones con sentido",
    "h1": "Vacaciones con sentido",
    "sub": "Siete días para descansar, aprender y cuidarte en plena naturaleza",
    "lead": "No son unas vacaciones al uso. Es una semana de inmersión para tomar conciencia de tu salud, descansar de verdad y volver con hábitos nuevos, en un entorno natural que cambia en cada edición.",
    "facts_title": "Cada edición",
    "facts": ["7 días", "Un destino distinto en cada edición", "Charlas, práctica y naturaleza", "Plazas limitadas", "Vuelos no incluidos"],
    "cta2": ("Qué incluye", "#como-es-cada-edicion"),
    "wa": "Hola, me interesa Vacaciones con sentido. ¿Me enviáis la próxima convocatoria?",
    "blocks": [
        {"type": "explain", "eyebrow": "Qué son", "h2": "Más que unas vacaciones: una semana de inmersión",
         "paras": ["El ritmo de vida actual acumula en el cuerpo y en la mente un estrés, una inflamación y un cansancio que unas vacaciones convencionales no resuelven. Vacaciones con sentido nace para eso: retiros clínico-terapéuticos de una semana pensados para recuperar el equilibrio físico, mental y emocional.",
                   "No es un viaje turístico más. Es una semana para tomar conciencia de cómo vives y de cómo te cuidas, y para empezar a incorporar nuevos hábitos con acompañamiento. Cada edición se celebra en un escenario natural elegido por su belleza y su serenidad, donde el entorno ayuda a bajar el ritmo.",
                   "Al volver no te llevas solo el recuerdo de un lugar especial, sino herramientas concretas para sostener en tu día a día una vida más consciente y saludable."]},
        {"type": "cards", "eyebrow": "La experiencia", "h2": "Qué vivirás durante la semana",
         "items": [{"h": "Yoga terapéutico y meditación guiada", "p": "Para regular el sistema nervioso, mejorar la postura y la movilidad y aprender a respirar mejor."},
                   {"h": "Charlas y talleres de medicina integrativa", "p": "Cómo influyen la alimentación, la respiración, el descanso y las emociones en tu salud, con herramientas prácticas para aplicarlas en casa."},
                   {"h": "Alimentación consciente y antiinflamatoria", "p": "Cocina con productos frescos y locales que cuida la microbiota intestinal y ayuda a reducir la inflamación."},
                   {"h": "Exposición al agua fría", "p": "Una práctica que estimula la circulación y entrena la capacidad de adaptación del cuerpo y de la mente."},
                   {"h": "Caminatas conscientes en la naturaleza", "p": "Movimiento y atención plena en el entorno natural del retiro."}]},
        {"type": "cards", "eyebrow": "Lo que te llevas", "h2": "Para qué sirve esta semana",
         "items": [{"h": "Menos estrés", "p": "Prácticas que activan la respuesta de calma del sistema nervioso."},
                   {"h": "Mejor descanso", "p": "Hábitos que ayudan a ordenar los ritmos circadianos y a dormir mejor."},
                   {"h": "Menos inflamación", "p": "Una alimentación antiinflamatoria y prácticas de recuperación."},
                   {"h": "Más claridad y energía", "p": "Atención, vitalidad y una mente más despejada al volver."}]},
        {"type": "explain", "eyebrow": "Una experiencia compartida", "h2": "Cuerpo, corazón y mente",
         "paras": ["El retiro gira en torno a cuatro intenciones: cultivar un cuerpo alegre y con energía, un corazón amable y compasivo, una mente reflexiva y atenta, y una forma más ligera de estar en la vida. Cada día empieza y termina con yoga, y las actividades en grupo crean vínculos que muchas veces continúan después del viaje."]},
        {"type": "explain", "eyebrow": "Condiciones", "h2": "Cómo es cada edición",
         "paras": ["El destino, las fechas y el alojamiento se anuncian en cada convocatoria, y el precio varía según el lugar escogido. Los vuelos y el seguro de viaje corren a cargo de cada participante."]},
    ],
    "faq": [("¿Dónde se celebran?", "En un lugar distinto en cada edición, siempre en un entorno natural. Lo anunciamos en cada convocatoria."),
            ("¿Necesito experiencia en yoga o meditación?", "No. Las prácticas se adaptan a todos los niveles."),
            ("¿Están incluidos los vuelos?", "No. Los vuelos y el seguro de viaje corren a cargo de cada participante, que los reserva por su cuenta."),
            ("¿Cuánto cuesta?", "El precio varía según el destino de cada edición y se indica en la convocatoria.")],
    "related": ["programas-re-trace", "retiros-mindfulness-meditacion-silencio", "curso-mindfulness-mbsr-barcelona", "prevencion-longevidad"],
    "cta": {"h2": "Recibe la próxima convocatoria", "p": "Escríbenos por WhatsApp y te enviamos el destino, las fechas y el programa."},
})


# ---------------------------------------------------------------- QUIÉN ATIENDE
# Credenciales tomadas del currículum publicado en walambcn.com/curriculum.
# Nombre completo (mejor para E-E-A-T). Para usar iniciales, cambiar ROSA y SITE["owner"].
SITE.update({
    "booking": "https://www.walambcn.com/reserva-sarri%C3%A0-sant-gervasi-barcelona",
    "street": "C/ Bisbe Sivilla, 44, local",
    "postal": "08022",
    "address_short": "C/ Bisbe Sivilla, 44 · 08022 Barcelona (Sarrià–Sant Gervasi)",
    "hours": "De lunes a viernes, de 9 a 21 h. Sábados, domingos y urgencias, solo con cita previa.",
    "opening": ["Mo-Fr 09:00-21:00"],
    "reviewer_md": "Rosa María Rodríguez Valls, osteópata D.O. · máster en medicina integrativa",
    "owner": "Rosa María Rodríguez Valls",
    "reviewer": {"name": "Rosa María Rodríguez Valls", "title": "Osteópata D.O. y máster en medicina integrativa"},
})

ROSA = "Rosa María Rodríguez Valls"
PRO = {
    "medicina-integrativa-barcelona": f"{ROSA}, osteópata D.O. y máster en medicina integrativa, fundadora de WA LAM (2004)",
    "neurolongevidad-salud-cognitiva": f"{ROSA}, máster en medicina integrativa y profesora de MBSR",
    "dolor-persistente-cronico": f"{ROSA}, osteópata D.O.",
    "estres-ansiedad": f"{ROSA}, profesora de MBSR: dos másteres en mindfulness para la salud (Universidad de Zaragoza y Universidad Complutense de Madrid), formación de formadores de profesores de MBSR con Nirakara (nivel 2) y formación de profesora de mindfulness de 200 horas",
    "sueno-insomnio": f"{ROSA}",
    "salud-digestiva-microbiota": f"{ROSA}, máster en PNIE",
    "acompanamiento-fertilidad": f"{ROSA}",
    "salud-mujer-menopausia": f"{ROSA}",
    "prevencion-longevidad": f"{ROSA}, osteópata D.O. y máster en medicina integrativa",
    "osteopatia-sarria-sant-gervasi": f"{ROSA}, osteópata D.O.",
    "osteopatia-visceral-barcelona": f"{ROSA}, osteópata D.O., formación en manipulación visceral (Barral Institute)",
    "osteopatia-craneosacral-barcelona": f"{ROSA}, osteópata D.O., formación en terapia craneosacral (Upledger Institute)",
    "manipulaciones-neuroviscerales": f"{ROSA}, osteópata D.O., formación en manipulación neural y visceral (Barral Institute)",
    "suelo-pelvico-dolor-pelvico": f"{ROSA}, osteópata D.O., formación en manipulación visceral (Barral Institute)",
    "neuralgia-pudendo": f"{ROSA}, osteópata D.O., formación en manipulación visceral (Barral Institute)",
    "dolor-menstrual-endometriosis": f"{ROSA}, osteópata D.O., formación en manipulación visceral (Barral Institute)",
    "dispareunia-dolor-relaciones": f"{ROSA}, osteópata D.O., formación en manipulación visceral (Barral Institute)",
    "dolor-coxis-coccigodinia": f"{ROSA}, osteópata D.O., formación en manipulación visceral (Barral Institute)",
    "cistitis-repeticion-vejiga-dolorosa": f"{ROSA}, osteópata D.O., formación en manipulación visceral (Barral Institute)",
    "osteopatia-embarazo-posparto": f"{ROSA}, osteópata D.O., formación en manipulación visceral (Barral Institute)",
    "incontinencia-urinaria-esfuerzo": f"{ROSA}, osteópata D.O., formación en manipulación visceral (Barral Institute)",
    "drenaje-linfatico-linfedema": f"{ROSA}, formada en drenaje linfático manual",
    "perdida-de-peso-sarria-sant-gervasi": f"{ROSA}, posgrado en acupuntura para la obesidad",
    "dejar-de-fumar-acupuntura": f"{ROSA}, acupuntura",
    "acupuntura-medicina-tradicional-china": f"{ROSA}, acupuntura y MTC",
    "pni-pnie-barcelona": f"{ROSA}, máster en PNIE (Xevi Verdaguer)",
    "nutricion-salud-intestinal": f"{ROSA}, máster en PNIE",
    "drenaje-linfatico-postoperatorio": f"{ROSA}, formada en drenaje linfático manual",
    "masajes-sarria-sant-gervasi": f"{ROSA}",
    "reflexologia-sarria-sant-gervasi": f"{ROSA}",
    "curso-mindfulness-mbsr-barcelona": f"{ROSA}, profesora de MBSR: dos másteres en mindfulness para la salud (Universidad de Zaragoza y Universidad Complutense de Madrid), formación de formadores de profesores de MBSR con Nirakara (nivel 2) y formación de profesora de mindfulness de 200 horas",
    "yoga-particular-grupos-reducidos": f"{ROSA}, profesora de Hatha yoga (550 h)",
    "qigong-barcelona": f"{ROSA}, máster en ejercicios para la salud basados en Qigong (Universidad de Extremadura, Badajoz)",
    "formacion-re-trace": f"{ROSA}, osteópata D.O.",
    "retiros-mindfulness-meditacion-silencio": f"{ROSA}, profesora de MBSR: dos másteres en mindfulness para la salud (Universidad de Zaragoza y Universidad Complutense de Madrid), formación de formadores de profesores de MBSR con Nirakara (nivel 2) y formación de profesora de mindfulness de 200 horas",
    "vacaciones-con-sentido": f"{ROSA}",
}
_TOKENS = ["[[nombre, titulación]]", "[[Nombre y titulación]]", "[[nombre, formación]]", "[[profesional responsable]]",
           "[[nombre, nº colegiado/a]]", "[[nombre, acreditación MBSR]]", "[[Profesional/es responsable/s]]",
           "[[Profesional responsable de la primera valoración de dolor]]", "[[nombre]]", "[[profesionales]]"]


def _fix(o, who):
    if isinstance(o, str):
        for t in _TOKENS:
            o = o.replace(t, who)
        return o.replace("[[Nº colegiado/a]]", "[[nº de colegiada]]").replace("D.O..", "D.O.")
    if isinstance(o, list):
        return [_fix(x, who) for x in o]
    if isinstance(o, tuple):
        return tuple(_fix(x, who) for x in o)
    if isinstance(o, dict):
        return {k: (v if k in ("slug", "type", "group", "related", "refs") else _fix(v, who)) for k, v in o.items()}
    return o


for _i, _p in enumerate(PAGES):
    _w = PRO.get(_p["slug"], ROSA)
    _p = _fix(_p, _w)
    if _p["slug"] != "fisioterapia-sarria-sant-gervasi":
        for _b in _p["blocks"]:
            if _b.get("type") == "pro":
                _b["rows"] = [r for r in _b["rows"] if "colegiad" not in r[0]]
    _p["pro_who"] = _w
    PAGES[_i] = _p

# Precios confirmados por Rosa (nov. 2026)
_H70 = {"Sesión de [[duración]] · [[precio]]": "Sesión de 1 hora · 70 €", "[[min]]": "60 min", "[[€]]": "70 €", "[[Duración]]": "Una hora", "[[duración]]": "1 hora", "[[precio]]": "70 €"}
_H50 = {"Sesión de [[duración]] · [[precio]]": "Sesión de 1 hora · 50 €", "[[min]]": "60 min", "[[€]]": "50 €", "[[Duración]]": "Una hora", "[[duración]]": "1 hora", "[[precio]]": "50 €"}
PRICES = {s_: _H70 for s_ in ("osteopatia-sarria-sant-gervasi", "osteopatia-visceral-barcelona", "osteopatia-craneosacral-barcelona",
                              "manipulaciones-neuroviscerales", "suelo-pelvico-dolor-pelvico", "reflexologia-sarria-sant-gervasi", "masajes-sarria-sant-gervasi")}
PRICES.update({"acupuntura-medicina-tradicional-china": _H50, "dejar-de-fumar-acupuntura": _H50,
               "pni-pnie-barcelona": {"Primera consulta de [[duración]] · [[precio]]": "Primera visita: 90 €", "[[min]]": "Primera visita", "[[€]]": "90 €"}})


def _price(o, m):
    if isinstance(o, str):
        for k_, v_ in m.items():
            o = o.replace(k_, v_)
        return o
    if isinstance(o, list):
        return [_price(x, m) for x in o]
    if isinstance(o, tuple):
        return tuple(_price(x, m) for x in o)
    if isinstance(o, dict):
        return {k: (v if k in ("slug", "type", "group", "related", "refs") else _price(v, m)) for k, v in o.items()}
    return o


for _i, _p in enumerate(PAGES):
    if _p["slug"] in PRICES:
        PAGES[_i] = _price(_p, PRICES[_p["slug"]])

# Enlaces de vuelta a Longevidad desde los recorridos que la componen
for _p in PAGES:
    if _p["slug"] in ("estres-ansiedad", "sueno-insomnio", "salud-digestiva-microbiota", "pni-pnie-barcelona", "salud-mujer-menopausia",
                      "dolor-persistente-cronico", "curso-mindfulness-mbsr-barcelona", "yoga-particular-grupos-reducidos", "qigong-barcelona",
                      "perdida-de-peso-sarria-sant-gervasi"):
        _rel = [r for r in _p.get("related", []) if r != "prevencion-longevidad"]
        _p["related"] = (["prevencion-longevidad"] + _rel)[:4]

# ---------------------------------------------------------------- PROLAPSO
R["hagen"] = _r("Hagen S, Stark D, 2011. «Conservative prevention and management of pelvic organ prolapse in women». Cochrane Database of Systematic Reviews.", "10.1002/14651858.CD003882.pub4")
R["barber"] = _r("Barber MD, Maher C, 2013. «Epidemiology and outcome assessment of pelvic organ prolapse». International Urogynecology Journal.", "10.1007/s00192-013-2169-9")
uro_page("prolapso-organos-pelvicos", "Prolapso de órganos pélvicos", "Sensación de bulto o peso vaginal por el descenso de la vejiga, el útero o el recto.",
  "Prolapso de órganos pélvicos en Barcelona | WA LAM",
  "Prolapso de órganos pélvicos en Sarrià–Sant Gervasi, Barcelona: sensación de peso o bulto vaginal. Abordaje osteopático externo complementario a la fisioterapia y la ginecología.",
  "Prolapso de órganos pélvicos", "Prolapso de órganos pélvicos", "Cistocele, prolapso uterino y rectocele · Sarrià–Sant Gervasi",
  "El prolapso de órganos pélvicos es el descenso de la vejiga, el útero o el recto hacia la vagina, cuando los ligamentos, las fascias y la musculatura que los sostienen pierden su capacidad de soporte. Se nota como peso, presión o un bulto en la vagina, que suele aumentar al final del día o tras un esfuerzo.",
  ["Sensación de peso o bulto vaginal", "Tras el parto y en la menopausia", "Sistema de soporte de la pelvis", "Abordaje externo complementario", "Primera visita: 60 min · 90 €"],
  "Hola, me gustaría información sobre el prolapso de órganos pélvicos.",
  "Cuando notas peso en la pelvis",
  ["¿Notas una sensación de peso, presión o bulto en la vagina?", "¿Las molestias aumentan al final del día, al estar mucho de pie o al cargar peso?", "¿Te cuesta vaciar del todo la vejiga o el intestino?", "¿Te han diagnosticado un cistocele, un prolapso uterino o un rectocele?"],
  "El diagnóstico y el grado del prolapso los establece tu ginecóloga. Si el bulto sale fuera de la vagina, sangra o no puedes orinar, consulta con ella sin demora.",
  "Un problema del sistema de soporte",
  ["La vejiga, el útero y el recto se mantienen en su posición gracias a un sistema de ligamentos, fascias y músculos. El embarazo y el parto, el descenso hormonal de la menopausia, el estreñimiento crónico, la tos persistente o el esfuerzo repetido pueden debilitarlo.",
   "Es muy frecuente: según una revisión internacional, entre el 3 % y el 6 % de las mujeres tienen síntomas de prolapso, y hasta la mitad presenta algún grado de descenso en la exploración, aunque muchas no lo noten. El entrenamiento de la musculatura del suelo pélvico con una fisioterapeuta especializada es el tratamiento conservador de referencia; en WA LAM lo complementamos con un abordaje osteopático externo de la pelvis, el abdomen y el diafragma."],
  "Cómo afecta a la vida diaria",
  ["La sensación de peso, las molestias al estar de pie y las dificultades para orinar o defecar afectan a la actividad física, a la sexualidad y a la confianza en el propio cuerpo."],
  [("Revisión Cochrane", "En mujeres con prolapso, el entrenamiento de la musculatura del suelo pélvico mejoró los síntomas y aumentó la probabilidad de mejorar el grado del prolapso frente a no hacer tratamiento (Hagen y Stark, 2011)."),
   ("Revisión (Int Urogynecol J)", "Entre el 3 % y el 6 % de las mujeres refieren síntomas de prolapso, y hasta el 50 % presenta algún grado de descenso en la exploración vaginal (Barber y Maher, 2013).")],
  [R["hagen"], R["barber"]],
  [("¿Sustituye a la fisioterapia de suelo pélvico o a la cirugía?", "No. El entrenamiento del suelo pélvico es el tratamiento conservador de referencia y, en los casos que lo requieren, la ginecóloga valora otras opciones. Nuestro abordaje es complementario."),
   ("¿Hacéis tratamiento interno?", "No. Nuestro abordaje es siempre externo.")],
  ["suelo-pelvico-dolor-pelvico", "incontinencia-urinaria-esfuerzo", "osteopatia-embarazo-posparto", "salud-mujer-menopausia"], "Recuperar la confianza en tu cuerpo")
PRO["prolapso-organos-pelvicos"] = PRO["incontinencia-urinaria-esfuerzo"]
for _p in PAGES:
    if _p["slug"] == "suelo-pelvico-dolor-pelvico":
        for _b in _p["blocks"]:
            if _b.get("h2") == "Motivos de consulta":
                _b["items"].append({"h": "[Prolapso de órganos pélvicos](prolapso-organos-pelvicos)"})

# re:trace solo aparece en su propia página (y en la de su formación)
for _p in PAGES:
    if _p["slug"] not in ("programas-re-trace", "formacion-re-trace"):
        _p["related"] = [r for r in _p.get("related", []) if r != "programas-re-trace"]

# H1 descriptivos (comparativa SEO de noviembre de 2026)
_H1 = {
    "dolor-persistente-cronico": "Abordaje del dolor crónico en Barcelona",
    "estres-ansiedad": "Estrés y ansiedad en Barcelona",
    "sueno-insomnio": "Sueño e insomnio en Barcelona",
    "salud-mujer-menopausia": "Salud de la mujer y menopausia en Barcelona",
    "neurolongevidad-salud-cognitiva": "Salud cognitiva y regulación del sistema nervioso en Barcelona",
    "suelo-pelvico-dolor-pelvico": "Salud pélvica y tratamiento urogenital en Barcelona",
    "nutricion-salud-intestinal": "Nutrición y salud intestinal en Barcelona",
    "pni-pnie-barcelona": "Psiconeuroinmunoendocrinología (PNIE) en Barcelona",
    "neuralgia-pudendo": "Neuralgia del pudendo y dolor perineal",
    "incontinencia-urinaria-esfuerzo": "Incontinencia urinaria de esfuerzo y suelo pélvico",
    "osteopatia-embarazo-posparto": "Osteopatía en el embarazo y el posparto en Barcelona",
    "salud-digestiva-microbiota": "Salud digestiva y microbiota en Barcelona",
}
_BLOG_INTRO = {
    "nutricion-salud-intestinal": "En el magazín de WA LAM encontrarás más información sobre alimentación y microbiota:",
    "salud-digestiva-microbiota": "En el magazín de WA LAM encontrarás más información sobre el intestino y la microbiota:",
}
_NUTRI_STEPS = {"type": "steps", "eyebrow": "Primera visita", "h2": "Cómo es la primera visita de nutrición",
    "items": [("Antes de venir", "Rellenas el [formulario de primera cita](https://www.walambcn.com/primera-cita) y nos envías tus analíticas recientes, si las tienes."),
              ("La consulta", "Setenta y cinco minutos para revisar tus síntomas digestivos, tu historia clínica, qué comes, cómo y cuándo comes, tu descanso y tu nivel de estrés."),
              ("Las pautas", "Recibes por escrito unas pautas de alimentación antiinflamatoria individualizadas, progresivas y adaptadas a tu vida."),
              ("El seguimiento", "En las visitas de seguimiento (40 minutos) revisamos cómo responde tu digestión y ajustamos las pautas.")]}
def _blog_block(sl):
    from urllib.parse import unquote as _uq
    from seo_map import BLOG as _B
    links = []
    for b in _B.get(sl, []):
        t = _uq(b).split("/post/")[1].replace("-", " ")
        links.append("[" + t[0].upper() + t[1:] + "](https://www.walambcn.com" + b + ")")
    return {"type": "explain", "eyebrow": "Magazín", "h2": "Artículos relacionados", "paras": [_BLOG_INTRO[sl] + " " + " · ".join(links)]}
for _p in PAGES:
    if _p["slug"] in _H1:
        _p["h1"] = _H1[_p["slug"]]
    if _p["slug"] == "nutricion-salud-intestinal":
        _p["blocks"].insert(1, _NUTRI_STEPS)
    if _p["slug"] in _BLOG_INTRO:
        _k = next((n for n, b in enumerate(_p["blocks"]) if b.get("type") == "pro"), len(_p["blocks"]))
        _p["blocks"].insert(_k, _blog_block(_p["slug"]))

# Salud pélvica: motivos de consulta, primera visita y formación separada (comparativa SEO)
_PELV_VISITA = {"type": "steps", "eyebrow": "Primera visita", "h2": "Cómo es la primera visita",
    "items": [("Tu historia", "Hablamos de tus síntomas, de cuándo empezaron, de tus partos, cirugías o caídas y de cómo afectan a tu vida diaria."),
              ("La valoración", "Exploración externa de la pelvis, el abdomen, la columna y el diafragma. Nunca realizamos exploraciones internas."),
              ("El plan", "Te explicamos qué factores creemos que intervienen y te proponemos un tratamiento, complementario al seguimiento de tu ginecóloga o tu médico."),
              ("Cómo pedir cita", "Escríbenos por WhatsApp o llámanos. La primera visita dura 60 minutos y cuesta 90 €.")]}
for _p in PAGES:
    if _p["slug"] == "suelo-pelvico-dolor-pelvico":
        _bl = _p["blocks"]
        _mot = next(b for b in _bl if b.get("h2") == "Motivos de consulta en salud pélvica")
        _form = next(b for b in _bl if b.get("h2") == "Formación urogenital con Olivier Bazin")
        _rest = [b for b in _bl if b not in (_mot, _form) and b.get("h2") != "Qué acompañamos"]
        _mot["h2"] = "Motivos de consulta"
        _k = next(n for n, b in enumerate(_rest) if b.get("type") == "explain") + 1
        _p["blocks"] = _rest[:_k] + [_mot, _PELV_VISITA] + _rest[_k:] + [_form]
    if _p["slug"] == "yoga-particular-grupos-reducidos":
        _p["h1"] = "Yoga terapéutico en Barcelona"
        _p["blocks"][1:1] = [
            {"type": "explain", "eyebrow": "Para quién", "h2": "A quién va dirigido",
             "paras": ["Personas que quieren moverse mejor sin exigencias: con dolor de espalda o rigidez, que vuelven a la actividad tras una lesión, que viven con estrés o que nunca han practicado yoga. Si tienes dolor reciente o intenso, te recomendamos una valoración previa."]},
            {"type": "steps", "eyebrow": "La sesión", "h2": "Cómo es una sesión",
             "items": [("Inicio", "Comentamos cómo estás ese día y adaptamos la práctica."),
                       ("Práctica", "Respiración, movilidad, fuerza y equilibrio, con las modificaciones que necesites."),
                       ("Cierre", "Relajación guiada y pautas sencillas para practicar en casa.")]}]

# Frases elegidas por Rosa (noviembre de 2026)
for _p in PAGES:
    if _p["slug"] == "medicina-integrativa-barcelona":
        _p["sub"] = "Mirar más allá del síntoma"
        for _b in _p["blocks"]:
            if _b.get("h2") == "Cómo practicamos la medicina integrativa en WA LAM":
                _b["quote"] = "Ciencia y cuidado, en un mismo tratamiento."
        _p["cta"] = {"h2": "Tu salud, hoy y en los años que vienen", "p": "Escríbenos por WhatsApp y te orientamos sobre tu caso."}
    if _p["slug"] == "prevencion-longevidad":
        _p["sub"] = "Vivir más años y vivirlos mejor · Sarrià–Sant Gervasi"
        _p["blocks"][0]["quote"] = "La salud que construyes hoy es la que vivirás mañana."
    if _p["slug"] == "neurolongevidad-salud-cognitiva":
        _p["sub"] = "Un cerebro joven a cualquier edad · Sarrià–Sant Gervasi"
        for _b in _p["blocks"]:
            if _b.get("type") == "explain":
                _b["quote"] = "Tu cerebro también envejece. Puedes cuidarlo."
                break
for _p in PAGES:
    if _p["slug"] == "curso-mindfulness-mbsr-barcelona":
        _p["h1"] = "Curso de mindfulness MBSR de 8 semanas, online y en Barcelona"


# Portada (noviembre 2026): un solo apartado de presentación, sin ejemplo del hombro
for _p in PAGES:
    if _p["slug"] == "medicina-integrativa-barcelona":
        _b = _p["blocks"][0]
        _b["eyebrow"] = "Medicina integrativa"
        _b["h2"] = "Qué es la medicina integrativa y cómo la practicamos"
        _b["_id"] = "que-es-la-medicina-integrativa"
        _b["h2"] = "Qué es la medicina integrativa"
        _b["paras"] = ["La medicina integrativa es un enfoque basado en la evidencia científica que contempla a la persona en su globalidad, no solo el síntoma. Aúna el conocimiento científico actual y las terapias que cuentan con respaldo en la evidencia en un único plan terapéutico, diseñado de forma individual para cada paciente."]
        _p["blocks"].insert(1, {"type": "cards", "eyebrow": "", "h2": _p["facts_title"], "_id": "te-ayudamos",
                                "items": [{"h": f, "p": ""} for f in _p["facts"]]})
        for _c in _p["blocks"]:
            if _c.get("h2") == "Una medicina sin prisas":
                _c["eyebrow"] = "Slow medicine"
for _p in PAGES:
    if _p["slug"] == "medicina-integrativa-barcelona":
        _p["lead"] = ""
        _p["blocks"] = [b for b in _p["blocks"] if b.get("h2") != "¿Qué es WA LAM?"]

for _p in PAGES:
    if _p["slug"] == "en-que-podemos-ayudarte":
        _p["blocks"] = [b for b in _p["blocks"] if b.get("h2") != "Por qué abordamos estos procesos de forma integrada"]
        _p["lead"] = _p["lead"].replace("Estas son las situaciones clínicas por las que se consulta", "Estos son los motivos por los que se consulta")

# Fertilidad y acupuntura: sin datos negativos (noviembre 2026)
for _p in PAGES:
    for _b in _p["blocks"]:
        if _b.get("type") == "evidence":
            _b["items"] = [(lv, t) for lv, t in _b["items"] if "nacidos vivos" not in t]
            _b["refs"] = [r for r in _b.get("refs", []) if "Smith CA" not in r["t"]]
    if _p.get("faq"):
        _p["faq"] = [("¿Qué aporta la acupuntura durante un tratamiento de fertilidad?", "Puede ayudarte a gestionar el estrés y a cuidar tu bienestar durante el proceso, como complemento del seguimiento de tu clínica de reproducción.") if q.startswith("¿La acupuntura mejora las probabilidades de embarazo") else (q, a) for q, a in _p["faq"]]

# Landings de patologías nuevas (noviembre 2026)
from new_pages import integrate_pages as _np_int  # noqa: E402
_np_int(PAGES)
from new_pages import integrate_areas as _np_areas  # noqa: E402
_np_areas(PAGES)

# Portada: botón de WhatsApp bajo «Qué es la medicina integrativa»; Slow medicine en grande
for _p in PAGES:
    if _p["slug"] == "medicina-integrativa-barcelona":
        for _b in _p["blocks"]:
            if _b.get("_id") == "que-es-la-medicina-integrativa":
                _b["wa_btn"] = _p["wa"]
            if _b.get("h2") == "Una medicina sin prisas":
                _b["h2"] = "Slow medicine"; _b["eyebrow"] = ""; _b["intro"] = "Una medicina sin prisas"; _b["_id"] = "slow-medicine"

# Salud pélvica (noviembre 2026): página principal «Suelo pélvico en Barcelona»
for _p in PAGES:
    if _p["slug"] == "suelo-pelvico-dolor-pelvico":
        _p["h1"] = "Suelo pélvico en Barcelona"; _p["nav"] = "Suelo pélvico"; _p["eyebrow"] = "Salud pélvica"
        _p["sub"] = "Salud pélvica de la mujer · Sarrià–Sant Gervasi"
        _p["title"] = "Suelo pélvico en Barcelona | WA LAM"
        _p["blocks"] = [b for b in _p["blocks"] if b.get("type") != "evidence"]
        for _b in _p["blocks"]:
            if _b.get("h2") == "Formación urogenital con Olivier Bazin":
                _b["eyebrow"] = ""; _b["h2"] = "Para profesionales"
        _i = next(k for k, b in enumerate(_p["blocks"]) if b["type"] == "explain") + 1
        _p["blocks"].insert(_i, {"type": "cards", "eyebrow": "", "h2": "También en salud pélvica", "_id": "tambien-salud-pelvica",
            "items": [{"h": "[Dolor pélvico](dolor-pelvico-barcelona)", "p": "Dolor menstrual, endometriosis, vejiga dolorosa, dolor perineal o en las relaciones: cómo lo trabajamos."},
                      {"h": "[Ejercicios de suelo pélvico](ejercicios-suelo-pelvico)", "p": "Guía práctica para localizar, fortalecer y coordinar tu suelo pélvico en el día a día."}]})
        _p["cta"] = {"h2": "Pide una primera valoración", "p": "Escríbenos por WhatsApp y te orientamos sobre tu caso."}
        _p["related"] = ["dolor-pelvico-barcelona", "ejercicios-suelo-pelvico", "prolapso-organos-pelvicos", "incontinencia-urinaria-esfuerzo"]
_PELV_FIX = [(", como complemento del seguimiento ginecológico o urológico.", "."),
             (", complementario al seguimiento de tu ginecóloga o tu médico.", "."),
             (", complementaria al seguimiento médico.", ". Valoración global de la pelvis.")]
_known = {p["slug"] for p in PAGES}
for _p in PAGES:
    if _p["slug"] == "suelo-pelvico-dolor-pelvico":
        def _fx(s):
            for a, b in _PELV_FIX:
                s = s.replace(a, b)
            return s
        from new_pages import _walk as _w
        _w(_p, _fx)
        for _b in _p["blocks"]:
            if _b.get("paras"):
                _b["paras"] = [x for x in _b["paras"] if not x.startswith("Si necesitas fisioterapia de suelo pélvico")]
        _p["faq_title"] = "Preguntas sobre salud pélvica"
        _p["related"] = [x for x in _p["related"] if x in _known]
for _p in PAGES:
    if _p["slug"] == "suelo-pelvico-dolor-pelvico" and _p.get("faq") is not None:
        _q = "¿Cómo pido cita para una valoración de suelo pélvico?"
        if not any(q == _q for q, a in _p["faq"]):
            _p["faq"] = list(_p["faq"]) + [(_q, "Escríbenos por WhatsApp, cuéntanos brevemente qué notas y te proponemos día y hora para la primera valoración, de 60 minutos, en Sarrià–Sant Gervasi.")]

# Todas las páginas de salud pélvica enlazan a la formación de Olivier Bazin
for _p in PAGES:
    if _p["slug"] in ("dolor-pelvico-barcelona", "ejercicios-suelo-pelvico") and not any(b.get("eyebrow") == "Para profesionales" for b in _p["blocks"]):
        _p["blocks"].append(uro_pro())

# Menopausia (noviembre 2026): título directo y sin frases de complemento
import json as _json
from pathlib import Path as _Path
_MENO = _json.loads((_Path(__file__).parent / "meno_fix.json").read_text())
for _p in PAGES:
    if _p["slug"] == "salud-mujer-menopausia":
        _p["h1"] = "Menopausia en Barcelona"; _p["nav"] = "Menopausia"
        def _mf(s):
            for a, b in _MENO:
                s = s.replace(a, b)
            return s
        from new_pages import _walk as _w2
        _w2(_p, _mf)

# Botón a la formación de Olivier Bazin en todo lo que se trata en su curso (pelvis, mujer, menopausia, visceral)
OLIVIER_PAGES = ["suelo-pelvico-dolor-pelvico", "dolor-pelvico-barcelona", "ejercicios-suelo-pelvico", "neuralgia-pudendo", "dolor-menstrual-endometriosis",
                 "dispareunia-dolor-relaciones", "dolor-coxis-coccigodinia", "cistitis-repeticion-vejiga-dolorosa", "osteopatia-embarazo-posparto",
                 "incontinencia-urinaria-esfuerzo", "prolapso-organos-pelvicos", "salud-mujer-menopausia", "sindrome-ovario-poliquistico",
                 "candidiasis-vaginal-repeticion", "acompanamiento-fertilidad", "manipulaciones-neuroviscerales", "osteopatia-visceral-barcelona",
                 "osteopatia-sarria-sant-gervasi", "osteopatia-craneosacral-barcelona", "nervio-vago",
                 "osteopatia-fascia-barcelona", "osteopatia-trauma", "cicatrices-adherencias", "osteopatia-bebes-ninos", "fisioterapia-sarria-sant-gervasi", "congestion-pelvica-sindrome-premenstrual", "trompas-salpingitis", "dolor-ovarico-quistes-ovario", "retroversion-utero", "vejiga-hiperactiva-urgencia", "cicatrices-episiotomia-cesarea", "sindrome-lacomme-dolor-pelvis-embarazo", "sindrome-ligamento-redondo", "posparto-recuperacion", "dolor-ingle-neuralgia-obturador", "lumbalgia-ciatica-origen-visceral"]
for _p in PAGES:
    if _p["slug"] in OLIVIER_PAGES:
        _p["blocks"] = [b for b in _p["blocks"] if b.get("h2") != "Para profesionales" and b.get("eyebrow") != "Para profesionales"]
        _ob = uro_pro()
        _ob["link_btn"] = ("Ver la formación de Olivier Bazin", OB_URL)
        _p["blocks"].append(_ob)
import copy as _copy
_PRIMER = _copy.deepcopy(PAGE["blocks"][1])
from new_pages import integrate_home_list as _np_home, integrate_home_areas as _np_home_areas  # noqa: E402
_np_home(PAGES)
_np_home_areas(PAGES, _PRIMER)

# Dolor persistente: enfoques que combinamos (noviembre 2026)
_ENFOQUES = [
    {"k": "Terapia manual", "h": "Osteopatía, fisioterapia y acupuntura", "p": "Para mejorar la movilidad, la función y la percepción corporal, con abordaje visceral y craneal cuando está indicado. La [acupuntura](acupuntura-medicina-tradicional-china) está recomendada como tratamiento inicial del dolor lumbar crónico por el American College of Physicians."},
    {"k": "Movimiento", "h": "Ejercicio adaptado", "p": "Recuperar fuerza y confianza en el movimiento con un programa progresivo y adaptado."},
    {"k": "Mente y cuerpo", "h": "Mindfulness (MBSR)", "p": "Programa de 8 semanas creado por Jon Kabat-Zinn en la Universidad de Massachusetts para personas con dolor crónico y estrés. El American College of Physicians lo recomienda como tratamiento inicial del dolor lumbar crónico."},
    {"k": "Hábitos saludables", "h": "Sueño, alimentación antiinflamatoria y microbiota", "p": "El descanso, la alimentación y el estado de la microbiota influyen en la inflamación y en la sensibilidad al dolor. Los trabajamos desde la [PNIE](pni-pnie-barcelona) (psiconeuroinmunoendocrinología)."},
]
for _p in PAGES:
    if _p["slug"] == "dolor-persistente-cronico":
        for _b in _p["blocks"]:
            if _b.get("h2") == "Enfoques que combinamos según tu caso":
                _b["items"] = _ENFOQUES

# Mi forma de trabajar: los mismos pasos en todas las páginas clínicas (noviembre 2026)
from new_pages import WORK_STEPS as _WS  # noqa: E402
_REPLACE_STEPS = {"Qué valoramos cuando vienes por dolor", "Cómo es la primera visita", "Cómo es la primera visita de nutrición",
                  "Cómo es la consulta de PNIE", "Cómo es una consulta de acupuntura", "Cómo es una sesión de osteopatía",
                  "Cómo es una sesión de osteopatía visceral"}
for _p in PAGES:
    if _p["group"] not in ("motivo", "servicio") or _p["slug"] in ("programas-re-trace",):
        continue
    _steps = {"type": "steps", "eyebrow": "", "h2": "Mi forma de trabajar", "intro": "Un enfoque integrativo", "items": _WS}
    _idx = [k for k, b in enumerate(_p["blocks"]) if b.get("type") in ("steps", "cards") and b.get("h2") in _REPLACE_STEPS]
    if _idx:
        _p["blocks"][_idx[0]] = _steps
        for k in reversed(_idx[1:]):
            _p["blocks"].pop(k)
    elif _p["group"] == "motivo" and not any(b.get("h2") == "Mi forma de trabajar" for b in _p["blocks"]):
        _ev = next((k for k, b in enumerate(_p["blocks"]) if b.get("type") == "evidence"), len(_p["blocks"]))
        _p["blocks"].insert(_ev, _steps)

# Osteopatía: definición de Jean-Pierre Barral
for _p in PAGES:
    if _p["slug"] == "osteopatia-sarria-sant-gervasi":
        _e = next((b for b in _p["blocks"] if b.get("type") == "explain"), None)
        if _e is not None:
            _e["quote"] = "«El concepto de la osteopatía es la movilidad: devolver movilidad al cuerpo». Jean-Pierre Barral"

# Estrés y ansiedad: relación con el nervio vago y la teoría polivagal
for _p in PAGES:
    if _p["slug"] in ("estres-ansiedad", "cortisol-estres-cronico") and not any(b.get("_id") == "nervio-vago-estres" for b in _p["blocks"]):
        _i = next((k for k, b in enumerate(_p["blocks"]) if b.get("type") == "explain"), 0) + 1
        _p["blocks"].insert(_i, {"type": "explain", "eyebrow": "", "h2": "El nervio vago y la teoría polivagal", "_id": "nervio-vago-estres",
            "paras": ["El nervio vago es la principal vía del sistema nervioso parasimpático, el que favorece la calma, la digestión y la recuperación. Cuando el estrés se mantiene en el tiempo, predomina la respuesta de alerta y el tono vagal tiende a disminuir, algo que puede reflejarse en la variabilidad de la frecuencia cardiaca.",
                      "La teoría polivagal, formulada por Stephen Porges, propone que el sistema nervioso evalúa de forma continua si el entorno es seguro y ajusta en consecuencia nuestras respuestas de calma, alerta o bloqueo. Lo explicamos con más detalle, junto con el abordaje osteopático, en [Osteopatía, nervio vago y teoría polivagal](nervio-vago)."]})

# Dolor musculoesquelético (noviembre 2026): primera visita y tres fases del tratamiento, enfoque osteopático.
# Sustituye «Mi forma de trabajar» (enfoque integrativo) y retira re:trace y acupuntura de «Cómo lo abordamos».
MSK_SLUGS = {"trocanteritis-dolor-lateral-cadera", "bursitis-subacromial-hombro", "tendinitis-rotuliana", "tenosinovitis-de-quervain", "lumbalgia-dolor-lumbar", "cervicalgia-dolor-cuello", "dorsalgia-dolor-espalda-alta", "ciatica", "hernia-disco-incipiente",
             "artrosis", "hombro-doloroso", "dolor-rodilla-condromalacia", "torticolis", "tunel-carpiano", "fascitis-plantar",
             "dolor-persistente-cronico", "dolor-musculoesqueletico", "dolor-articular-miofascial", "contracturas-desgarros-musculares",
             "esguinces", "lesiones-deportivas", "fibromialgia", "cicatrices-adherencias", "dolor-postquirurgico",
             "cefaleas-migrana", "bruxismo-dolor-mandibular-atm", "dolor-coxis-coccigodinia"}
VISIT_MSK = {"type": "visit", "eyebrow": "Primera visita", "h2": "Cómo es la primera visita", "_id": "primera-visita",
             "intro": "Antes de tratar, hay que entender qué le pasa. La primera visita dura unos 60 minutos y, si procede, el tratamiento se inicia en esa misma sesión.",
             "items": [
                 {"i": "historia", "h": "Historia clínica", "p": "Una anamnesis detallada: cómo empezó el dolor, cómo evoluciona, sus antecedentes y las pruebas e informes que aporte."},
                 {"i": "postura", "h": "Observación postural", "p": "Cómo se reparten las cargas en su cuerpo, en reposo y en movimiento."},
                 {"i": "movilidad", "h": "Exploración del movimiento", "p": "Movilidad activa y pasiva de la región dolorosa y de las zonas relacionadas con ella."},
                 {"i": "neuro", "h": "Exploración neurológica y ortopédica", "p": "Fuerza, sensibilidad, reflejos y pruebas específicas cuando están indicadas."},
                 {"i": "palpacion", "h": "Palpación y escucha manual", "p": "Palpación de los tejidos para localizar las zonas de tensión, restricción y dolor, según el enfoque de Jean-Pierre Barral."},
                 {"i": "dialogo", "h": "Explicación y plan", "p": "Le explicamos lo que hemos encontrado, el tratamiento que proponemos y lo que puede esperar."}],
             "note": "Si detectamos alguna señal que requiera valoración médica, se lo indicamos antes de iniciar el tratamiento."}
PHASES_MSK = {"type": "phases", "eyebrow": "Tratamiento", "h2": "Las tres fases del tratamiento", "_id": "fases-del-tratamiento",
              "intro": "El tratamiento es conservador y progresivo. La duración de cada fase depende del caso, del tiempo de evolución y de la respuesta de cada paciente.",
              "items": [
                  {"h": "Fase de alivio", "paras": ["El objetivo es reducir el dolor y la sensibilidad de los tejidos y recuperar el movimiento perdido. En esta fase las sesiones suelen estar más próximas entre sí.",
                                                   "Se acompaña de pautas sencillas para el día a día: cómo moverse, qué posturas evitar y cuándo aplicar calor."]},
                  {"h": "Fase de recuperación", "paras": ["Con el dolor más controlado, las sesiones se espacian. Se trabaja la movilidad de las zonas relacionadas y se incorpora ejercicio terapéutico progresivo de movilidad, control motor y fuerza.",
                                                         "El objetivo es que la región recupere su función y que usted vuelva a sus actividades con confianza."]},
                  {"h": "Fase de mantenimiento", "paras": ["Una vez resuelto el episodio, el objetivo es prevenir las recaídas. Recibe pautas de ejercicio y de hábitos para mantener lo conseguido.",
                                                          "Si lo necesita, se programan revisiones espaciadas."]}]}
import re as _re  # noqa: E402
_BAD = _re.compile(r"(?i)re:trace|acupunt|mindfulness|MBSR")
for _p in PAGES:
    if _p["slug"] not in MSK_SLUGS:
        continue
    _bl = _p["blocks"]
    _k = next((k for k, b in enumerate(_bl) if b.get("h2") == "Mi forma de trabajar"), None)
    if _k is not None:
        _bl[_k:_k + 1] = [dict(VISIT_MSK), dict(PHASES_MSK)]
    else:
        _ev = next((k for k, b in enumerate(_bl) if b.get("type") == "evidence"), len(_bl))
        _bl[_ev:_ev] = [dict(VISIT_MSK), dict(PHASES_MSK)]
    for _b in _bl:
        if _b.get("type") == "cards" and _b.get("items"):
            _b["items"] = [it for it in _b["items"] if not _BAD.search(" ".join(str(it.get(x, "")) for x in ("k", "h", "p")))]
    _bl[:] = [b for b in _bl if not (b.get("type") == "cards" and not b.get("items") and b.get("_id") != "datos-clave")]

# Osteopatía (25 nov 2026): estructura de clínica (qué es, qué hace un osteópata, para quién, primera visita, fases, técnicas)
OSTEO_BLOCKS = [
    {"type": "explain", "eyebrow": "Qué es", "h2": "¿Qué es la osteopatía?", "_id": "que-es-la-osteopatia",
     "quote": "«El concepto de la osteopatía es la movilidad: devolver movilidad al cuerpo». Jean-Pierre Barral",
     "paras": [
         "La osteopatía es una disciplina de terapia manual que valora y trata las alteraciones de la movilidad de los tejidos del cuerpo: articulaciones, músculos, fascias, vísceras, nervios y vasos. Parte de una idea sencilla: las estructuras del cuerpo están relacionadas entre sí, y cuando una pierde movilidad, las demás se adaptan y pueden aparecer dolor o alteraciones de la función.",
         "Fue fundada en 1874 por el médico estadounidense Andrew Taylor Still, que en 1892 abrió en Kirksville (Misuri) la primera escuela de osteopatía. Con el tiempo se desarrollaron tres grandes enfoques: el estructural, centrado en el sistema musculoesquelético; el visceral, sistematizado por Jean-Pierre Barral; y el craneal, iniciado por William Garner Sutherland y desarrollado después por John Upledger.",
         "La Organización Mundial de la Salud publicó en 2010 unas directrices sobre la formación y la seguridad en osteopatía, que la describen como un abordaje centrado en el contacto manual para el diagnóstico y el tratamiento."]},
    {"type": "explain", "eyebrow": "", "h2": "¿Qué hace un osteópata?", "_id": "que-hace-un-osteopata",
     "paras": [
         "Antes de cualquier técnica, el osteópata necesita entender por qué aparece el dolor o la disfunción. Por eso la consulta empieza con una **anamnesis** detallada y una **exploración**: observación de la postura, pruebas de movilidad, pruebas neurológicas y ortopédicas cuando están indicadas y, sobre todo, la **palpación**.",
         "Jean-Pierre Barral llama a esta palpación **escucha manual**: las manos buscan diferencias de tensión, densidad, movilidad y temperatura en los tejidos para localizar la zona que necesita ser tratada y precisar qué estructura está implicada. A menudo el lugar donde duele no es el origen del problema: un dolor de hombro puede relacionarse con la columna cervical, el diafragma o una cicatriz abdominal.",
         "A partir de esa valoración, el osteópata elige las técnicas manuales adecuadas para cada tejido y cada persona, y las combina con pautas y ejercicios para que la mejoría se mantenga. Si detecta algo que requiere valoración médica, deriva al paciente a su médico."]},
    {"type": "audience", "eyebrow": "Para quién", "h2": "¿Para quién es la osteopatía?", "_id": "para-quien",
     "intro": "La osteopatía se adapta a cada edad y a cada etapa de la vida. Las técnicas, la intensidad y la duración de la sesión cambian según la persona.",
     "items": [
         {"h": "Bebés y niños", "paras": [
             "En los bebés se utilizan técnicas muy suaves, adaptadas a sus tejidos. Las consultas más frecuentes son el **cólico del lactante**, los gases y la irritabilidad, las dificultades de succión o de lactancia, la **tortícolis congénita** y la **plagiocefalia postural** (el aplanamiento de una zona de la cabeza). Una revisión sistemática con metaanálisis observó que la terapia manual reducía el tiempo de llanto en los bebés con llanto excesivo (Carnes et al., BMJ Open, 2018).",
             "En niños y adolescentes se consulta por dolor de espalda, alteraciones posturales, lesiones deportivas o dolores de cabeza. Siempre trabajamos en coordinación con el pediatra. Más información en [osteopatía en bebés y niños](osteopatia-bebes-ninos)."]},
         {"h": "Embarazo y posparto", "paras": [
             "Durante el embarazo cambian el centro de gravedad, la curvatura lumbar y la laxitud de los ligamentos, y es frecuente el dolor lumbar y de la cintura pélvica. Un metaanálisis encontró que el tratamiento osteopático reducía el dolor y mejoraba la función en las mujeres embarazadas con dolor lumbar (Franke et al., Journal of Bodywork and Movement Therapies, 2017).",
             "En el posparto, la osteopatía acompaña la recuperación de la pelvis y del abdomen, la cicatriz de la cesárea y los dolores de espalda y de cuello asociados al cuidado del bebé. Más información en [osteopatía en el embarazo y el posparto](osteopatia-embarazo-posparto)."]},
         {"h": "Adultos", "paras": [
             "Es el grupo que más consulta, sobre todo por dolor de espalda y de cuello, ciática, dolores de cabeza, problemas de la mandíbula, molestias digestivas funcionales, cicatrices y adherencias, o tensión asociada al estrés."],
          "list": ["[Lumbalgia](lumbalgia-dolor-lumbar) y [cervicalgia](cervicalgia-dolor-cuello)", "[Ciática](ciatica) y [hernia discal](hernia-disco-incipiente)",
                   "[Cefaleas y migraña](cefaleas-migrana) y [bruxismo](bruxismo-dolor-mandibular-atm)", "[Osteopatía visceral](osteopatia-visceral-barcelona) para molestias digestivas funcionales",
                   "[Cicatrices y adherencias](cicatrices-adherencias)"]},
         {"h": "Deportistas", "paras": [
             "En el deporte, la osteopatía ayuda a recuperar la movilidad después de un esguince, una contractura o una sobrecarga, a tratar las lesiones que se repiten y a revisar las cadenas de movimiento que las favorecen. Se combina con la readaptación y el ejercicio progresivo. Más información en [lesiones deportivas](lesiones-deportivas)."]},
         {"h": "Personas mayores", "paras": [
             "Con la edad aparecen la rigidez, la artrosis y la pérdida de movilidad. En las personas mayores se utilizan técnicas suaves, sin manipulaciones bruscas, adaptadas a la artrosis o a la osteoporosis, con el objetivo de aliviar el dolor y mantener la movilidad y la autonomía. Más información en [artrosis](artrosis)."]}]},
    {"type": "visit", "eyebrow": "Primera visita", "h2": "Cómo es la primera visita", "_id": "primera-visita",
     "intro": "La primera visita dura unos 60 minutos. Antes de tratar, hay que entender qué le pasa.",
     "items": [
         {"i": "historia", "h": "Historia clínica", "p": "Una anamnesis detallada: el motivo de consulta, cómo ha evolucionado, sus antecedentes y las pruebas e informes que aporte."},
         {"i": "postura", "h": "Observación postural", "p": "Cómo se reparten las cargas en su cuerpo, en reposo y en movimiento."},
         {"i": "movilidad", "h": "Exploración del movimiento", "p": "Movilidad activa y pasiva de la región que duele y de las zonas relacionadas."},
         {"i": "neuro", "h": "Pruebas neurológicas y ortopédicas", "p": "Fuerza, sensibilidad, reflejos y pruebas específicas cuando están indicadas."},
         {"i": "palpacion", "h": "Palpación y escucha manual", "p": "La palpación de los tejidos, según el enfoque de Jean-Pierre Barral, para localizar las zonas de restricción."},
         {"i": "plan", "h": "Primer tratamiento y plan", "p": "Si procede, se realiza el primer tratamiento y le explicamos el plan y las pautas para casa."}],
     "note": "Si detectamos alguna señal que requiera valoración médica, se lo indicamos antes de iniciar el tratamiento."},
    {"type": "phases", "eyebrow": "Tratamiento", "h2": "Las tres fases del tratamiento", "_id": "fases-del-tratamiento",
     "intro": "El número de sesiones y su frecuencia dependen del caso, del tiempo de evolución y de la respuesta de cada paciente.",
     "items": [
         {"h": "Fase de alivio", "paras": ["El objetivo es reducir el dolor y recuperar el movimiento perdido. Las sesiones suelen estar más próximas entre sí, porque los tejidos todavía no mantienen los cambios.",
                                          "Muchas personas notan una mejoría desde las primeras sesiones, aunque la recuperación completa requiere tiempo, según la gravedad y la duración del problema."]},
         {"h": "Fase de recuperación", "paras": ["Las sesiones se espacian. Se trabaja la movilidad de las zonas relacionadas con el problema y se incorpora ejercicio progresivo para recuperar la función, la fuerza y la confianza en el movimiento."]},
         {"h": "Fase de mantenimiento", "paras": ["Una vez resuelto el episodio, el objetivo es prevenir las recaídas. Recibe pautas de ejercicio y de hábitos y, si lo necesita, se programan revisiones espaciadas."]}]},
    {"type": "techniques", "h2": "Técnicas osteopáticas", "_id": "tecnicas-osteopaticas",
     "paras": ["La osteopatía dispone de técnicas muy diversas, desde movilizaciones articulares hasta técnicas muy suaves sobre las vísceras, las fascias o el cráneo. La técnica o técnicas se eligen en cada caso **después de la valoración**, según el tejido implicado, la edad y el estado de cada persona."],
     "list_title": "Enfoques que utilizamos en WA LAM",
     "items": ["**Osteopatía estructural**, la base de la osteopatía de Andrew Taylor Still: articulaciones, músculos y ligamentos.",
               "**[Osteopatía visceral](osteopatia-visceral-barcelona)**, desarrollada por Jean-Pierre Barral: movilidad de las vísceras y de sus fascias.",
               "**[Manipulaciones neuroviscerales](manipulaciones-neuroviscerales)** y manipulación neural, también de la línea de Barral.",
               "**[Osteopatía craneosacral](osteopatia-craneosacral-barcelona)**, iniciada por William Garner Sutherland y desarrollada por John Upledger.",
               "**[Osteopatía fascial y liberación miofascial](osteopatia-fascia-barcelona)**.",
               "**Osteopatía urogenital con abordaje externo**, en la línea de Jean-Pierre Barral y Olivier Bazin, para el [dolor pélvico](dolor-pelvico-barcelona) en la mujer."]},
]
OSTEO_EVIDENCE = {"type": "evidence", "h2": "Qué dice la evidencia", "items": [
    ("Metaanálisis (BMJ)", "En el dolor lumbar crónico, la terapia manipulativa vertebral obtuvo efectos similares a los de los tratamientos recomendados y mejoró la función a corto plazo (Rubinstein et al., 2019; 47 ensayos)."),
    ("Metaanálisis (BMC Musculoskeletal Disorders)", "El tratamiento osteopático manipulativo redujo el dolor y mejoró la función en el dolor lumbar inespecífico (Franke et al., 2014)."),
    ("Metaanálisis (Int J Osteopath Med)", "El tratamiento osteopático redujo el dolor en la cervicalgia crónica inespecífica (Franke et al., 2015)."),
    ("Embarazo (J Bodyw Mov Ther)", "En el dolor lumbar del embarazo, el tratamiento osteopático redujo el dolor y mejoró la función (Franke et al., 2017)."),
    ("Bebés (BMJ Open)", "La terapia manual redujo el tiempo de llanto en los bebés con llanto excesivo (Carnes et al., 2018).")],
    "refs": [
        {"t": "Rubinstein SM, de Zoete A, van Middelkoop M, et al., 2019. «Benefits and harms of spinal manipulative therapy for the treatment of chronic low back pain: systematic review and meta-analysis of randomised controlled trials». BMJ.", "doi": "10.1136/bmj.l689"},
        {"t": "Franke H, Franke JD, Fryer G, 2014. «Osteopathic manipulative treatment for nonspecific low back pain: a systematic review and meta-analysis». BMC Musculoskeletal Disorders.", "doi": "10.1186/1471-2474-15-286"},
        {"t": "Franke H, Franke JD, Fryer G, 2015. «Osteopathic manipulative treatment for chronic nonspecific neck pain: a systematic review and meta-analysis». International Journal of Osteopathic Medicine.", "doi": "10.1016/j.ijosm.2015.05.003"},
        {"t": "Franke H, Franke JD, Belz S, Fryer G, 2017. «Osteopathic manipulative treatment for low back and pelvic girdle pain during and after pregnancy: a systematic review and meta-analysis». Journal of Bodywork and Movement Therapies.", "doi": "10.1016/j.jbmt.2017.05.014"},
        {"t": "Carnes D, Plunkett A, Ellwood J, Miles C, 2018. «Manual therapy for unsettled, distressed and excessively crying infants: a systematic review and meta-analyses». BMJ Open.", "doi": "10.1136/bmjopen-2017-019040"}]}
for _p in PAGES:
    if _p["slug"] != "osteopatia-sarria-sant-gervasi":
        continue
    _old = _p["blocks"]
    _mirror = next((b for b in _old if b.get("type") == "mirror"), None)
    _keep = [b for b in _old if b.get("type") == "pro" or (b.get("type") == "explain" and "Olivier Bazin" in b.get("h2", ""))]
    _nb = OSTEO_BLOCKS[:3] + ([_mirror] if _mirror else []) + OSTEO_BLOCKS[3:] + [b for b in _keep if b.get("type") == "pro"] + [OSTEO_EVIDENCE] + [b for b in _keep if b.get("type") != "pro"]
    _p["blocks"] = _nb
    _p["lead"] = "La osteopatía es una disciplina de terapia manual que valora y trata la movilidad de los tejidos del cuerpo: articulaciones, músculos, fascias, vísceras y sistema nervioso. Cada tratamiento parte de una anamnesis y una exploración palpatoria detalladas."
    _p["sub"] = "Osteopatía estructural, visceral y craneosacral · Barcelona"

# Ilustraciones propias (25 nov 2026): (figura, fragmento del H2 tras el que va, pie)
FIG_PLACE = {
    "osteopatia-sarria-sant-gervasi": [("columna_organos", "¿Qué hace un osteópata?", "Cada nivel de la columna se relaciona con órganos concretos a través del sistema nervioso autónomo."),
                                       ("menos_mas", "Las tres fases", "")],
    "osteopatia-visceral-barcelona": [("columna_organos", "víscera", "Niveles de la columna relacionados con cada órgano.")],
    "cervicalgia-dolor-cuello": [("cabeza_adelantada", "cabeza adelantada", ""), ("cabeza_adelantada_zonas", "cabeza adelantada", "")],
    "cefaleas-migrana": [("cabeza_adelantada_zonas", "postura", "")],
    "ciatica": [("nervio_ciatico", "¿Qué es", ""), ("disco_progresion", "ernia", ""), ("sintomas_compresion", "ernia", "")],
    "lumbalgia-dolor-lumbar": [("disco_progresion", "ernia", ""), ("sintomas_compresion", "ernia", ""), ("eje_intestino_disco", "icrobiota", "")],
    "hernia-disco-incipiente": [("disco_progresion", "¿Qué es", ""), ("sintomas_compresion", "fectos", ""), ("eje_intestino_disco", "icrobiota", "")],
    "salud-digestiva-microbiota": [("eje_intestino_disco", "dolor de espalda", ""), ("escala_bristol", "heces", "")],
    "diarrea-cronica": [("escala_bristol", "¿Qué es", "")],
    "estrenimiento": [("escala_bristol", "¿Qué es", "")],
    "colon-irritable-sibo": [("escala_bristol", "¿Qué es", "")],
    "pni-pnie-barcelona": [("eje_intestino_disco", "dolor de espalda", ""), ("estados_sna", "simpático", "")],
    "nervio-vago": [("nervio_vago_anatomia", "¿Qué es", ""), ("nervio_vago_funciones", "¿Qué hace", ""),
                    ("estados_sna", "polivagal", ""), ("nervio_vago_social", "implicación social", ""),
                    ("nervio_vago_metodos", "estimular", "")],
    "estres-ansiedad": [("estados_sna", "¿Qué es", "")],
    "sueno-insomnio": [("nervio_vago_metodos", "prevenir", "")],
}


def _place_figs():
    for _p in PAGES:
        for fig, frag, cap in FIG_PLACE.get(_p["slug"], []):
            bl = _p["blocks"]
            k = next((i for i, b in enumerate(bl) if frag.lower() in str(b.get("h2", "")).lower()), None)
            if k is None:
                continue
            j = k + 1
            while j < len(bl) and bl[j].get("type") == "figure":
                j += 1
            bl.insert(j, {"type": "figure", "fig": fig, "caption": cap, "_id": f"fig-{fig}"})



# Apartados añadidos a páginas existentes (material de Rosa, 25 nov 2026)
def _extra_sections():
    import json as _j
    from pathlib import Path as _P
    fx = _P(__file__).with_name("new_pages") / "extra_sections.json"
    if not fx.exists():
        return
    ex = _j.loads(fx.read_text(encoding="utf-8"))
    for _p in PAGES:
        e = ex.get(_p["slug"])
        if not e:
            continue
        bl = _p["blocks"]
        have = " ".join(str(b.get("h2", "")).lower() for b in bl)
        new = []
        for sec in e.get("sections", []):
            if sec["h2"].lower() in have or ("víscera" in sec["h2"].lower() and "víscera" in have):
                continue
            blk = {"type": "explain", "eyebrow": "", "h2": sec["h2"], "paras": sec.get("paras", [])}
            if sec.get("list"):
                blk["list_title"] = sec.get("list_title", ""); blk["list"] = sec["list"]
            new.append(blk)
        k = next((i for i, b in enumerate(bl) if b.get("type") in ("visit", "phases", "steps", "pro", "evidence")), len(bl))
        bl[k:k] = new
        ev = next((b for b in bl if b.get("type") == "evidence"), None)
        if ev is not None:
            ev["items"] = list(ev.get("items", [])) + [tuple(x) for x in e.get("evidence_items", [])]
            dois = {r.get("doi") for r in ev.get("refs", []) if isinstance(r, dict)}
            ev["refs"] = list(ev.get("refs", [])) + [r for r in e.get("refs", []) if r.get("doi") not in dois]


_extra_sections()
_place_figs()

# Títulos en forma de pregunta (25 nov 2026), en dolencias, microbiota y osteopatía
from h2_questions import to_question as _toq  # noqa: E402
for _p in PAGES:
    if _p["group"] not in ("motivo", "servicio"):
        continue
    for _b in _p["blocks"]:
        if _b.get("h2"):
            _b["h2"] = _toq(_p["slug"], _b["h2"])

# Medicina integrativa (25 nov 2026, revisión de Rosa): sin repeticiones
for _p in PAGES:
    if _p["slug"] != "medicina-integrativa-barcelona":
        continue
    _bl = _p["blocks"]
    for _b in _bl:
        if _b.get("_id") == "que-es-la-medicina-integrativa":
            _b["list_title"] = "Le ayudamos a"
            _b["list"] = list(_p.get("facts", []))
    _5p = next((b for b in _bl if b.get("h2") == "Basada en la medicina 5P"), None)
    for _b in _bl:
        if _b.get("_id") == "slow-medicine" and _5p:
            _b["intro"] = "Una medicina sin prisas: tiempo para escucharle, entender su historia y explicarle qué ocurre y por qué. Basada en los cinco principios de la medicina 5P."
            _b["items"] = [dict(it) for it in _5p["items"]]
        if _b.get("h2") == "¿Por qué WA LAM?":
            _b["items"] = [it for it in _b["items"] if it["h"] not in ("Abordaje personalizado", "Una visión médica integrativa", "Método re:trace")]
    _bl[:] = [b for b in _bl if b.get("_id") != "te-ayudamos" and b.get("h2") not in ("Del primer contacto a un plan claro", "Basada en la medicina 5P")]

# Osteopatía (Rosa, 25 nov 2026): botones a bebés y niños, fascia y trauma dentro de la página
for _p in PAGES:
    if _p["slug"] == "osteopatia-sarria-sant-gervasi":
        _bl = _p["blocks"]
        _k = next((i for i, b in enumerate(_bl) if b.get("type") == "techniques"), len(_bl) - 1) + 1
        _bl.insert(_k, {"type": "chips", "eyebrow": "Más sobre osteopatía", "h2": "Osteopatía para cada necesidad", "_id": "mas-osteopatia",
                        "items": [("Osteopatía en bebés y niños", "osteopatia-bebes-ninos"), ("Fascia y liberación miofascial", "osteopatia-fascia-barcelona"),
                                  ("Trauma físico y emocional", "osteopatia-trauma")]})

# Rosa (25 nov 2026): el nombre del botón (nav) igual que en la lista de medicina integrativa
_NAV_FIX = {"hernia-disco-incipiente": "Hernias de disco incipientes y protrusión",
            "dolor-rodilla-condromalacia": "Dolor de rodilla y condromalacia rotuliana",
            "tunel-carpiano": "Síndrome del túnel carpiano",
            "osteoporosis": "Osteoporosis y salud ósea",
            "bruxismo-dolor-mandibular-atm": "Bruxismo, dolor mandibular y ATM",
            "contracturas-desgarros-musculares": "Contracturas y desgarros musculares"}
for _p in PAGES:
    if _p["slug"] in _NAV_FIX:
        _p["nav"] = _NAV_FIX[_p["slug"]]

# ── Dolor crónico: enlaces a las tres osteopatías (Rosa, 25 nov 2026) ──
for _p in PAGES:
    if _p["slug"] != "dolor-persistente-cronico":
        continue
    for _b in _p["blocks"]:
        if _b.get("h2", "").startswith("¿Cómo se entiende el dolor crónico desde la osteopatía?"):
            _b["paras"] = [x.replace("Puede leer más en nuestra página de [osteopatía visceral](osteopatia-visceral-barcelona).",
                "Puede leer más en nuestras páginas de [osteopatía](osteopatia-sarria-sant-gervasi), [osteopatía craneosacral](osteopatia-craneosacral-barcelona) y [osteopatía visceral](osteopatia-visceral-barcelona).")
                for x in _b["paras"]]

# ── Orden lógico de las secciones en todas las landings (Rosa, 25 nov 2026) ──
# Qué es → síntomas → visión osteopática → diagnóstico y exploración → tratamiento → primera visita → fases
# → frecuencia, causas, riesgo, tipos y mecanismos (orden original) → cuándo consultar al médico → prevención → resto
import unicodedata as _ud2
def _norm(t):
    return _ud2.normalize("NFD", t).encode("ascii", "ignore").decode().lower().strip()
def _rank(b, first_explain):
    t, h = b.get("type"), _norm(b.get("h2", ""))
    S = lambda *k: h.startswith(k)
    if b is first_explain: return 0
    if t == "mirror" or S("se reconoce", "le suena", "cuales son los sintomas", "que sintomas"): return 1
    if "para quien" in h or S("beneficios"): return 1.5
    if "desde la osteopatia" in h or S("y si el dolor viene", "puede un dolor de", "puede el dolor venir de una viscera", "por que el osteopata"): return 2
    if S("como se diagnostica", "como se valora", "como se explora", "que se explora", "que aporta la exploracion"): return 3
    if S("por que es importante entender"): return 3.5
    if S("como se trata", "como se trabaja", "como lo abordamos", "mi forma de trabajar", "como es una sesion") or t == "techniques": return 4
    if t == "visit": return 5
    if t == "phases": return 6
    if S("cuando debo consultar"): return 8
    if S("que puedo hacer", "se puede prevenir", "como se puede prevenir", "como prevenir"): return 9
    if t in ("evidence", "pro", "pack") or S("formacion en osteopatia", "estudios de referencia", "precio", "modalidades", "precauciones", "que modalidades", "que precauciones"): return 10
    if S("es frecuente", "son frecuentes"): return 7.0
    if S("por que aparece", "por que duele", "por que se produce", "que lo causa", "cuales son las causas"): return 7.1
    if S("quien tiene mas riesgo"): return 7.2
    if S("puede complicarse"): return 7.3
    return 7.5
for _p in PAGES:
    if _p.get("group") == "home" or not _p.get("blocks"):
        continue
    # cada figura viaja pegada al bloque que la precede
    _units = []
    for _b in _p["blocks"]:
        if _b.get("type") == "figure" and _units:
            _units[-1].append(_b)
        else:
            _units.append([_b])
    _fe = next((u[0] for u in _units if u[0].get("type") == "explain"), None)
    _units = sorted(enumerate(_units), key=lambda iu: (_rank(iu[1][0], _fe), iu[0]))
    _p["blocks"] = [b for _, u in _units for b in u]

# Rosa (25 nov 2026): fuera «¿Cómo es la primera visita?» (ya se explica en diagnóstico/exploración)
# y fuera el precio en las páginas de motivos de consulta.
for _p in (PAGES if isinstance(PAGES, list) else PAGES.values()):
    if _p.get("group") == "home":
        continue
    _p["blocks"] = [b for b in _p.get("blocks", []) if b.get("type") != "visit"]
    if _p.get("group") == "motivo":
        for _b in _p["blocks"]:
            if _b.get("type") == "pro" and _b.get("rows"):
                _b["rows"] = [r for r in _b["rows"] if "Precio" not in str(r) and "Preu" not in str(r)]


# Rosa (26 nov 2026): botones de mindfulness (curso MBSR, formación RE:TRACE de 9 meses, retiros) tras «¿Qué modalidades hay?»
for _p in (PAGES if isinstance(PAGES, list) else PAGES.values()):
    if _p.get("slug") != "mindfulness-barcelona":
        continue
    _i = next((k for k, b in enumerate(_p["blocks"]) if b.get("h2", "").startswith("¿Qué modalidades")), None)
    if _i is not None:
        _p["blocks"].insert(_i + 1, {"type": "chips", "eyebrow": "", "h2": "¿Por dónde quiere empezar?", "items": [
            ("Curso MBSR de 8 semanas, en directo por Zoom", "curso-mindfulness-mbsr-barcelona"),
            ("Formación RE:TRACE de 9 meses", "formacion-re-trace"),
            ("Retiros de meditación y silencio", "retiros-mindfulness-meditacion-silencio")]})

# Rosa (26 nov 2026): material del blog de traumatología (sin cirugía ni casos) → nuevas secciones en páginas existentes
import json as _jx  # noqa: E402
from pathlib import Path as _P  # noqa: E402
_MX = _jx.loads((_P(__file__).with_name("new_pages") / "msk_extra_sections.json").read_text(encoding="utf-8"))
_DROP = ("Abríguese bien las articulaciones que más le molestan: rodilleras", "Aplique calor local", "Postura del niño")
_REPL = {"Cuando la herida esté cerrada, masajee suavemente la cicatriz": "Cuando ya no haya puntos ni costras, masajee la cicatriz en seco unos minutos al día, en zigzag, a lo largo y de forma transversal, insistiendo donde la piel no se desliza.",
         "Proteja la cicatriz del sol con ropa o protector solar alto": "Proteja la cicatriz del sol cubriéndola con ropa durante el primer año."}
for _p in PAGES:
    for _b in _p["blocks"]:
        if isinstance(_b.get("list"), list):
            pass  # Rosa (26 nov): crema, protector solar, rodilleras, plantillas, frío/calor y postura del niño SÍ se ponen
    _x = _MX.get(_p["slug"])
    if not _x:
        continue
    _new = []
    for _s in _x.get("sections", []):
        _bk = {"type": "explain", "eyebrow": "", "h2": _s["h2"], "paras": _s.get("paras", [])}
        if _s.get("list"):
            _bk["list_title"] = _s.get("list_title", ""); _bk["list"] = _s["list"]
        _new.append(_bk)
    _bl = _p["blocks"]
    _k = next((k for k, b in enumerate(_bl) if _norm(b.get("h2", "")).startswith(("cuando debo consultar", "que puedo hacer", "se puede prevenir"))), None)
    if _k is None:
        _k = next((k for k, b in enumerate(_bl) if b.get("type") in ("evidence", "pro", "pack")), len(_bl))
    _bl[_k:_k] = _new
    if _x.get("faq"):
        _p["faq"] = list(_p.get("faq", [])) + [tuple(q) for q in _x["faq"]]
    _ev = next((b for b in _bl if b.get("type") == "evidence"), None)
    if _ev is not None and _x.get("evidence_add"):
        _ev["items"] = list(_ev["items"]) + [tuple(i) for i in _x["evidence_add"]]
        _ev["refs"] = list(_ev.get("refs", [])) + _x.get("refs_add", [])

# Rosa (26 nov 2026): en musculoesquelético el abordaje de WA LAM es fisioterapia y osteopatía, con botones a esas páginas
for _p in PAGES:
    if _p["slug"] not in MSK_SLUGS:
        continue
    _bl = _p["blocks"]
    _k = next((k for k, b in enumerate(_bl) if _norm(b.get("h2", "")).startswith(("como se trata", "como se trabaja"))), None)
    if _k is None:
        _k = next((k for k, b in enumerate(_bl) if b.get("type") in ("visit", "phases")), 0) - 1
    _bl.insert(_k + 1, {"type": "chips", "eyebrow": "Nuestro abordaje", "h2": "¿Cómo lo abordamos en WA LAM?",
                        "intro": "En WA LAM, el dolor musculoesquelético se aborda con fisioterapia y osteopatía.",
                        "items": [("Fisioterapia", "fisioterapia-sarria-sant-gervasi"), ("Osteopatía", "osteopatia-sarria-sant-gervasi"),
                                  ("Osteopatía craneosacral", "osteopatia-craneosacral-barcelona"), ("Osteopatía visceral", "osteopatia-visceral-barcelona")]})


# Rosa (26 nov 2026): la página de suelo pélvico pasa a ser la página general de salud pélvica (libro de Olivier Bazin)
import json as _jz  # noqa: E402
_hub = next((d for d in _jz.loads((_P(__file__).with_name("new_pages") / "batchZZ4.json").read_text(encoding="utf-8"))), None)
for _p in PAGES:
    if _hub and _p["slug"] == "suelo-pelvico-dolor-pelvico":
        for _k in ("h1", "nav", "sub", "title", "desc", "lead", "card"):
            _p[_k] = _hub[_k]
        _p["blocks"] = [b for b in _p["blocks"] if b.get("_id") != "tambien-salud-pelvica" and b.get("eyebrow") != "Para profesionales" and b.get("h2") not in ("Para profesionales", "Formación en osteopatía urogenital con Olivier Bazin", "Mi forma de trabajar")]
        if not any(b.get("type") == "evidence" for b in _p["blocks"]):
            _ev = _hub["evidence"]
            _k = next((k for k, b in enumerate(_p["blocks"]) if b.get("type") == "pro"), len(_p["blocks"]))
            _p["blocks"].insert(_k, {"type": "evidence", "h2": _ev.get("h2", "¿Qué dice la evidencia?"), "items": [tuple(x) for x in _ev["items"]], "refs": _ev.get("refs", [])})


# Rosa (26 nov 2026): páginas ligeras de salud pélvica (libro de Olivier Bazin): abordaje con osteopatía y fisioterapia
PELVIC_LIGHT = ['congestion-pelvica-sindrome-premenstrual', 'trompas-salpingitis', 'dolor-ovarico-quistes-ovario', 'retroversion-utero', 'vejiga-hiperactiva-urgencia', 'cicatrices-episiotomia-cesarea', 'sindrome-lacomme-dolor-pelvis-embarazo', 'sindrome-ligamento-redondo', 'posparto-recuperacion', 'dolor-ingle-neuralgia-obturador', 'lumbalgia-ciatica-origen-visceral']
for _p in PAGES:
    if _p["slug"] not in PELVIC_LIGHT:
        continue
    _bl = _p["blocks"]
    _k = next((k for k, b in enumerate(_bl) if _norm(b.get("h2", "")).startswith("que se busca con el tratamiento")), None)
    if _k is None:
        _k = next((k for k, b in enumerate(_bl) if b.get("type") == "explain"), 0)
    _bl.insert(_k + 1, {"type": "chips", "eyebrow": "Nuestro abordaje", "h2": "¿Cómo lo abordamos en WA LAM?",
                        "intro": "En WA LAM, la salud pélvica se aborda con osteopatía y fisioterapia.",
                        "items": [("Osteopatía", "osteopatia-sarria-sant-gervasi"), ("Osteopatía visceral", "osteopatia-visceral-barcelona"),
                                  ("Osteopatía craneosacral", "osteopatia-craneosacral-barcelona"), ("Fisioterapia", "fisioterapia-sarria-sant-gervasi")]})


# Rosa (27 nov 2026): en las páginas de salud pélvica (abordaje con osteopatía y fisioterapia) no va «Mi forma de trabajar»
PELVIC_OSTEO = PELVIC_LIGHT + ["suelo-pelvico-dolor-pelvico", "neuralgia-pudendo", "incontinencia-urinaria-esfuerzo", "cistitis-repeticion-vejiga-dolorosa",
                               "prolapso-organos-pelvicos", "dispareunia-dolor-relaciones", "dolor-menstrual-endometriosis", "dolor-coxis-coccigodinia",
                               "dolor-pelvico-barcelona", "osteopatia-embarazo-posparto", "acompanamiento-fertilidad", "ejercicios-suelo-pelvico"]
for _p in PAGES:
    if _p["slug"] in PELVIC_OSTEO:
        _p["blocks"] = [b for b in _p["blocks"] if b.get("h2") != "Mi forma de trabajar"]

VISIT_PEL = {"type": "visit", "eyebrow": "Primera visita", "h2": "Cómo es la primera visita", "_id": "primera-visita",
             "intro": "Antes de tratar, hay que entender qué le pasa. La primera visita dura unos 60 minutos y, si procede, el tratamiento se inicia en esa misma sesión. El abordaje es siempre externo.",
             "items": [
                 {"i": "historia", "h": "Historia clínica", "p": "Una anamnesis detallada: cómo empezaron las molestias, su relación con el ciclo, los embarazos y partos, las cirugías e infecciones previas, y las pruebas e informes que aporte."},
                 {"i": "postura", "h": "Observación postural", "p": "La postura de la pelvis, la columna y la respiración, en reposo y en movimiento."},
                 {"i": "movilidad", "h": "Movilidad de la pelvis", "p": "Movilidad del sacro, el cóccix, las caderas, la zona lumbar y el abdomen."},
                 {"i": "palpacion", "h": "Palpación y escucha manual", "p": "Palpación externa del abdomen y la pelvis para localizar las zonas de tensión y de restricción de movilidad de los órganos y sus ligamentos."},
                 {"i": "dialogo", "h": "Explicación y plan", "p": "Le explicamos lo que hemos encontrado, el tratamiento que proponemos y lo que puede esperar."}],
             "note": "Si detectamos alguna señal que requiera valoración médica o ginecológica, se lo indicamos antes de iniciar el tratamiento."}
PHASES_PEL = {"type": "phases", "eyebrow": "Tratamiento", "h2": "Las tres fases del tratamiento", "_id": "fases-del-tratamiento",
              "intro": "El tratamiento es suave y progresivo. La duración de cada fase depende del caso, del tiempo de evolución y de la respuesta de cada paciente.",
              "items": [
                  {"h": "Fase de alivio", "paras": ["El objetivo es reducir las molestias y devolver la movilidad a las zonas más restringidas. Las primeras sesiones suelen estar más próximas entre sí, idealmente la semana siguiente a la regla."]},
                  {"h": "Fase de recuperación", "paras": ["Con las molestias más controladas, las sesiones se espacian. Se trabajan las relaciones de la pelvis con el abdomen, la columna y el resto del cuerpo, y se incorporan pautas de hábitos y de movimiento."]},
                  {"h": "Fase de mantenimiento", "paras": ["El objetivo es mantener lo conseguido y prevenir recaídas, sobre todo en las etapas de cambio hormonal: embarazo, posparto y menopausia. Si lo necesita, se programan revisiones espaciadas."]}]}
for _p in PAGES:
    if _p["slug"] not in PELVIC_OSTEO or _p["slug"] == "suelo-pelvico-dolor-pelvico":
        continue
    _bl = _p["blocks"]
    if any(b.get("type") in ("visit", "phases") for b in _bl):
        continue
    _k = next((k for k, b in enumerate(_bl) if b.get("type") == "chips"), None)
    if _k is None:
        _k = next((k for k, b in enumerate(_bl) if _norm(b.get("h2", "")).startswith(("que se busca", "como se trata", "como se trabaja", "que busca"))), None)
    if _k is None:
        _k = next((k for k, b in enumerate(_bl) if b.get("type") == "evidence"), len(_bl)) - 1
    _bl[_k + 1:_k + 1] = [dict(VISIT_PEL), dict(PHASES_PEL)]

# Rosa (27 nov 2026): musculoesquelético y salud pélvica se trabajan con osteopatía: primera y segunda visita + tres fases
VISIT_OSTEO = {"type": "visit", "eyebrow": "Primera visita", "h2": "Cómo es la primera visita", "_id": "primera-visita",
               "intro": "Antes de tratar, hay que entender qué le pasa. La primera visita dura unos 60 minutos.",
               "items": [
                   {"i": "historia", "h": "Anamnesis", "p": "Su historia de salud: cómo empezaron las molestias, cómo evolucionan, sus antecedentes y las pruebas e informes que aporte."},
                   {"i": "postura", "h": "Análisis postural", "p": "Cómo se reparten las cargas en su cuerpo, en reposo y en movimiento."},
                   {"i": "movilidad", "h": "Examen osteopático", "p": "Valoración de la movilidad de las articulaciones, los músculos, las fascias y las vísceras relacionadas con sus molestias."},
                   {"i": "palpacion", "h": "Palpación", "p": "Palpación y escucha manual de los tejidos para localizar las zonas de tensión y de restricción."},
                   {"i": "tratamiento", "h": "Primer tratamiento osteopático", "p": "El primer tratamiento osteopático se inicia en la misma sesión."}],
               "note": "Si detectamos alguna señal que requiera valoración médica, se lo indicamos antes de iniciar el tratamiento."}
VISIT2_OSTEO = {"type": "visit", "eyebrow": "Seguimiento", "h2": "La segunda visita", "_id": "segunda-visita",
                "items": [
                    {"i": "historia", "h": "Informe y recomendaciones", "p": "Le entregamos un informe con consejos de higiene postural, hábitos y recomendaciones específicas."},
                    {"i": "plan", "h": "Plan de visitas", "p": "Su plan de visitas, dividido en tres fases."},
                    {"i": "tratamiento", "h": "Segundo tratamiento osteopático", "p": "Continuamos el tratamiento según lo valorado en la primera visita."},
                    {"i": "ejercicio", "h": "Ejercicios y consejos", "p": "A lo largo del tratamiento le proponemos ejercicios personalizados y consejos de alimentación, dentro de un enfoque global de su salud."}]}
from new_pages import AREA_EXTRA as _AE
_OSTEO_SET = set(MSK_SLUGS) | set(PELVIC_OSTEO) | set(_AE[0])
for _p in PAGES:
    if _p["slug"] not in _OSTEO_SET or _p["slug"] == "suelo-pelvico-dolor-pelvico":
        continue
    _bl = _p["blocks"]
    _mf = next((k for k, b in enumerate(_bl) if b.get("h2") == "Mi forma de trabajar"), None)
    _bl[:] = [b for b in _bl if b.get("h2") != "Mi forma de trabajar" and b.get("_id") != "segunda-visita"]
    _k = next((k for k, b in enumerate(_bl) if b.get("type") == "visit"), None)
    if _k is None:
        _k = next((k for k, b in enumerate(_bl) if b.get("type") == "phases"), None)
        if _k is None:
            _k = _mf if _mf is not None else next((k for k, b in enumerate(_bl) if b.get("type") == "evidence"), len(_bl))
            _bl.insert(_k, dict(PHASES_MSK))
        _bl.insert(_k, dict(VISIT_OSTEO))
    else:
        _bl[_k] = dict(VISIT_OSTEO)
    _bl.insert(_k + 1, dict(VISIT2_OSTEO))

# Rosa (27 nov 2026): todas las páginas de salud pélvica del curso de Olivier, con el mismo abordaje y sin precios
_CHIPS_PEL = {"type": "chips", "eyebrow": "Nuestro abordaje", "h2": "¿Cómo lo abordamos en WA LAM?",
              "intro": "En WA LAM, la salud pélvica se aborda con osteopatía y fisioterapia.",
              "items": [("Osteopatía", "osteopatia-sarria-sant-gervasi"), ("Osteopatía visceral", "osteopatia-visceral-barcelona"),
                        ("Osteopatía craneosacral", "osteopatia-craneosacral-barcelona"), ("Fisioterapia", "fisioterapia-sarria-sant-gervasi")]}
for _p in PAGES:
    if _p["slug"] not in PELVIC_OSTEO or _p["slug"] == "suelo-pelvico-dolor-pelvico":
        continue
    _bl = _p["blocks"]
    _bl[:] = [b for b in _bl if b.get("type") not in ("pro",)]
    if not any(b.get("type") == "chips" and b.get("h2") == "¿Cómo lo abordamos en WA LAM?" for b in _bl):
        _k = next((k for k, b in enumerate(_bl) if b.get("type") == "visit"), None)
        if _k is None:
            _k = next((k for k, b in enumerate(_bl) if b.get("type") == "evidence"), len(_bl))
        _bl.insert(_k, dict(_CHIPS_PEL))

# Rosa (27 nov 2026): en las páginas de salud pélvica, el bloque de la formación va al final, antes de la evidencia
for _p in PAGES:
    if _p["slug"] not in PELVIC_OSTEO:
        continue
    _bl = _p["blocks"]
    _fb = [b for b in _bl if b.get("eyebrow") == "Para profesionales"]
    if not _fb:
        continue
    _bl[:] = [b for b in _bl if b.get("eyebrow") != "Para profesionales"]
    _k = next((k for k, b in enumerate(_bl) if b.get("type") == "evidence"), len(_bl))
    _bl[_k:_k] = _fb


# Rosa (27 nov 2026): «¿Cómo lo abordamos?» va dentro de «¿Cómo se valora?»; sin bloque de botones aparte (musculoesquelético y salud pélvica)
_ABORD_TXT = "En WA LAM lo abordamos con [osteopatía](osteopatia-sarria-sant-gervasi), [osteopatía visceral](osteopatia-visceral-barcelona), [osteopatía craneosacral](osteopatia-craneosacral-barcelona) y [fisioterapia](fisioterapia-sarria-sant-gervasi)."
for _p in PAGES:
    if _p["slug"] not in _OSTEO_SET or _p["slug"] == "suelo-pelvico-dolor-pelvico":
        continue
    _bl = _p["blocks"]
    _bl[:] = [b for b in _bl if not (b.get("type") == "chips" and b.get("h2") == "¿Cómo lo abordamos en WA LAM?")]
    _v = next((b for b in _bl if _norm(b.get("h2", "")).startswith("como se valora")), None)
    if _v is not None:
        _v["h2"] = "¿Cómo se valora y cómo lo abordamos?"
        if _ABORD_TXT not in _v.get("paras", []):
            _v.setdefault("paras", []).append(_ABORD_TXT)
    else:
        for b in _bl:
            if b.get("type") == "visit" and b.get("_id") == "primera-visita":
                b["intro"] = b.get("intro", "") + " " + _ABORD_TXT
                break


# Rosa (27 nov 2026): las tres fases, adaptadas a osteopatía a partir del material que pasó (sin añadidos)
PHASES_OSTEO = {'type': 'phases', 'eyebrow': 'Tratamiento', 'h2': '¿Cuáles son las tres fases del tratamiento osteopático?', '_id': 'fases-del-tratamiento', 'items': [{'h': 'Fase intensiva', 'lab': 'Fase intensiva', 'paras': ['En esta **primera fase**, el paciente necesita **sesiones más frecuentes** (según el estado de cada persona), porque el **sistema nervioso** se encuentra **alterado** y los tejidos están mal adaptados.', 'La mayoría de los pacientes ya nota una **mejora significativa**; sin embargo, la recuperación completa requiere tiempo, según la gravedad y la duración del problema.']}, {'h': 'Fase correctiva o reconstructiva', 'lab': 'Fase correctiva', 'paras': ['En esta fase las **visitas se espacian**. Las restricciones de movilidad se han reducido y corregido, aunque pueden persistir algunas tensiones crónicas.', 'El paciente empieza a sentirse más **ligero, equilibrado, con más energía, descansa mejor y está más relajado**. Y un dato importante: empieza a **responsabilizarse de su salud**.']}, {'h': 'Fase de mantenimiento o bienestar', 'lab': 'Fase de bienestar', 'paras': ['La **tercera fase** es la del **bienestar**. Ahora los tratamientos se realizan **periódicamente**, ya que el cuerpo mantiene los resultados **durante más tiempo y con más facilidad**.', 'Los pacientes suelen experimentar una sensación de **buena salud, buena energía, menos estrés y más ganas de cuidarse**.']}]}
for _p in PAGES:
    if _p["slug"] not in _OSTEO_SET:
        continue
    for _i, _b in enumerate(_p["blocks"]):
        if _b.get("type") == "phases":
            _p["blocks"][_i] = dict(PHASES_OSTEO)

# Rosa (27 nov 2026): la fase intensiva trabaja la dolencia de cada página y regula el sistema nervioso
_DOL_OVR = {"Acompañamiento en fertilidad": "dificultades para concebir", "Osteopatía en el embarazo y el posparto": "molestias del embarazo y el posparto",
            "Ejercicios de suelo pélvico": "debilidad o tensión del suelo pélvico", "Osteoporosis y salud ósea": "osteoporosis",
            "Acompanyament en fertilitat": "dificultats per concebre", "Osteopatia a l'embaràs i el postpart": "molèsties de l'embaràs i el postpart",
            "Exercicis de sòl pelvià": "debilitat o tensió del sòl pelvià", "Osteoporosi i salut òssia": "osteoporosi"}
def _dolencia(nav):
    if nav in _DOL_OVR:
        return _DOL_OVR[nav]
    n = _re.sub(r"\s*\(.*?\)", "", nav).strip()
    return n if (len(n) > 1 and n[1].isupper()) else n[:1].lower() + n[1:]
_FI1 = ("En esta **primera fase** se trabaja en dos niveles a la vez. Por un lado, directamente sobre **lo que le ha traído a la consulta** "
        "(en esta página, {d}): la zona afectada y las estructuras relacionadas con ella. Por otro, sobre el **sistema nervioso**, que el dolor o la molestia "
        "mantienen **alterado**: cuando un problema se prolonga, los tejidos se adaptan mal y el cuerpo entra en un estado de alerta que lo perpetúa. "
        "El tratamiento manual actúa sobre los receptores de los tejidos y tiene un efecto **local** y **central** que ayuda a **regular el sistema nervioso**. "
        "En esa regulación tiene un papel clave el [nervio vago](nervio-vago).")
_FI2 = ("En esta fase las **sesiones son más frecuentes**, según el estado de cada persona. La mayoría de los pacientes ya nota una **mejora significativa**, "
        "pero la recuperación completa requiere tiempo, según la gravedad y la duración del problema.")
import copy as _cp
for _p in PAGES:
    if _p["slug"] not in _OSTEO_SET:
        continue
    for _i, _b in enumerate(_p["blocks"]):
        if _b.get("type") == "phases" and _b.get("h2") == PHASES_OSTEO["h2"]:
            _nb = _cp.deepcopy(_b)
            _nb["items"][0]["paras"] = [_FI1.format(d=_dolencia(_p["nav"])), _FI2]
            _p["blocks"][_i] = _nb

for _p in PAGES:
    if _p["slug"] == "suelo-pelvico-dolor-pelvico":
        _p["blocks"] = [b for b in _p["blocks"] if b.get("type") != "pro"]

# Rosa (27 nov 2026): sin precios en las páginas de salud pélvica y del curso de Olivier (solo «Reservar por WhatsApp»)
_NOPRICE = set(PELVIC_OSTEO) | set(OLIVIER_PAGES)
_PRX = _re.compile(r"\s*\((?:[^()]*?)\d+\s?€(?:[^()]*?)\)|,?\s*\d+\s?€|\s*·\s*\d+\s?€")
def _strip_price(o):
    if isinstance(o, str):
        return _PRX.sub("", o) if "€" in o else o
    if isinstance(o, list):
        return [_strip_price(x) for x in o]
    if isinstance(o, tuple):
        return tuple(_strip_price(x) for x in o)
    if isinstance(o, dict):
        return {k: _strip_price(v) for k, v in o.items()}
    return o
for _p in PAGES:
    if _p["slug"] not in _NOPRICE:
        continue
    for _b in _p["blocks"]:
        if _b.get("type") == "pro":
            _b["rows"] = [r for r in _b.get("rows", []) if "€" not in str(r) and _re.sub(r"\W", "", str(r[0])).lower() not in ("precio", "preu", "bono", "bo")]
    _p["blocks"] = _strip_price(_p["blocks"])
    _p["faq"] = _strip_price(_p.get("faq", []))
    if _p.get("facts"):
        _p["facts"] = [f for f in _p["facts"] if "€" not in f]

# Rosa (27 nov 2026): en la página general de salud pélvica no se repite «También puede interesarte»
for _p in PAGES:
    if _p["slug"] == "suelo-pelvico-dolor-pelvico":
        _p["related"] = []

# Rosa (27 nov 2026): título «Salud pélvica y urogenital»; palabra clave «salud pélvica»
for _p in PAGES:
    if _p["slug"] == "suelo-pelvico-dolor-pelvico":
        _p["h1"] = "Salud pélvica y urogenital en Barcelona"; _p["title"] = "Salud pélvica y urogenital en Barcelona | WA LAM"; _p["nav"] = "Salud pélvica"

# Rosa (27 nov 2026): Salud pélvica: primero qué es, después los problemas; sin la valoración osteopática
for _p in PAGES:
    if _p["slug"] != "suelo-pelvico-dolor-pelvico":
        continue
    _bl = [b for b in _p["blocks"] if not str(b.get("h2", "")).startswith("¿Cómo se valora la salud pélvica")]
    def _take(pref):
        for _i, b in enumerate(_bl):
            if str(b.get("h2", "")).startswith(pref):
                return _bl.pop(_i)
        return None
    _first = [x for x in (_take("¿Qué es la salud pélvica"), _take("¿Qué problemas de vejiga"), _take("¿Qué dolores pélvicos"),
                          _take("¿Qué se aborda en el embarazo"), _take("¿Se reconoce")) if x]
    _p["blocks"] = _first + _bl

# Rosa (27 nov 2026): la página general de salud pélvica también lleva primera y segunda visita y las tres fases
for _p in PAGES:
    if _p["slug"] != "suelo-pelvico-dolor-pelvico":
        continue
    _bl = _p["blocks"]
    if any(b.get("type") in ("visit", "phases") for b in _bl):
        continue
    _k = next((k for k, b in enumerate(_bl) if str(b.get("h2", "")).startswith("¿Qué busca el tratamiento")), None)
    _k = (_k + 1) if _k is not None else len(_bl)
    _ph = _cp.deepcopy(PHASES_OSTEO)
    _ph["items"][0]["paras"] = [_FI1.format(d="salud pélvica"), _FI2]
    _v = dict(VISIT_OSTEO); _v["intro"] = VISIT_OSTEO["intro"] + " " + _ABORD_TXT
    _bl[_k:_k] = [_v, dict(VISIT2_OSTEO), _ph]

# Rosa (27 nov 2026): los tres bloques de problemas en un único apartado con subtítulos
for _p in PAGES:
    if _p["slug"] != "suelo-pelvico-dolor-pelvico":
        continue
    _bl = _p["blocks"]
    _idx = [k for k, b in enumerate(_bl) if str(b.get("h2", "")).startswith(("¿Qué problemas de vejiga", "¿Qué dolores pélvicos", "¿Qué se aborda en el embarazo"))]
    if len(_idx) == 3:
        _a, _b2, _c = (_bl[k] for k in _idx)
        _pa = [x for x in _a["paras"] if not x.startswith("Pulse en cada uno")]
        _new = dict(_a); _new["h2"] = "¿Cuáles son los principales motivos de consulta?"; _new["_id"] = "problemas-salud-pelvica"
        _new["paras"] = ["Pulse en cada uno para ver más información.", "### Problemas de vejiga y sostén:"] + _pa + \
                        ["### Dolores pélvicos:"] + list(_b2["paras"]) + ["### Las diferentes etapas de la vida de la mujer:"] + list(_c["paras"])
        for k in sorted(_idx, reverse=True):
            del _bl[k]
        _bl.insert(_idx[0], _new)

# Rosa (27 nov 2026): «¿Se reconoce…?» justo antes de «¿Qué funciones cumple el suelo pélvico…?»
for _p in PAGES:
    if _p["slug"] != "suelo-pelvico-dolor-pelvico":
        continue
    _bl = _p["blocks"]
    _m = next((k for k, b in enumerate(_bl) if str(b.get("h2", "")).startswith("¿Se reconoce")), None)
    if _m is not None:
        _mb = _bl.pop(_m)
        _f = next((k for k, b in enumerate(_bl) if str(b.get("h2", "")).startswith("¿Qué funciones cumple")), len(_bl))
        _bl.insert(_f, _mb)

# Rosa (27 nov 2026): hormonas, embarazo, parto y posparto, y menopausia en un solo apartado (sin quitar texto)
for _p in PAGES:
    if _p["slug"] != "suelo-pelvico-dolor-pelvico":
        continue
    _bl = _p["blocks"]
    _pref = ("¿Cómo influyen las hormonas", "¿Qué ocurre en la pelvis durante el embarazo", "¿Qué necesita el cuerpo para el parto", "¿Qué cambia en la perimenopausia")
    _idx = [k for k, b in enumerate(_bl) if str(b.get("h2", "")).startswith(_pref)]
    if len(_idx) == 4:
        _paras = []
        for k in _idx:
            _paras += ["### " + _bl[k]["h2"]] + list(_bl[k].get("paras", []))
        _new = dict(_bl[_idx[0]]); _new["h2"] = "¿Cómo cambia la pelvis a lo largo de la vida genital de la mujer?"; _new["paras"] = _paras
        for k in sorted(_idx, reverse=True):
            del _bl[k]
        _bl.insert(_idx[0], _new)

# Rosa (27 nov 2026): «¿Qué tiene de particular la región pélvica y urogenital?» y «¿Cómo funciona el suelo pélvico?» arriba, tras «qué es»
for _p in PAGES:
    if _p["slug"] != "suelo-pelvico-dolor-pelvico":
        continue
    _bl = _p["blocks"]
    def _pop(pref):
        for _i, b in enumerate(_bl):
            if str(b.get("h2", "")).startswith(pref):
                return _bl.pop(_i)
    _part = _pop("¿Qué tiene de particular la región pélvica"); _func = _pop("¿Cómo funciona el suelo pélvico")
    if _part is not None:
        _part = dict(_part); _part["h2"] = "¿Qué tiene de particular la región pélvica y urogenital?"
    _q = next((k for k, b in enumerate(_bl) if str(b.get("h2", "")).startswith("¿Qué es la salud pélvica")), -1)
    _bl[_q + 1:_q + 1] = [x for x in (_part, _func) if x is not None]
