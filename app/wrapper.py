import subprocess
import config
import time
from app.core.logging_config import get_logger

# lista de símbolos
symbols = config.SYMBOLS_ALL
logger = get_logger("etl_history")
logger.info("Inicio del job de carga histórica")

for symbol in symbols:
    logger.info(f"Ejecutando main_symbol.py con {symbol}...")
    subprocess.run(["python","-m", "app.main_symbol", "--symbols", symbol])
    time.sleep(2)

for symbol in symbols:
    logger.info(f"Ejecutando main_history.py con {symbol}...")
    subprocess.run(["python","-m", "app.main_history", "--symbols", symbol])
    time.sleep(2)

logger.info("Fin del job de carga histórica")
