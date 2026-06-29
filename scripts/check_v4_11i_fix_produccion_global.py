#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path.cwd()
REPORT = ROOT / "QA_V4_11I_FIX_PRODUCCION_GLOBAL_REPORT.md"

OLD_HREFS = [
    "glosario.html",
    "fuentes.html",
    "cadena-trueba.html",
    "barrio-banales.html",
    "citas.html",
    "archivo-tecnico.html",
    "metodologia.html",
    "citar.html",
    "afirmaciones.html",
]

BAD_PUBLIC_TEXT = [
    "[Propuesta interactiva:",
    "absorbe la antigua página",
    "antigua página de afirmaciones",
    "Trueba V2.5",
    "Búsqueda ciega V2.3a",
    "Búsqueda ciega V2.3",
]

HEADER_RE = re.compile(r'<header\b(?=[^>]*class=["\'][^"\']*\bsite-header\b[^"\']*["\'])[\s\S]*?</header>', re.I)
NAV_RE = re.compile(r'<nav\b(?=[^>]*class=["\'][^"\']*\bnav-simple\b[^"\']*["\'])[\s\S]*?</nav>', re.I)
SUPPORT_RE = re.compile(r'<section\b(?=[^>]*class=["\'][^"\']*\bglobal-support\b[^"\']*["\'])(?=[^>]*aria-label=["\']Apoyar el proyecto["\'])[\s\S]*?</section>', re.I)
FOOTER_RE = re.compile(r'<footer\b(?=[^>]*class=["\'][^"\']*\bv341-footer\b[^"\']*["\'])[\s\S]*?</footer>', re.I)

def read(path):
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

def main() -> int:
    errors = []
    lines = ["# QA V4.11I — Corrección de producción global", ""]

    html_files = sorted(ROOT.glob("*.html"))
    if not html_files:
        errors.append("FAIL no hay HTML en raíz")

    css = ROOT / "assets" / "v411i-production-polish.css"
    if css.exists():
        lines.append("OK existe assets/v411i-production-polish.css")
    else:
        errors.append("FAIL falta assets/v411i-production-polish.css")

    canonical_nav = None
    canonical_footer = None
    canonical_header = None

    for path in html_files:
        txt = read(path)

        for href, label in [
            ("assets/v411d-nav-footer.css", "CSS V4.11D"),
            ("assets/v411e-footer-support.css", "CSS V4.11E"),
            ("assets/v411i-production-polish.css", "CSS V4.11I"),
        ]:
            if href in txt:
                lines.append(f"OK {path.name}: {label} enlazado")
            else:
                errors.append(f"FAIL {path.name}: no enlaza {label}")

        header = HEADER_RE.search(txt)
        nav = NAV_RE.search(txt)
        footer = FOOTER_RE.search(txt)
        support = SUPPORT_RE.findall(txt)

        if header:
            h = re.sub(r"\s+", " ", header.group(0)).strip()
            if canonical_header is None:
                canonical_header = h
            elif h != canonical_header:
                errors.append(f"FAIL {path.name}: header no coincide con el canónico")
            lines.append(f"OK {path.name}: header presente")
        else:
            errors.append(f"FAIL {path.name}: header ausente")

        if nav:
            n = re.sub(r"\s+", " ", nav.group(0)).strip()
            if canonical_nav is None:
                canonical_nav = n
            elif n != canonical_nav:
                errors.append(f"FAIL {path.name}: nav-simple no coincide con el canónico")
            if "Síntesis crítica" in nav.group(0) and "Conclusión" not in nav.group(0):
                lines.append(f"OK {path.name}: nav usa Síntesis crítica")
            else:
                errors.append(f"FAIL {path.name}: nav no usa nomenclatura correcta")
        else:
            errors.append(f"FAIL {path.name}: nav-simple ausente")

        if len(support) == 1:
            lines.append(f"OK {path.name}: bloque Apoyar único")
        else:
            errors.append(f"FAIL {path.name}: bloques Apoyar = {len(support)}")

        if footer:
            f = re.sub(r"\s+", " ", footer.group(0)).strip()
            if canonical_footer is None:
                canonical_footer = f
            elif f != canonical_footer:
                errors.append(f"FAIL {path.name}: footer no coincide con el canónico")
            if "<h4>Información</h4>" in footer.group(0) and "<h4>Contacto</h4>" in footer.group(0):
                lines.append(f"OK {path.name}: footer Información/Contacto")
            else:
                errors.append(f"FAIL {path.name}: footer no contiene Información/Contacto")
            if "ko-fi.com/ikeritu" in footer.group(0) or "paypal.me/ikeritus" in footer.group(0) or "<h4>Apoyar</h4>" in footer.group(0):
                errors.append(f"FAIL {path.name}: footer conserva apoyo duplicado")
        else:
            errors.append(f"FAIL {path.name}: footer ausente")

        for old in OLD_HREFS:
            if ('href="' + old) in txt or ("href='" + old) in txt:
                errors.append(f"FAIL {path.name}: conserva href antiguo a {old}")

        for bad in BAD_PUBLIC_TEXT:
            if bad in txt:
                errors.append(f"FAIL {path.name}: conserva texto interno visible: {bad}")

    biblioteca = read(ROOT / "biblioteca.html")
    if 'id="bibliotecaEmpty" hidden' in biblioteca and "empty.hidden" in biblioteca:
        lines.append("OK biblioteca.html: mensaje vacío oculto y controlado por JS")
    else:
        errors.append("FAIL biblioteca.html: bibliotecaEmpty no está oculto/controlado correctamente")

    veredicto = read(ROOT / "veredicto.html")
    if "assets/veredicto-rediseno.css" in veredicto and "El veredicto en 30 segundos" in veredicto:
        lines.append("OK veredicto.html: rediseño interactivo presente")
    else:
        errors.append("FAIL veredicto.html: rediseño interactivo V4.11H no detectado")

    montes = read(ROOT / "montes.html")
    if all(x in montes for x in ["ondas-gernika.js", "eco-acustico-v33.js", "Ver cómo viajaba el aviso"]):
        lines.append("OK montes.html: animaciones de ondas/radar detectadas")
    else:
        errors.append("FAIL montes.html: animaciones de ondas/radar no detectadas")

    index = read(ROOT / "index.html")
    if "relieve-3d-index.css" in index and 'id="v34-relief"' in index:
        lines.append("OK index.html: hero relieve detectado")
    else:
        errors.append("FAIL index.html: hero relieve no detectado")

    if errors:
        lines += ["", "## Errores"] + errors

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("\nRESULTADO:", "PASS" if not errors else "FAIL")
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
