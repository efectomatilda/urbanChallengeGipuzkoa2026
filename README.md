# urbanChallengeGipuzkoa2026
Nuestro agente IA para la fase "Urban Challenge" de "Gipuzkoa AI Hackaton 2026".
<div align="center">

# MATILDA.AI

### Seguridad y movilidad nocturna de las mujeres en Donostia-San Sebastián

**Urban AI · Donostia-San Sebastián · Gipuzkoa**

> **Preguntar. Comparar. Comprobar.**
>
> Una guía de análisis urbano para convertir datos dispersos en preguntas investigables, sin inventar lo que los datos no pueden demostrar.

</div>

---

## 01 · El proyecto

**MATILDA.AI** es un agente de análisis de datos urbanos desarrollado para estudiar la **movilidad nocturna de las mujeres** en Donostia-San Sebastián y apoyar el trabajo de **Puntos Morados** y **Emakumeen Etxea**.

El proyecto parte de una pregunta sencilla, pero exige relacionar fuentes con escalas y capacidades diferentes:

> **¿Qué patrones existen entre la distribución de la población femenina, la oferta programada de transporte nocturno Gautxori y los registros municipales de seguridad en Donostia-San Sebastián, y dónde se observan posibles diferencias de cobertura que requieran una investigación más detallada?**

MATILDA no pretende etiquetar barrios como “seguros” o “peligrosos”. Su función es **hacer visibles diferencias, comprobar cifras y señalar qué información falta para avanzar hacia un diagnóstico urbano más completo**.

---

## 02 · El problema urbano

La movilidad nocturna no depende de un único dato. Para entenderla hay que mirar, al menos, **quién vive en cada zona, qué transporte nocturno está programado y qué información existe sobre seguridad y accesibilidad**.

La versión actual de MATILDA añade una capa espacial al análisis: las coordenadas de las paradas del Gautxori se relacionan con los polígonos oficiales de los barrios. Esto permite pasar de una visión únicamente municipal a una comparación descriptiva por barrio.

La herramienta puede ayudar a detectar, por ejemplo, que dos barrios con poblaciones femeninas diferentes presentan distribuciones distintas de paradas y pasos programados. Ese hallazgo **no decide una actuación**: abre una pregunta que puede investigarse con datos adicionales de accesibilidad, uso y experiencia de las usuarias.

---

## 03 · Qué analiza

| Dimensión | Fuente | Periodo / escala | Qué permite estudiar |
|---|---|---|---|
| **Población femenina** | `poblacion_barrio_2025_2.csv` | 01/01/2025 · 18 barrios | Mujeres por barrio, concentración y ratios descriptivos |
| **Movilidad nocturna** | GTFS Gautxori | Servicio programado | Rutas, viajes, paradas, horarios, pasos y franjas |
| **Espacio urbano** | `barrios_donostia.json` | Barrios de Donostia | Asignación espacial de paradas a polígonos |
| **Seguridad** | `seguridad_donostia_2025_2026_2.csv` | Ene–jun 2025 vs ene–jun 2026 · municipio | Evolución agregada de registros de infracciones |

### La capa espacial

`gautxori_paradas_barrios.csv` actúa como tabla de correspondencia entre `stop_id` y barrio. Para las comparaciones por barrio se utilizan las paradas clasificadas como `DENTRO_POLIGONO`; las paradas que no entran en ningún polígono se conservan como **sin asignar** y no se fuerzan a una zona.

---

## 04 · Resultados de la versión validada

### 96.814
**mujeres** en los 18 barrios de Donostia según la fuente de población de 01/01/2025.

### 245
**paradas Gautxori** asignadas dentro de los polígonos de los 18 barrios analizados.

### 5.716 → 5.624
El GTFS contiene **5.716 registros de paso**. De ellos, **5.624** se pueden asignar espacialmente a los 18 barrios con los polígonos disponibles.

### 4.230
**pasos programados** entre 01:00 y 03:59 cuando se analiza el GTFS completo, equivalentes al **74,0 %** de los registros de paso analizados en esa distribución horaria.

### 8.832 → 8.321
Registros de **infracciones penales totales** en Donostia para enero-junio de 2025 y enero-junio de 2026, respectivamente: **511 menos**, aproximadamente **−5,8 %**.

> **Importante:** los pasos GTFS son registros de programación por parada, no pasajeros ni demanda real. Los registros municipales de seguridad son agregados y no contienen barrio, parada, coordenadas ni hora individual.

---

## 05 · Cómo funciona MATILDA

```text
FUENTES DE DATOS
      │
      ├── Población femenina 2025
      ├── GTFS Gautxori
      ├── Barrios / geometrías
      └── Seguridad municipal agregada
      │
      ▼
SELECCIÓN DE LA FUENTE RELEVANTE
      │
      ▼
EJECUCIÓN REPRODUCIBLE CON PYTHON
      │
      ├── filtros y validaciones
      ├── uniones por claves
      ├── asignación espacial de paradas
      ├── cálculos por barrio y franja
      └── indicadores relativos
      │
      ▼
RESPUESTA EXPLICABLE
      │
      ├── HECHO
      ├── PATRÓN
      ├── INTERPRETACIÓN
      └── LIMITACIÓN
```

El agente está diseñado para utilizar `ejecutar_codigo` antes de responder a preguntas que requieren datos, cálculos o comparaciones. La intención es que las cifras puedan comprobarse en lugar de depender de memoria o de explicaciones genéricas.

---

## 06 · Indicadores

### Paradas por 1.000 mujeres

`paradas del barrio / mujeres del barrio × 1.000`

Sirve para describir la relación entre el número de paradas y el tamaño de la población femenina residente.

### Pasos programados por 1.000 mujeres

`pasos programados del barrio / mujeres del barrio × 1.000`

Añade la dimensión temporal del GTFS y permite comparar la oferta programada relativa entre barrios.

### Franjas nocturnas

MATILDA puede estudiar la distribución de los pasos programados por hora y centrarse en periodos como **01:00–03:59**, manteniendo siempre explícito que se trata de programación.

---

## 07 · Qué puede decir y qué no puede decir

### Sí puede decir

- cuántas mujeres hay en cada barrio según la fuente de 2025;
- cuántas paradas del Gautxori quedan dentro de cada polígono;
- cuántos pasos programados se registran por barrio y franja;
- cómo cambia la oferta relativa cuando se divide entre la población femenina;
- qué diferencias descriptivas merecen una investigación posterior;
- cómo evoluciona el total municipal de infracciones entre los periodos disponibles.

### No puede demostrar con los datos actuales

- que un barrio sea seguro o peligroso;
- que una zona concentre más violencia contra las mujeres;
- que una oferta relativa menor implique peor movilidad real;
- que el Gautxori reduzca las infracciones;
- que exista una relación causal entre movilidad y seguridad;
- que una parada situada dentro de un polígono sea igualmente accesible para toda la población del barrio.

La seguridad se mantiene a **escala municipal**, porque la fuente disponible no tiene localización por barrio, calle, parada o coordenadas.

---

## 08 · Arquitectura del repositorio

```text
MATILDA-AI/
│
├── README.md
│
├── agente/
│   ├── main.py
│   ├── tools.py
│   ├── FUENTES_8.md
│   └── INSTRUCCIONES_V11_JSON.md
│
├── web/
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│   └── assets/
│       └── matilda.png
│
├── branding/
│   ├── matilda-avatar.png
│   └── logo-mt-concept.png
│
├── datos/
│   ├── README.md
│   ├── poblacion_barrio_2025_2.csv
│   ├── barrios_donostia.json
│   └── gautxori_paradas_barrios.csv
│
├── docs/
│   ├── metodologia.md
│   ├── limitaciones.md
│   └── preguntas_demo.md
│
└── capturas/
    └── README.md
```

---

## 09 · La web

La carpeta `web/` contiene una **landing page estática** que presenta el problema, las fuentes, los hallazgos, la capa espacial por barrios, el funcionamiento del agente y las limitaciones.

No necesita backend para mostrarse. Puede desplegarse directamente en servicios de hosting estático como Netlify o GitHub Pages.

---

## 10 · El agente en Studio

`agente/main.py` está pensado para el entorno de Studio del hackathon.

La plataforma proporciona el modelo y la herramienta `ejecutar_codigo`, por lo que **no se incluye ninguna API key en el código**.

`agente/tools.py` reproduce la herramienta proporcionada por la plataforma y debe mantenerse sin cambios en Studio.

### Contexto esperado por `main.py`

El agente referencia estos archivos:

```text
FUENTES_8.md
poblacion_barrio_2025_2.csv
demografiapiramideedadbarrio2.csv
seguridad_donostia_2025_2026_2.csv
barrios_donostia.json
gautxori_paradas_barrios.csv
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

Los archivos de trabajo que no se publican en este repositorio deben mantenerse en el workspace del hackathon y coincidir con los nombres utilizados por `main.py`.

---

## 11 · Cómo probar MATILDA

Las preguntas recomendadas para una demostración están en [`docs/preguntas_demo.md`](docs/preguntas_demo.md).

La secuencia narrativa es deliberadamente sencilla:

**¿Dónde vive la población femenina? → ¿Cómo se distribuye el Gautxori? → ¿Qué ocurre de madrugada? → ¿Qué podemos y qué no podemos relacionar con la seguridad? → ¿Qué datos necesitamos después?**

---

## 12 · Siguiente fase

La siguiente evolución de MATILDA no consiste en asignar una etiqueta a cada barrio, sino en incorporar información que permita medir mejor la accesibilidad y el uso real del sistema.

### Datos especialmente valiosos

- red peatonal y tiempos reales o estimados de acceso a pie;
- características físicas y accesibilidad de las paradas;
- expediciones realmente realizadas, cancelaciones y retrasos;
- uso anonimizado por parada y franja;
- seguridad agregada espacial y temporalmente;
- iluminación, obras y barreras del entorno;
- percepción y experiencias de las mujeres usuarias y residentes.

El objetivo sería pasar de una **aproximación descriptiva de oferta** a una visión más completa de **accesibilidad potencial, oferta efectiva, uso, seguridad registrada y experiencia**.

---

## 13 · Filosofía del proyecto

MATILDA toma su nombre y su identidad visual de una **guía**: una figura que acompaña la lectura de los datos, pero no decide por quien los utiliza.

Su principio central es:

> **Preguntar. Comparar. Comprobar.**

Una diferencia en los datos puede abrir una investigación. No debe convertirse automáticamente en una conclusión.

---

<div align="center">

**MATILDA.AI** · Urban AI · Donostia-San Sebastián

_Análisis reproducible · datos reales · límites explícitos_

</div>
