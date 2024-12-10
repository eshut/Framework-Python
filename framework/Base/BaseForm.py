"""Framework: https://github.com/eshut/Framework-Python"""

from selenium.common.exceptions import StaleElementReferenceException

from framework.logger.logger import Logger


class BaseForm(Logger):
    def __init__(self, elem="", logger=__file__):
        super().__init__(logger)
        self.elem = elem

    def isDisplayed(self):
        try:
            self.logger.debug("Checking that element " + str(self.elem) + " is displayed")
            result = self.elem.is_displayed()
            return result
        except StaleElementReferenceException:
            self.logger.debug("Got StaleElementReferenceException")
            return False
