#!/usr/bin/env python3
#Program to log the gate events to database
import pymysql
from encryptor import Encryptor

class DatabaseHandler:
 
    def __init__(self):
        self._data = Encryptor.getData(Encryptor())
 
    def connect(self):
        try:
            self._conn = pymysql.Connect(self._data['databaseHost'],self._data['databaseUserName'],self._data['databasePassword'],self._data['databaseDatabase'])
            print('MySQL connection successfully established')
            return True
        except pymysql.Error as e:
            print(str(e))
            return False

    def disconnect(self):
        try:
            self._conn.close()
            return True
        except pymysql.Error as e:
            print(str(e))
            return False
        except AttributeError:
            print('Connection not established')
            return False

    def insertGatelog(self,book_id,book_name,alaram_time):
        self.connect()
        query = '''INSERT INTO gatelog (book_id,book_name,alaram_time) values('''+'\''+str(book_id)+'\''+',\''+str(book_name)+'\',\''+str(alaram_time)+'\');'
        print(query)
        cursor = self._conn.cursor()
        try:
            cursor.execute(query)
            self._conn.commit()
            print('Data successfully written')
        except:
            self._conn.rollback()
            print('Failed to write data')
        finally:
            self.disconnect()
