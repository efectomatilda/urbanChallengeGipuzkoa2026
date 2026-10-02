# Preguntas de demo — MATILDA.AI

Este documento recoge las preguntas recomendadas para presentar y probar MATILDA.AI durante una demostración.

La secuencia está pensada para mostrar la evolución del análisis:

**población → oferta nocturna → barrios → cobertura descriptiva → contexto de seguridad → siguiente fase**

Todas las preguntas están formuladas para que el agente utilice `ejecutar_codigo` cuando sea necesario y no invente información.

---

## 1. Población femenina

### Pregunta

> ¿Cuáles son los 5 barrios de Donostia con más población femenina en 2025 y qué porcentaje representan sobre el total de mujeres de la ciudad? Usa ejecutar_codigo para calcularlo.

### Qué queremos demostrar

Que MATILDA sabe leer correctamente `poblacion_barrio_2025_2.csv`, identificar exclusivamente los 18 barrios de Donostia y calcular porcentajes con el denominador correcto.

### Resultado de referencia

Los cinco barrios con mayor población femenina son:

| Barrio | Mujeres |
|---|---:|
| Amara Berri | 15.861 |
| Centro | 11.633 |
| Altza | 10.353 |
| Gros | 9.408 |
| Intxaurrondo | 7.811 |

En conjunto representan **55.066 mujeres**, aproximadamente el **56,9 %** de las 96.814 mujeres de los 18 barrios analizados.

---

## 2. Oferta nocturna del Gautxori

### Pregunta

> ¿Cómo se distribuye la oferta programada del Gautxori durante la noche? Identifica las franjas con más pasos y calcula qué porcentaje del total se concentra entre la 01:00 y las 03:59. Usa ejecutar_codigo.

### Qué queremos demostrar

Que MATILDA puede trabajar con los archivos GTFS y analizar horarios programados por franjas.

### Resultado de referencia

| Franja | Pasos programados |
|---|---:|
| 00:00–00:59 | 961 |
| 01:00–01:59 | 1.600 |
| 02:00–02:59 | 1.553 |
| 03:00–03:59 | 1.077 |
| 04:00–04:59 | 443 |
| 05:00–05:59 | 82 |

El GTFS analizado contiene **5.716 registros de paso programados** asociados a **303 viajes**.

Entre 01:00 y 03:59 se concentran **4.230 registros**, el **74,0 %** del total analizado.

Estos datos representan programación GTFS, no pasajeros ni uso real.

---

## 3. Paradas por barrio

### Pregunta

> ¿Cuántas paradas del Gautxori hay en cada uno de los 18 barrios de Donostia? Usa los datos disponibles y ejecuta ejecutar_codigo para calcularlo. Muestra una tabla con el barrio y el número de paradas. No inventes datos.

### Qué queremos demostrar

Que MATILDA puede utilizar la nueva correspondencia espacial entre las coordenadas de las paradas y los polígonos de barrio.

### Resultado de referencia

| Barrio | Paradas |
|---|---:|
| Aiete | 39 |
| Altza | 31 |
| Amara Berri | 17 |
| Antiguo | 24 |
| Ategorrieta-Ulia | 7 |
| Añorga | 12 |
| Centro | 24 |
| Egia | 14 |
| Gros | 6 |
| Ibaeta | 15 |
| Igeldo | 0 |
| Intxaurrondo | 26 |
| Landarbaso | 0 |
| Loiola | 12 |
| Martutene | 7 |
| Miracruz-Bidebieta | 11 |
| Miramon-Zorroaga | 0 |
| Zubieta | 0 |

Se obtienen **245 paradas asignadas** a los polígonos de los 18 barrios. El GTFS contiene 248 paradas únicas; 3 no quedan dentro de un polígono utilizado para la asignación.

---

## 4. Población + paradas

### Pregunta

> Compara los 18 barrios de Donostia según su población femenina en 2025 y el número de paradas del Gautxori. Calcula también cuántas paradas hay por cada 1.000 mujeres. Usa ejecutar_codigo. No inventes datos y explica las limitaciones de este indicador.

### Qué queremos demostrar

Que MATILDA puede integrar el fichero de población con la correspondencia espacial del Gautxori y calcular un indicador relativo.

### Qué debe explicar

El indicador:

```text
paradas / mujeres × 1.000
```

es un indicador descriptivo de oferta espacial programada.

No mide:

- accesibilidad real;
- distancia a pie;
- frecuencia;
- demanda;
- uso;
- ocupación;
- seguridad.

Un valor alto también puede estar condicionado por un número pequeño de mujeres en el denominador.

---

## 5. Población + paradas + horario

### Pregunta

> Para cada uno de los 18 barrios de Donostia, calcula cuántos pasos programados del Gautxori existen y cuántos se producen entre la 01:00 y las 03:59. Compáralos con la población femenina de 2025. Usa ejecutar_codigo.

### Qué queremos demostrar

Que MATILDA puede hacer un análisis espacial y temporal integrado.

### Criterio

Los pasos se obtienen de `stop_times2.txt` y se asignan a barrio mediante `stop_id` y `gautxori_paradas_barrios.csv`.

La franja 01:00–03:59 se define mediante `departure_time`.

Es importante referirse a ellos como **pasos programados en parada** o **registros de paso programados**, no como pasajeros.

---

# 6. Pregunta estrella: análisis conjunto

### Pregunta

> Con los datos disponibles, analiza conjuntamente la población femenina de los barrios, la oferta programada del Gautxori y los registros municipales de seguridad. Identifica patrones descriptivos que puedan ser relevantes para la movilidad nocturna de las mujeres. Distingue claramente entre hechos que muestran los datos, interpretaciones y aspectos que no podemos demostrar. Usa ejecutar_codigo y no inventes información.

### Qué queremos demostrar

Esta es la demostración principal de MATILDA.

Debe integrar:

1. población femenina por barrio;
2. oferta programada del Gautxori;
3. horarios;
4. seguridad municipal.

La respuesta debe mantener la seguridad a escala municipal porque el fichero de seguridad no contiene barrio, calle, parada ni coordenadas.

### Qué debería dejar claro

El análisis sí permite observar diferencias territoriales descriptivas en la oferta programada.

No permite afirmar que:

- un barrio sea seguro o peligroso;
- exista más violencia contra las mujeres en una zona concreta;
- una oferta menor implique peor movilidad;
- el Gautxori reduzca las infracciones;
- exista causalidad entre transporte y seguridad.

---

# 7. Pregunta de siguiente fase

### Pregunta

> Si Puntos Morados y Emakumeen Etxea quisieran estudiar en una siguiente fase si existen zonas con menor accesibilidad al transporte nocturno, ¿qué tres análisis realizarías con los datos actuales y qué datos nuevos solicitarías al Ayuntamiento para poder hacer un análisis espacial y temporal más completo?

### Qué queremos demostrar

Que MATILDA no solo devuelve cifras, sino que puede detectar **qué información falta para avanzar**.

Una respuesta adecuada debería plantear, como mínimo:

### Accesibilidad

Red peatonal, distancias o tiempos de caminata y características de las paradas.

### Cobertura temporal efectiva

Horarios reales, cancelaciones, retrasos, uso y ocupación.

### Seguridad y experiencia

Datos georreferenciados y temporalmente agregados, junto con encuestas o información sobre percepción y experiencia de las mujeres.

---

# 8. Pregunta de control metodológico

### Pregunta

> ¿Qué diferencia hay entre los 5.716 registros de paso del GTFS y los 5.624 registros que aparecen al hacer el análisis por los 18 barrios?

### Respuesta que esperamos

MATILDA debería explicar que:

- **5.716** corresponden al GTFS completo analizado;
- **5.624** corresponden a los registros asociados a paradas que sí pudieron asignarse a alguno de los 18 barrios;
- la diferencia de **92 registros** procede de las **3 paradas que no quedaron dentro de ningún polígono**.

Esta pregunta sirve para demostrar transparencia y trazabilidad.

---

# 9. Pregunta de control sobre los ceros

### Pregunta

> En algunos barrios aparecen 0 paradas Gautxori. ¿Qué significa exactamente ese 0 y qué no podemos concluir a partir de él?

### Respuesta que esperamos

El 0 significa que **no se identificaron paradas dentro del polígono del barrio utilizando la correspondencia espacial disponible**.

No demuestra que:

- las residentes no tengan ninguna alternativa de transporte;
- no exista una parada cercana fuera del límite;
- la accesibilidad sea nula;
- el barrio tenga peor movilidad.

---

# 10. Guion recomendado para la demo

Una presentación fluida puede seguir este orden:

### 1 — ¿Dónde vive la población femenina?

Mostrar el análisis de población de 2025.

### 2 — ¿Cuándo funciona el Gautxori?

Mostrar la distribución por franjas y la concentración entre 01:00 y 03:59.

### 3 — ¿Dónde están las paradas?

Mostrar el análisis espacial por barrios.

### 4 — ¿Cómo se distribuye la oferta respecto a la población?

Mostrar paradas y pasos programados por 1.000 mujeres.

### 5 — ¿Qué sabemos sobre seguridad?

Explicar la evolución municipal de los registros y, sobre todo, la limitación espacial.

### 6 — ¿Qué podemos concluir?

Separar hechos, interpretaciones y límites.

### 7 — ¿Qué haríamos después?

Mostrar los datos que habría que solicitar para estudiar accesibilidad real, uso y seguridad espacial.

---

# 11. Consejos para la demostración

Durante la demo conviene:

- preguntar al agente de forma natural, no solo con preguntas memorizadas;
- pedir al agente que utilice `ejecutar_codigo` en los análisis cuantitativos;
- pedir tablas cuando se comparen barrios;
- pedir explícitamente las limitaciones cuando una pregunta implique seguridad;
- evitar formular preguntas como “¿qué barrio es peligroso?” porque los datos no permiten responderlo con rigor;
- distinguir siempre entre **oferta programada** y **uso real**;
- recordar que `gautxori_paradas_barrios.csv` es un archivo derivado construido a partir de las coordenadas de las paradas y los polígonos de los barrios.

---

# 12. Frase final para cerrar la demo

> **MATILDA.AI no pretende decidir dónde intervenir automáticamente. Su función es convertir datos urbanos dispersos en evidencia descriptiva, hacer visibles las limitaciones y señalar qué preguntas y datos necesitamos para investigar mejor la movilidad nocturna de las mujeres.**
