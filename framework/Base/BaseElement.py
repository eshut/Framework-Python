from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from framework.logger.logger import Logger
logger = Logger(__file__).getlog()

from framework.Browser import *
from abc import ABC

WaitTime = jsonGetter.GetJson.getFile(CONFIG, "WaitTime")


class BaseElement(ABC):

    def __init__(self, locatorType, locator, parent_elem=""):
        self.locatorType = locatorType
        self.locator = locator
        self.driver = RunBrowser().driver
        self.elem = parent_elem




    def _find(self, WaitTime = WaitTime):
        '''
        :param WaitTime: time in seconds while the driver will try to find an element
        :return: element
        '''
        if self.elem == "":
            wait = WebDriverWait(self.driver, WaitTime)
        else:
            wait = WebDriverWait(self.elem, WaitTime)

        try:
            logger.info("Waiting for element" + self.locator)
            wait.until(EC.presence_of_element_located((self.locatorType, self.locator)))
            if self.elem == "":
                self.element = self.driver.find_element(self.locatorType, self.locator)
            else:
                self.element = self.elem.find_element(self.locatorType, self.locator)
            return self.element
        except TimeoutException:
            logger.warn("Cannot find such an element!" + self.locator)
            return False




    def _finds(self, WaitTime = WaitTime):
        '''
        :param WaitTime: time in seconds while the driver will try to find an element
        :return: Many elements
        '''
        wait = WebDriverWait(self.driver, WaitTime)
        try:
            logger.info("Waiting for element" + self.locator)
            wait.until(EC.presence_of_element_located((self.locatorType, self.locator)))
        except TimeoutException:
            logger.warn("Cannot find such an element!" + self.locator)
        if self.elem == "":
            self.elements = self.driver.find_elements(self.locatorType, self.locator)
        else:
            self.elements = self.element.find_elements(self.locatorType, self.locator)
        return self.elements

    def click(self):
        '''
        :return: nothing
        Find and click to element
        '''
        self._find()
        logger.info("Trying to click an element")
        self.element.click()
        return self.element


    def move(self):
        '''
        Moves mouse to an element
        '''
        self._find()
        hov = ActionChains(self.driver).move_to_element((self.element)).perform()

