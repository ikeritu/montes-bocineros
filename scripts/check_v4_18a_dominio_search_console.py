#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
from urllib.parse import urlparse
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
NEW = "https://montesbocineros.eus"
OLD = "https://ikeritu.github.io/montes-bocineros"
DATE = "2026-07-06"
errors = []

def read(rel: str) -> str:
    p = ROOT / rel
    if not p.exists():
        errors.append(f"Falta {rel}")
        return ""
    return p.read_text(encoding="utf-8", errors="ignore")

# CNAME
if read("CNAME").strip() != "montesbocineros.eus":
    errors.append("CNAME no contiene exactamente montesbocineros.eus")

robots = read("robots.txt")
if "Sitemap: https://montesbocineros.eus/sitemap.xml" not in robots:
    errors.append("robots.txt no apunta al sitemap del dominio propio")

sitemap = read("sitemap.xml")
locs = re.findall(r"<loc>\s*(.*?)\s*</loc>", sitemap, re.I)
if not locs:
    errors.append("sitemap.xml no contiene URLs")
for loc in locs:
    if not loc.startswith(NEW + "/"):
        errors.append(f"sitemap.xml contiene URL no canónica: {loc}")
    if "github.io" in loc:
        errors.append(f"sitemap.xml conserva github.io: {loc}")
if f"<lastmod>{DATE}</lastmod>" not in sitemap:
    errors.append("sitemap.xml no contiene lastmod V4.18A")

# Public HTML should not advertise old GitHub Pages URL in canonical/OG/schema.
for path in sorted(ROOT.glob("*.html")):
    text = path.read_text(encoding="utf-8", errors="ignore")
    if OLD in text:
        errors.append(f"{path.name} conserva URL antigua {OLD}")
    canon = re.search(r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']|href=["\']([^"\']+)["\'][^>]*rel=["\']canonical["\']', text, re.I)
    if canon:
        href = canon.group(1) or canon.group(2)
        if not href.startswith(NEW + "/"):
            errors.append(f"{path.name}: canonical no usa dominio propio: {href}")
    if "property=\"og:url\"" in text or "property='og:url'" in text:
        if NEW not in text:
            errors.append(f"{path.name}: posible og:url sin dominio propio")
    # Freshness after migration.
    if "last-modified" in text and DATE not in text:
        errors.append(f"{path.name}: last-modified no actualizado a {DATE}")

llms = read("llms.txt")
for needle in [
    "https://montesbocineros.eus/guia-lector.html",
    "https://montesbocineros.eus/veredicto.html",
    "## Estado V4.18A",
    "Última actualización editorial: 2026-07-06 · V4.18A dominio propio y Search Console",
]:
    if needle not in llms:
        errors.append(f"llms.txt no contiene {needle!r}")
if OLD in llms:
    errors.append("llms.txt conserva URLs antiguas de github.io")

required = {
    "README.md": ["V4.18A", "https://montesbocineros.eus/"],
    "VERSION.txt": ["V4.18A"],
    "CHANGELOG.txt": ["V4.18A", "montesbocineros.eus"],
    "ESTADO_ACTUAL.md": ["V4.18A", "Search Console"],
    "ROADMAP.md": ["V4.18A", "Dominio propio"],
    "INFORME_V4_18A_DOMINIO_SEARCH_CONSOLE.md": ["Dominio propio", "Search Console"],
    "QA_V4_18A_DOMINIO_SEARCH_CONSOLE.md": ["PASS"],
    "QA_V4_18A_DOMINIO_SEARCH_CONSOLE_REPORT.md": ["PASS"],
    "ROADMAP_V4_18A_DOMINIO_SEARCH_CONSOLE.md": ["V4.18A"],
}
for rel, needles in required.items():
    text = read(rel)
    for n in needles:
        if n not in text:
            errors.append(f"{rel}: falta {n!r}")

if errors:
    print("V4.18A CHECK FAIL")
    for err in errors:
        print("-", err)
    sys.exit(1)
print("V4.18A CHECK PASS — dominio propio y Search Console preparados.")
