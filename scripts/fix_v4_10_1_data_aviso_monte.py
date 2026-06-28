from pathlib import Path
import re

p = Path("montes.html")
txt = p.read_text(encoding="utf-8", errors="replace")

# 1. Eliminar atributos sueltos data-aviso-monte="..."
txt = re.sub(r'\s*data-aviso-monte=["\'][^"\']*["\']', '', txt, flags=re.I)

# 2. Eliminar cualquier botón residual que fuera solo del aviso sonoro
txt = re.sub(
    r'\s*<button\b[^>]*data-aviso-monte[^>]*>[\s\S]*?</button>\s*',
    '\n',
    txt,
    flags=re.I
)

# 3. Eliminar referencias residuales a la función/JS si quedaron en onclick o similares
txt = re.sub(r'\s*onclick=["\'][^"\']*aviso[^"\']*["\']', '', txt, flags=re.I)

p.write_text(txt, encoding="utf-8")
print("OK restos data-aviso-monte eliminados de montes.html")
