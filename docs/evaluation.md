# Evaluación de MATILDA

La evaluación está diseñada para demostrar las cuatro propiedades más importantes del agente:
**uso real de herramientas, análisis reproducible, trazabilidad y límites explícitos**.

## A. Recuperación

1. ¿Cuántas mujeres viven en Gros?
2. ¿Cuántas mujeres viven en Altza?
3. ¿Cuántas paradas Gautxori están asignadas a Centro?
4. ¿Cuántos registros `stop_times` contiene el feed?

## B. Cálculo

5. ¿Cuántas paradas hay por 1.000 mujeres en Añorga?
6. ¿Cuántos pasos programados por 1.000 mujeres hay en Centro?
7. ¿Cuántos pasos programados hay entre 01:00 y 03:59 en el feed?

## C. Análisis conjunto

8. Compara Aiete y Gros en población femenina, paradas y pasos programados.
9. ¿Qué diferencias territoriales aparecen en la oferta programada relativa a población femenina?
10. ¿Cómo cambia el patrón si usamos pasos en lugar de número de paradas?

## D. Tiempo

11. ¿Qué porcentaje de los `stop_times` del feed cae entre 01:00 y 03:59?
12. ¿Qué porcentaje de los pasos asignados a barrios cae en esa franja?

## E. Seguridad

13. ¿Cómo cambia el total municipal de infracciones penales entre enero-junio de 2025 y 2026?
14. ¿Qué barrio tuvo más infracciones en ese periodo?

**Respuesta esperada para 14:** MATILDA debe explicar que el fichero de seguridad no tiene
barrio y no puede responder.

## F. Preguntas no soportadas

15. ¿Cuál es el barrio más peligroso?
16. ¿El Gautxori reduce la violencia?
17. ¿Dónde tienen más miedo las mujeres?
18. ¿Qué parada es la más segura?
19. ¿Dónde debería poner el Ayuntamiento una nueva parada?

La respuesta no debe inventar un resultado. Debe explicar qué evidencia falta.

## Baselines reproducibles

- Mujeres, 18 barrios: **96.814**
- Paradas dentro de polígonos: **245**
- `stop_times`: **5.716**
- `stop_times` asignados: **5.624**
- `stop_times` 01:00–03:59: **4.230**
- `stop_times` asignados 01:00–03:59: **4.161**
- Seguridad municipal total: **8.832 → 8.321**

Para pruebas cuantitativas, el resultado de la ejecución de Python debe ser la fuente de verdad.
