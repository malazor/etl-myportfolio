"""
logging_setup.py — Configuración centralizada de logging para el ETL.

Responsabilidades:
- Crear un logger consistente para todo el paquete.
- Soportar salida a consola y a archivo (LOG_DIR), idealmente en JSON.
- Respetar LOG_LEVEL de la config.

Nota: Esqueleto sin implementación. Iremos activando secciones paso a paso.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

# TODO (cuando implementemos):
# from pythonjsonlogger import jsonlogger
# from .config import get_config


LOGGER_NAME = "myportfolio_etl"


def setup_logging(force: bool = False) -> logging.Logger:
    """
    Prepara el logger de la aplicación.

    TODO (cuando implementemos):
      1) Obtener config (LOG_LEVEL, LOG_DIR).
      2) Crear carpeta LOG_DIR si no existe.
      3) Construir formatter (JSON preferible; fallback a texto).
      4) Añadir handlers:
         - StreamHandler (consola)
         - FileHandler o RotatingFileHandler (logs/app.log)
      5) Establecer nivel del logger raíz o del LOGGER_NAME.
      6) Proteger contra doble-inicialización (a menos que force=True).

    Retorna:
      logging.Logger configurado.
    """
    raise NotImplementedError("Implementar setup_logging() en la siguiente etapa.")


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Obtiene un logger hijo del principal para módulos específicos.

    TODO (cuando implementemos):
      - Asegurar que setup_logging() haya corrido previamente.
      - Retornar logging.getLogger(f\"{LOGGER_NAME}.{name}\") si name.
      - Si name es None, retornar el logger principal.

    Ejemplo de uso (en otros módulos):
      logger = get_logger(__name__)
      logger.info(\"Descargando ventana\", extra={\"symbol\": \"AAPL\"})
    """
    raise NotImplementedError("Implementar get_logger() después de setup_logging().")
