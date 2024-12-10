"""Framework: https://github.com/eshut/Framework-Python"""

import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FS_options

from framework.common import jsonGetter

load_dotenv()
log_level = os.getenv("LOG_LEVEL")
localization = os.getenv("LOCALIZATION")
browser = os.getenv("BROWSER")
save_dir = os.getenv("SAVE_DIR")
firefox_location = os.getenv("FIREFOX_LOCATION")


BROWSERS = ["ChromeBrowser", "FireFoxBrowser"]


class ChromeBrowser():
    def run_browser(self, locale="en"):
        preferences = {"download.default_directory": save_dir, "safebrowsing.enabled": "false"}
        options = webdriver.ChromeOptions()
        options.add_argument("--lang={}".format(locale))
        options.add_experimental_option("prefs", preferences)

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.set_page_load_timeout(20)
        driver.maximize_window()
        return (driver)


class FireFoxBrowser():
    def run_browser(self, locale="en"):
        options = FS_options()
        options.set_preference("intl.accept_languages", locale)
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", save_dir)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.helperApps.alwaysAsk.force", False)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        options.binary_location = firefox_location
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        driver.maximize_window()
        return (driver)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def clear(cls):
        try:
            del Singleton._instances[cls]
        except KeyError:
            pass


class BrowserFactory(metaclass=Singleton):
    @staticmethod
    def get_browser(browsertype):

        try:
            if browsertype == BROWSERS.index("FireFoxBrowser"):
                driver = FireFoxBrowser().run_browser(localization)
                return driver
            elif browsertype == BROWSERS.index("ChromeBrowser"):
                driver = ChromeBrowser().run_browser(localization)
                return driver
            raise AssertionError("Browser not found")
        except AssertionError as _e:
            print(_e)


class RunBrowser(metaclass=Singleton):
    def __init__(self):
        if browser in BROWSERS:
            browser_index = BROWSERS.index(browser)
            self.driver = BrowserFactory.get_browser(browser_index)
        else:
            raise Exception("No Such Browser")

