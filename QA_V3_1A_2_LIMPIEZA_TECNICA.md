# QA V3.1A.2 — Limpieza técnica pendiente

## Resultado
PASS.

## Comprobaciones
- HTML raíz revisados: 32
- 404.html: OK
- assets/menu.js en páginas con Profundizar: OK
- JSON-LD @id duplicados: OK
- Enlaces/assets locales faltantes: OK
- sitemap.xml URLs indexables: 20
- Páginas HTML raíz indexables: 20
- Páginas HTML raíz noindex/follow: 12
- PNG pesados no referenciados: OK
- Query strings normalizados a v=3.1.2: 127

## Decisiones técnicas
- `veredicto.html` mantiene el nombre de archivo por compatibilidad, pero la etiqueta pública queda como “Síntesis crítica”.
- Las páginas `noindex,follow` quedan fuera del sitemap.
- `404.html` también es `noindex,follow`.
- No se mueve todavía el archivo interno `QA_*`, `ROADMAP_*`, `NOTA_*`.

## Tesis documental
Sin cambios. Llorente → Madoz → Trueba sigue como hipótesis historiográfica fuerte pendiente de facsímil directo.
