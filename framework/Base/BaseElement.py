from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from framework.logger.logger import Logger

logger = Logger(__file__).get_log()

from framework.Browser import *
from abc import ABC

wait_time = jsonGetter.GetJson.get_file(CONFIG, "WaitTime")


class BaseElement(ABC):

    def __init__(self, locator_type, locator, parent_elem=None):
        self.locator_type = locator_type
        self.locator = locator
        self.driver = RunBrowser().driver
        self.elem = parent_elem

    def find(self, wait_time=wait_time):
        '''
        :param WaitTime: time in seconds while the driver will try to find an element
        :return: element
        '''
        if self.elem == None:
            wait = WebDriverWait(self.driver, wait_time)
        else:
            wait = WebDriverWait(self.elem, wait_time)

        try:
            logger.info("Waiting for element" + self.locator)
            wait.until(EC.visibility_of_element_located((self.locator_type, self.locator)))
            if self.elem == None:
                self.element = self.driver.find_element(self.locator_type, self.locator)
            else:
                self.element = self.elem.find_element(self.locator_type, self.locator)
            return self.element
        except TimeoutException:
            logger.warn("Cannot find such an element!" + self.locator)
            return False

    def finds(self, wait_time=wait_time):
        '''
        :param WaitTime: time in seconds while the driver will try to find an element
        :return: Many elements
        '''
        if self.elem == None:
            wait = WebDriverWait(self.driver, wait_time)
        else:
            wait = WebDriverWait(self.elem, wait_time)

        try:
            logger.info("Waiting for element" + self.locator)
            wait.until(EC.visibility_of_all_elements_located((self.locator_type, self.locator)))
            if self.elem == None:
                self.elements = self.driver.find_elements(self.locator_type, self.locator)
            else:
                self.elements = self.element.find_elements(self.locator_type, self.locator)
            return self.elements
        except TimeoutException:
            logger.warn("Cannot find such an element!" + self.locator)
            return False

    def click(self):
        '''
        :return: nothing
        Find and click to element
        '''
        self.find()
        logger.info("Trying to click an element")
        self.element.click()
        return self.element

    def move(self):
        '''
        Moves mouse to an element
        '''
        self.find()
        hov = ActionChains(self.driver).move_to_element((self.element)).perform()

    def screenshot_elem(self, save_path):
        with open(save_path, 'wb') as file:
            file.write(self.element.screenshot_as_png)

    def screenshot(self, save_path):
        self.driver.get_screenshot_as_file(save_path)
