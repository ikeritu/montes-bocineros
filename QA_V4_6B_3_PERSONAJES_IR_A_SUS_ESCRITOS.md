# QA V4.6B.3 — Personajes: Ir a sus escritos

## Comprobación automática

```powershell
py -3 scripts/check_v4_6b_3_personajes_ir_a_sus_escritos.py
```

## Comprobación manual obligatoria

En `personajes.html`:

1. Confirmar que todos los botones documentales se llaman `Ir a sus escritos`.
2. Pulsar cada botón.
3. Confirmar que lleva a los escritos/pruebas del personaje correcto.
4. Confirmar que no salta a otro personaje.
5. Confirmar que no salta a una zona genérica.
6. Probar en móvil.

## Diagnóstico desde navegador

En la consola del navegador se puede comprobar:

```javascript
document.documentElement.getAttribute("data-v46b3-escritos-wired")
document.documentElement.getAttribute("data-v46b3-escritos-unresolved")
```

Si `unresolved` es mayor que 0, habrá que pasar a V4.6B.4 con IDs fijos.
