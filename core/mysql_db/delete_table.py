import mysql.connector as msql_conn

mydb = msql_conn.connect(host='localhost', user='root', password='root@123', database='sql_db1')
# print(mydb.connection_id)
cur = mydb.cursor()

#q_sql_del_table = "DELETE FROM book WHERE title = 'Java'"
q_sql_del_table = "DELETE FROM book WHERE title = 'Java' OR price = 400"
cur.execute(q_sql_del_table)
mydb.commit()
