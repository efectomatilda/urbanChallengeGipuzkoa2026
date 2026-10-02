# Metodología — MATILDA.AI

## 1. Propósito

MATILDA.AI es un agente de análisis urbano centrado en la seguridad y la movilidad nocturna de las mujeres en Donostia-San Sebastián.

La metodología combina cuatro capas de información:

1. población femenina por barrio;
2. delimitación espacial de los barrios;
3. oferta programada del Gautxori mediante datos GTFS;
4. registros municipales agregados de seguridad.

El objetivo no es etiquetar barrios como seguros o peligrosos, sino identificar **patrones descriptivos de población y oferta de movilidad** y señalar qué análisis adicionales serían necesarios para estudiar la accesibilidad y la relación espacial o temporal con la seguridad.

---

## 2. Fuentes de datos

### 2.1. Población femenina de 2025

Archivo:

`poblacion_barrio_2025_2.csv`

Periodo:

**01/01/2025**

La fuente contiene población por municipio y barrio, desagregada por sexo y otros grupos.

Para MATILDA se utiliza la columna `Mujeres`.

Los 18 barrios considerados son:

- Aiete
- Altza
- Amara Berri
- Antiguo
- Ategorrieta-Ulia
- Añorga
- Centro
- Egia
- Gros
- Ibaeta
- Igeldo
- Intxaurrondo
- Landarbaso
- Loiola
- Martutene
- Miracruz-Bidebieta
- Miramon-Zorroaga
- Zubieta

La fila municipal de Donostia / San Sebastián contiene **96.814 mujeres**. La suma de los 18 barrios se utiliza como comprobación de consistencia.

### Lectura del CSV

Los valores de población usan el punto como separador de miles:

- `7.354` = 7.354 personas
- `520` = 520 personas
- `165` = 165 personas

Por este motivo, MATILDA conserva inicialmente los valores como texto y convierte los números eliminando el punto de miles cuando corresponde.

No se filtran nombres de barrio globalmente por todo el fichero, porque nombres como `Centro` pueden repetirse en otros municipios. Primero se localiza la fila municipal de Donostia y después se valida el bloque de sus 18 barrios.

---

## 3. Pirámide demográfica

Archivo:

`demografiapiramideedadbarrio2.csv`

Periodo:

**2019**

Columnas principales:

- `Auzoa`
- `AdinTartea`
- `PertsonenKopG`

`PertsonenKopG` representa la población femenina de esta fuente.

Esta fuente se utiliza para análisis detallados por grupos de edad cuando se solicitan. Sus cifras se presentan siempre como **datos de 2019** y no se mezclan silenciosamente con la población de 2025.

---

## 4. Seguridad municipal

Archivo:

`seguridad_donostia_2025_2026_2.csv`

Periodo:

**enero-junio de 2025 frente a enero-junio de 2026**

La fuente contiene categorías de infracción y valores de Ertzaintza, Policía Local y totales.

Para el total municipal se utiliza la fila:

`TOTAL INFRACCIONES PENALES`

Resultado de referencia:

- enero-junio 2025: **8.832**
- enero-junio 2026: **8.321**
- variación absoluta: **−511**
- variación porcentual: **−5,8 %**

### Restricción espacial

Esta fuente no contiene:

- barrio;
- calle;
- parada;
- coordenadas;
- hora concreta de cada registro.

Por ello, la seguridad se mantiene a **escala municipal**. No se asignan infracciones a barrios o paradas y no se calcula una supuesta peligrosidad territorial.

Tampoco se interpreta el total como una medida completa de la inseguridad de las mujeres, ya que el fichero no es específico de mujeres ni representa necesariamente todos los incidentes o experiencias.

---

## 5. Gautxori / GTFS

Los datos del Gautxori se distribuyen en los archivos:

- `agency2.txt`
- `routes2.txt`
- `trips2.txt`
- `stops2.txt`
- `stop_times2.txt`
- `calendar2.txt`
- `calendar_dates2.txt`
- `shapes2.txt`
- `feed_info2.txt`

Con ellos se pueden estudiar:

- rutas;
- viajes;
- paradas;
- horarios programados;
- franjas horarias;
- pasos programados;
- calendarios y excepciones.

Un punto importante es la diferencia entre **programación** y **uso real**. Los registros GTFS describen la oferta planificada y no equivalen a pasajeros, demanda, ocupación ni percepción de seguridad.

---

## 6. Asignación de paradas a barrios

Para introducir una dimensión espacial en el análisis se utiliza:

`barrios_donostia.json`

Este archivo contiene una `FeatureCollection` con geometrías `Polygon` de los barrios y atributos como `KodAuzo` e `IzenAuzo`.

La asignación espacial sigue este proceso:

```text
stops2.txt
    ↓
coordenadas de cada parada
    ↓
barrios_donostia.json
    ↓
polígono que contiene la coordenada
    ↓
gautxori_paradas_barrios.csv
```

No se utiliza una simple coincidencia textual entre el nombre de la parada y el nombre del barrio.

---

## 7. Archivo derivado `gautxori_paradas_barrios.csv`

`gautxori_paradas_barrios.csv` es un **archivo derivado**, no una fuente original.

Relaciona cada parada del GTFS con el polígono de barrio que contiene sus coordenadas.

Columnas principales:

- `stop_id`: identificador de la parada.
- `stop_name`: nombre de la parada.
- `stop_lat`: latitud.
- `stop_lon`: longitud.
- `codigo_barrio`: código del barrio asignado.
- `barrio`: nombre normalizado del barrio.
- `nombre_geojson`: nombre del barrio tal como aparece en el GeoJSON.
- `asignacion`: estado de la correspondencia espacial.

Los nombres se normalizan para poder cruzar la capa espacial con la población de 2025. Por ejemplo:

- `AMARABERRI` → `Amara Berri`
- `ERDIALDEA` → `Centro`
- `ANTIGUA` → `Antiguo`
- `LANDERBASO` → `Landarbaso`
- `MIRAMON - ZORROAGA` → `Miramon-Zorroaga`
- `ATEGORRIETA - ULIA` → `Ategorrieta-Ulia`
- `MIRAKRUZ - BIDEBIETA` → `Miracruz-Bidebieta`

El GeoJSON también contiene `OARAIN`, pero ese nombre no forma parte de los 18 barrios de la fuente de población 2025. MATILDA no le atribuye población por inferencia.

### Estados de asignación

`DENTRO_POLIGONO`:

la coordenada de la parada queda dentro de un polígono de barrio.

`SIN_ASIGNAR_EN_GEOJSON`:

la coordenada no queda dentro de ningún polígono utilizado para la correspondencia.

Las paradas no asignadas se conservan y **no se fuerzan** a ningún barrio.

En el GTFS analizado hay **248 paradas únicas**. De ellas, **245** quedan dentro de un polígono y **3** no quedan asignadas.

---

## 8. Cálculo de indicadores por barrio

Cuando el usuario solicita comparar población femenina y Gautxori por barrio, MATILDA sigue este flujo:

### Paso 1 — Población

Obtiene las 18 filas de población femenina de 2025 y valida que corresponden al bloque de Donostia.

### Paso 2 — Paradas

Utiliza `gautxori_paradas_barrios.csv` y conserva las filas con:

`asignacion == DENTRO_POLIGONO`

Después cuenta `stop_id` únicos por barrio.

### Paso 3 — Pasos programados

Relaciona `stop_times2.txt` con el mapeo de paradas mediante `stop_id`.

Cada registro de `stop_times2.txt` representa un **paso programado de un viaje por una parada**.

Por tanto, una métrica de pasos no equivale a una métrica de pasajeros ni a una frecuencia comercial única.

### Paso 4 — Franjas horarias

Cuando se solicita una franja, se utiliza `departure_time`.

Para el análisis de madrugada:

**01:00–03:59**

se incluyen las horas 01, 02 y 03.

### Paso 5 — Cruce

Se realiza un `LEFT JOIN` desde los 18 barrios de población para conservar todos los barrios.

Si un barrio no tiene paradas asignadas, la métrica de paradas queda en **0**.

---

## 9. Indicadores utilizados

### Paradas por 1.000 mujeres

```text
paradas del Gautxori / mujeres del barrio × 1.000
```

Este indicador describe la cantidad de paradas asignadas espacialmente al barrio en relación con su población femenina.

### Pasos programados por 1.000 mujeres

```text
pasos programados / mujeres del barrio × 1.000
```

Describe la intensidad de los registros de paso programados en las paradas del barrio respecto a la población femenina.

Estos indicadores **no miden accesibilidad real**. No incorporan distancia a pie, tiempo de acceso, frecuencia percibida, demanda, ocupación, uso real ni características del recorrido.

---

## 10. Diferencia entre 5.716 y 5.624 registros

En los análisis generales del GTFS se han contabilizado:

**5.716 registros de `stop_times2.txt`**

Cuando el análisis se limita a los 18 barrios y solo incluye las paradas con `DENTRO_POLIGONO`, quedan:

**5.624 registros**

La diferencia es:

**92 registros**, asociados a las **3 paradas que no pudieron asignarse a un polígono de barrio**.

Por tanto, las dos cifras responden a universos distintos:

- **5.716** → GTFS completo analizado.
- **5.624** → registros que pueden atribuirse espacialmente a los 18 barrios mediante la correspondencia disponible.

---

## 11. Análisis conjunto

MATILDA puede combinar:

1. población femenina de 2025 por barrio;
2. paradas Gautxori por barrio;
3. pasos programados por barrio y franja;
4. contexto municipal de seguridad.

La integración se realiza únicamente cuando existe una correspondencia de datos real.

Por ejemplo, sí es válido comparar:

> población femenina de un barrio ↔ número de paradas asignadas a ese barrio ↔ pasos programados en esas paradas.

Pero no es válido afirmar:

> barrio ↔ número de delitos

cuando el fichero de seguridad no contiene una clave territorial.

---

## 12. Hecho, interpretación y límite

Las respuestas de MATILDA procuran separar tres niveles:

### Hecho

Una cifra o patrón que puede obtenerse directamente mediante el cálculo sobre los archivos.

### Interpretación

Una lectura descriptiva del patrón observado.

### Límite

Una explicación de aquello que los datos no permiten concluir.

Ejemplo:

**Hecho:** un barrio presenta menos pasos programados por 1.000 mujeres que otro.

**Interpretación:** existe una diferencia descriptiva en la oferta programada relativa.

**Límite:** esto no demuestra que sus residentes tengan peor movilidad ni menor seguridad.

---

## 13. Principios de calidad

MATILDA sigue estas reglas:

- calcular sobre los registros pertinentes;
- revisar columnas, tipos y claves antes de hacer cruces;
- comprobar denominadores antes de calcular porcentajes;
- distinguir cero de dato ausente;
- no mezclar años sin indicarlo;
- no duplicar categorías de seguridad solapadas;
- no inventar correspondencias espaciales;
- no convertir correlación o coincidencia en causalidad;
- utilizar la ejecución verificable más reciente ante resultados contradictorios;
- presentar las limitaciones relevantes junto al resultado.

---

## 14. Próxima evolución metodológica

Los datos actuales permiten estudiar **diferencias descriptivas en la oferta programada**.

Para medir accesibilidad real sería necesario incorporar, entre otros:

- red peatonal;
- distancias o tiempos de caminata;
- características y accesibilidad física de las paradas;
- servicio efectivamente realizado;
- cancelaciones y retrasos;
- uso del Gautxori por parada y franja;
- seguridad georreferenciada y temporalmente agregada;
- percepción y experiencia de las mujeres.

La siguiente fase debería distinguir entre:

**accesibilidad potencial → oferta efectiva → uso → seguridad registrada → percepción y experiencia.**
