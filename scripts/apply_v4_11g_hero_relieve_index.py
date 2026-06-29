#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V4.11G — Hero animado de relieve en portada.
Ejecutar desde la raíz del repo:
    py -3 scripts/apply_v4_11g_hero_relieve_index.py
"""
from pathlib import Path
import re, shutil
ROOT = Path.cwd(); PACKAGE_ROOT = Path(__file__).resolve().parent.parent
CSS_HREF = "assets/relieve-3d-index.css"; JS_SRC = "assets/relieve-3d-index.js"
RELIEF_DIV = '<div aria-hidden="true" class="v34-relief" id="v34-relief"></div>'
def read(p): return p.read_text(encoding="utf-8", errors="replace")
def write(p,t): p.write_text(t, encoding="utf-8")
def copy_assets():
    for rel in [CSS_HREF, JS_SRC]:
        src = PACKAGE_ROOT / rel; dst = ROOT / rel
        if not src.exists(): raise SystemExit(f"ERROR: falta {rel} en el paquete")
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.resolve() != dst.resolve(): shutil.copy2(src, dst)
def ensure_css(html):
    if CSS_HREF in html: return html
    link = '<link rel="stylesheet" href="assets/relieve-3d-index.css?v=4.11g"/>'
    return html.replace("</head>", link + "\n</head>", 1) if "</head>" in html else link + "\n" + html
def ensure_js(html):
    if JS_SRC in html: return html
    script = '<script defer src="assets/relieve-3d-index.js?v=4.11g"></script>'
    return html.replace("</body>", script + "\n</body>", 1) if "</body>" in html else html + "\n" + script + "\n"
def ensure_div(html):
    if 'id="v34-relief"' in html or "id='v34-relief'" in html: return html
    m = re.search(r'(<div\s+aria-hidden=["\']true["\']\s+class=["\']v34-echo["\'][\s\S]*?</div>)', html, re.I)
    if m: return html[:m.end()] + "\n" + RELIEF_DIV + html[m.end():]
    m = re.search(r'(<section\b[^>]*class=["\'][^"\']*\bv34-hero\b[^"\']*["\'][^>]*>)', html, re.I)
    if m: return html[:m.end()] + "\n" + RELIEF_DIV + html[m.end():]
    raise SystemExit("ERROR: no encuentro la sección .v34-hero en index.html")
def main():
    index = ROOT / "index.html"
    if not index.exists(): raise SystemExit("ERROR: no existe index.html")
    copy_assets()
    old = read(index); new = ensure_js(ensure_div(ensure_css(old))).replace('defer="True"','defer').replace("defer='True'","defer")
    if old != new: write(index,new); print("OK V4.11G aplicada: index.html modificado")
    else: print("OK V4.11G: index.html ya estaba actualizado")
    print("- Menú, footer y apoyo no se sustituyen")
    return 0
if __name__ == "__main__": raise SystemExit(main())
