from dev_db import cursor, db

# q_sql_del_table = "DELETE FROM book WHERE title = 'Java'"
q_sql_del_table = "DELETE FROM book WHERE title = 'Java' OR price = 400"
cursor.execute(q_sql_del_table)
db.commit()
db.close()
