# INFORME V4.7D — Microglosario y escritos reales

## Problemas corregidos

1. El contenido del antiguo `Glosario y términos clave` no quedó bien integrado en `Microglosario / Palabras clave`.
2. En `personajes.html`, varios personajes no llevaban a escritos, originales o facsímiles: Lope García de Salazar, Tomás de Goicolea, Ibargüen-Cachopín y Juan Ramón de Iturriza y Zabala.
3. Iturriza podía llevar a una página técnica/markdown, lo cual no debe presentarse como escrito original.

## Solución

- Se intenta recuperar el antiguo `glosario.html` desde Git.
- Si no se puede recuperar, se incorpora un microglosario crítico de reserva con los términos clave.
- El microglosario queda dentro de `Palabras clave`, no como bloque separado.
- En personajes, los casos sin facsímil/original local quedan marcados explícitamente como pendientes.
- No se enlaza a markdown ni a una página técnica como si fuese prueba documental directa.

## Criterio

Mejor marcar `pendiente de facsímil/original local` que simular un enlace documental con una página genérica.
