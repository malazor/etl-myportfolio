# app/yf/normalize.py
from typing import List, Dict
import pandas as pd

def df_to_price_rows(symbol_id: int, df: pd.DataFrame) -> List[Dict]:
    """
    Espera df con columnas: date, open, high, low, close, adj_close, volume
    Devuelve lista de dicts listos para INSERT/UPSERT en prices_daily.
    """
    if df is None or df.empty:
        return []

    rows: List[Dict] = []
    for _, r in df.iterrows():
        def nz(v):
            return None if pd.isna(v) else v

        rows.append({
            "symbol_id": symbol_id,
            "date": r["date"],                          # date (YYYY-MM-DD o date)
            "open": nz(r.get("open")),
            "high": nz(r.get("high")),
            "low": nz(r.get("low")),
            "close": nz(r.get("close")),
            "adj_close": nz(r.get("adj_close")),
            "volume": None if pd.isna(r.get("volume")) else int(r.get("volume")),
        })
    return rows
