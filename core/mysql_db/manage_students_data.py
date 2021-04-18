import mysql.connector as msconn

studentdb = msconn.connect(
    host='localhost',
    user='root',
    password='root@123'
)

cur = studentdb.cursor()
# Query:::
q1 = "CREATE DATABASE IF NOT EXISTS students_data"
cur.execute(q1)
