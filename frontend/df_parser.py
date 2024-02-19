import pandas as pd

def parse(df: pd.DataFrame):
    res = []
    values = df.values
    """
    (0, 0) -> A18; (18, A)
    (17, 10) -> K1; (1, K)
    """
    values = [chr(ord('A') + j) + f"{18 - i}" for i in range(len(values)) for j in range(len(values[0])) if values[i][j]]
    return values