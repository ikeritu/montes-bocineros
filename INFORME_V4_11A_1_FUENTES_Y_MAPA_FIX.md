# INFORME V4.11A.1 — Fuentes absorbida y mapa limpiado

## Motivo

Tras V4.11A todavía quedaba una separación artificial entre `fuentes.html` y `biblioteca.html`. Esta microfase corrige eso y deja `biblioteca.html` como Biblioteca documental unificada real.

Además, el `montes.html` revisado conservaba restos de la prueba de ondas desde Gernika y enlaces a páginas que la arquitectura limpia ya absorbe.

## Cambios

- `fuentes.html` queda absorbida en `biblioteca.html#tabla-maestra-fuentes`.
- Se eliminan las páginas documentales absorbidas si siguen existiendo.
- Se actualizan enlaces internos hacia los nuevos anclajes de `biblioteca.html`.
- Se retira de `montes.html` el panel de ondas desde Gernika.
- Se retiran referencias `ondas-gernika.css/js`.
- Se normaliza `defer="True"` a `defer`.
- Se parchea `assets/mapbox-montes.js` para ocultar capas POI del mapa base que pueden mostrar iconos ajenos al relato, incluidos animales.

## Límite

Esta fase no fusiona todavía `metodologia.html`, `citar.html` ni `afirmaciones.html`. Eso corresponde a V4.11B.
