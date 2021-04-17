"""
module used here: mysql-connector-python
"""

import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='root@123', database='sql_db1')
# print(mydb.connection_id)
cur = mydb.cursor()

# execute SQL query using execute() method.
cur.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cur.fetchone()

print("Database version : %s " % data)