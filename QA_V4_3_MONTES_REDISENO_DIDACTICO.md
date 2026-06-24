# QA V4.3 — Montes rediseño didáctico

## Comprobaciones manuales

Revisar en local y online:

- `montes.html` carga sin errores visuales.
- El bloque “De las merindades a los montes” aparece antes de las fichas.
- Los botones de anclaje saltan a cada monte.
- El mapa 3D sigue funcionando.
- El mapa estático sigue disponible.
- El radar acústico sigue funcionando.
- En móvil, las fichas se ven en una sola columna y no se rompen.
- La página no afirma que los cinco montes concretos estén probados como medievales.

## Comprobación automática

Ejecutar:

```powershell
python scripts/check_v4_3_montes_redisenio_didactico.py
```
