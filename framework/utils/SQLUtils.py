import mysql.connector
# from framework.Base.BaseElement import *
from framework.logger.logger import Logger

logger = Logger(__file__).getlog()

class SQL:
    def __init__(self, host, user, passwd, database):
        self.db = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

    def cursor(self):
        result = self.db.cursor()
        return result

    def runscript(self, cursor, script):
        cursor.execute(script)
        x = [x for x in cursor]
        return x

    def closeConnect(self):
        self.db.cursor().close()
