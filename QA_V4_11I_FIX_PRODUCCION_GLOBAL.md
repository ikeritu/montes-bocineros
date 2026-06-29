# QA V4.11I — Corrección de producción global

Ejecutar:

```powershell
py -3 scripts/check_v4_11i_fix_produccion_global.py
```

Revisión visual:

1. Abrir `index.html`.
2. Abrir `montes.html`.
3. Abrir `veredicto.html`.
4. Abrir `biblioteca.html`.
5. Confirmar que el menú principal es idéntico.
6. Confirmar que el menú “Profundizar” es idéntico.
7. Confirmar que el footer es idéntico.
8. Confirmar que “Apoyar el proyecto” aparece una sola vez.
9. Confirmar que `biblioteca.html` no muestra textos `[Propuesta interactiva: ...]`.
10. Confirmar que `biblioteca.html` no muestra “No hay resultados...” al cargar.
