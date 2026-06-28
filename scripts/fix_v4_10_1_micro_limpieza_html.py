from pathlib import Path
import re

# 1. Normalizar defer="True" en todos los HTML.
for p in Path(".").glob("*.html"):
    txt = p.read_text(encoding="utf-8", errors="replace")
    before = txt

    txt = txt.replace('defer="True"', 'defer')
    txt = txt.replace("defer='True'", "defer")

    if txt != before:
        p.write_text(txt, encoding="utf-8")
        print(f"OK defer normalizado: {p}")

# 2. Compactar líneas en blanco excesivas en index.html.
index = Path("index.html")
if index.exists():
    txt = index.read_text(encoding="utf-8", errors="replace")
    before = txt

    # Caso concreto: cierre de hero antes de sección ruta.
    txt = re.sub(
        r'(</div>\s*</section>)\s{3,}(<section class="v34-section" id="ruta")',
        r'\1\n\n\2',
        txt,
        flags=re.I
    )

    # Limpieza general suave: máximo dos saltos de línea consecutivos en zonas HTML.
    txt = re.sub(r'\n{4,}', '\n\n\n', txt)

    if txt != before:
        index.write_text(txt, encoding="utf-8")
        print("OK espacios compactados en index.html")
    else:
        print("INFO index.html no requería compactación")
