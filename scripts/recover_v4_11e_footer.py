from pathlib import Path
import re

ROOT = Path(".")

SUPPORT_BLOCK = """<section aria-label="Apoyar el proyecto" class="global-support">
<div class="global-support-copy"><span class="support-kicker">Apoyar el proyecto</span><strong>¿Te ha servido esta investigación?</strong><span>Ayuda a mantener y ampliar este trabajo documental.</span></div>
<div class="support-buttons"><a class="support-card kofi" href="https://ko-fi.com/ikeritu" rel="noopener noreferrer" target="_blank"><span aria-hidden="true" class="support-icon">☕</span><span><strong>Ko-fi</strong><small>ko-fi.com/ikeritu</small></span></a><a class="support-card paypal" href="https://www.paypal.com/paypalme/ikeritus" rel="noopener noreferrer" target="_blank"><span aria-hidden="true" class="support-icon">💙</span><span><strong>PayPal</strong><small>paypal.me/ikeritus</small></span></a></div>
</section>"""

FOOTER_BLOCK = """<footer aria-label="Pie de página" class="v341-footer">
<div class="v341-footer-wrap">
<div class="v341-footer-brand">
<h4>Montes Bocineros de Bizkaia</h4>
<p>Investigación histórico-divulgativa: tradición viva, fuentes verificables y cautela documental.</p>
</div>
<div>
<h4>Información</h4>
<nav aria-label="Información del proyecto" class="v341-footer-links">
<a href="archivo.html">Archivo</a>
<a href="biblioteca.html">Biblioteca documental</a>
<a href="personajes.html">Personajes</a>
<a href="metodo-citacion.html">Método y citación</a>
<a href="autor.html">Autoría y correcciones</a>
</nav>
</div>
<div>
<h4>Contacto</h4>
<nav aria-label="Contacto" class="v341-footer-links">
<a href="mailto:iker.ituarte.tejedor@gmail.com?subject=Correccion%20Montes%20Bocineros">✉ Enviar corrección</a>
</nav>
</div>
</div>
</footer>"""

CSS_TEXT = """/* V4.11E · Footer único sin apoyo duplicado */
.global-support{width:min(1180px,calc(100% - 2rem));margin:clamp(2.5rem,5vw,4rem) auto 1.2rem;padding:1.25rem 1.45rem;border:1px solid rgba(1180px,calc(100% - 2rem));margin:clamp(2.5rem,5vw,4rem) auto 1.2rem;padding:1.25rem 1.45rem;border:1px solid rgba(19,63,53,.16);border-radius:24px;background:linear-gradient(135deg,rgba(255,253,248,.94),rgba(238,247,242,.88));box-shadow:0 20px 50px -38px rgba(19,63,53,.45);display:flex;align-items:center;justify-content:space-between;gap:1.4rem}
.global-support-copy{display:grid;gap:.28rem;color:#123f35}.support-kicker{width:min(420px,100%);border-radius:999px;padding:.28rem .7rem;background:rgba(19,63,53,.08);color:#0e4b3e;font-size:.78rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase}.global-support-copy strong{font-size:1.18rem;line-height:1.25}.global-support-copy span:last-child{color:#475952;font-weight:600}
.support-buttons{display:flex;flex-wrap:wrap;gap:.75rem;justify-content:flex-end}.support-card{min-width:190px;display:flex;align-items:center;gap:.75rem;padding:.82rem 1rem;border-radius:18px;background:#fffdf8;border:1px solid rgba(19,63,53,.14);color:#123f35;text-decoration:none;box-shadow:0 12px 26px -22px rgba(19,63,53,.5)}.support-card:hover{transform:translateY(-1px);box-shadow:0 18px 34px -24px rgba(19,63,53,.55)}.support-card strong{display:block;line-height:1.1}.support-card small{display:block;margin-top:.16rem;color:#51645c;font-weight:700}.support-icon{width:2.3rem;height:2.3rem;display:grid;place-items:center;border-radius:14px;background:rgba(185,119,47,.12)}.support-card.paypal .support-icon{background:rgba(71,132,255,.14)}
.v341-footer{margin-top:0;background:#0f463a;color:#f5f0e7}.v341-footer-wrap{width:min(1180px,calc(100% - 2rem));margin-inline:auto;padding:clamp(2.2rem,4vw,3.6rem) 0;display:grid;grid-template-columns:minmax(220px,1.2fr) minmax(220px,.9fr) minmax(220px,.75fr);gap:clamp(1.6rem,5vw,4rem)}.v341-footer h4{margin:0 0 .8rem;color:#fff7e6}.v341-footer p{max-width:34ch;margin:0;color:#f4efe2;line-height:1.65}.v341-footer-links{display:grid;gap:.58rem}.v341-footer-links a{color:#f5b84c;text-decoration:none;overflow-wrap:anywhere}.v341-footer-links a:hover{color:#ffd782;text-decoration:underline}
@media(max-width:800px){.global-support{align-items:flex-start;flex-direction:column}.support-buttons{width:100%;justify-content:flex-start}.support-card{width:100%;min-width:0}.v341-footer-wrap{grid-template-columns:1fr}}
"""

REPLACEMENTS = {
    "fuentes.html#tabla": "biblioteca.html#tabla-maestra-fuentes",
    "fuentes.html": "biblioteca.html#tabla-maestra-fuentes",
    "cadena-trueba.html#trueba-facsimil": "biblioteca.html#trueba",
    "cadena-trueba.html#llorente-madoz-trueba": "biblioteca.html#madoz-llorente-trueba",
    "cadena-trueba.html#recepcion": "biblioteca.html#recepcion-trueba",
    "cadena-trueba.html#busqueda-ciega-v23a": "biblioteca.html#cadena-trueba",
    "cadena-trueba.html": "biblioteca.html#cadena-trueba",
    "barrio-banales.html": "biblioteca.html#barrio-banales",
    "citas.html": "biblioteca.html#citas-verificadas",
    "archivo-tecnico.html#busqueda-ciega-v23a": "biblioteca.html#archivo-tecnico",
    "archivo-tecnico.html": "biblioteca.html#archivo-tecnico",
    "informes.html": "biblioteca.html#informes-ia",
    "pendientes-documentales.html": "biblioteca.html#pendientes-documentales",
    "metodologia.html": "metodo-citacion.html#metodologia",
    "citar.html": "metodo-citacion.html#como-citar",
    "afirmaciones.html": "metodo-citacion.html#afirmaciones",
}

support_re = re.compile(
    r'\s*<section\b(?=[^>]*class=["\'][^"\']*\bglobal-support\b[^"\']*["\'])(?=[^>]*aria-label=["\']Apoyar el proyecto["\'])[\s\S]*?</section>\s*',
    re.I
)

footer_re = re.compile(r'\s*<footer\b[\s\S]*?</footer>\s*', re.I)

def read(path):
    return path.read_text(encoding="utf-8", errors="replace")

def write(path, txt):
    path.write_text(txt, encoding="utf-8")

def ensure_css_file():
    css_path = ROOT / "assets" / "v411e-footer-support.css"
    css_path.parent.mkdir(parents=True, exist_ok=True)
    css_path.write_text(CSS_TEXT, encoding="utf-8")

def ensure_css_link(txt):
    if "assets/v411e-footer-support.css" in txt:
        return txt

    link = '<link rel="stylesheet" href="assets/v411e-footer-support.css?v=4.11e"/>'

    if "</head>" in txt:
        return txt.replace("</head>", link + "\n</head>", 1)

    return link + "\n" + txt

def normalize_html(txt):
    for old, new in REPLACEMENTS.items():
        txt = txt.replace(old, new)

    txt = txt.replace('defer="True"', "defer").replace("defer='True'", "defer")

    # Eliminar todos los apoyos previos.
    txt = support_re.sub("\n", txt)

    # Eliminar cualquier footer previo, aunque no sea v341.
    txt = footer_re.sub("\n", txt)

    # Insertar bloque único antes de </body>.
    final_block = "\n" + SUPPORT_BLOCK + "\n" + FOOTER_BLOCK + "\n"

    if "</body>" in txt:
        txt = txt.replace("</body>", final_block + "</body>", 1)
    else:
        txt = txt + final_block

    txt = ensure_css_link(txt)
    txt = re.sub(r"\n{4,}", "\n\n", txt)

    return txt

def main():
    ensure_css_file()

    changed = []

    for path in sorted(ROOT.glob("*.html")):
        old = read(path)
        new = normalize_html(old)

        if old != new:
            write(path, new)
            changed.append(path.name)

    print("OK recuperación V4.11E aplicada")
    print("HTML modificados:", ", ".join(changed) if changed else "ninguno")

if __name__ == "__main__":
    main()
