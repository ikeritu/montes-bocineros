#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re
ROOT=Path.cwd()
REPORT=ROOT/"QA_V4_11E_FOOTER_SIN_APOYO_DUPLICADO_REPORT.md"
OLD=["fuentes.html","cadena-trueba.html","barrio-banales.html","citas.html","archivo-tecnico.html","informes.html","pendientes-documentales.html","metodologia.html","citar.html","afirmaciones.html"]
FOOTER_RE=re.compile(r'<footer\b(?=[^>]*class=["\'][^"\']*\bv341-footer\b[^"\']*["\'])[\s\S]*?</footer>',re.I)
SUPPORT_RE=re.compile(r'<section\b(?=[^>]*class=["\'][^"\']*\bglobal-support\b[^"\']*["\'])(?=[^>]*aria-label=["\']Apoyar el proyecto["\'])[\s\S]*?</section>',re.I)
def read(p): return p.read_text(encoding="utf-8",errors="replace") if p.exists() else ""
def main():
    errors=[]; lines=["# QA V4.11E — Footer sin apoyo duplicado",""]
    if (ROOT/"assets"/"v411e-footer-support.css").exists(): lines.append("OK existe assets/v411e-footer-support.css")
    else: errors.append("FAIL falta assets/v411e-footer-support.css")
    for p in sorted(ROOT.glob("*.html")):
        txt=read(p)
        if "assets/v411e-footer-support.css" in txt: lines.append(f"OK {p.name}: CSS V4.11E enlazado")
        else: errors.append(f"FAIL {p.name}: no enlaza CSS V4.11E")
        supports=SUPPORT_RE.findall(txt)
        if len(supports)==1: lines.append(f"OK {p.name}: un único bloque Apoyar")
        else: errors.append(f"FAIL {p.name}: bloques Apoyar encontrados = {len(supports)}")
        footers=FOOTER_RE.findall(txt)
        if len(footers)==1:
            footer=footers[0]
            if "<h4>Información</h4>" in footer and "<h4>Contacto</h4>" in footer: lines.append(f"OK {p.name}: footer Información/Contacto")
            else: errors.append(f"FAIL {p.name}: footer no contiene Información y Contacto")
            if "<h4>Apoyar</h4>" in footer or "ko-fi.com/ikeritu" in footer or "paypal.me/ikeritus" in footer: errors.append(f"FAIL {p.name}: footer conserva apoyo duplicado")
            else: lines.append(f"OK {p.name}: footer sin Ko-fi/PayPal duplicados")
            for req in ['href="archivo.html"','href="biblioteca.html"','href="personajes.html"','href="metodo-citacion.html"','href="autor.html"','mailto:iker.ituarte.tejedor@gmail.com']:
                if req in footer: lines.append(f"OK {p.name}: footer contiene {req}")
                else: errors.append(f"FAIL {p.name}: footer no contiene {req}")
        else:
            errors.append(f"FAIL {p.name}: footers encontrados = {len(footers)}")
        for old in OLD:
            if f'href="{old}' in txt or f"href='{old}" in txt: errors.append(f"FAIL {p.name}: conserva href antiguo a {old}")
    if errors: lines+=["","## Errores"]+errors
    REPORT.write_text("\n".join(lines)+"\n",encoding="utf-8")
    print("\n".join(lines)); print("\nRESULTADO:","PASS" if not errors else "FAIL")
    return 0 if not errors else 1
if __name__=="__main__": raise SystemExit(main())
