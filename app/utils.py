import pandas as pd


def load_clean_data(countries, data_dir="data"):
    frames = []
    for country in countries:
        path = f"{data_dir}/{country.lower()}_clean.csv"
        df = pd.read_csv(path)
        if "DATE" in df.columns:
            df["DATE"] = pd.to_datetime(df["DATE"])
        elif {"YEAR", "DOY"}.issubset(df.columns):
            df["DATE"] = pd.to_datetime(df["YEAR"] * 1000 + df["DOY"], format="%Y%j")
        else:
            raise ValueError(f"Missing DATE or YEAR/DOY columns in {path}")
        if "Country" not in df.columns:
            df["Country"] = country.title()
        frames.append(df)

    if not frames:
        return pd.DataFrame()

    data = pd.concat(frames, ignore_index=True)
    data["Year"] = data["DATE"].dt.year
    data["Month"] = data["DATE"].dt.month
    return data
