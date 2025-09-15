# app/db/models.py

# Representación en Python de la tabla symbols
SYMBOL_FIELDS = [
    "symbol", "name", "short_name", "exchange", "currency",
    "country", "sector", "industry", "website", "quote_type",
    "status"
]

# Representación en Python de la tabla prices_daily
PRICES_DAILY_FIELDS = [
    "symbol_id", "date", "open", "high", "low", "close",
    "adj_close", "volume", "created_at"
]
