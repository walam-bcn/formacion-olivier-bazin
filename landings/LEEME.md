# Landing pages WA LAM

24 páginas con el mismo estilo que la landing de formación de Olivier Bazin: Poppins, verde petróleo `#1D3F40`, turquesa `#0CBFC2`, blanco y piedra `#F2F1EE`, con fondo de partículas en las secciones verdes.

Vista previa de todas las páginas: `landings/index.html` (o https://walam-bcn.github.io/formacion-olivier-bazin/landings/ una vez publicada en GitHub Pages).

## Páginas (24)

| Bloque | URL propuesta en Wix | Tanda |
|---|---|---|
| Portada | /medicina-integrativa-barcelona | 1 |
| Motivo de consulta | /dolor-persistente-cronico | 1 |
| Motivo de consulta | /estres-ansiedad | 1 |
| Motivo de consulta | /salud-digestiva-microbiota | 2 |
| Motivo de consulta | /acompanamiento-fertilidad | 2 |
| Motivo de consulta | /salud-mujer-menopausia | 3 |
| Motivo de consulta | /prevencion-longevidad | 3 |
| Servicio | /osteopatia-sarria-sant-gervasi | 1 |
| Servicio | /fisioterapia-sarria-sant-gervasi | 1 |
| Servicio | /perdida-de-peso-sarria-sant-gervasi | 1 |
| Motivo de consulta | /sueno-insomnio | 1 |
| Servicio | /dejar-de-fumar-acupuntura | 2 |
| Servicio | /acupuntura-medicina-tradicional-china | 2 |
| Servicio | /pni-pnie-barcelona | 2 |
| Servicio | /nutricion-salud-intestinal | 3 |
| Servicio | /drenaje-linfatico-postoperatorio | 1 |
| Servicio | /masajes-sarria-sant-gervasi | 2 |
| Servicio | /reflexologia-sarria-sant-gervasi | 2 |
| Healthy Lifestyle Academy | /curso-mindfulness-mbsr-barcelona | 1 |
| Healthy Lifestyle Academy | /yoga-particular-grupos-reducidos | 2 |
| Healthy Lifestyle Academy | /qigong-barcelona | 2 |
| Healthy Lifestyle Academy | /formacion-medicina-tradicional-china | 3 |
| Healthy Lifestyle Academy | /retiros-mindfulness-meditacion-silencio | 2 |
| Healthy Lifestyle Academy | /vacaciones-con-sentido | 1 |

Vista previa sin código: https://claude.ai/artifact/SJpd32PmKkjCpQEKCxrwej (privada). Guía SEO completa: `landings/guia-seo.html`.

Archivos para Wix: `seo-wix.csv` (URL, title, description, H1 y palabras clave), `schema/*.json` (datos estructurados por página) y `og/*.png` (imagen para redes de cada página).

## Antes de publicar

1. **Completar los datos resaltados** (recuadro turquesa discontinuo): nombre, titulación y número de colegiado del profesional, duración, precio, fechas, horarios y enlaces de inscripción. No los hemos inventado. En una web de salud, el nombre y la colegiación del profesional son lo que más pesa para Google (E-E-A-T) y para el paciente.
2. **Revisar las URL y el enlace de reserva** en `tools/landings_content.py` → `SITE`. Ahora se usan `https://www.walambcn.com/<slug>` y `https://www.walambcn.com/book-online` (la URL por defecto de Wix Bookings).
3. Volver a generar: `python3 tools/build_landings.py` (imágenes para redes: `node tools/make_og.js`).

## SEO: aviso importante

Si la página se inserta en Wix como **iframe (HTML embed)**, Google no atribuye ese texto a la página de Wix. Para posicionar:
- crea la página en Wix con el mismo slug, **título SEO** y **meta descripción** (están en el `<title>` y `<meta name="description">` de cada HTML),
- y, si es posible, pega los textos principales (H1, primeros párrafos y FAQ) como texto nativo de Wix. El iframe puede quedarse para la parte visual.

Cada página incluye datos estructurados (`MedicalWebPage` o `Course` y `FAQPage`) listos para copiarlos en *Configuración SEO › Datos estructurados* de Wix.

## Referencias científicas

Todas las referencias citadas (guía ACP 2017, revisiones Cochrane, metaanálisis de JAMA, BMJ, Gut, BJSM, Psychological Bulletin, Biological Psychiatry, etc.) se comprobaron por título, autor, revista y DOI en noviembre de 2026. Están centralizadas en `R` dentro de `tools/landings_content.py`. Si se añade un estudio nuevo, hay que verificar el DOI antes de publicarlo.
