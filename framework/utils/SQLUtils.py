"""Framework: https://github.com/eshut/Framework-Python"""

import mysql.connector
from framework.logger.logger import Logger


class SQL(Logger):
    def __init__(self, host, user, passwd, database, port, logger=__file__):
        super().__init__(logger)
        self.db = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database, port=port)

    def cursor(self):
        result = self.db.cursor()
        return result

    def run_script(self, cursor, script, args=None):
        cursor.execute(script, args)
        x = [x for x in cursor]
        return x

    def close_connect(self):
        self.db.cursor().close()

    def commit(self):
        self.db.commit()
