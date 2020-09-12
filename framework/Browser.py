from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from framework.common import jsonGetter


CONFIG = 'resources/config.json'
BROWSERS = ["ChromeBrowser", "FireFoxBrowser"]
LOCAL = jsonGetter.GetJson.getFile(CONFIG, "LOCAL")

class ChromeBrowser():
    def runBrowser(self, locale="en"):
        DIR = jsonGetter.GetJson.getFile(CONFIG, "DIR")
        preferences = {"download.default_directory": DIR, "safebrowsing.enabled": "false"}
        options = webdriver.ChromeOptions()
        options.add_argument("--lang={}".format(locale))
        options.add_experimental_option("prefs", preferences)
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.set_page_load_timeout(20)
        driver.maximize_window()
        return (driver)


class FireFoxBrowser():
    def runBrowser(self, locale="en"):
        DIR = jsonGetter.GetJson.getConfig("DIR")
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
    def getBrowser(browsertype):

        try:
            if browsertype == BROWSERS.index("FireFoxBrowser"):
                driver = FireFoxBrowser().runBrowser(LOCAL)
                # driver.set_window_size(get.resolutionH, get.resolutionW)
                # driver.maximize_window()
                return driver
            elif browsertype == BROWSERS.index("ChromeBrowser"):
                driver = ChromeBrowser().runBrowser(LOCAL)
                # driver.set_window_size(get.resolutionH, get.resolutionW)
                # driver.maximize_window()

                return driver
            raise AssertionError("Browser not found")
        except AssertionError as _e:
            print(_e)


class RunBrowser(metaclass=Singleton):
    def __init__(self, actualBrowser="ChromeBrowser"):
        actualBrowser = jsonGetter.GetJson.getFile(CONFIG ,"actualBrowser")
        if actualBrowser in BROWSERS:
            BROWSERindex = BROWSERS.index(actualBrowser)
            self.driver = BrowserFactory.getBrowser(BROWSERindex)
        else:
            raise Exception("Такого браузера нет!")

