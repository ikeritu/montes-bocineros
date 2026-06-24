# QA V3.6.2 — Ajustes de personajes y scroll

## Archivos modificados

- `assets/personajes-interactivo-v36.css`
- `assets/menu.js`

## Comprobaciones manuales

### Personajes

- Abrir `personajes.html`.
- Revisar la ficha de Tomás de Goicolea.
- Confirmar que la imagen ya no recorta parte importante del rostro.
- Confirmar que el badge “Recreación IA” sigue visible.
- Confirmar que las demás fichas no se rompen.

### Navegación

- Desde una página con scroll avanzado, pulsar en el header:
  - Inicio
  - Historia
  - Montes
  - Síntesis crítica
  - Guía del lector
  - Archivo
- Confirmar que cada página nueva carga arriba.
- Confirmar que los enlaces con ancla siguen funcionando, por ejemplo:
  - `historia.html#linea-tiempo-certezas`
  - `montes.html#visual-acustica`

## Resultado esperado

Parche visual/UX correcto sin cambios documentales.
