# INFORME V4.7A — Guía del lector unificada

## Objetivo

Simplificar la arquitectura de lectura.

Antes había tres entradas potenciales de apoyo:

- Preguntas frecuentes.
- Guía del lector.
- Glosario.

La decisión de V4.7A es dejarlo todo concentrado en una sola página: `guia-lector.html`.

## Cambios

- En la zona `Profundizar`, `Preguntas frecuentes` pasa a ser `Guía del lector`.
- El contenido de `glosario.html` se integra dentro de `guia-lector.html`.
- Los enlaces internos a `glosario.html` pasan a `guia-lector.html#glosario`.
- `glosario.html` se elimina como subpágina independiente.
- Si existen subpáginas FAQ (`preguntas-frecuentes.html`, `faq.html`, etc.), se eliminan.

## Criterio UX

Menos páginas auxiliares, menos dispersión y una ruta de lectura más clara para usuarios nuevos.

## Riesgo

La guía puede quedar larga. Si visualmente queda densa, la siguiente fase debe ordenar la guía con índice interno, acordeones o secciones más compactas.
