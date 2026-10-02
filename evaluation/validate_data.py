from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

def fail(msg):
    raise AssertionError(msg)

# Population
pop = pd.read_csv(
    DATA / "poblacion_barrio_2025_2.csv",
    sep=";",
    skiprows=1,
    header=1,
    dtype=str,
    engine="python",
    keep_default_na=False,
)
names = pop.iloc[:, 0].astype(str)
matches = names[names.eq("Donostia / San Sebastián")].index
if len(matches) != 1:
    fail(f"Expected one Donostia row, found {len(matches)}")
i = matches[0]
donostia = pop.iloc[i:i+19].copy()
if len(donostia) != 19:
    fail("Expected municipal row + 18 neighbourhood rows")

def parse_people(value):
    value = str(value).strip()
    if not value:
        return None
    return int(value.replace(".", "").replace(",", "."))

municipal = parse_people(donostia.iloc[0]["Mujeres"])
neighbourhoods = donostia.iloc[1:].copy()
neighbourhoods["mujeres_num"] = neighbourhoods["Mujeres"].map(parse_people)
if len(neighbourhoods) != 18:
    fail("Expected 18 neighbourhoods")
if neighbourhoods["mujeres_num"].sum() != municipal:
    fail("Neighbourhood female population does not reconcile with municipal total")
if municipal != 96814:
    fail(f"Unexpected municipal female population: {municipal}")

# Spatial mapping
mapping = pd.read_csv(DATA / "gautxori_paradas_barrios.csv", dtype=str)
counts = mapping["asignacion"].value_counts().to_dict()
if len(mapping) != 248:
    fail(f"Unexpected mapping rows: {len(mapping)}")
if counts.get("DENTRO_POLIGONO", 0) != 245:
    fail(f"Unexpected mapped stops: {counts}")
if counts.get("SIN_ASIGNAR_EN_GEOJSON", 0) != 3:
    fail(f"Unexpected unassigned stops: {counts}")


# Demography (2019 source)
dem = pd.read_csv(DATA / "demografiapiramideedadbarrio2.csv", dtype=str)
if len(dem) != 140:
    fail(f"Unexpected demographic rows: {len(dem)}")
if set(dem["Urtea"].astype(str)) != {"2019"}:
    fail(f"Unexpected demographic years: {sorted(set(dem['Urtea'].astype(str)))}")
if dem["Auzoa"].nunique() != 7:
    fail(f"Unexpected demographic neighbourhood count: {dem['Auzoa'].nunique()}")

# GeoJSON
import json
with (DATA / "barrios_donostia.json").open(encoding="utf-8-sig") as f:
    gj = json.load(f)
if gj.get("type") != "FeatureCollection":
    fail(f"Unexpected GeoJSON type: {gj.get('type')}")
features = gj.get("features", [])
if len(features) != 20:
    fail(f"Unexpected GeoJSON feature count: {len(features)}")
if not all((feat.get("geometry") or {}).get("type") == "Polygon" for feat in features):
    fail("GeoJSON contains a geometry that is not Polygon")

# GTFS
stop_times = pd.read_csv(DATA / "stop_times2.txt", dtype=str)
trips = pd.read_csv(DATA / "trips2.txt", dtype=str)
routes = pd.read_csv(DATA / "routes2.txt", dtype=str)
if len(stop_times) != 5716:
    fail(f"Unexpected stop_times rows: {len(stop_times)}")
if len(trips) != 303:
    fail(f"Unexpected trips rows: {len(trips)}")
if len(routes) != 14:
    fail(f"Unexpected routes rows: {len(routes)}")

hours = stop_times["departure_time"].astype(str).str.split(":").str[0].astype(int)
night = hours.between(1, 3)
if int(night.sum()) != 4230:
    fail(f"Unexpected 01:00-03:59 count: {int(night.sum())}")

assigned = mapping[mapping["asignacion"].eq("DENTRO_POLIGONO")][["stop_id", "barrio"]]
assigned_times = stop_times.merge(assigned, on="stop_id", how="inner")
if len(assigned_times) != 5624:
    fail(f"Unexpected assigned stop_times rows: {len(assigned_times)}")
assigned_hours = assigned_times["departure_time"].astype(str).str.split(":").str[0].astype(int)
if int(assigned_hours.between(1, 3).sum()) != 4161:
    fail(f"Unexpected assigned night count: {int(assigned_hours.between(1, 3).sum())}")

# Security
security = pd.read_csv(DATA / "seguridad_donostia_2025_2026_2.csv", dtype=str)
row = security[security["tipo_infraccion"].str.strip().str.upper().eq("TOTAL INFRACCIONES PENALES")]
if len(row) != 1:
    fail(f"Expected one municipal total row, found {len(row)}")
row = row.iloc[0]
if int(row["total_2025"]) != 8832 or int(row["total_2026"]) != 8321:
    fail("Security totals do not match published baseline")

print("MATILDA validation: PASS")
print(f"- Women in 18 neighbourhoods: {municipal:,}")
print("- Mapped stops: 245 / 248")
print("- stop_times: 5,716")
print("- Assigned stop_times: 5,624")
print("- stop_times 01:00-03:59: 4,230")
print("- Assigned stop_times 01:00-03:59: 4,161")
print("- Security total: 8,832 -> 8,321")
