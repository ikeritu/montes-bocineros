# QA V3.6.6 — Ajuste de encuadre de Tomás de Goicolea

## Objetivo

Corregir únicamente el encuadre de la imagen de Tomás de Goicolea en `personajes.html`.

## Cambios

- Archivo modificado: `assets/personajes-interactivo-v36.css`.
- Regla afectada: `.p36-media-goicolea img`.
- Cambio escritorio: `object-position: 58% 18%` → `66% 18%`.
- Cambio móvil: `object-position: 58% 16%` → `64% 16%`.

## Criterio

El ajuste es específico para la clase `p36-media-goicolea`, por lo que no afecta al resto de imágenes de personajes.

## Revisión manual

Revisar:

- `personajes.html#tomas-goicolea`
- Escritorio: la imagen ocupa todo el alto y el rostro queda más centrado.
- Móvil: la imagen mantiene un encuadre aceptable.
- Resto de retratos: sin cambios visuales.
