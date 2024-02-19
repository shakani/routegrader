import pandas as pd

def parse(df: pd.DataFrame):
    res = []
    values = df.values()
    values = [(i, j) for i in range(len(values)) for j in range(len(values[0])) if values[i][j]]
    return values