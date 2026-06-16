# V5.50 — Home CSS aislado y cache busting

Fecha: 2026-06-16

## Diagnóstico

La imagen seguía descentrada por combinación de:
1. CSS antiguo acumulado en `styles.css`.
2. Regla previa `max-height` que reducía el ancho visual.
3. Posible caché de `assets/styles.css` en GitHub Pages/navegador.
4. Falta de aislamiento del layout del index.

## Solución aplicada

- `body class="home-page"` en `index.html`.
- `assets/styles.css?v=5.50`.
- Nuevo `assets/home.css?v=5.50`.
- `.index-hero-image` escala por ancho, no por alto.
- `max-height:none`.
- `main`, header, imagen, CTA y bloque “En 30 segundos” forzados a una columna centrada.
- Contenido documental V5.49 conservado.
