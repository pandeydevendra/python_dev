from dev_db import cursor, db

q_sql_update_table = "UPDATE book SET price = price + 10 WHERE price > 400"
cursor.execute(q_sql_update_table)
db.commit()
db.close()
