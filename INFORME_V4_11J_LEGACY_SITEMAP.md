# Informe V4.11J — Redirecciones legacy y sitemap limpio

Fecha: 2026-06-30

## Objetivo

Cerrar la deuda técnica generada por la unificación de páginas en V4.11: varias URLs antiguas seguían apareciendo en `sitemap.xml` o en informes auxiliares, aunque su contenido ya había sido absorbido por `biblioteca.html`, `guia-lector.html`, `metodo-citacion.html`, `trueba-facsimil.html` y otras páginas canónicas.

## Cambios aplicados

- Se crean páginas puente `noindex,follow` para conservar enlaces antiguos y evitar errores 404.
- Se actualiza `sitemap.xml` con páginas reales/canónicas y `lastmod` `2026-06-30`.
- Se excluyen del sitemap las URLs legacy que solo sirven como puente.
- Se añade checker específico `scripts/check_v4_11j_legacy_sitemap.py`.

## Redirecciones creadas

- `fuentes.html` → `biblioteca.html#tabla-maestra-fuentes`
- `archivo-tecnico.html` → `biblioteca.html#archivo-tecnico`
- `glosario.html` → `guia-lector.html#glosario-rapido`
- `faq.html` → `guia-lector.html#faq-rapida`
- `barrio-banales.html` → `biblioteca.html#barrio-banales`
- `metodologia.html` → `metodo-citacion.html#metodologia`
- `afirmaciones.html` → `metodo-citacion.html#afirmaciones-verificables`
- `citas.html` → `biblioteca.html#citas-verificadas`
- `citar.html` → `metodo-citacion.html#como-citar`
- `cadena-trueba.html` → `trueba-facsimil.html`
- `pendientes-documentales.html` → `biblioteca.html#pendientes-documentales`
- `informes.html` → `biblioteca.html#informes-ia`

## Resultado esperado

- Los informes antiguos dejan de provocar enlaces rotos.
- Google/GitHub Pages no reciben un sitemap con páginas eliminadas.
- Las URLs históricas siguen funcionando para lectores o enlaces externos.
