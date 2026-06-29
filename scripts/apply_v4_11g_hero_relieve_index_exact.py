#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V4.11G — Hero animado de relieve en portada EXACTO.

Este parche integra la animación exacta aportada por el usuario:
- assets/relieve-3d-index.css
- assets/relieve-3d-index.js

No sustituye index.html completo.
No toca menú Profundizar.
No toca footer V4.11E.
No toca bloque Apoyar.
"""

from pathlib import Path
import re
import shutil

ROOT = Path.cwd()
PACKAGE_ROOT = Path(__file__).resolve().parent.parent

CSS_HREF = "assets/relieve-3d-index.css"
JS_SRC = "assets/relieve-3d-index.js"
RELIEF_DIV = '<div aria-hidden="true" class="v34-relief" id="v34-relief"></div>'

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")

def copy_asset(rel: str) -> None:
    src = PACKAGE_ROOT / rel
    dst = ROOT / rel
    if not src.exists():
        raise SystemExit(f"ERROR: falta {rel} en el paquete")
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.resolve() != dst.resolve():
        shutil.copy2(src, dst)

def ensure_css_link(html: str) -> str:
    # Elimina duplicados previos del mismo asset.
    html = re.sub(r'\s*<link[^>]+href=["\']assets/relieve-3d-index\.css[^"\']*["\'][^>]*/?>', '', html, flags=re.I)
    link = '<link rel="stylesheet" href="assets/relieve-3d-index.css?v=1.0.0"/>'
    if "</head>" in html:
        return html.replace("</head>", link + "\n</head>", 1)
    return link + "\n" + html

def ensure_js_link(html: str) -> str:
    # Elimina duplicados previos del mismo asset.
    html = re.sub(r'\s*<script[^>]+src=["\']assets/relieve-3d-index\.js[^"\']*["\'][^>]*>\s*</script>', '', html, flags=re.I)
    script = '<script defer src="assets/relieve-3d-index.js?v=1.0.0"></script>'
    if "</body>" in html:
        return html.replace("</body>", script + "\n</body>", 1)
    return html + "\n" + script + "\n"

def ensure_relief_div(html: str) -> str:
    if 'id="v34-relief"' in html or "id='v34-relief'" in html:
        return html

    echo_match = re.search(
        r'(<div\s+aria-hidden=["\']true["\']\s+class=["\']v34-echo["\'][\s\S]*?</div>)',
        html,
        flags=re.I
    )
    if echo_match:
        return html[:echo_match.end()] + "\n" + RELIEF_DIV + html[echo_match.end():]

    hero_match = re.search(
        r'(<section\b[^>]*class=["\'][^"\']*\bv34-hero\b[^"\']*["\'][^>]*>)',
        html,
        flags=re.I
    )
    if hero_match:
        return html[:hero_match.end()] + "\n" + RELIEF_DIV + html[hero_match.end():]

    raise SystemExit("ERROR: no encuentro .v34-hero en index.html")

def main() -> int:
    index = ROOT / "index.html"
    if not index.exists():
        raise SystemExit("ERROR: no existe index.html en la raíz del repo")

    copy_asset("assets/relieve-3d-index.css")
    copy_asset("assets/relieve-3d-index.js")

    old = read(index)
    new = old
    new = ensure_css_link(new)
    new = ensure_relief_div(new)
    new = ensure_js_link(new)
    new = new.replace('defer="True"', "defer").replace("defer='True'", "defer")
    new = re.sub(r"\n{4,}", "\n\n", new)

    if new != old:
        write(index, new)
        print("OK V4.11G EXACTA aplicada: index.html modificado")
    else:
        print("OK V4.11G EXACTA: index.html ya estaba actualizado")

    print("- Copiados assets exactos: relieve-3d-index.css / relieve-3d-index.js")
    print("- No se sustituye index.html completo")
    print("- No se toca menú, footer ni apoyo")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
