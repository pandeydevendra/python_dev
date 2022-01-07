# database connectivity:
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@123',
    database='dev_db'
    )
# print(mydb.connection_id)
cursor = mydb.cursor()
# from dev_db import cursor, db

# Query:::
q = "INSERT INTO students(student_name, student_age, student_fee) VALUES(%s, %s, %s)"

# assign data:::::
new_student = ['Sunil', 28, 5000]
# cur.execute(q3, d1) #execute single data
cursor.execute(q, new_student)  # cur.executemany for many data but cur.execute for one(single) data
mydb.commit()