import pytest
from framework.Browser import *


@pytest.fixture(scope="function")
def get_driver(request):
    driver = RunBrowser().driver
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    RunBrowser.clear()
