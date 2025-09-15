from app.core.logging_config import get_logger

logger = get_logger(__name__)


logger = get_logger("test_logger")

logger.debug("Mensaje DEBUG")
logger.info("Mensaje INFO")
logger.warning("Mensaje WARNING")
logger.error("Mensaje ERROR")
logger.critical("Mensaje CRITICAL")
