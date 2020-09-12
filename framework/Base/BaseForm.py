from framework.Base import BaseElement
from selenium.common.exceptions import StaleElementReferenceException

from framework.logger.logger import Logger
logger = Logger(__file__).getlog()


class BaseForm():
    def __init__(self, elem= ""):
        self.elem = elem

    def isDisplayed(self):
        try:
            logger.info("Checking that element " + str(self.elem) + " is displayed")
            result = self.elem.is_displayed()
            return result
        except StaleElementReferenceException:
            logger.info("Got StaleElementReferenceException")
            return False