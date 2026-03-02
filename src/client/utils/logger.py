import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ss12000_client")

def log_info(message: str):
    logger.info(message)

def log_error(message: str):
    logger.error(message)
