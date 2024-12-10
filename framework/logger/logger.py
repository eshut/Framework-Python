"""Framework: https://github.com/eshut/Framework-Python"""

import logging
import os
import time
import sys
from dotenv import load_dotenv


load_dotenv()
log_level = os.getenv("LOG_LEVEL")


"""
Usage:
In any class add inheritance like this, so self.logger.info will be available:

class main(Logger):
    def __init__(self, logger=__file__):
        super().__init__(logger)
"""


class Logger:
    def __init__(self, logger):
        self.log_level = log_level
        self.logger = logging.getLogger(os.path.basename(logger))
        self.logger.setLevel(self.log_level)
        if not os.path.exists("logs"):
            os.mkdir("logs")

        log_time = time.strftime('-%Y-%m-%d-%H%M-%S', time.localtime(time.time()))
        log_path = os.getcwd() + "/logs/"
        log_name = log_path + log_time + '.log'

        fh = logging.FileHandler(log_name, encoding="utf-8")
        fh.setLevel(self.log_level)

        ch = logging.StreamHandler()
        ch.setLevel(self.log_level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        sys.excepthook = self.handle_exception

    def handle_exception(self, exc_type, exc_value, exc_traceback):
        """Handles uncaught exceptions"""
        if issubclass(exc_type, KeyboardInterrupt):
            # Call the default hook if KeyboardInterrupt
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        self.logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

    def get_log(self):
        return self.logger

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def set_prefix(self, prefix):
        """Update the prefix dynamically."""
        self.prefix = prefix
        self._update_formatter()

    def _update_formatter(self):
        """Update the formatter with the new prefix."""
        new_format = f'%(asctime)s - %(name)s - %(levelname)s - {self.prefix} - %(message)s'
        self.formatter = logging.Formatter(new_format)

        # Update formatters for all handlers
        for handler in self.logger.handlers:
            handler.setFormatter(self.formatter)
