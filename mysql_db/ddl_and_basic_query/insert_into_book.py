"""
module used here: mysql-connector-python
"""
# database connectivity:
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='root@123', database='sql_db1')
# print(mydb.connection_id)
cur = mydb.cursor()


def insert_in_booktest():
    """
    no check for id as it not primary and is non-incrementable
    :return:
    """
    insert_in_booktest = "INSERT INTO book_test(id, title, price) VALUES(%s,%s,%s)"
    book_test = (1, 'Python3', 345)
    cur.execute(insert_in_booktest, book_test)
    mydb.commit()


def insert_in_book():
    """
    id is primary key an auto incrementable entity, can't be duplicated
    :return:
    """
    insert_in_book = "INSERT INTO book(title, price) VALUES(%s,%s)"
    book = ('Math', 500)
    cur.execute(insert_in_book, book)
    mydb.commit()


# insert_in_booktest()
insert_in_book()
