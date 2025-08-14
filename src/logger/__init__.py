import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime

log_dir = 'logs'
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
max_log_size = 5 * 1024 * 1024  # 5MB
backup_count = 3

# log file path making
log_dir_path = os.path.join(from_root(), log_dir)
os.makedirs(log_dir_path, exist_ok=True)
log_file_path = os.path.join(log_dir_path, log_file)

def configure_logger():
    """Apply logging with a rotating file handler and a console handler"""

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    # Define the formatter
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # File handler (rotating)
    file_handler = RotatingFileHandler(
        log_file_path, maxBytes=max_log_size, backupCount=backup_count
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Configure the logger
configure_logger()
