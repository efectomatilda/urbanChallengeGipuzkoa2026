# MATILDA agent

`main.py` is the Studio entry point. `tools.py` exposes the `ejecutar_codigo` tool expected
by the hackathon environment.

## Contract

For any question requiring data, calculations, comparisons, patterns, rankings, geography,
routes or times, the agent should execute Python before answering.

Every answer should make the following distinction when relevant:

- **HECHO**: directly observed/calculated.
- **PATRÓN**: descriptive difference.
- **INTERPRETACIÓN**: cautious reading.
- **LIMITACIÓN**: what the available evidence cannot establish.

The agent must not infer neighbourhood-level security from the current municipal security file.

## Studio-only dependency

The local repository cannot run `main.py` without the hackathon Studio runtime. The local
data validation therefore lives separately in `../evaluation/validate_data.py`.

## Demo evidence

Real Studio executions should be saved as screenshots/transcripts under `../demo/`. Never
invent a transcript merely to make the repository look complete.
