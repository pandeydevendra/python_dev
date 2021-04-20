from dev_db import cursor, db

# Query:::
q2 = "CREATE TABLE IF NOT EXISTS student(" \
     "student_id int(4)," \
     "student_name varchar(32)," \
     "student_age int(2)," \
     "student_fee float(6,2)" \
     ")"
cursor.execute(q2)
