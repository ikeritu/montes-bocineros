from pathlib import Path

p = Path("montes.html")
txt = p.read_text(encoding="utf-8", errors="replace")

txt = txt.replace(
    "No reproduce la velocidad real del sonido",
    "no reproduce la velocidad real del sonido"
)

# Por si el texto no estuviera ya en el caption visible, añadirlo a la cautela metodológica.
if "no reproduce la velocidad real del sonido" not in txt:
    txt = txt.replace(
        "esto no reconstruye cómo sonaron las bocinas ni demuestra cobertura acústica histórica.",
        "esto no reconstruye cómo sonaron las bocinas, no reproduce la velocidad real del sonido ni demuestra cobertura acústica histórica."
    )

p.write_text(txt, encoding="utf-8")
print("OK texto de cautela normalizado en montes.html")
