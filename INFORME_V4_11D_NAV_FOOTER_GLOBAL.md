# INFORME V4.11D — Navegación global y ajuste visual final

## Motivo

Tras V4.11A–C, la arquitectura ya estaba consolidada, pero cada subpágina conservaba una variante distinta del menú “Profundizar”. Además, en `personajes.html` algunos botones largos de facsímiles/locales podían desbordar las tarjetas.

## Cambios

- Unificación del menú “Profundizar” en todas las páginas con cabecera.
- Unificación del footer “Información” en todas las páginas con footer.
- Normalización de enlaces hacia la arquitectura actual:
  - `archivo.html`
  - `biblioteca.html`
  - `personajes.html`
  - `metodo-citacion.html`
  - `autor.html`
- Eliminación de referencias residuales a páginas absorbidas.
- CSS nuevo `assets/v411d-nav-footer.css` para:
  - evitar overflow en botones largos de `personajes.html`;
  - permitir salto de línea en enlaces largos;
  - mejorar comportamiento móvil del menú.

## Límite

No crea páginas nuevas y no fusiona contenido adicional. Es una fase de coherencia global, navegación y limpieza visual.
