"""
-> Create logger (child of root)
-> Define log format (time name level message)
-> Save logs to respective files
"""


import logging
from logging.handlers import TimedRotatingFileHandler

FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")


def get_file_handler(LOG_FILE):
    """
    -> Use file format
    -> Transfer logs to new files
    Return handler
    """
    file_handler = TimedRotatingFileHandler(LOG_FILE, when="midnight")
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(LOG_FILE, logger_name):
    """
    return the new logger (with min level of logging as Debug)
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler(LOG_FILE))
    logger.propagate = False
    return logger
