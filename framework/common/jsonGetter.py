import json

class GetJson:
    '''
    Use .get("element") to get element from .json
    '''
    @staticmethod
    def getFile(FilePath, getELEMENT):
        '''
        :return: element from config
        '''

        with open(FilePath, "rb") as config_file:
            data = json.load(config_file)
        ELEMENT = data[getELEMENT]
        return (ELEMENT)


