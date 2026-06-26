#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path.cwd()
TARGET = ROOT / "personajes.html"
START = "<!-- V4_7C_PERSONAJES_ESCRITOS_FIJOS_START -->"
END = "<!-- V4_7C_PERSONAJES_ESCRITOS_FIJOS_END -->"
STYLE_ID = "v47c-personajes-escritos-fijos-style"

PERSON_MAP = {
    "juan-nunez-de-lara": {
        "title": "Juan Núñez de Lara", "status": "Documento transmitido",
        "note": "Cuaderno/Capitulado de 1342 transmitido en copia posterior. Sirve para la fórmula de las cinco vozinas en contexto de Junta, no para una lista nominal moderna de montes.",
        "links": [("Abrir PDF del capitulado", "fuentes/capitulado-1342-juan-nunez-de-lara.pdf"), ("Ver pruebas documentales", "veredicto.html#pruebas-documentales")]
    },
    "lope-garcia-de-salazar": {
        "title": "Lope García de Salazar", "status": "Tradición bajomedieval",
        "note": "Bienandanzas e fortunas es clave para el ciclo de Don Çuria/Jaun Zuria y las cinco vozinas, pero no enumera Gorbea, Oiz, Sollube, Ganecogorta y Colisa.",
        "links": [("Ver tabla maestra documental", "fuentes.html#tabla-maestra-documental"), ("Ver contexto histórico", "historia.html#linea-tiempo-certezas")]
    },
    "tomas-goicolea": {
        "title": "Tomás de Goicolea", "status": "Crónica atribuida",
        "note": "Pieza útil para la transmisión del ciclo legendario. Queda pendiente completar el cotejo directo del manuscrito o facsímil.",
        "links": [("Ver cadena documental", "cadena-trueba.html#goicolea"), ("Ver tabla maestra documental", "fuentes.html#tabla-maestra-documental")]
    },
    "ibarguen-cachopin": {
        "title": "Ibargüen-Cachopín", "status": "Crónica moderna temprana",
        "note": "Aporta contexto sobre adarrak, cuernos y bocinas, pero no fija la lista moderna de cinco montes.",
        "links": [("Ver tabla maestra documental", "fuentes.html#tabla-maestra-documental"), ("Ver metodología", "metodologia.html")]
    },
    "juan-ruiz-de-anguiz": {
        "title": "Juan Ruiz de Anguiz", "status": "Transmisión documental",
        "note": "Escribano vinculado a la copia de Gernika de 1600. Su interés es la transmisión documental, no la autoría del texto medieval.",
        "links": [("Abrir folio original", "fuentes/fuero-viejo-1600-folio35-original.webp"), ("Ver biblioteca documental", "biblioteca.html")]
    },
    "juan-ramon-iturriza": {
        "title": "Juan Ramón de Iturriza y Zabala", "status": "Historiografía vizcaína",
        "note": "Aporta sustrato institucional sobre gobierno antiguo, merindades, bocinas y bocineros. La pista de la lista moderna queda descartada en las páginas revisadas.",
        "links": [("Ver archivo técnico", "archivo-tecnico.html"), ("Ver biblioteca documental", "biblioteca.html")]
    },
    "pascual-madoz": {
        "title": "Pascual Madoz", "status": "Fuente puente anterior a Trueba",
        "note": "En la entrada Guernica recoge cinco heraldos que subían a las alturas y tañían bocinas, pero no enumera los cinco montes tradicionales.",
        "links": [("Abrir facsímil Madoz", "fuentes/madoz_tomo_ix_guernica_p69_cinco_heraldos.pdf"), ("Ver Llorente / Madoz / Trueba", "llorente-madoz-trueba.html")]
    },
    "antonio-trueba": {
        "title": "Antonio de Trueba", "status": "Primera lista completa localizada",
        "note": "En 1872 documenta la lista Gorbea, Oiz, Sollube, Ganecogorta y Colisa con la fórmula cautelosa «se cree fuesen».",
        "links": [("Ver facsímil Trueba", "trueba-facsimil.html"), ("Ver cadena Trueba", "cadena-trueba.html")]
    },
    "juan-eustaquio-delmas": {
        "title": "Juan Eustaquio Delmas", "status": "Recepción decimonónica",
        "note": "Su guía de 1864 sirve como contexto territorial e institucional. El facsímil revisado no aporta la lista moderna de cinco montes.",
        "links": [("Ver nota Delmas", "NOTA_DOCUMENTAL_DELMAS_1864.md"), ("Ver ficha Museotik", "https://museotik.euskadi.eus/autoria-lerchundi-y-sirotich-jose-antonio-de-lerchundi-y-sirotich-luis-de/titulo-retrato-de-juan-eustaquio-delmas/objeto-pintura/museotik-ca-177711/webmus00-contenedor/es/")]
    },
    "barrio-banales": {
        "title": "Javier Barrio Marro y Goio Bañales García", "status": "Síntesis moderna",
        "note": "Estudio secundario clave para ordenar documentos y recepción. No sustituye la lectura directa de las fuentes primarias.",
        "links": [("Abrir estudio PDF", "fuentes/barrio_banales_el_tanido_cinco_bocinas_simbolo_bizkaia.pdf"), ("Ver página del estudio", "barrio-banales.html")]
    },
}

STYLE = '''
<style id="v47c-personajes-escritos-fijos-style">
  .p47c-escritos-section { padding: clamp(2.25rem, 5vw, 4.5rem) 0; background: linear-gradient(180deg, rgba(246,241,231,.55), rgba(255,255,255,.92)); }
  .p47c-escritos-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; margin-top: 1.15rem; }
  .p47c-escritos-card { border: 1px solid rgba(31,107,85,.18); border-radius: 18px; background: rgba(255,255,255,.9); padding: 1rem; box-shadow: 0 12px 28px rgba(28,45,38,.07); scroll-margin-top: 7rem; }
  .p47c-escritos-card h3 { margin: .15rem 0 .35rem; }
  .p47c-escritos-status { display: inline-flex; font-size: .72rem; font-weight: 800; letter-spacing: .045em; text-transform: uppercase; color: #1f6b55; }
  .p47c-escritos-card p { margin: .45rem 0 .75rem; }
  .p47c-escritos-links { display: flex; flex-wrap: wrap; gap: .45rem; }
  .p47c-escritos-links a { display: inline-flex; align-items: center; gap: .25rem; border: 1px solid rgba(31,107,85,.25); border-radius: 999px; padding: .42rem .72rem; text-decoration: none; font-weight: 700; }
</style>
'''.strip()

def read(path): return path.read_text(encoding="utf-8", errors="replace")
def write(path, text): path.write_text(text, encoding="utf-8")
def remove_block(text, start, end): return re.sub(re.escape(start) + r"[\s\S]*?" + re.escape(end), "", text).strip() + "\n"

def add_style(text):
    text = re.sub(r'<style\b[^>]*id=["\']' + re.escape(STYLE_ID) + r'["\'][^>]*>[\s\S]*?</style>\s*', '', text, flags=re.I)
    return text.replace("</head>", STYLE + "\n</head>", 1) if "</head>" in text else STYLE + "\n" + text

def clean_menu(text):
    for pattern in [
        r'<a\b[^>]*href=["\']glosario\.html(?:#[^"\']*)?["\'][^>]*>[\s\S]*?Glosario[\s\S]*?</a>\s*',
        r'<a\b[^>]*href=["\']guia-lector\.html#(?:glosario|palabras-clave)["\'][^>]*>[\s\S]*?Glosario[\s\S]*?</a>\s*',
        r'<a\b[^>]*href=["\'](?:preguntas-frecuentes|preguntas|faq|faqs)\.html(?:#[^"\']*)?["\'][^>]*>[\s\S]*?(?:Preguntas frecuentes|FAQ)[\s\S]*?</a>\s*',
    ]:
        text = re.sub(pattern, "", text, flags=re.I)
    text = text.replace("Preguntas frecuentes", "Guía del lector")
    text = text.replace("preguntas frecuentes", "guía del lector")
    text = text.replace(">FAQ<", ">Guía del lector<")
    text = re.sub(r'(["\'])glosario\.html(?:#[^"\']*)?\1', r'\1guia-lector.html#palabras-clave\1', text, flags=re.I)
    text = re.sub(r'(["\'])(?:preguntas-frecuentes|preguntas|faq|faqs)\.html(?:#[^"\']*)?\1', r'\1guia-lector.html\1', text, flags=re.I)
    return text

def patch_article_link(text, person_id):
    target = f"#escritos-{person_id}"
    article_pattern = re.compile(rf'(<article\b[^>]*id=["\']{re.escape(person_id)}["\'][^>]*>)([\s\S]*?)(</article>)', flags=re.I)
    def repl_article(match):
        start, body, end = match.group(1), match.group(2), match.group(3)
        link_pattern = re.compile(r'<a\b(?P<attrs>[^>]*class=["\'][^"\']*\bp36-escritos-link\b[^"\']*["\'][^>]*)>[\s\S]*?</a>', flags=re.I)
        def repl_link(lm):
            attrs = lm.group("attrs")
            attrs = re.sub(r'\s+href=["\'][^"\']*["\']', '', attrs, flags=re.I)
            attrs = re.sub(r'\s+target=["\'][^"\']*["\']', '', attrs, flags=re.I)
            attrs = re.sub(r'\s+rel=["\'][^"\']*["\']', '', attrs, flags=re.I).rstrip()
            return f'<a{attrs} href="{target}">Ir a sus escritos →</a>'
        body_new, count = link_pattern.subn(repl_link, body, count=1)
        if count == 0:
            insert = f'<div class="p36-escritos"><a class="p36-escritos-link" href="{target}">Ir a sus escritos →</a></div>'
            m = re.search(r'</h3>', body, flags=re.I)
            body_new = body[:m.end()] + "\n      " + insert + body[m.end():] if m else insert + body
        return start + body_new + end
    text, count = article_pattern.subn(repl_article, text, count=1)
    if count == 0:
        raise SystemExit(f"ERROR: no encuentro article id={person_id} en personajes.html")
    return text

def build_section():
    cards = []
    for person_id, data in PERSON_MAP.items():
        links_html = []
        for label, href in data["links"]:
            external = href.startswith("http://") or href.startswith("https://")
            attrs = ' target="_blank" rel="noopener noreferrer"' if external else ''
            links_html.append(f'<a href="{href}"{attrs}>{label} →</a>')
        cards.append(f'''<article class="p47c-escritos-card" id="escritos-{person_id}">
  <span class="p47c-escritos-status">{data["status"]}</span>
  <h3>{data["title"]}</h3>
  <p>{data["note"]}</p>
  <div class="p47c-escritos-links">{"".join(links_html)}</div>
</article>''')
    return f'''{START}
<section class="p47c-escritos-section" aria-labelledby="escritos-personajes-title">
  <div class="p36-wrap">
    <span class="p36-eyebrow">Escritos y pruebas por personaje</span>
    <h2 id="escritos-personajes-title">Dónde leer a cada personaje</h2>
    <p class="p36-note">Cada botón "Ir a sus escritos" lleva primero a esta zona, para evitar saltos genéricos y separar claramente documento directo, página de contexto o estado pendiente.</p>
    <div class="p47c-escritos-grid">
      {''.join(cards)}
    </div>
  </div>
</section>
{END}'''

def insert_section(text):
    text = remove_block(text, START, END)
    section = build_section()
    marker = re.search(r'<section\b[^>]*class=["\'][^"\']*\bp36-section\b[^"\']*["\'][^>]*>\s*<div\b[^>]*class=["\']p36-wrap["\'][^>]*>\s*<h2>\s*Criterio de imágenes', text, flags=re.I)
    return text[:marker.start()] + section + "\n" + text[marker.start():] if marker else text.replace("</main>", section + "\n</main>", 1)

def main():
    if not TARGET.exists():
        raise SystemExit("ERROR: no existe personajes.html")
    text = read(TARGET)
    text = add_style(text)
    text = clean_menu(text)
    for old_start, old_end in [
        ("<!-- V4_6B_2_PERSONAJES_PRUEBAS_DIRECTAS_START -->", "<!-- V4_6B_2_PERSONAJES_PRUEBAS_DIRECTAS_END -->"),
        ("<!-- V4_6B_3_PERSONAJES_IR_A_SUS_ESCRITOS_START -->", "<!-- V4_6B_3_PERSONAJES_IR_A_SUS_ESCRITOS_END -->"),
    ]:
        text = remove_block(text, old_start, old_end)
    for person_id in PERSON_MAP:
        text = patch_article_link(text, person_id)
    text = insert_section(text)
    write(TARGET, text)
    print("OK personajes.html actualizado")
    print("- Profundizar limpio de Glosario/FAQ.")
    print("- Todos los botones principales dicen 'Ir a sus escritos →'.")
    print("- Cada botón apunta a una sección fija #escritos-<personaje>.")
    print("- Añadida sección 'Dónde leer a cada personaje'.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
