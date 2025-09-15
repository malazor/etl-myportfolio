import yfinance as yf
import pandas as pd
from app.core.logging_config import get_logger



def download_symbol_info(symbol: str) -> dict:
    ticker = yf.Ticker(symbol)
    info = ticker.info or {}
    return {
        "symbol": symbol,  # confiamos en el input
        "longName": info.get("longName"),
        "market": info.get("market"),
        "shortName": info.get("shortName"),
        "fullExchangeName": info.get("fullExchangeName"),
        "currency": info.get("currency"),
        "country": info.get("country"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "website": info.get("website"),
        "quoteType": info.get("quoteType"),
        "status": "active"
    }

def download_daily_prices_df(symbol: str, start: str) -> pd.DataFrame:
    """
    Devuelve un DataFrame con columnas:
    date, open, high, low, close, adj_close, volume
    """
    logger = get_logger("etl_history")
    logger.info("Inicio descarga YF")
    df = yf.Ticker(symbol).history(interval="1d", start=start, auto_adjust=False)
    logger.info("DataFrame descargado")


    if df.empty:
        logger.info("DataFrame vacio")
        return pd.DataFrame(columns=["date","open","high","low","close","adj_close","volume"])

    df = df.reset_index()  # Index -> 'Date'
    df = df.rename(columns={
        "Date": "date",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Adj Close": "adj_close",
        "Volume": "volume",
    })
    # Normaliza tipo de fecha a date (YYYY-MM-DD)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    logger.info("DataFrame devuelto")

    return df[["date","open","high","low","close","adj_close","volume"]]