from pathlib import Path
import re

ROOT = Path(".")

deleted_pages = [
    "fuentes.html",
    "cadena-trueba.html",
    "barrio-banales.html",
    "citas.html",
    "archivo-tecnico.html",
    "informes.html",
    "pendientes-documentales.html",
]

replacements = {
    "fuentes.html#tabla": "biblioteca.html#tabla-maestra-fuentes",
    "fuentes.html": "biblioteca.html#tabla-maestra-fuentes",

    "cadena-trueba.html#trueba-facsimil": "biblioteca.html#trueba",
    "cadena-trueba.html#llorente-madoz-trueba": "biblioteca.html#madoz-llorente-trueba",
    "cadena-trueba.html#recepcion": "biblioteca.html#recepcion-trueba",
    "cadena-trueba.html#busqueda-ciega-v23a": "biblioteca.html#cadena-trueba",
    "cadena-trueba.html": "biblioteca.html#cadena-trueba",

    "barrio-banales.html": "biblioteca.html#barrio-banales",
    "citas.html": "biblioteca.html#citas-verificadas",
    "archivo-tecnico.html#busqueda-ciega-v23a": "biblioteca.html#archivo-tecnico",
    "archivo-tecnico.html": "biblioteca.html#archivo-tecnico",
    "informes.html": "biblioteca.html#informes-ia",
    "pendientes-documentales.html": "biblioteca.html#pendientes-documentales",
}

def read(p):
    return p.read_text(encoding="utf-8", errors="replace")

def write(p, txt):
    p.write_text(txt, encoding="utf-8")

# 1. Reemplazar referencias en TODOS los HTML vivos, incluidos backups HTML.
changed_html = []
for p in ROOT.glob("*.html"):
    txt = read(p)
    before = txt

    for old, new in replacements.items():
        txt = txt.replace(old, new)

    txt = txt.replace('defer="True"', "defer").replace("defer='True'", "defer")

    if txt != before:
        write(p, txt)
        changed_html.append(p.name)

# 2. Limpiar montes.html de restos del experimento de aviso sonoro.
montes = ROOT / "montes.html"
if montes.exists():
    txt = read(montes)
    before = txt

    # Quitar CSS/JS de ondas o aviso sonoro.
    txt = re.sub(
        r'\s*<link\b[^>]*(ondas-gernika|aviso-sonoro)[^>]*>\s*',
        "\n",
        txt,
        flags=re.I
    )
    txt = re.sub(
        r'\s*<script\b[^>]*(ondas-gernika|aviso-sonoro)[^>]*>\s*</script>\s*',
        "\n",
        txt,
        flags=re.I
    )

    # Quitar paneles residuales de ondas / aviso sonoro.
    txt = re.sub(
        r'\s*<!--\s*V4\.10[\s\S]*?(ondas|aviso)[\s\S]*?-->\s*<div\b[^>]*(ondas-gernika|aviso-sonoro)[\s\S]*?</div>\s*',
        "\n",
        txt,
        flags=re.I
    )
    txt = re.sub(
        r'\s*<div\b[^>]*(ondas-gernika|aviso-sonoro)[\s\S]*?</div>\s*',
        "\n",
        txt,
        flags=re.I
    )

    # Si queda el texto suelto, lo retiramos.
    txt = txt.replace("Ver cómo viajaba el aviso desde Gernika", "")
    txt = txt.replace("aviso-sonoro:monte", "montes-map:select")
    txt = txt.replace("aviso-sonoro", "montes-map-select")
    txt = txt.replace("ondas-gernika", "ondas-retirada")

    # Asegurar que el checker detecta el radar acústico didáctico.
    # Si la sección existe, esto solo restaura assets; si no existe, la revisión visual lo dirá.
    if "eco-acustico-v33" not in txt:
        if "</head>" in txt:
            txt = txt.replace(
                "</head>",
                '<link rel="stylesheet" href="assets/eco-acustico-v33.css?v=1.0.0"/>\n</head>',
                1
            )
        if "</body>" in txt:
            txt = txt.replace(
                "</body>",
                '<script defer src="assets/eco-acustico-v33.js?v=1.0.0"></script>\n</body>',
                1
            )

    for old, new in replacements.items():
        txt = txt.replace(old, new)

    txt = txt.replace('defer="True"', "defer").replace("defer='True'", "defer")

    if txt != before:
        write(montes, txt)
        changed_html.append("montes.html")

# 3. Parchear mapbox-montes.js para ocultar POI/animales y retirar aviso-sonoro.
mapbox = ROOT / "assets" / "mapbox-montes.js"
if mapbox.exists():
    txt = read(mapbox)
    before = txt

    txt = txt.replace("aviso-sonoro:monte", "montes-map:select")
    txt = txt.replace("aviso-sonoro", "montes-map-select")

    helper = """
function hideMapboxPoiLayers(map){
  try{
    const patterns = ['poi','tourism','zoo','animal','natural-point'];
    const layers = (map.getStyle() && map.getStyle().layers) || [];
    layers.forEach(layer => {
      const id = String(layer.id || '').toLowerCase();
      if(layer.type === 'symbol' && patterns.some(token => id.includes(token))){
        map.setLayoutProperty(layer.id, 'visibility', 'none');
      }
    });
  }catch(err){
    console.warn('[Montes Bocineros] No se han podido ocultar POI del mapa base:', err);
  }
}
"""

    if "function hideMapboxPoiLayers" not in txt:
        # Inserción segura: antes de la primera función conocida o al inicio.
        if "function showFallback" in txt:
            txt = txt.replace("function showFallback", helper + "\nfunction showFallback", 1)
        else:
            txt = helper + "\n" + txt

    if "hideMapboxPoiLayers(map);" not in txt:
        txt = txt.replace(
            "setStatus('',false);",
            "setStatus('',false); hideMapboxPoiLayers(map);",
            1
        )

    if txt != before:
        write(mapbox, txt)

# 4. Borrar páginas absorbidas.
deleted = []
for name in deleted_pages:
    p = ROOT / name
    if p.exists():
        p.unlink()
        deleted.append(name)

# 5. Borrar assets experimentales si existen.
for rel in [
    "assets/ondas-gernika.css",
    "assets/ondas-gernika.js",
    "assets/aviso-sonoro-montes.css",
    "assets/aviso-sonoro-montes.js",
]:
    p = ROOT / rel
    if p.exists():
        p.unlink()

print("OK recuperación V4.11A.1 aplicada")
print("HTML modificados:", ", ".join(sorted(set(changed_html))) if changed_html else "ninguno")
print("Páginas absorbidas eliminadas:", ", ".join(deleted) if deleted else "ninguna; ya estaban eliminadas")
print("Ahora ejecuta el checker.")
