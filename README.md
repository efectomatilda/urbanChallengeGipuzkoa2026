# MATILDA.AI

## Seguridad y movilidad nocturna de las mujeres en Donostia-San Sebastián

> **Una guía de análisis urbano para preguntar, comparar y comprobar.**

MATILDA.AI es un agente de análisis urbano creado para estudiar la **movilidad nocturna** y su contexto en materia de población femenina y registros municipales de seguridad en **Donostia-San Sebastián**.

Su propósito no es clasificar barrios como seguros o peligrosos ni tomar decisiones automáticamente. MATILDA.AI transforma datos urbanos heterogéneos en **preguntas investigables**, calcula indicadores reproducibles y hace explícitas las limitaciones de cada fuente para ayudar a **Puntos Morados y Emakumeen Etxea** a orientar futuras investigaciones sobre movilidad y accesibilidad nocturna.

---

## 01 · El reto urbano

La movilidad nocturna no puede entenderse a partir de un único conjunto de datos. MATILDA.AI combina tres dimensiones principales:

- **Población femenina:** dónde se concentra la población femenina residente.
- **Movilidad nocturna:** cómo se distribuye territorial y temporalmente la oferta programada del Gautxori.
- **Seguridad registrada:** qué muestran los registros municipales agregados y, sobre todo, qué no permiten demostrar.

La versión actual añade una **capa espacial**: las coordenadas de las paradas del Gautxori se cruzan con los polígonos de los barrios para poder describir la oferta por barrio.

### Pregunta de investigación

> **¿Qué patrones existen entre la distribución de la población femenina, la oferta programada de transporte nocturno Gautxori y los registros municipales de seguridad en Donostia-San Sebastián, y dónde se observan posibles diferencias de cobertura que requieran una investigación más detallada?**

---

## 02 · Qué hace MATILDA.AI

El agente puede:

1. Analizar la población femenina por barrio.
2. Analizar rutas, viajes, paradas, horarios, calendarios y excepciones del Gautxori mediante GTFS.
3. Asociar espacialmente las paradas del Gautxori a los barrios.
4. Calcular pasos programados por barrio y por franja horaria.
5. Comparar la oferta programada con la población femenina mediante indicadores descriptivos.
6. Utilizar los registros municipales de seguridad como **contexto agregado**, manteniéndolos a escala municipal por sus limitaciones espaciales.
7. Separar **hechos, interpretaciones y límites**.
8. Identificar qué datos adicionales harían falta para una siguiente fase de análisis urbano.

Los cálculos cuantitativos se realizan mediante la herramienta de ejecución de Python proporcionada por la plataforma del hackathon.

---

## 03 · Estructura del repositorio

```text
urbanChallengeGipuzkoa2026/
│
├── .github/
│   └── workflows/
│
├── agent/
│   ├── main.py
│   ├── tools.py
│   ├── FUENTES_8.md
│   └── README.md
│
├── data/
│   ├── README.md
│   ├── poblacion_barrio_2025_2.csv
│   ├── demografiapiramideedadbarrio2.csv
│   ├── seguridad_donostia_2025_2026_2.csv
│   ├── barrios_donostia.json
│   ├── gautxori_paradas_barrios.csv
│   ├── agency2.txt
│   ├── routes2.txt
│   ├── trips2.txt
│   ├── stops2.txt
│   ├── stop_times2.txt
│   ├── calendar2.txt
│   ├── calendar_dates2.txt
│   ├── shapes2.txt
│   └── feed_info2.txt
│
├── demo/
├── docs/
│   ├── metodologia.md
│   ├── preguntas_demo.md
│   ├── limitaciones.md
│   └── reproducibilidad.md
│
├── evaluation/
├── web/
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│   └── assets/
│       └── matilda.png
│
├── .gitignore
└── README.md
```

### Carpetas principales

**`agent/`** contiene el agente y la configuración que utiliza la plataforma para ejecutarlo.

**`data/`** contiene las fuentes de datos utilizadas por el proyecto y el archivo derivado necesario para el análisis espacial.

**`docs/`** recoge metodología, preguntas de demostración, limitaciones y reproducibilidad.

**`web/`** contiene la web pública de presentación del proyecto.

**`evaluation/`** contiene material de validación del proyecto.

---

## 04 · Fuentes de datos

La carpeta `data/` distingue entre **fuentes originales** y **archivos derivados**.

Para una explicación específica de cada archivo, consulta [`data/README.md`](data/README.md).

### 4.1 · Población femenina por barrios · 2025

**Archivo:** `poblacion_barrio_2025_2.csv`

Fuente estadística utilizada para la población de la C.A. de Euskadi por barrios de municipios de más de 10.000 habitantes, según sexo, grupos de edad y nacionalidad, con fecha **01/01/2025**.

En MATILDA.AI se utiliza principalmente la columna `Mujeres` para los 18 barrios de Donostia:

Aiete, Altza, Amara Berri, Antiguo, Ategorrieta-Ulia, Añorga, Centro, Egia, Gros, Ibaeta, Igeldo, Intxaurrondo, Landarbaso, Loiola, Martutene, Miracruz-Bidebieta, Miramon-Zorroaga y Zubieta.

La fila municipal de Donostia / San Sebastián contiene **96.814 mujeres**, y la suma de los 18 barrios se utiliza como comprobación de consistencia.

#### Lectura de las cifras

El fichero utiliza el punto como separador de miles:

```text
7.354  →  7.354 personas
520    →  520 personas
165    →  165 personas
```

MATILDA conserva inicialmente los valores como texto y los convierte posteriormente para evitar interpretar de forma incorrecta los valores con formato de miles.

---

### 4.2 · Estructura demográfica por edades · 2019

**Archivo:** `demografiapiramideedadbarrio2.csv`

Esta fuente se utiliza para consultas detalladas por **barrio y grupo de edad**.

- **Año:** 2019
- **Registros:** 140
- **Barrios:** 7
- **Población femenina:** `PertsonenKopG`
- **Barrio:** `Auzoa`
- **Grupo de edad:** `AdinTartea`

Esta fuente **no representa la población femenina actual de 2025**. MATILDA mantiene explícitamente separados los años 2019 y 2025.

---

### 4.3 · Registros municipales de seguridad · 2025–2026

**Archivo:** `seguridad_donostia_2025_2026_2.csv`

Cobertura:

- Donostia-San Sebastián
- enero-junio de 2025
- enero-junio de 2026

La fila `TOTAL INFRACCIONES PENALES` registra:

| Periodo | Total |
|---|---:|
| Enero-junio 2025 | 8.832 |
| Enero-junio 2026 | 8.321 |

Variación observada: **−511 registros**, aproximadamente **−5,8 %**.

#### Limitación fundamental

El fichero no contiene **barrio, calle, parada, coordenadas ni hora concreta de cada registro**.

Por ello, MATILDA utiliza estos datos únicamente como **contexto municipal agregado**. No los usa para calcular una supuesta peligrosidad por barrio ni para atribuir una categoría de infracción a una zona concreta.

Tampoco son datos específicos de mujeres ni una medida completa de la inseguridad o de todas las experiencias de las usuarias.

---

## 05 · Gautxori / GTFS

La oferta programada del Gautxori está distribuida en nueve archivos GTFS:

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

### Qué contiene cada archivo

| Archivo | Función principal |
|---|---|
| `agency2.txt` | Información de la agencia o operador. |
| `routes2.txt` | Definición de las rutas. |
| `trips2.txt` | Viajes programados. |
| `stops2.txt` | Paradas y sus coordenadas. |
| `stop_times2.txt` | Horarios y pasos programados de cada viaje por parada. |
| `calendar2.txt` | Calendario de los servicios. |
| `calendar_dates2.txt` | Excepciones al calendario. |
| `shapes2.txt` | Geometrías de los recorridos. |
| `feed_info2.txt` | Metadatos del feed GTFS. |

En el análisis validado se identificaron **14 rutas definidas**, **8 rutas con viajes asociados** y **303 viajes programados**.

El archivo `stop_times2.txt` contiene **5.716 registros de paso programados** en el análisis general del GTFS.

### Importante: “paso programado” no significa “pasajero”

Los datos GTFS describen una **oferta planificada**. No equivalen a:

- pasajeros;
- demanda;
- ocupación;
- retrasos reales;
- cancelaciones reales;
- percepción de seguridad;
- accesibilidad peatonal;
- calidad del entorno.

---

## 06 · Capa espacial de barrios

**Archivo:** `barrios_donostia.json`

Es un archivo GeoJSON que contiene una `FeatureCollection` con geometrías de tipo `Polygon` y atributos de identificación de los barrios.

El archivo se utiliza para determinar **qué polígono de barrio contiene la coordenada de cada parada** del Gautxori.

El objetivo es poder pasar de:

```text
parada + coordenadas
        ↓
polígono de barrio
        ↓
barrio
```

La asignación espacial no se realiza por una simple coincidencia de texto entre nombres.

---

## 07 · Archivo derivado: `gautxori_paradas_barrios.csv`

Este archivo es una de las piezas centrales de la versión actual de MATILDA.AI.

**No es una fuente original.** Es un archivo derivado preparado a partir de:

```text
stops2.txt
    +
barrios_donostia.json
    ↓
gautxori_paradas_barrios.csv
```

Su función es guardar una correspondencia reproducible entre cada parada del GTFS y el barrio cuyo polígono contiene sus coordenadas, cuando existe esa correspondencia.

### Columnas principales

| Columna | Significado |
|---|---|
| `stop_id` | Identificador de la parada en el GTFS. |
| `stop_code` | Código de parada, cuando existe. |
| `stop_name` | Nombre de la parada. |
| `stop_lat` | Latitud. |
| `stop_lon` | Longitud. |
| `codigo_barrio` | Código del barrio asignado desde la capa espacial. |
| `barrio` | Nombre normalizado utilizado por MATILDA. |
| `nombre_geojson` | Nombre original procedente del GeoJSON. |
| `asignacion` | Resultado de la correspondencia espacial. |

### Estados de asignación

**`DENTRO_POLIGONO`**

La coordenada de la parada queda dentro de un polígono de barrio. Estas filas pueden utilizarse en los análisis comparativos por barrio.

**`SIN_ASIGNAR_EN_GEOJSON`**

La coordenada de la parada no queda dentro de ninguno de los polígonos utilizados para la asignación. Estas paradas se conservan, pero no se fuerzan a un barrio por inferencia.

En el GTFS utilizado:

- **248** paradas únicas;
- **245** asignadas a un barrio;
- **3** sin asignación espacial.

Las tres paradas sin asignar son `287`, `111` y `138`.

### Normalización de nombres

Para poder cruzar la capa espacial con la fuente de población 2025, algunos nombres se normalizan:

```text
AMARABERRI            → Amara Berri
ERDIALDEA             → Centro
ANTIGUA               → Antiguo
LANDERBASO            → Landarbaso
MIRAMON - ZORROAGA    → Miramon-Zorroaga
ATEGORRIETA - ULIA    → Ategorrieta-Ulia
MIRAKRUZ - BIDEBIETA  → Miracruz-Bidebieta
```

El GeoJSON contiene también `OARAIN`, pero ese nombre no forma parte del conjunto de 18 barrios de la fuente de población 2025. MATILDA no le asigna una población por inferencia.

---

## 08 · Cómo se construye el análisis

El flujo espacial y analítico de la versión actual es:

```text
Población femenina 2025
          │
          │
          ├───────────────┐
          │               │
          ▼               ▼
barrios_donostia.json   stops2.txt
          │               │
          └───────┬───────┘
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

Para una comparación por barrio, MATILDA:

1. obtiene las 18 filas de población femenina de Donostia en 2025;
2. utiliza `gautxori_paradas_barrios.csv` para localizar las paradas;
3. cuenta `stop_id` únicos por barrio;
4. relaciona `stop_times2.txt` mediante `stop_id`;
5. cuenta registros de paso programados por barrio;
6. filtra por `departure_time` cuando se solicita una franja horaria;
7. calcula indicadores relativos cuando corresponde;
8. conserva los 18 barrios y representa con 0 los barrios sin paradas asignadas;
9. explica las limitaciones de esos indicadores.

---

## 09 · Indicadores

### Concentración de población femenina

```text
mujeres del barrio / 96.814 × 100
```

Mide qué proporción de las mujeres contabilizadas en los 18 barrios reside en cada barrio según la fuente de 01/01/2025.

### Paradas por 1.000 mujeres

```text
paradas del Gautxori / mujeres × 1.000
```

Es un indicador descriptivo de distribución espacial de la oferta.

### Pasos programados por 1.000 mujeres

```text
pasos programados / mujeres × 1.000
```

Es un indicador descriptivo para comparar magnitudes de oferta programada entre barrios con tamaños de población diferentes.

### Qué NO significan estos indicadores

Un valor alto o bajo no demuestra por sí mismo:

- mejor o peor movilidad;
- mayor o menor accesibilidad real;
- mayor o menor uso;
- mayor o menor seguridad;
- necesidad automática de crear o modificar una parada.

---

## 10 · Resultados de referencia

Los análisis validados de la versión actual muestran:

### Población femenina · 2025

Los cinco barrios con mayor población femenina son:

| Barrio | Mujeres |
|---|---:|
| Amara Berri | 15.861 |
| Centro | 11.633 |
| Altza | 10.353 |
| Gros | 9.408 |
| Intxaurrondo | 7.811 |

Los cinco suman **55.066 mujeres**, aproximadamente el **56,9 %** de las 96.814 mujeres de los 18 barrios analizados.

### Gautxori · oferta programada

Sobre el GTFS completo se han contabilizado **5.716 registros de paso programados**.

Entre **01:00 y 03:59** se concentran **4.230 registros**, el **74,0 %** del total analizado.

### Población + Gautxori por barrio

Al utilizar la correspondencia espacial disponible, **245 de las 248 paradas** quedan asignadas a los 18 barrios de referencia.

En el análisis por barrio, los registros de `stop_times2.txt` asignables a esas paradas suman **5.624**. Los **92 registros restantes** corresponden a las tres paradas que no pudieron asignarse espacialmente a un polígono de barrio.

### Seguridad municipal

La fila `TOTAL INFRACCIONES PENALES` pasa de **8.832** en enero-junio de 2025 a **8.321** en enero-junio de 2026: **−511 registros**, aproximadamente **−5,8 %**.

Estas cifras de seguridad se mantienen a nivel municipal porque el fichero no incluye información espacial suficiente para relacionarlas directamente con barrios o paradas.

---

## 11 · Qué no puede demostrar MATILDA.AI con los datos actuales

Con las fuentes disponibles no se puede afirmar, únicamente a partir de estos datos, que:

- un barrio sea seguro o peligroso;
- una menor oferta relativa implique peor movilidad para sus residentes;
- el Gautxori reduzca las infracciones;
- exista una relación causal entre movilidad y seguridad;
- los registros municipales representen toda la inseguridad;
- los registros de seguridad se refieran específicamente a mujeres;
- los pasos programados equivalgan a personas usuarias;
- un barrio con cero paradas dentro de su polígono carezca de alternativas de movilidad nocturna.

La población residente, la oferta programada y la seguridad registrada son **dimensiones diferentes**. No deben tratarse como si fueran una única medida.

---

## 12 · Siguiente fase

La versión actual permite estudiar **diferencias descriptivas de oferta programada por barrio y franja horaria**.

Para evaluar accesibilidad de forma más completa, una siguiente fase podría incorporar:

### Accesibilidad peatonal

- red peatonal georreferenciada;
- tiempos y distancias reales a pie;
- pendientes y escaleras;
- barreras arquitectónicas;
- características y accesibilidad de las paradas;
- iluminación y condiciones del entorno.

### Servicio efectivo y uso

- viajes realmente realizados;
- cancelaciones y retrasos;
- subidas y bajadas por parada;
- uso por franja horaria;
- ocupación aproximada.

### Seguridad y experiencia

- incidentes georreferenciados y temporalmente agregados;
- entorno de paradas y trayectos;
- franjas horarias;
- encuestas de percepción de seguridad;
- experiencias de movilidad nocturna de las usuarias.

El objetivo sería evolucionar desde **oferta programada** hacia una comprensión más completa de **accesibilidad, servicio efectivo, uso, seguridad registrada y experiencia**.

---

## 13 · Transparencia y reproducibilidad

MATILDA.AI sigue unas reglas explícitas de calidad:

- trabajar con los archivos reales disponibles en el proyecto;
- comprobar columnas, claves y denominadores antes de calcular indicadores;
- validar el bloque de los 18 barrios de Donostia antes de utilizar la población femenina;
- mantener separados los años 2019 y 2025;
- distinguir las fuentes originales de los archivos derivados;
- no forzar asignaciones espaciales cuando no existe correspondencia;
- diferenciar hechos, interpretaciones e hipótesis;
- no convertir coincidencias en causalidad;
- indicar las limitaciones relevantes junto a los resultados.

La metodología detallada se encuentra en [`docs/metodologia.md`](docs/metodologia.md).

Las preguntas recomendadas para la demostración se encuentran en [`docs/preguntas_demo.md`](docs/preguntas_demo.md).

La descripción específica de los datasets se encuentra en [`data/README.md`](data/README.md).

---

## 14 · Cómo probar MATILDA.AI

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

## 15 · Web del proyecto

La web pública de presentación acompaña al agente y resume el problema, los datos, los hallazgos, la capa espacial por barrios, las limitaciones y la siguiente fase.

**Web:** https://matildaai.netlify.app/

El código de la web está disponible en la carpeta [`web/`](web/).

---

## 16 · Nota sobre los datos derivados

`gautxori_paradas_barrios.csv` se incluye para que la relación espacial entre paradas y barrios pueda reutilizarse de forma consistente en el análisis.

Su contenido debe interpretarse como un **resultado de procesamiento geográfico**, no como una fuente independiente del Ayuntamiento o del operador de transporte.

La trazabilidad se mantiene mediante la relación:

```text
stops2.txt + barrios_donostia.json
                ↓
gautxori_paradas_barrios.csv
```

---

## 17 · Privacidad y uso responsable

El proyecto utiliza fuentes urbanas y estadísticas agregadas. No pretende publicar trayectorias individuales ni información personal.

Para futuras ampliaciones con datos de seguridad, movilidad o uso del transporte, MATILDA.AI plantea trabajar con niveles de agregación espacial y temporal suficientes para proteger la privacidad y evitar la identificación de personas o incidentes individuales.

---

## MATILDA.AI

**Preguntar. Comparar. Comprobar.**

Donostia-San Sebastián · Urban AI · Movilidad nocturna · Datos abiertos · Análisis reproducible
