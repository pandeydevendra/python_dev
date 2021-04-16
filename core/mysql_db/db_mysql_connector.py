# database connectivity:
import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', password='root@123', database='sql_db1')
#print(mydb.connection_id)
cur=mydb.cursor()
s = "INSERT INTO book(book_id, title, price) VALUE(%s,%s,%s)"
b1 = (1, 'Python3', 345)
cur.execute(s, b1)
