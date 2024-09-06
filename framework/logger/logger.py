import logging
import os
import time
import sys

from framework.common import jsonGetter

CONFIG = 'resources/config.json'
BROWSER = jsonGetter.GetJson.get_file(CONFIG, "actualBrowser")


class Logger:
    def __init__(self, logger):
        self.log_level = constants.LOG_LEVEL
        self.logger = logging.getLogger(os.path.basename(logger))
        self.logger.setLevel(self.log_level)
        if not os.path.exists("logs"):
            os.mkdir("logs")

        log_time = time.strftime(TOKEN_LOG + '-%Y-%m-%d-%H%M-%S', time.localtime(time.time()))
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

