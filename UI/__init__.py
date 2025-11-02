import mysql.connector

class user:
    def __init__(self):
        self._cnx = mysql.connector.connect(user='root', password='',host='localhost',
                                            database='autonoleggio')