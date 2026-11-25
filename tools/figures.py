# -*- coding: utf-8 -*-
"""Ilustraciones propias de WA LAM (SVG en línea, colores de marca, tipografía fina).

Cada figura es una función que recibe tr() y devuelve el SVG. Los textos pasan por tr()
para que el catalán funcione con i18n_ca.json.
"""
import html

PET = "#1D3F40"   # petróleo
TQ = "#0CBFC2"    # turquesa
SAGE = "#5FC9CB"  # salvia
SAND = "#F2F1EE"  # piedra
CORAL = "#4A6B6C"
BONE = "#E2F6F6"

FONT = "font-family:Montserrat,system-ui,sans-serif"


def _t(x, y, s, size=13, weight=300, fill=PET, anchor="start", extra=""):
    return (f'<text x="{x}" y="{y}" style="{FONT};font-size:{size}px;font-weight:{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" {extra}>{html.escape(s)}</text>')


def _svg(w, h, body, label):
    return (f'<svg class="figsvg" viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(label)}" '
            f'xmlns="http://www.w3.org/2000/svg">{body}</svg>')


# ---------------------------------------------------------------- columna frontal genérica
def _spine_front(cx, top, scale=1.0):
    """Columna vista de frente: 7 cervicales, 12 dorsales, 5 lumbares y sacro. Devuelve (svg, centros)."""
    out, centers = [], {}
    y = top
    spec = [("C", 7, 26, 12), ("T", 12, 32, 15), ("L", 5, 40, 19)]
    for pre, n, w, h in spec:
        for i in range(1, n + 1):
            ww, hh = w * scale, h * scale
            out.append(f'<rect x="{cx - ww/2:.1f}" y="{y:.1f}" width="{ww:.1f}" height="{hh:.1f}" rx="{hh/2.6:.1f}" '
                       f'fill="{BONE}" stroke="{PET}" stroke-width="1"/>')
            centers[f"{pre}{i}"] = y + hh / 2
            y += hh + 3 * scale
    sw = 50 * scale
    out.append(f'<path d="M{cx - sw/2:.1f} {y:.1f} L{cx + sw/2:.1f} {y:.1f} L{cx:.1f} {y + 62*scale:.1f} Z" '
               f'fill="{BONE}" stroke="{PET}" stroke-width="1" stroke-linejoin="round"/>')
    centers["S"] = y + 22 * scale
    return "".join(out), centers, y + 62 * scale


# ---------------------------------------------------------------- 1. columna y órganos
def columna_organos(tr):
    W, H = 760, 700
    cx = 380
    spine, c, bottom = _spine_front(cx, 40, 1.05)
    # (rango de niveles, órgano, lado) — inervación simpática de referencia (y frénico C3–C5)
    rows = [
        (("C3", "C5"), tr("Diafragma (nervio frénico)"), "L"),
        (("T1", "T5"), tr("Corazón"), "R"),
        (("T2", "T7"), tr("Pulmones y bronquios"), "L"),
        (("T5", "T9"), tr("Estómago"), "R"),
        (("T6", "T10"), tr("Hígado, vesícula y páncreas"), "L"),
        (("T9", "T11"), tr("Intestino delgado"), "R"),
        (("T10", "L1"), tr("Riñones"), "L"),
        (("T10", "L2"), tr("Colon"), "R"),
        (("T10", "L1"), tr("Útero y ovarios"), "L"),
        (("T11", "L2"), tr("Vejiga"), "R"),
    ]
    body = [f'<rect width="{W}" height="{H}" fill="#fff"/>',
            f'<path d="M{cx} 30 C{cx-8} 300 {cx+8} 520 {cx} {bottom}" stroke="{TQ}" stroke-width="2" fill="none" opacity=".5"/>',
            spine]
    used = {"L": [], "R": []}
    nside = {"L": 0, "R": 0}
    for (a, b), name, side in rows:
        y1, y2 = c[a], c[b]
        ym = (y1 + y2) / 2
        # evita solapes de etiquetas en el mismo lado
        while any(abs(ym - u) < 46 for u in used[side]):
            ym += 46
        used[side].append(ym)
        off = 30 + nside[side] * 9
        nside[side] += 1
        bx = cx - off if side == "L" else cx + off
        tx = 60 if side == "L" else W - 60
        anchor = "start" if side == "L" else "end"
        body.append(f'<path d="M{bx} {y1:.1f} L{bx} {y2:.1f}" stroke="{TQ}" stroke-width="3" stroke-linecap="round"/>')
        lx2 = 250 if side == "L" else W - 250
        body.append(f'<path d="M{bx} {(y1+y2)/2:.1f} L{lx2} {ym:.1f} L{(tx + (150 if side == "L" else -150))} {ym:.1f}" '
                    f'stroke="{SAGE}" stroke-width="1" fill="none"/>')
        body.append(f'<circle cx="{lx2}" cy="{ym:.1f}" r="2.5" fill="{SAGE}"/>')
        body.append(_t(tx, ym - 6, name, 14, 400, PET, anchor))
        body.append(_t(tx, ym + 12, f"{a}–{b}", 12, 300, "#0a8f91", anchor))
    for lab, key in (("C", "C1"), ("T / D", "T1"), ("L", "L1")):
        body.append(_t(cx, c[key] - 12, "", 10))
    body.append(_t(cx + 70, c["C4"], tr("Cervicales"), 11, 300, SAGE))
    body.append(_t(cx - 70, c["T6"], tr("Dorsales"), 11, 300, SAGE, "end"))
    body.append(_t(cx + 70, c["L3"], tr("Lumbares"), 11, 300, SAGE))
    body.append(_t(cx, bottom + 24, tr("Sacro"), 11, 300, SAGE, "middle"))
    body.append(_t(W / 2, H - 18, tr("Niveles de referencia de la inervación del sistema nervioso autónomo"), 12, 300, "#5d7778", "middle"))
    return _svg(W, H, "".join(body), tr("La columna y los órganos: niveles de inervación"))


# ---------------------------------------------------------------- 2. menos / más
def menos_mas(tr):
    W, H = 760, 420
    cx, cy = 380, 210
    spine, c, bottom = _spine_front(cx, 52, 0.62)
    menos = [tr("Dolor"), tr("Rigidez"), tr("Tensión"), tr("Sobrecarga")]
    mas = [tr("Movilidad"), tr("Flexibilidad"), tr("Confianza al moverse"), tr("Calidad de vida")]
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>',
         f'<circle cx="{cx}" cy="{cy}" r="150" fill="{SAND}"/>', spine,
         _t(150, 70, tr("MENOS"), 22, 300, CORAL, "middle", 'letter-spacing="6"'),
         _t(W - 150, 70, tr("MÁS"), 22, 300, "#0a9fa2", "middle", 'letter-spacing="6"')]
    for i, s in enumerate(menos):
        y = 130 + i * 62
        b.append(f'<path d="M95 {y-5} L110 {y-5}" stroke="{CORAL}" stroke-width="2" stroke-linecap="round"/>')
        b.append(_t(122, y, s, 17, 300))
    for i, s in enumerate(mas):
        y = 130 + i * 62
        b.append(f'<path d="M{W-110} {y-5} L{W-95} {y-5} M{W-102.5} {y-12.5} L{W-102.5} {y+2.5}" stroke="#0a9fa2" stroke-width="2" stroke-linecap="round"/>')
        b.append(_t(W - 122, y, s, 17, 300, PET, "end"))
    return _svg(W, H, "".join(b), tr("Menos dolor, más movilidad"))


# ---------------------------------------------------------------- 3. progresión del disco
def _vertebra_top(x, y, stage, tr):
    g = [f'<g transform="translate({x},{y})">']
    # apófisis y lámina (detrás)
    g.append(f'<path d="M-18 46 L-62 92 M18 46 L62 92 M0 58 L0 112" stroke="{PET}" stroke-width="14" stroke-linecap="round" opacity=".14"/>')
    g.append(f'<path d="M-22 44 Q0 70 22 44" fill="none" stroke="{PET}" stroke-width="1"/>')
    # médula
    g.append(f'<ellipse cx="0" cy="58" rx="13" ry="10" fill="{SAND}" stroke="{PET}" stroke-width="1"/>')
    # raíces nerviosas
    g.append(f'<path d="M-11 60 C-30 66 -44 70 -64 66 M11 60 C30 66 44 70 64 66" stroke="#0CBFC2" stroke-width="3" fill="none" stroke-linecap="round"/>')
    # anillo fibroso
    g.append(f'<ellipse cx="0" cy="0" rx="62" ry="44" fill="#F2F1EE" stroke="{PET}" stroke-width="1.2"/>')
    for r in (52, 42):
        g.append(f'<ellipse cx="0" cy="0" rx="{r}" ry="{r*0.7:.0f}" fill="none" stroke="{SAGE}" stroke-width=".8" opacity=".7"/>')
    # núcleo
    if stage == 0:
        g.append(f'<ellipse cx="0" cy="-2" rx="22" ry="15" fill="{TQ}" opacity=".55"/>')
    elif stage == 1:
        g.append(f'<path d="M-22 -4 C-22 -20 22 -20 22 -4 C22 10 30 30 16 40 C6 46 -10 30 -22 -4Z" fill="{TQ}" opacity=".55"/>')
        g.append(f'<path d="M10 30 C20 40 30 44 34 40" stroke="{CORAL}" stroke-width="1.5" fill="none"/>')
    else:
        g.append(f'<path d="M-22 -4 C-22 -20 22 -20 22 -4 C22 8 24 26 24 38 C26 54 40 62 34 72 C26 80 14 66 10 56 C4 40 -14 24 -22 -4Z" fill="{TQ}" opacity=".6"/>')
        g.append(f'<circle cx="30" cy="66" r="12" fill="none" stroke="{CORAL}" stroke-width="1.5" stroke-dasharray="3 3"/>')
    g.append("</g>")
    return "".join(g)


def disco_progresion(tr):
    W, H = 900, 380
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>']
    titles = [tr("Disco normal"), tr("Protrusión discal"), tr("Hernia discal")]
    for i, t in enumerate(titles):
        x = 150 + i * 300
        b.append(_t(x, 40, t, 17, 400, PET, "middle"))
        b.append(_vertebra_top(x, 140, i, tr))
    b.append(_t(70, 312, tr("Anillo fibroso"), 12, 300, SAGE))
    b.append(f'<path d="M96 302 L112 182" stroke="{SAGE}" stroke-width=".8"/>')
    b.append(_t(150, 350, tr("Núcleo pulposo"), 12, 300, "#0a8f91", "middle"))
    b.append(f'<path d="M150 338 L150 152" stroke="{TQ}" stroke-width=".8" stroke-dasharray="2 3"/>')
    b.append(_t(530, 350, tr("Médula espinal"), 12, 300, SAGE, "middle"))
    b.append(f'<path d="M500 340 L450 205" stroke="{SAGE}" stroke-width=".8"/>')
    b.append(_t(885, 350, tr("La hernia presiona la raíz nerviosa"), 12, 300, CORAL, "end"))
    b.append(f'<path d="M800 338 L782 218" stroke="{CORAL}" stroke-width=".8"/>')
    b.append(_t(260, 312, tr("Raíz nerviosa"), 12, 300, "#0A8F91"))
    b.append(f'<path d="M258 304 L222 210" stroke="#0CBFC2" stroke-width=".8"/>')
    return _svg(W, H, "".join(b), tr("Evolución de un disco: normal, protrusión y hernia"))


# ---------------------------------------------------------------- 4. síntomas de compresión
def sintomas_compresion(tr):
    W, H = 780, 560
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>']
    # silueta de espalda en línea fina
    sx = 560
    b.append(f'<path d="M{sx-34} 70 C{sx-34} 30 {sx+34} 30 {sx+34} 70 C{sx+34} 96 {sx+20} 108 {sx+18} 118 '
             f'C{sx+60} 126 {sx+110} 134 {sx+120} 170 L{sx+128} 300 C{sx+130} 330 {sx+112} 330 {sx+108} 300 L{sx+96} 200 '
             f'C{sx+92} 260 {sx+86} 300 {sx+92} 350 C{sx+104} 420 {sx+70} 470 {sx+60} 540 '
             f'M{sx-34} 70 C{sx-34} 96 {sx-20} 108 {sx-18} 118 C{sx-60} 126 {sx-110} 134 {sx-120} 170 L{sx-128} 300 '
             f'C{sx-130} 330 {sx-112} 330 {sx-108} 300 L{sx-96} 200 C{sx-92} 260 {sx-86} 300 {sx-92} 350 C{sx-104} 420 {sx-70} 470 {sx-60} 540" '
             f'fill="none" stroke="{SAGE}" stroke-width="1.4" stroke-linecap="round"/>')
    spine, c, bottom = _spine_front(sx, 112, 0.5)
    b.append(spine)
    # pelvis
    b.append(f'<path d="M{sx-80} {bottom-40} C{sx-70} {bottom+10} {sx-30} {bottom+30} {sx} {bottom+26} '
             f'C{sx+30} {bottom+30} {sx+70} {bottom+10} {sx+80} {bottom-40}" fill="none" stroke="{PET}" stroke-width="1" opacity=".5"/>')
    # zona lumbar destacada
    b.append(f'<circle cx="{sx}" cy="{c["L4"]:.0f}" r="20" fill="{CORAL}" opacity=".18"/>')
    b.append(f'<circle cx="{sx}" cy="{c["L4"]:.0f}" r="7" fill="{CORAL}" opacity=".6"/>')
    # trayecto ciático
    b.append(f'<path d="M{sx+8} {c["L5"]:.0f} C{sx+40} {bottom+20} {sx+50} 420 {sx+62} 536" stroke="#0CBFC2" stroke-width="2.5" fill="none" stroke-dasharray="6 5"/>')
    b.append(_t(40, 64, tr("Cuando una hernia comprime una raíz nerviosa"), 18, 400))
    sint = [(tr("Hormigueo"), PET), (tr("Pérdida de sensibilidad"), PET), (tr("Dolor que baja por la pierna"), PET),
            (tr("Pérdida de fuerza"), PET)]
    for i, (s, col) in enumerate(sint):
        y = 120 + i * 50
        b.append(f'<circle cx="52" cy="{y-5}" r="4" fill="{TQ}"/>')
        b.append(_t(68, y, s, 17, 300, col))
    b.append(f'<path d="M40 336 L420 336" stroke="{SAND}" stroke-width="2"/>')
    b.append(_t(40, 372, tr("Señales de alarma: acuda a urgencias"), 14, 500, CORAL))
    alar = [tr("Pérdida de control de la orina o las heces"), tr("Adormecimiento en la zona genital o perineal"),
            tr("Pérdida de fuerza del suelo pélvico"), tr("Alteraciones de la erección"), tr("Debilidad que avanza en las piernas")]
    for i, s in enumerate(alar):
        y = 404 + i * 30
        b.append(f'<path d="M48 {y-5} L58 {y-5}" stroke="{CORAL}" stroke-width="1.6" stroke-linecap="round"/>')
        b.append(_t(68, y, s, 14, 300))
    return _svg(W, H, "".join(b), tr("Síntomas de compresión de una raíz nerviosa y señales de alarma"))


# ---------------------------------------------------------------- 5. cabeza alineada / adelantada
def _head_side(x, y, fwd, col):
    dx = 38 if fwd else 0
    g = [f'<g transform="translate({x},{y})">']
    # columna cervical
    pts = [(0, 140), (2, 120), (4 + dx*0.3, 100), (6 + dx*0.55, 80), (8 + dx*0.8, 60), (10 + dx*0.95, 42), (12 + dx, 26)]
    for (px, py) in pts:
        g.append(f'<rect x="{px-9}" y="{py-7}" width="18" height="13" rx="5" fill="{BONE}" stroke="{PET}" stroke-width=".9"/>')
    # cráneo
    hx, hy = 14 + dx, -26
    g.append(f'<path d="M{hx-36} {hy+40} C{hx-50} {hy+4} {hx-30} {hy-42} {hx+8} {hy-42} C{hx+50} {hy-42} {hx+62} {hy} {hx+54} {hy+22} '
             f'L{hx+60} {hy+36} L{hx+50} {hy+40} L{hx+48} {hy+58} C{hx+30} {hy+64} {hx+10} {hy+60} {hx} {hy+50} C{hx-14} {hy+52} {hx-30} {hy+48} {hx-36} {hy+40}Z" '
             f'fill="#fff" stroke="{PET}" stroke-width="1.2" stroke-linejoin="round"/>')
    # línea de plomada
    g.append(f'<path d="M14 {hy-70} L14 150" stroke="{col}" stroke-width="1.4" stroke-dasharray="4 5"/>')
    if fwd:
        g.append(f'<path d="M{dx+84} -40 L{dx+124} -40" stroke="{CORAL}" stroke-width="2" marker-end="url(#ar)"/>')
    else:
        g.append(f'<path d="M14 -100 L14 -84" stroke="{TQ}" stroke-width="2"/><path d="M8 -92 L14 -102 L20 -92" stroke="{TQ}" stroke-width="2" fill="none"/>')
    g.append("</g>")
    return "".join(g)


def cabeza_adelantada(tr):
    W, H = 760, 380
    b = [f'<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8Z" fill="{CORAL}"/></marker></defs>',
         f'<rect width="{W}" height="{H}" fill="#fff"/>',
         f'<rect x="40" y="290" width="680" height="60" fill="{SAND}"/>']
    b.append(_head_side(190, 150, False, TQ))
    b.append(_head_side(500, 150, True, CORAL))
    b.append(_t(204, 330, tr("Cabeza alineada"), 15, 400, "#0a8f91", "middle"))
    b.append(_t(514, 330, tr("Cabeza adelantada"), 15, 400, CORAL, "middle"))
    b.append(_t(204, 350, tr("La carga cae sobre la columna"), 12, 300, PET, "middle"))
    b.append(_t(514, 350, tr("Más carga para el cuello y la espalda alta"), 12, 300, PET, "middle"))
    return _svg(W, H, "".join(b), tr("Cabeza alineada frente a cabeza adelantada"))


def cabeza_adelantada_zonas(tr):
    W, H = 780, 520
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>']
    x0 = 470
    # silueta lateral sentada mirando el móvil
    b.append(f'<path d="M{x0+60} 92 C{x0+30} 60 {x0+60} 20 {x0+100} 30 C{x0+140} 40 {x0+148} 86 {x0+120} 108 L{x0+128} 128 L{x0+112} 132 '
             f'L{x0+108} 150 C{x0+92} 152 {x0+80} 146 {x0+70} 138" fill="#fff" stroke="{PET}" stroke-width="1.2"/>')
    b.append(f'<path d="M{x0+62} 120 C{x0+20} 150 {x0+10} 230 {x0+20} 330 L{x0+40} 470" fill="none" stroke="{SAGE}" stroke-width="1.4"/>')
    b.append(f'<path d="M{x0+100} 150 C{x0+120} 200 {x0+118} 280 {x0+110} 340 L{x0+230} 352 L{x0+236} 470" fill="none" stroke="{SAGE}" stroke-width="1.4"/>')
    b.append(f'<path d="M{x0+40} 360 L{x0+110} 352" stroke="{SAGE}" stroke-width="1.4"/>')
    b.append(f'<path d="M{x0+90} 150 C{x0+110} 190 {x0+130} 230 {x0+170} 250 L{x0+230} 236" fill="none" stroke="{SAGE}" stroke-width="1.4"/>')
    b.append(f'<rect x="{x0+228}" y="214" width="12" height="36" rx="3" transform="rotate(-30 {x0+234} 232)" fill="{TQ}" opacity=".7"/>')
    # columna curvada
    for i, (px, py) in enumerate([(x0+70, 132), (x0+62, 150), (x0+54, 168), (x0+48, 186), (x0+44, 204), (x0+40, 222), (x0+38, 240),
                                  (x0+36, 260), (x0+35, 282), (x0+35, 304), (x0+37, 326), (x0+40, 348)]):
        b.append(f'<rect x="{px-8}" y="{py-6}" width="16" height="12" rx="4" fill="{BONE}" stroke="{PET}" stroke-width=".8"/>')
    # médula
    b.append(f'<path d="M{x0+76} 130 C{x0+52} 180 {x0+40} 260 {x0+46} 350" stroke="{TQ}" stroke-width="1.6" fill="none" opacity=".6"/>')
    zones = [(x0+96, 46, tr("Dolor de cabeza"), tr("Nuca y base del cráneo")),
             (x0+70, 134, tr("Dolor y rigidez"), tr("Base del cuello y hombros")),
             (x0+56, 170, tr("Debilidad muscular"), tr("Cuello, hombros y espalda alta")),
             (x0+44, 210, tr("Vértebras"), tr("Más carga en la columna cervical")),
             (x0+38, 250, tr("Irritación nerviosa"), tr("Hormigueo hacia brazos y manos"))]
    for i, (zx, zy, h, sub) in enumerate(zones):
        ty = 70 + i * 82
        b.append(f'<circle cx="{zx}" cy="{zy}" r="6" fill="{CORAL}" opacity=".55"/>')
        b.append(f'<path d="M{zx-8} {zy} L330 {ty-4} L300 {ty-4}" stroke="{SAGE}" stroke-width=".9" fill="none"/>')
        b.append(_t(40, ty, h, 16, 400, PET))
        b.append(_t(40, ty + 20, sub, 13, 300, "#5d7778"))
    return _svg(W, H, "".join(b), tr("Zonas que pueden verse afectadas por la cabeza adelantada"))


# ---------------------------------------------------------------- 6. eje intestino–disco
def eje_intestino_disco(tr):
    W, H = 840, 380
    b = [f'<defs><marker id="ar2" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0 0 L9 4.5 L0 9Z" fill="{SAGE}"/></marker></defs>',
         f'<rect width="{W}" height="{H}" fill="#fff"/>']
    # intestino
    b.append(f'<path d="M70 120 C70 80 230 80 230 120 C230 150 90 150 90 180 C90 210 230 210 230 240 C230 280 70 280 70 240" '
             f'fill="none" stroke="{SAGE}" stroke-width="18" stroke-linecap="round" opacity=".55"/>')
    for (x, y) in [(110, 105), (180, 112), (130, 175), (200, 190), (100, 255), (170, 245)]:
        b.append(f'<circle cx="{x}" cy="{y}" r="4" fill="{CORAL}" opacity=".7"/>')
    b.append(_t(150, 50, tr("Intestino"), 16, 400, PET, "middle"))
    b.append(_t(150, 320, tr("Disbiosis"), 13, 300, CORAL, "middle"))
    b.append(_t(150, 338, tr("desequilibrio de la microbiota"), 12, 300, "#5d7778", "middle"))
    # flecha 1
    b.append(f'<path d="M260 180 L340 180" stroke="{SAGE}" stroke-width="1.5" marker-end="url(#ar2)"/>')
    # inflamación / permeabilidad
    b.append(f'<circle cx="420" cy="180" r="62" fill="{SAND}"/>')
    b.append(_t(420, 172, tr("Inflamación"), 14, 400, PET, "middle"))
    b.append(_t(420, 192, tr("y permeabilidad"), 14, 400, PET, "middle"))
    b.append(_t(420, 274, tr("Paso de moléculas"), 12, 300, "#5d7778", "middle"))
    b.append(_t(420, 290, tr("y bacterias a la sangre"), 12, 300, "#5d7778", "middle"))
    b.append(f'<path d="M500 180 L580 180" stroke="{SAGE}" stroke-width="1.5" marker-end="url(#ar2)"/>')
    # disco
    b.append(f'<rect x="620" y="110" width="150" height="34" rx="10" fill="{BONE}" stroke="{PET}" stroke-width="1"/>')
    b.append(f'<ellipse cx="695" cy="180" rx="75" ry="24" fill="#F2F1EE" stroke="{PET}" stroke-width="1"/>')
    b.append(f'<ellipse cx="695" cy="180" rx="28" ry="10" fill="{TQ}" opacity=".5"/>')
    b.append(f'<rect x="620" y="216" width="150" height="34" rx="10" fill="{BONE}" stroke="{PET}" stroke-width="1"/>')
    b.append(_t(695, 80, tr("Disco intervertebral"), 16, 400, PET, "middle"))
    b.append(_t(695, 290, tr("Posible degeneración"), 13, 300, CORAL, "middle"))
    b.append(_t(695, 306, tr("y dolor (hipótesis en estudio)"), 12, 300, "#5d7778", "middle"))
    b.append(_t(W / 2, H - 12, tr("El eje intestino–disco: una línea de investigación emergente"), 12, 300, "#5d7778", "middle"))
    return _svg(W, H, "".join(b), tr("El eje intestino–disco"))


# ---------------------------------------------------------------- 7. nervio ciático
def nervio_ciatico(tr):
    W, H = 720, 760
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>']
    cx = 420
    # columna lumbar y sacro
    y = 40
    for i in range(5):
        b.append(f'<rect x="{cx-22}" y="{y}" width="44" height="22" rx="8" fill="{BONE}" stroke="{PET}" stroke-width="1"/>')
        y += 26
    b.append(f'<path d="M{cx-30} {y} L{cx+30} {y} L{cx} {y+70} Z" fill="{BONE}" stroke="{PET}" stroke-width="1"/>')
    # pelvis
    b.append(f'<path d="M{cx-30} {y+4} C{cx-70} {y-40} {cx-150} {y-30} {cx-160} {y+20} C{cx-166} {y+60} {cx-140} {y+96} {cx-118} {y+108} '
             f'M{cx-26} {y+60} C{cx-50} {y+110} {cx-80} {y+130} {cx-118} {y+120}" fill="none" stroke="{PET}" stroke-width="1.2" opacity=".55"/>')
    b.append(f'<circle cx="{cx-122}" cy="{y+114}" r="16" fill="none" stroke="{PET}" stroke-width="1" opacity=".4"/>')
    # piriforme
    b.append(f'<path d="M{cx-14} {y+30} C{cx-60} {y+40} {cx-90} {y+56} {cx-118} {y+70}" stroke="{CORAL}" stroke-width="10" opacity=".25" stroke-linecap="round"/>')
    # fémur / pierna
    b.append(f'<path d="M{cx-120} {y+110} L{cx-110} {y+300} M{cx-110} {y+320} L{cx-104} {y+480}" stroke="{PET}" stroke-width="14" stroke-linecap="round" opacity=".12"/>')
    # raíces L4–S3 que convergen
    roots_y = [40 + 26*3 + 11, 40 + 26*4 + 11, y + 14, y + 30, y + 46]
    for ry in roots_y:
        b.append(f'<path d="M{cx-18} {ry} C{cx-50} {ry+10} {cx-70} {y+50} {cx-92} {y+76}" stroke="#0CBFC2" stroke-width="2" fill="none"/>')
    # nervio ciático
    b.append(f'<path d="M{cx-92} {y+76} C{cx-104} {y+150} {cx-100} {y+250} {cx-98} {y+310} C{cx-96} {y+380} {cx-80} {y+440} {cx-74} {y+500}" '
             f'stroke="#0CBFC2" stroke-width="5" fill="none" stroke-linecap="round"/>')
    b.append(f'<path d="M{cx-98} {y+312} C{cx-120} {y+380} {cx-126} {y+440} {cx-130} {y+500}" stroke="#0CBFC2" stroke-width="3" fill="none" stroke-linecap="round"/>')
    labels = [(roots_y[0], tr("Raíces L4 a S3"), tr("se unen para formar el nervio")),
              (y + 62, tr("Músculo piramidal"), tr("el nervio pasa por debajo o a través")),
              (y + 200, tr("Nervio ciático"), tr("el más grueso y largo del cuerpo")),
              (y + 330, tr("Rodilla"), tr("se divide en tibial y peroneo común")),
              (y + 470, tr("Pierna y pie"), tr("sensibilidad y fuerza"))]
    for ly, h, s in labels:
        b.append(f'<path d="M{cx-100} {ly} L250 {ly}" stroke="{SAGE}" stroke-width=".8"/>')
        b.append(_t(40, ly - 4, h, 15, 400))
        b.append(_t(40, ly + 15, s, 12, 300, "#5d7778"))
    return _svg(W, H, "".join(b), tr("Trayecto del nervio ciático"))


FIGS = {
    "columna_organos": columna_organos,
    "menos_mas": menos_mas,
    "disco_progresion": disco_progresion,
    "sintomas_compresion": sintomas_compresion,
    "cabeza_adelantada": cabeza_adelantada,
    "cabeza_adelantada_zonas": cabeza_adelantada_zonas,
    "eje_intestino_disco": eje_intestino_disco,
    "nervio_ciatico": nervio_ciatico,
}


# ---------------------------------------------------------------- 8. escala de Bristol
def escala_bristol(tr):
    W, H = 860, 640
    BR1, BR2 = "#BDB6AA", "#8F877A"
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>',
         _t(W / 2, 38, tr("Escala de Bristol"), 20, 400, PET, "middle"),
         _t(W / 2, 60, tr("Una forma sencilla de describir la consistencia de las heces"), 13, 300, "#5d7778", "middle")]
    rows = [
        (tr("Tipo 1"), tr("Bolitas duras y separadas"), tr("Estreñimiento"), CORAL),
        (tr("Tipo 2"), tr("Forma de salchicha, con bultos"), tr("Estreñimiento leve"), CORAL),
        (tr("Tipo 3"), tr("Salchicha con grietas en la superficie"), tr("Normal"), "#0a9fa2"),
        (tr("Tipo 4"), tr("Salchicha lisa y blanda"), tr("Normal"), "#0a9fa2"),
        (tr("Tipo 5"), tr("Trozos blandos de bordes definidos"), tr("Tendencia a heces blandas"), "#5FC9CB"),
        (tr("Tipo 6"), tr("Trozos esponjosos de bordes irregulares"), tr("Diarrea leve"), CORAL),
        (tr("Tipo 7"), tr("Acuosas, sin trozos sólidos"), tr("Diarrea"), CORAL),
    ]
    for i, (k, d, verdict, col) in enumerate(rows):
        y = 100 + i * 76
        if i in (2, 3):
            b.append(f'<rect x="30" y="{y-30}" width="{W-60}" height="70" rx="8" fill="{TQ}" opacity=".07"/>')
        b.append(_t(50, y + 6, k, 15, 500, PET))
        cx, cy = 230, y
        g = []
        if i == 0:
            for j, dx in enumerate((-48, -18, 12, 42)):
                g.append(f'<circle cx="{cx+dx}" cy="{cy + (j % 2) * 6 - 3}" r="11" fill="{BR2}"/>')
        elif i == 1:
            g.append(f'<path d="M{cx-70} {cy} q10 -16 24 -10 q12 -12 26 -4 q14 -12 28 -2 q14 -10 26 2 q14 4 10 16 q-6 10 -22 8 q-14 10 -28 2 q-14 8 -28 0 q-14 8 -26 -2 q-12 -2 -10 -10z" fill="{BR2}"/>')
        elif i == 2:
            g.append(f'<rect x="{cx-72}" y="{cy-13}" width="144" height="26" rx="13" fill="{BR1}"/>')
            for dx in (-40, -10, 22, 48):
                g.append(f'<path d="M{cx+dx} {cy-12} l-5 8 M{cx+dx+6} {cy+12} l4 -7" stroke="#fff" stroke-width="1.6" stroke-linecap="round"/>')
        elif i == 3:
            g.append(f'<path d="M{cx-74} {cy+4} C{cx-70} {cy-16} {cx+40} {cy-20} {cx+70} {cy-6} C{cx+80} {cy+2} {cx+76} {cy+14} {cx+60} {cy+14} C{cx+20} {cy+14} {cx-60} {cy+20} {cx-74} {cy+4}Z" fill="{BR1}"/>')
        elif i == 4:
            for dx, rx in ((-52, 18), (-14, 16), (22, 17), (56, 14)):
                g.append(f'<ellipse cx="{cx+dx}" cy="{cy}" rx="{rx}" ry="11" fill="{BR1}"/>')
        elif i == 5:
            g.append(f'<path d="M{cx-70} {cy} q8 -18 22 -8 q8 -14 20 -4 q12 -16 22 -2 q12 -12 22 0 q14 -8 20 6 q8 12 -6 16 q-10 8 -22 2 q-10 10 -22 2 q-12 8 -22 0 q-12 6 -20 -2 q-16 4 -14 -10z" fill="{BR1}" opacity=".85"/>')
        else:
            g.append(f'<path d="M{cx-78} {cy+4} C{cx-50} {cy-14} {cx-20} {cy+16} {cx+10} {cy} S{cx+60} {cy-12} {cx+80} {cy+6} C{cx+60} {cy+18} {cx-50} {cy+20} {cx-78} {cy+4}Z" fill="{BR1}" opacity=".55"/>')
        b.extend(g)
        b.append(_t(340, y - 2, d, 15, 300, PET))
        b.append(_t(340, y + 18, verdict, 13, 400, col))
    b.append(_t(W / 2, H - 14, tr("Los tipos 3 y 4 son los más habituales en un intestino que funciona bien"), 12, 300, "#5d7778", "middle"))
    return _svg(W, H, "".join(b), tr("Escala de Bristol de las heces"))


FIGS["escala_bristol"] = escala_bristol


# ---------------------------------------------------------------- 9. nervio vago: qué hace
TERRA = "#0A8F91"   # terracota suave
SKY = "#6FD3D5"     # azul suave
SKYL = "#E2F6F6"


def _organ(kind, x, y, s=1.0):
    t = f'transform="translate({x},{y}) scale({s})"'
    st = f'fill="{SKYL}" stroke="{SKY}" stroke-width="1.4"'
    if kind == "brain":
        return (f'<g {t}><path d="M-40 6 C-46 -20 -24 -40 0 -36 C24 -42 48 -22 42 4 C40 22 22 28 0 26 C-20 30 -38 24 -40 6Z" {st}/>'
                f'<path d="M-24 -18 C-14 -10 -26 0 -12 6 M2 -30 C-4 -16 10 -10 4 2 M22 -20 C14 -8 28 0 18 12" fill="none" stroke="{SKY}" stroke-width="1.1"/></g>')
    if kind == "face":
        return (f'<g {t}><path d="M-14 -26 C10 -30 26 -14 24 6 L30 14 L22 18 L22 28 C10 32 -6 28 -14 18 C-22 4 -24 -18 -14 -26Z" {st}/>'
                f'<path d="M8 2 L16 2 M10 20 L18 20" stroke="{SKY}" stroke-width="1.2"/></g>')
    if kind == "larynx":
        return f'<g {t}><rect x="-8" y="-14" width="16" height="28" rx="6" {st}/><path d="M-6 -4 H6 M-6 4 H6" stroke="{SKY}"/></g>'
    if kind == "lungs":
        return (f'<g {t}><path d="M-6 -30 C-30 -24 -44 10 -38 34 C-28 42 -10 36 -6 20Z" {st}/>'
                f'<path d="M6 -30 C30 -24 44 10 38 34 C28 42 10 36 6 20Z" {st}/></g>')
    if kind == "heart":
        return (f'<g {t}><path d="M0 26 C-30 6 -32 -18 -14 -24 C-4 -27 0 -18 0 -14 C0 -18 6 -27 16 -24 C34 -18 30 6 0 26Z" {st}/></g>')
    if kind == "stomach":
        return (f'<g {t}><path d="M-10 -26 C-14 -6 -30 0 -26 16 C-20 32 14 30 24 14 C30 2 20 -6 10 -2 C4 0 2 -12 4 -26Z" {st}/></g>')
    if kind == "liver":
        return (f'<g {t}><path d="M-34 -6 C-30 -22 20 -26 34 -14 C40 -6 30 8 10 12 C-10 16 -36 14 -34 -6Z" {st}/></g>')
    if kind == "gut":
        return (f'<g {t}><path d="M-28 22 V-16 C-28 -24 28 -24 28 -16 V22" fill="none" stroke="{SKY}" stroke-width="7" stroke-linecap="round" opacity=".55"/>'
                f'<path d="M-14 -6 C-4 -14 6 -2 14 -8 M-16 4 C-6 -4 6 10 16 2 M-14 14 C-4 6 6 20 14 12" fill="none" stroke="{SKY}" stroke-width="3.2" stroke-linecap="round" opacity=".85"/></g>')
    return ""


def nervio_vago_funciones(tr):
    W, H = 900, 760
    cx = 450
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>',
         _t(W / 2, 40, tr("¿Qué hace el nervio vago?"), 20, 400, PET, "middle")]
    # tronco del nervio
    b.append(f'<path d="M{cx} 120 C{cx-6} 200 {cx+8} 260 {cx} 330 C{cx-8} 420 {cx+10} 500 {cx} 600 L{cx} 660" '
             f'fill="none" stroke="{TERRA}" stroke-width="3.2" stroke-linecap="round"/>')
    org = [("brain", cx, 92, 1.0), ("face", cx + 46, 180, 0.8), ("larynx", cx + 4, 230, 1.0), ("lungs", cx - 60, 330, 0.85),
           ("heart", cx + 50, 360, 0.75), ("stomach", cx + 56, 470, 0.85), ("liver", cx - 60, 470, 0.8), ("gut", cx, 640, 1.0)]
    # ramas
    for k, x, y, s in org[1:]:
        if k in ("larynx", "gut"):
            continue
        sx = cx
        sy = y - 10 if k != "face" else 170
        b.append(f'<path d="M{sx} {sy} C{(sx+x)/2} {sy-10} {(sx+x)/2} {y} {x - (30 if x > cx else -30)} {y}" '
                 f'fill="none" stroke="{TERRA}" stroke-width="1.8" stroke-linecap="round"/>')
    for k, x, y, s in org:
        b.append(_organ(k, x, y, s))
    labels = [
        (40, 120, tr("Estado de ánimo"), tr("Modula la respuesta al estrés y el sistema límbico")),
        (40, 270, tr("Respiración"), tr("Coordina el ritmo respiratorio con el cardiaco")),
        (40, 520, tr("Inflamación"), tr("Reflejo antiinflamatorio a través de la acetilcolina")),
        (40, 620, tr("Digestión"), tr("Motilidad, enzimas y esfínteres, en diálogo con el intestino")),
        (W - 40, 150, tr("Cara y voz"), tr("Expresión facial y tono de voz, con el nervio facial")),
        (W - 40, 250, tr("Habla"), tr("Cuerdas vocales coordinadas con la respiración")),
        (W - 40, 400, tr("Corazón"), tr("Enlentece el pulso y favorece la calma (freno vagal)")),
    ]
    for x, y, h, s in labels:
        a = "start" if x < cx else "end"
        b.append(_t(x, y, h.upper(), 13, 500, "#0a8f91", a, 'letter-spacing="1.5"'))
        b.append(_t(x, y + 20, s, 13, 300, PET, a))
    b.append(_t(W / 2, H - 14, tr("Ilustración conceptual: no representa la anatomía con exactitud"), 11, 300, "#7d9192", "middle"))
    return _svg(W, H, "".join(b), tr("Funciones del nervio vago"))


# ---------------------------------------------------------------- 10. nervio vago: anatomía
def nervio_vago_anatomia(tr):
    W, H = 760, 800
    cx = 380
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>',
         _t(W / 2, 40, tr("Anatomía del nervio vago"), 20, 400, PET, "middle"),
         f'<rect x="230" y="70" width="300" height="680" rx="24" fill="none" stroke="{SKY}" stroke-width="2"/>']
    # tronco cerebral y dos ramas que convergen
    b.append(_organ("brain", cx, 120, 1.15))
    b.append(f'<path d="M{cx-10} 150 C{cx-26} 230 {cx-20} 280 {cx-8} 330 M{cx+10} 150 C{cx+26} 230 {cx+20} 280 {cx+8} 330" '
             f'fill="none" stroke="{TERRA}" stroke-width="2.6" stroke-linecap="round"/>')
    b.append(f'<path d="M{cx} 330 C{cx-10} 420 {cx+10} 520 {cx} 690" fill="none" stroke="{TERRA}" stroke-width="3" stroke-linecap="round"/>')
    org = [("lungs", cx, 300, 1.15, tr("Pulmones"), "L", 270), ("heart", cx + 30, 360, 0.75, tr("Corazón"), "R", 360),
           ("liver", cx - 50, 450, 0.9, tr("Hígado y vesícula"), "L", 450), ("stomach", cx + 50, 455, 0.85, tr("Estómago, bazo y páncreas"), "R", 455),
           ("gut", cx, 610, 1.3, tr("Intestino delgado y grueso"), "R", 610)]
    for k, x, y, s, lab, side, ly in org:
        b.append(_organ(k, x, y, s))
        if side == "L":
            b.append(f'<path d="M{x-40} {ly} L200 {ly}" stroke="{SAGE}" stroke-width=".8"/>')
            b.append(_t(195, ly + 4, lab, 13, 300, PET, "end"))
        else:
            b.append(f'<path d="M{x+40} {ly} L560 {ly}" stroke="{SAGE}" stroke-width=".8"/>')
            b.append(_t(565, ly + 4, lab, 13, 300, PET))
    for kx in (cx - 34, cx + 34):
        b.append(f'<ellipse cx="{kx}" cy="540" rx="11" ry="17" fill="{SKYL}" stroke="{SKY}" stroke-width="1.3"/>')
    b.append(f'<path d="M{cx+46} 540 L560 540" stroke="{SAGE}" stroke-width=".8"/>')
    b.append(_t(565, 544, tr("Riñones"), 13, 300, PET))
    b.append(f'<path d="M{cx-40} 120 L200 120" stroke="{SAGE}" stroke-width=".8"/>')
    b.append(_t(195, 116, tr("Tronco cerebral"), 13, 300, PET, "end"))
    b.append(_t(195, 134, tr("X par craneal"), 12, 300, "#0a8f91", "end"))
    b.append(_t(W / 2, 772, tr("Dos ramas, derecha e izquierda, que convergen por encima del tórax. Los órganos pélvicos dependen de los nervios sacros (S2–S4)."), 11, 300, "#5d7778", "middle"))
    return _svg(W, H, "".join(b), tr("Anatomía del nervio vago"))


# ---------------------------------------------------------------- 11. métodos naturales
def nervio_vago_metodos(tr):
    W, H = 820, 620
    cx, cy = 410, 320
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>',
         _t(W / 2, 40, tr("Hábitos que favorecen la actividad del nervio vago"), 18, 400, PET, "middle"),
         f'<circle cx="{cx}" cy="{cy}" r="118" fill="none" stroke="{SKY}" stroke-width="10" opacity=".45"/>',
         f'<circle cx="{cx}" cy="{cy}" r="100" fill="none" stroke="{SKY}" stroke-width="2"/>',
         _t(cx, cy - 10, tr("Métodos naturales"), 17, 400, PET, "middle"),
         _t(cx, cy + 14, tr("para estimular"), 15, 300, PET, "middle"),
         _t(cx, cy + 36, tr("el nervio vago"), 15, 300, PET, "middle")]
    import math
    items = [(tr("Respiración lenta"), '<path d="M-10 6 C-22 -8 -14 -20 -2 -14 M10 6 C22 -8 14 -20 2 -14 M0 -20 V8"/>'),
             (tr("Sueño reparador"), '<path d="M6 -14 A12 12 0 1 0 14 6 A10 10 0 0 1 6 -14Z"/>'),
             (tr("Luz natural"), '<circle r="7"/><path d="M0 -16 V-12 M0 12 V16 M-16 0 H-12 M12 0 H16 M-11 -11 l3 3 M8 8 l3 3 M-11 11 l3 -3 M8 -8 l3 -3"/>'),
             (tr("Gárgaras"), '<path d="M-8 -14 H8 L6 14 H-6 Z M-4 -4 H4"/>'),
             (tr("Movimiento diario"), '<circle cx="2" cy="-14" r="3"/><path d="M1 -10 L-3 2 L4 8 L2 16 M-3 2 L-10 6 M1 -8 L8 -2"/>'),
             (tr("Cantar o tararear"), '<path d="M-4 10 V-12 L10 -16 V6"/><circle cx="-8" cy="10" r="4"/><circle cx="6" cy="6" r="4"/>'),
             (tr("Risa y conexión social"), '<circle cx="-7" cy="-6" r="5"/><circle cx="7" cy="-6" r="5"/><path d="M-14 12 C-12 2 -2 2 0 12 C2 2 12 2 14 12"/>'),
             (tr("Frío moderado"), '<path d="M0 -14 V14 M-12 -7 L12 7 M-12 7 L12 -7"/>'),
             (tr("Yoga y meditación"), '<circle cy="-12" r="3"/><path d="M0 -8 V2 M-12 10 C-6 4 6 4 12 10 M-10 -2 L0 0 L10 -2"/>')]
    n = len(items)
    for i, (lab, icon) in enumerate(items):
        ang = -math.pi / 2 + i * 2 * math.pi / n
        x, y = cx + 215 * math.cos(ang), cy + 200 * math.sin(ang)
        b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="{SKYL}"/>')
        b.append(f'<g transform="translate({x:.0f},{y:.0f})" fill="none" stroke="{TERRA}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{icon}</g>')
        b.append(_t(x, y + 50, lab, 13, 300, PET, "middle"))
    return _svg(W, H, "".join(b), tr("Métodos naturales para estimular el nervio vago"))


# ---------------------------------------------------------------- 12. sistema de implicación social
def nervio_vago_social(tr):
    W, H = 800, 460
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>']
    hx = 230
    b.append(f'<path d="M{hx+60} 60 C{hx-30} 50 {hx-80} 120 {hx-70} 190 L{hx-88} 220 L{hx-70} 232 L{hx-74} 262 C{hx-70} 290 {hx-40} 300 {hx-10} 296 '
             f'L{hx-6} 340 C{hx+20} 380 {hx+60} 400 {hx+90} 420 M{hx+60} 60 C{hx+150} 70 {hx+170} 170 {hx+130} 250 C{hx+110} 290 {hx+110} 330 {hx+130} 420" '
             f'fill="#fff" stroke="{SKY}" stroke-width="1.6"/>')
    # tronco y ramas a cara, oído, garganta
    b.append(f'<path d="M{hx+70} 230 C{hx+70} 300 {hx+60} 360 {hx+64} 420" stroke="{TERRA}" stroke-width="3" fill="none"/>')
    for d in (f"M{hx+68} 240 C{hx+30} 230 {hx-10} 210 {hx-50} 200", f"M{hx+68} 250 C{hx+20} 260 {hx-20} 270 {hx-50} 262",
              f"M{hx+70} 230 C{hx+90} 210 {hx+110} 200 {hx+110} 180", f"M{hx+66} 290 C{hx+40} 300 {hx+20} 320 {hx} 330",
              f"M{hx+70} 240 C{hx+40} 200 {hx+20} 160 {hx-30} 140"):
        b.append(f'<path d="{d}" stroke="{TERRA}" stroke-width="1.6" fill="none"/>')
    b.append(_t(470, 90, tr("Sistema de implicación social"), 18, 400, PET))
    txt = [tr("El complejo vagal ventral trabaja junto a los"), tr("pares craneales V, VII, IX, X y XI."), "",
           tr("Coordina la expresión de la cara, el tono de la voz,"), tr("la escucha y la mirada con el ritmo del corazón."), "",
           tr("Cuando el sistema nervioso percibe seguridad,"), tr("favorece la calma, la conexión y la corregulación."),
           tr("Con el estrés crónico dominan"), tr("las respuestas de defensa.")]
    for i, line in enumerate(txt):
        b.append(_t(470, 130 + i * 24, line, 14, 300, PET))
    b.append(_t(470, 380, tr("Modelo propuesto por Stephen Porges (teoría polivagal)"), 12, 300, "#0a8f91"))
    return _svg(W, H, "".join(b), tr("Sistema de implicación social y nervio vago"))


FIGS.update({"nervio_vago_funciones": nervio_vago_funciones, "nervio_vago_anatomia": nervio_vago_anatomia,
             "nervio_vago_metodos": nervio_vago_metodos, "nervio_vago_social": nervio_vago_social})


# ---------------------------------------------------------------- 13. estados del sistema nervioso autónomo
def estados_sna(tr):
    W, H = 900, 820
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>',
         _t(W / 2, 40, tr("Estados del sistema nervioso autónomo"), 20, 400, PET, "middle"),
         _t(W / 2, 62, tr("Según la teoría polivagal de Stephen Porges"), 13, 300, "#5d7778", "middle")]
    C = [(450, 300, SKY, "#F2F1EE"), (330, 520, "#1D3F40", "#eef3f3"), (570, 520, "#0CBFC2", "#e6f8f8")]
    for x, y, st, fl in C:
        b.append(f'<circle cx="{x}" cy="{y}" r="205" fill="{fl}" fill-opacity=".55" stroke="{st}" stroke-width="2"/>')
    def block(x, y, title, sub1, sub2, lines, anchor="middle"):
        out = [_t(x, y, title, 17, 500, PET, anchor, 'letter-spacing="1.5"'),
               _t(x, y + 20, sub1, 12, 400, "#0a8f91", anchor)]
        if sub2:
            out.append(_t(x, y + 36, sub2, 12, 400, "#0a8f91", anchor))
        yy = y + (58 if sub2 else 42)
        for ln in lines:
            out.append(_t(x, yy, ln, 11.5, 300, PET, anchor)); yy += 16
        return "".join(out)
    b.append(block(450, 150, tr("EN RELAJACIÓN"), tr("Sistema nervioso parasimpático"), tr("Vía vagal ventral"),
                   [tr("Frecuencia cardiaca y tono muscular normales"), tr("Calma, conexión, curiosidad,"), tr("creatividad y esperanza")]))
    b.append(block(250, 520, tr("EN INMOVILIZACIÓN"), tr("Parasimpático"), tr("Vía vagal dorsal"),
                   [tr("Pulso bajo, tono y energía bajos"), tr("Con seguridad: tranquilidad,"), tr("ensoñación, meditación"),
                    tr("Sin seguridad: desánimo,"), tr("soledad, desesperanza")]))
    b.append(block(655, 520, tr("EN MOVILIZACIÓN"), tr("Sistema nervioso simpático"), "",
                   [tr("Más pulso, tensión y tono muscular"), tr("Con seguridad: energía, juego,"), tr("motivación"),
                    tr("Sin seguridad: lucha o huida,"), tr("estrés, ansiedad, miedo")]))
    b.append(_t(355, 400, tr("Quietud"), 12, 500, PET, "middle")); b.append(_t(355, 416, tr("e intimidad"), 12, 300, PET, "middle"))
    b.append(_t(545, 400, tr("Juego, baile,"), 12, 500, PET, "middle")); b.append(_t(545, 416, tr("deporte"), 12, 300, PET, "middle"))
    b.append(_t(450, 600, tr("Congelación"), 12, 500, PET, "middle")); b.append(_t(450, 616, tr("defensiva"), 12, 300, PET, "middle"))
    b.append(_t(W / 2, H - 40, tr("Los estados no son compartimentos: se combinan en estados híbridos."), 12, 300, "#5d7778", "middle"))
    b.append(_t(W / 2, H - 22, tr("La regulación sana es la flexibilidad para pasar de uno a otro y volver a la calma."), 12, 300, "#5d7778", "middle"))
    return _svg(W, H, "".join(b), tr("Estados del sistema nervioso autónomo según la teoría polivagal"))


FIGS["estados_sna"] = estados_sna
