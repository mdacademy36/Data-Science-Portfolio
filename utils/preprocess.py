import pandas as pd
import numpy as np
from datetime import datetime

# ==================================================
# CLEAN + FEATURE ENGINEERING BASED ON COLAB PIPELINE
# ==================================================
def clean_input(df):

# ======================
# CAR AGE FEATURE
# ======================
    if "Prod. year" in df.columns:

        current_year = datetime.now().year

        df["Prod. year"] = pd.to_numeric(
            df["Prod. year"],
            errors="coerce"
        )

        df["car_age"] = current_year - df["Prod. year"]

        # Optional safety: jika ada tahun > current_year
        df.loc[df["car_age"] < 0, "car_age"] = np.nan

    # ======================
    # LEVY CLEANING
    # ======================
    if "Levy" in df.columns:
        df["Levy"] = df["Levy"].replace("-", np.nan)
        df["Levy_available"] = df["Levy"].notna().astype(int)
        df["Levy"] = pd.to_numeric(df["Levy"], errors="coerce")

    # ======================
    # MILEAGE CLEANING
    # ======================
    if "Mileage" in df.columns:
        df["Mileage"] = df["Mileage"].str.replace("km", "", regex=False)
        df["Mileage"] = df["Mileage"].str.strip()
        df["Mileage"] = pd.to_numeric(df["Mileage"], errors="coerce")

        df.loc[
            (df["Mileage"] == 0) | (df["Mileage"] >= 99999),
            "Mileage"
        ] = np.nan

    # ======================
    # ENGINE VOLUME + TURBO FLAG
    # ======================
    if "Engine volume" in df.columns:

        df["Turbo"] = df["Engine volume"].str.contains(
            "Turbo",
            case=False,
            na=False
        ).astype(int)

        df["Engine volume"] = (
            df["Engine volume"]
            .str.replace("Turbo", "", regex=False)
            .str.strip()
        )

        df["Engine volume"] = pd.to_numeric(
            df["Engine volume"],
            errors="coerce"
        )

    # ======================
    # DOORS CLEANING
    # ======================
    if "Doors" in df.columns:

        doors_map = {
            "04-May": 5,
            "02-Mar": 3
        }

        df["Doors"] = df["Doors"].replace(doors_map)
        df["Doors"] = pd.to_numeric(df["Doors"], errors="coerce")

    return df
