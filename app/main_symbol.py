# loader.py
import argparse
import os
from app.yf.client import download_symbol_info
from app.db.connection import test_connection
from app.db.queries import upsert_symbol
import pandas as pd

# Sub proceso descargar infor de symbol

# Proceso Load Symbol
def load_by_symbol(symbol):
    # Descargar info del symbol
    symbol_info = download_symbol_info(symbol)
    upsert_symbol(symbol_info)






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
