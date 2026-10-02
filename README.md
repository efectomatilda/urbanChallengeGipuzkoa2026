# MATILDA.AI

## Seguridad y movilidad nocturna de las mujeres en Donostia-San Sebastián

> **Una guía de análisis urbano para preguntar, comparar y comprobar.**

MATILDA.AI es un agente de análisis urbano creado para estudiar la movilidad nocturna y su relación contextual con la población femenina y los registros municipales de seguridad en **Donostia-San Sebastián**.

Su objetivo no es etiquetar barrios como seguros o peligrosos ni tomar decisiones automáticamente. MATILDA.AI transforma datos urbanos en **preguntas investigables**, combina fuentes heterogéneas y hace explícitas sus limitaciones para ayudar a **Puntos Morados y Emakumeen Etxea** a orientar futuras investigaciones sobre accesibilidad y movilidad nocturna.

---

## 01 · El problema urbano

La movilidad nocturna no depende de un único dato. Para comprenderla mejor hay que observar, al menos, tres dimensiones:

- **Dónde vive la población femenina.**
- **Cómo se distribuye la oferta programada de transporte nocturno.**
- **Qué muestran los registros municipales de seguridad y qué no permiten demostrar.**

MATILDA.AI integra estas dimensiones y, a partir de la versión actual del proyecto, añade una capa espacial que permite asociar las paradas del Gautxori a los barrios mediante sus coordenadas y los polígonos oficiales disponibles.

La pregunta de investigación actual es:

> **¿Qué patrones existen entre la distribución de la población femenina, la oferta programada de transporte nocturno Gautxori y los registros municipales de seguridad en Donostia-San Sebastián, y dónde se observan posibles diferencias de cobertura que requieran una investigación más detallada?**

---

## 02 · Qué hace MATILDA.AI

El agente puede:

1. Analizar la población femenina por barrio.
2. Analizar rutas, viajes, paradas y horarios programados del Gautxori mediante GTFS.
3. Asociar espacialmente las paradas a barrios.
4. Calcular pasos programados por barrio y por franja horaria.
5. Comparar la oferta programada con la población femenina mediante indicadores descriptivos.
6. Contextualizar estos resultados con los registros municipales agregados de seguridad.
7. Separar de forma explícita **hechos, interpretaciones y límites**.
8. Proponer qué datos adicionales serían necesarios para una siguiente fase de análisis urbano.

---

## 03 · Arquitectura del proyecto

```text
MATILDA-AI/
│
├── agente/
│   ├── main.py
│   ├── tools.py
│   ├── FUENTES_8.md
│   └── INSTRUCCIONES_V11_JSON.md
│
├── datos/
│   ├── población femenina 2025
│   ├── población por edades 2019
│   ├── seguridad municipal 2025–2026
│   ├── GTFS Gautxori
│   ├── barrios_donostia.json
│   └── gautxori_paradas_barrios.csv
│
├── web/
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│   └── assets/
│       └── matilda.png
│
├── branding/
├── docs/
└── capturas/
```

`main.py` contiene el comportamiento del agente. `tools.py` corresponde a la herramienta de ejecución proporcionada por la plataforma y se utiliza para ejecutar análisis reproducibles con Python.

---

# 04 · Fuentes de datos

La carpeta `datos/` contiene las fuentes utilizadas por el proyecto y los archivos derivados necesarios para el análisis espacial.

## 4.1 Población femenina por barrios · 2025

**Archivo:** `poblacion_barrio_2025_2.csv`

Fuente estadística utilizada para la población de 2025 por barrio.

La fuente corresponde a la población de Euskadi por barrios de municipios de más de 10.000 habitantes, según sexo, grupos de edad y nacionalidad, con fecha **01/01/2025**.

Para MATILDA.AI, la magnitud principal es la columna **`Mujeres`**.

En el bloque de Donostia aparecen los 18 barrios utilizados en el análisis:

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

La fila municipal de Donostia indica **96.814 mujeres**.

### Regla de lectura

Los valores de población conservan el formato de miles del fichero original: por ejemplo, `7.354` representa **7.354 mujeres**, mientras que `520` representa **520**.

MATILDA.AI valida que los 18 barrios del bloque de Donostia sumen la población femenina municipal utilizada como referencia.

---

## 4.2 Estructura demográfica por edades · 2019

**Archivo:** `demografiapiramideedadbarrio2.csv`

Fuente utilizada para análisis detallados por **grupo de edad y barrio**.

Características relevantes:

- Año: **2019**.
- 140 registros.
- 7 barrios.
- Variable de población femenina: **`PertsonenKopG`**.
- Barrio: **`Auzoa`**.
- Grupo de edad: **`AdinTartea`**.

Esta fuente se mantiene separada de la población de 2025: sus cifras de edad **no deben presentarse como población femenina actual de 2025**.

---

## 4.3 Registros municipales de seguridad · 2025–2026

**Archivo:** `seguridad_donostia_2025_2026_2.csv`

Cobertura:

- Donostia-San Sebastián.
- Enero–junio de 2025.
- Enero–junio de 2026.

Variables principales:

- `periodo`
- `municipio`
- `tipo_infraccion`
- valores de Ertzaintza
- valores de Policía Local
- `total_2025`
- `total_2026`

La fila **`TOTAL INFRACCIONES PENALES`** registra:

| Periodo | Total |
|---|---:|
| Enero–junio 2025 | 8.832 |
| Enero–junio 2026 | 8.321 |

Variación observada: **−511 registros**, aproximadamente **−5,8 %**.

### Limitación espacial

El fichero actual **no contiene barrio, calle, parada, coordenadas ni hora concreta de cada registro**.

Por ello, MATILDA.AI no utiliza esta fuente para calcular peligrosidad por barrio ni para afirmar que una determinada zona sea más o menos segura. Los registros de seguridad se utilizan como **contexto municipal agregado**.

---

# 05 · Datos GTFS del Gautxori

La oferta programada del Gautxori se encuentra desglosada en los archivos GTFS:

```text
agency2.txt
routes2.txt
trips2.txt
stops2.txt
stop_times2.txt
calendar2.txt
calendar_dates2.txt
shapes2.txt
feed_info2.txt
```

En conjunto permiten analizar:

- agencia y metadatos del servicio;
- rutas;
- viajes programados;
- paradas;
- tiempos de llegada y salida programados;
- calendario de servicio;
- excepciones de calendario;
- geometrías de las rutas;
- información del feed.

### Qué significa “oferta programada”

El GTFS describe **cómo está planificado el servicio**, no cómo se utilizó realmente.

Por tanto, estos datos no equivalen a:

- pasajeros;
- demanda;
- ocupación;
- retrasos reales;
- cancelaciones reales;
- percepción de seguridad;
- accesibilidad peatonal;
- iluminación o calidad del entorno.

En el análisis base validado se identificaron **14 rutas definidas**, **8 rutas con viajes asociados** y **303 viajes programados**.

El archivo `stop_times2.txt` contiene **5.716 registros de paso programados** asociados a esos viajes. La distribución horaria observada se concentra especialmente entre la 01:00 y las 03:59.

---

# 06 · Delimitación oficial de los barrios

**Archivo:** `barrios_donostia.json`

Este archivo contiene una `FeatureCollection` GeoJSON denominada **`Auzoak`** con geometrías de tipo **`Polygon`**.

Sus atributos incluyen, entre otros:

- `KodAuzo`
- `IzenAuzo`

El archivo se utiliza como referencia espacial para determinar en qué polígono de barrio cae cada parada del Gautxori.

### Por qué es necesario

El GTFS proporciona las coordenadas de las paradas, pero no asigna por sí mismo cada parada a uno de los 18 barrios de la fuente de población.

El GeoJSON permite realizar esa asociación mediante una operación espacial de **punto dentro de polígono**.

---

# 07 · Archivo derivado: `gautxori_paradas_barrios.csv`

Este archivo es una pieza clave de la versión actual de MATILDA.AI.

**No es una fuente original:** es un **archivo derivado** generado a partir de:

```text
stops2.txt
      +
barrios_donostia.json
      ↓
 gautxori_paradas_barrios.csv
```

Su función es dejar preparada una correspondencia reproducible entre cada parada del Gautxori y el barrio correspondiente, cuando la coordenada de la parada cae dentro de un polígono.

## 7.1 Columnas

| Columna | Descripción |
|---|---|
| `stop_id` | Identificador de la parada en el GTFS. |
| `stop_code` | Código de parada, cuando está disponible. |
| `stop_name` | Nombre de la parada. |
| `stop_lat` | Latitud de la parada. |
| `stop_lon` | Longitud de la parada. |
| `codigo_barrio` | Código del barrio procedente de la capa espacial. |
| `barrio` | Nombre normalizado del barrio utilizado por MATILDA.AI. |
| `nombre_geojson` | Nombre original del barrio en el GeoJSON. |
| `asignacion` | Resultado de la asignación espacial. |

## 7.2 Valores de `asignacion`

### `DENTRO_POLIGONO`

La coordenada de la parada queda dentro de uno de los polígonos de barrio disponibles.

Estas son las paradas que MATILDA.AI puede utilizar para los análisis por barrio.

### `SIN_ASIGNAR_EN_GEOJSON`

La parada no queda dentro de ningún polígono de barrio de la capa disponible.

En el archivo actual:

- **248** paradas únicas.
- **245** asignadas a un barrio.
- **3** sin asignación espacial.

Las tres paradas sin asignar son:

| `stop_id` | Parada |
|---:|---|
| 287 | Errekalde II |
| 111 | Herrera Euskotren |
| 138 | Pasaiako Portua - Escalerillas |

Estas paradas **no se fuerzan** a ningún barrio por inferencia.

## 7.3 Normalización de nombres

El archivo derivado conserva tanto el nombre original del GeoJSON (`nombre_geojson`) como el nombre normalizado (`barrio`) utilizado para enlazarlo con la población de 2025.

Ejemplos de normalización utilizados en el proyecto:

```text
AMARABERRI             → Amara Berri
ERDIALDEA              → Centro
ANTIGUA                → Antiguo
LANDERBASO             → Landarbaso
MIRAMON - ZORROAGA     → Miramon-Zorroaga
ATEGORRIETA - ULIA     → Ategorrieta-Ulia
MIRAKRUZ - BIDEBIETA   → Miracruz-Bidebieta
```

Cuando el GeoJSON contiene nombres que no pertenecen al conjunto de los 18 barrios de la fuente de población, MATILDA.AI no inventa una equivalencia.

---

# 08 · Cómo se construye el análisis espacial

El flujo principal de la versión actual es:

```text
Población femenina 2025
          │
          ├──────────────┐
          │              │
          ▼              ▼
 barrios_donostia.json   stops2.txt
          │              │
          └──────┬───────┘
                 ▼
    gautxori_paradas_barrios.csv
                 │
                 ▼
          stop_times2.txt
                 │
                 ▼
      pasos programados por barrio
                 │
                 ▼
      indicadores descriptivos
```

Esto permite estudiar, por barrio:

- número de paradas;
- pasos programados;
- pasos programados en determinadas franjas;
- pasos por cada 1.000 mujeres.

---

# 09 · Indicadores utilizados

## Población femenina por barrio

```text
mujeres del barrio / 96.814 × 100
```

Representa la proporción de las mujeres contabilizadas en los 18 barrios respecto al total femenino municipal utilizado en la fuente de 2025.

## Paradas por 1.000 mujeres

```text
paradas Gautxori / mujeres × 1.000
```

Es un **indicador descriptivo de distribución espacial de la oferta**.

No mide accesibilidad real ni calidad del servicio.

## Pasos programados por 1.000 mujeres

```text
pasos programados / mujeres × 1.000
```

También es un indicador descriptivo. Se utiliza para comparar magnitudes de oferta programada con tamaños de población distintos.

No significa que ese número de mujeres tenga acceso al servicio ni que las personas utilicen el Gautxori.

---

# 10 · Resultados de referencia

Los análisis ya validados muestran, entre otros, los siguientes resultados:

### Población femenina · 2025

Los cinco barrios con mayor población femenina son:

| Barrio | Mujeres |
|---|---:|
| Amara Berri | 15.861 |
| Centro | 11.633 |
| Altza | 10.353 |
| Gros | 9.408 |
| Intxaurrondo | 7.811 |

En conjunto representan **55.066 mujeres**, aproximadamente el **56,9 %** de las 96.814 mujeres de los 18 barrios analizados.

### Gautxori · oferta programada

Sobre el GTFS completo se han contabilizado **5.716 registros de paso programados**.

Entre **01:00 y 03:59** se concentran **4.230 registros**, el **74,0 %** del total analizado.

### Seguridad municipal

La fila `TOTAL INFRACCIONES PENALES` pasa de **8.832** en enero–junio de 2025 a **8.321** en enero–junio de 2026, una diferencia de **−511 registros** (**−5,8 %**).

Estos resultados deben leerse junto a las limitaciones descritas en este repositorio.

---

# 11 · Qué MATILDA.AI no puede demostrar con estos datos

El proyecto no permite afirmar, únicamente a partir de estas fuentes, que:

- un barrio sea seguro o peligroso;
- una menor oferta relativa implique peor movilidad para las mujeres;
- el Gautxori reduzca las infracciones;
- exista causalidad entre movilidad y seguridad;
- los registros municipales representen toda la inseguridad o estén referidos específicamente a mujeres;
- los pasos programados equivalgan a personas usuarias;
- un barrio con cero paradas dentro de su polígono carezca de cualquier alternativa de movilidad nocturna.

La seguridad disponible es municipal y agregada. La oferta del Gautxori es programada. La población es residencial. Estas dimensiones **no son equivalentes** y no deben interpretarse como si fueran una única variable.

---

# 12 · Próxima fase de investigación

La versión actual permite detectar diferencias descriptivas de oferta por barrio y franja horaria. Una fase posterior podría incorporar:

### Accesibilidad peatonal

- red peatonal georreferenciada;
- distancias y tiempos reales a pie;
- pendientes y escaleras;
- barreras arquitectónicas;
- características de las paradas;
- iluminación y condiciones del entorno.

### Servicio efectivo y uso

- viajes realmente realizados;
- cancelaciones y retrasos;
- subidas y bajadas por parada;
- uso por franja horaria;
- ocupación aproximada.

### Seguridad y experiencia

- incidentes georreferenciados y agregados;
- franjas horarias;
- entornos de paradas o trayectos;
- encuestas de percepción de seguridad;
- experiencias de movilidad nocturna de las usuarias.

El objetivo sería pasar de una medida de **oferta programada** a una comprensión más completa de la **accesibilidad, el uso y la experiencia** sin convertir los indicadores en etiquetas automáticas para barrios.

---

# 13 · Transparencia y reproducibilidad

MATILDA.AI sigue varias reglas de calidad:

- utiliza los archivos reales disponibles en el proyecto;
- comprueba columnas y denominadores antes de calcular indicadores;
- valida el bloque de 18 barrios de Donostia antes de usar la población femenina;
- distingue datos de 2019 y 2025;
- distingue fuentes originales de archivos derivados;
- revisa las claves antes de combinar datasets;
- no fuerza asignaciones espaciales cuando no existe correspondencia;
- separa hechos, interpretaciones e hipótesis;
- no convierte coincidencias en causalidad;
- explicita las limitaciones de cada fuente.

La metodología detallada y las reglas de lectura se encuentran en `agente/FUENTES_8.md`.

---

# 14 · Cómo probar el agente

Algunas preguntas de demostración:

### Población

> ¿Cuáles son los 5 barrios de Donostia con más población femenina en 2025 y qué porcentaje representan sobre el total de mujeres de la ciudad? Usa ejecutar_codigo.

### Gautxori

> ¿Cómo se distribuye la oferta programada del Gautxori durante la noche? Identifica las franjas con más pasos y calcula qué porcentaje del total se concentra entre la 01:00 y las 03:59. Usa ejecutar_codigo.

### Barrios

> ¿Cuántas paradas del Gautxori hay en cada uno de los 18 barrios de Donostia? Usa ejecutar_codigo y muestra una tabla. No inventes datos.

### Análisis conjunto

> Con los datos disponibles, analiza conjuntamente la población femenina de los barrios, la oferta programada del Gautxori y los registros municipales de seguridad. Distingue claramente entre hechos, interpretaciones y aspectos que no podemos demostrar.

### Siguiente fase

> ¿Qué datos adicionales necesitaríamos para evaluar la accesibilidad real del Gautxori para las mujeres de los distintos barrios?

---

# 15 · Estructura de los datos del repositorio

```text
datos/
├── poblacion_barrio_2025_2.csv
├── demografiapiramideedadbarrio2.csv
├── seguridad_donostia_2025_2026_2.csv
│
├── agency2.txt
├── routes2.txt
├── trips2.txt
├── stops2.txt
├── stop_times2.txt
├── calendar2.txt
├── calendar_dates2.txt
├── shapes2.txt
├── feed_info2.txt
│
├── barrios_donostia.json
└── gautxori_paradas_barrios.csv
```

### Original vs. derivado

**Fuentes originales / de entrada**

- población 2025;
- pirámide demográfica 2019;
- seguridad municipal 2025–2026;
- archivos GTFS del Gautxori;
- delimitación espacial de barrios.

**Archivo derivado**

- `gautxori_paradas_barrios.csv`.

El archivo derivado permite repetir de forma consistente el análisis espacial sin tener que recalcular cada vez la asignación punto-polígono.

---

# 16 · Nota sobre datos y privacidad

El proyecto está planteado sobre datos agregados y fuentes de carácter urbano/estadístico. No se pretende publicar información personal ni trayectorias individuales.

Para una futura ampliación, los datos de seguridad y uso del transporte deberían solicitarse con un nivel de agregación suficiente para proteger la privacidad, especialmente cuando se incorporen coordenadas y dimensión temporal.

---

## MATILDA.AI · Preguntar. Comparar. Comprobar.

**Donostia-San Sebastián · Urban AI · Movilidad nocturna · Datos abiertos · Análisis reproducible**

