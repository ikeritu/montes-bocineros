# Informe V4.14 — Auditoría global de enlaces internos y anchors

## Objetivo

Cerrar una fase técnica de salud de navegación antes de continuar con la biblioteca viva y la investigación documental.

## Alcance

Se revisan todas las páginas HTML del repositorio público, incluidas páginas raíz y los informes auxiliares dentro de `informes/`.

La fase valida:

- enlaces internos `href`;
- recursos internos enlazados con `src`;
- anchors `#...` contra atributos `id` y `name`;
- rutas del `sitemap.xml` bajo GitHub Pages;
- páginas canónicas raíz sin `noindex` incluidas en sitemap.

No se validan enlaces externos para evitar falsos positivos por red, rate limits o disponibilidad temporal de terceros.

## Correcciones aplicadas

Se corrigieron enlaces heredados que apuntaban a anchors ya absorbidos o renombrados:

- `veredicto.html#pruebas-documentales` → `veredicto.html#prueba-fuente-por-fuente`
- `biblioteca.html#archivo-tecnico#informe-iturriza-1884` → `estado-investigacion.html#iturriza-estado`
- `biblioteca.html#tabla-maestra-fuentes-maestra-documental` → `biblioteca.html#tabla-maestra-fuentes`
- `biblioteca.html#archivo-tecnico#informe-trueba-v25` → `biblioteca.html#archivo-tecnico`
- `biblioteca.html#trueba-1872-v25` → `biblioteca.html#trueba-1872`
- `../cadena-trueba.html#recepcion` → `../biblioteca.html#recepcion-trueba`
- `../informes.html#comparativa` → `../comparativa.html`

También se corrigió un enlace local con doble fragmento en `estado-investigacion.html`.

## Archivos HTML modificados

- `estado-investigacion.html`
- `historia.html`
- `personajes.html`
- `trueba-facsimil.html`
- `informes/chatgpt.html`
- `informes/copilot.html`
- `informes/minimax-m3.html`
- `informes/nemotron.html`
- `informes/perplexity.html`

## Resultado

`python3 scripts/check_v4_14_links_anchors.py` devuelve PASS.

## Impacto documental

Ninguno. Esta fase no modifica la tesis, las fuentes ni el veredicto histórico.
