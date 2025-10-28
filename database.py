import os
from flask_mysqldb import MySQL
import MySQLdb.cursors


class Database():

    def __init__(self, app):
        self.app = app

        self.mysql = MySQL(self.app)

        self.app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
        self.app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
        self.app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
        self.app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

        def connect(self):
            self.cur = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        def query(self, sql):
            self.connect()

            self.cur.execute(sql)

            result = self.cur.fetchall()

            self.cur.close()

            return result
