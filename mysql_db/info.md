MySQL: Data Connectivity::::

database connectivity: 
import mysql.connector
mydb =mysql.connector.connect(host='localhost', user = 'root', password = '')
print(mydb.connection_id)

create database::
import mysql.connector
mydb =mysql.connector.connect(host='localhost', user = 'root', password = '')
cur=mydb.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS db1")

check it on MySQL>>
show databases;

import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='root@123', database='sql_db1')
# print(mydb.connection_id)
cur = mydb.cursor(dictionary=True)


# cur = mydb.cursor()

#SELECT OPERATION:
def get_book_id(b_title):
    sql_query = "SELECT * FROM book WHERE title = '{}'".format(b_title)
    print(sql_query)
    cur.execute(sql_query)
    book = cur.fetchone()
    print(book)
    if book:
        book_id = book["id"]
    else:
        book_id = 0
    return book_id

#INSERT OPERATION:
def insert(b_title, b_price):
    print(b_title, b_price)
    insert_in_book = "INSERT INTO book(title, price) VALUES(%s,%s)"
    book = (b_title, b_price)
    cur.execute(insert_in_book, book)
    mydb.commit()

#UPDATE OPERATION:
def update(b_id, updated_title, new_price):
    q_sql_update_table = "UPDATE book SET title = '{}', price = '{}' WHERE id = '{}'".format(
        updated_title, new_price, b_id
    )
    print(q_sql_update_table)
    cur.execute(q_sql_update_table)
    mydb.commit()



#DELETE OPERATION:
def delete(b_id):
    q_sql_del_table = "DELETE FROM book WHERE id = '{}'".format(b_id)
    print(q_sql_del_table)
    cur.execute(q_sql_del_table)
    mydb.commit()


#SELECT ALL OPERATION:
def select():
    sql_query = "SELECT * FROM book"
    cur.execute(sql_query)
    books = cur.fetchall()
    print(books)
    print(type(books))
    return books




def manage_book():
    action_ch = input("Which operation do you want; CRUD: ")
    action = action_ch.upper()
    if action == 'C':
        insert_process()
    elif action == 'R':
        select_process()
    elif action == 'U':
        update_process()
    elif action == 'D':
        delete_process()
    else:
        print('''Wrong input!! enter valid choice: ''')



mydb = mysql.connector.connect(host='localhost', user='root', password='root@123', database='sql_db1')
# print(mydb.connection_id)
cur = mydb.cursor(dictionary=True)














