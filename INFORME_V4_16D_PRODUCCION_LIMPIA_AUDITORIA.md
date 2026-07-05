# INFORME V4.16D — Producción limpia según auditoría

## Objetivo

Atender los hallazgos de mayor impacto del informe de auditoría web recibido el 4 de julio de 2026, sin alterar la tesis histórica ni romper los checkers históricos del proyecto.

## Alcance aplicado

- Añadir `_config.yml` para que GitHub Pages/Jekyll excluya las notas internas `.md` y `.txt` de la publicación.
- Mantener `llms.txt` y `robots.txt` como archivos públicos útiles.
- Eliminar copias de respaldo HTML publicadas accidentalmente, especialmente `guia-lector.BACKUP_TRUEBA_MARKERS.html`.
- Sustituir enlaces públicos a notas internas por rutas HTML públicas.
- Limpiar `.gitignore` duplicado.

## Decisión técnica

No se mueven físicamente las notas históricas del repositorio para no romper checkers previos que verifican su presencia. En su lugar, se excluyen de la build de GitHub Pages y se retiran los enlaces públicos directos hacia ellas.

## Resultado

La raíz del repositorio puede seguir conservando la bitácora interna para trazabilidad, pero la producción pública queda protegida por `_config.yml` y ya no enlaza esos archivos como contenido público.

## Pendiente posterior

- Consolidar CSS.
- Mejorar `alt` de imágenes informativas.
- Revisar hero con texto HTML real.
- Reauditar navegación secundaria y sitemap cuando se decida el conjunto final de páginas públicas.
