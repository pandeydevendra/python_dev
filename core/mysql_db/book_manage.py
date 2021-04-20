from dev_db import cursor, db

cur = cursor
mydb = db


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


def insert(b_title, b_price):
    print(b_title, b_price)
    insert_in_book = "INSERT INTO book(title, price) VALUES(%s,%s)"
    book = (b_title, b_price)
    cur.execute(insert_in_book, book)
    mydb.commit()


def update(b_id, updated_title, new_price):
    q_sql_update_table = "UPDATE book SET title = '{}', price = '{}' WHERE id = '{}'".format(
        updated_title, new_price, b_id
    )
    print(q_sql_update_table)
    cur.execute(q_sql_update_table)
    mydb.commit()


def delete(b_id):
    q_sql_del_table = "DELETE FROM book WHERE id = '{}'".format(b_id)
    print(q_sql_del_table)
    cur.execute(q_sql_del_table)
    mydb.commit()


def select():
    sql_query = "SELECT * FROM book"
    cur.execute(sql_query)
    books = cur.fetchall()
    print(books)
    print(type(books))
    return books


def insert_process():
    book_title = input("Enter title of the book: ")
    book_price = float(input("Enter the book's price: "))
    insert(book_title.title(), book_price)


def select_process():
    books = select()
    for book in books:
        # print(book, type(book))
        print("the price of {} is {}.".format(book['title'], book['price']))


def update_process():
    current_title = input("Enter the book's current title: ")
    book_id = get_book_id(current_title)
    if book_id == 0:
        print("Book titled {} doesn't exist.".format(current_title))
    else:
        updated_title = input("Enter the book's updated  title: ")
        updated_price = float(input("Enter new price: "))
        update(book_id, updated_title, updated_price)


def delete_process():
    book_title = input("Enter the book's title to be deleted: ")
    book_id = get_book_id(book_title)
    if book_id == 0:
        print("Book titled {} doesn't exist.".format(book_title))
    else:
        ch = input("Are you sure you want to delete {} book?y/n: ".format(book_title))
        if ch.lower() == 'y':
            delete(book_id)
        else:
            print("Thank you! Your book is safe in our record.")


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


keep_on = True
while keep_on is True:
    ch_input = input("Do you want to continue? y/n: ")
    ch = ch_input.lower()
    if ch == 'y':
        manage_book()
    elif ch == 'n':
        keep_on = False
        print("program end")
    else:
        print('''Wrong input!! enter valid choice: ''')
