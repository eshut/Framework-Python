"""Framework: https://github.com/eshut/Framework-Python"""

import json


class GetJson:
    '''
    Use .get("element") to get element from .json
    '''

    @staticmethod
    def get_file(file_path, get_element):
        '''
        :return: element from config
        '''

        with open(file_path, "rb") as config_file:
            data = json.load(config_file)
        element = data[get_element]
        return (element)
