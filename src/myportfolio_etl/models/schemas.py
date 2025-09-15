"""
models/schemas.py — Esquemas de datos normalizados usados por el ETL.

Responsabilidades:
- Definir las estructuras (tipos y campos) para filas ya limpias:
  * PriceDaily: OHLCV + adj_close por (symbol, date)
  * Dividend: dividendos por (symbol, date)
  * Split: splits por (symbol, date)

Nota: Esqueleto inicial; validaciones y defaults se añadirán luego.
"""

from __future__ import annotations

from datetime import date
from typing import Optional

# TODO: habilitar cuando empecemos validaciones
# from pydantic import BaseModel, Field, field_validator


# Placeholder vacío para que el archivo importe sin romper.
# Cambiaremos a BaseModel cuando implementemos validaciones.
class _Base:  # TODO: reemplazar por `BaseModel`
    pass


class PriceDaily(_Base):
    """
    Fila diaria por símbolo:
      - Clave natural: (symbol, date)
      - Usaremos adj_close para retornos; close como referencia “no ajustada”.
    """
    # TODO: definir como campos reales (cuando usemos pydantic)
    # symbol: str
    # date: date
    # open: Optional[float]
    # high: Optional[float]
    # low: Optional[float]
    # close: Optional[float]
    # adj_close: Optional[float]
    # volume: Optional[int]


class Dividend(_Base):
    """Dividendos por día (importe por acción)."""
    # symbol: str
    # date: date
    # amount: float


class Split(_Base):
    """Splits por día (ratio, p.ej., 2.0 significa 2:1)."""
    # symbol: str
    # date: date
    # ratio: float
