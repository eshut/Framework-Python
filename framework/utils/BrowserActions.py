from urllib.parse import urlparse

from framework.Base.BaseElement import *

BROWSER = jsonGetter.GetJson.get_file(CONFIG, "actualBrowser")



class LinkOperations:
    def __init__(self, link=""):
        '''
        :param link: Link to get
        '''
        self.driver = RunBrowser().driver
        self.link = link

    def get(self):
        '''
        Follow to link
        '''
        self.driver.get(self.link)

    def auth(self, login, password):
        logger.info("Trying to log in")
        site = urlparse(self.link)
        link = site.scheme + "://" + login + ":" + password + "@" + site.netloc + site.path
        return link


class Alert:
    def __init__(self):
        '''
        :param link: Link to get
        '''
        self.driver = RunBrowser().driver
        self.alert = self.driver.switch_to_alert()

    def get_text(self):
        text = self.alert.text
        return text

    def accept(self):
        self.alert.accept()

    def cancel(self):
        self.alert.dismiss()

    def send_text(self, text):
        self.alert.send_keys(text)


class IFrame:
    def __init__(self):
        self.driver = RunBrowser().driver

    def switch_frame(self, id):
        self.driver.switch_to.frame(id)

    def switch_default(self):
        self.driver.switch_to.default_content()


class Browser:
    def back(self):
        RunBrowser().driver.back()

    def refresh(self):
        RunBrowser().driver.refresh()


class JavaScript:
    def exec(self, script):
        RunBrowser().driver.execute_script(script)
