"""
module used here: mysql-connector-python
"""
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='root@123', database='sql_db1')
# print(mydb.connection_id)
cur = mydb.cursor()
#this is for testing purpose only, we will create table using mysql directly.

create_table_query ="CREATE TABLE IF NOT EXISTS book_test(id int(4), title varchar(20), price float(5, 2))"
cur.execute(create_table_query)
