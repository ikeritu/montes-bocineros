# QA V4.11A.1 — Fuentes absorbida y mapa limpiado

Ejecutar:

```powershell
py -3 scripts/check_v4_11a_1_fuentes_y_mapa_fix.py
```

Revisión manual:

1. Abrir `biblioteca.html`.
2. Confirmar que existe la sección “Tabla maestra de fuentes”.
3. Confirmar que `fuentes.html` ya no existe.
4. Abrir `montes.html`.
5. Confirmar que el mapa 3D carga.
6. Confirmar que no aparece el botón “Ver cómo viajaba el aviso desde Gernika”.
7. Confirmar que el radar acústico didáctico sigue visible.
8. Revisar visualmente que no aparecen POI/animales ajenos en el mapa base.
