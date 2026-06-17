# V5.54 — Mapa 3D en posición correcta

Fecha: 2026-06-16

Problema real localizado:
- Seguía existiendo arriba una sección antigua:
  `<section class="mapa-simple-map"><div class="mapbox-shell mapa-shell-simple"></div></section>`
- Esa caja vacía era el rectángulo verde gigante.
- El Mapbox real de V5.53 estaba más abajo.

Solución:
- Eliminada la sección antigua `mapa-simple-map`.
- Extraído el único bloque `mapbox-3d-section`.
- Reinsertado justo después de “Puntos incluidos”.
- Cache busting del JS a `assets/mapbox-montes.js?v=5.54`.
- CSS defensivo para ocultar restos vacíos si aparecen.
