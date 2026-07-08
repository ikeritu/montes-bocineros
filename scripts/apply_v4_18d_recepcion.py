from pathlib import Path

BLOCK_HTML = """
<!-- V4.18D_RECEPCION_CONTEMPORANEA_START -->
<section class="section" id="recepcion-contemporanea">
  <h2>Recepción contemporánea y fuentes externas</h2>
  <p>La investigación incorpora fuentes modernas de contraste —prensa, divulgación local y especialistas— para explicar cómo la tradición de los Montes Bocineros sigue viva culturalmente, aunque la documentación revisada no confirme una red medieval de cinco cumbres concretas.</p>
  <p>Estas fuentes se usan como apoyo interpretativo y de recepción, no como prueba primaria anterior a 1872.</p>
  <div class="cards">
    <article class="card">
      <h3>DEIA · exposición de cuernos bocineros</h3>
      <p>Recepción institucional y divulgativa contemporánea sobre la tradición material de los cuernos bocineros en el entorno de Juntas Generales.</p>
      <p><a href="https://www.deia.eus/bilbao/2026/05/04/exposicion-repasa-historia-cuernos-bocineros-juntas-generales-11019613.html" target="_blank" rel="noopener">Abrir fuente</a></p>
    </article>
    <article class="card">
      <h3>Harresi · Kolitza / Colisa</h3>
      <p>Lectura local crítica sobre Colisa/Kolitza y su recepción como monte bocinero dentro de la tradición moderna.</p>
      <p><a href="https://editorialharresi.com/colisa-kolitza-de-monte-bocinero-a-monte-molinero/" target="_blank" rel="noopener">Abrir fuente</a></p>
    </article>
    <article class="card">
      <h3>Alberto Santana · lectura crítica</h3>
      <p>Apoyo secundario para explicar la tradición de los montes bocineros como construcción moderna vinculada a la recepción de Antonio de Trueba y el siglo XIX.</p>
      <p><a href="https://www.deia.eus/bizkaia/2017/05/13/bocineros-son-primeros-funcionarios-diputacion-4954034.html" target="_blank" rel="noopener">Abrir fuente</a></p>
    </article>
    <article class="card">
      <h3>Cadena SER / Javier Barrio</h3>
      <p>Síntesis divulgativa reciente sobre la diferencia entre las bocinas documentadas en Gernika y la llamada legendaria desde montes.</p>
      <p><a href="https://cadenaser.com/euskadi/2026/06/04/la-llamada-a-juntas-desde-los-montes-bocineros-historia-o-mito-la-documentacion-nos-dice-que-se-llamaba-desde-gernika-radio-bilbao/" target="_blank" rel="noopener">Abrir fuente</a></p>
    </article>
  </div>
  <p><strong>Uso metodológico:</strong> estas fuentes refuerzan la recepción contemporánea y la lectura crítica, pero no sustituyen a los facsímiles primarios ni desplazan a Trueba 1872 como primer punto firme localizado para la lista nominal completa.</p>
</section>
<!-- V4.18D_RECEPCION_CONTEMPORANEA_END -->
"""

BIB_HTML = """
<!-- V4.18D_BIBLIOTECA_RECEPCION_START -->
<article class="bib-card" id="recepcion-contemporanea" data-bib-item data-tags="recepcion moderna deia harresi santana barrio kolitza colisa">
  <h3>Recepción contemporánea y lectura crítica</h3>
  <p>Las fuentes modernas de prensa, divulgación local e interpretación histórica ayudan a separar la tradición cultural viva de la prueba documental antigua. No sustituyen a los facsímiles primarios, pero refuerzan la cautela metodológica: las cinco bocinas documentadas no equivalen automáticamente a una red medieval de cinco cumbres concretas.</p>
  <ul>
    <li><strong>DEIA, 2026:</strong> exposición sobre cuernos bocineros en el entorno de Juntas Generales.</li>
    <li><strong>Harresi, 2023:</strong> lectura local crítica sobre Colisa/Kolitza y su recepción como monte bocinero.</li>
    <li><strong>Alberto Santana / DEIA, 2017:</strong> interpretación crítica de los montes bocineros como tradición reciente vinculada a Trueba y al siglo XIX.</li>
    <li><strong>Cadena SER / Javier Barrio, 2026:</strong> síntesis divulgativa de la diferencia entre bocinas documentadas en Gernika y llamada legendaria desde montes.</li>
  </ul>
  <p><strong>Clasificación:</strong> fuentes secundarias modernas / recepción contemporánea. <strong>Impacto:</strong> refuerzo editorial; no desplazan la tesis documental.</p>
</article>
<!-- V4.18D_BIBLIOTECA_RECEPCION_END -->
"""

README_BLOCK = """
## Recepción contemporánea

- Se incorporan fuentes modernas de contraste —DEIA, Harresi, Alberto Santana y Javier Barrio/Cadena SER— como apoyo secundario para explicar la vigencia cultural de la tradición y la lectura crítica actual.
- No se usan como prueba primaria anterior a 1872.
- No sustituyen a los facsímiles primarios ni desplazan a Trueba 1872 como primer punto firme localizado para la lista nominal completa.
"""

LLMS_BLOCK = """
- Fuentes modernas de recepción: DEIA, Harresi, Alberto Santana y Javier Barrio/Cadena SER se tratan como apoyo secundario contemporáneo. Refuerzan la lectura crítica, pero no sustituyen a los facsímiles primarios ni desplazan Trueba 1872.
"""

def insert_before_main_end(path: str, block: str, marker: str):
    p = Path(path)
    s = p.read_text(encoding="utf-8-sig")
    if marker in s:
        return
    if "</main>" in s:
        s = s.replace("</main>", block + "\n</main>", 1)
    else:
        s = s.rstrip() + "\n\n" + block + "\n"
    p.write_text(s, encoding="utf-8")

def append_if_missing(path: str, block: str, marker: str):
    p = Path(path)
    s = p.read_text(encoding="utf-8-sig")
    if marker in s:
        return
    s = s.rstrip() + "\n\n" + block.strip() + "\n"
    p.write_text(s, encoding="utf-8")

insert_before_main_end("biblioteca.html", BIB_HTML, "V4.18D_BIBLIOTECA_RECEPCION_START")
insert_before_main_end("estado-investigacion.html", BLOCK_HTML, "V4.18D_RECEPCION_CONTEMPORANEA_START")
insert_before_main_end("historia.html", BLOCK_HTML, "V4.18D_RECEPCION_CONTEMPORANEA_START")
append_if_missing("README.md", README_BLOCK, "## Recepción contemporánea")
append_if_missing("llms.txt", LLMS_BLOCK, "Fuentes modernas de recepción: DEIA, Harresi")
