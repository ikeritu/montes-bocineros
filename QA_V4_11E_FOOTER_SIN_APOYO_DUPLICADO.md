# QA V4.11E — Footer sin apoyo duplicado

Ejecutar:

```powershell
py -3 scripts/check_v4_11e_footer_sin_apoyo_duplicado.py
```

Revisión manual:
1. Abrir `index.html`, `personajes.html`, `archivo.html`, `biblioteca.html`, `metodo-citacion.html`.
2. Confirmar que solo hay un bloque “Apoyar el proyecto”.
3. Confirmar que el footer tiene “Información” y “Contacto”.
4. Confirmar que Ko-fi y PayPal no aparecen duplicados en el footer.
