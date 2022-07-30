import pandas as pd
import os


def converter():
    arquivo = "chess_games.parquet"
    if not os.path.isfile(arquivo):
        csvfile = pd.read_csv("chess_games.csv")
        csvfile.to_parquet("chess_games.parquet", compression="BROTLI")

