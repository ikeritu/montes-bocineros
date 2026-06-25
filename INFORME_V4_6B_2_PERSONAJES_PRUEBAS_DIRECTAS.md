# INFORME V4.6B.2 — Personajes: enlaces directos a pruebas documentales

## Objetivo

Corregir la navegación de `personajes.html`.

Cuando el usuario pulse `Ver pruebas documentales` dentro de la ficha de un personaje, debe ir directamente al bloque de pruebas documentales de ese personaje.

## Solución aplicada

Se añade un bloque JS/CSS idempotente al final de `personajes.html`:

- detecta botones y enlaces con texto `Ver pruebas documentales`;
- identifica la ficha del personaje;
- localiza el bloque de pruebas documentales dentro de esa ficha o en la página;
- asigna un `id` estable con prefijo `pruebas-documentales-`;
- convierte el botón/enlace en navegación directa;
- abre `<details>` si el bloque está plegado;
- desplaza suavemente hasta el bloque;
- añade `aria-controls` para accesibilidad.

## Alcance

Solo toca `personajes.html`.

No cambia contenido documental.
No altera la tesis.
No toca páginas de fuentes, cronología o veredicto.

## Revisión manual

Después de aplicar:

1. Abrir `personajes.html`.
2. Pulsar `Ver pruebas documentales` en cada ficha.
3. Confirmar que salta al bloque de pruebas del mismo personaje.
4. Probar en móvil.
