import logging
import os
import time

from framework.common import jsonGetter
CONFIG = 'resources/config.json'
BROWSER = jsonGetter.GetJson.getFile(CONFIG,"actualBrowser")


class Logger:
    def __init__(self, logger):
        self.logger = logging.getLogger(os.path.basename(logger))
        self.logger.setLevel(logging.DEBUG)
        if os.path.exists("logs"):
            pass
        else:
            os.mkdir("logs")

        log_time = time.strftime(BROWSER + '-%Y-%m-%d-%H%M-%S', time.localtime(time.time()))
        log_path = os.getcwd() + "/logs/"
        log_name = log_path + log_time + '.log'

        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

