"""
Setup logging for the project.
"""

import logging
from config.constants import LOGGING_CONFIG


def setup_logging():
    """Configure logging for the application."""
    logging.basicConfig(
        level=getattr(logging, LOGGING_CONFIG['level']),
        format=LOGGING_CONFIG['format'],
        filename=LOGGING_CONFIG.get('file'),
        filemode='w'  # Overwrite log file each run
    )
    # Also log to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(LOGGING_CONFIG['format'])
    console_handler.setFormatter(formatter)
    logging.getLogger().addHandler(console_handler)
