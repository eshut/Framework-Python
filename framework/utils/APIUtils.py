#from framework.Base.BaseElement import *
import requests
from framework.logger.logger import Logger
from framework.common import jsonGetter


logger = Logger(__file__).getlog()

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

    def getJson(self, get):
        logger.info("Trying to get Json")
        req = requests.get(self.site + get)
        result = req.status_code
        try:
            json = req.json()
            return json
        except:
            return "NOT JSON!"

    def SendPOST(self, get, data):
        logger.info("Trying to send POST data")
        result = requests.post(self.site + get, data=data)
        return result







