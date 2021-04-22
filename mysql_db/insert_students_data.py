from dev_db import cursor, db

# Query:::
q3 = "INSERT INTO student(student_name, student_age, student_fee) VALUES(%s, %s, %s)"
# one can omit student_id after altering it with [PK(primary key), NN(not null) and AI(auto-increment)]
# assign data:
# d1 = ('H. C. Verma', 22, 1500)  # single data

# assign mutliple data:::::
students_data_list = [('Ramanujan', 20, 000), ('Lavosier', 26, 220), ('Newton', 25, 110)]
# cur.execute(q3, d1) #execute single data
cursor.executemany(q3, students_data_list)  # cur.executemany for many data
db.commit()
db.close()
