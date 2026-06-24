#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# V4.0 — Llorente 1807 verificado por facsímil
# Ejecutar desde la raíz del repo:
#   python scripts/apply_v4_0_llorente_1807_facsimil.py
# Parche selectivo: no toca diseño global, header ni mapa.

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path.cwd()

REQUIRED_ASSETS = [
    ROOT / 'fuentes' / 'llorente_1807_tomo_ii_p463.png',
    ROOT / 'fuentes' / 'llorente_1807_tomo_ii_p464_cinco_bocinas.png',
]

REPORT = '''# INFORME V4.0 — Llorente 1807 verificado por facsímil

## Fuente revisada

Juan Antonio Llorente, *Noticias históricas de las tres provincias vascongadas*, Tomo II, Parte II: *Origen de sus fueros*, Madrid, Imprenta Real, 1807.

Facsímil digital localizado en HathiTrust / Google Books, ejemplar de University of Michigan.
Handle: https://hdl.handle.net/2027/mdp.39015010944620

## Páginas comprobadas

- Página impresa 463: contexto inmediatamente anterior al comentario de Llorente.
- Página impresa 464: pasaje clave sobre la junta general convocada por medio de las cinco bocinas.
- Página impresa 390: revisada como pista previa; no contiene la referencia útil a bocinas.

## Resultado documental

### Confirmado

Llorente menciona que, en Guernica/Gernika, Juan Núñez de Lara y doña María Díaz de Haro estaban con caballeros, escuderos e hijosdalgo del condado, llamados a junta general por medio de las cinco bocinas.

La formulación relevante está en la página 464:

> llamados á junta general por medio de las cinco bocinas

Esto confirma que Llorente 1807 es una fuente moderna temprana que transmite la fórmula de las cinco bocinas en contexto de Junta General de Vizcaya.

### No confirmado

Llorente no enumera los cinco montes modernos: Gorbeia/Gorbea, Oiz, Sollube, Ganekogorta y Kolitza/Colisa.

La expresión de la misma página sobre “los montes que de derecho le pertenecían” debe entenderse como cuestión de derechos señoriales o patrimoniales, no como lista de montes bocineros nominales.

## Impacto en la tesis de la web

V4.0 refuerza la cadena documental e historiográfica:

- Llorente 1807: cinco bocinas como medio de convocatoria de junta general.
- Madoz 1847: cinco heraldos que suben a alturas con bocinas, sin nombres de montes.
- Trueba 1858/1862/1872: evolución literaria hacia vocinas/montes y fijación nominal tardía.

La conclusión central no cambia: las cinco bocinas están documentadas antes de la lista moderna, pero la lista cerrada de cinco montes concretos no queda probada en Llorente.

## Clasificación

- Cinco bocinas en Llorente: CONFIRMADO.
- Convocatoria de junta general: CONFIRMADO.
- Nombres de cinco montes modernos: NO CONFIRMADO.
- Prueba de lista medieval cerrada de montes bocineros: NO CONFIRMADO.
'''

ROADMAP = '''# ROADMAP V4.0 — Llorente 1807 verificado por facsímil

## Objetivo

Incorporar a la web la verificación directa de Llorente 1807, Tomo II, p. 464, como fuente de la fórmula de las cinco bocinas en contexto de Junta General de Vizcaya.

## Cambios

- Añadir facsímiles locales:
  - `fuentes/llorente_1807_tomo_ii_p463.png`
  - `fuentes/llorente_1807_tomo_ii_p464_cinco_bocinas.png`
- Añadir informe técnico:
  - `INFORME_V4_0_LLORENTE_1807_FACSIMIL.md`
- Actualizar, si existen:
  - `llorente-madoz-trueba.html`
  - `fuentes.html`
  - `historia.html`
  - `cronologia.html`
  - `archivo.html`
  - `pendientes-documentales.html`
  - `TABLA_MAESTRA_FUENTES.md`

## Regla de cautela

La fuente confirma cinco bocinas y junta general, pero no confirma los cinco montes nominales modernos.
'''

QA = '''# QA V4.0 — Llorente 1807 verificado por facsímil

## Comprobaciones esperadas

- Existen los dos recortes de Llorente 1807 en `/fuentes/`.
- `llorente-madoz-trueba.html` deja de presentar la línea como mera hipótesis pendiente.
- `fuentes.html` incorpora una sección clara sobre Llorente 1807.
- `historia.html` añade Llorente 1807 como eslabón anterior a Madoz.
- `cronologia.html` sustituye la entrada pendiente de Llorente por una entrada documentada de 1807.
- La web repite la cautela central: cinco bocinas no equivalen a cinco montes nominales.
- No se toca diseño global ni navegación principal.
'''

V40_BLOCK = '''<section class="v13-panel" id="v40-llorente-1807-facsimil">
  <span class="v13-hook">V4.0 · facsímil directo</span>
  <h2>Llorente 1807: cinco bocinas confirmadas, no cinco montes nominales</h2>
  <p>La revisión del Tomo II de <em>Noticias históricas de las tres provincias vascongadas</em> confirma que Juan Antonio Llorente transmite la fórmula de la junta general llamada <strong>por medio de las cinco bocinas</strong>.</p>
  <p>El pasaje clave está en la página impresa 464. Allí aparecen Juan Núñez de Lara y doña María Díaz de Haro en Guernica/Gernika, con caballeros, escuderos e hijosdalgo del condado, <em>llamados á junta general por medio de las cinco bocinas</em>.</p>
  <p><strong>Límite documental:</strong> Llorente no enumera Gorbeia/Gorbea, Oiz, Sollube, Ganekogorta ni Kolitza/Colisa. La expresión cercana sobre “los montes que de derecho le pertenecían” no debe confundirse con la lista moderna de montes bocineros.</p>
  <div class="source-card-grid">
    <article class="source-card"><span class="v13-label ok">Facsímil</span><h3>Llorente 1807 · p. 463</h3><p>Contexto previo del comentario de Llorente.</p><p><a class="btn" href="fuentes/llorente_1807_tomo_ii_p463.png">Ver p. 463</a></p></article>
    <article class="source-card"><span class="v13-label ok">Clave</span><h3>Llorente 1807 · p. 464</h3><p>Contiene la fórmula “por medio de las cinco bocinas”.</p><p><a class="btn" href="fuentes/llorente_1807_tomo_ii_p464_cinco_bocinas.png">Ver p. 464</a></p></article>
  </div>
  <p class="v13-actions"><a class="btn btn-primary" href="INFORME_V4_0_LLORENTE_1807_FACSIMIL.md">Ver informe V4.0</a><a class="btn btn-ghost" href="https://hdl.handle.net/2027/mdp.39015010944620" rel="noopener noreferrer" target="_blank">Abrir HathiTrust</a></p>
</section>'''

FUENTES_BLOCK = '''<section class="v13-section" id="llorente-1807-facsimil"><div class="v13-panel">
  <div class="section-title-clean"><p class="kicker">V4.0 · facsímil directo</p><h2>Llorente 1807 confirma las cinco bocinas</h2><p class="lead">El Tomo II de Llorente verifica la fórmula de una junta general en Guernica/Gernika llamada por medio de las cinco bocinas. La fuente no enumera los cinco montes modernos.</p></div>
  <div class="source-card-grid">
    <article class="source-card"><span class="v13-label ok">Confirmado</span><h3>Llorente 1807 · Tomo II, p. 464</h3><p>Confirma “llamados á junta general por medio de las cinco bocinas”.</p><p><a class="btn" href="fuentes/llorente_1807_tomo_ii_p464_cinco_bocinas.png">Ver facsímil</a><a class="btn btn-ghost" href="INFORME_V4_0_LLORENTE_1807_FACSIMIL.md">Informe V4.0</a></p></article>
    <article class="source-card"><span class="v13-label pending">Límite</span><h3>No enumera montes</h3><p>Llorente no da la lista Gorbea, Oiz, Sollube, Ganekogorta y Colisa/Kolitza. Cinco bocinas no equivalen automáticamente a cinco cumbres nominales.</p></article>
  </div>
</div></section>'''

ARCHIVO_BLOCK = '''<section class="v13-panel" id="archivo-v40-llorente">
  <span class="v13-hook">Nuevo en V4.0</span>
  <h2>Llorente 1807 verificado por facsímil</h2>
  <p>Se incorpora el recorte de la página 464 del Tomo II de Llorente, donde aparece la fórmula de la junta general llamada por medio de las cinco bocinas.</p>
  <p class="v13-actions"><a class="btn btn-primary" href="INFORME_V4_0_LLORENTE_1807_FACSIMIL.md">Ver informe V4.0</a><a class="btn" href="fuentes/llorente_1807_tomo_ii_p464_cinco_bocinas.png">Ver facsímil clave</a></p>
</section>'''

PENDIENTES_BLOCK = '''<section class="v13-panel" id="v40-llorente-cerrado"><span class="v13-hook">Actualización V4.0</span><h2>Llorente deja de ser una pista pendiente principal</h2><p>La referencia de Llorente 1807 a las cinco bocinas queda verificada por facsímil directo en el Tomo II, p. 464. Lo que sigue sin estar probado en Llorente es la lista nominal moderna de cinco montes.</p><p class="v13-actions"><a class="btn" href="INFORME_V4_0_LLORENTE_1807_FACSIMIL.md">Ver informe V4.0</a></p></section>'''

HISTORIA_CARD = '<article class="v21d-chain-card" id="v40-llorente-chain"><span class="v21d-pill ok">1807</span><h3>Llorente: cinco bocinas verificadas</h3><p>El Tomo II confirma junta general llamada por medio de las cinco bocinas. No enumera los cinco montes modernos.</p></article>'

CRONO_ENTRY = '''<article class="timeline-certainty-item" data-certainty="documentado" data-index="5" data-timeline-event="" id="v40-llorente-1807">
<div class="timeline-certainty-date">1807</div>
<div aria-hidden="true" class="timeline-certainty-dot"></div>
<div class="timeline-certainty-card">
<span class="timeline-certainty-badge">Facsímil verificado</span>
<h3>Llorente: junta general por medio de las cinco bocinas</h3>
<p>El Tomo II de <em>Noticias históricas de las tres provincias vascongadas</em> confirma la fórmula de una junta general en Guernica/Gernika llamada por medio de las cinco bocinas.</p>
<p class="timeline-certainty-limit"><strong>Prueba:</strong> cinco bocinas como medio de convocatoria. <strong>No prueba:</strong> Gorbea, Oiz, Sollube, Ganekogorta y Colisa/Kolitza como lista nominal de montes.</p>
<a class="timeline-certainty-link" href="fuentes/llorente_1807_tomo_ii_p464_cinco_bocinas.png">Ver facsímil →</a>
</div>
</article>'''


def write_text(path: Path, content: str):
    path.write_text(content, encoding='utf-8')
    print(f'OK write: {path.name}')


def read(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def save(path: Path, text: str):
    path.write_text(text, encoding='utf-8')
    print(f'OK update: {path}')


def insert_before_main_end(text: str, block: str) -> str:
    if '</main>' in text:
        return text.replace('</main>', block + '\n</main>', 1)
    if '</body>' in text:
        return text.replace('</body>', block + '\n</body>', 1)
    return text + '\n' + block + '\n'


def update_llorente_page():
    path = ROOT / 'llorente-madoz-trueba.html'
    if not path.exists():
        print('WARN skip: llorente-madoz-trueba.html no existe')
        return
    text = read(path)
    if 'v40-llorente-1807-facsimil' in text:
        print('SKIP: llorente-madoz-trueba.html ya contiene V4.0')
        return
    text = text.replace('V3.1A · investigación en curso', 'V4.0 · facsímil directo')
    text = text.replace('Investigación en curso', 'Llorente 1807 verificado por facsímil')
    text = text.replace(
        '<section class="v13-panel"><h2>Resultado provisional</h2><p>La cadena <strong>Llorente → Madoz → Trueba</strong> es verosímil como evolución historiográfica moderna, pero no está probada como dependencia textual directa y exclusiva.</p><p>Llorente parece reforzar la interpretación de las cinco bocinas como medio de convocatoria a Junta General. Madoz parece añadir una escena más espacializada: cinco heraldos en alturas. Trueba cristaliza después la tradición literaria de los montes mediante la secuencia ya verificada: 1858, 1862 y 1872.</p></section>',
        '<section class="v13-panel"><h2>Resultado V4.0</h2><p>La referencia de Llorente a las cinco bocinas queda verificada por facsímil directo: Tomo II, 1807, página impresa 464.</p><p>Esto refuerza a Llorente como eslabón moderno temprano para la fórmula de las cinco bocinas en contexto de Junta General. No prueba una dependencia textual directa y exclusiva hacia Madoz o Trueba, ni enumera los cinco montes modernos.</p></section>'
    )
    text = text.replace(
        '<tr><td>Llorente es eslabón moderno fuerte.</td><td>Probable</td></tr>',
        '<tr><td>Llorente confirma cinco bocinas como medio de convocatoria.</td><td>Confirmado por facsímil directo, Tomo II, p. 464</td></tr>'
    )
    text = text.replace(
        '<tr><td>Madoz espacializa la tradición hacia alturas/heraldos.</td><td>Probable, pendiente de facsímil directo</td></tr>',
        '<tr><td>Madoz espacializa la tradición hacia alturas/heraldos.</td><td>Confirmado por facsímil directo en Tomo IX, p. 69</td></tr>'
    )
    text = text.replace(
        '<section class="v13-panel"><h2>Siguiente verificación</h2><p>La fase V3.1B debe comprobar directamente las páginas concretas: Llorente 1807, p. 390 y pp. 463-464; Madoz, tomo IX, p. 69. Hasta entonces, esta línea debe mantenerse como investigación en curso.</p><p class="v13-actions"><a class="btn btn-primary" href="INFORME_V3_1A_LLORENTE_MADOZ_TRUEBA.md">Ver informe técnico V3.1A</a><a class="btn btn-ghost" href="pendientes-documentales.html">Ver pendientes documentales</a></p></section>',
        '<section class="v13-panel"><h2>Estado tras V4.0</h2><p>Llorente 1807 queda confirmado como fuente de las cinco bocinas en contexto de Junta General. La prudencia sigue siendo obligatoria: no aporta la lista nominal de cinco montes.</p><p class="v13-actions"><a class="btn btn-primary" href="INFORME_V4_0_LLORENTE_1807_FACSIMIL.md">Ver informe técnico V4.0</a><a class="btn btn-ghost" href="fuentes/llorente_1807_tomo_ii_p464_cinco_bocinas.png">Ver facsímil clave</a></p></section>'
    )
    text = insert_before_main_end(text, V40_BLOCK)
    save(path, text)


def update_fuentes():
    path = ROOT / 'fuentes.html'
    if not path.exists():
        print('WARN skip: fuentes.html no existe')
        return
    text = read(path)
    if 'llorente-1807-facsimil' in text:
        print('SKIP: fuentes.html ya contiene V4.0')
        return
    marker = '<section class="v13-section" id="trueba-facsimil-v25">'
    if marker in text:
        text = text.replace(marker, FUENTES_BLOCK + '\n' + marker, 1)
    else:
        text = insert_before_main_end(text, FUENTES_BLOCK)
    save(path, text)


def update_historia():
    path = ROOT / 'historia.html'
    if not path.exists():
        print('WARN skip: historia.html no existe')
        return
    text = read(path)
    if 'v40-llorente-chain' in text:
        print('SKIP: historia.html ya contiene V4.0')
        return
    madoz_card_start = '<article class="v21d-chain-card"><span class="v21d-pill pending">1847</span><h3>Madoz como puente</h3>'
    if madoz_card_start in text:
        text = text.replace(madoz_card_start, HISTORIA_CARD + '\n' + madoz_card_start, 1)
    else:
        text = insert_before_main_end(text, '<section class="v13-panel" id="v40-llorente-chain"><h2>Llorente 1807 confirmado</h2><p>El facsímil del Tomo II confirma junta general llamada por medio de las cinco bocinas, sin nombres de montes modernos.</p></section>')
    save(path, text)


def update_cronologia():
    path = ROOT / 'cronologia.html'
    if not path.exists():
        print('WARN skip: cronologia.html no existe')
        return
    text = read(path)
    if 'v40-llorente-1807' in text:
        print('SKIP: cronologia.html ya contiene V4.0')
        return
    pattern = re.compile(r'<article class="timeline-certainty-item" data-certainty="pendiente" data-index="5" data-timeline-event="">\s*<div class="timeline-certainty-date">s\. XVIII–XIX</div>[\s\S]*?<h3>Posible eslabón Llorente → Madoz → Trueba</h3>[\s\S]*?</article>', re.M)
    new_text, n = pattern.subn(CRONO_ENTRY, text, count=1)
    if n:
        text = new_text
    else:
        marker = '<article class="timeline-certainty-item" data-certainty="recepcion" data-index="6" data-timeline-event="">\n<div class="timeline-certainty-date">1847</div>'
        if marker in text:
            text = text.replace(marker, CRONO_ENTRY + '\n' + marker, 1)
        else:
            text = insert_before_main_end(text, '<section class="v13-panel" id="v40-llorente-1807"><h2>1807 · Llorente verificado</h2><p>Fórmula de cinco bocinas confirmada por facsímil; no enumera montes.</p></section>')
    save(path, text)


def update_archivo():
    path = ROOT / 'archivo.html'
    if not path.exists():
        print('WARN skip: archivo.html no existe')
        return
    text = read(path)
    if 'archivo-v40-llorente' in text:
        print('SKIP: archivo.html ya contiene V4.0')
        return
    text = insert_before_main_end(text, ARCHIVO_BLOCK)
    save(path, text)


def update_pendientes():
    path = ROOT / 'pendientes-documentales.html'
    if not path.exists():
        print('WARN skip: pendientes-documentales.html no existe')
        return
    text = read(path)
    if 'v40-llorente-cerrado' in text:
        print('SKIP: pendientes-documentales.html ya contiene V4.0')
        return
    text = insert_before_main_end(text, PENDIENTES_BLOCK)
    save(path, text)


def update_tabla_maestra():
    path = ROOT / 'TABLA_MAESTRA_FUENTES.md'
    if not path.exists():
        print('WARN skip: TABLA_MAESTRA_FUENTES.md no existe')
        return
    text = read(path)
    if 'V4.0 — Llorente 1807' in text:
        print('SKIP: TABLA_MAESTRA_FUENTES.md ya contiene V4.0')
        return
    block = '''\n\n## V4.0 — Llorente 1807\n\n| Fuente | Fecha | Estado | Qué prueba | Qué no prueba |\n|---|---:|---|---|---|\n| Juan Antonio Llorente, *Noticias históricas de las tres provincias vascongadas*, Tomo II, p. 464 | 1807 | Confirmado por facsímil directo | Junta general llamada por medio de las cinco bocinas | No enumera Gorbea, Oiz, Sollube, Ganekogorta ni Kolitza/Colisa; no prueba una lista medieval cerrada de montes |\n'''
    text += block
    save(path, text)


def main() -> int:
    for asset in REQUIRED_ASSETS:
        if not asset.exists():
            raise SystemExit(f'ERROR: falta activo requerido: {asset}')
    write_text(ROOT / 'INFORME_V4_0_LLORENTE_1807_FACSIMIL.md', REPORT)
    write_text(ROOT / 'ROADMAP_V4_0_LLORENTE_1807_FACSIMIL.md', ROADMAP)
    write_text(ROOT / 'QA_V4_0_LLORENTE_1807_FACSIMIL.md', QA)
    update_llorente_page()
    update_fuentes()
    update_historia()
    update_cronologia()
    update_archivo()
    update_pendientes()
    update_tabla_maestra()
    print('OK: V4.0 Llorente 1807 aplicado.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
