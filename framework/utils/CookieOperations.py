from framework.Base.BaseElement import *


class Cookie():
    def __init__(self):
        self.driver = RunBrowser().driver

    def add_cookie(self, cookies):
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def delete_cookie(self, cookies):
        for cookie in cookies:
            self.driver.delete_cookie(cookie)

    def edit_cookie(self, cookie, param):
        x = {"name": cookie, "value": param}
        self.driver.add_cookie(x)

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    def get_cookies(self):
        cookies = self.driver.get_cookies()
        return cookies

    def get_cookie(self, name):
        cookie = self.driver.get_cookie(name)
        return cookie

    def split_cookie(self, site_cookies):
        result = []
        for cookie in site_cookies:
            x = cookie.get("name")
            y = cookie.get("value")
            z = {'name': x, 'value': y}
            result.insert(0, z)
        return result
