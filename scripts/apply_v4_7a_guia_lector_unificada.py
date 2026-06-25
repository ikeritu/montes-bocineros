#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path.cwd()
GUIDE = ROOT / "guia-lector.html"
GLOSSARY = ROOT / "glosario.html"

FAQ_CANDIDATES = ["preguntas-frecuentes.html", "preguntas.html", "faq.html", "faqs.html"]

START = "<!-- V4_7A_GUIA_LECTOR_UNIFICADA_START -->"
END = "<!-- V4_7A_GUIA_LECTOR_UNIFICADA_END -->"
STYLE_ID = "v47a-guia-lector-unificada-style"

STYLE = """
<style id="v47a-guia-lector-unificada-style">
.v47a-glosario-integrado {
  margin: clamp(1.5rem, 4vw, 3rem) 0;
  padding: clamp(1rem, 2.5vw, 1.45rem);
  border: 1px solid rgba(31, 107, 85, .22);
  border-radius: 20px;
  background: linear-gradient(135deg, rgba(246, 252, 248, .98), rgba(246, 241, 231, .82));
  box-shadow: 0 12px 30px rgba(28,45,38,.08);
  scroll-margin-top: 7rem;
}
.v47a-glosario-integrado h2,
.v47a-glosario-integrado h3 { margin-top: 0; }
.v47a-glosario-integrado .v47a-kicker {
  display:inline-flex;
  margin-bottom:.55rem;
  font-size:.78rem;
  font-weight:800;
  letter-spacing:.055em;
  text-transform:uppercase;
  color:#1f6b55;
}
.v47a-glosario-integrado .v47a-note { margin:.75rem 0 1rem; color:#4b5a53; }
</style>
""".strip()

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")

def remove_block(text: str, start: str, end: str) -> str:
    return re.sub(re.escape(start) + r"[\s\S]*?" + re.escape(end), "", text).strip() + "\n"

def strip_outer_main_or_body(html: str) -> str:
    m = re.search(r"<main\b[^>]*>([\s\S]*?)</main>", html, flags=re.I)
    if m:
        content = m.group(1)
    else:
        b = re.search(r"<body\b[^>]*>([\s\S]*?)</body>", html, flags=re.I)
        content = b.group(1) if b else html

    content = re.sub(r"<header\b[\s\S]*?</header>", "", content, flags=re.I)
    content = re.sub(r"<nav\b[\s\S]*?</nav>", "", content, flags=re.I)
    content = re.sub(r"<footer\b[\s\S]*?</footer>", "", content, flags=re.I)
    content = re.sub(r"<script\b[\s\S]*?</script>", "", content, flags=re.I)
    content = re.sub(r"<style\b[\s\S]*?</style>", "", content, flags=re.I)
    return content.strip()

def add_style(html: str) -> str:
    if STYLE_ID in html:
        return html
    if "</head>" in html:
        return html.replace("</head>", STYLE + "\n</head>", 1)
    return STYLE + "\n" + html

def build_glossary_block(glossary_html: str) -> str:
    content = strip_outer_main_or_body(glossary_html)
    content = re.sub(r"<h1\b[^>]*>[\s\S]*?</h1>", "", content, count=1, flags=re.I).strip()
    return f"""{START}
<section id="glosario" class="v47a-glosario-integrado" aria-labelledby="glosario-integrado-title">
  <span class="v47a-kicker">Guía del lector · glosario integrado</span>
  <h2 id="glosario-integrado-title">Glosario y términos clave</h2>
  <p class="v47a-note">Esta sección integra el antiguo glosario para que la guía del lector concentre en una sola página las ayudas de lectura, términos y cautelas básicas del proyecto.</p>
  {content}
</section>
{END}"""

def insert_block(html: str, block: str) -> str:
    html = remove_block(html, START, END)
    html = add_style(html)
    if "</main>" in html:
        return html.replace("</main>", block + "\n</main>", 1)
    if "</body>" in html:
        return html.replace("</body>", block + "\n</body>", 1)
    return html + "\n" + block + "\n"

def update_links(text: str) -> str:
    text = text.replace("Preguntas frecuentes", "Guía del lector")
    text = text.replace("preguntas frecuentes", "guía del lector")
    for filename in FAQ_CANDIDATES:
        text = re.sub(rf'(["\']){re.escape(filename)}(?:#[^"\']*)?\1', r'\1guia-lector.html\1', text, flags=re.I)
    text = re.sub(r'(["\'])glosario\.html(#[^"\']+)\1', r'\1guia-lector.html\2\1', text, flags=re.I)
    text = re.sub(r'(["\'])glosario\.html\1', r'\1guia-lector.html#glosario\1', text, flags=re.I)
    return text

def main() -> int:
    if not GUIDE.exists():
        raise SystemExit("ERROR: no existe guia-lector.html")

    glossary_html = read(GLOSSARY) if GLOSSARY.exists() else "<p><strong>Glosario pendiente:</strong> no se encontró glosario.html durante la integración.</p>"

    guide_html = update_links(read(GUIDE))
    guide_html = insert_block(guide_html, build_glossary_block(glossary_html))
    write(GUIDE, guide_html)
    print("OK actualizado: guia-lector.html con glosario integrado")

    updated = []
    for path in sorted(ROOT.glob("*.html")):
        if path.name == "glosario.html":
            continue
        text = read(path)
        new = update_links(text)
        if new != text:
            write(path, new)
            updated.append(path.name)

    for name in updated:
        print(f"OK enlaces/texto actualizados: {name}")

    if GLOSSARY.exists():
        GLOSSARY.unlink()
        print("OK eliminado: glosario.html")

    for name in FAQ_CANDIDATES:
        path = ROOT / name
        if path.exists():
            path.unlink()
            print(f"OK eliminado: {name}")

    print("\nResumen:")
    print("- Profundizar deja de mostrar Preguntas frecuentes como entrada separada.")
    print("- Guía del lector concentra guía + glosario.")
    print("- glosario.html queda eliminado como subpágina independiente.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
