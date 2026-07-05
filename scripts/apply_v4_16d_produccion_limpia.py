from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

EXCEPTIONS = {
    "NOTA_DOCUMENTAL_DELMAS_1864.md": "biblioteca.html#delmas-1864-revisado-v416b",
    "FUENTE_V4_6B_TRUEBA_1872.md": "trueba-facsimil.html#trueba-1872-recotejo-v416a",
    "FUENTE_V4_6B_1_TRUEBA_1872_PDF_REGISTRO.md": "trueba-facsimil.html#trueba-1872-recotejo-v416a",
    "TABLA_V4_6B_TRUEBA_1872_FACSIMIL.md": "trueba-facsimil.html#trueba-1872-recotejo-v416a",
    "TABLA_V4_6B_1_PAGINACION_TRUEBA_1872.md": "trueba-facsimil.html#trueba-1872-recotejo-v416a",
    "INFORME_V4_6B_TRUEBA_1872_FACSIMIL.md": "trueba-facsimil.html#trueba-1872-recotejo-v416a",
    "INFORME_V4_6B_1_REGISTRO_PDF_TRUEBA_1872.md": "trueba-facsimil.html#trueba-1872-recotejo-v416a",
    "INFORME_V3_1B_MADOZ_1847_FACSIMIL.md": "llorente-madoz-trueba.html",
    "INFORME_V4_0_LLORENTE_1807_FACSIMIL.md": "llorente-madoz-trueba.html",
}

def generate_config() -> str:
    keep_publish = {"llms.txt", "robots.txt"}
    exclude = ["_proceso/", "scripts/", "*.zip", "*.docx", "*.tmp", "*.part", "*BACKUP*.html"]
    for p in sorted(ROOT.iterdir(), key=lambda x: x.name.lower()):
        if p.is_file() and p.suffix.lower() in {".md", ".txt"} and p.name not in keep_publish:
            exclude.append(p.name)
    lines = [
        "# V4.16D — Limpieza de producción",
        "# GitHub Pages/Jekyll no debe publicar notas internas ni herramientas.",
        "exclude:",
    ]
    lines.extend(f"  - {item}" for item in exclude)
    return "\n".join(lines) + "\n"

def main() -> None:
    deleted = []
    for path in sorted(ROOT.glob("*BACKUP*.html")):
        if path.is_file():
            path.unlink()
            deleted.append(path.name)

    updated = []
    for html in ROOT.glob("*.html"):
        text = html.read_text(encoding="utf-8-sig", errors="ignore")
        original = text
        for old, new in EXCEPTIONS.items():
            text = text.replace(f'href="{old}"', f'href="{new}"')
        text = re.sub(r'href="([A-ZÁÉÍÓÚÑ0-9_\-]+\.(?:md|txt))"', 'href="biblioteca.html#archivo-tecnico"', text)
        if text != original:
            html.write_text(text, encoding="utf-8", newline="\n")
            updated.append(html.name)

    (ROOT / "_config.yml").write_text(generate_config(), encoding="utf-8", newline="\n")
    print(f"V4.16D apply OK — backups_deleted={len(deleted)} html_links_updated={len(updated)} config_regenerated=1")

if __name__ == "__main__":
    main()
