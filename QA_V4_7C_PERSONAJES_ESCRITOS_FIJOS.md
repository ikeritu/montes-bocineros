# QA V4.7C — Personajes: escritos fijos

## Comprobación automática

```powershell
py -3 scripts/check_v4_7c_personajes_escritos_fijos.py
```

## Comprobación manual

En `personajes.html`:

1. Abrir Profundizar.
2. Confirmar que no aparece `Glosario`.
3. Confirmar que no aparece `Preguntas frecuentes`.
4. Confirmar que todos los botones de ficha dicen `Ir a sus escritos`.
5. Pulsar cada botón y confirmar que baja a la sección correcta del mismo personaje.
6. Revisar móvil.
