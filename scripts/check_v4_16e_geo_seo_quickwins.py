#!/usr/bin/env python3
from pathlib import Path
import re, sys, json
ROOT = Path(__file__).resolve().parents[1]
DATE_MIN = "2026-07-05"
errors = []

def text(name):
    return (ROOT/name).read_text(encoding="utf-8", errors="ignore")

# YAML glob safety
cfg = text("_config.yml")
for bad in ["- *.md", "- *.txt", "- QA_*.md", "- ROADMAP_*.md", "- INFORME_*.md"]:
    if bad in cfg:
        errors.append(f"_config.yml contiene comodín sin comillas: {bad}")

if 'data-generated="v416e-faqpage"' not in text("guia-lector.html") or '"@type": "FAQPage"' not in text("guia-lector.html"):
    errors.append("Falta FAQPage JSON-LD en guia-lector.html")
if 'data-generated="v416e-dataset-fuentes"' not in text("biblioteca.html") or '"@type": "Dataset"' not in text("biblioteca.html"):
    errors.append("Falta Dataset JSON-LD en biblioteca.html")
if "Última actualización editorial:" not in text("llms.txt"):
    errors.append("llms.txt no incluye fecha de actualización editorial")
for page in ["veredicto.html", "historia.html", "montes.html"]:
    s = text(page)
    if "geo-tldr" not in s:
        errors.append(f"Falta TL;DR geo-tldr en {page}")
    if "v416e-geo-seo-quickwins.css" not in s:
        errors.append(f"Falta CSS V4.16E en {page}")
sm = text("sitemap.xml")
if not re.search(r"<lastmod>\d{4}-\d{2}-\d{2}</lastmod>", sm):
    errors.append("sitemap.xml no contiene lastmod ISO válido")
for stub in ["faq.html", "glosario.html", "fuentes.html", "citas.html", "citar.html", "metodologia.html", "afirmaciones.html", "fuentes-sospechosas.html", "mapa.html", "informe-nemotron.html"]:
    if f"/{stub}</loc>" in sm:
        errors.append(f"Página-puente/noindex en sitemap: {stub}")
for html in ROOT.glob("*.html"):
    s = html.read_text(encoding="utf-8", errors="ignore")
    if "http-equiv=\"refresh\"" in s or "http-equiv='refresh'" in s or "http-equiv=refresh" in s:
        if "noindex,follow" not in s:
            errors.append(f"Página-puente sin noindex: {html.name}")
if errors:
    print("V4.16E CHECK: FAIL")
    for e in errors:
        print("-", e)
    sys.exit(1)
print("V4.16E CHECK: PASS")
print("FAQPage, Dataset, llms.txt, TL;DR, sitemap y YAML OK")
