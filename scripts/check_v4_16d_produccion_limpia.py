from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

required = [
    "_config.yml",
    "scripts/apply_v4_16d_produccion_limpia.py",
    "scripts/check_v4_16d_produccion_limpia.py",
    "INFORME_V4_16D_PRODUCCION_LIMPIA_AUDITORIA.md",
    "QA_V4_16D_PRODUCCION_LIMPIA_AUDITORIA.md",
    "QA_V4_16D_PRODUCCION_LIMPIA_AUDITORIA_REPORT.md",
    "ROADMAP_V4_16D_PRODUCCION_LIMPIA_AUDITORIA.md",
]
for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f"Falta archivo requerido: {rel}")

backups = [p.name for p in ROOT.glob("*BACKUP*.html") if p.is_file()]
if backups:
    errors.append("Backups HTML públicos encontrados: " + ", ".join(backups))

config = (ROOT / "_config.yml").read_text(encoding="utf-8", errors="ignore") if (ROOT / "_config.yml").exists() else ""
for must in ["scripts/", "*.zip", "*BACKUP*.html", "README.md", "CHANGELOG.txt", "ESTADO_ACTUAL.md", "ROADMAP.md"]:
    if must not in config:
        errors.append(f"_config.yml no excluye: {must}")
for public in ["llms.txt", "robots.txt"]:
    if re.search(rf"^\s*-\s*{re.escape(public)}\s*$", config, re.M):
        errors.append(f"_config.yml excluye indebidamente archivo público: {public}")

link_re = re.compile(r'href="([^"]+\.(?:md|txt))"', re.I)
for html in ROOT.glob("*.html"):
    text = html.read_text(encoding="utf-8", errors="ignore")
    for href in link_re.findall(text):
        if href not in {"llms.txt", "robots.txt"} and not href.startswith(("http://", "https://", "mailto:")):
            errors.append(f"{html.name}: enlace público a nota interna {href}")

for rel in ["robots.txt", "llms.txt", "sitemap.xml", "index.html"]:
    if not (ROOT / rel).exists():
        errors.append(f"Falta archivo público esencial: {rel}")

sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8", errors="ignore") if (ROOT / "sitemap.xml").exists() else ""
if "BACKUP" in sitemap or ".md" in sitemap or ".txt" in sitemap or "scripts/" in sitemap:
    errors.append("sitemap.xml contiene rutas internas, backups o notas")

checks = [
    ("biblioteca.html", "Iturriza 1790 queda cerrado"),
    ("biblioteca.html", "Delmas 1864 se cierra"),
    ("estado-investigacion.html", "Iturriza 1790 queda como fuente anterior"),
    ("veredicto.html", "Trueba 1872"),
]
for rel, needle in checks:
    text = (ROOT / rel).read_text(encoding="utf-8", errors="ignore") if (ROOT / rel).exists() else ""
    if needle not in text:
        errors.append(f"No se encuentra marcador documental en {rel}: {needle}")

excluded_docs = [line.strip()[2:] for line in config.splitlines() if line.strip().startswith("- ") and line.strip()[2:].endswith((".md", ".txt"))]
if len(excluded_docs) < 50:
    errors.append("_config.yml no refleja una exclusión amplia de notas internas")

if errors:
    print("V4.16D CHECK FAIL")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("V4.16D CHECK PASS — producción limpia: notas internas excluidas de Pages, sin backups ni enlaces públicos a .md/.txt internos")
