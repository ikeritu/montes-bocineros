# QA V3.9 — navegación, enlaces y coherencia documental

## Archivos añadidos

- `scripts/check_v3_9_navigation_links.py`
- `ROADMAP_V3_9_NAVEGACION_ENLACES.md`
- `QA_V3_9_NAVEGACION_ENLACES.md`

## Ejecución

Desde la raíz del repositorio:

```powershell
python scripts/check_v3_9_navigation_links.py
```

o:

```powershell
py -3 scripts/check_v3_9_navigation_links.py
```

## Resultado esperado

- El script termina con `PASS — sin errores bloqueantes`.
- Se genera `QA_V3_9_NAVEGACION_ENLACES_REPORT.md`.
- Si aparecen errores, no congelar V3.9 hasta corregirlos.
