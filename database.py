import os
from flask_mysqldb import MySQL
import MySQLdb.cursors


class MyDatabase():

    def __init__(self, app):
        ''' Constructor which connects to the database'''
        self.app = app

        # Define the database connection string
        self.mysql = MySQL(self.app)

        # Configure MySQL using environment variables and Connect
        self.app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
        self.app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
        self.app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
        self.app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

    def connect(self):
        # Connect to the database -DictCursor will return a cursor
        # containing data as a python dictionary that can be
        # iterated over in application code
        self.cur = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    def query(self, sql):

        # Connect to database
        self.connect()

        # Execute query
        self.cur.execute(sql)

        # Return Results
        result = self.cur.fetchall()

        # Close the connection
        self.cur.close()

        return result
