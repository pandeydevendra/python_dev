from dev_db import cursor, db

# Query:::
q_delete = "DELETE FROM student WHERE student_id = 1"

# assign data:
# d1 = (1, 'Ranjendra Prasad', 25, 1000)  # single data

# assign mutliple data:::::
# students-data_list = [()()()()]
cursor.execute(q_delete)
db.commit()
db.close()