from collections import deque
from tqdm.auto import tqdm

import os.path
import pandas as pd
import sqlite3


def refactor_cocktail_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    # Drop last row
    df.drop(df.index[-1], inplace = True)

    # Remove duplicates
    df.drop_duplicates(inplace = True)

    # Remove na values
    df.dropna(inplace = True)

    # Relabel Columns
    relabel = {
        'Date': 'date',
        'Open': 'open',
        'High': 'high',
        'Low': 'low',
        'Close*': 'close',
        'Adj Close**': 'adj_close',
        'Volume': 'volume'
        }
    
    for old, new in relabel:
        df.rename(columns = {old: new}, inplace = True)

    # Remove "Dividend" rows if exist
    rows_to_remove = deque()
    for index, row in df.iterrows():
        if 'Dividend' in row['open']:
            rows_to_remove.append(index)
    df = df.drop(rows_to_remove)

    # Convert types of columns
    df['date'] = pd.to_datetime(df['date'])
    df['open'] = df['open'].astype('float')
    df['high'] = df['high'].astype('float')
    df['low'] = df['low'].astype('float')
    df['close'] = df['close'].astype('float')
    df['adj_close'] = df['adj_close'].astype('float')
    df['volume'] = df['volume'].astype('int')

    return df


if __name__ == "__main__":
    print("1")