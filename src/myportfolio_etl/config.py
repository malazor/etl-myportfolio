"""
Config module for the ETL (myportfolio_etl).

Responsabilidades:
- Centralizar lectura de variables de entorno / .env.
- Aplicar defaults y validaciones mínimas.
- Exponer un objeto de configuración para el resto del paquete.

Nota: Aún sin implementación. Iremos habilitando secciones paso a paso.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import List, Optional

# TODO: cuando implementemos:
# from dotenv import load_dotenv
# import os


@dataclass
class ETLConfig:
    """Estructura de configuración normalizada (sin lógica)."""

    # --- Base de datos ---
    database_url: str                 # mysql+pymysql://user:pass@host:port/db
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    # db_password: str  # no exponer en logs; decidir si se mantiene aquí o solo en database_url

    # --- ETL ---
    tickers: List[str]                # lista normalizada (p.ej., ["AAPL","MSFT"])
    yf_batch_size: int                # p.ej., 25
    window_buffer_days: int           # p.ej., 7
    backfill_start: date              # p.ej., 1990-01-01
    tz: str                           # p.ej., "America/Lima"

    # --- Logging ---
    log_level: str                    # "INFO", "DEBUG", etc.
    log_dir: Path                     # ruta a carpeta de logs

    # --- Metadatos internos ---
    source_env_path: Optional[Path] = None   # .env usado (local o /etc/myportfolio/etl.env)


# Singleton (perezoso): se inicializará con load_config() cuando implementemos
_config: Optional[ETLConfig] = None


def load_config() -> ETLConfig:
    """
    Construye ETLConfig a partir de variables de entorno.

    TODO (cuando implementemos):
      1) Cargar .env desde DOTENV_PATH (si existe) o ./.env.
      2) Precedencia: OS env > .env > defaults.
      3) Si no hay DATABASE_URL, construirla con DB_HOST/PORT/NAME/USER/PASSWORD.
      4) Parsear y validar tipos (enteros, fecha BACKFILL_START).
      5) Normalizar TICKERS (upper/strip) y asegurar no vacía.
      6) Devolver instancia ETLConfig.
    """
    raise NotImplementedError("Implementar load_config() en la siguiente etapa.")


def get_config() -> ETLConfig:
    """
    Acceso perezoso al singleton de configuración.

    TODO (cuando implementemos):
      - Si _config es None, llamar a load_config().
      - Retornar _config.
    """
    global _config
    if _config is None:
        # _config = load_config()
        raise RuntimeError("Config aún no inicializado (pendiente de implementación).")
    return _config
