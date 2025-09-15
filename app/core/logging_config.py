import logging, os
from datetime import datetime
from pythonjsonlogger import jsonlogger
import config

def get_logger(job_name: str) -> logging.Logger:
    date_str = datetime.today().strftime("%Y-%m-%d")
    log_filename = f"{job_name}_{date_str}.json"   # 👉 extensión JSON
    log_path = os.path.join(config.LOG_DIR, log_filename)

    logger = logging.getLogger(job_name)
    logger.setLevel(getattr(logging, config.LOG_LEVEL, logging.INFO))

    if not logger.handlers:
        h = logging.FileHandler(log_path, encoding="utf-8")
        f = jsonlogger.JsonFormatter(
            "%(asctime)s %(levelname)s %(name)s "
            "%(pathname)s %(funcName)s %(lineno)d "
            "%(thread)d %(threadName)s %(message)s"
        )
        h.setFormatter(f)
        logger.addHandler(h)
        logger.propagate = False

    return logger
