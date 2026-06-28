#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re
import shutil

ROOT = Path.cwd()
HERE = Path(__file__).resolve().parent
PACKAGE_ROOT = HERE.parent

DELETED_PAGES = [
    "fuentes.html",
    "cadena-trueba.html",
    "barrio-banales.html",
    "citas.html",
    "archivo-tecnico.html",
    "informes.html",
    "pendientes-documentales.html",
]

LINK_REPLACEMENTS = {
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

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")

def replace_links_in_html() -> int:
    changed = 0
    for path in ROOT.glob("*.html"):
        if path.name in DELETED_PAGES:
            continue
        txt = read(path)
        before = txt
        for old, new in LINK_REPLACEMENTS.items():
            txt = txt.replace(old, new)
        txt = txt.replace('defer="True"', 'defer').replace("defer='True'", "defer")
        if txt != before:
            write(path, txt)
            changed += 1
    return changed

def remove_ondas_from_montes() -> bool:
    path = ROOT / "montes.html"
    if not path.exists():
        return False
    txt = read(path)
    before = txt

    txt = re.sub(r'\s*<link\b[^>]*href=["\']assets/ondas-gernika\.css[^"\']*["\'][^>]*>\s*', "\n", txt, flags=re.I)
    txt = re.sub(r'\s*<script\b[^>]*src=["\']assets/ondas-gernika\.js[^"\']*["\'][^>]*>\s*</script>\s*', "\n", txt, flags=re.I)

    txt = re.sub(
        r'\s*<!--\s*V4\.10\s*·\s*Ondas desde Gernika[\s\S]*?<div class=["\']ondas-gernika-panel["\'][\s\S]*?</div>\s*',
        "\n",
        txt,
        flags=re.I,
        count=1,
    )
    txt = re.sub(
        r'\s*<div class=["\']ondas-gernika-panel["\'][\s\S]*?</div>\s*',
        "\n",
        txt,
        flags=re.I,
        count=1,
    )

    for old, new in LINK_REPLACEMENTS.items():
        txt = txt.replace(old, new)
    txt = txt.replace('defer="True"', 'defer').replace("defer='True'", "defer")

    if txt != before:
        write(path, txt)
        return True
    return False

def patch_mapbox_js() -> bool:
    path = ROOT / "assets" / "mapbox-montes.js"
    if not path.exists():
        return False
    txt = read(path)
    before = txt

    helper = """
  function hideMapboxPoiLayers(map){
    try{
      const patterns=['poi','tourism','zoo','animal','natural-point'];
      const layers=(map.getStyle()&&map.getStyle().layers)||[];
      layers.forEach(layer=>{
        const id=String(layer.id||'').toLowerCase();
        if(layer.type==='symbol' && patterns.some(token=>id.includes(token))){
          map.setLayoutProperty(layer.id,'visibility','none');
        }
      });
    }catch(err){
      console.warn('[Montes Bocineros] No se han podido ocultar POI del mapa base:', err);
    }
  }
"""

    if "function hideMapboxPoiLayers" not in txt:
        txt = txt.replace("  function showFallback(message){", helper + "\n  function showFallback(message){", 1)

    if "hideMapboxPoiLayers(map);" not in txt:
        txt = txt.replace("map.on('load',()=>{ setStatus('',false);", "map.on('load',()=>{ setStatus('',false); hideMapboxPoiLayers(map);", 1)

    txt = re.sub(
        r"\s*if\(p\.id!==['\"]gernika['\"]\)\{\s*el\.title=['\"][\s\S]*?window\.dispatchEvent\(new CustomEvent\(['\"]aviso-sonoro:monte['\"][\s\S]*?\}\s*",
        "\n",
        txt,
        flags=re.I,
    )
    txt = re.sub(
        r"if\(id&&id!==['\"]gernika['\"]\)\s*window\.dispatchEvent\(new CustomEvent\(['\"]aviso-sonoro:monte['\"][^;]*;\s*",
        "if(id&&id!=='gernika') window.location.hash = id;\n",
        txt,
        flags=re.I,
    )
    txt = txt.replace("aviso-sonoro:monte", "montes-map:select")

    if txt != before:
        write(path, txt)
        return True
    return False

def delete_old_pages() -> list[str]:
    deleted = []
    for name in DELETED_PAGES:
        path = ROOT / name
        if path.exists():
            path.unlink()
            deleted.append(name)
    return deleted

def main() -> int:
    src_bib = PACKAGE_ROOT / "biblioteca.html"
    if not src_bib.exists():
        raise SystemExit("ERROR: el paquete no contiene biblioteca.html")

    shutil.copy2(src_bib, ROOT / "biblioteca.html")

    link_changed = replace_links_in_html()
    montes_changed = remove_ondas_from_montes()
    mapbox_changed = patch_mapbox_js()
    deleted = delete_old_pages()

    print("OK V4.11A.1 aplicada")
    print("- fuentes.html queda absorbida en biblioteca.html#tabla-maestra-fuentes")
    print("- biblioteca.html queda como Biblioteca documental unificada.")
    print("- enlaces internos a páginas absorbidas actualizados.")
    print("- páginas absorbidas eliminadas:", ", ".join(deleted) if deleted else "ninguna; ya estaban eliminadas")
    print("- montes.html limpiado:", "sí" if montes_changed else "sin cambios")
    print("- mapbox-montes.js parcheado para ocultar POI/animales del mapa base:", "sí" if mapbox_changed else "sin cambios o no encontrado")
    print("- HTML con enlaces normalizados:", link_changed)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
