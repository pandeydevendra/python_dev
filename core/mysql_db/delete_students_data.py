import mysql.connector as msconn

studentdb = msconn.connect(
    host='localhost',
    user='root',
    password='root@123',
    database='students_data'
)

cur = studentdb.cursor()
# Query:::
q_delete = "DELETE FROM student WHERE student_id = 1"

# assign data:
# d1 = (1, 'Ranjendra Prasad', 25, 1000)  # single data

# assign mutliple data:::::
# students-data_list = [()()()()]
cur.execute(q_delete)
studentdb.commit()
