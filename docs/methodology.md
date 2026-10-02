# Metodología

## 1. Pregunta

MATILDA estudia de forma descriptiva la relación entre:

- población femenina por barrio;
- oferta programada del Gautxori;
- contexto municipal de seguridad.

No intenta estimar causalidad ni producir una clasificación de seguridad de barrios.

## 2. Población

Se lee `poblacion_barrio_2025_2.csv.csv` como CSV separado por `;`. La fuente contiene
una fila municipal para Donostia seguida de las 18 filas de barrio relevantes.

La columna `Mujeres` usa `.` como separador de miles. Por ejemplo, `7.354` representa
7.354 personas, no 7,354 en notación decimal.

La suma de las 18 filas de barrio es **96.814 mujeres**, coherente con la fila municipal.

## 3. GTFS

Los registros de `stop_times2.txt` representan pasos programados de viajes por paradas.
Se unen con `stops2.txt` cuando se necesita información de parada y con `trips2.txt`
cuando se necesitan rutas.

El indicador de pasos es, por tanto, una medida de **oferta programada**, no de uso real.

## 4. Espacialización

`gautxori_paradas_barrios.csv` es la correspondencia operativa entre `stop_id` y los
polígonos de `barrios_donostia.geojson.json`.

- 245 paradas quedan dentro de un polígono.
- 3 quedan sin asignar.

Las 3 no se fuerzan a ningún barrio.

## 5. Indicadores

### Paradas por 1.000 mujeres

`paradas únicas / mujeres × 1.000`

### Pasos programados por 1.000 mujeres

`stop_times asignados / mujeres × 1.000`

### Pasos por franja

Se filtra `departure_time` por la hora solicitada antes de agrupar.

## 6. Seguridad

`seguridad_donostia_2025_2026_2.csv` se mantiene a escala municipal. Para el total se utiliza
la fila `TOTAL INFRACCIONES PENALES`; no se suman categorías potencialmente solapadas.

## 7. Interpretación

Un indicador relativo mayor o menor describe una diferencia en la relación entre oferta
programada y población femenina. No demuestra accesibilidad, demanda, calidad, seguridad
percibida ni causalidad.

## 8. Regla de respuesta

Cada análisis debería distinguir:

**HECHO → PATRÓN → INTERPRETACIÓN → LIMITACIÓN**

La ejecución verificable tiene prioridad sobre cifras recordadas de conversaciones anteriores.
