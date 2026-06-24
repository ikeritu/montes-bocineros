# ROADMAP V3.9 — QA final de navegación, enlaces y coherencia documental

## Objetivo

Cerrar una fase de estabilidad tras los cambios visuales V3.7 y la reorganización de archivo V3.8.

## Alcance

- Revisar enlaces internos `href` y recursos `src`.
- Revisar recursos `url(...)` en CSS.
- Verificar anclas internas.
- Comprobar que el header global está unificado:
  - Inicio
  - Historia
  - Montes
  - Síntesis crítica
  - Guía del lector
  - Archivo
- Detectar si `Cronología` vuelve a aparecer como botón principal.
- Detectar typos conocidos como `iturrriza` o `profudizar`.
- Generar reporte local `QA_V3_9_NAVEGACION_ENLACES_REPORT.md`.

## Límites

- No cambia contenido histórico.
- No modifica páginas HTML.
- No toca portada, guía, personajes ni archivo salvo que el reporte detecte errores posteriores.
- Es una fase de auditoría, no de rediseño.
