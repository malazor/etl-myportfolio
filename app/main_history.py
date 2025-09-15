# loader.py
import argparse
import os
from app.yf.client import download_daily_prices_df
from app.yf.normalize import df_to_price_rows
from app.db.connection import test_connection
from app.db.queries import get_start_date, get_symbol_id, upsert_prices_daily_rows
import pandas as pd

from app.core.logging_config import get_logger

# Sub proceso descargar infor de symbol
logger = get_logger("etl_history")
# Proceso Load Symbol
def load_by_symbol(symbol):
    
    # Obtener start_date
    # start_date = get_start_date(symbol)
    start_date = None

    if not start_date:
        start_date = "1990-01-01"
    logger.info(f"Fecha de inicio {start_date}")
    
    df = download_daily_prices_df(symbol, start_date)

    symbol_id = get_symbol_id(symbol)
    logger.info(f"Symbol ID {symbol_id} mapeado con {symbol}")

    if symbol_id:
        df["symbol_id"] = symbol_id
        list_result = df_to_price_rows(symbol_id,df)
        upsert_prices_daily_rows(list_result)

    










# Proceso Load Group
def load_by_group():
    print ("Load by group")

def main():
    parser = argparse.ArgumentParser(description="ETL de símbolos desde Yahoo Finance")
    parser.add_argument(
        "--group",
        nargs="+",
        choices=["index", "tech", "forex", "etc", "etf"],
        help="Grupo(s) de símbolos a cargar",
    )
    parser.add_argument(
        "--symbols",
        type=str,
        help="Lista de símbolos separados por coma (ej: AAPL,MSFT,NVDA)",
    )

    args = parser.parse_args()

    if not (args.group or args.symbols):
         parser.error("Debes especificar al menos --group o --symbols")
    else:
        if args.group:
            load_by_group()
        if args.symbols:
            load_by_symbol(str(args.symbols))

if __name__ == "__main__":
    main()
