"""
module used here: mysql-connector-python
"""
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='root@123', database='')
# print(mydb.connection_id)
cur = mydb.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS db_dev_test")