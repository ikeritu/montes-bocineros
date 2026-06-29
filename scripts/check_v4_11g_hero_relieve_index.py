#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re
ROOT=Path.cwd(); REPORT=ROOT/"QA_V4_11G_HERO_RELIEVE_INDEX_REPORT.md"
def read(p): return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
def main():
    errors=[]; lines=["# QA V4.11G — Hero animado de relieve en portada",""]
    html=read(ROOT/"index.html"); css=read(ROOT/"assets/relieve-3d-index.css"); js=read(ROOT/"assets/relieve-3d-index.js")
    checks=[
      ("existe index.html",(ROOT/"index.html").exists()),
      ("existe assets/relieve-3d-index.css",(ROOT/"assets/relieve-3d-index.css").exists()),
      ("existe assets/relieve-3d-index.js",(ROOT/"assets/relieve-3d-index.js").exists()),
      ("index enlaza CSS de relieve","assets/relieve-3d-index.css" in html),
      ("index enlaza JS de relieve","assets/relieve-3d-index.js" in html),
      ("index contiene #v34-relief",'id="v34-relief"' in html or "id='v34-relief'" in html),
      ("#v34-relief es aria-hidden", re.search(r'<div[^>]+aria-hidden=["\']true["\'][^>]+id=["\']v34-relief["\']|<div[^>]+id=["\']v34-relief["\'][^>]+aria-hidden=["\']true["\']', html, re.I) is not None),
      ("bloque Apoyar no duplicado", html.count('aria-label="Apoyar el proyecto"') <= 1),
      ("se mantiene footer", "<footer" in html and "v341-footer" in html),
      ("se mantiene menú Profundizar", "menu-global" in html and "Profundizar" in html),
      ("CSS respeta prefers-reduced-motion", "prefers-reduced-motion" in css),
      ("JS usa requestAnimationFrame", "requestAnimationFrame" in js),
    ]
    for label, ok in checks:
        if ok: lines.append(f"OK {label}")
        else: errors.append(f"FAIL {label}")
    for old in ["fuentes.html","cadena-trueba.html","barrio-banales.html","citas.html","archivo-tecnico.html","metodologia.html","citar.html","afirmaciones.html"]:
        if f'href="{old}' in html or f"href='{old}" in html: errors.append(f"FAIL index conserva href antiguo a {old}")
    if errors: lines += ["","## Errores"] + errors
    REPORT.write_text("\n".join(lines)+"\n", encoding="utf-8")
    print("\n".join(lines)); print("\nRESULTADO:", "PASS" if not errors else "FAIL")
    return 0 if not errors else 1
if __name__ == "__main__": raise SystemExit(main())
