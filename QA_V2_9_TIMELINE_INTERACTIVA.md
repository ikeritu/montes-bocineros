# QA V2.9 — Cronología interactiva de certezas documentales

## Resultado
PASS con revisión manual recomendada de `cronologia.html` en escritorio y móvil.

## Cambios verificados
- `cronologia.html` usa `assets/timeline-interactiva.css?v=2.9.0`.
- `cronologia.html` usa `assets/timeline-interactiva.js?v=2.9.0`.
- Existe explorador interactivo horizontal con `data-timeline-interactive`.
- Existe rail dinámico `data-timeline-rail`.
- Existe ficha dinámica `data-timeline-detail`.
- Existe navegación anterior/siguiente.
- Se conserva lista completa como fallback accesible y rastreable.

## Métricas QA
- HTML raíz revisados: 30
- Páginas sin `main#contenido`: 0
- Enlaces/assets locales faltantes: 0
- Anclas internas dudosas: 0
- `href="#"`: 0
- Enlaces directos a `.md` fuera de `archivo-tecnico.html`: 0
- Items de timeline/fallback: 15
- Botones de filtro: 5
- JSON-LD en cronología: 2
- Asset CSS interactivo existe: True
- Asset JS interactivo existe: True

## Errores
No se detectan errores estáticos bloqueantes.

## Nota documental
No se han añadido nuevos hechos históricos. La tesis se mantiene intacta:
- 1858: siete vocinas / siete montes euskaros.
- 1862: cinco vocinas / cinco montes euskaros, sin nombres.
- 1872: primera lista nominal completa localizada hasta ahora.

## Revisión visual recomendada
- Comprobar filtros.
- Comprobar clic en puntos del eje.
- Comprobar botones anterior/siguiente.
- Comprobar scroll horizontal en móvil.
- Comprobar que la lista completa/fallback se despliega correctamente.
