import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='root@123', database='sql_db1')
# print(mydb.connection_id)
cur = mydb.cursor()

q_sql_update_table = "UPDATE book SET price = price + 10 WHERE price > 400"
cur.execute(q_sql_update_table)
mydb.commit()
