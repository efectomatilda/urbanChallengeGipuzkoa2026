# Datos de MATILDA.AI

Esta carpeta reúne los datos utilizados por **MATILDA.AI** para analizar la población femenina, la oferta programada del transporte nocturno Gautxori y el contexto municipal de seguridad en **Donostia-San Sebastián**.

La documentación distingue entre:

- **fuentes originales**: archivos procedentes de las fuentes de datos utilizadas por el proyecto;
- **archivo derivado**: `gautxori_paradas_barrios.csv`, generado para relacionar espacialmente las paradas del Gautxori con los barrios.

> **Nota de reproducibilidad:** los archivos se mantienen con sus nombres originales de trabajo para que coincidan con los nombres que utiliza el agente en `agente/main.py`.

---

## 1. Resumen de los conjuntos de datos

| Archivo | Tipo | Cobertura | Uso en MATILDA.AI |
|---|---|---|---|
| `poblacion_barrio_2025_2.csv` | CSV | Donostia, 01/01/2025 | Población total y femenina por barrio |
| `demografiapiramideedadbarrio2.csv` | CSV | 2019 · 7 barrios | Detalle de población femenina por grupos de edad |
| `seguridad_donostia_2025_2026_2.csv` | CSV | Donostia · ene–jun 2025 y ene–jun 2026 | Evolución agregada de infracciones |
| `barrios_donostia.json` | GeoJSON | Barrios de Donostia | Límites espaciales de los barrios |
| `agency2.txt` | GTFS | Gautxori | Información de la agencia |
| `routes2.txt` | GTFS | Gautxori | Definición de rutas |
| `trips2.txt` | GTFS | Gautxori | Viajes programados |
| `stops2.txt` | GTFS | Gautxori | Paradas y coordenadas |
| `stop_times2.txt` | GTFS | Gautxori | Horarios y pasos programados |
| `calendar2.txt` | GTFS | Gautxori | Calendario de servicios |
| `calendar_dates2.txt` | GTFS | Gautxori | Excepciones al calendario |
| `shapes2.txt` | GTFS | Gautxori | Geometrías de los recorridos |
| `feed_info2.txt` | GTFS | Gautxori | Metadatos del feed |
| `gautxori_paradas_barrios.csv` | CSV derivado | Donostia · paradas del GTFS | Correspondencia parada → barrio |

---

# 2. Población femenina por barrio · 2025

### `poblacion_barrio_2025_2.csv`

Fuente utilizada para el análisis demográfico actual de MATILDA.AI.

La fuente corresponde a la **población de Euskadi por barrios de municipios de más de 10.000 habitantes según sexo, grupos de edad y nacionalidad, a 01/01/2025**.

Para Donostia se utiliza la columna `Mujeres` y se trabaja con los **18 barrios** incluidos en el bloque de Donostia / San Sebastián:

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

### Lectura del archivo

El CSV utiliza `;` como separador y presenta encabezados de varias líneas. Los valores de población utilizan el punto como separador de miles:

```text
7.354  →  7.354 personas
520    →  520 personas
165    →  165 personas
```

En el análisis se conserva primero el valor como texto y se convierte posteriormente a número retirando el separador de miles cuando corresponde.

La suma de las mujeres de los 18 barrios debe ser coherente con la fila municipal de Donostia: **96.814 mujeres**.

### Qué permite analizar

- población femenina por barrio;
- concentración de mujeres dentro de Donostia;
- comparación descriptiva con la distribución de paradas y pasos programados del Gautxori;
- indicadores como mujeres por barrio y pasos/paradas por cada 1.000 mujeres.

### Qué no permite afirmar por sí sola

La población residente no informa sobre desplazamientos nocturnos reales, uso del transporte ni necesidad de servicio.

---

# 3. Pirámide demográfica · 2019

### `demografiapiramideedadbarrio2.csv`

Esta fuente contiene **140 registros** para **7 barrios** y utiliza las columnas principales:

- `Auzoa` — barrio;
- `AdinTartea` — grupo de edad;
- `PertsonenKopG` — población femenina de la fuente.

Los barrios presentes son:

- Amara Berri
- Altza
- Antiguo
- Ibaeta
- Ategorrieta-Ulia
- Añorga
- Igeldo

### Regla de interpretación

Esta fuente es de **2019**. Sus grupos de edad no deben presentarse como si fueran la estructura de edad actual de 2025.

Se utiliza principalmente cuando MATILDA necesita estudiar la distribución de la población femenina por grupos de edad y barrio.

---

# 4. Seguridad municipal · 2025–2026

### `seguridad_donostia_2025_2026_2.csv`

Fuente agregada para **Donostia-San Sebastián**, con comparación entre:

- enero–junio de 2025;
- enero–junio de 2026.

Las columnas principales incluyen:

- `periodo`;
- `municipio`;
- `tipo_infraccion`;
- valores de Ertzaintza;
- valores de Policía Local;
- `total_2025`;
- `total_2026`.

### Uso en MATILDA.AI

Se utiliza para calcular, entre otros indicadores:

```text
variación porcentual =
(total_2026 - total_2025) / total_2025 × 100
```

Por ejemplo, la fila `TOTAL INFRACCIONES PENALES` permite comparar el volumen agregado entre ambos periodos.

### Limitación espacial y de interpretación

Este archivo **no contiene barrio, calle, parada, coordenadas ni hora individual de cada registro**.

Por tanto, MATILDA.AI no utiliza este conjunto para:

- asignar infracciones a barrios;
- identificar una parada como más insegura;
- construir un mapa de delitos por zona;
- calcular una supuesta “peligrosidad” de un barrio;
- atribuir todas las infracciones a mujeres;
- establecer una relación causal entre transporte y seguridad.

Los registros representan **incidencias registradas**, no una medida completa de la inseguridad percibida o experimentada.

---

# 5. Gautxori · GTFS

Los archivos GTFS forman el núcleo de los análisis de transporte nocturno.

## `agency2.txt`

Contiene la información de la agencia operadora incluida en el feed GTFS.

## `routes2.txt`

Define las rutas del Gautxori disponibles en el feed.

Se utiliza para estudiar:

- identificadores de ruta;
- nombres de las rutas;
- información asociada a cada servicio.

## `trips2.txt`

Contiene los **viajes programados** asociados a las rutas y servicios del GTFS.

Se utiliza para identificar los viajes que generan los registros de `stop_times2.txt`.

## `stops2.txt`

Contiene las **paradas** y sus coordenadas geográficas, principalmente mediante:

- `stop_id`;
- `stop_name`;
- `stop_lat`;
- `stop_lon`.

Este archivo es la base espacial para localizar las paradas.

## `stop_times2.txt`

Relaciona cada viaje con sus paradas y horarios programados.

Se utiliza para analizar:

- hora de llegada/salida programada;
- secuencia de paradas;
- pasos programados;
- distribución horaria de la oferta.

En MATILDA.AI, un registro de `stop_times` se interpreta como un **paso programado por una parada**, no como una persona usuaria.

## `calendar2.txt`

Define los calendarios de servicio asociados a los viajes.

## `calendar_dates2.txt`

Contiene excepciones al calendario, como altas o bajas de servicios en fechas determinadas.

## `shapes2.txt`

Contiene la geometría de los recorridos del feed GTFS.

## `feed_info2.txt`

Contiene metadatos generales del feed.

### Qué permite analizar el GTFS

- rutas programadas;
- viajes programados;
- paradas;
- horarios;
- pasos programados por parada;
- franjas horarias;
- relación entre rutas, viajes y paradas;
- días y excepciones de servicio.

### Qué no permite medir por sí solo

- uso real;
- número de pasajeros;
- ocupación;
- demanda;
- retrasos reales;
- cancelaciones reales;
- percepción de seguridad;
- accesibilidad peatonal;
- iluminación o calidad del entorno.

---

# 6. Delimitación espacial de los barrios

### `barrios_donostia.json`

Es el archivo **GeoJSON** utilizado para incorporar una dimensión espacial al proyecto.

Contiene una `FeatureCollection` con geometrías de tipo `Polygon` y atributos de identificación de los barrios.

Su función es proporcionar los **límites geográficos** necesarios para comprobar si las coordenadas de una parada de `stops2.txt` se encuentran dentro de un determinado barrio.

### Importante

La geometría del barrio se utiliza únicamente para hacer una **asignación espacial de la parada**. Que una parada esté dentro de un polígono no significa que ese barrio concentre la demanda ni que todas las personas residentes tengan ese nivel de acceso al servicio.

Los nombres del GeoJSON se normalizan cuando es necesario para hacerlos compatibles con los nombres utilizados en la fuente de población 2025.

Las entidades del GeoJSON que no tienen correspondencia clara con los 18 barrios de la fuente de población no reciben población inventada ni se fuerzan a otro barrio.

---

# 7. Archivo derivado: `gautxori_paradas_barrios.csv`

Este archivo es **resultado de un procesamiento realizado para MATILDA.AI**. No es una nueva fuente externa.

Se obtiene combinando:

```text
stops2.txt
    │
    │  coordenadas de las paradas
    ▼
barrios_donostia.json
    │
    │  comprobación espacial punto → polígono
    ▼
gautxori_paradas_barrios.csv
```

Su objetivo es evitar que el agente tenga que repetir esta correspondencia espacial en cada consulta y, al mismo tiempo, dejar documentado cómo se realizó.

## Columnas principales

| Columna | Significado |
|---|---|
| `stop_id` | Identificador de la parada del GTFS |
| `stop_code` | Código de parada, cuando está disponible |
| `stop_name` | Nombre de la parada |
| `stop_lat` | Latitud de la parada |
| `stop_lon` | Longitud de la parada |
| `codigo_barrio` | Código del barrio asignado |
| `barrio` | Nombre normalizado usado por el proyecto |
| `nombre_geojson` | Nombre del barrio tal como aparece en el GeoJSON |
| `asignacion` | Resultado de la comprobación espacial |

## Valores de `asignacion`

### `DENTRO_POLIGONO`

La coordenada de la parada queda dentro de uno de los polígonos de barrios utilizados.

Estas son las paradas que se utilizan para las comparaciones territoriales por barrio.

### `SIN_ASIGNAR_EN_GEOJSON`

La parada no queda dentro de ningún polígono de los barrios disponibles o no puede asignarse de forma inequívoca.

Estas filas **se conservan** en el archivo para no perder información, pero no se fuerzan artificialmente a un barrio.

## Resultado de la correspondencia

En el GTFS analizado hay **248 paradas únicas**. La correspondencia preparada identifica **245 paradas dentro de los polígonos de los barrios** y mantiene **3 paradas sin asignación espacial**.

Por este motivo, cuando se hace un análisis exclusivamente “por barrios”, los registros correspondientes a las paradas sin asignar se mantienen fuera de la comparación territorial.

---

# 8. Cómo se utiliza `gautxori_paradas_barrios.csv`

El archivo permite construir análisis como:

```text
Barrio
  ↓
población femenina 2025
  ↓
paradas Gautxori
  ↓
pasos programados
  ↓
pasos en franjas de madrugada
  ↓
indicadores descriptivos por 1.000 mujeres
```

Por ejemplo, MATILDA puede calcular:

### Paradas por barrio

```text
número de stop_id únicos asignados al barrio
```

### Pasos programados por barrio

```text
número de registros de stop_times asociados a las paradas del barrio
```

### Pasos programados entre 01:00 y 03:59

```text
registros de stop_times cuyo departure_time
se encuentra entre 01:00 y 03:59
```

### Indicador descriptivo

```text
pasos programados / mujeres × 1.000
```

Este indicador debe interpretarse únicamente como una **relación descriptiva entre oferta programada y población femenina residente**.

No significa que 1.000 mujeres reciban o utilicen esa cantidad de servicios.

---

# 9. Qué significa “cobertura” en MATILDA

En la versión actual, cuando MATILDA habla de diferencias de “cobertura” se refiere a una **aproximación territorial a la oferta programada**.

Todavía no se mide la accesibilidad real de una persona.

Para medir accesibilidad real harían falta datos adicionales, por ejemplo:

- red peatonal;
- distancias o tiempos caminando hasta las paradas;
- pendientes y barreras;
- características de accesibilidad de las paradas;
- servicio efectivamente realizado;
- uso o demanda;
- iluminación y condiciones del entorno.

Por ello, un valor bajo de pasos por 1.000 mujeres **no demuestra por sí mismo una mala movilidad**, y un valor alto no demuestra una buena accesibilidad.

---

# 10. Principios de uso de los datos

MATILDA.AI aplica estas reglas al analizar esta carpeta:

1. **No inventar datos.** Si una variable no existe, se explica.
2. **Mantener los periodos explícitos.** 2019, 2025 y 2026 no se mezclan silenciosamente.
3. **Separar oferta de uso.** El GTFS describe programación, no pasajeros.
4. **Separar seguridad registrada de seguridad percibida.**
5. **No convertir una coincidencia en causalidad.**
6. **No etiquetar barrios como seguros o peligrosos** a partir de estos archivos.
7. **No forzar asignaciones espaciales.** Las paradas sin correspondencia se conservan como sin asignar.
8. **Comprobar denominadores y unidades** antes de calcular porcentajes o ratios.
9. **Documentar las transformaciones.** Los archivos derivados deben poder rastrearse hasta sus fuentes.

---

# 11. Relación entre los datos y el problema urbano

La finalidad de esta carpeta no es construir una clasificación de barrios.

Los datos permiten estudiar, de forma progresiva:

```text
¿Dónde vive la población femenina?
            ↓
¿Qué paradas Gautxori existen en cada zona?
            ↓
¿Cuántos pasos están programados y en qué franjas?
            ↓
¿Hay diferencias descriptivas de oferta entre barrios?
            ↓
¿Qué datos necesitamos para medir accesibilidad real?
```

Los registros de seguridad aportan **contexto municipal**, pero la versión actual no permite cruzarlos espacialmente con las paradas o los barrios.

La siguiente fase del proyecto podría incorporar datos de red peatonal, servicio efectivo, uso del transporte, seguridad georreferenciada y experiencia de las usuarias.

---

## Resumen

**Fuentes originales:**

- población femenina 2025;
- pirámide demográfica 2019;
- seguridad municipal 2025–2026;
- feed GTFS del Gautxori;
- límites de barrios en GeoJSON.

**Archivo derivado:**

- `gautxori_paradas_barrios.csv` → correspondencia espacial entre las paradas del GTFS y los polígonos de barrios.

El conjunto de datos permite a MATILDA.AI pasar de un análisis municipal general a un **análisis descriptivo territorial de la oferta programada de movilidad nocturna**, manteniendo explícitas las limitaciones de lo que los datos pueden demostrar.
