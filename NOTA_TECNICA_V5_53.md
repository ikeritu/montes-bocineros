# V5.53 — Mapbox token + contenedor único

Fecha: 2026-06-16

Cambios:
- Eliminados contenedores antiguos/duplicados del mapa.
- `mapa.html` usa un único bloque:
  - `#mapbox-3d-section`
  - `#mapbox-map`
  - `#mapbox-status`
- `assets/mapbox-montes.js` reescrito con el token público indicado por el usuario.
- El mapa usa Mapbox GL JS v3.8.0.
- La imagen estática no aparece en mapa.html.
- Portada/index sin cambios.

Token público usado:
pk.eyJ1IjoiaWtlcml0dSIsImEiOiJjbXFjdGNpMm8wbG1tMnFxd24xNmxxOW80In0.9_4k7dTyGJPcKKsVcHnBHA
