# config.py
import os
from dotenv import load_dotenv

# Cargar archivo .env desde la raíz
load_dotenv()

# === MariaDB ===
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_NAME = os.getenv("DB_NAME", "portfolio")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# DATABASE_URL opcional (si prefieres usar SQLAlchemy Core o un driver directo)
DATABASE_URL = os.getenv("DATABASE_URL", f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# === ETL: símbolos ===
def _parse_symbols(var: str) -> list[str]:
    return [s.strip() for s in os.getenv(var, "").split(",") if s.strip()]

SYMBOLS_INDEX = _parse_symbols("SYMBOLS_INDEX")
SYMBOLS_TECH = _parse_symbols("SYMBOLS_TECH")
SYMBOLS_FOREX = _parse_symbols("SYMBOLS_FOREX")
SYMBOLS_ETC = _parse_symbols("SYMBOLS_ETC")
SYMBOLS_ETF = _parse_symbols("SYMBOLS_ETF")
SYMBOLS_MINSUR = _parse_symbols("SYMBOLS_MINSUR")
SYMBOLS_ALL = _parse_symbols("SYMBOLS_ALL")

# === ETL: parámetros ===
BACKFILL_START = os.getenv("BACKFILL_START", "1990-01-01")
YF_BATCH_SIZE = int(os.getenv("YF_BATCH_SIZE", 25))
WINDOW_BUFFER_DAYS = int(os.getenv("WINDOW_BUFFER_DAYS", 7))
TZ = os.getenv("TZ", "UTC")

# === Logging ===
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_DIR = os.getenv("LOG_DIR", "./logs")
LOG_FILE = os.getenv("LOG_FILE", "etl.log")