# V3.6.2 — Ajustes de personajes y carga superior

## Objetivo

Parche quirúrgico posterior a V3.6 para corregir dos incidencias visuales/UX detectadas en QA:

1. La recreación IA de Tomás de Goicolea quedaba mal encajada en la tarjeta y recortaba parte del rostro.
2. Al navegar desde el header entre páginas, el navegador podía restaurar una posición de scroll anterior en lugar de cargar la página desde arriba.

## Cambios

- `assets/personajes-interactivo-v36.css`
  - Ajuste específico para `#tomas-goicolea .p36-media img`.
  - Se usa `object-fit: contain` para priorizar que no se corte el rostro.

- `assets/menu.js`
  - Se añade control de `history.scrollRestoration = 'manual'`.
  - En `pageshow`, si la URL no tiene ancla, se fuerza `scrollTo(0, 0)`.
  - Si la URL contiene `#seccion`, se respeta el salto al ancla.

## No cambia

- No se modifica la tesis documental.
- No se modifican textos históricos.
- No se tocan imágenes ni activos de fuentes.
- No se cambia la arquitectura de páginas.
