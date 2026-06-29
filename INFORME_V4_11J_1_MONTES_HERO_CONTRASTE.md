# INFORME V4.11J.1 — Contraste del hero en montes.html

## Objetivo

Corregir un problema visual detectado tras V4.11J: el relieve animado heredado del `index.html` aparecía en `montes.html` con poco contraste. Los montes y el punto de Gernika quedaban demasiado integrados con el fondo verde.

## Causa

La fase V4.11I.1 añadió en `assets/v411i1-produccion-polish.css` una regla específica para `montes.html`:

- `.mb2-hero .v34-relief{opacity:.58;}`
- máscara verde inferior en `.mb2-hero .v34-relief::before`

Esto suavizaba demasiado los trazos del relieve dentro de un hero que ya usa tonos verdes próximos.

## Cambios aplicados

- Nuevo CSS: `assets/v411j1-montes-hero-contrast.css`.
- Enlace añadido en `montes.html`, después de `v411i1-produccion-polish.css`.
- Se eleva la opacidad del relieve en `montes.html`.
- Se reduce la máscara verde inferior.
- Se refuerzan trazos, sombras y brillo de los montes.
- Se refuerza el punto de Gernika con color claro, contorno oscuro y halo.
- No se toca contenido documental ni estructura de navegación.

## Archivos modificados

- `montes.html`
- `assets/v411j1-montes-hero-contrast.css`
- `scripts/check_v4_11j_1_montes_hero_contrast.py`
- `QA_V4_11J_1_MONTES_HERO_CONTRASTE.md`
- `QA_V4_11J_1_MONTES_HERO_CONTRASTE_REPORT.md`
- `ROADMAP_V4_11J_1_MONTES_HERO_CONTRASTE.md`

## Resultado esperado

El hero de `montes.html` conserva su diseño propio, pero el relieve se lee mejor y queda más próximo al contraste visual del hero de `index.html`.
