# MATILDA.AI — Urban Challenge Gipuzkoa 2026

> **Preguntar. Comparar. Comprobar.**
>
> Un agente de análisis urbano para investigar la relación entre población femenina,
> movilidad nocturna programada y datos municipales de seguridad en Donostia-San Sebastián,
> haciendo explícito qué puede demostrarse y qué no.

## 30 segundos para entenderlo

**Pregunta urbana**

> ¿Qué patrones existen entre la distribución de la población femenina, la oferta programada
> del Gautxori y los registros municipales de seguridad, y qué diferencias territoriales
> merecen una investigación más detallada?

**MATILDA no etiqueta barrios como seguros o peligrosos.** Cruza datos verificables,
calcula indicadores reproducibles y explica sus límites.

**Pipeline**

`pregunta → fuente → Python → validación → hecho → patrón → interpretación → limitación`

### Demo

- Web: https://matildaai.netlify.app/
- Agente: [`agent/main.py`](agent/main.py)
- Fuentes y límites: [`agent/FUENTES_8.md`](agent/FUENTES_8.md)
- Datos: [`data/`](data/)
- Evaluación: [`evaluation/`](evaluation/)
- Metodología: [`docs/methodology.md`](docs/methodology.md)

---

## Evidencia validada en los datos incluidos

| Métrica | Resultado |
|---|---:|
| Mujeres en los 18 barrios analizados, 01/01/2025 | **96.814** |
| Paradas Gautxori dentro de los polígonos analizados | **245** |
| Registros `stop_times` del GTFS | **5.716** |
| Registros `stop_times` asignados a los 18 barrios | **5.624** |
| Registros `stop_times` entre 01:00–03:59 | **4.230** |
| Infracciones penales municipales, ene–jun 2025 | **8.832** |
| Infracciones penales municipales, ene–jun 2026 | **8.321** |

Estos valores están comprobados contra los archivos incluidos. La validación reproducible está
en [`evaluation/validate_data.py`](evaluation/validate_data.py).

**Importante:** un `stop_time` es un paso programado en una parada; no es un pasajero.
Los datos municipales de seguridad incluidos no tienen barrio, parada, coordenadas ni hora
individual, por lo que no permiten construir una tasa de seguridad por barrio.

---

## Por qué este agente es distinto

El objetivo no es producir una visualización preconfigurada ni responder con cifras memorizadas.

Para preguntas cuantitativas, MATILDA debe usar `ejecutar_codigo` antes de responder. La
respuesta separa:

1. **HECHO** — cifra observada/calculada.
2. **PATRÓN** — diferencia o coincidencia descriptiva.
3. **INTERPRETACIÓN** — lectura prudente.
4. **LIMITACIÓN** — qué no permiten demostrar los datos.

Ante preguntas que los datos no permiten responder, el comportamiento esperado es explicar
la insuficiencia de evidencia y, cuando sea posible, indicar qué dato adicional permitiría
avanzar.

---

## Datos

### Población femenina

`data/poblacion_barrio_2025_2.csv.csv`

- Fuente: Eustat / Censo de población y viviendas.
- Referencia: 01/01/2025.
- Se utilizan las 18 filas de barrios de Donostia que siguen a la fila municipal.
- `Mujeres` se interpreta con punto como separador de miles.

### Gautxori / GTFS

`data/agency2.txt`, `routes2.txt`, `trips2.txt`, `stops2.txt`,
`stop_times2.txt`, `calendar2.txt`, `calendar_dates2.txt`, `shapes2.txt`,
`feed_info2.txt`.

Permite estudiar oferta programada: rutas, viajes, paradas, horarios y pasos.

### Barrios

`data/barrios_donostia.geojson.json`

GeoJSON con los polígonos utilizados para asignar espacialmente las paradas.

### Correspondencia espacial

`data/gautxori_paradas_barrios.csv`

Tabla derivada `stop_id → barrio`. Las 3 paradas sin polígono se conservan como
`SIN_ASIGNAR_EN_GEOJSON` y no se fuerzan a ningún barrio.

### Seguridad

`data/seguridad_donostia_2025_2026_2.csv`

Enero–junio de 2025 frente a enero–junio de 2026, a escala municipal.

---

## Arquitectura

```text
                 ┌───────────────────┐
                 │   Pregunta humana │
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │    MATILDA.AI     │
                 │ interpreta +      │
                 │ selecciona fuente │
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │ ejecutar_codigo   │
                 │ Python / pandas   │
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │ Validación        │
                 │ claves · fechas   │
                 │ denominadores     │
                 │ geografía         │
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │ Respuesta         │
                 │ hecho/patrón/     │
                 │ interpretación/   │
                 │ limitación        │
                 └───────────────────┘
```

---

## Repositorio

```text
.
├── README.md
├── website.md
├── agent/
│   ├── main.py
│   ├── tools.py
│   ├── FUENTES_8.md
│   └── README.md
├── data/
│   ├── README.md
│   ├── *.txt / *.csv / *.json
├── docs/
│   ├── methodology.md
│   ├── sources.md
│   ├── limitations.md
│   ├── reproducibility.md
│   ├── evaluation.md
│   └── demo_questions.md
├── evaluation/
│   ├── validate_data.py
│   └── README.md
└── demo/
    └── README.md
```

---

## Cómo reproducir la validación local

Requiere Python 3 y pandas:

```bash
pip install pandas
python evaluation/validate_data.py
```

El agente de `agent/main.py` está preparado para el entorno Studio del hackathon y depende
de las interfaces `studio` y `ejecucion` proporcionadas por ese entorno. Por eso la
validación de datos es independiente del runtime de Studio.

---

## Límites que MATILDA debe respetar

Con los datos actuales no puede demostrar:

- que un barrio sea seguro o peligroso;
- que una zona concentre más violencia contra las mujeres;
- que menor oferta programada implique peor movilidad real;
- que el Gautxori reduzca las infracciones;
- una relación causal entre transporte y seguridad;
- accesibilidad peatonal real desde cualquier vivienda a una parada.

Para una lista detallada de límites y datos que faltan: [`docs/limitations.md`](docs/limitations.md).

---

## Fuente espacial adicional recomendada

El Ayuntamiento de Donostia publica un conjunto de **Puntos críticos** con ubicación, barrio,
coordenadas, motivo e información sobre intervención. Es una fuente potencialmente valiosa para
una siguiente versión porque aporta una capa espacial de seguridad/accesibilidad distinta del
fichero municipal agregado usado actualmente.

**No se incorpora automáticamente a los indicadores actuales:** primero debe documentarse su
fecha, unidad de análisis, relación con la definición de “seguridad” y compatibilidad temporal
con el resto de fuentes.

---

## Licencias y procedencia

Los datos son fuentes públicas de terceros y deben conservar sus condiciones de uso originales.
La documentación de procedencia está en [`docs/sources.md`](docs/sources.md).

El código de este repositorio no declara una licencia de software nueva para no atribuir una
licencia que el equipo no haya elegido.

---

## Equipo

**Efecto Matilda — Gipuzkoa AI Hackathon 2026**
