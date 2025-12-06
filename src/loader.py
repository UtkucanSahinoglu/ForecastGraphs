import pandas as pd
import zipfile
import glob
import os


def load_shot_data(path="data/NBA_Shots_04_25/NBA_*_Shots.csv.zip"):
    """
    Loads all ZIP-based NBA shot files into a single DataFrame.
    Each ZIP file contains one CSV.
    """

    print("Loading NBA shot data from ZIP files...")

    zip_paths = glob.glob(path)
    if not zip_paths:
        raise FileNotFoundError(f"No ZIP files found with pattern: {path}")

    all_dfs = []

    for zip_path in zip_paths:
        print(f"Reading: {zip_path}")

        with zipfile.ZipFile(zip_path, "r") as z:
            # Take first CSV in the ZIP
            csv_files = [f for f in z.namelist() if f.lower().endswith(".csv")]
            if not csv_files:
                continue
            filename = csv_files[0]
            df = pd.read_csv(z.open(filename))
            all_dfs.append(df)

    if not all_dfs:
        raise ValueError("No CSV data loaded from ZIP files.")

    df = pd.concat(all_dfs, ignore_index=True)
    df["GAME_DATE"] = pd.to_datetime(df["GAME_DATE"])

    print("Data loaded. Total rows:", df.shape[0])
    return df
