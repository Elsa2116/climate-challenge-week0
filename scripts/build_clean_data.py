import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import zscore


WEATHER_COLS = [
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

ZSCORE_COLS = ["T2M", "T2M_MAX", "T2M_MIN", "PRECTOTCORR", "RH2M", "WS2M", "WS2M_MAX"]


def clean_country(country: str, data_dir: Path) -> pd.DataFrame:
    source = data_dir / f"{country}.csv"
    if not source.exists():
        raise FileNotFoundError(f"Missing input file: {source}")

    df = pd.read_csv(source)
    df["Country"] = country.title()
    df["DATE"] = pd.to_datetime(df["YEAR"] * 1000 + df["DOY"], format="%Y%j")
    df["Month"] = df["DATE"].dt.month

    df = df.replace(-999, np.nan)
    duplicates = int(df.duplicated().sum())
    df = df.drop_duplicates()

    z_frame = df[ZSCORE_COLS].copy().fillna(df[ZSCORE_COLS].median(numeric_only=True))
    z_abs = np.abs(zscore(z_frame, nan_policy="omit"))
    outlier_count = int((z_abs > 3).any(axis=1).sum())

    row_missing_ratio = df.isna().mean(axis=1)
    df = df[row_missing_ratio <= 0.30].copy()

    for col in WEATHER_COLS:
        if col in df.columns:
            df[col] = df[col].ffill()

    out_path = data_dir / f"{country}_clean.csv"
    df.to_csv(out_path, index=False)

    print(f"[{country}] duplicates_removed={duplicates}, outliers_flagged={outlier_count}, rows_after_clean={len(df)}")
    print(f"[{country}] saved -> {out_path}")
    return df


def main() -> None:
    parser = argparse.ArgumentParser(description="Build cleaned climate CSVs for all countries.")
    parser.add_argument("--data-dir", default="data", help="Directory containing raw country CSVs")
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    countries = ["ethiopia", "kenya", "sudan", "tanzania", "nigeria"]

    for country in countries:
        clean_country(country, data_dir)


if __name__ == "__main__":
    main()
