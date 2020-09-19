import glob
import json
import os
from datetime import datetime

from testrail_api import TestRailAPI

from framework.common import jsonGetter

DATA = "resources/testrail.json"
CREDITALS = jsonGetter.GetJson.get_file(DATA, "creditals")
HOST = CREDITALS.get("host")
LOGIN = CREDITALS.get("login")
PASSWORD = CREDITALS.get("pass")

DEFAULT_TEST_NAME = "Automated run at: " + str(datetime.now())


class TR:
    def __init__(self):
        self.api = TestRailAPI(HOST, LOGIN, PASSWORD)
        self.temp_status_path = "TESTRAIL/TEMP/status.txt"
        self.case_id = "case_id"
        self.data_str = "data"
        self.id_str = "id"

    def add_run(self, project_id, test_name=DEFAULT_TEST_NAME):
        my_test_run = self.api.runs.add_run(
            project_id,
            name=test_name,
            include_all=True,
        )
        return my_test_run

    def add_test_results(self, my_test_run, case_id, comment):
        f = open(self.temp_status_path, "r")
        status = f.read()
        f.close()

        result = self.api.results.add_result_for_case(
            run_id=my_test_run[self.id_str],
            case_id=case_id,
            status_id=status,  # 5 - fail, 1 - passed
            comment=comment,
            version="1"
        )
        return result

    def add_image_to_result(self, result, image):
        attach = image
        self.api.attachments.add_attachment_to_result(result[self.id_str], attach)

    def read_log(self, log_path, count=10):
        list_of_files = glob.glob(log_path)
        latest_file = max(list_of_files, key=os.path.getctime)
        f = open(latest_file, "r")
        x = f.readlines()[-count:]
        log = ""
        for elem in x:
            log += elem
        f.close()
        return log

    def set_status(self, status="5"):
        f = open(self.temp_status_path, "w")
        f.write(status)
        f.close()

    def set_case(self, case_id):
        with open(DATA, 'r+') as f:
            config = json.load(f)
            data = config[self.data_str]
            data[self.case_id] = case_id

            f.seek(0)
            json.dump(config, f, indent=4)
            f.truncate()
