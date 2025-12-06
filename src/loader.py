import pandas as pd
import zipfile
import glob


def load_shot_data(path="data/NBA_Shots_04_25/NBA_*_Shots.csv.zip"):
    print("Loading NBA ZIP files...")
    all_dfs = []

    for zip_path in glob.glob(path):
        print(f"Reading: {zip_path}")
        with zipfile.ZipFile(zip_path, "r") as z:
            filename = z.namelist()[0]
            df = pd.read_csv(z.open(filename))
            all_dfs.append(df)

    df = pd.concat(all_dfs, ignore_index=True)
    df["GAME_DATE"] = pd.to_datetime(df["GAME_DATE"])

    print("Data loaded. Rows:", df.shape[0])
    return df
