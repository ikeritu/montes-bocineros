#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V4.9 — Estado documental provisional, sin crear páginas nuevas.

Objetivo:
- Centralizar el veredicto documental en veredicto.html.
- No crear páginas HTML nuevas.
- No tocar guia-lector.html.
- No tocar estructura visual general.
- Añadir una sección breve y clara: fuentes verificadas, conclusión y pendientes.

Ejecutar desde la raíz del repo:
    py -3 scripts/apply_v4_9_estado_documental_minimo.py
"""

from pathlib import Path
import re

ROOT = Path.cwd()
TARGET = ROOT / "veredicto.html"

START = "<!-- V4_9_ESTADO_DOCUMENTAL_MINIMO_START -->"
END = "<!-- V4_9_ESTADO_DOCUMENTAL_MINIMO_END -->"
STYLE_ID = "v49-estado-documental-minimo-style"

STYLE = """
<style id="v49-estado-documental-minimo-style">
  .v49-estado-documental {
    margin: clamp(1.5rem, 4vw, 3rem) 0;
    padding: clamp(1rem, 2.5vw, 1.5rem);
    border: 1px solid rgba(31,107,85,.22);
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(246,252,248,.98), rgba(246,241,231,.88));
    box-shadow: 0 16px 34px rgba(28,45,38,.07);
    scroll-margin-top: 7rem;
  }
  .v49-estado-documental .v49-kicker {
    display: inline-flex;
    margin-bottom: .45rem;
    font-size: .76rem;
    font-weight: 800;
    letter-spacing: .055em;
    text-transform: uppercase;
    color: #1f6b55;
  }
  .v49-estado-documental h2,
  .v49-estado-documental h3 {
    margin-top: 0;
  }
  .v49-estado-documental .v49-lead {
    max-width: 76ch;
  }
  .v49-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(235px, 1fr));
    gap: .8rem;
    margin: 1rem 0;
  }
  .v49-card {
    border: 1px solid rgba(31,107,85,.16);
    border-radius: 16px;
    padding: .9rem;
    background: rgba(255,255,255,.82);
  }
  .v49-card strong {
    display:block;
    margin-bottom:.35rem;
    color:#133f35;
  }
  .v49-badge {
    display:inline-flex;
    align-items:center;
    width:max-content;
    margin-bottom:.45rem;
    border-radius:999px;
    padding:.2rem .55rem;
    font-size:.68rem;
    font-weight:800;
    letter-spacing:.04em;
    text-transform:uppercase;
    background:rgba(31,107,85,.12);
    color:#133f35;
  }
  .v49-badge.no { background:rgba(190,125,35,.14); color:#7a4e12; }
  .v49-badge.yes { background:rgba(31,107,85,.17); color:#0c473a; }
  .v49-badge.variant { background:rgba(97,61,124,.13); color:#613d7c; }
  .v49-table-wrap {
    overflow-x:auto;
    margin:1rem 0;
    border-radius:16px;
    border:1px solid rgba(31,107,85,.16);
    background:white;
  }
  .v49-table {
    width:100%;
    min-width:780px;
    border-collapse:collapse;
    font-size:.94rem;
  }
  .v49-table th,
  .v49-table td {
    padding:.75rem .8rem;
    border-bottom:1px solid rgba(31,107,85,.12);
    vertical-align:top;
    text-align:left;
  }
  .v49-table th {
    color:#133f35;
    background:rgba(31,107,85,.08);
  }
  .v49-table tr:last-child td {
    border-bottom:0;
  }
  .v49-callout {
    margin-top:1rem;
    padding:.85rem 1rem;
    border-left:4px solid rgba(31,107,85,.50);
    border-radius:14px;
    background:rgba(255,255,255,.72);
  }
  .v49-pending {
    margin:.5rem 0 0;
    padding-left:1.2rem;
  }
  .v49-pending li {
    margin:.35rem 0;
  }
</style>
""".strip()

BLOCK = f"""
{START}
<section class="v49-estado-documental" id="estado-documental-provisional">
  <span class="v49-kicker">V4.9 · Estado documental provisional</span>
  <h2>De las cinco vozinas a los cinco montes: qué está verificado</h2>
  <p class="v49-lead">Esta sección concentra el veredicto documental sin crear páginas nuevas. La clave es mantener separadas tres capas: las vozinas medievales, la convocatoria foral y la lista nominal moderna de montes.</p>

  <div class="v49-grid" aria-label="Resumen del estado documental">
    <article class="v49-card">
      <span class="v49-badge yes">Verificado</span>
      <strong>Vozinas y convocatoria</strong>
      <p>1342, 1394 y 1452 documentan vozinas, merindades, Junta, vozineros y sayones.</p>
    </article>
    <article class="v49-card">
      <span class="v49-badge no">No verificado</span>
      <strong>Lista medieval de montes</strong>
      <p>No se ha localizado una fuente medieval que enumere Gorbea, Oiz, Sollube, Ganekogorta y Colisa/Kolitza.</p>
    </article>
    <article class="v49-card">
      <span class="v49-badge yes">Ancla documental</span>
      <strong>Trueba 1872</strong>
      <p>Primer punto firme verificado para la lista nominal completa, con la cautela “que se cree fuesen”.</p>
    </article>
    <article class="v49-card">
      <span class="v49-badge variant">Recepción</span>
      <strong>Euskal-Erria 1880</strong>
      <p>Incluye los cinco dentro de una lista ampliada. Sirve para estudiar variantes posteriores, no para adelantar el origen.</p>
    </article>
  </div>

  <div class="v49-table-wrap">
    <table class="v49-table">
      <thead>
        <tr>
          <th>Fuente</th>
          <th>Año</th>
          <th>Qué documenta</th>
          <th>¿Lista completa?</th>
          <th>Impacto</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Capitulado de Juan Núñez de Lara</strong></td>
          <td>1342</td>
          <td>“Cinco vozinas de Vizcaia” vinculadas a las cinco merindades.</td>
          <td>No</td>
          <td>Refuerza la capa antigua de vozinas, no la lista de cumbres.</td>
        </tr>
        <tr>
          <td><strong>Cuaderno de Hermandad de Gonzalo Moro</strong></td>
          <td>1394</td>
          <td>Convocatoria a Junta General de Guernica mediante cinco vozinas.</td>
          <td>No</td>
          <td>Refuerza el contexto institucional de llamada.</td>
        </tr>
        <tr>
          <td><strong>Fuero Viejo de Vizcaya</strong></td>
          <td>1452</td>
          <td>Vozineros, vozinas y sayones: oficios y mecanismos de llamamiento.</td>
          <td>No</td>
          <td>Refuerza el marco foral, no identifica montes concretos.</td>
        </tr>
        <tr>
          <td><strong>Antonio de Trueba, Resumen descriptivo e histórico</strong></td>
          <td>1872</td>
          <td>Enumera Gorbea, Oiz, Sollube, Ganecogorta y Colisa.</td>
          <td>Sí</td>
          <td>Primer punto firme verificado para la lista canónica completa.</td>
        </tr>
        <tr>
          <td><strong>Antonio de Trueba, “Jaun-Zuria”, Euskal-Erria</strong></td>
          <td>1880</td>
          <td>Variante posterior con los cinco dentro de una lista ampliada.</td>
          <td>Incluye los cinco, pero no como lista cerrada.</td>
          <td>No cambia el ancla de 1872; muestra recepción variable.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="v49-callout">
    <h3>Diagnóstico documental provisional</h3>
    <p>La documentación verificada acredita una tradición antigua de vozinas y convocatorias, pero no acredita una lista medieval de cinco montes bocineros concretos. Con el corpus revisado, Trueba 1872 sigue siendo el primer punto firme para la lista nominal completa.</p>
    <p><strong>Riesgo principal:</strong> convertir “cinco vozinas” o “cinco merindades” en “cinco montes”. Esa equivalencia no está demostrada por los documentos medievales verificados.</p>
  </div>

  <div class="v49-callout">
    <h3>Pendientes antes de cerrar la investigación</h3>
    <ul class="v49-pending">
      <li><strong>Trueba 1858, El Mundo Pintoresco:</strong> verificar facsímil, página y posible fórmula de siete vocinas / siete montes.</li>
      <li><strong>Trueba 1859 / 1862:</strong> comprobar si hay cinco vocinas en cinco montes sin lista nominal.</li>
      <li><strong>Madoz:</strong> separar heraldos, alturas, bocinas y Junta de una posible lista de montes.</li>
      <li><strong>Lope García de Salazar, Fuero Viejo, Ibargüen-Cachopín, Iturriza y Goicolea:</strong> incorporar solo con facsímil, página o edición directamente verificable.</li>
    </ul>
  </div>
</section>
{END}
""".strip()

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")

def remove_block(text: str, start: str, end: str) -> str:
    return re.sub(re.escape(start) + r"[\s\S]*?" + re.escape(end) + r"\s*", "", text, flags=re.I)

def remove_style(text: str, style_id: str) -> str:
    return re.sub(r'<style\b[^>]*id=["\']' + re.escape(style_id) + r'["\'][^>]*>[\s\S]*?</style>\s*', "", text, flags=re.I)

def main() -> int:
    if not TARGET.exists():
        raise SystemExit("ERROR: no existe veredicto.html")

    text = read(TARGET)

    if "Síntesis crítica" not in text or "Respuesta breve" not in text or "</head>" not in text:
        raise SystemExit("ERROR: veredicto.html no parece ser la página esperada.")

    text = remove_block(text, START, END)
    text = remove_style(text, STYLE_ID)

    text = text.replace("</head>", STYLE + "\n</head>", 1)

    # Insertar después de la sección respuesta-breve.
    m = re.search(r'<section\b[^>]*id=["\']respuesta-breve["\'][^>]*>[\s\S]*?</section>', text, flags=re.I)
    if not m:
        raise SystemExit("ERROR: no encuentro la sección id='respuesta-breve'.")

    insert_at = m.end()
    text = text[:insert_at] + "\n" + BLOCK + "\n" + text[insert_at:]

    write(TARGET, text)

    print("OK V4.9 aplicada")
    print("- Páginas HTML nuevas creadas: 0")
    print("- Página modificada: veredicto.html")
    print("- No se ha tocado guia-lector.html")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
