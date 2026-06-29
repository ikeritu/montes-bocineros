#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re, shutil
ROOT=Path.cwd()
PACKAGE_ROOT=Path(__file__).resolve().parent.parent
SUPPORT_BLOCK='<section aria-label="Apoyar el proyecto" class="global-support">\n<div class="global-support-copy"><span class="support-kicker">Apoyar el proyecto</span><strong>¿Te ha servido esta investigación?</strong><span>Ayuda a mantener y ampliar este trabajo documental.</span></div>\n<div class="support-buttons"><a class="support-card kofi" href="https://ko-fi.com/ikeritu" rel="noopener noreferrer" target="_blank"><span aria-hidden="true" class="support-icon">☕</span><span><strong>Ko-fi</strong><small>ko-fi.com/ikeritu</small></span></a><a class="support-card paypal" href="https://www.paypal.com/paypalme/ikeritus" rel="noopener noreferrer" target="_blank"><span aria-hidden="true" class="support-icon">💙</span><span><strong>PayPal</strong><small>paypal.me/ikeritus</small></span></a></div>\n</section>'
FOOTER_BLOCK='<footer aria-label="Pie de página" class="v341-footer">\n<div class="v341-footer-wrap">\n<div class="v341-footer-brand">\n<h4>Montes Bocineros de Bizkaia</h4>\n<p>Investigación histórico-divulgativa: tradición viva, fuentes verificables y cautela documental.</p>\n</div>\n<div>\n<h4>Información</h4>\n<nav aria-label="Información del proyecto" class="v341-footer-links">\n<a href="archivo.html">Archivo</a>\n<a href="biblioteca.html">Biblioteca documental</a>\n<a href="personajes.html">Personajes</a>\n<a href="metodo-citacion.html">Método y citación</a>\n<a href="autor.html">Autoría y correcciones</a>\n</nav>\n</div>\n<div>\n<h4>Contacto</h4>\n<nav aria-label="Contacto" class="v341-footer-links">\n<a href="mailto:iker.ituarte.tejedor@gmail.com?subject=Correccion%20Montes%20Bocineros">✉ Enviar corrección</a>\n</nav>\n</div>\n</div>\n</footer>'
REPL={"fuentes.html#tabla":"biblioteca.html#tabla-maestra-fuentes","fuentes.html":"biblioteca.html#tabla-maestra-fuentes","cadena-trueba.html#trueba-facsimil":"biblioteca.html#trueba","cadena-trueba.html#llorente-madoz-trueba":"biblioteca.html#madoz-llorente-trueba","cadena-trueba.html#recepcion":"biblioteca.html#recepcion-trueba","cadena-trueba.html#busqueda-ciega-v23a":"biblioteca.html#cadena-trueba","cadena-trueba.html":"biblioteca.html#cadena-trueba","barrio-banales.html":"biblioteca.html#barrio-banales","citas.html":"biblioteca.html#citas-verificadas","archivo-tecnico.html#busqueda-ciega-v23a":"biblioteca.html#archivo-tecnico","archivo-tecnico.html":"biblioteca.html#archivo-tecnico","informes.html":"biblioteca.html#informes-ia","pendientes-documentales.html":"biblioteca.html#pendientes-documentales","metodologia.html":"metodo-citacion.html#metodologia","citar.html":"metodo-citacion.html#como-citar","afirmaciones.html":"metodo-citacion.html#afirmaciones"}
SUPPORT_RE=re.compile(r'\s*<section\b(?=[^>]*class=["\'][^"\']*\bglobal-support\b[^"\']*["\'])(?=[^>]*aria-label=["\']Apoyar el proyecto["\'])[\s\S]*?</section>\s*',re.I)
FOOTER_RE=re.compile(r'\s*<footer\b(?=[^>]*class=["\'][^"\']*\bv341-footer\b[^"\']*["\'])[\s\S]*?</footer>\s*',re.I)
def read(p): return p.read_text(encoding="utf-8",errors="replace")
def write(p,t): p.write_text(t,encoding="utf-8")
def ensure_css(t):
    if "assets/v411e-footer-support.css" in t: return t
    link='<link rel="stylesheet" href="assets/v411e-footer-support.css?v=4.11e"/>'
    return t.replace("</head>",link+"\n</head>",1) if "</head>" in t else link+"\n"+t
def normalize(t):
    for a,b in REPL.items(): t=t.replace(a,b)
    t=t.replace('defer="True"','defer').replace("defer='True'","defer")
    t=SUPPORT_RE.sub("\n",t)
    if FOOTER_RE.search(t):
        t=FOOTER_RE.sub("\n"+SUPPORT_BLOCK+"\n"+FOOTER_BLOCK+"\n",t,count=1)
        t=FOOTER_RE.sub("\n"+FOOTER_BLOCK+"\n",t)
    else:
        t=t.replace("</body>",SUPPORT_BLOCK+"\n"+FOOTER_BLOCK+"\n</body>",1) if "</body>" in t else t+"\n"+SUPPORT_BLOCK+"\n"+FOOTER_BLOCK+"\n"
    t=ensure_css(t)
    return re.sub(r'\n{4,}',"\n\n",t)
def main():
    src=PACKAGE_ROOT/"assets"/"v411e-footer-support.css"; dst=ROOT/"assets"/"v411e-footer-support.css"
    dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dst)
    changed=[]
    for p in ROOT.glob("*.html"):
        old=read(p); new=normalize(old)
        if old!=new: write(p,new); changed.append(p.name)
    print("OK V4.11E aplicada")
    print("- Footer canónico sin columna Apoyar duplicada.")
    print("- Bloque Apoyar el proyecto único por página.")
    print("- HTML modificados:",", ".join(changed) if changed else "ninguno")
    return 0
if __name__=="__main__": raise SystemExit(main())
