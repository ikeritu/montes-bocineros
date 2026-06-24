#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3.9 — QA navegación y enlaces internos
Ejecutar desde la raíz del repositorio:
    python scripts/check_v3_9_navigation_links.py

No modifica archivos. Solo audita:
- enlaces internos href/src en HTML;
- url(...) en CSS;
- anclas internas;
- header global;
- presencia accidental de Cronología como botón principal;
- typos conocidos.
"""

from __future__ import annotations

import html
import re
import sys
import urllib.parse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path.cwd().resolve()

EXPECTED_MAIN_NAV = [
    "Inicio",
    "Historia",
    "Montes",
    "Síntesis crítica",
    "Guía del lector",
    "Archivo",
]

KEY_FILES = [
    "index.html",
    "historia.html",
    "montes.html",
    "veredicto.html",
    "guia-lector.html",
    "archivo.html",
    "personajes.html",
    "fuentes.html",
    "trueba-facsimil.html",
    "llorente-madoz-trueba.html",
    "barrio-banales.html",
    "metodologia.html",
    "citas.html",
    "citar.html",
    "autor.html",
    "sitemap.xml",
    "llms.txt",
]

SKIP_DIRS = {
    ".git",
    ".github",
    "__pycache__",
    "node_modules",
    ".venv",
    "venv",
    "dist",
    "build",
}

SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
ATTR_RE = re.compile(r"""\b(?:href|src)=["']([^"']+)["']""", re.I)
CSS_URL_RE = re.compile(r"""url\(\s*['"]?([^'")]+)['"]?\s*\)""", re.I)
ID_RE = re.compile(r"""\b(?:id|name)=["']([^"']+)["']""", re.I)
NAV_RE = re.compile(
    r"""<nav[^>]*class=["'][^"']*\bnav-simple\b[^"']*["'][^>]*>(.*?)</nav>""",
    re.I | re.S,
)
A_RE = re.compile(r"""<a\b[^>]*>(.*?)</a>""", re.I | re.S)
TAG_RE = re.compile(r"<[^>]+>")


@dataclass
class Issue:
    severity: str
    file: str
    detail: str


def iter_files(pattern: str) -> Iterable[Path]:
    for path in ROOT.rglob(pattern):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file():
            yield path


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except Exception:
        return str(path)


def strip_tags(value: str) -> str:
    return html.unescape(TAG_RE.sub("", value)).strip()


def is_external(raw: str) -> bool:
    raw = raw.strip()
    if not raw:
        return True
    if raw.startswith("#"):
        return False
    if raw.startswith("//"):
        return True
    if SCHEME_RE.match(raw):
        scheme = raw.split(":", 1)[0].lower()
        return scheme in {
            "http",
            "https",
            "mailto",
            "tel",
            "javascript",
            "data",
            "blob",
            "sms",
            "geo",
        }
    return False


def target_for(base_file: Path, raw_url: str) -> tuple[Path, str | None] | None:
    raw_url = html.unescape(raw_url.strip())
    if not raw_url or is_external(raw_url):
        if raw_url.startswith("#"):
            return base_file, urllib.parse.unquote(raw_url[1:])
        return None

    parsed = urllib.parse.urlsplit(raw_url)
    path_part = urllib.parse.unquote(parsed.path)
    fragment = urllib.parse.unquote(parsed.fragment) if parsed.fragment else None

    if not path_part and fragment:
        return base_file, fragment

    if path_part.startswith("/montes-bocineros/"):
        target = ROOT / path_part[len("/montes-bocineros/") :]
    elif path_part.startswith("/"):
        target = ROOT / path_part.lstrip("/")
    else:
        target = base_file.parent / path_part

    if str(raw_url).endswith("/") or (not target.suffix and not target.name.startswith(".")):
        candidate = target / "index.html"
        if candidate.exists():
            target = candidate

    return target.resolve(), fragment


def anchors_in(path: Path) -> set[str]:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return set()
    return {html.unescape(m.group(1)) for m in ID_RE.finditer(text)}


def check_key_files(issues: list[Issue]) -> None:
    for item in KEY_FILES:
        if not (ROOT / item).exists():
            issues.append(Issue("ERROR", item, "Falta archivo clave esperado."))


def check_links(issues: list[Issue]) -> None:
    for file in iter_files("*.html"):
        text = file.read_text(encoding="utf-8", errors="ignore")
        for raw in ATTR_RE.findall(text):
            if raw.startswith("#"):
                anchor = urllib.parse.unquote(raw[1:])
                if anchor and anchor not in anchors_in(file):
                    issues.append(Issue("ERROR", rel(file), f"Ancla local inexistente: {raw}"))
                continue

            resolved = target_for(file, raw)
            if resolved is None:
                continue

            target, fragment = resolved
            if not target.exists():
                issues.append(Issue("ERROR", rel(file), f"Enlace/recurso interno inexistente: {raw} -> {rel(target)}"))
                continue

            if fragment and target.suffix.lower() in {".html", ".htm"}:
                if fragment not in anchors_in(target):
                    issues.append(Issue("ERROR", rel(file), f"Ancla inexistente: {raw} -> {rel(target)}#{fragment}"))


def check_css_urls(issues: list[Issue]) -> None:
    for file in iter_files("*.css"):
        text = file.read_text(encoding="utf-8", errors="ignore")
        for raw in CSS_URL_RE.findall(text):
            raw = raw.strip()
            if not raw or is_external(raw):
                continue
            parsed = urllib.parse.urlsplit(html.unescape(raw))
            path_part = urllib.parse.unquote(parsed.path)
            if not path_part:
                continue
            target = (file.parent / path_part).resolve()
            if not target.exists():
                issues.append(Issue("ERROR", rel(file), f"Recurso CSS inexistente: {raw} -> {rel(target)}"))


def check_header(issues: list[Issue]) -> None:
    html_files = list(iter_files("*.html"))
    for file in html_files:
        text = file.read_text(encoding="utf-8", errors="ignore")
        nav_match = NAV_RE.search(text)
        if not nav_match:
            # Algunas páginas puente podrían no tener header completo: aviso, no fallo.
            issues.append(Issue("WARN", rel(file), "No se encontró nav-simple. Revisar si es página puente intencionada."))
            continue

        nav_html = nav_match.group(1)
        labels = [strip_tags(m.group(1)) for m in A_RE.finditer(nav_html)]
        labels = [label for label in labels if label]

        if "Cronología" in labels:
            issues.append(Issue("ERROR", rel(file), "El header principal todavía contiene Cronología."))

        missing = [label for label in EXPECTED_MAIN_NAV if label not in labels]
        if missing:
            issues.append(Issue("ERROR", rel(file), f"Header principal incompleto. Faltan: {', '.join(missing)}. Detectado: {labels}"))

        # Orden exacto cuando contiene todos los esperados.
        if not missing:
            positions = [labels.index(label) for label in EXPECTED_MAIN_NAV]
            if positions != sorted(positions):
                issues.append(Issue("ERROR", rel(file), f"Header principal con orden inesperado. Detectado: {labels}"))


def check_known_typos(issues: list[Issue]) -> None:
    patterns = {
        "iturrriza": "Posible typo: usar Iturriza / iturriza.",
        "profudizar": "Posible typo: usar Profundizar.",
        'href="cronologia.html">Cronología</a>': "Cronología aparece como enlace de header o navegación principal.",
        'href="../cronologia.html">Cronología</a>': "Cronología aparece como enlace de header en subpágina.",
    }
    for file in list(iter_files("*.html")) + list(iter_files("*.md")) + list(iter_files("*.txt")):
        text = file.read_text(encoding="utf-8", errors="ignore")
        lowered = text.lower()
        for pattern, message in patterns.items():
            haystack = lowered if pattern.islower() else text
            needle = pattern if pattern.islower() else pattern
            if needle in haystack:
                issues.append(Issue("ERROR", rel(file), message))


def check_expected_content(issues: list[Issue]) -> None:
    checks = {
        "guia-lector.html": [
            "Cómo se cristalizó la lista",
            "En 20 segundos",
            "guia-lector-v3611.css",
        ],
        "archivo.html": [
            "archivo-v38.css",
            "Los nombres que más se consultan",
            "Línea roja",
        ],
        "personajes.html": [
            "Tomás de Goicolea",
            "Recreación IA",
        ],
        "index.html": [
            "Cinco montes",
            "Cinco bocinas",
        ],
    }

    for filename, snippets in checks.items():
        path = ROOT / filename
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for snippet in snippets:
            if snippet not in text:
                issues.append(Issue("WARN", filename, f"No se encontró texto/asset esperado: {snippet!r}"))


def write_report(issues: list[Issue]) -> Path:
    errors = [issue for issue in issues if issue.severity == "ERROR"]
    warns = [issue for issue in issues if issue.severity == "WARN"]

    lines: list[str] = []
    lines.append("# QA V3.9 — navegación, enlaces y coherencia documental")
    lines.append("")
    lines.append(f"- Estado: {'FAIL' if errors else 'PASS'}")
    lines.append(f"- Errores: {len(errors)}")
    lines.append(f"- Avisos: {len(warns)}")
    lines.append("")

    if issues:
        lines.append("## Detalle")
        lines.append("")
        for issue in issues:
            lines.append(f"- **{issue.severity}** `{issue.file}` — {issue.detail}")
    else:
        lines.append("Sin incidencias detectadas.")

    report = ROOT / "QA_V3_9_NAVEGACION_ENLACES_REPORT.md"
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report


def main() -> int:
    issues: list[Issue] = []
    check_key_files(issues)
    check_links(issues)
    check_css_urls(issues)
    check_header(issues)
    check_known_typos(issues)
    check_expected_content(issues)

    report = write_report(issues)
    errors = [issue for issue in issues if issue.severity == "ERROR"]
    warns = [issue for issue in issues if issue.severity == "WARN"]

    print("Montes Bocineros — V3.9 QA navegación y enlaces")
    print("=" * 72)
    print(f"Repo: {ROOT}")
    print(f"Reporte: {report}")
    print(f"Errores: {len(errors)}")
    print(f"Avisos: {len(warns)}")

    if errors:
        print("\nERRORES:")
        for issue in errors[:40]:
            print(f"- {issue.file}: {issue.detail}")
        if len(errors) > 40:
            print(f"... y {len(errors) - 40} más. Ver reporte completo.")
        return 1

    if warns:
        print("\nAVISOS:")
        for issue in warns[:20]:
            print(f"- {issue.file}: {issue.detail}")
        if len(warns) > 20:
            print(f"... y {len(warns) - 20} más. Ver reporte completo.")

    print("\nPASS — sin errores bloqueantes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
