from framework.common import jsonGetter
from pytest_testrail.plugin import pytestrail
from framework.utils import BrowserActions, SystemActions
import pytest
import time

from framework.logger.logger import Logger
logger = Logger(__file__).getlog()

CONFIG = 'resources/config.json'
TESTDATA = 'resources/testdata.json'

SITE = jsonGetter.GetJson.getFile(CONFIG, "SITE")




@pytest.mark.usefixtures("get_driver")
class TestSuite1:
    #@pytest.mark.parametrize("login, password, token", testdata1)
    #@pytestrail.case('C19380774')
    def test_1(self):
        pass









