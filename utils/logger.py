# utils/logger.py

from loguru import logger
import sys
import os
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logger
logger.remove()  # Remove the default logger
logger.add(sys.stdout, level="INFO", format="<green>{time}</green> <level>{message}</level>")
logger.add("logs/multi_agent_system.log", rotation="1 MB", retention="10 days", level="DEBUG", format="{time} {level} {message}")

def measure_response_time(func):
    """Decorator to measure response time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        logger.info(f"Function {func.__name__} executed in {elapsed_time:.4f} seconds")
        return result
    return wrapper