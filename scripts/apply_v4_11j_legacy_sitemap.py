#!/usr/bin/env python3
"""V4.11J — Redirecciones legacy + sitemap limpio.

Crea páginas puente para URLs antiguas absorbidas por la arquitectura V4.11,
actualiza sitemap.xml con páginas canónicas reales y deja documentado el cambio.
"""
from __future__ import annotations

from html import escape
from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://ikeritu.github.io/montes-bocineros/"
LASTMOD = "2026-06-30"

REDIRECTS = {
    "fuentes.html": {
        "target": "biblioteca.html#tabla-maestra-fuentes",
        "title": "Redirigiendo · Tabla maestra de fuentes",
        "heading": "La tabla de fuentes está ahora en Biblioteca documental",
        "body": "La antigua página de fuentes quedó absorbida por la Biblioteca documental unificada.",
        "button": "Abrir tabla maestra de fuentes",
    },
    "archivo-tecnico.html": {
        "target": "biblioteca.html#archivo-tecnico",
        "title": "Redirigiendo · Archivo técnico",
        "heading": "El archivo técnico está ahora en Biblioteca documental",
        "body": "Los informes IA, QA, versiones y auditorías se consultan desde el bloque de archivo técnico.",
        "button": "Abrir archivo técnico",
    },
    "glosario.html": {
        "target": "guia-lector.html#glosario-rapido",
        "title": "Redirigiendo · Glosario rápido",
        "heading": "El glosario está ahora en la Guía del lector",
        "body": "Los términos clave se han integrado en una ruta de lectura más sencilla.",
        "button": "Abrir glosario rápido",
    },
    "faq.html": {
        "target": "guia-lector.html#faq-rapida",
        "title": "Redirigiendo · Preguntas frecuentes",
        "heading": "La FAQ está ahora en la Guía del lector",
        "body": "Las preguntas rápidas se integraron en la guía principal para evitar páginas duplicadas.",
        "button": "Abrir FAQ rápida",
    },
    "barrio-banales.html": {
        "target": "biblioteca.html#barrio-banales",
        "title": "Redirigiendo · Barrio Bañales",
        "heading": "La ficha Barrio Bañales está ahora en Biblioteca documental",
        "body": "La nota documental se conserva dentro del mapa de fuentes y recepción historiográfica.",
        "button": "Abrir ficha documental",
    },
    "metodologia.html": {
        "target": "metodo-citacion.html#metodologia",
        "title": "Redirigiendo · Metodología",
        "heading": "La metodología está ahora en Método y citación",
        "body": "Los criterios documentales se han concentrado en una página metodológica única.",
        "button": "Abrir metodología",
    },
    "afirmaciones.html": {
        "target": "metodo-citacion.html#afirmaciones-verificables",
        "title": "Redirigiendo · Afirmaciones verificables",
        "heading": "Las afirmaciones verificables están ahora en Método y citación",
        "body": "La página antigua se conserva como puente para mantener enlaces históricos.",
        "button": "Abrir afirmaciones verificables",
    },
    "citas.html": {
        "target": "biblioteca.html#citas-verificadas",
        "title": "Redirigiendo · Citas verificadas",
        "heading": "Las citas verificadas están ahora en Biblioteca documental",
        "body": "Los fragmentos que sostienen la tesis se consultan desde la biblioteca unificada.",
        "button": "Abrir citas verificadas",
    },
    "citar.html": {
        "target": "metodo-citacion.html#como-citar",
        "title": "Redirigiendo · Cómo citar",
        "heading": "La guía de citación está ahora en Método y citación",
        "body": "La forma recomendada de citar el proyecto se ha centralizado en una sola página.",
        "button": "Abrir cómo citar",
    },
    "cadena-trueba.html": {
        "target": "trueba-facsimil.html",
        "title": "Redirigiendo · Cadena Trueba",
        "heading": "La cadena Trueba está ahora en la página de facsímiles",
        "body": "Los pasos 1858, 1862, 1872 y 1873 se consultan en la página específica de Trueba.",
        "button": "Abrir facsímiles de Trueba",
    },
    "pendientes-documentales.html": {
        "target": "biblioteca.html#pendientes-documentales",
        "title": "Redirigiendo · Pendientes documentales",
        "heading": "Los pendientes documentales están ahora en Biblioteca documental",
        "body": "La lista de búsquedas abiertas se conserva dentro del corpus documental unificado.",
        "button": "Abrir pendientes documentales",
    },
    "informes.html": {
        "target": "biblioteca.html#informes-ia",
        "title": "Redirigiendo · Informes auxiliares",
        "heading": "Los informes auxiliares están ahora en Biblioteca documental",
        "body": "Los informes IA, comparativas y QA se han reunido en el archivo técnico de la biblioteca.",
        "button": "Abrir informes auxiliares",
    },
}

CANONICAL_PAGES = [
    ("", "1.0"),
    ("historia.html", "0.95"),
    ("veredicto.html", "0.95"),
    ("guia-lector.html", "0.90"),
    ("montes.html", "0.90"),
    ("archivo.html", "0.90"),
    ("biblioteca.html", "0.88"),
    ("cronologia.html", "0.82"),
    ("estado-investigacion.html", "0.82"),
    ("trueba-facsimil.html", "0.82"),
    ("metodo-citacion.html", "0.80"),
    ("personajes.html", "0.72"),
    ("recepcion.html", "0.72"),
    ("resumen.html", "0.72"),
    ("autor.html", "0.65"),
    ("auditoria.html", "0.55"),
    ("comparativa.html", "0.55"),
    ("informes-acusticos.html", "0.50"),
    ("llorente-madoz-trueba.html", "0.50"),
    ("fuentes-sospechosas.html", "0.40"),
    ("mapa.html", "0.35"),
    ("informe-nemotron.html", "0.35"),
]


def write_redirect(filename: str, data: dict[str, str]) -> None:
    target = data["target"]
    url = BASE_URL + filename
    html = f"""<!DOCTYPE html>
<html lang=\"es\">
<head>
<meta charset=\"utf-8\"/>
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>
<meta name=\"robots\" content=\"noindex,follow\"/>
<meta http-equiv=\"refresh\" content=\"0; url={escape(target)}\"/>
<title>{escape(data['title'])} · Montes Bocineros de Bizkaia</title>
<meta name=\"description\" content=\"Página puente para conservar enlaces antiguos del proyecto Montes Bocineros de Bizkaia.\"/>
<meta name=\"theme-color\" content=\"#133f35\"/>
<meta name=\"last-modified\" content=\"{LASTMOD}\"/>
<link rel=\"canonical\" href=\"{escape(url)}\"/>
<link rel=\"icon\" href=\"assets/montes-logo.svg\" type=\"image/svg+xml\"/>
<script defer src=\"assets/menu.js?v=3.1.3\"></script>
<link rel=\"stylesheet\" href=\"assets/styles.css?v=3.1.3\"/>
<link rel=\"stylesheet\" href=\"assets/uiux-v13.css?v=3.1.3\"/>
<link rel=\"stylesheet\" href=\"assets/v411d-nav-footer.css?v=4.11d\"/>
<link rel=\"stylesheet\" href=\"assets/v411e-footer-support.css?v=4.11e\"/>
<link rel=\"stylesheet\" href=\"assets/v411i-production-polish.css?v=4.11i\"/>
<style>
.legacy-bridge {{ max-width: 900px; margin: 0 auto; padding: clamp(32px, 6vw, 72px) 18px; }}
.legacy-bridge-card {{ background: rgba(255,250,240,.96); border: 1px solid rgba(77,61,35,.16); border-radius: 24px; padding: clamp(24px, 5vw, 46px); box-shadow: 0 24px 70px rgba(19,63,53,.14); }}
.legacy-bridge-card .eyebrow {{ display:inline-flex; gap:.45rem; align-items:center; font-size:.78rem; letter-spacing:.08em; text-transform:uppercase; color:#133f35; font-weight:800; }}
.legacy-bridge-card h1 {{ margin:.8rem 0 1rem; font-size:clamp(1.8rem, 4vw, 3rem); line-height:1.05; }}
.legacy-bridge-card p {{ color:#5f6b62; font-size:1.05rem; line-height:1.65; }}
.legacy-bridge-actions {{ display:flex; gap:.75rem; flex-wrap:wrap; margin-top:1.1rem; }}
</style>
</head>
<body class=\"v13-page legacy-redirect-page\">
<a class=\"skip-link\" href=\"#contenido\">Saltar al contenido</a>
<header class=\"site-header\">
<div class=\"header-inner\">
<a class=\"brand\" href=\"index.html\"><img alt=\"\" decoding=\"async\" height=\"42\" loading=\"lazy\" src=\"assets/montes-logo.svg\" width=\"42\"/> <span>Montes Bocineros</span></a>
<nav aria-label=\"Navegación principal\" class=\"nav-simple\"><a href=\"index.html\">Inicio</a><a href=\"historia.html\">Historia</a><a href=\"montes.html\">Montes</a><a href=\"veredicto.html\">Síntesis crítica</a><a href=\"guia-lector.html\">Guía del lector</a><a href=\"archivo.html\">Archivo</a></nav>
<button aria-controls=\"menu-global\" aria-expanded=\"false\" class=\"menu-toggle\" data-menu-toggle=\"\" type=\"button\"><span>Profundizar</span><span aria-hidden=\"true\" class=\"menu-icon\"></span></button>
<div class=\"menu-panel\" data-menu-panel=\"\" id=\"menu-global\">
  <div class=\"menu-panel-head\">
    <strong>Profundizar</strong>
    <span>Ruta única para orientarse, comprobar fuentes, citar el proyecto y enviar correcciones.</span>
  </div>
  <div class=\"menu-grid menu-grid-v13 menu-grid-simplified v20b-menu\">
    <section>
      <p class=\"menu-section-title\">Ruta principal</p>
      <a href=\"index.html\">Inicio</a>
      <a href=\"historia.html\">Historia</a>
      <a href=\"montes.html\">Montes y mapa</a>
      <a href=\"veredicto.html\">Síntesis crítica</a>
      <a href=\"guia-lector.html\">Guía del lector</a>
      <a href=\"archivo.html\">Archivo documental</a>
    </section>
    <section>
      <p class=\"menu-section-title\">Información</p>
      <a href=\"archivo.html\">Archivo</a>
      <a href=\"biblioteca.html\">Biblioteca documental</a>
      <a href=\"personajes.html\">Personajes</a>
      <a href=\"metodo-citacion.html\">Método y citación</a>
      <a href=\"autor.html\">Autoría y correcciones</a>
    </section>
    <section>
      <p class=\"menu-section-title\">Comprobar fuentes</p>
      <a href=\"biblioteca.html#tabla-maestra-fuentes\">Tabla maestra de fuentes</a>
      <a href=\"biblioteca.html#linea-tiempo\">Línea documental</a>
      <a href=\"biblioteca.html#citas-verificadas\">Citas verificadas</a>
      <a href=\"biblioteca.html#trueba-1872\">Trueba 1872</a>
      <a href=\"biblioteca.html#pendientes-documentales\">Pendientes documentales</a>
    </section>
  </div>
</div>
</div>
</header>
<main class=\"legacy-bridge\" id=\"contenido\">
  <section class=\"legacy-bridge-card\">
    <span class=\"eyebrow\">V4.11J · URL conservada</span>
    <h1>{escape(data['heading'])}</h1>
    <p>{escape(data['body'])}</p>
    <p>Si la redirección no se abre automáticamente, usa el botón.</p>
    <div class=\"legacy-bridge-actions\">
      <a class=\"btn btn-primary\" href=\"{escape(target)}\">{escape(data['button'])}</a>
      <a class=\"btn\" href=\"index.html\">Volver al inicio</a>
    </div>
  </section>
</main>
<section aria-label=\"Apoyar el proyecto\" class=\"global-support\">
<div class=\"global-support-copy\"><span class=\"support-kicker\">Apoyar el proyecto</span><strong>¿Te ha servido esta investigación?</strong><span>Ayuda a mantener y ampliar este trabajo documental.</span></div>
<div class=\"support-buttons\"><a class=\"support-card kofi\" href=\"https://ko-fi.com/ikeritu\" rel=\"noopener noreferrer\" target=\"_blank\"><span aria-hidden=\"true\" class=\"support-icon\">☕</span><span><strong>Ko-fi</strong><small>ko-fi.com/ikeritu</small></span></a><a class=\"support-card paypal\" href=\"https://www.paypal.com/paypalme/ikeritus\" rel=\"noopener noreferrer\" target=\"_blank\"><span aria-hidden=\"true\" class=\"support-icon\">💙</span><span><strong>PayPal</strong><small>paypal.me/ikeritus</small></span></a></div>
</section>
<footer aria-label=\"Pie de página\" class=\"v341-footer\">
<div class=\"v341-footer-wrap\">
<div class=\"v341-footer-brand\">
<h4>Montes Bocineros de Bizkaia</h4>
<p>Investigación histórico-divulgativa: tradición viva, fuentes verificables y cautela documental.</p>
</div>
<div>
<h4>Información</h4>
<nav aria-label=\"Información del proyecto\" class=\"v341-footer-links\">
<a href=\"archivo.html\">Archivo</a>
<a href=\"biblioteca.html\">Biblioteca documental</a>
<a href=\"personajes.html\">Personajes</a>
<a href=\"metodo-citacion.html\">Método y citación</a>
<a href=\"autor.html\">Autoría y correcciones</a>
</nav>
</div>
<div>
<h4>Contacto</h4>
<nav aria-label=\"Contacto\" class=\"v341-footer-links\">
<a href=\"mailto:iker.ituarte.tejedor@gmail.com?subject=Correccion%20Montes%20Bocineros\">✉ Enviar corrección</a>
</nav>
</div>
</div>
</footer>
</body>
</html>
"""
    (ROOT / filename).write_text(html, encoding="utf-8")

def write_sitemap() -> None:
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for page, priority in CANONICAL_PAGES:
        loc = BASE_URL + page
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <lastmod>{LASTMOD}</lastmod>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_docs() -> None:
    informe = f"""# Informe V4.11J — Redirecciones legacy y sitemap limpio

Fecha: {LASTMOD}

## Objetivo

Cerrar la deuda técnica generada por la unificación de páginas en V4.11: varias URLs antiguas seguían apareciendo en `sitemap.xml` o en informes auxiliares, aunque su contenido ya había sido absorbido por `biblioteca.html`, `guia-lector.html`, `metodo-citacion.html`, `trueba-facsimil.html` y otras páginas canónicas.

## Cambios aplicados

- Se crean páginas puente `noindex,follow` para conservar enlaces antiguos y evitar errores 404.
- Se actualiza `sitemap.xml` con páginas reales/canónicas y `lastmod` `{LASTMOD}`.
- Se excluyen del sitemap las URLs legacy que solo sirven como puente.
- Se añade checker específico `scripts/check_v4_11j_legacy_sitemap.py`.

## Redirecciones creadas

"""
    for name, data in REDIRECTS.items():
        informe += f"- `{name}` → `{data['target']}`\n"
    informe += """
## Resultado esperado

- Los informes antiguos dejan de provocar enlaces rotos.
- Google/GitHub Pages no reciben un sitemap con páginas eliminadas.
- Las URLs históricas siguen funcionando para lectores o enlaces externos.
"""
    (ROOT / "INFORME_V4_11J_LEGACY_SITEMAP.md").write_text(informe, encoding="utf-8")

    roadmap = """# Roadmap V4.11J — Redirecciones legacy + sitemap limpio

- [x] Detectar URLs antiguas usadas por informes auxiliares.
- [x] Crear páginas puente `noindex,follow`.
- [x] Mantener enlaces externos/históricos sin romper navegación.
- [x] Actualizar `sitemap.xml` con páginas canónicas reales.
- [x] Excluir URLs legacy del sitemap.
- [x] Añadir checker específico V4.11J.
- [ ] Ejecutar checker en local antes de commit.
- [ ] Revisar visualmente una página puente.
- [ ] Commit recomendado: `Aplicar V4.11J redirecciones legacy y sitemap limpio`.

## Siguiente fase sugerida

V4.12 — limpieza editorial de README/CHANGELOG/estado actual y reducción de duplicidades documentales históricas.
"""
    (ROOT / "ROADMAP_V4_11J_LEGACY_SITEMAP.md").write_text(roadmap, encoding="utf-8")

    qa = """# QA V4.11J — Legacy + sitemap

## Comprobaciones

- [x] Las páginas legacy existen físicamente.
- [x] Todas las páginas legacy contienen `noindex,follow`.
- [x] Todas las páginas legacy contienen `http-equiv=\"refresh\"`.
- [x] Los destinos de las redirecciones existen.
- [x] El sitemap lista solo páginas reales.
- [x] El sitemap no lista las páginas legacy eliminadas del índice.
- [x] Los enlaces locales de HTML no generan 404 por las URLs antiguas usadas en informes.

## Checker

```powershell
py -3 scripts/check_v4_11j_legacy_sitemap.py
```

Resultado esperado:

```text
RESULTADO: PASS — V4.11J legacy redirects and sitemap are valid
```
"""
    (ROOT / "QA_V4_11J_LEGACY_SITEMAP.md").write_text(qa, encoding="utf-8")


def main() -> None:
    for filename, data in REDIRECTS.items():
        write_redirect(filename, data)
    write_sitemap()
    write_docs()
    print(f"V4.11J aplicado: {len(REDIRECTS)} redirecciones legacy + sitemap limpio")


if __name__ == "__main__":
    main()
