from urllib.parse import urlparse
from framework.Base.BaseElement import *

BROWSER = jsonGetter.GetJson.getFile(CONFIG, "actualBrowser")
WaitTime = jsonGetter.GetJson.getFile(CONFIG, "WaitTime")


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

    def auth(self, SITE, login, password):
        logger.info("Trying to log in")
        site = urlparse(SITE)
        link = site.scheme + "://" + login + ":" + password + "@" + site.hostname + site.path
        return link

class Alert:
    def __init__(self):
        '''
        :param link: Link to get
        '''
        self.driver = RunBrowser().driver
        self.alert = self.driver.switch_to_alert()

    def getText(self):

        text = self.alert.text
        return text

    def accept(self):
        self.alert.accept()

    def cancel(self):
        self.alert.dismiss()

    def sendText(self, text):
        self.alert.send_keys(text)

class IFrame:
    def __init__(self):
        self.driver = RunBrowser().driver

    def switchFrame(self, id):
        self.driver.switch_to.frame(id)

    def switchDefault(self):
        self.driver.switch_to.default_content()