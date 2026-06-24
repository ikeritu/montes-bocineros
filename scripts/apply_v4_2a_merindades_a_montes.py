#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V4.2A — actualización narrativa pública: de las merindades a los montes.

Ejecutar desde la raíz del repo:
    python scripts/apply_v4_2a_merindades_montes.py

Toca solo páginas públicas narrativas si existen:
- cronologia.html
- historia.html
- veredicto.html
- guia-lector.html

No sustituye páginas completas. Inserta bloques marcados con:
<!-- V4.2A_MERINDADES_MONTES_START -->
<!-- V4.2A_MERINDADES_MONTES_END -->
"""

from __future__ import annotations

from pathlib import Path
import re

ROOT = Path.cwd()

START = "<!-- V4.2A_MERINDADES_MONTES_START -->"
END = "<!-- V4.2A_MERINDADES_MONTES_END -->"

STYLE_ID = "v42a-merindades-style"

STYLE_BLOCK = f"""
<style id="{STYLE_ID}">
.v42a-merindades-box {{
  margin: clamp(1.25rem, 3vw, 2.25rem) 0;
  padding: clamp(1rem, 2.5vw, 1.35rem);
  border: 1px solid rgba(125, 92, 52, .25);
  border-radius: 18px;
  background: linear-gradient(135deg, rgba(253, 248, 235, .92), rgba(245, 239, 221, .72));
  box-shadow: 0 12px 30px rgba(51, 38, 22, .08);
}}
.v42a-merindades-box h2,
.v42a-merindades-box h3 {{
  margin-top: 0;
}}
.v42a-merindades-kicker {{
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  margin-bottom: .55rem;
  font-size: .82rem;
  font-weight: 800;
  letter-spacing: .055em;
  text-transform: uppercase;
  color: #6f4d21;
}}
.v42a-merindades-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
  gap: .75rem;
  margin-top: 1rem;
}}
.v42a-merindades-pill {{
  padding: .75rem .85rem;
  border-radius: 14px;
  background: rgba(255,255,255,.65);
  border: 1px solid rgba(125, 92, 52, .16);
}}
.v42a-merindades-pill strong {{
  display: block;
  margin-bottom: .25rem;
}}
.v42a-merindades-caution {{
  margin-top: 1rem;
  padding: .8rem .95rem;
  border-left: 4px solid #9b6b27;
  background: rgba(255,255,255,.7);
  border-radius: 12px;
}}
</style>
""".strip()

MAIN_BLOCK_H2 = f"""{START}
<section class="v42a-merindades-box" aria-labelledby="v42a-merindades-title">
  <span class="v42a-merindades-kicker">Actualización V4.2A · lectura documental</span>
  <h2 id="v42a-merindades-title">De las merindades a los montes</h2>
  <p>La línea documental más fuerte no apunta primero a una red medieval de cinco cumbres concretas, sino a una fórmula institucional: <strong>cinco bocinas</strong>, <strong>Gernika/Garnica</strong>, <strong>Junta General</strong>, <strong>cinco merindades</strong> y oficios como <strong>vozineros/bocineros</strong> y <strong>sayones</strong>.</p>
  <div class="v42a-merindades-grid">
    <div class="v42a-merindades-pill"><strong>Capa antigua</strong><span>Bocinas, merindades, Gernika y convocatoria de Junta.</span></div>
    <div class="v42a-merindades-pill"><strong>Capa intermedia</strong><span>Llorente y Madoz transmiten o reinterpretan la fórmula en clave erudita.</span></div>
    <div class="v42a-merindades-pill"><strong>Capa literaria</strong><span>Trueba desplaza la tradición hacia un paisaje simbólico de montes.</span></div>
    <div class="v42a-merindades-pill"><strong>Capa fijada</strong><span>La lista Gorbeia, Oiz, Sollube, Ganekogorta y Kolitza/Colisa se consolida tarde.</span></div>
  </div>
  <p class="v42a-merindades-caution"><strong>Cautela:</strong> cinco bocinas no equivale automáticamente a cinco montes. La lista nominal moderna no queda probada como medieval por las fuentes revisadas.</p>
</section>
{END}"""

MAIN_BLOCK_H3 = MAIN_BLOCK_H2.replace("<h2 id=", "<h3 id=").replace("</h2>", "</h3>")

SHORT_BLOCK = f"""{START}
<section class="v42a-merindades-box" aria-labelledby="v42a-guia-merindades-title">
  <span class="v42a-merindades-kicker">Clave de lectura V4.2A</span>
  <h2 id="v42a-guia-merindades-title">La pregunta ya no es solo “qué montes eran”</h2>
  <p>La investigación apunta a una transformación: de una fórmula antigua de <strong>cinco bocinas, merindades, Gernika y Junta General</strong> hacia una tradición posterior de <strong>cinco montes simbólicos</strong>.</p>
  <p class="v42a-merindades-caution"><strong>Regla rápida:</strong> cuando una fuente antigua dice “cinco bocinas”, no está enumerando por sí sola Gorbeia, Oiz, Sollube, Ganekogorta y Kolitza/Colisa.</p>
</section>
{END}"""

VEREDICT_BLOCK = f"""{START}
<section class="v42a-merindades-box" aria-labelledby="v42a-veredicto-merindades-title">
  <span class="v42a-merindades-kicker">Matiz clave V4.2A</span>
  <h2 id="v42a-veredicto-merindades-title">Qué prueba la línea medieval y qué no</h2>
  <p><strong>Sí refuerza:</strong> una tradición institucional de cinco bocinas vinculada a Gernika/Garnica, Junta General, merindades y oficios.</p>
  <p><strong>No prueba:</strong> una lista medieval cerrada de cinco montes concretos con los nombres Gorbeia, Oiz, Sollube, Ganekogorta y Kolitza/Colisa.</p>
  <p>La tesis queda más sólida precisamente porque distingue la capa documental antigua de la fijación paisajística posterior.</p>
</section>
{END}"""


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def ensure_style(text: str) -> str:
    if STYLE_ID in text:
        return text
    if "</head>" in text:
        return text.replace("</head>", STYLE_BLOCK + "\n</head>", 1)
    return STYLE_BLOCK + "\n" + text


def remove_old_block(text: str) -> str:
    pattern = re.escape(START) + r"[\s\S]*?" + re.escape(END)
    return re.sub(pattern, "", text).strip() + "\n"


def insert_before_first(text: str, markers: list[str], block: str) -> str:
    for marker in markers:
        idx = text.find(marker)
        if idx != -1:
            return text[:idx] + block + "\n" + text[idx:]
    return text + "\n" + block + "\n"


def insert_after_first(text: str, markers: list[str], block: str) -> str:
    for marker in markers:
        idx = text.find(marker)
        if idx != -1:
            idx2 = idx + len(marker)
            return text[:idx2] + "\n" + block + "\n" + text[idx2:]
    return text + "\n" + block + "\n"


def patch_page(name: str, block: str, mode: str) -> bool:
    path = ROOT / name
    if not path.exists():
        print(f"SKIP no existe: {name}")
        return False

    text = read(path)
    text = ensure_style(remove_old_block(text))

    if mode == "after_header":
        text = insert_after_first(text, ["</header>", "</nav>"], block)
    elif mode == "before_main_end":
        text = insert_before_first(text, ["</main>", "</body>"], block)
    elif mode == "after_first_h1":
        m = re.search(r"</h1>", text, flags=re.I)
        if m:
            pos = m.end()
            text = text[:pos] + "\n" + block + "\n" + text[pos:]
        else:
            text = insert_after_first(text, ["</header>", "</nav>"], block)
    else:
        text = insert_before_first(text, ["</main>", "</body>"], block)

    write(path, text)
    print(f"OK actualizado: {name}")
    return True


def main() -> int:
    changed = []

    if patch_page("historia.html", MAIN_BLOCK_H2, "after_header"):
        changed.append("historia.html")
    if patch_page("cronologia.html", MAIN_BLOCK_H2, "after_header"):
        changed.append("cronologia.html")
    if patch_page("veredicto.html", VEREDICT_BLOCK, "after_header"):
        changed.append("veredicto.html")
    if patch_page("guia-lector.html", SHORT_BLOCK, "after_header"):
        changed.append("guia-lector.html")

    if not changed:
        raise SystemExit("ERROR: no se actualizó ninguna página esperada.")

    print("\nPáginas actualizadas:")
    for item in changed:
        print(f"- {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
