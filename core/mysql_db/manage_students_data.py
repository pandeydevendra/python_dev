from dev_db import cursor, db

# Query:::
q1 = "SELECT * FROM student"
cursor.execute(q1)
db_data = cursor.fetchall()
print(db_data)