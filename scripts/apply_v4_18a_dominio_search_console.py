#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""V4.18A — Dominio propio y Search Console.

Script idempotente de control: asegura CNAME, dominio canónico y sitemap/robots
sobre montesbocineros.eus. No cambia la tesis documental.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
OLD = "https://ikeritu.github.io/montes-bocineros"
NEW = "https://montesbocineros.eus"
DATE = "2026-07-06"

TEXT_EXT = {".html", ".xml", ".txt", ".md", ".toml", ".yml"}

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in TEXT_EXT:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    new_text = text.replace(OLD, NEW)
    if path.suffix.lower() == ".html":
        new_text = re.sub(r'(name="last-modified" content=")\d{4}-\d{2}-\d{2}("/?>)', rf'\g<1>{DATE}\2', new_text)
        new_text = re.sub(r'(content=")\d{4}-\d{2}-\d{2}(" name="last-modified"/?>)', rf'\g<1>{DATE}\2', new_text)
        new_text = re.sub(r'("dateModified"\s*:\s*")\d{4}-\d{2}-\d{2}(")', rf'\g<1>{DATE}\2', new_text)
    if path.name == "sitemap.xml":
        new_text = re.sub(r"<lastmod>\d{4}-\d{2}-\d{2}</lastmod>", f"<lastmod>{DATE}</lastmod>", new_text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")

(ROOT / "CNAME").write_text("montesbocineros.eus\n", encoding="utf-8")
(ROOT / "robots.txt").write_text(
    "User-agent: *\nAllow: /\n\nSitemap: https://montesbocineros.eus/sitemap.xml\n",
    encoding="utf-8",
)
print("V4.18A aplicado: dominio canónico montesbocineros.eus preparado.")
