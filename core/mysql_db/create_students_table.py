import mysql.connector as msconn

studentdb = msconn.connect(
    host='localhost',
    user='root',
    password='root@123',
    database='students_data'
)

cur = studentdb.cursor()
# Query:::
q2 = "CREATE TABLE IF NOT EXISTS student(" \
     "student_id int(4)," \
     "student_name varchar(32)," \
     "student_age int(2)," \
     "student_fee float(6,2)" \
     ")"
cur.execute(q2)
