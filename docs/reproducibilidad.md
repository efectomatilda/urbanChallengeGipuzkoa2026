# Reproducibilidad

## Qué se puede reproducir localmente

La validación de los datos incluidos se ejecuta sin Studio:

```bash
pip install pandas
python evaluation/validate_data.py
```

Esto comprueba las invariantes principales del proyecto.

## Qué depende de Studio

`agent/main.py` usa:

- `studio`
- `ejecucion`
- el modelo proporcionado por la plataforma.

`agent/tools.py` reproduce la interfaz de `ejecutar_codigo` usada en Studio y no debe
modificarse sin comprobar la compatibilidad con la plataforma.

## Invariantes validadas

- 18 barrios de Donostia en la fuente de población.
- 96.814 mujeres en esos 18 barrios.
- 248 paradas en el mapping espacial.
- 245 dentro de polígonos.
- 3 sin asignar.
- 5.716 registros `stop_times`.
- 5.624 registros asignados a los 18 barrios.
- 4.230 registros entre 01:00 y 03:59 en el GTFS completo.
- 8.832 y 8.321 en la fila municipal `TOTAL INFRACCIONES PENALES`.

## Buenas prácticas

- conservar los nombres de archivo usados por el agente;
- no mezclar periodos;
- comprobar claves antes de `merge`;
- indicar el denominador de ratios;
- distinguir cero de dato ausente;
- no forzar asignaciones espaciales.
