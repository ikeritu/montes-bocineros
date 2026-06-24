# V3.6.4 — Header global unificado y encuadre de Goicolea

## Objetivo
Corregir dos incidencias detectadas tras V3.6:

1. Headers inconsistentes entre páginas y subpáginas.
2. Encuadre incorrecto de la recreación IA de Tomás de Goicolea en personajes.html.

## Decisión
- Header único en todos los HTML con `site-header`.
- Menú principal: Inicio · Historia · Montes · Síntesis crítica · Guía del lector · Archivo.
- Cronología sale del header porque está integrada en Historia.
- No se elimina cronologia.html para no romper enlaces; queda como puente/noindex si ya estaba configurada así.
- La tarjeta de Tomás de Goicolea usa una clase específica para que la imagen llene el panel y centre el rostro.

## Fuera de alcance
- No se cambia la tesis documental.
- No se toca el contenido histórico de fichas.
- No se reestructura la página de personajes.
