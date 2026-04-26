from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

import pandas as pd


BASE_URL = "https://power.larc.nasa.gov/api/temporal/daily/point"
PARAMETERS = [
    "T2M",
    "T2M_MAX",
    "T2M_MIN",
    "T2M_RANGE",
    "PRECTOTCORR",
    "RH2M",
    "WS2M",
    "WS2M_MAX",
    "PS",
    "QV2M",
]

# Representative points (capital cities)
COUNTRIES = {
    "ethiopia": {"lat": 8.9806, "lon": 38.7578},   # Addis Ababa
    "kenya": {"lat": -1.286389, "lon": 36.817223}, # Nairobi
    "sudan": {"lat": 15.5007, "lon": 32.5599},     # Khartoum
    "tanzania": {"lat": -6.1630, "lon": 35.7516},  # Dodoma
    "nigeria": {"lat": 9.0765, "lon": 7.3986},     # Abuja
}


def fetch_country_daily(country: str, lat: float, lon: float, start: str, end: str) -> pd.DataFrame:
    query = {
        "parameters": ",".join(PARAMETERS),
        "community": "RE",
        "latitude": lat,
        "longitude": lon,
        "start": start,
        "end": end,
        "format": "JSON",
    }
    url = f"{BASE_URL}?{urlencode(query)}"

    with urlopen(url, timeout=60) as response:
        payload = json.loads(response.read().decode("utf-8"))

    parameter_data = payload["properties"]["parameter"]
    dates = sorted(next(iter(parameter_data.values())).keys())

    records = []
    for date_key in dates:
        dt = datetime.strptime(date_key, "%Y%m%d")
        row = {
            "YEAR": dt.year,
            "DOY": dt.timetuple().tm_yday,
        }
        for p in PARAMETERS:
            row[p] = parameter_data[p].get(date_key)
        records.append(row)

    return pd.DataFrame(records)


def main() -> None:
    start = "20150101"
    end = "20260331"
    out_dir = Path("data")
    out_dir.mkdir(parents=True, exist_ok=True)

    for country, coords in COUNTRIES.items():
        df = fetch_country_daily(country, coords["lat"], coords["lon"], start, end)
        out_path = out_dir / f"{country}.csv"
        df.to_csv(out_path, index=False)
        print(f"saved {out_path} ({len(df)} rows)")


if __name__ == "__main__":
    main()
