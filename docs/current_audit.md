# Repository audit — 2026-10-02

## What was checked

The following uploaded snapshots were inspected together:

- `main`
- `agente`
- `datos`

The audit checked the agent prompt, tool wrapper, source/limitations documentation, raw CSV/GTFS
files, spatial mapping and the published headline figures.

## Findings

### Confirmed

The principal published figures reconcile with the raw files:

- 96,814 women across the 18 population-source neighbourhoods.
- 245 of 248 mapped stops fall inside the available neighbourhood polygons.
- 3 stops remain explicitly unassigned.
- 5,716 GTFS `stop_times` rows.
- 5,624 `stop_times` rows can be spatially assigned to the 18 analysed neighbourhoods.
- 4,230 GTFS `stop_times` rows have departure hours 01:00–03:59.
- 4,161 assigned `stop_times` rows fall in that same period.
- Municipal `TOTAL INFRACCIONES PENALES`: 8,832 → 8,321.

### Improvements implemented in this package

1. Unified `main` + `agente` + `datos` into one judge-facing structure.
2. Reworked README around the project, evidence and limitations.
3. Added a source/provenance ledger.
4. Added methodology and reproducibility documentation.
5. Added explicit limitations and human-supervision guidance.
6. Added a 19-question evaluation suite including unsupported/adversarial questions.
7. Added a demo script.
8. Added `evaluation/validate_data.py`.
9. Added GitHub Actions to run the validation on pushes and pull requests.
10. Strengthened the Studio system prompt with source/period/denominator/spatial-quality controls.
11. Added a documented path for a future geolocated safety/accessibility layer.

## Important manual item

The repository cannot manufacture evidence of a Studio run. Before final submission, capture real
Studio executions for the demo questions and put those screenshots/transcripts under `demo/`.

The strongest evidence set is:

1. one simple lookup;
2. one multi-source calculation;
3. one spatial comparison;
4. one temporal analysis;
5. one unsupported question where MATILDA correctly refuses to overclaim.

## One strategic next step

Donostia's official open-data portal publishes a "Puntos críticos" dataset with location,
neighbourhood, coordinates, reason and intervention status. It could support a future spatial
safety/accessibility layer, but it should be added only after checking temporal compatibility
and defining exactly what the variable represents.
