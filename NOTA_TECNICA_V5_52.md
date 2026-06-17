# V5.52 — Mapa 3D único reparado

Fecha: 2026-06-16

Cambios:
- Eliminada de `mapa.html` la imagen estática de portada añadida en V5.51.
- Eliminado bloque duplicado `mapa-3d-montes`.
- Creado un único bloque real `mapbox-3d-section`.
- Contenedor real: `#mapbox-montes`.
- Altura mínima visible: 560px.
- Se añade/asegura carga de Mapbox GL JS/CSS si faltaba.
- Se conserva la portada/index intacta.

Objetivo:
- La imagen estática solo debe aparecer en el index.
- La pantalla de montes/mapa debe mostrar un único mapa interactivo 3D.
