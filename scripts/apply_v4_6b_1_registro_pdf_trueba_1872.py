#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V4.6B.1 - Registrar PDF facsimil Trueba 1872.

Esta fase no cambia la tesis. Registra en las paginas implicadas que el PDF/facsimil
ya esta localizado y que la referencia interna exacta es:
- archivo PDF: 991004848149703351.pdf
- portada interior: pagina 2 del PDF
- fragmento clave: pagina 7 del PDF / pagina impresa 13

Ejecutar desde la raiz del repo:
    py -3 scripts/apply_v4_6b_1_registro_pdf_trueba_1872.py
"""
from pathlib import Path
import re

ROOT = Path.cwd()
START = "<!-- V4_6B_1_TRUEBA_1872_PDF_START -->"
END = "<!-- V4_6B_1_TRUEBA_1872_PDF_END -->"
STYLE_ID = "v46b1-trueba-pdf-style"

STYLE = f"""
<style id=\"{STYLE_ID}\">
.v46b1-pdf-box {{
  margin: clamp(1.25rem, 3vw, 2.25rem) 0;
  padding: clamp(1rem, 2.5vw, 1.35rem);
  border: 1px solid rgba(38, 92, 84, .30);
  border-radius: 18px;
  background: linear-gradient(135deg, rgba(240,250,247,.98), rgba(250,244,233,.88));
  box-shadow: 0 12px 30px rgba(28,45,38,.08);
}}
.v46b1-pdf-box h2,.v46b1-pdf-box h3 {{ margin-top: 0; }}
.v46b1-kicker {{
  display:inline-flex;
  margin-bottom:.55rem;
  font-size:.78rem;
  font-weight:800;
  letter-spacing:.055em;
  text-transform:uppercase;
  color:#1f6b55;
}}
.v46b1-status {{
  display:inline-flex;
  align-items:center;
  padding:.25rem .58rem;
  border-radius:999px;
  font-size:.74rem;
  font-weight:800;
  letter-spacing:.035em;
  text-transform:uppercase;
  background:rgba(37,122,88,.13);
  color:#176247;
  border:1px solid rgba(37,122,88,.25);
}}
.v46b1-grid {{
  display:grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap:.75rem;
  margin-top:1rem;
}}
.v46b1-card {{
  padding:.85rem .95rem;
  border-radius:14px;
  background:rgba(255,255,255,.76);
  border:1px solid rgba(38,92,84,.16);
}}
.v46b1-card strong {{ display:block; margin-bottom:.25rem; color:#173f34; }}
.v46b1-card span,.v46b1-pdf-box p {{ color:#4b5a53; }}
.v46b1-quote {{
  margin:1rem 0;
  padding:.85rem 1rem;
  border-left:4px solid #1f6b55;
  background:rgba(255,255,255,.72);
  border-radius:12px;
  color:#31453e;
  font-style:italic;
}}
.v46b1-caution {{
  margin-top:1rem;
  padding:.8rem .95rem;
  border-left:4px solid #9b6b27;
  background:rgba(255,255,255,.72);
  border-radius:12px;
}}
.v46b1-links {{
  display:flex;
  flex-wrap:wrap;
  gap:.55rem;
  margin-top:1rem;
}}
.v46b1-links a {{
  display:inline-flex;
  align-items:center;
  padding:.4rem .72rem;
  border-radius:999px;
  border:1px solid rgba(38,92,84,.25);
  text-decoration:none;
  font-weight:700;
  color:#173f34;
  background:rgba(255,255,255,.55);
}}
</style>
""".strip()

BLOCK = f"""{START}
<section class=\"v46b1-pdf-box\" aria-labelledby=\"v46b1-title\">
  <span class=\"v46b1-kicker\">V4.6B.1 · registro del PDF facsimil</span>
  <h2 id=\"v46b1-title\">Trueba 1872: facsimil primario registrado</h2>
  <p><span class=\"v46b1-status\">PDF localizado y paginado</span></p>
  <p>El facsimil primario de <strong>Antonio de Trueba, <em>Resumen descriptivo e historico del M.N. y M.L. Señorío de Vizcaya</em></strong>, Bilbao, Juan E. Delmas, 1872, queda registrado como evidencia interna de la fase V4.6B.</p>
  <blockquote class=\"v46b1-quote\">“tañeron las bocinas de guerra en los cinco montes mas altos de Vizcaya, que se cree fuesen Gorbea, Oiz, Sollube, Ganecogorta y Colisa”</blockquote>
  <div class=\"v46b1-grid\">
    <div class=\"v46b1-card\"><strong>Archivo</strong><span><code>991004848149703351.pdf</code></span></div>
    <div class=\"v46b1-card\"><strong>Portada interior</strong><span>Pagina 2 del PDF: titulo, autor, Bilbao y año 1872.</span></div>
    <div class=\"v46b1-card\"><strong>Fragmento clave</strong><span>Pagina 7 del PDF / pagina impresa 13.</span></div>
    <div class=\"v46b1-card\"><strong>Estado</strong><span>Trueba 1872 queda como primer punto firme localizado para la lista nominal completa.</span></div>
  </div>
  <p class=\"v46b1-caution\"><strong>Matiz:</strong> la formula “se cree fuesen” confirma una identificacion documentada en 1872, pero mantiene la cautela sobre su antiguedad.</p>
  <div class=\"v46b1-links\">
    <a href=\"FUENTE_V4_6B_1_TRUEBA_1872_PDF_REGISTRO.md\">Ficha PDF</a>
    <a href=\"TABLA_V4_6B_1_PAGINACION_TRUEBA_1872.md\">Paginacion</a>
    <a href=\"INFORME_V4_6B_1_REGISTRO_PDF_TRUEBA_1872.md\">Informe V4.6B.1</a>
  </div>
</section>
{END}"""

PAGES = [
    'index.html',
    'historia.html',
    'fuentes.html',
    'cronologia.html',
    'veredicto.html',
    'pendientes-documentales.html',
    'metodologia.html',
    'archivo.html',
    'llorente-madoz-trueba.html',
    'biblioteca.html',
    'cadena-trueba.html',
    'trueba-facsimil.html',
]

INSERT_MARKERS = [
    '<!-- V4_6B_TRUEBA_1872_END -->',
    '<!-- V4_6A_CONTROL_FACSIMIL_END -->',
    '<!-- V4_5_COTEJO_LEXICOGRAFICO_END -->',
    '<!-- V4_2B_DOCUMENTAL_MERINDADES_END -->',
    '<!-- V4_4_LEXICO_VASCO_END -->',
]

def update_page(rel: str) -> bool:
    path = ROOT / rel
    if not path.exists():
        print(f'SKIP no existe: {rel}')
        return False
    text = path.read_text(encoding='utf-8', errors='replace')
    text = re.sub(re.escape(START) + r'[\s\S]*?' + re.escape(END), '', text).strip() + '\n'
    if STYLE_ID not in text:
        if '</head>' in text:
            text = text.replace('</head>', STYLE + '\n</head>', 1)
        else:
            text = STYLE + '\n' + text
    inserted = False
    for marker in INSERT_MARKERS:
        idx = text.find(marker)
        if idx != -1:
            pos = idx + len(marker)
            text = text[:pos] + '\n' + BLOCK + '\n' + text[pos:]
            inserted = True
            break
    if not inserted:
        for marker in ['</main>', '</body>']:
            idx = text.find(marker)
            if idx != -1:
                text = text[:idx] + BLOCK + '\n' + text[idx:]
                inserted = True
                break
    if not inserted:
        text += '\n' + BLOCK + '\n'
    path.write_text(text, encoding='utf-8')
    print(f'OK actualizado V4.6B.1: {rel}')
    return True

def main():
    changed = []
    for rel in PAGES:
        if update_page(rel):
            changed.append(rel)
    core = {'fuentes.html','cronologia.html','veredicto.html','pendientes-documentales.html','metodologia.html','archivo.html'}
    missing_core = [p for p in core if p not in changed]
    if missing_core:
        raise SystemExit('ERROR: faltan paginas nucleares: ' + ', '.join(missing_core))
    print('\nPaginas actualizadas:')
    for rel in changed:
        print('-', rel)

if __name__ == '__main__':
    main()
