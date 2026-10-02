# Fuentes y trazabilidad

| ID | Fuente | Archivo local | Periodo | Uso |
|---|---|---|---|---|
| POP-2025 | Eustat, Censo de población y viviendas / estructura de población | `poblacion_barrio_2025_2.csv.csv` | 01/01/2025 | Mujeres por barrio |
| AGE-2019 | Pirámide demográfica | `demografiapiramideedadbarrio2.csv` | 2019 | Desglose por edad; no usar como 2025 |
| GTFS | Feed Gautxori | `agency2.txt`, `routes2.txt`, `trips2.txt`, `stops2.txt`, `stop_times2.txt`, `calendar2.txt`, `calendar_dates2.txt`, `shapes2.txt`, `feed_info2.txt` | Feed incluido | Oferta programada |
| GEO-01 | Barrios de Donostia | `barrios_donostia.geojson.json` | Versión incluida | Polígonos |
| GEO-02 | Correspondencia espacial derivada | `gautxori_paradas_barrios.csv` | Derivada del feed + polígonos | `stop_id → barrio` |
| SEC-2025/26 | Registros municipales agregados | `seguridad_donostia_2025_2026_2.csv` | Ene–jun 2025/2026 | Contexto municipal |

## Fuentes oficiales consultadas

### Eustat / Open Data Euskadi

La ficha oficial de población por ámbitos territoriales describe el Censo de población y
viviendas, con referencia 01/01/2025 y población por barrios en municipios de más de 10.000
habitantes:

https://opendata.euskadi.eus/catalogo/-/poblacion-de-la-c-a-de-euskadi-por-ambitos-territoriales-segun-sexo-y-los-componentes-de-la-variacion/frequency/

### Donostia Open Data

Portal oficial de datos abiertos:

https://www.donostia.eus/datosabiertos/

Catálogo de transporte:

https://donostia.eus/datosabiertos/catalogo?_keywords_es_limit=0&groups=transporte

### Barrios de Donostia

El catálogo municipal incluye el conjunto oficial “Barrios de Donostia / San Sebastián” y
describe sus geometrías territoriales:

https://www.donostia.eus/datosabiertos/catalogo?_keywords_es_limit=0&res_format=GeoJSON

### Puntos críticos

El Ayuntamiento mantiene un conjunto de Puntos críticos con ubicación, barrio, coordenadas,
motivo e información de intervención:

https://www.donostia.eus/datosabiertos/dataset/seguridad-ptos_criticos

## Qué debe añadirse si se conoce

Para una trazabilidad de nivel publicación, completar cada fila con:

- URL exacta de descarga del archivo;
- fecha de descarga;
- fecha de publicación/modificación de la fuente;
- licencia;
- transformación aplicada;
- hash del archivo original, si se conserva.

No se inventan URLs de descarga que no estén documentadas.
