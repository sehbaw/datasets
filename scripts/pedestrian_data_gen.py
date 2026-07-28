import random
import uuid
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

# -----------------------------
# CONFIG
# -----------------------------
NUM_ROWS = 2000
START_DATE = datetime(2025, 6, 1)
DAYS = 21

# DC Neighborhoods with bounding boxes (approximate)
NEIGHBORHOODS = {
    "Dupont Circle": ((38.905, 38.915), (-77.050, -77.035)),
    "Georgetown": ((38.900, 38.910), (-77.070, -77.050)),
    "Capitol Hill": ((38.880, 38.895), (-77.020, -76.990)),
    "Navy Yard": ((38.870, 38.880), (-77.015, -76.995)),
    "Adams Morgan": ((38.915, 38.925), (-77.050, -77.030)),
    "Columbia Heights": ((38.920, 38.935), (-77.045, -77.025)),
    "NoMa": ((38.900, 38.915), (-77.010, -76.990)),
    "Downtown": ((38.895, 38.905), (-77.040, -77.020)),
    "National Mall": ((38.885, 38.895), (-77.035, -77.010)),
}

# Metro stations
STATIONS = [
    ("ST001", "Dupont Circle", "Red"),
    ("ST002", "Metro Center", "Red"),
    ("ST003", "Gallery Place", "Green"),
    ("ST004", "Smithsonian", "Blue"),
    ("ST005", "L’Enfant Plaza", "Yellow"),
    ("ST006", "Navy Yard–Ballpark", "Green"),
    ("ST007", "Capitol South", "Blue"),
    ("ST008", "Foggy Bottom", "Orange"),
]

LOCATION_TYPES = ["Intersection", "Sidewalk", "Park", "Transit Hub"]
WEATHER = ["Clear", "Cloudy", "Rain"]
EVENT_TYPES = ["None", "Festival", "Sports", "Political"]

# -----------------------------
# HELPERS
# -----------------------------
def random_timestamp():
    day_offset = random.randint(0, DAYS - 1)
    base = START_DATE + timedelta(days=day_offset)
    hour = random.choices(
        population=[8, 12, 17, 21],
        weights=[0.3, 0.2, 0.3, 0.2]
    )[0]
    minute = random.randint(0, 59)
    return base.replace(hour=hour, minute=minute)

def get_time_of_day(hour):
    if 6 <= hour < 11:
        return "Morning"
    elif 11 <= hour < 16:
        return "Midday"
    elif 16 <= hour < 20:
        return "Evening"
    else:
        return "Night"

def density_from_count(count):
    if count < 80:
        return "Low"
    elif count < 180:
        return "Medium"
    elif count < 300:
        return "High"
    return "Congested"

def speed_from_density(density):
    return {
        "Low": round(random.uniform(1.3, 1.6), 2),
        "Medium": round(random.uniform(1.1, 1.4), 2),
        "High": round(random.uniform(0.9, 1.2), 2),
        "Congested": round(random.uniform(0.6, 1.0), 2),
    }[density]

def pick_station():
    return random.choice(STATIONS)

def generate_point(bounds):
    lat = round(random.uniform(*bounds[0]), 6)
    lon = round(random.uniform(*bounds[1]), 6)
    return lat, lon

# -----------------------------
# GENERATION
# -----------------------------
rows = []

for i in range(NUM_ROWS):
    record_id = f"REC-{i+1:06d}"

    neighborhood = random.choice(list(NEIGHBORHOODS.keys()))
    bounds = NEIGHBORHOODS[neighborhood]
    lat, lon = generate_point(bounds)

    timestamp = random_timestamp()
    time_of_day = get_time_of_day(timestamp.hour)
    day_type = "Weekend" if timestamp.weekday() >= 5 else "Weekday"

    location_type = random.choice(LOCATION_TYPES)

    station_id, station_name, line = pick_station()

    distance = random.randint(50, 1000)

    # Pedestrian count influenced by distance + time
    base_count = np.random.normal(150, 60)
    if distance < 200:
        base_count *= 1.5
    if location_type == "Transit Hub":
        base_count *= 1.4
    if time_of_day in ["Morning", "Evening"]:
        base_count *= 1.3

    pedestrian_count = max(10, int(base_count))

    density = density_from_count(pedestrian_count)
    speed = speed_from_density(density)

    weather = random.choices(WEATHER, weights=[0.6, 0.25, 0.15])[0]
    temp = random.randint(60, 95)

    event_flag = random.random() < 0.15
    event_type = random.choice(EVENT_TYPES) if event_flag else "None"

    transit_activity = (
        "High" if distance < 200 else
        "Medium" if distance < 500 else
        "Low"
    )

    estimated_boardings = int(pedestrian_count * random.uniform(0.2, 0.6))

    rows.append({
        "record_id": record_id,
        "timestamp": timestamp.isoformat(),
        "neighborhood": neighborhood,
        "zone_id": f"{neighborhood[:3].upper()}-{random.randint(1,3):02d}",
        "latitude": lat,
        "longitude": lon,
        "location_type": location_type,
        "pedestrian_count": pedestrian_count,
        "avg_speed_mps": speed,
        "density_level": density,
        "direction_flow": random.choice(["N-S", "E-W", "Mixed"]),
        "nearest_station": station_name,
        "station_id": station_id,
        "station_line": line,
        "distance_to_station_m": distance,
        "transit_activity_level": transit_activity,
        "estimated_boardings": estimated_boardings,
        "weather": weather,
        "temperature_f": temp,
        "time_of_day": time_of_day,
        "day_type": day_type,
        "event_flag": event_flag,
        "event_type": event_type
    })



#export !>!>!>
df = pd.DataFrame(rows)
df.to_csv("pedestrian_flows_dc.csv", index=False)

print("✅ Dataset generated: pedestrian_flows_dc.csv")