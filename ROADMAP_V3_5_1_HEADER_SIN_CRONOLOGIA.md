# V3.5.1 — Header sin Cronología y Montes como puerta principal

## Objetivo

Actualizar la arquitectura visible tras integrar la cronología interactiva dentro de Historia.

## Cambios

- Header principal en todas las páginas:
  - Inicio
  - Historia
  - Montes
  - Síntesis crítica
  - Guía del lector
  - Archivo
- `cronologia.html` deja de ser destino visible y pasa a página-puente `noindex,follow` hacia `historia.html#linea-tiempo-certezas`.
- `sitemap.xml` deja de priorizar `cronologia.html`.
- `llms.txt` se actualiza para IA/GEO.

## Criterio de cierre

- El header ya no muestra Cronología.
- El header muestra Montes.
- Historia contiene la cronología interactiva.
- `cronologia.html` redirige correctamente.
- No hay enlaces rotos internos.
