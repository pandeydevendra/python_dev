MySQL: Data Connectivity::::

database connectivity: 
import mysql.connector
mydb =mysql.connector.connect(host='localhost', user = 'root', password = '')
print(mydb.connection_id)

create database::
import mysql.connector
mydb =mysql.connector.connect(host='localhost', user = 'root', password = '')
cur=mydb.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS db1")

check it on MySQL>>
show databases;
