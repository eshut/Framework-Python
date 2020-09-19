from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from framework.common import jsonGetter

CONFIG = 'resources/config.json'
BROWSERS = ["ChromeBrowser", "FireFoxBrowser"]
LOCAL = jsonGetter.GetJson.get_file(CONFIG, "LOCAL")


class ChromeBrowser():
    def run_browser(self, locale="en"):
        DIR = jsonGetter.GetJson.get_file(CONFIG, "DIR")
        preferences = {"download.default_directory": DIR, "safebrowsing.enabled": "false"}
        options = webdriver.ChromeOptions()
        options.add_argument("--lang={}".format(locale))
        options.add_experimental_option("prefs", preferences)
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.set_page_load_timeout(20)
        driver.maximize_window()
        return (driver)


class FireFoxBrowser():
    def run_browser(self, locale="en"):
        DIR = jsonGetter.GetJson.get_file(CONFIG, "DIR")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", locale)
        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.dir", DIR)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.helperApps.alwaysAsk.force", False)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp)
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
                driver = FireFoxBrowser().run_browser(LOCAL)
                return driver
            elif browsertype == BROWSERS.index("ChromeBrowser"):
                driver = ChromeBrowser().run_browser(LOCAL)
                return driver
            raise AssertionError("Browser not found")
        except AssertionError as _e:
            print(_e)


class RunBrowser(metaclass=Singleton):
    def __init__(self):
        actual_browser = jsonGetter.GetJson.get_file(CONFIG, "actualBrowser")
        if actual_browser in BROWSERS:
            browser_index = BROWSERS.index(actual_browser)
            self.driver = BrowserFactory.get_browser(browser_index)
        else:
            raise Exception("Такого браузера нет!")

