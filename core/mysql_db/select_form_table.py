"""
module used here: mysql-connector-python
"""
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='root@123', database='sql_db1')
# print(mydb.connection_id)
# cur = mydb.cursor()  # it will return in tuple
cur = mydb.cursor(dictionary=True)  # it will give dictionary
sql_query = "SELECT * FROM book"
cur.execute(sql_query)
books = cur.fetchall()
print(books)
print(type(books))

for book in books:
    # print(book, type(book))
    print("the price of {} is {}.".format(book['title'], book['price']))
