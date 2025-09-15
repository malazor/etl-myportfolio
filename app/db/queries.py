# app/db/queries.py
from typing import Dict, List
from app.db.connection import get_connection
from app.core.logging_config import get_logger

# Espera un dict YA normalizado a los nombres de columnas de tu tabla `symbols`
# Ej: {
#   "symbol": "AAPL", "name": "...", "short_name": "...", "exchange": "...",
#   "currency": "USD", "country": "US", "sector": "...", "industry": "...",
#   "website": "...", "quote_type": "EQUITY", "status": "ACTIVE",
#   "last_yf_sync": "2025-09-03 10:00:00"
# }

logger = get_logger("etl_history")

def get_start_date(symbol: str) -> str:
    payload = {
        "symbol" : symbol
    }

    sql = """
        SELECT max(date) FROM prices_daily WHERE symbol_id = %(symbol)s;
    """

    conn = get_connection()
    logger.info("Conexcion establecida")
    try:
        with conn.cursor() as cur:
            logger.info(f"Ejecutando consulta para symbol: {symbol}")
            row = cur.fetchone()
            if not row or row[0] is None:
                logger.info("No hay registros previos para este símbolo")
                return None

            max_date = row[0]
            result = max_date.strftime("%Y-%m-%d")
            logger.info(f"Última fecha encontrada: {result}")
            return result
    finally:
        logger.info("Conexion cerrada")
        conn.close()


def upsert_prices_daily_rows(rows: List[Dict], batch_size: int = 1000) -> int:
    """
    Inserta/actualiza filas en prices_daily.
    Devuelve la cantidad de filas procesadas.
    """
    if not rows:
        return 0

    sql = """
    INSERT INTO prices_daily
      (symbol_id, `date`, `open`, `high`, `low`, `close`, adj_close, volume)
    VALUES
      (%(symbol_id)s, %(date)s, %(open)s, %(high)s, %(low)s, %(close)s, %(adj_close)s, %(volume)s)
    ON DUPLICATE KEY UPDATE
      `open` = VALUES(`open`),
      `high` = VALUES(`high`),
      `low`  = VALUES(`low`),
      `close`= VALUES(`close`),
      adj_close = VALUES(adj_close),
      volume = VALUES(volume),
      updated_at = NOW();
    """

    conn = get_connection()
    logger.info("Conexcion establecida")

    try:
        with conn.cursor() as cur:
            for i in range(0, len(rows), batch_size):
                logger.info(f"Insertando fila: {rows[i]}")
                cur.executemany(sql, rows[i:i+batch_size])
        conn.commit()
        logger.info(f"Commit realizado")
        return len(rows)
    finally:
        logger.info(f"Conexion finalizada")
        conn.close()


def upsert_symbol(data: Dict) -> None:
    payload = {
        "symbol": data.get("symbol"),
        "name": data.get("longName"),
        "market_tz": data.get("market"),
        "short_name": data.get("shortName"),
        "exchange": data.get("fullExchangeName"),
        "currency": data.get("currency"),
        "country": data.get("country"),
        "sector": data.get("sector"),
        "industry": data.get("industry"),
        "website": data.get("website"),
        "quote_type": data.get("quoteType"),
        "status": data.get("status")
    }

    sql = """
    INSERT INTO symbols (
        symbol, name, short_name, exchange, currency, country,
        sector, industry, website, quote_type, status, market_tz
    ) VALUES (
        %(symbol)s, %(name)s, %(short_name)s, %(exchange)s, %(currency)s, %(country)s,
        %(sector)s, %(industry)s, %(website)s, %(quote_type)s, %(status)s, %(market_tz)s
    )
    ON DUPLICATE KEY UPDATE
        name = VALUES(name),
        short_name = VALUES(short_name),
        exchange = VALUES(exchange),
        currency = VALUES(currency),
        country = VALUES(country),
        sector = VALUES(sector),
        industry = VALUES(industry),
        website = VALUES(website),
        quote_type = VALUES(quote_type),
        status = VALUES(status),
        market_tz = VALUES(market_tz),
        updated_at = NOW();
    """

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, payload)
        conn.commit()
    finally:
        conn.close()

def get_symbol_id(symbol: str) -> int | None:
    sql = """
        SELECT id FROM symbols WHERE symbol = %(symbol)s;
    """
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, {"symbol": symbol})
            row = cur.fetchone()
            return row["id"] if row else None
    finally:
        conn.close()
    