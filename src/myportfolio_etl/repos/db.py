# ... cabecera y comentarios previos ...

_engine = None
_SessionLocal = None

def init_engine() -> None:
    # TODO: crear engine y sessionmaker desde la config
    raise NotImplementedError

def get_session():
    # TODO: devolver sesión (y luego un context manager)
    raise NotImplementedError

def ping() -> bool:
    """
    Prueba básica de conectividad a la BD (e.g., SELECT 1).
    TODO:
      - Ejecutar SELECT 1 usando una sesión temporal.
      - Retornar True si OK, False si hay excepción.
    """
    raise NotImplementedError

def test_db_connection(verbose: bool = False) -> bool:
    """
    Atajo explícito para probar conexión a BD.
    TODO:
      - Llamar a ping().
      - Si verbose=True, loggear resultado (éxito/fallo).
    """
    # return ping()
    raise NotImplementedError

def dispose_engine() -> None:
    # TODO: cerrar/dispose del engine
    raise NotImplementedError
