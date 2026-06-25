# QA V4.6B.2 — Personajes: pruebas documentales directas

## Comprobaciones automáticas

- Existe `personajes.html`.
- Existe marcador `V4_6B_2_PERSONAJES_PRUEBAS_DIRECTAS_START`.
- Existe script `v46b2-personajes-pruebas-script`.
- Se usa prefijo `pruebas-documentales-`.
- Se añade navegación con `scrollIntoView`.
- Se añade `aria-controls`.

## Comprobación manual obligatoria

En `personajes.html`:

1. Pulsar `Ver pruebas documentales` en cada ficha.
2. Confirmar que lleva al bloque de pruebas del personaje correcto.
3. Confirmar que no abre una zona genérica.
4. Confirmar que en móvil no se rompe el diseño.

## Comando

```powershell
py -3 scripts/check_v4_6b_2_personajes_pruebas_directas.py
```
