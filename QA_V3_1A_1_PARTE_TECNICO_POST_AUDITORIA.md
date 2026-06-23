# QA V3.1A.1 — Parche técnico post-auditoría

## Resultado
PASS.

## Cambios verificados
- `assets/menu.js` cargado en páginas con botón Profundizar: 31 páginas revisadas, 0 fallos.
- JSON-LD duplicado: 0 páginas con duplicado tras limpieza.
- Enlaces/assets locales en HTML raíz: 0 faltantes.
- `404.html`: OK.
- `sitemap.xml`: 20 URLs indexables.
- Páginas HTML raíz indexables: 20.
- Páginas HTML raíz noindex/follow: 12.
- PNG pesados no referenciados restantes: 0.

## Decisiones técnicas
- `veredicto.html` mantiene el nombre del archivo para no romper enlaces, pero la etiqueta pública queda como “Síntesis crítica”.
- Las páginas `noindex,follow` no se incluyen en `sitemap.xml`.
- No se mueve aún el archivo interno `QA_*`, `ROADMAP_*`, `NOTA_*`; queda para una fase de arquitectura del repositorio.

## Tesis documental
Sin cambios.

La cadena Llorente → Madoz → Trueba sigue clasificada como hipótesis historiográfica fuerte pendiente de facsímil directo.
