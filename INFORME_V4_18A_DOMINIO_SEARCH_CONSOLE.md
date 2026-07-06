# Informe V4.18A — Dominio propio y Search Console

## Resultado

V4.18A establece `https://montesbocineros.eus/` como dominio público y canónico del proyecto **Montes Bocineros de Bizkaia**.

La infraestructura técnica continúa siendo GitHub Pages, pero la URL citable, los metadatos, el sitemap y `llms.txt` pasan a priorizar el dominio propio.

## Cambios aplicados

- Añadido archivo `CNAME` con `montesbocineros.eus`.
- Sustituidas URLs absolutas antiguas de `https://ikeritu.github.io/montes-bocineros/` por `https://montesbocineros.eus/` en páginas HTML públicas.
- Actualizados `canonical`, `og:url`, `og:image`, `twitter:image` y JSON-LD `@id`/`url`.
- Actualizado `robots.txt` para declarar `https://montesbocineros.eus/sitemap.xml`.
- Regenerado `sitemap.xml` con URLs del dominio propio y `lastmod` 2026-07-06.
- Actualizado `llms.txt` para que las páginas prioritarias apunten al dominio `.eus`.
- Actualizados `README.md`, `VERSION.txt`, `CHANGELOG.txt`, `ESTADO_ACTUAL.md` y `ROADMAP.md`.
- Añadidos scripts `apply_v4_18a_dominio_search_console.py` y `check_v4_18a_dominio_search_console.py`.

## Search Console

V4.18A no verifica Search Console automáticamente, porque Google requiere una acción externa del propietario. Queda preparado el flujo:

1. Añadir propiedad de dominio o prefijo URL en Google Search Console.
2. Verificar `https://montesbocineros.eus/`.
3. Enviar sitemap: `https://montesbocineros.eus/sitemap.xml`.
4. Solicitar indexación de páginas nucleares: inicio, guía, veredicto, historia, montes, biblioteca, archivo, Trueba facsímil y autor.

## Tesis documental

Sin cambios. Trueba 1872 continúa como primer punto firme localizado para la lista nominal completa Gorbea, Oiz, Sollube, Ganecogorta y Colisa.
