import logging
import sys
from logging.handlers import TimedRotatingFileHandler
from .config import ConfigManager

FORMATTER = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
LOG_FILE = "my_app.log"


class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    grey = "\u001b[38;21m"
    yellow = "\u001b[33;21m"
    red = "\u001b[31;21m"
    white = "\u001b[37;1m"
    bright_blue = "\u001b[34;1m"
    bold_red = "\u001b[31;1m"

    reset = "\u001b[0m"
    format_text = (
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    )

    FORMATS = {
        logging.DEBUG: bright_blue + format_text + reset,
        logging.INFO: white + format_text + reset,
        logging.WARNING: yellow + format_text + reset,
        logging.ERROR: red + format_text + reset,
        logging.CRITICAL: bold_red + format_text + reset,
    }

    def format(self, record):
        # print(f"Record: {record.levelno}")
        # print("\u001b[31mHelloWorld")

        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_console_handler():
    console_handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(CustomFormatter())
    return console_handler


def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE, when="midnight")
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name):
    return init_log(logger_name)


def init_log(logger_name):
    logger = logging.getLogger(logger_name)

    cm = ConfigManager()
    if cm.verbose >= 2:
        log_level = logging.DEBUG
    elif cm.verbose == 1:
        log_level = logging.WARNING
    else:
        log_level = logging.INFO

    logger.setLevel(log_level)  # better to have too much log than not enough

    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False
    return logger
