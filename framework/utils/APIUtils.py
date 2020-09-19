# from framework.Base.BaseElement import *
import requests

from framework.logger.logger import Logger

logger = Logger(__file__).get_log()


class API:
    def __init__(self, site):
        self.site = site

    def status(self, get):
        '''
        :return: request > request.status_code
        '''
        logger.info("Trying to get status code")
        req = requests.get(self.site + get)
        result = req
        return result

    def get_json(self, get):
        logger.info("Trying to get Json")
        req = requests.get(self.site + get)
        result = req.status_code
        try:
            json = req.json()
            return json
        except:
            return "NOT JSON!"

    def send_post(self, get, data):
        logger.info("Trying to send POST data to: " + str(self.site + get) + " With data: " + str(data))
        result = requests.post(self.site + get, data=data)
        logger.info("Got response: " + str(result) + "With data: " + str(result.text))
        return result
