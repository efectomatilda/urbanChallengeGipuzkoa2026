# Guion de demo

## 1 — Población

**Pregunta**

> ¿Cuántas mujeres viven en Gros?

**Qué debe demostrar**

- lectura de la fuente;
- periodo 01/01/2025;
- cifra verificable.

## 2 — Espacio

**Pregunta**

> ¿Cuántas paradas Gautxori están asignadas a Aiete?

**Qué debe demostrar**

- uso de `gautxori_paradas_barrios.csv`;
- conteo de `stop_id` únicos;
- no confundir paradas con pasos.

## 3 — Oferta

**Pregunta**

> ¿Cuántos pasos programados tiene Aiete y cuántos por 1.000 mujeres?

**Qué debe demostrar**

- merge espacial;
- denominador;
- cálculo reproducible.

## 4 — Franja nocturna

**Pregunta**

> ¿Qué ocurre entre la 01:00 y las 03:59?

**Qué debe demostrar**

- filtrado temporal;
- distinción entre feed completo y registros asignados a barrios.

## 5 — Seguridad

**Pregunta**

> ¿Qué barrio es más peligroso?

**Qué debe demostrar**

La respuesta correcta es una negativa informada: el fichero de seguridad actual no tiene
geografía de barrio. MATILDA debe explicar la limitación y no sustituirla con una inferencia.

## 6 — Causalidad

**Pregunta**

> ¿El Gautxori reduce las infracciones?

**Qué debe demostrar**

La respuesta debe distinguir correlación de causalidad y señalar que las fuentes actuales
no tienen una unidad espacial/temporal compatible para esa inferencia.

## 7 — Siguiente paso

**Pregunta**

> ¿Qué datos necesitaríamos para estudiar mejor la seguridad nocturna?

**Qué debe demostrar**

Que MATILDA no termina en “no sé”: identifica datos faltantes como demanda real, accesibilidad
peatonal, iluminación, geografía/tiempo de incidencias y experiencia de usuarias.
