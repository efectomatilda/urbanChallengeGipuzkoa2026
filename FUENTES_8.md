# FUENTES_8.md — MATILDA.AI

## 1. Proyecto

**Nota técnica:** `barrios_donostia.json` es un archivo JSON cuyo contenido es una GeoJSON `FeatureCollection` con geometrías de tipo `Polygon`; la extensión `.json` no cambia el contenido geográfico.


**Nombre:** MATILDA.AI — Seguridad y movilidad nocturna de las mujeres  
**Territorio:** Donostia-San Sebastián, Gipuzkoa  
**Usuarios objetivo:** Puntos Morados y Emakumeen Etxea

Pregunta de investigación actualizada:

> ¿Qué patrones existen entre la distribución de la población femenina, la oferta programada de transporte nocturno Gautxori y los registros municipales de seguridad en Donostia-San Sebastián, y dónde se observan posibles diferencias de cobertura que requieran una investigación más detallada?

Problema urbano que se estudia:

> Comprender cómo se distribuye la oferta programada de movilidad nocturna respecto a la población femenina de Donostia-San Sebastián y detectar posibles diferencias territoriales de cobertura que puedan orientar futuras investigaciones y actuaciones.

La herramienta no decide automáticamente dónde actuar ni determina qué barrio es seguro o peligroso.

## 2. Población femenina 2025

Archivo:

`poblacion_barrio_2025_2.csv`

Fuente indicada en el propio archivo:

“Población de la C.A. de Euskadi por barrios de los municipios de más de 10.000 habitantes,
según sexo, grupos de edad y nacionalidad. 01/01/2025”

Formato:
- CSV delimitado por `;`
- contiene una línea inicial de título y dos niveles de encabezado en dos niveles.

Columnas operativas:
- nombre del municipio o barrio
- `Total`
- `Hombres`
- `Mujeres`
- `Sex ratio`
- `0-19`
- `20-64`
- `>=65`
- `UE-27`
- `Resto`

Donostia / San Sebastián:
- población total municipal: 183.388
- mujeres: 96.814
- barrios incluidos en la fuente: 18

Los 18 barrios son:
Aiete, Altza, Amara Berri, Antiguo, Ategorrieta-Ulia, Añorga, Centro, Egia, Gros,
Ibaeta, Igeldo, Intxaurrondo, Landarbaso, Loiola, Martutene, Miracruz-Bidebieta,
Miramon-Zorroaga y Zubieta.

Regla:
Para análisis de población femenina por barrio en 2025, utilizar la columna `Mujeres`.
No mezclar filas de otros municipios. Validar la lista de barrios y, cuando proceda,
comprobar coherencia con la fila municipal.

## 3. Pirámide demográfica

Archivo:

`demografiapiramideedadbarrio2.csv`

Periodo:
2019

Columnas principales:
- `Auzoa`
- `AdinTartea`
- `PertsonenKopG`

`PertsonenKopG` representa la población femenina de la fuente para cada barrio y grupo de edad.

Regla:
Utilizar esta fuente para el detalle por grupos de edad, dejando siempre claro que es de 2019.
No presentar sus cifras como población femenina actual de 2025.

## 4. Seguridad

Archivo:

`seguridad_donostia_2025_2026_2.csv`

Cobertura:
- Donostia-San Sebastián
- enero-junio de 2025
- enero-junio de 2026

La fuente contiene categorías de infracción y valores de Ertzaintza, Policía Local y totales.

No contiene en esta versión:
- barrio
- calle
- parada
- coordenadas
- hora concreta de cada registro

Por tanto:
- no localizar infracciones por barrio o parada;
- no calcular peligrosidad por barrio;
- no atribuir las cifras a mujeres;
- no interpretar el total municipal como una medida completa de inseguridad.

## 5. Gautxori / GTFS

Archivos:
- `agency2.txt`
- `routes2.txt`
- `trips2.txt`
- `stops2.txt`
- `stop_times2.txt`
- `calendar2.txt`
- `calendar_dates2.txt`
- `shapes2.txt`
- `feed_info2.txt`

Se pueden analizar:
- rutas
- viajes
- servicios
- paradas
- horarios programados
- franjas horarias
- pasos programados
- días y excepciones de servicio

No equivale a:
- uso real
- ocupación
- demanda
- percepción de seguridad
- iluminación
- accesibilidad percibida

## 6. Delimitación espacial de barrios

Archivo fuente:

`barrios_donostia.json`

El archivo es un GeoJSON con una `FeatureCollection` llamada `Auzoak` y geometrías `Polygon`.
Sus atributos incluyen `KodAuzo` e `IzenAuzo`.

Se utiliza para asignar espacialmente cada parada del GTFS a un barrio mediante sus coordenadas.

## 7. Correspondencia de paradas con barrios

Archivo derivado para uso operativo del agente:

`gautxori_paradas_barrios.csv`

Este archivo relaciona cada `stop_id` del GTFS con su barrio mediante el polígono oficial
contenido en `barrios_donostia.json`.

Columnas principales:
- `stop_id`
- `stop_name`
- `stop_lat`
- `stop_lon`
- `codigo_barrio`
- `barrio`
- `nombre_geojson`
- `asignacion`

La correspondencia normaliza nombres del GeoJSON a los nombres utilizados por la fuente
de población 2025, por ejemplo:
- `AMARABERRI` → `Amara Berri`
- `ERDIALDEA` → `Centro`
- `ANTIGUA` → `Antiguo`
- `LANDERBASO` → `Landarbaso`
- `MIRAMON - ZORROAGA` → `Miramon-Zorroaga`
- `ATEGORRIETA - ULIA` → `Ategorrieta-Ulia`
- `MIRAKRUZ - BIDEBIETA` → `Miracruz-Bidebieta`

`OARAIN` aparece en el GeoJSON pero no está entre los 18 barrios de la fuente de población 2025.
No debe recibir población femenina inventada ni debe forzarse su equivalencia con otro barrio.

En la correspondencia preparada sobre el GTFS actual hay paradas que no quedan dentro de ningún
polígono de barrio del GeoJSON. Deben conservarse como `SIN_ASIGNAR_EN_GEOJSON` y excluirse de
comparaciones por barrio, sin inventar una asignación.

## 8. Indicadores de movilidad por barrio

A partir de `gautxori_paradas_barrios.csv` + `stop_times2.txt` + `trips2.txt` + `routes2.txt`,
MATILDA puede calcular:

### Indicador 1 — Paradas Gautxori por barrio

Número de `stop_id` únicos asignados a cada barrio.

### Indicador 2 — Pasos programados por barrio

Número de registros de `stop_times2.txt` asociados a paradas de cada barrio.
Cada registro representa una visita/paso programado del servicio por una parada en un viaje.
No debe presentarse como pasajeros ni como demanda real.

### Indicador 3 — Pasos programados nocturnos por barrio

Mismo cálculo restringido a una franja indicada por el usuario, por ejemplo 01:00–03:59.

### Indicador 4 — Rutas con servicio por barrio

Número de rutas únicas que tienen viajes que realizan paradas dentro del barrio.

### Indicador 5 — Oferta relativa a población femenina

Ejemplos descriptivos:
- paradas por 1.000 mujeres;
- pasos programados por 1.000 mujeres.

Fórmula general:

`indicador relativo = indicador de oferta del barrio / mujeres del barrio * 1000`

Estos indicadores describen oferta programada y densidad relativa. No demuestran calidad del
servicio, demanda, accesibilidad real ni seguridad.

## 9. Análisis conjunto

Puede combinarse, respetando los periodos y unidades:

- población femenina 2025 por barrio;
- paradas Gautxori por barrio;
- pasos programados por barrio y franja horaria;
- rutas que sirven cada barrio;
- seguridad municipal enero-junio 2025 vs enero-junio 2026.

El análisis espacial de seguridad por barrio no es posible con el fichero actual de seguridad
porque carece de localización.

## 10. Interpretación correcta

Puede decirse:
- “este barrio concentra X mujeres y tiene Y paradas del Gautxori”;
- “este barrio registra Z pasos programados en la franja indicada”;
- “la oferta programada por 1.000 mujeres es mayor/menor según el indicador calculado”;
- “se observa una diferencia territorial de oferta que merece una investigación adicional”.

No debe decirse sin datos adicionales:
- “este barrio es peligroso”;
- “aquí hay más violencia contra las mujeres”;
- “el Gautxori no cubre suficientemente a las mujeres” como conclusión causal;
- “hay que poner una parada aquí” como decisión automática.

## 11. Indicadores base ya validados

### Población femenina 2025

Los 18 barrios de Donostia suman 96.814 mujeres, coherente con la fila municipal.

### Seguridad

La fila `TOTAL INFRACCIONES PENALES` pasa de 8.832 en enero-junio 2025 a 8.321 en enero-junio 2026:
- cambio absoluto: -511
- cambio porcentual: -5,79 %

No sumar categorías generales y subcategorías solapadas para obtener un total alternativo.

### Gautxori

El GTFS contiene 14 definiciones de ruta; 8 tienen viajes asociados y hay 303 viajes.
`stop_times2.txt` contiene 5.716 registros de parada-viaje.
La oferta programada observada se concentra especialmente entre las 01:00 y las 03:59.

## 12. Calidad y transparencia

- Calcular sobre todos los registros pertinentes.
- Comprobar columnas, tipos, nulos y duplicados cuando sea relevante.
- Comprobar denominadores antes de porcentajes.
- Distinguir dato cero de dato ausente.
- Revisar claves antes de merges.
- No usar cifras recordadas de mensajes anteriores si una nueva ejecución puede verificarlas.
- Ante resultados contradictorios, confiar en la ejecución verificable más reciente, explicar la discrepancia y no mezclar ambas cifras.
- Distinguir siempre hecho, interpretación e hipótesis.
- No convertir correlaciones o coincidencias en causalidad.
- No inventar barrios, rutas, paradas, horarios, población ni seguridad.

## 13. Regla crítica de lectura del CSV 2025

Los valores deben conservarse como texto antes de convertirlos. `7.354` representa 7354; `520` representa 520; `165` representa 165.
No interpretar `520.000` o `165.000` como valores de población reales si solo son una representación decimal generada por pandas.
