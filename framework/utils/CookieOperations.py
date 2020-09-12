from framework.Base.BaseElement import *


class Cookie():
    def __init__(self):
        self.driver = RunBrowser().driver

    def addCookie(self, cookies):
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def deleteCookie(self, cookies):
        for cookie in cookies:
            self.driver.delete_cookie(cookie)

    def editCookie(self, cookie, param):
        x = {"name": cookie, "value": param}
        self.driver.add_cookie(x)

    def deleteAllCookies(self):
        self.driver.delete_all_cookies()

    def getCookies(self):
        cookies = self.driver.get_cookies()
        return cookies

    def getCookie(self, name):
        cookie = self.driver.get_cookie(name)
        return cookie

    def splitCookie(self, siteCookies):
        result = []
        for cookie in siteCookies:
            x = cookie.get("name")
            y = cookie.get("value")
            z = {'name': x, 'value': y}
            result.insert(0, z)
        return result
