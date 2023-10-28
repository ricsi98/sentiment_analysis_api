import logging
import os


_LOG_FILE = os.getenv(
    "LOG_PATH", 
    os.path.join(os.path.dirname(__file__), "../logs")
)

print(_LOG_FILE)


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(_LOG_FILE)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger